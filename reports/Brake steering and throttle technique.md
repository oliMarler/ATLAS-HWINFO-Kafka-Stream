# Peak early, release by corner, call once

The research gives a clear picture of good inputs and a clear coaching method, but almost none of the numbers a coaching assistant would want to hard-code. Through a corner the three controls work as **one sequence drawing on one grip budget**: a fast, smooth rise to peak brake pressure at the very top of the zone; a steady bleed-off as speed and downforce fall; a release that tapers in proportion to steering and changes rate with corner type; one steering build to no more lock than the front tyres can use; and throttle that waits for the wheel to start unwinding, then reaches committed full throttle with no lift. Faults travel down that sequence. An abrupt release or a misjudged entry speed shows up later as extra lock, corrections, a late or interrupted throttle and an exit slide. So the most useful change to the assistant is to **coach the earliest input that departs from the reference and hold back the symptoms it explains**. The existing thresholds (peak pressure 10% low, 0.15 s slower to full pressure, two extra steering corrections) are placeholders. The only time-to-peak data are an anecdotal, search-summary-only forum report of **about 0.45 s for a pro in an IMSA LMP-C car**, set against a second-hand 0.2 s yardstick. No source publishes release rates, correction counts, wheelspin limits or GTP tyre windows. Several checks should become **two-sided**: a release can be too fast or too slow, steering too little or past the knee, coasting deliberate or hesitant. They should be judged against a reference lap from the **same stint phase**, not a fresh-tyre best, and they should infer lockups and wheelspin from longitudinal g and rpm, because the telemetry has no wheel speeds. iRacing's brake migration needs its own convention: **base bias applies at 100% pedal, and migration is added as the pedal comes off**. One Le Mans Ultimate guide describes the reverse. Some questions stay contested: whether traction control saves rear tyres, the optimal slip ratio, and whether a radio call should prescribe a number or build awareness, as Ross Bentley prefers. Little professional material is GTP-specific, so most of the guidance comes from general race-car coaching and sim-coaching sites. Read it with the labels set out below.

## Labels, quotes and how much each line can carry

Every finding keeps the label its research note gave it. **PRO** marks real-world professional material: drivers, teams, suppliers, and professional data and coaching schools. **SIM** marks iRacing's own documents and sim-coaching sites; **LMU** is added where the source covers Le Mans Ultimate rather than iRacing. **RESEARCH** marks motor-learning science. Three confidence markers recur:

- **single-source**: only one source was found for the claim.
- **search-summary only**: the page was blocked or not fetched, so the wording comes from a search engine's summary and is unverified.
- **inferred**: reasoning by the researchers or by me, not a sourced claim.

