# Race engineering in professional endurance / sportscar racing

Coverage note: web search returned thin material on current-era IMSA/WEC engineer practice. Most of the concrete, quotable radio guidance found is from F1 (Mercedes, Lotus) and Porsche LMP1 (2010s). Items marked [F1], [LMP1], [1990s] are not current-era endurance. Nothing here is invented; where I generalise it is under Inferences.

## What does the race engineer do before the weekend, in practice and qualifying, and during the race?

### Takeaway
Sources agree the role is technical knowledge plus planning plus communication, and that the endurance version adds length, sustained focus and real-time fuel/tyre/strategy decisions. Detailed current-era weekend-by-weekend breakdowns were not found in primary sources.

### Cited Findings
- Leena Gade (Ford Racing WEC hire, ex-Audi Le Mans winner) describes the job as "technical expertise, strategic foresight, and clear communication", needing to understand "every nuance of the car", and notes six-to-24-hour races demand "meticulous preparation and unwavering focus"; she cites "split-second decisions in the garage" on strategy, fuel and tyres. (Ford corporate feature, 2026; promotional in tone) — [Ford From the Road](https://www.fromtheroad.ford.com/us/en/articles/2026/leena-gade-ford-racing-wec)
- Race engineer acts as translator between driver and mechanics (driver requests become changes made at stops). [F1 example] — summarised from search result: [FlowRacers](https://flowracers.com/blog/what-do-f1-race-engineers-do)
- Porsche Penske staffing: Brandon Fry (ex-BMW M Team RLL technical director) joined as lead race engineer for the IMSA programme in 2024, supporting the two car race engineers; Raul Prados engineered Josef Newgarden and the No. 6 Porsche at Detroit. Shows IMSA GTP teams layer a lead engineer over per-car engineers. — [Sportscar365 Fry](https://sportscar365.com/imsa/iwsc/fry-joins-porsche-penske-in-team-engineering-expansion/), [Sportscar365 Detroit notebook](https://sportscar365.com/imsa/iwsc/detroit-friday-notebook-9/) (from search snippets, pages not fully read)
- Division of labour: assistant engineers take on monitoring so the race engineer can focus on the driver. [F1, Jordan-era] — [Crash.net](https://www.crash.net/f1/news/38397/1/jordan-adds-to-engineering-strength-at-races)
- Le Mans pitwall engineer, 1990s Peugeot (Tim Wright, 4 Le Mans races): worked out fuel consumption from the driver's reported figure each lap, recorded lap times, adjusted strategy; no backup or data engineer existed, so he prepared to stay awake "at least 36 hours"; headsets "clamped to your head for the best part of 25 hours". [1990s, foundational only] — [Autosport](https://www.autosport.com/le-mans/news/how-an-engineer-survives-le-mans/10485835/)
- Ferrari describes each Le Mans car having an engineer who monitors parameters, stays in radio contact and keeps drivers calm and focused, working the full day without a break (snippet only; page content did not load) — [Ferrari magazine](https://www.ferrari.com/en-CA/magazine/articles/ferrari-car-engineers-at-le-mans)
- Goodyear tyre engineers analyse returned tyres to set optimal stint length for track conditions; LMP2 driver Gabriel Aubry calls it a "triangulation between driver, team engineer and Goodyear". (snippet) — [Goodyear Europe](https://news.goodyear.eu/goodyear-at-le-mans-the-insight-into-a-driver-tire-engineer-relationship/)

### Inferences
- Modern GTP crews likely split: car/race engineer (driver voice), performance/data engineers, strategist, tyre engineer. Supported only by the Penske staffing items and F1 analogy; no source describes the exact split.
- For a sim assistant, the "before weekend" work reduces to: know the car's limits (fuel/energy per lap, tyre windows) and bring a plan.

### Gaps
- No primary current-era interview detailing practice/qualifying programmes (run plans, tyre-allocation, setup change loops) in IMSA/WEC was found.
- Racecar Engineering coverage was not reachable via search.

## What data does the engineer watch live, and what triggers a call?

### Takeaway
Live telemetry plus driver feedback is the core. Tyre temperature/pressure is cited as the primary stint-performance input in LMP2; GTP adds virtual energy as a hard-limited resource. Specific trigger thresholds were not found in sources.

### Cited Findings
- LMP2 context: engineer follows the radio and reads car behaviour from live telemetry; tyre temperature and pressure combined with driver feedback are the main performance inputs — Goodyear piece above and [PMW Magazine](https://pmw-magazine.com/news/team-news/goodyear-reveals-how-driver-tire-engineer-relationship-enhances-performance.html)
- GTP "virtual energy" is the combined fuel + electrical energy usable over a stint. A secondary source states IMSA GTP combined output cap 500 kW and a stint energy allowance of 255.6 kWh, subject to BoP, with a 100-second stop-and-go for a first overuse. SINGLE-SOURCE, from a search summary of unclear origin (sim/press); verify against IMSA technical regs before use — [Traxion (sim hybrid opinion)](https://traxion.gg/opinion-why-iracings-hybrid-system-still-needs-some-work/) and [RaceControl](https://racecontrol.gg/?p=762) were the result links; I could not attribute the figures to one of them.
- In Le Mans Ultimate the Fuel Ratio setting determines the battery vs fuel share of the virtual-energy budget (sim guide, snippet only).
- Mercedes' Shovlin: engineers must tell drivers about energy-recovery charge levels and fuel management because they change car balance [F1] (snippet) — [Autosport/F1 radio feature](https://www.autosport.com/f1/news/the-secrets-of-in-race-radio-chat-5102490/5102490/)
- Lotus' Permane: give tyre-stop windows and targets (e.g. "target minus three") so the driver knows when to conserve or push [F1] — same Autosport feature.
- Driver fatigue: sunrise period is widely cited as when fatigue mistakes rise (Le Mans organisers' driver features, snippet) — [24h-lemans.com](https://24h-lemans.com/en/news/24-hours-of-le-mans-how-do-drivers-cope-with-tiredness-52122)

### Inferences
- Triggers for calls plausibly are: energy/fuel delta vs target, tyre temp/pressure out of window, stint-time/box window, traffic/class approaching, gap changes. These are my synthesis, not sourced trigger lists.

### Gaps
- No source listing brake temps, damper/ride-height, or lap-time-consistency triggers in endurance. No current-era GTP virtual-energy target-management quotes found.

## How is radio communication structured (what, how short, tone, never during...), real examples, handling stress/fatigue?

### Takeaway
Best-sourced guidance: be minimal, make the driver able to act, time calls to straights, state positive actions, require a readback, stay calm. Real endurance transcripts were not found; the one structured example is Porsche LMP1.

### Cited Findings
- Porsche 919 (LMP1, Monza test) engineer Mathieu Galoche to Timo Bernhard: "Alpha position four, Timo, alpha four," driver replies "Alpha four copy, alpha four copy!" and sets the wheel switch. Instructions say the action to take not the one to avoid: "Stay out" rather than "no pit stop", so a partly heard negative cannot be misread. "Copy" used for confirmation as clearer than "yes". Pit call: "Pit Timo, pit now!" — "Copy!" [LMP1] — [Porsche Newsroom](http://newsroom.porsche.com/en/motorsports/tests-in-monza-10499.html)
- Andreas Seidl (Porsche LMP1 team leader): "What we're trying to do is pack as much information as possible into just a few words" and "Information has got to keep flowing even when things get hectic"; he consulted a German Air Force fighter pilot on radio discipline. [LMP1] — same Porsche page.
- Shovlin (Mercedes) [F1]: avoid the braking zone; drivers "don't really mind" talk on straights but corner talk can make them miss a braking point; in qualifying give all information before the final sector, then leave them alone; give info when the driver can act on it (e.g. tyre temps mid out-lap); reminders are cheap and let drivers react to commands; encouragement suits some drivers and backfires on others; avoid "telling them the obvious"; "The engineer's job is to calm them down and not to panic themselves." — [Autosport](https://www.autosport.com/f1/news/the-secrets-of-in-race-radio-chat-5102490/5102490/) (fetch summarised by tool; quotes as returned)
- Permane (Lotus) [F1]: assume talking costs the driver time; give "what they need and nothing more than that"; Räikkönen wanted little, Villeneuve every lap; non-urgent changes (e.g. fuel mixture) can wait until the pit lane; do not just tell a struggling driver to stop making mistakes, "fill them with confidence"; engineer must be able to criticise without being "in awe". — same Autosport feature.
- Wright 1992 Mulsanne [1990s]: driver Warwick reported calmly that the engine was cutting out and asked what he could do; engineers advised switching off non-essentials and he nursed the car home — [Autosport](https://www.autosport.com/le-mans/news/how-an-engineer-survives-le-mans/10485835/). Illustrates calm driver report plus short, actionable engineer reply.
- Ferrari and Le Mans organisers say engineers keep drivers calm and focused (snippets).

### Inferences
- Good call template (my synthesis from the above): [name/attention] + [one fact] + [one action/deadline] + [expect readback]. E.g. "Box this lap, box box" style positive phrasing; avoid negatives.
- Never talk mid-corner or in dense traffic; hold non-urgent items until a straight or the pit lane; batch info before a known quiet moment.
- For a sim assistant with TTS: hard cap on message length, queue and defer by track-position (straights), suppress during traffic/incident, prefer driver-configurable verbosity (the Räikkönen/Villeneuve spectrum).
- Fatigue handling: sources only state calm/steady tone; specific techniques (more reminders, check-ins) are inference.

### Gaps
- No verbatim IMSA/WEC/Le Mans race radio transcripts found from reliable text sources; do not fabricate. Video compilations (YouTube, team content) were not accessible.
- No sourced technique for handling driver errors/fatigue specific to endurance.

## How do engineers use debriefs and telemetry overlays to find lap time?

### Takeaway
Overlays against a reference (own best, team-mate, benchmark) located by distance delta, then drill into channels at that point; debriefs pair driver narrative with data. Sources found are generic/F1/consumer-tool; no endurance-specific primary source.

### Cited Findings
- F1 glossary: debrief is a post-session meeting where driver, race engineer and performance engineers review telemetry against driver feedback; good debriefs reference lap, reference tyre, reference fuel load and deviations — [F1 Fansite](https://www.f1-fansite.com/glossary/debrief/) (fan glossary, low authority)
- Delta vs reference lap shows where time is gained/lost; then compare other channels at that point (line, throttle, brake point) — [GoSetups](https://support.gosetups.gg/hc/en-gb/articles/34406195292690-Understanding-Your-Telemetry-Data) (sim tool support doc)
- Setup sheets paired with telemetry and driver notes isolate which changes helped — search snippet, source not identified.

### Inferences
- A sim assistant should normalise for fuel/tyre state before comparing laps; compare same-car-state laps.

### Gaps
- No practitioner interview on driver-vs-driver corner comparison in GTP/Hypercar.

## Common mistakes and failure modes

### Takeaway
Practitioner sources (F1) point to over-talking, badly timed calls, reciting the obvious, and mismatching style to driver. Endurance-specific failure-mode accounts were not found.

### Cited Findings
- Talking in braking zones/corners risks missed braking points; info given when the driver cannot act on it is wasted; "telling them the obvious" is a mistake; panicking engineer worsens driver state; one-size tone fails (Shovlin, Permane) [F1] — [Autosport](https://www.autosport.com/f1/news/the-secrets-of-in-race-radio-chat-5102490/5102490/)
- Negated phrasing can be misheard, with a risk of an erroneous pit entry [LMP1] — Porsche Newsroom above.
- Silence is also a risk: Shovlin said drivers cannot be left without input on key things [F1] (snippet) — Autosport.

### Inferences
- Late calls (pit window, fuel/energy) are the mirror failure to too much talk; implied by the sources but not directly sourced for endurance.
- Wrong data (stale or mis-scaled values) leads to wrong calls; this project's CLAUDE.md lesson on silent wrong decoding is a direct analogue (internal, not research).

### Gaps
- No endurance practitioner post-mortems of engineer errors found.
