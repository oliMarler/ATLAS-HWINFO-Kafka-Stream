"""
Derived channels — additional ATLAS parameters computed from other channels'
already-sampled values, rather than read from HWiNFO.

Defined declaratively in ``configs/derived_channels.json`` so a new calculation
can be added without touching Python: each entry is a formula string that
references other channels with a ``$Name`` token, e.g.::

    {
      "metric_key": "CPU0_Tctl_F",
      "formula": "$CPU0_CPUTctlTdie * 1.8 + 32",
      "units": "F",
      "description": "CPU Tctl/Tdie in Fahrenheit",
      "min_value": 32,
      "max_value": 250,
      "format_string": "%5.1f"
    }

This is inspired by ATLAS's own FDL function syntax (arithmetic, relational
and boolean operators, ``$Parameter`` references —
https://atlas.motionapplied.com/key-functionality/analyse/viewer/functions/function-editor/)
but is *not* FDL: only the single-expression subset applies here, since a
derived channel is one scalar computed per sample, not a multi-statement
function with loops. Formulas are parsed as Python expressions (after
substituting ``$Name`` for ``Name``), so operators follow Python spelling —
``**`` for power, ``and``/``or``/``not`` for boolean logic, ``a if c else b``
for a conditional — not FDL's own grammar.

Formulas are compiled once at session start and walked against an AST
whitelist that excludes calls, attribute access, subscripting, comprehensions
and lambdas, so a formula can only combine numbers and referenced channel
values with operators. That whitelist is what makes it safe to ``eval()`` the
compiled expression per sample tick without sandboxing beyond it.
"""
import ast
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from types import CodeType

from bridge.channel_registry import ATLAS_APP, ChannelDef

logger = logging.getLogger(__name__)

DEFAULT_PATH = Path(__file__).resolve().parents[2] / "configs" / "derived_channels.json"

_REF_RE = re.compile(r"\$([A-Za-z_][A-Za-z0-9_]*)")

# Deliberately excludes ast.Call, ast.Attribute, ast.Subscript, ast.Lambda and
# every comprehension/statement node — a formula is arithmetic over numbers
# and $-references, nothing that can call out or access anything else.
_ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
    ast.UnaryOp, ast.USub, ast.UAdd, ast.Not,
    ast.BoolOp, ast.And, ast.Or,
    ast.Compare, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Eq, ast.NotEq,
    ast.IfExp,
    ast.Name, ast.Load,
    ast.Constant,
)


class FormulaError(ValueError):
    pass


@dataclass
class DerivedSpec:
    metric_key: str
    formula: str
    refs: list[str]
    code: CodeType
    units: str
    description: str
    format_string: str
    min_value: float
    max_value: float


def _compile_formula(formula: str) -> tuple[CodeType, list[str]]:
    """Turn a ``$Name``-referencing formula into a compiled expression plus its refs."""
    refs = sorted(set(_REF_RE.findall(formula)))
    python_expr = _REF_RE.sub(lambda m: m.group(1), formula)
    try:
        tree = ast.parse(python_expr, mode="eval")
    except SyntaxError as e:
        raise FormulaError(f"{formula!r}: invalid syntax ({e})") from e

    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED_NODES):
            raise FormulaError(
                f"{formula!r}: {type(node).__name__} is not allowed here "
                "(only arithmetic, comparison, boolean and if/else expressions)"
            )
        if isinstance(node, ast.Name) and node.id not in refs:
            raise FormulaError(f"{formula!r}: {node.id!r} is not a $-reference")

    return compile(tree, filename=f"<derived:{formula}>", mode="eval"), refs


def load_specs(path: Path = DEFAULT_PATH) -> list[DerivedSpec]:
    """Load and compile every entry in the derived-channels config.

    A malformed entry is logged and skipped rather than failing the whole
    bridge start — one typo in a formula shouldn't take down real channels.
    """
    if not path.exists():
        return []

    raw = json.loads(path.read_text())
    specs: list[DerivedSpec] = []
    for entry in raw:
        metric_key = entry.get("metric_key", "?")
        try:
            code, refs = _compile_formula(entry["formula"])
        except (FormulaError, KeyError) as e:
            logger.error("Skipping derived channel %r: %s", metric_key, e)
            continue

        specs.append(
            DerivedSpec(
                metric_key=metric_key,
                formula=entry["formula"],
                refs=refs,
                code=code,
                units=entry.get("units", ""),
                description=entry.get("description", metric_key),
                format_string=entry.get("format_string", "%8.2f"),
                min_value=float(entry.get("min_value", 0.0)),
                max_value=float(entry.get("max_value", 10000.0)),
            )
        )
    return specs


def resolve(
    specs: list[DerivedSpec], available_keys: set[str], frequency: int
) -> list[tuple[ChannelDef, DerivedSpec]]:
    """Build ChannelDefs for specs whose references are all available.

    A derived channel silently drops if a reference doesn't exist on this
    machine (e.g. no CPU temp sensor) — same behaviour as the built-in preset
    predicates in channel_registry.py when a category is empty. Specs are
    resolved in file order and each resolved key is added to the known set
    before the next spec is checked, so a later formula can reference an
    earlier derived channel.
    """
    known = set(available_keys)
    resolved: list[tuple[ChannelDef, DerivedSpec]] = []

    for spec in specs:
        missing = [r for r in spec.refs if r not in known]
        if missing:
            logger.warning(
                "Derived channel %r skipped: missing reference(s) %s",
                spec.metric_key, missing,
            )
            continue

        channel = ChannelDef(
            metric_key=spec.metric_key,
            atlas_identifier=f"{spec.metric_key}:{ATLAS_APP}",
            atlas_name=spec.metric_key,
            atlas_app=ATLAS_APP,
            units=spec.units,
            description=spec.description,
            format_string=spec.format_string,
            min_value=spec.min_value,
            max_value=spec.max_value,
            frequency=frequency,
            group="Derived",
            is_derived=True,
        )
        resolved.append((channel, spec))
        known.add(spec.metric_key)

    return resolved


def evaluate(spec: DerivedSpec, values: dict[str, float]) -> float:
    """Evaluate one compiled formula against this tick's sampled values.

    Never raises — a bad input (e.g. divide-by-zero from a sensor reading
    0) yields 0.0 rather than breaking the sampling loop.
    """
    try:
        inputs = {ref: values.get(ref, 0.0) for ref in spec.refs}
        return float(eval(spec.code, {"__builtins__": {}}, inputs))
    except Exception as e:
        logger.debug("Derived channel %r failed to evaluate: %s", spec.metric_key, e)
        return 0.0
