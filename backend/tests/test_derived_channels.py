"""
Tests for derived_channels.py — the formula compiler/evaluator behind
configs/derived_channels.json.

Run with pytest, or directly:  py backend/tests/test_derived_channels.py
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bridge.derived_channels import evaluate, load_specs, resolve


def _write_config(tmp_path: Path, entries: list[dict]) -> Path:
    path = tmp_path / "derived_channels.json"
    path.write_text(json.dumps(entries))
    return path


def test_compiles_arithmetic_formula(tmp_path):
    path = _write_config(
        tmp_path,
        [{"metric_key": "CPU0_Tctl_F", "formula": "$CPU0_Tctl * 1.8 + 32"}],
    )
    specs = load_specs(path)
    assert len(specs) == 1
    assert specs[0].refs == ["CPU0_Tctl"]
    assert evaluate(specs[0], {"CPU0_Tctl": 64.25}) == 64.25 * 1.8 + 32


def test_missing_reference_is_zero_not_an_error(tmp_path):
    path = _write_config(
        tmp_path, [{"metric_key": "K", "formula": "$Missing + 1"}]
    )
    specs = load_specs(path)
    assert evaluate(specs[0], {}) == 1.0


def test_comparison_and_conditional_formula(tmp_path):
    path = _write_config(
        tmp_path,
        [{"metric_key": "K", "formula": "1.0 if $Temp > 80 else 0.0"}],
    )
    specs = load_specs(path)
    assert evaluate(specs[0], {"Temp": 90}) == 1.0
    assert evaluate(specs[0], {"Temp": 10}) == 0.0


def test_divide_by_zero_yields_zero_not_a_crash(tmp_path):
    path = _write_config(
        tmp_path, [{"metric_key": "K", "formula": "1 / $Zero"}]
    )
    specs = load_specs(path)
    assert evaluate(specs[0], {"Zero": 0}) == 0.0


def test_disallowed_constructs_are_rejected_at_load(tmp_path):
    dangerous = [
        "__import__('os').system('echo hi')",
        "$A.bit_length()",
        "[x for x in range(3)]",
        "(lambda: 1)()",
    ]
    for formula in dangerous:
        path = _write_config(tmp_path, [{"metric_key": "K", "formula": formula}])
        specs = load_specs(path)
        assert specs == [], f"formula should have been rejected: {formula!r}"


def test_missing_file_yields_no_specs(tmp_path):
    assert load_specs(tmp_path / "does-not-exist.json") == []


def test_resolve_skips_channel_with_missing_reference(tmp_path):
    path = _write_config(
        tmp_path,
        [{"metric_key": "K", "formula": "$NotPresent + 1", "units": "x"}],
    )
    specs = load_specs(path)
    resolved = resolve(specs, available_keys={"SomethingElse"}, frequency=2)
    assert resolved == []


def test_resolve_builds_channel_def_for_available_reference(tmp_path):
    path = _write_config(
        tmp_path,
        [
            {
                "metric_key": "CPU0_Tctl_F",
                "formula": "$CPU0_Tctl * 1.8 + 32",
                "units": "F",
                "min_value": 32,
                "max_value": 250,
            }
        ],
    )
    specs = load_specs(path)
    resolved = resolve(specs, available_keys={"CPU0_Tctl"}, frequency=4)
    assert len(resolved) == 1
    channel, spec = resolved[0]
    assert channel.metric_key == "CPU0_Tctl_F"
    assert channel.is_derived is True
    assert channel.units == "F"
    assert channel.frequency == 4
    assert spec.formula == "$CPU0_Tctl * 1.8 + 32"


def test_resolve_allows_chaining_onto_an_earlier_derived_channel(tmp_path):
    path = _write_config(
        tmp_path,
        [
            {"metric_key": "A_Plus_One", "formula": "$A + 1"},
            {"metric_key": "A_Plus_Two", "formula": "$A_Plus_One + 1"},
        ],
    )
    specs = load_specs(path)
    resolved = resolve(specs, available_keys={"A"}, frequency=2)
    assert [c.metric_key for c, _s in resolved] == ["A_Plus_One", "A_Plus_Two"]


def test_malformed_entry_is_skipped_not_fatal(tmp_path):
    path = _write_config(
        tmp_path,
        [
            {"metric_key": "Bad", "formula": "$A +"},
            {"metric_key": "Good", "formula": "$A + 1"},
        ],
    )
    specs = load_specs(path)
    assert [s.metric_key for s in specs] == ["Good"]


if __name__ == "__main__":
    import tempfile

    failures = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_") or not callable(fn):
            continue
        with tempfile.TemporaryDirectory() as td:
            try:
                fn(Path(td))
                print(f"PASS  {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL  {name}: {e}")
            except Exception as e:
                failures += 1
                print(f"ERROR {name}: {e!r}")
    print(f"\n{'FAILED' if failures else 'OK'} ({failures} failure(s))")
    sys.exit(1 if failures else 0)