Each section keeps three kinds of content apart: **Findings** (what a cited page says), **Suggestions** (inference: mine unless credited to the notes' researchers) and **Gaps**.

Direct quotation is kept only where the notes mark the wording as checked against a page that was actually read. Those pages are:

- Ross Bentley's *Coaching With Data* PDF and his best-lap Q&A, both read in full;
- his "If-Then" page and his throttle-histogram article, both marked verbatim;
- the iRacing Cadillac GTP manual;
- the phrase lists that the braking, steering and throttle notes flag as verbatim, minus their search-summary entries.

Everything else is paraphrased. Every suggested radio call below is my wording. It is set in italics and never in quotation marks.

Two cautions frame the whole report. First, very little PRO material covers GTP technique specifically. The exceptions are a feature on the Porsche 963's brake system and some IMSA tyre quotes, so most technique guidance is general race-car coaching. Second, the notes treat the iRacing Valkyrie as an LMH car whose powertrain they did not confirm. Findings about rear-axle hybrid deployment and regenerative braking come from LMDh material (the Porsche 963) and are unverified for the Valkyrie.

Material from the earlier endurance research in this conversation is folded in where it still applies.

## One corner, one chain: faults travel downstream

The notes describe each control in terms of the other two. Reviewing the inputs separately misses that one early mistake can trip several of the assistant's checks at once.

### The sequence the sources describe

**Findings.** All three controls draw on one tyre grip budget, shared between braking, accelerating and cornering: the traction circle Brian Beckman set out in 1991 [PRO] ([Beckman](https://miata.net/sport/Physics/07-Circle.html)). HP Academy [PRO, search-summary only] adds two points. A tyre loaded in combined braking and turning cannot brake as hard as it can in a straight line. And the useful information in a G-G cloud sits in the transitions between pure braking, pure cornering and drive ([HP Academy, G-G diagram](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-gg-diagram/)).

Read in order, the sources describe a corner as five linked phases:

1. **Application.** Peak pressure belongs at the start of the stop ([HP Academy, braking](https://hpacademy.com/courses/professional-motorsport-data-analysis/braking-performance-braking-technique)).
2. **Bleed-off.** Pressure falls as speed and downforce fall (same source; [Coach Dave, Porsche 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)).
3. **Release blended into turn-in.** Pressure comes off in proportion to steering, checked on an XY plot of steering against brake pressure ([HP Academy](https://hpacademy.com/courses/professional-motorsport-data-analysis/braking-performance-braking-technique)). Coach Dave [SIM] puts it as "The brake pressure should gradually taper off as steering input increases" ([Coach Dave, brake traces](https://coachdaveacademy.com/tutorials/a-delta-guide-understanding-brake-traces-to-be-faster)). Trailing light pressure keeps the fronts loaded and lightens the rear so the car rotates (Bryan Van Noy [PRO], [NASA Speed News](https://nasaspeed.news/columns/driver-instruction/the-art-of-releasing-the-brakes/)). Bentley [PRO] says the timing and rate of the release rotate the car "with a minimum of steering" ([Speed Secrets](https://speedsecrets.com/q-how-can-i-make-my-car-rotate-more-into-a-corner/)).
4. **Rotation through minimum speed.** Bentley says to wait a moment before the throttle so the car can finish rotating: throttle applied too soon moves load rearward and stops the rotation (same page). The Racers360 coaches [PRO] "don't want to touch the throttle until we can start to unwind the steering wheel" ([Mazda Motorsports](https://www.mazdamotorsports.com/2020/02/25/driving-tip-1-the-top-mistakes-grassroots-race-car-drivers-make/)).
5. **Unwind and drive.** Driver61 [PRO]: "Continue to add more throttle as you open up the steering angle" ([Driver61](https://driver61.com/uni/corner-exit/)). Track Titan [SIM]: "Gradually increase throttle as you unwind the steering wheel" ([Track Titan](https://www.tracktitan.io/study-plans/a4463edd-0169-4895-a7b8-644df1db64d1-accelerating-the-unwind)).

The sequence has exceptions. Bentley rejects fixed rules such as always starting the throttle at the apex ([Speed Secrets If-Then](https://rossbentley.substack.com/p/speed-secrets-if-then-revisited)). Notes on *Ultimate Speed Secrets* say earlier throttle helps some cars [PRO, search-summary only] ([Goodreads notes](https://www.goodreads.com/notes/19027835-ultimate-speed-secrets/69038094-teeranai-tananusin?page=6)). The throttle also steers. Peter Krause [PRO, search-summary only] widens an exit by adding power rather than opening the wheel ([Classic Motorsports](https://classicmotorsports.com/articles/basic-training-10-steps-faster-laps/)). Don Alexander [PRO, single-source] used small throttle changes to cut steering lock and spare a left-front tyre ([NASA Speed News](https://nasaspeed.news/tech/suspension/tire-management-how-to-get-the-most-out-of-your-race-tires-from-behind-the-wheel/)).

### How an early fault shows up later

**Findings.** Only one complete chain is sourced. HP Academy [PRO] describes entry or mid-corner understeer that makes the driver delay the throttle and then apply it aggressively, so the rear breaks away and the steering trace shows rapid countersteer ([HP Academy, steering and balance](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)). The other links are each sourced on their own:

- **Release.** An abrupt release unloads the front and causes understeer; too slow a release over-slows the car and overloads the fronts [PRO, search-summary only] ([Speed Secrets](https://speedsecrets.com/?p=26035)). A sudden pressure drop destabilises the car and, in an aero car, costs downforce [SIM] ([Coach Dave](https://coachdaveacademy.com/tutorials/a-delta-guide-understanding-brake-traces-to-be-faster)). More trail braking can itself overload the fronts into understeer [PRO] ([Speed Secrets](https://speedsecrets.com/q-how-can-i-make-my-car-rotate-more-into-a-corner/)).
- **Entry speed to throttle.** Bentley's If-Then rules [PRO, checked] make the connection ([If-Then](https://rossbentley.substack.com/p/speed-secrets-if-then-revisited)):
  - "If you can begin to apply the throttle early in the corner" then "you probably over-slowed."
  - "If you have to wait until you're well beyond the apex before starting to apply the throttle…" then "you probably (but there are exceptions to this) carried too much entry speed."
  - "If you're inconsistent with where you begin to apply the throttle in corners…" then "you probably don't have enough references and/or your braking is inconsistent."

  The Racers360 coaches add that early throttle is often a reaction to over-slowing, and should be fixed in the braking zone ([Mazda](https://www.mazdamotorsports.com/2020/02/25/driving-tip-1-the-top-mistakes-grassroots-race-car-drivers-make/)).
- **Early throttle and steering.** Dion von Moltke [PRO] says throttle applied while still heading to the apex shifts weight rearward and causes understeer, so the driver adds steering just when the hands should be opening. He names early turn-in, unused track width and too much entry speed as the other reasons a driver cannot unwind ([Blayze](https://blayze.io/blog/car-racing/why-you-cant-open-your-hands-at-corner-exit)). HP Academy adds that after an early turn-in the car simply needs turning more sharply, at a lower apex speed. Coach Dave [SIM] reads power applied with lock still on as understeer; it shows as a throttle trace rising earlier than the reference while the delta is still growing ([Coach Dave, throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)).
- **Apex and downshifts.** MotoIQ [PRO] says holding the apex too long delays the throttle ([MotoIQ](https://motoiq.com/youre-doing-it-wrong-common-driver-errors-often-mistaken-for-handling-issues/3)). HP Academy ties unsteady downshift blips and brake modulation to rear locking and entry instability.
- **Across corners.** Track Titan's ranking tool found an Oulton Park loss that began two corners earlier, where the driver had not straightened the car for braking [SIM, vendor claim, search-summary only] ([Track Titan](https://www.tracktitan.io/post/december-2025-track-titan-update-faster-coaching-flows-social-leaderboards-bigger-team)). YDD [PRO] warns that a gain in one corner changes the approach to and exit from the next ([YDD](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)).

| Earliest departure from the reference | Downstream flags it can raise | Basis | Coach this |
|---|---|---|---|
| Release snapped off at turn-in | Entry understeer, added lock, corrections, late or hesitant throttle; exit slide if the throttle is then stabbed | Speed Secrets [PRO, search-summary only]; Coach Dave [SIM]; HP Academy chain [PRO]; the join [inferred] | Release rate |
| Brake held too deep into the corner | Over-slowed apex, understeer from front overload, early pick-up then back-off | Speed Secrets [PRO, search-summary only]; Bentley [PRO]; If-Then [PRO] | Release earlier, or brake later |
| Too much entry speed | Cannot unwind, throttle well past the apex, corrections | If-Then [PRO]; von Moltke [PRO] | Brake point or entry speed |
| Over-slowed entry | Early throttle with lock on, understeer, lock added at the apex, back-off | If-Then [PRO]; Racers360 [PRO]; von Moltke [PRO]; Coach Dave [SIM] | The braking zone, not the throttle |
| Early turn-in | Lock added after the apex, low apex speed, late throttle | HP Academy [PRO]; von Moltke [PRO] | Turn-in point |
| Apex held, late unwind | Late throttle, low exit speed | MotoIQ [PRO] | Unwind timing |
| Unsteady downshifts | Rear lock, entry instability, countersteer under braking | HP Academy [PRO] | Pedal and blips through the downshifts |
| Throttle stab or too-fast application | Wheelspin, rear slide, exit countersteer | Driver61 [PRO]; HP Academy [PRO]; Fanatec [SIM] | Throttle application |
| Previous corner's exit or the straight | Next corner's braking or entry fault | Track Titan [SIM, vendor claim, search-summary only] | The earlier corner |

**Suggestions [inferred].** HP Academy's chain from understeer to oversteer is the only one any source describes end to end. The longer chains in the table join links sourced separately. Read that way, one snapped-off release can trip the release-time, steering-correction, throttle-back-off and exit-slide checks on the same corner: four radio calls for one cause.

### The root-cause rule: coach the earliest departure

**What is sourced.**

- Bentley's If-Then rules and his diagnosis of throttle lifts point from a throttle symptom back to entry speed, braking or line.
- The Racers360 coaches put the fix for early throttle in the braking zone.
- Von Moltke has drivers check their own entry errors before cutting entry speed.
- Track Titan traces some losses to earlier corners (vendor claim, search-summary only).
- YDD says gains from different corners do not add up.
- Bentley and Scott Mansell keep the work to one or two items.

The steering researcher inferred that the first error in the chain, usually at entry, should be fixed before any of it is blamed on setup. None of the sources states the rule below.

**The rule (my suggestion).**

1. For each corner, align the lap to the reference by distance.
2. Walk the phases in order: the previous corner's exit and the straight, brake onset, time to peak, peak, bleed-off, release start and rate, turn-in point and rate, minimum speed and where it falls, unwind start, throttle-on, time to full throttle, exit speed.
3. Stop at the first phase whose departure exceeds the driver's own lap-to-lap spread on at least three of the last five clean laps. Coach only that.
4. Mark the downstream flags that phase's table row predicts as explained. Keep them off the radio and list them in the debrief as consequences.
5. If those flags have not faded within three to five clean laps of the fix, promote the next departure.

A downstream flag with no upstream departure is a root cause in its own right. If it repeats under clean inputs, it becomes a car or tyre question. Deliberate upstream changes are not faults: traffic, fuel-saving lifts, cold out-laps and yellow flags.

**Limits of the rule [inferred].** Causality can run backwards. A driver who slid on exit last lap may brake earlier this lap, so the earliest departure is the response, not the cause. Checking which flag appeared first on earlier laps guards against this. "Earliest" also favours entry, while VRS ranks exit first for lap time, so the rule decides what to coach and the time delta decides whether it is worth a call. The spread gate keeps noise in an early phase from capturing the call.

### The same chain explains tyre wear

**Findings.** Across the notes, the common heat source is slip beyond what the corner needs.

- Alexander [PRO] says turning the wheel faster than the slip angles can build scrubs and heats the tyres, and a hard, fast throttle overheats them through wheelspin. Hard braking heats the fronts and hard acceleration the rears. Smooth trail braking reduces entry understeer, but braking that unsettles the car while turning wears the tyres ([NASA Speed News](https://nasaspeed.news/tech/suspension/tire-management-how-to-get-the-most-out-of-your-race-tires-from-behind-the-wheel/)).
- Coach Dave [SIM] calls lock beyond the optimum a brake that scrubs the fronts, and says jerky inputs overload the tyres ([Coach Dave, steering](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)). Its guide to the 2025 iRacing tyre model [SIM] names lockups, wheelspin and overdriving as accelerating wear ([Coach Dave, 2025 tyre model](https://coachdaveacademy.com/announcements/the-2025-iracing-gt3-tyre-model-update-explained/)).
- RaceLab [SIM, attribution search-summary only] says turning while braking too hard exceeds the grip budget and causes braking-induced understeer ([RaceLab](https://docs.racelab.app/news/2025/09/22/2025/g-force-meter)).
- HP Academy [PRO] links front degradation to more mid-corner understeer, and rear degradation to more exit corrections ([HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)).

**Suggestions [inferred].** A mismatch between inputs is a demand larger than one axle's share of the grip budget.

- **Entry mismatches spend the fronts:** a lock, trailing deep into high lock, or lock added because of early throttle or an early turn-in.
- **Exit mismatches spend the rears:** a stab, throttle with lock still on, or a slide after a delayed throttle.
- **HP Academy's chain spends both:** front scrub mid-corner, then a rear slide on exit.

Fixing the earliest departure therefore protects both axles, which is a tyre argument for the chain rule. The loop also runs the other way. Worn fronts move the steering knee to lower lateral g, and worn rears spin earlier, so they raise the same flags as technique faults. That is why late-stint flags need a phase-matched reference.

On the G-G plot:

- a straight chord, or a notch toward the origin, is unused grip;
- a spike past the reference envelope is slip spent;
- a full envelope bought with extra lock is tyre life spent.

### What the notes do not establish

**Gaps.**

- No source measures how often a given upstream fault produces a given downstream symptom, or what each link costs in time or tyre wear.
- No source tests the earliest-departure rule, or any data-only method for telling a chain of driver faults from car balance.
- Track Titan's multi-corner tracing is a vendor claim, seen only in a search summary.
- Nothing covers how GTP-specific systems alter the chain: regen and brake-by-wire in the braking phase, pedal-dependent migration in the release (its sign unconfirmed in iRacing), rear-axle deployment on the 963's exit, or the Valkyrie's unconfirmed powertrain.
- No source says how much steering may remain at full throttle in a prototype, or how traffic and dirty air reshape the sequence.

## Ten existing checks, held against the research

The table sets each existing check against what the notes support. The change column is my suggestion. The last column says whether any number survives.

| Existing check | What the research supports | Suggested change (mine) | Threshold standing |
|---|---|---|---|
| Brake release time (trail braking) | Release is the decisive entry skill; pressure tapers in proportion to steering; rate differs by corner type [PRO, SIM] | Give it a sign (snapped off vs held too long); add brake % at turn-in, steering-vs-brake linearity and a snap-off gradient; read it with migration | No sourced release rate, brake % at turn-in or trail length |
| Initial application (peak 10% low, or 0.15 s slower) | Fast, smooth rise with the peak at the start of the zone, then bleed-off [PRO, SIM] | Measure time to peak as onset to ~95% of that zone's peak; check lockups, out-lap and fuel before calling for more pedal; add a re-application check | 0.15 s and 10% unsourced; one anecdotal pro figure (~0.45 s) |
| Coasting time | Minimise the gap between throttle and brake [PRO]; pros also coast while waiting to unwind [PRO] | Split pre-brake from mid-corner coasting; mute pre-brake coasting while fuel saving | No sourced limit |
| Steering corrections (2+ over best) | Corrections are symptoms; count reversals after filtering, above a gap [PRO, road research] | Classify by type and phase, pair with time lost, trace to the brake or throttle cause | "Two" unsourced; no published counts |
| Throttle back-offs before full | Pick up, ease off, pick up again (on-off-on) costs about a tenth [PRO, search-summary only]; early pick-up means over-slowed [PRO] | Make apex to sustained full throttle the primary metric; diagnose back-offs through steering and entry | ~0.1 s rule of thumb; ">95% = full" from a forum |
| Rear slides on exit | A slide after a smooth input points to the car, after a stab to the driver [inferred from PRO]; hybrid torque can spike [SIM] | Look upstream first; detect spin from rpm/speed per gear; slides at a fixed lap distance whatever the input point to the car | No wheelspin limit; 6–7% vs ~10% conflict |
| Shift points, downshift over-revs | Thin coverage: unsteady downshifts lock the rears [PRO]; short-shift in the wet and for fuel [SIM] | Tie entry instability to downshift timing; offer short-shifting as a rear-tyre tool | Nothing GTP-specific |
| Tyre temps across the tread (practice) | Middle vs edges reads pressure; inner vs outer reads camber [SIM] | Remap telemetry left/right to inner/outer per side; compare the same lap of a stint; read spreads | 6–10° and ≤7 °C are forum or low-authority; no GTP window |
| G-G diagram | Transitions carry the information; a straight chord means unused grip [PRO, search-summary only] | Add a per-corner transition dip and overload spike; overlay pedal state | No GTP G-G data |
| Balance index | Steering against lateral g and yaw shows when extra lock stops buying turn [PRO]; balance is relative | Compare only within the same car, setup and tyre state; consistent signatures point to the car, variable ones to the driver | No published thresholds |
| One radio call at a time | Keep radio short, on straights, from one voice [PRO, search-summary only]; work on one or two items [PRO] | One root-cause item until confirmed over 3–5 clean laps; numbers only when earned | No tested call format |

## Brakes: peak at the top of the zone, bleed off with the downforce

### Initial application: one anecdotal pro figure of 0.45 seconds

**Findings.** HP Academy's professional data-analysis course [PRO] makes four points ([HP Academy](https://hpacademy.com/courses/professional-motorsport-data-analysis/braking-performance-braking-technique)):

- The quicker the pressure builds, the sooner the tyres reach peak slip ratio. The ideal rate depends on the car, tyres, suspension and stability margin.
- **Peak pressure belongs at the start of the stop**, followed by a smooth release.
- A named fault: the driver hits peak, realises the brake point was early, releases and reapplies.
- High-downforce cars need a **steady drop in pedal pressure** as speed and downforce-driven tyre load fall, to hold peak slip without locking. Low-downforce cars can hold a flatter plateau.

Coach Dave Academy [SIM] wants "a smooth but rapid initial application". It reads a gradual rise as low confidence in the zone or the references, and says to check that the pedal setup delivers full pressure easily ([Coach Dave, brake traces](https://coachdaveacademy.com/tutorials/a-delta-guide-understanding-brake-traces-to-be-faster)). Driver61 [PRO] puts peak grip at 3–10% slip and warns against shocking the car. It says slight under-rotation of a tyre signals an imminent lock, and the fix for a front lock is a slight release. It gives one example where braking 10 m later saved about 0.2 s [single-source] ([Driver61](https://driver61.com/uni/braking/)).

For the GTP cars, Coach Dave's iRacing Porsche 963 guide [SIM] stresses that the car has no ABS and tends to lock its fronts, and that entry understeer adds front load and lock risk. It advises "Being lighter on the pedal when the effect of downforce is less prevalent will make braking easier", and recommends braking in a straight line before turn-in ([Coach Dave, 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)). The only Valkyrie material covers LMU [SIM, LMU, search-summary only]: brake earlier, as in an LMDh car; lockups are common; the car tends to lock front and rear equally ([Coach Dave, LMU Valkyrie](https://coachdaveacademy.com/tutorials/lmu-aston-martin-valkyrie-guide-the-inside-line/)).

**Numbers.** One Rennlist thread [PRO, single-source, search-summary only; about eight years old; page returned 403] reports ([Rennlist](https://rennlist.com/forums/data-acquisition-and-analysis-for-racing-and-de/1120029-understanding-brake-pressure-psi-what-is-it-telling-me.html)):

- **0.45–0.47 s to maximum pressure** in most zones, for the fastest IMSA LMP-C pole lap at Sebring and a lap near the VIR record;
- club drivers often well over 0.33 s, some at 0.8–1.0 s;
- an OptimumG yardstick of about 0.2 s, known only second-hand;
- the poster's own target of under 0.4 s.

**Conflict:** 0.45 s for pros against a 0.2 s yardstick. The braking researcher offers three untested explanations [inferred]: "maximum" may be defined differently (first plateau or absolute peak), pros may shape the end of the rise to settle the platform, or 0.2 s may be an ideal.

Fanatec [SIM, single vendor, search-summary only] gives an **85–90% peak** for iRacing's closed-wheel GT and LMDh cars, and 70–90% for GT cars depending on conditions. But the same article tells LMDh drivers to avoid triggering ABS, which those cars do not have, so it is unreliable on prototypes ([Fanatec](https://fanatec.com/eu/en/explorer/games/gaming-tips/sim-racing-braking-technique/); contradicted by [Coach Dave, 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)).

The deceleration figures are all LMP1-era: braking at Le Mans of no more than 3.5 g [PRO, search-summary only, page returned 403] ([F1Technical](https://www.f1technical.net/features/21668)), and about 3.2 s from nearly 200 mph to 60 mph [PRO, search-summary only] ([Autocar](https://autocar.co.uk/node/87174)), which the researcher converts to an average near 2.0 g [inferred]. No figure comes from the GTP era.

**Suggestions.**

- **Calibrate the 0.15 s threshold.** It is about a third of the only pro rise time: a plausible scale, but unsourced. Set it per corner from the spread of the driver's own clean laps, and flag only deficits beyond that spread [mine].
- **Define time to peak consistently.** Measure from brake onset to about 95% of that zone's own peak [inferred, braking notes]. This also defuses the definition conflict.
- **Compare peak pedal only like for like.** It depends on the garage brake-pressure or master-cylinder setting and on pedal calibration [inferred], so compare it within one car, setup and rig, as the own-best reference already does.
- **Treat a lower peak as possibly deliberate.** In a car without ABS it often is: after a lockup, on cold tyres, with worn fronts, or on more fuel than the best lap carried. Before calling for more pedal, check for recent locks at that corner, out-lap status and fuel load [mine]. Pair the pedal peak with peak longitudinal g in the first 20–30% of the zone: normal pedal with low g points to grip, low pedal with low g to technique [inferred].
- **Add the re-application pattern** HP Academy names, and AiM's reading of a pressure spike as a stab and a mid-zone dip as an early release [PRO/kart, search-summary only] ([AiM](https://www.aimshop.com/blogs/news/save-a-second-off-your-lap-time-for-under-200)).
- **Infer lockups from what the telemetry has** [inferred; to validate in iRacing data]. With no wheel speeds, a lockup would show as longitudinal g falling while the pedal is flat or rising, and speed decay flattening against the reference. A front lock would add a pressure dip, small corrections or a late apex; a rear lock would add countersteer under braking. HP Academy calls wheel speed the real lockup channel and pressure alone a weak one [PRO, search-summary only] ([HP Academy, speed sensors](https://www.hpacademy.com/courses/data-analysis-fundamentals/essential-sensors-speed/)). Whether iRacing exposes live per-wheel speed was not checked.

**Calls (suggested).**

- *Turn 1, firmer at the top, same marker.*
- *Turn 4, one squeeze, then bleed it off.*
- *Front lock at the bottom of Turn 1: bleed it off sooner as the speed drops.*

No source publishes these. The last echoes the 963 guide's advice to go lighter on the pedal as the downforce fades.

**Gaps.**

- No time-to-peak, peak-pressure or deceleration figure from 2023 onward for any GTP, LMH, LMP2 or race GT3 car.
- No peak percentage for the iRacing GTP cars.
- No lap-time cost per tenth of a slower build.

### Release and trail braking: faults in both directions, rates that change by corner

**Findings.** HP Academy [PRO] says that during trail braking, pressure should come down in proportion to steering, steadily and linearly toward the apex. Plot steering against brake pressure on an XY chart: points above a linear target line mean too much brake held while steering, points below mean too little. Small applications between corners should be gentle and symmetrical, and channels must be aligned before laps are compared ([HP Academy](https://hpacademy.com/courses/professional-motorsport-data-analysis/braking-performance-braking-technique)).

Coach Dave [SIM] says ([Coach Dave](https://coachdaveacademy.com/tutorials/a-delta-guide-understanding-brake-traces-to-be-faster)):

- "The brake pressure should gradually taper off as steering input increases."
- A sudden drop at the end of the zone, against the reference, is releasing too quickly. It destabilises the car and, in an aero car, drops downforce.
- An early release can reflect low confidence.
- Staying at peak longer than the reference means too long on the brakes.

Van Noy [PRO] calls the release, not the hit, the difference-maker, and varies it by corner ([NASA Speed News](https://nasaspeed.news/columns/driver-instruction/the-art-of-releasing-the-brakes/)):

- **Slow corners and hairpins:** hold pressure deeper and ease off toward the apex.
- **Medium corners:** a quicker but progressive release, then straight to throttle without coasting.
- **High-speed corners:** softer, longer initial pressure and a smooth, gradual release, because "Too much brake pressure tends to upset most cars in the highest-speed corners."

He also says "The steering wheel is also a brake."

Speed Secrets [PRO, search-summary only; exact page unconfirmed] says too quick a release unloads the front and causes understeer, too slow over-slows the car and overloads the fronts, and one release used in every corner cannot be right ([Speed Secrets](https://speedsecrets.com/?p=26035)). Bentley reportedly coaches release more than anything else [PRO, search-summary only] ([Speed Secrets](https://speedsecrets.com/?p=39183)). A Speed Secrets Q&A moves the whole braking zone later when an early release causes understeer [PRO, search-summary only] ([Speed Secrets](https://speedsecrets.com/q-how-do-i-stop-over-braking-and-causing-my-car-to-understeer/)). Bentley's own data read [PRO] needs only the speed trace: trail braking makes a "hockey stick" at the bottom of a corner, while a "square" bottom means little or none ([Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)). Driver61 [PRO] frames trail braking as adjusting balance at a much-reduced rate, brushing the brakes over a longer distance in fast corners ([Driver61](https://driver61.com/uni/braking/)).

**Numbers.** None sourced: no release rate, no brake percentage at turn-in and no trail length for any class.

**Suggestions.**

- **Give the release check a sign.** The current check flags release time against the best lap. The sources describe faults in both directions with different consequences, so the check should carry a direction and a cause [inferred mapping from the braking notes]: shorter than the reference, with entry understeer or added lock, is a snap-off; longer, with the brake still on at peak lock and a lower minimum speed, is over-trailing or over-slowing.
- **Adopt the braking researcher's metric set**, which fits the available channels [inferred]:
  - release start: pressure below ~90% of the zone peak;
  - release rate, in %/s or %/m against the reference;
  - brake % at the first meaningful steering input;
  - trail length, from turn-in to zero pressure;
  - the residual from HP Academy's XY line;
  - a snap-off measure: the steepest negative gradient in the last ~10% of the zone.
- **Use the hockey stick as a cross-check.** Bentley's shape needs only speed.
- **Key expectations to corner type.** Use Van Noy's three profiles, keyed on minimum speed, as expectations rather than rules [mine].
- **Weight high-speed releases most.** In a high-downforce GTP, an abrupt release in a fast corner moves the aero platform as well as the load [inferred].
- **For the 963,** the straight-line braking advice plus the car's tendency to lock its fronts argue for finishing the heavy part of the stop before the wheel turns, and carrying only the bleed-off into the corner [inferred].

**Calls (suggested).**

- *Turn 6, ease the brake off as you turn in.* (snap-off)
- *Turn 6, brake's still on at the apex; let it go a few metres sooner.* (over-trail)

For practice, Bentley's checked wording is a model awareness instruction: "Experiment with the timing & rate of release of the brakes – focus on Turns 6, 7, 8, 9" ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)).

**Gaps.** No GTP driver interview on how much they trail brake.

### Bias and migration: iRacing applies the base bias at full pedal

**Findings.** iRacing's 2025 Season 3 Patch 3 notes of 27 June 2025 [SIM, official] cover the GTP class ([iRacing release notes](https://support.iracing.com/support/solutions/articles/31000176763-2025-season-3-patch-3-release-notes-2025-06-27-02-)):

- They fixed migration being applied at half its stated value, and adjusted the "ramping reference location".
- They define the convention: **at 100% pedal the bias equals the base setting; at 0% pedal it equals base plus the migration gain**.
- To carry existing setups over, they say to halve the migration and move bias forward 1–1.25%.
- The Acura gained a migration adjustment to match the rest of the class; the Ferrari 499P's migration already worked.

Traxion's LMU guide [SIM, LMU] uses the opposite reference point: migration moves the balance forward as pedal travel reaches 100%, so a 54:46 base with 2.0F becomes 56:44 at full travel. LMU offers migration from 0 to 2.5 in 0.5 steps, adjustable on track. The guide calls 2.5F optimal for all Hypercars [single-source] and says migration aids trail braking ([Traxion](https://traxion.gg/le-mans-ultimate-how-to-master-hypercar-braking/)). **Conflict:** Coach Dave's LMU Valkyrie guide [SIM, LMU, search-summary only] disables migration as a safe baseline ([Coach Dave, LMU Valkyrie](https://coachdaveacademy.com/tutorials/lmu-aston-martin-valkyrie-guide-the-inside-line/)).

On the real Porsche 963 [PRO] ([Motorsport.com via Yahoo](https://sports.yahoo.com/article/point-brake-complexities-behind-porsches-120003063.html)):

- The rear axle uses Bosch brake-by-wire to blend friction braking, MGU regeneration and engine braking, with no fixed split.
- Bosch's Jordan Krell describes migration as dynamic bias that can move rearward as the car slows.
- Felipe Nasr says the migration shaping is cockpit-adjustable, with separate terms for straight-line and cornering braking. Drivers make a handful of bias and migration changes per lap. Long zones are the trickiest, and the aim is not to lock any tyre.
- The MGU supplies up to 40% of rear braking in the hardest zones, and the regen available depends on the battery's state of charge.

**Discarded:** the fetched summary of that article reverses the usual bias direction, against every other source ([Speed Secrets, bias Q&A](https://speedsecrets.com/q-should-i-adjust-brake-bias-during-a-race-how-do-i-know-when-to-adjust-brake-bias/); [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)).

The direction rules elsewhere agree. Speed Secrets' bias Q&A [PRO; attribution to Bentley inferred from the site] says ([Speed Secrets](https://speedsecrets.com/q-should-i-adjust-brake-bias-during-a-race-how-do-i-know-when-to-adjust-brake-bias/)):

- Numb steering, or a pull to one side under hard braking, means a front lock: move bias rearward.
- A wiggling rear and entry oversteer mean move it forward.
- Balance shifts as fuel burns and tyres wear. Make small changes, and return to baseline from time to time.
- "Ideally, you want all four tires to lock up at the exact same time if you brake too hard."
- "If you're getting a touch of front tire lock up, then make a small adjustment towards the rear."

Its bias test is to over-brake on purpose and move bias away from whichever axle locks first, in steps of about half a percent [PRO, search-summary only] ([Speed Secrets](https://speedsecrets.com/q-how-can-i-tell-whether-i-have-my-brake-bias-set-correctly/)). Coach Dave's 963 guide [SIM] offers rearward bias against front locking, and bias as a quicker, safer cure for understeer than the front anti-roll bar ([Coach Dave, 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)). Box This Lap [SIM] puts bias forward for stability. The earlier research recorded its illustrative values of about 44% bias and migration of around −3 to −5, plus its advice to re-check bias as tyres wear ([Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)). LMU guides [SIM, LMU, search-summary only] find a baseline by moving bias rearward until the rear goes unstable, then one or two clicks forward. They move bias rearward as the fronts wear, warn that more than 3–4% from baseline usually creates more problems than it solves, and trim forward early in a stint while the tyres warm ([Simgasm](https://simgasm.com/blogs/news/le-mans-ultimate-how-to-avoid-lock-ups-in-hypercar); [SimRacingCockpit](https://simracingcockpit.gg/le-mans-ultimate-how-to-drive-the-lmgt3-and-hypercar/)).

**Suggestions.**

- **Report bias on iRacing's convention.** Treat the displayed base bias as the peak-pressure bias, and migration as acting on the trail and release [inferred]. Never port LMU migration numbers, which use the opposite reference.
- **Confirm the sign.** The patch note does not give the sign of the gain. Real LMDh practice and LMU both point rearward as pressure falls; confirm in the garage tooltip or the 963 and Valkyrie manuals [inferred].
- **Discount old migration values.** Any value published before 27 June 2025 was applied at half strength and is not comparable [inferred]. That includes the −3 to −5 examples if they predate the patch; their date is not in the notes.
- **Coach the release before migration.** Because migration depends on pedal position, it is coupled to the release check: a driver who trails deeper gets less migration, one who releases early gets more [inferred]. Coaching a release change therefore also changes the bias during the trail phase. Coach the release first and adjust migration afterwards, one change at a time [mine].
- **Tag each lock with its pedal level.** A front lock near full pedal points to base bias too far forward; rear instability late in the zone at low pedal points to too much migration [inferred]. If the ramp shape is ever confirmed, the assistant could compute the effective bias sample by sample from pedal % [mine]; the notes do not document the ramp.
- **Use starting rails, not data, for step sizes.** Steps of half a percent (Speed Secrets, search-summary only) to one percent (the earlier report's suggestion), with a cap of 3–4% from baseline (LMU guides, search-summary only), are reasonable starting points.
- **Allow for regen if it is modelled.** On the 963, a regen share that moves with state of charge could change the tendency to lock the rears from lap to lap. That is unverified for every iRacing car and unknown for the Valkyrie.

**Calls (suggested).**

- *Fronts locking at the top of Turn 1: bias one step rearward.*
- *Rear moving late into Turn 5 as you come off the brake: one step less migration.*
- *Bias is three steps from baseline; go back to baseline and re-check.*

Positive wording ("rearward", not "less forward") follows the Porsche LMP1 radio practice of naming the action wanted rather than the one to avoid ([Porsche Newsroom](http://newsroom.porsche.com/en/motorsports/tests-in-monza-10499.html)).

**Gaps.**

- The 963 and Valkyrie manual brake sections were not read.
- iRacing's migration sign, range and ramp are undocumented beyond the patch note.
- Unknown whether iRacing models the real car's cornering migration term, or regen on the Valkyrie.
- No GTP bias numbers, and no schedule of bias changes per hour of a stint.

### Brakes over a stint: a flat spot outlives the lap that made it

**Findings.** Brembo [PRO] says Hypercar carbon discs need **at least 200 °C**, average **about 400 °C** in a race and can **exceed 1,000 °C**. Brake ducts cost drag, and drivers must control disc and pad temperature and modulate pressure to avoid premature wear ([24h-lemans.com](https://www.24h-lemans.com/en/news/brembo-sheds-light-on-24-hours-of-le-mans-hypercar-brake-systems-59607)). **Conflict:** a separately reported operating range of 250–850 °C [PRO, search-summary only] ([Autobiz](https://www.autobiz.ie/home/brembo-is-official-braking-technology-provider-of-the-le-mans-24-hournbsp)). Porsche and Bosch [PRO] say teams can use regen to manage brake temperature and wear ([Motorsport.com via Yahoo](https://sports.yahoo.com/article/point-brake-complexities-behind-porsches-120003063.html)). Traxion [SIM, LMU] says Hypercars can lose front braking over long stints, which moves the effective bias rearward ([Traxion](https://traxion.gg/le-mans-ultimate-how-to-master-hypercar-braking/)).

Lockups cost more later. Pirelli blamed Sergio Pérez's tyre failure at the 2013 Korean GP on a flat spot from an earlier lockup [PRO, F1, search-summary only] ([Crash.net](https://crash.net/f1/news/196677/1/flat-spot-to-blame-for-perez-tyre-failure)). At Le Mans in 2026, Alpine cut a stint short because of vibration from a slight flat spot [PRO] ([Alpine](https://www.alpine-cars.co.uk/fia-wec/news/a-night-full-of-challenges-for-alpine-2026.html)). An LMU guide [SIM, LMU, search-summary only] advises care on the out-lap, with a small forward bias trim until the tyres warm ([SimRacingCockpit](https://simracingcockpit.gg/le-mans-ultimate-how-to-drive-the-lmgt3-and-hypercar/)).

**Suggestions.**

- **Rank lockups first in a race** [inferred; none of these costs is quantified]. A flat spot lasts the rest of the stint and a locked front loses the corner, so a lockup outranks a slow pressure rise. Trailing deep into high lock adds front wear, and long high-pressure zones add brake heat.
- **Grade out-laps separately.** Use a cold reference, or flag only lockups there [inferred].
- **Measure brake-point consistency** as the spread of brake-onset distance per corner over clean green-flag laps [inferred]. Driver61's single example (10 m later ≈ 0.2 s) gives a sense of scale.

**Calls (suggested).**

- *Two locks into Turn 1 this stint: bleed it off sooner, protect the fronts.*
- *Out-lap: brakes and tyres are cold, brake early into 1 and 2.*

**Gaps.** No source on:

- braking in traffic or dirty air;
- pad and disc wear per stint for LMDh cars;
- how iRacing models brake temperature, fade or flat spots;
- LMP2 braking.

## Steering: one build, one unwind, no lock past the knee

**Findings.**

- **Turn-in rate.** Bentley [PRO] separates the *timing* of steering from its *rate*, and names linear, progressive and digressive rate profiles ([Bentley, Substack, paywalled after the introduction](https://rossbentley.substack.com/p/speed-secrets-timing-and-rate-of)). Fast corners generally want a gentle, progressive turn-in and tight ones a quick, crisp one: "It's impossible to be really fast while always turning the wheel the same way" ([Speed Secrets](https://speedsecrets.com/how-to-turn-the-steering-wheel/)). Blayze coach Colin Mullan [PRO, single-source] prefers a slower first input that lets the weight shift: "Then once the weight is set, the turn can be more aggressive" ([Blayze](https://blayze.io/blog/car-racing/analyze-your-steering-traces)). **Mild conflict:** the steering researcher reconciles the two by reading Bentley's "quick" as a short time to full lock, not a jolt [inferred].
- **Steering against lateral g.** HP Academy [PRO] shows that lateral g plotted against steering traces the shape of the tyre's force-versus-slip curve. Its example has steering still rising while lateral g falls, meaning the fronts have passed peak slip. It also ([HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)):
  - uses steering-roughness and steering-integral channels, and reads a rising integral as a shift toward understeer;
  - notes that extra lock after an early turn-in is not genuine understeer;
  - found front degradation over a stint produced more mid-corner understeer, and rear degradation more exit corrections;
  - says a more oversteering balance needs less steering;
  - warns that steering sign conventions vary.
- **Corrections.** Coach Dave [SIM] reads understeer as high steering angle with little gain in lateral g. It wants minimal mid-corner corrections, and blames them on exit throttle and excess entry speed ([Coach Dave, steering](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)). Fanatec [SIM] adds that some countersteer is normal, and that excessive corrections point to setup or a technique that unsettles the rear ([Fanatec](https://www.fanatec.com/us/en/explorer/products/steering-wheel/steering-input-telemetry/)).
- **Counting reversals.** Road-safety research [PRO, not racing] defines a steering-reversal-rate method, standardised in SAE J2944: low-pass filter the steering, then count reversals larger than a gap threshold. The parameters were not retrieved, and they are tuned for road driving ([SteeringWheelReversalRate](https://github.com/gmarkkula/SteeringWheelReversalRate); [Markkula and Engström 2006](https://eprints.whiterose.ac.uk/id/eprint/131534/)). McLean and Hoffmann (1973) [search-summary only] found that reversal rates track how often the driver corrects, but not necessarily how well they steer ([TRID](https://trid.trb.org/view/64028)).
- **Wear.** Don Alexander [PRO] says turning faster than the slip angles can build leads to over-steering the wheel, scrub, heat and tread wear. He puts peak traction at about 6° of slip, with near-maximum at 4.5–5.5° [single-source, generic race tyres] ([NASA Speed News](https://nasaspeed.news/tech/suspension/tire-management-how-to-get-the-most-out-of-your-race-tires-from-behind-the-wheel/)). Coach Dave [SIM] calls lock beyond the optimal slip angle a brake that scrubs the fronts. Trophi [SIM] defends "smooth is fast" for most cases, but notes that hesitant drivers understeer for lack of front load, and that more abrupt steering helps on slippery street circuits ([trophi.ai](https://www.trophi.ai/post/why-smooth-is-fast-most-of-the-time)).
- **Unwind.** MotoIQ [PRO] says holding the apex delays the throttle: "Instead of driving the car out to your exit point, let the car go out there," and if the car ends up mid-track, "start unwinding your steering a little earlier" ([MotoIQ](https://motoiq.com/youre-doing-it-wrong-common-driver-errors-often-mistaken-for-handling-issues/3)).

**Numbers.** The only figure is Alexander's 4.5–6° of slip: single-source, for generic race tyres, and not observable in the listed channels. No source gives a turn-in rate in degrees per second, a reversal count, a peak-lock tolerance or an understeer-angle limit for any class. The "two more corrections than the best lap" threshold is a placeholder.

**Suggestions.**

- **Count reversals the road-research way:** filter, find the extremes, and count swings above a gap calibrated on the driver's own clean laps for each car [inferred]. The McLean and Hoffmann caveat says to pair the count with time lost.
- **Classify each correction** [inferred, steering notes]:
  - *Countersteer* (steering sign opposite to the yaw or lateral-g direction) is a rear slide. Trace it to exit throttle, or at entry to the brake release or a downshift.
  - *Saw-tooth* oscillation mid-corner is hunting for grip. Trending over a stint, it suggests rear degradation.
  - *Added lock after the first peak* is understeer or a tightening line. Separate them by the lateral-g response: if g rises with the extra lock it is the line; if g is flat or falling, the fronts are saturated.
  - *A late unwind* is holding the apex.

  Check iRacing's steering sign convention before detecting countersteer.
- **Add a minimum-steering check.** Per corner, plot lateral g (or yaw rate times speed) against steering. The best lap runs up to the knee of the curve and stops there. Steering that keeps rising after g flattens is scrub; a driver who never reaches the knee is leaving front grip unused. So this check is two-sided too [inferred].
- **Trend wear indicators over the stint.** Use steering-per-g and steering integral as front-degradation indicators, and exit reversals as a rear one. Coach against the current knee, which moves to lower g as grip falls [inferred].
- **Grade out-laps and traffic laps separately** [inferred].
- **Look for a steering-torque channel.** iRacing may expose one, which would show the steering going light at the limit directly; this is unverified.

**Calls (suggested).**

- *Turn 7, turn in a touch later; you're adding lock at the apex.*
- *Turn 5, less lock, same speed.*
- *Turn 9, open the hands at the apex and let the car run out.*
- *Turn 3, rear's stepping out on entry; ease off the brake as you turn.*

The last is a brake call for a steering symptom: the chain rule at work.

**Gaps.**

- Bentley's paid steering posts, Carroll Smith and Skip Barber were unreachable.
- The reversal-method parameters, the GTP steering ratio and wheelbase (needed for a true understeer angle), and how faithfully iRacing's force feedback reproduces the limit were not found.
- No data link steering smoothness to measured tyre degradation.
- Nothing covers fatigue, night running or line changes in traffic.

## Throttle: the earliest committed full throttle, not the earliest touch

### Exit timing and back-offs

**Findings.**

- **Bentley.** His If-Then rules (quoted in the chain section) [PRO] tie throttle timing to entry. A search summary credits him with valuing how soon full throttle arrives over how early the pedal first moves. It also credits him with a rule of thumb: picking up the throttle too early and then having to ease off costs about a tenth [PRO, search-summary only] ([Speed Secrets 365](https://speedsecrets.com/wp-content/uploads/2025/07/Speed-Secrets-365-v1.1-6-1-25.pdf)).
- **Driver61** [PRO] moves gently from brake to throttle just before the apex and warns "any sharp inputs will cause a premature loss of traction". It builds throttle lap by lap until the car begins to break traction, progressively and predictably ([Driver61, corner exit](https://driver61.com/uni/corner-exit/)).
- **Coach Dave** [SIM] wants full throttle as soon as possible without releasing again, and reads a trace that rises, dips and rises again as power in the wrong phase. It compares the timing, slope and smoothness of the trace with the reference, after first checking pedal calibration ([Coach Dave, throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)). Its 963 guide [SIM] says "Patience then is a virtue before asking for the power to accelerate from the bend," linking this to the car's heavy nose ([Coach Dave, 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)).
- **VRS** [SIM] treats steady part throttle as a balance tool. After an abrupt mid-corner lift, the remedy is to "quickly reapply some maintenance throttle" ([VRS](https://virtualracingschool.com/academy/iracing-career-guide/second-season/car-control/)).
- **Full-throttle share.** Bentley's throttle-histogram article [PRO] gives the strongest caution: "I spent 61% of the lap at full throttle – he was flat to the floor for 68% of the lap. But, we had turned the same lap time, to within a couple of hundredths of a second." The other driver used the throttle "like an on-off switch" and sat at 0% almost 14% more of the lap. When a lift appears on exit, Bentley checks the steering for added lock or countersteer, and if neither, the line ([Speed Secrets](https://speedsecrets.com/use-data-acquisition-be-better-driver/)). HP Academy [PRO, search-summary only] agrees that throttle data alone cannot rank performance ([HP Academy, throttle histogram](https://hpacademy.com/courses/data-analysis-fundamentals/the-data-analysis-tool-box-throttle-histogram)). A MoTeC forum answer [search-summary only] defines "full" as above 95% ([MoTeC forum](https://forum.motec.com.au/viewtopic.php?p=5149)).
- **Pedal map.** The iRacing Cadillac GTP manual [SIM, official] says Throttle Shape setting 1 is linear ("25% throttle = 25% torque"). Higher settings behave like a butterfly valve, with less torque change at the ends of the pedal travel and more in the mid-range ([Cadillac GTP manual](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)).

**Suggestions.**

- **Change the primary exit metric** to the distance from the apex (the minimum-speed point) to sustained throttle of 95% or more, with no lift before the next braking zone. First touch becomes secondary [inferred].
- **Route back-off flags through the chain** [inferred from Bentley]. An early touch followed by a back-off is an entry (over-slowing) call. A first touch well past the apex is an entry-speed or late-apex call. Scattered pick-up points are a call about references or braking consistency.
- **Do not flag steady part throttle.**
- **Compare traces only on the same Throttle Shape setting.** Above setting 1, 40% pedal is not 40% torque [inferred].
- **Measure exit speed carried** at fixed distances after the corner, for example +100 m and +300 m (illustrative). A deficit that grows down the straight is a real exit loss [inferred].
- **Keep full-throttle share as a trend,** never a ranking.

### Wheelspin, traction control and the hybrid

**Findings.**

- **Optimal slip: conflicting figures.** HP Academy [PRO, search-summary only] says traction control compares driven and undriven wheel speeds, with maximum acceleration at around **10% slip** ([HP Academy, traction control](https://www.hpacademy.com/blog/how-traction-control-works/)). Hondata [PRO, search-summary only, road tyres] puts the optimum at **6–7%**, and warns that tyre creep produces a few percent of slip with no real spin ([Hondata](https://www.hondata.com/help/tractioncontrol/theory_of_operation.htm)). Neither is a figure for GTP slicks.
- **iRacing's two TC settings.** The Cadillac GTP manual [SIM, official] defines them, shown on the dash as TC A and TC B ([Cadillac GTP manual](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)):
  - Gain is "the amount of intervention the Traction Control will exert when wheel spin is detected. Higher values result in a more aggressive throttle cut to control wheelspin."
  - Slip is "how sensitive the Traction Control system will be to wheelspin. Higher values will activate the Traction Control system with smaller amounts of wheelspin, while lower values will allow slightly more wheelspin prior to activating the system."
- **Adjusting TC.** Coach Dave [SIM, search-summary only] says to map TC to the wheel for changes in the race as fuel burns, tyres wear and the track rubbers in ([Coach Dave, Cadillac GTP](https://coachdaveacademy.com/tutorials/under-the-hood-tips-and-tricks-to-driving-the-cadillac-v-series-r-gtp/)). Its 963 guide [SIM, single-source] suggests TC around level five or six, and warns that the V8 plus hybrid can spike power on exits ([Coach Dave, 963](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)). Box This Lap [SIM] advises the lowest intervention the driver can run consistently: conservative early, looser once warm, more protective as the tyres wear ([Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)).
- **Conflict: does TC save rear tyres?**
  - *No:* a Michelin remark about motorcycles [PRO, single-source, search-summary only] says constant TC pulses wear tyres faster than a smooth roll-on ([DriveTribe](https://medium.com/@drivetribe/how-traction-control-could-be-prematurely-wearing-out-your-tyre-8e221e333e4e)).
  - *Yes, or it depends:* sim sources say TC off lets a skilled driver control spin and slow wear ([Driver61](https://driver61.com/sim-racing/how-to-be-faster-without-traction-control-in-gran-turismo-sport/)); that a high TC setting saves tyre life [search-summary only] ([trophi.ai](https://www.trophi.ai/post/how-to-drive-without-traction-control-in-f1-24)); and that lower TC is faster but wears more [forum] ([Steam](https://steamcommunity.com/app/805550/discussions/0/2967272951896758149/)).
- **Real IMSA practice.** Racer [PRO, search-summary only] reports teams tuning TC on fresh tyres to build heat, for a small gain ([Racer](https://racer.com/2023/09/16/solving-gtps-cold-tire-conundrum)).
- **The hybrid.** LMDh cars carry a spec 50 kW rear-axle hybrid. Sources **conflict** on whether it can deploy from 0 km/h or only above 120 km/h; LMH front-axle deployment speeds are set by Balance of Performance [PRO, search-summary only] ([Motorsport.com](https://www.motorsport.com/wec/news/what-are-lmh-and-lmdh-the-top-le-mans-24-hours-series-explained/10480126/); [a-e.li](https://a-e.li/reports/le-mans-hypercar-lmdh/)). The Cadillac manual's Balanced hybrid mode needs a few flying laps to learn the track ([Cadillac GTP manual](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)).

**Suggestions.**

- **Detect spin without wheel speeds.** Compare rpm divided by speed against a per-gear baseline learned on steady straight-line samples. Ignore low speeds, and count only excursions clearly above the driver's clean-exit baseline [inferred]. Detect a rear slide from countersteer, or from yaw rate exceeding what steering and speed imply.
- **Check what the throttle channel records.** TC cuts torque downstream of the pedal. If iRacing's throttle channel is the raw pedal, intervention shows as pedal near 100% while acceleration and the rpm rise flatten. This needs verifying per channel [inferred].
- **Attribute each slide by the input before it** [inferred]:
  - within a short window after a stab, a lift or a faster-than-baseline application: the driver;
  - under a smooth application at the driver's baseline rate: the car (rear grip, differential, TC or tyres);
  - at the same lap distance whatever the input: possibly hybrid deployment or the turbos;
  - more slip from the same input as the stint goes on: the tyres.

  The Cadillac manual's note that more differential locking adds understeer under braking and acceleration makes a persistent exit push under clean technique a setup item, not a coaching one.
- **Present TC versus tyre wear as a trade-off,** measured from the driver's own stints (rear temperatures, lap-time fade), not as a settled fact [inferred].
- **Allow some exit slip.** A small, progressive slide at the best exit speed is the limit Driver61 describes. In the second stint of a double, though, it costs rear-tyre life [mine].
- **Scope the hybrid points.** They apply to the 963; the Valkyrie is unverified.

### Coasting, fuel saving and shifts

**Findings.**

- **Coasting, a conflict that resolves by phase.** HP Academy [PRO] says to minimise the gap between throttle and brake, because coasting is lost time ([HP Academy](https://hpacademy.com/courses/professional-motorsport-data-analysis/braking-performance-braking-technique)). Van Noy [PRO] goes straight to throttle in medium corners so the rear stays planted. The Racers360 coaches [PRO] say professional drivers do spend time coasting, while waiting to unwind ([Mazda Motorsports](https://www.mazdamotorsports.com/2020/02/25/driving-tip-1-the-top-mistakes-grassroots-race-car-drivers-make/)). The two sides describe different phases: before the brake, and between brake and throttle. Coach Dave [SIM] reads a gradual roll-off before braking as coasting too much ([Coach Dave, throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)).
- **Fuel saving.**
  - Lift and coast is the primary energy-saving method in IMSA GTP [PRO] ([Motorsport.com](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)).
  - A generic lap model saved 10% fuel for +0.411 s at Catalunya [SIM model, single-source] ([fastest-lap](https://fastest-lap.readthedocs.io/en/latest/blogs/blog_lift_and_coast.html)).
  - The earlier research found an LMU example at Spa of about 1.45 L saved for 0.7 s per lap. The technique taught: lift at a board, brake later, keep apex speed, and lift fully before braking ([Coach Dave, LMU](https://coachdaveacademy.com/tutorials/mastering-lift-and-coast-how-to-save-fuel-without-sacrificing-speed/)).
  - LMU guides add that lifting earlier regenerates less energy, and that short-shifting saves more engine energy [SIM, LMU, search-summary only] ([Traxion](https://traxion.gg/how-to-manage-virtual-energy-in-le-mans-ultimate/)).
  - The Cadillac manual's dash shows a fuel-per-lap delta and target but no virtual-energy readout, so iRacing's stint limiter is probably fuel [inferred] ([Cadillac GTP manual](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)).
- **Shifts.** HP Academy [PRO] calls inconsistent downshift blips and unsteady brake modulation, which lock the rears and destabilise entry, a driver technique issue ([HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)). Short-shifting is advised in the wet [SIM, search-summary only] ([Box This Lap](https://boxthislap.org/f1-23-from-dry-to-wet-tracks-unlocking-the-perfect-start-in-any-condition/)). Ken Hill, quoting John Andretti, says to ease off when a wet track spins the tyres [PRO] ([Blayze](https://blayze.io/blog/car-racing/finding-the-limit-on-a-wet-race-track)). Connor De Phillippi recalled wheelspin in fourth and fifth gear in the BMW GTP at Long Beach [PRO] ([Motorsport.com](https://www.motorsport.com/imsa/news/gtp-tire-challenges-allow-drivers-to-make-a-difference/10467756/)).

**Suggestions.**

- **Split coasting** into pre-brake (fuel saving or hesitation) and mid-corner (rotation or hesitation). Set the expectation by corner class: some mid-corner coasting in slow corners, little in medium ones [mine].
- **Mute pre-brake coasting while fuel saving.** Express a fuel target in the earlier report's form: lift N metres earlier, brake later, same apex speed.
- **Report brake-throttle overlap neutrally.** No source establishes a legitimate use.
- **Link entry instability to downshift timing.** The rear moving within a short window after a downshift is a downshift call, not a bias call [inferred].
- **Offer short-shifting** on cold tyres, in the wet and late in a double stint [inferred].

**Numbers.**

- About a tenth for on-off-on: rule of thumb, search-summary only.
- Above 95% as "full": forum.
- 61% and 68% full throttle: one anecdote, checked.
- 15–40% part throttle mid-corner: single-source, low-power cars ([Mental Apex](https://mentalapexracing.com/telemetry-guide/)).
- ~10% versus 6–7% optimal slip: road and ECU figures.
- TC level five or six on the 963: single-source SIM.

Application rate, apex-to-full-throttle distance, wheelspin share and coasting limits are all placeholders.

**Calls (suggested).**

- *Turn 11, wait for the unwind, then one squeeze to full.*
- *Turn 2, roll it on; the rear's stepping out.*
- *Turn 11, full throttle a car-length sooner.*
- *Turn 2 rear goes at the same spot every lap on a clean throttle: want one step more TC?* (an engineering offer, put as a question)
- *Rears are fading: short-shift out of 2 and 10.*
- *Turn 1, smoother on the pedal through the downshifts.*

For practice, Bentley's checked "Spend 3% more of the lap at full throttle" shows the awareness form ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)).

**Gaps.**

- No throttle-application targets for GTP, LMP2 or GT3.
- No pro driver describing exit technique in their own words.
- No link between slip and rear wear.
- No real-world TC schedule through a stint.
- The LMDh deployment floor and iRacing's deployment timing are unconfirmed.
- No source on brake-throttle overlap or left-foot braking.
- No cost for stabbing or coasting.
- Nothing on GTP shift points or over-revs.

A circulating "60–40–100 sawtooth" claim was not found on the pages checked and should not be used.

## Tyres and control: match the reference to the stint

**Findings.**

- **Choosing the reference.** Bentley [PRO] warns that a single lap "can be dangerous", and compares the fastest lap with three or four of the next fastest ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)). For consistency work he overlays five or so best laps ([Ask Ross](https://speedsecrets.com/q-how-close-should-my-lap-time-be-to-the-data-systems-theoretical-best/)).
- **Cold tyres in the real world**, the most-cited endurance hazard:
  - WEC Hypercar drivers called the 2023 cold-tyre out-laps dangerous, and Brendon Hartley's first-lap crash was described as a classic cold-tyre off [PRO] ([Motorsport.com](https://www.motorsport.com/wec/news/kobayashi-concerned-by-crazy-dangerous-wec-out-laps-on-cold-tyres-at-spa/10462097/)).
  - De Phillippi said GTP tyres took **11–13 laps** to switch on in one 2023 Long Beach qualifying session [PRO, single-source] ([Motorsport.com](https://www.motorsport.com/imsa/news/gtp-tire-challenges-allow-drivers-to-make-a-difference/10467756/)).
  - Racer reports GTP cars slower than GTD cars in corners for a few laps on cold tyres [PRO, search-summary only] ([Racer](https://racer.com/2023/09/16/solving-gtps-cold-tire-conundrum)).
  - Michelin targeted a 3–5 s first-lap gain for its 2026 tyre [PRO] ([Sportscar365](https://sportscar365.substack.com/p/insight-how-michelin-developed-its)).
- **Cold tyres in iRacing.** The 2025 GT3 tyre model starts tyres cooler, with peak laps typically on the **fourth or fifth flying lap** (a developer estimate reported by Coach Dave) [SIM, single-source, GT3]. Burnouts overheat the rears, and weaving adds little heat but more wear ([Coach Dave, 2025 tyre model](https://coachdaveacademy.com/announcements/the-2025-iracing-gt3-tyre-model-update-explained/)). **Conflict:** Fanatec [SIM] calls weaving the most popular warm-up method ([Fanatec](https://www.fanatec.com/uk/en/explorer/games/gaming-tips/tire-management-in-endurance-sim-racing/)). Box This Lap [SIM] found GTP braking distances changing over the first few laps ([Box This Lap](https://boxthislap.org/iracing-this-time-the-tyres-feel-alive/)), and says cold tyres do not tolerate a sudden hit of power [search-summary only] ([Box This Lap](https://boxthislap.org/iracing-mastering-cold-tyres/)).
- **The 2025 iRacing model** [SIM] is more forgiving of small slides and spins, but wears more for sustained pushing. Coach Dave says the GTP update came a few months before the GT3 one ([Coach Dave, 2025 tyre model](https://coachdaveacademy.com/announcements/the-2025-iracing-gt3-tyre-model-update-explained/)).
- **Traffic** pushes tyres out of their window, as Alpine's António Félix da Costa said at Le Mans in 2026 [PRO] ([Alpine](https://www.alpine-cars.co.uk/fia-wec/news/a-night-full-of-challenges-for-alpine-2026.html)).
- **Tyre temperatures.** Coach Dave [SIM] reads the middle against the edges for pressure (cool middle: too low; hot middle: too high) and inner against outer for camber. It notes that most iRacing cars give no live tyre data ([Coach Dave, tyre pressures](https://coachdaveacademy.com/tutorials/understanding-tire-pressures-in-iracing/)). iRacing's 2010 blog [SIM, dated] says readings spike with cornering load, cool in the pit lane and are spoiled by locks, spins or contact ([iRacing](https://www.iracing.com/hot-and-tired/)). AIM's iRacing guide [SIM] lists, per tyre, surface and carcass temperatures by left/middle/right, percent tread left and pressures, without saying which update live ([AIM](https://store.aimsports.com/download/doc/eng/simracing/iRacing_102_eng.pdf)).
- **G-G and balance.**
  - HP Academy [PRO, search-summary only] reads the transitions on a G-G plot, calls a straight chord between the braking and cornering peaks unused grip, and describes the egg shape (braking exceeds acceleration) ([HP Academy, G-G diagram](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-gg-diagram/)).
  - YDD [PRO] expects the combined-g peaks to be of equal height ([YDD](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)).
  - Two balance channels appear in the notes: steering-predicted against measured yaw rate [PRO, forum, search-summary only] ([MoTeC forum](https://forum.motec.com.au/viewtopic.php?p=7343)), and GPS-derived against gyro yaw rate [PRO, vendor, search-summary only] ([AiM](https://support.aimshop.com/donloads/on-track-session/Adria.pdf)).
  - HP Academy [PRO] says balance is always relative to another driver, setup or tyre set. Its car-side causes: mechanical imbalance, rearward brake bias, the aero centre of pressure moving forward, and tyre degradation ([HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)).
  - For the in-car levers, Box This Lap [SIM] uses a softer front anti-roll bar for rotation and a stiffer one for stability, more conservative on cold tyres and not changed lap to lap ([Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)).

**Numbers.**

- Inner tyre edge 6–10 degrees hotter than outer: forum, units unstated ([Overtake](https://www.overtake.gg/threads/question-about-tyre-temp.80015/)).
- Inner no more than about 7 °C over outer, and an optimum of 85–105 °C: low-authority site, search-summary only ([SimRacingSetup](https://simracingsetup.com/iracing/iracing-tyre-setup-guide/)).
- Hot pressures of 1.50–1.55 bar and 80–90 °C: iRacing GT3, not GTP ([Coach Dave, tyre pressures](https://coachdaveacademy.com/tutorials/understanding-tire-pressures-in-iracing/)).
- Michelin's 2.1 bar minimum hot pressure for Hypercars at Le Mans 2026: real world, single-source, not transferable to iRacing ([Motorsport.com](https://www.motorsport.com/lemans/news/le-mans-24-long-run-analysis-where-the-hypercars-stand-before-the-race/10829713/)).
- 11–13 laps and the fourth or fifth flying lap: one real qualifying session, and one GT3 developer estimate.

No GTP tyre window exists in the notes.

**Suggestions.**

- **Match the reference to the stint phase.** This is the largest structural change. In a 2h40 race the session-best lap is usually a fresh-tyre, light-fuel, clear-track lap, so tyre and fuel state read as lost technique [inferred]. Compare against the median of the best three to five clean laps in the same stint phase (mine, after Bentley's warning about single laps). Use three phases: the out-lap plus the first two to four flying laps; the body of a stint; the second stint of a double. Under the user's rule (tyres changed unless less than about 35 L of fuel is added), nearly every full stop creates a cold out-lap and a splash creates a double stint [inferred].
- **In the cold phase,** replace technique calls with warm-up guidance. Before restarts, remind the driver that the tyres are below their window [inferred].
- **Coach repeatable slip,** not one-off moments, which the 2025 model penalises less [inferred].
- **For tyre temperatures** [inferred]:
  - Remap telemetry left/right to inner/outer for each side before applying "inner slightly hotter". On left-side tyres L is the outer edge; on right-side tyres L is the inner edge. iRacing documentation does not confirm this.
  - Compare like with like: the same lap of the stint, and no cool-down lap.
  - Read spreads rather than absolute values.
  - Use the wear channels for a per-zone wear rate.
  - Tie temperatures to technique only through trends, such as hot fronts with rising steering-per-g [mine].
- **On the G-G plot,** add a per-corner transition dip (the lowest combined g between the braking and lateral peaks) and an overload spike, both against the reference. A notch toward the origin is a coasting gap [inferred].
- **For the balance index** [inferred]:
  - A true understeer angle (road-wheel angle minus wheelbase × yaw rate ÷ speed) needs the steering ratio and wheelbase, which the notes did not find. A ratio-free proxy is steering per unit of lateral g, compared only within one car, setup and tyre state.
  - A signature that repeats at one corner type at a similar entry speed, grows over the stint, or shifts with speed band points to the car.
  - One that comes and goes with turn-in point, entry speed or throttle timing points to the driver.
- **Judge lap-time fall-off fuel-corrected** [inferred].

**Calls (suggested; the first three adapted from the tyre researcher's drafts [inferred]).**

- *Tyres are cold for two more laps: brake early into 1 and 2, gentle on the power.*
- *Second stint on these tyres: no kerbs, no wheelspin.*
- *Same lap time with less steering through 5. That's tyre life.*
- *Restart: tyres are cold, leave margin into the first two braking zones.*

For practice debriefs: *Left-front middle hotter than its edges: pressure, not driving.*

**Gaps.**

- No GTP tyre temperature window, and no iRacing GTP laps-to-peak figure.
- No confirmation of which iRacing tyre channels update live.
- No lap-time degradation per lap for any class.
- No source on kerbs, on which IMSA tracks are front- or rear-limited, or on GTP G-G shapes.

## Radio and debrief: one item, earned numbers, external cues

**Findings.**

- **Method.**
  - Bentley [PRO] built a two-point plan from one lap, mostly from the speed trace, then warned that one lap can mislead and checked it against three or four of the next fastest. He refused another driver's lap as the reference: "Sure, that's the easiest way of finding speed, but it usually means you're just copying" ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)).
  - Sim tools [SIM] overlay laps by distance against pro, community or the driver's own laps ([Track Titan](https://www.tracktitan.io/post/how-to-analyse-telemetry-for-sim-racing); [VRS](https://virtualracingschool.com/academy/tag/replay/); [Coach Dave Delta](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/)).
  - YDD [PRO] asks the driver first. It lists failure modes of automated analysis, including invented reference laps and unsupported speculation about fatigue, and warns that per-corner gains are not additive ([YDD](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)).
  - In remote coaching, Bentley [PRO, search-summary only] treats the driver's feel as at least as important as the data ([Grassroots Motorsports](https://grassrootsmotorsports.com/articles/imsa-coach-ross-bentley-remote-coaching/)).
- **What to coach first: a conflict.** VRS [SIM]: "the priority for speed should be on the exit of the corner, then the entry, and finally mid-corner" ([VRS](https://virtualracingschool.com/academy/tag/replay/)). Krause [PRO, search-summary only] calls braking the greatest variable ([YDD](https://www.yourdatadriven.com/how-to-improve-braking-and-corner-entry/)).
- **How many items.** Bentley [PRO] focused the driver on "just two things", would ideally have split them across two sessions, and asked for a small change. The result, a little more than 3 s at Watkins Glen, is one anecdote [single-source] ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)).
- **Consistency gate.** Bentley [PRO] says "A half second off your theoretical is a good goal," and "Being a second or more from your theoretical is starting to point at too many inconsistencies" ([Ask Ross](https://speedsecrets.com/q-how-close-should-my-lap-time-be-to-the-data-systems-theoretical-best/)). A karting vendor uses a tenth [search-summary only] ([Purpl](https://purpl.app/blog/lap-consistency-karting/)).
- **Delivery.** Bentley's two instructions were "Spend 3% more of the lap at full throttle" (a number, no place) and "Experiment with the timing & rate of release of the brakes – focus on Turns 6, 7, 8, 9" (a place and an input, no value). He adds: "I didn't actually tell him what exactly to do… I had simply made him aware of a few things, then asked him to be more aware of two things while driving" ([Bentley](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)). Scott Gardner [PRO] asks "What are you going to do now?" rather than giving orders ([YDD](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)). Delta and Track Titan [SIM, vendor claims] give tips tagged by corner phase, with percentages ([Coach Dave Delta](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/)). YDD [PRO]: "It's also important to celebrate the positives." Give gains as ranges.
- **Focus of attention.** A 2021 meta-analysis (Chua and colleagues, *Psychological Bulletin*) [RESEARCH] found an external focus beats an internal one for both performance and learning. External means the effect of the movement, such as the car or a track point; internal means the body ([UNLV repository](https://digitalscholarship.unlv.edu/kns_fac_articles/424)). One simulated-driving study [RESEARCH, search-summary only] found both kinds helped under pressure ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3488937)).
- **Radio practice** [PRO, search-summary only]: keep it as simple as possible ([Red Bull Racing](https://www.redbullracing.com/int-en/bulls-guide-to-team-radio)), speak on straights rather than at braking points ([The SportsRush](https://thesportsrush.com/f1-news-how-does-f1-team-radio-work/)), use one voice ([F1 Briefing](https://f1briefing.com/who-talks-to-f1-drivers-during-races/)), and keep radio silence at high-pressure moments ([F1 Briefing](https://f1briefing.com/how-f1-teams-use-radio-for-strategy/)). The earlier research adds two points. Mercedes' Andrew Shovlin says talk in corners costs drivers braking points, and information should come when the driver can act on it ([Autosport](https://www.autosport.com/f1/news/the-secrets-of-in-race-radio-chat-5102490/5102490/)). Porsche names the action wanted rather than the one to avoid ([Porsche Newsroom](http://newsroom.porsche.com/en/motorsports/tests-in-monza-10499.html)).
- **Capacity.** Scott Mansell [PRO] says traffic uses up the mental capacity a driver needs for conscious technique, so drivers revert to habit ([YDD](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)).
- **Products and racecraft.** Voice race-engineer products advertise cooldowns between calls [SIM, vendor, search-summary only] ([AI Race Engineer](https://airaceengineer.com/); [PitWise](https://pitwise.net/)). In multi-class racing [SIM, search-summary only], losing as little time as possible when being passed beats fighting side by side ([LVRY](https://lvry.co/multi-class-racecraft/)).

**The format conflict.** The first option is location + action + number: the format sim tools use, and close to the earlier report's template (attention word, one fact, one action). It is fast to parse and easy to check. The second is Bentley's awareness-first approach, with Gardner's questions. It builds the driver's own model of the car and avoids a number that fits the data but not the driver. No source tested one against the other.

**Suggestions (mine).** Resolve the conflict by context:

- **On race radio:** use location + input + direction. Add a number only when it is earned: the same deviation on at least three of the last five clean laps (after Bentley's three or four laps). Use only units the driver can act on at speed: a board, a car-length, a gear, metres. Pedal percentages and steering degrees belong in the debrief.
- **In practice:** use Bentley-style experiments on one input across a few named corners.
- **In the debrief:** ask first, explain why, celebrate what worked, and show the chain.

How to phrase and pace calls:

- Phrase cues externally (the kerb, the board, what the car does) and positively.
- Hold one active item, chosen by the chain rule, until it is confirmed over three to five clean laps or abandoned. Confirm out loud when it lands.
- Do not stack items, and apply a cooldown per corner.

What to prioritise and when to stay quiet:

- In a race, rank items that protect the stint (lockups and flat-spot risk, repeated rear slides) above the largest repeatable time loss. Break ties toward exits onto long straights, following VRS's reasoning.
- Mute technique calls in traffic, on out-laps (give warm-up guidance instead), during fuel saving (for coasting), and while the driver is a second or more off their theoretical best, when consistency comes first.
- In multi-class running, favour low-risk changes (release, throttle timing) over moving brake points [inferred].
- Never add up per-corner gains (YDD).

**Gaps.**

- No verbatim radio calls from a pro driver coach.
- No test of call formats.
- No statistical rule for when a change has worked.
- Nothing on coaching across co-drivers sharing a car, or on how to word endurance traffic calls.
- Jorge Segers' data-analysis book and Bentley's minimum-speed table were not reached.

## Where the sources disagree

The table collects the conflicts flagged above. The handling column is my suggestion.

| Question | One side | Other side | Handling (mine) |
|---|---|---|---|
| Migration convention | iRacing GTP: base bias at 100% pedal, migration added toward 0% [SIM, official] | LMU (Traxion): base at low pedal, forward shift at 100% travel [SIM, LMU] | Use iRacing's; never port LMU numbers; confirm the sign in the garage |
| Migration on or off | 2.5F "optimal for all Hypercars" [SIM, LMU, single-source] | Disabled as a Valkyrie baseline [SIM, LMU, search-summary only] | Neither source is iRacing; start from the car's default |
| Bias direction | Forward = stability and understeer (every other source) | Reversed in one fetched summary of the 963 article | Discard the reversal |
| Time to peak pressure | ~0.45–0.47 s, pro IMSA LMP-C [PRO, single-source, search-summary only] | ~0.2 s yardstick; under 0.4 s target | Judge only against the driver's own laps |
| Peak pedal % in iRacing GTP | 85–90% [SIM, vendor, search-summary only] | Same article wrong on ABS; pedal % depends on setup | No absolute target |
| Does TC save rear tyres? | No: TC pulses wear more than a smooth roll-on [PRO, motorcycle, single-source, search-summary only] | Yes: higher TC saves tyres [SIM, search-summary only]; lower TC wears more [SIM, forum]; TC off lets a skilled driver manage spin [SIM] | A trade-off to measure on the driver's own stints |
| Optimal wheelspin | ~10% [PRO, search-summary only] | 6–7%, with 1–3% creep [PRO, road tyres, search-summary only] | The driver's own clean-exit baseline |
| Call format | Location + action + number (sim tools; the earlier report's template) | Awareness first with no prescribed value (Bentley); questions (Gardner) [PRO] | Race: place + input + direction, number when earned; practice: awareness |
| Turn-in rate | Quick and crisp in tight corners (Bentley) [PRO] | Slow first, then firmer (Mullan) [PRO, single-source] | Compatible if "quick" means a short time to lock |
| Throttle before unwind | Not until the wheel starts to unwind [PRO] | Earlier helps some cars [PRO, search-summary only]; no fixed throttle point (Bentley) | Judge by time to committed full throttle |
| Coasting | Minimise it [PRO]; none in medium corners [PRO] | Pros coast while waiting to unwind [PRO] | Classify by phase and corner class |
| What to coach first | Exit, then entry, then mid-corner [SIM] | Braking is the greatest variable [PRO, search-summary only] | Chain rule picks the item; the time delta weights it |
| Consistency gate | ~0.5 s from theoretical best [PRO] | ~0.1 s [PRO, karting vendor, search-summary only] | Bentley's figure for GTP stints |
| Focus of attention | External beats internal (meta-analysis) [RESEARCH] | Both helped under pressure in simulated driving [RESEARCH, search-summary only] | Prefer external cues without over-claiming |
| Out-lap weaving | The most popular warm-up method [SIM] | Little heat, more wear in iRacing's 2025 model [SIM] | Follow the iRacing-specific source |
| Brake temperature window | ≥200 °C, ~400 °C average, >1,000 °C peaks [PRO] | 250–850 °C [PRO, search-summary only] | Context only; iRacing's modelling unknown |
| LMDh deployment floor | Deploys from 0 km/h | Only above 120 km/h [both search-summary only] | Check each iRacing car |

## Conclusion

The research changes what the assistant should be more than it changes any threshold. It moves the assistant from a set of one-sided detectors measuring "worse than the best lap" to a diagnostic. That diagnostic classifies each departure by direction and cause, along the brake-to-throttle chain, against a reference from the same stint phase. In that framing the missing numbers matter less. The driver's own lap-to-lap spread decides whether a departure is real, and the chain decides which departure earns the single radio call. The same rule is the tyre argument: fixing the earliest mismatch removes slip at both axles, the fronts at entry and the rears at exit. And because iRacing's migration depends on pedal position, coaching the brake release and advising on bias are one decision, not two. An assistant that treats them separately will contradict itself.

The cheapest evidence the literature lacks is evidence the assistant can generate itself. Does coaching the earliest departure make the downstream flags fade within three to five clean laps? Logged per corner, that test would turn the chain rule from inference into a measured result for this driver and these cars. Outside research is still needed to settle the inputs the inference rests on. The Porsche 963 and Valkyrie manuals should give the migration sign and ramp, the TC semantics, and regen and powertrain behaviour. And it remains to be checked whether iRacing exposes wheel speeds and steering torque, which would turn inferred lockups, wheelspin and front-limit detection into measured ones.
