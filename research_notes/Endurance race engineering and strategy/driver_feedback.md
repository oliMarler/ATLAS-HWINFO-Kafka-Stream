# Driver Feedback in Racing: Vocabulary, Structure, Setup Mapping, Stint Evolution, Multi-Driver Programmes, Coaching Tone

Research caveat: web search returned mostly secondary and sim-oriented material. Many pages (ESPN, Winding Road, getcarcurious transcript, Ferrari) could not be fetched in full. Items under "Inferences" are general vehicle-dynamics/engineering knowledge or reasoning, NOT sourced in this research; treat as unverified and cross-check before shipping. Sim-specific material is labelled.

## 1. How drivers describe balance and handling (vocabulary)

### Takeaway
Core vocabulary is consistent: "push/tight" = understeer, "loose" = oversteer, split by corner phase (entry/mid/exit) and speed class. Sourced material on the finer terms (snap, lazy, numb, nervous, platform, pitch/heave) was not found; those definitions are given only as inference.

### Cited Findings
- Drivers say the car "has a push" or "is tight" for understeer and "is loose" for oversteer; NASCAR uses loose/tight as standard terms. — [Racer.com racerpedia](https://racer.com/racerpedia/racing-101/what-are-oversteer-and-understeer) (as summarised by search; page not fully read)
- Corners are split into entry, mid-corner and exit; one source states ideal is mild understeer on entry (stabilises brake-to-throttle transition) and just enough oversteer on exit for directional control. — [SimXPro guide](https://simxpro.com/en-us/blogs/guides/understeer-vs-oversteer-how-to-diagnose-it-and-fix-it-in-one-corner) (sim vendor, single source). An F1 forum view differs: slight understeer on exit maximises tyre traction — [f1technical forum](https://www.f1technical.net/forum/viewtopic.php?p=158953) (forum opinion).
- Entry understeer often starts with braking and turn-in timing; exit oversteer is usually throttle timing and steering rate (driver cause before car cause). — [SimXPro](https://simxpro.com/en-us/blogs/guides/understeer-vs-oversteer-how-to-diagnose-it-and-fix-it-in-one-corner)
- Too much front brake bias stops the car turning in (entry understeer); abrupt brake release while steering to the apex lets the rear keep rotating past the apex. — [Speed Secrets understeer Q&A](https://speedsecrets.com/q-how-can-i-reduce-the-amount-of-understeer-i-experience-with-my-driving-technique-or-cars-setup/) (search summary)
- A PCA slide deck lists: entry understeer from abrupt brake release; exit understeer from too much throttle too soon; too-stiff front roll bar makes understeer grow through mid-corner into exit. — [PCA "Car Balance" PDF](https://nnjr-pca.com/wp-content/uploads/2024/04/Car-Balance.pdf) (search summary)
- Engineers' "understeer-snap-oversteer" label: mid-corner understeer that turns to oversteer on exit, attributed in the anecdote to the driver adding steering when they should ease it. — search summary of [Speed Secrets](https://speedsecrets.com/?p=44157) (single source, anecdote)
- Ross Bentley (via Winding Road) describes Jeff Braun's (CORE autosport) method around "the terms and phrases drivers use to describe how their cars are handling", and says good engineers do not want drivers to dictate setup changes. — [Winding Road via search summary](https://windingroad.com/articles/features/speed-secrets-getting-the-most-out-of-driver-feedback/) (page returned 403; only snippet seen)
- IndyCar engineer Anderson: a driver asking for more front grip must say where (e.g. low vs high speed), since moving aero balance forward may make the car undriveable in fast corners. — [Motorsport.com](https://www.motorsport.com/indycar/news/ripple-effect-engineering-Arrow-SPM/4480010/) (search summary)
- Romain Grosjean: the chain is feeling -> words -> terms the engineer can map to data; language and level of detail matter. — [ESPN](https://www.espn.com.au/f1/story/_/id/22433084/inside-vital-relationship-f1-driver-engineer) (search summary; fetch failed)

### Inferences
(General knowledge, unsourced here.)
- Speed class: low-speed (<~100 km/h) problems are mostly mechanical (springs/ARB/diff/TC/brake bias); high-speed problems mostly aero/platform (wing, ride height, rake, dampers).
- "Snap" = sudden loss of rear grip with little warning (often lift-off or trail-brake, or curbs); "lazy/slow to rotate" = delayed yaw response at turn-in; "nervous/twitchy" = high yaw response, unpredictable; "numb/dead" = steering lacks feedback (front grip near limit/overheated tyre or high aero load); "on the nose" = pitched forward, front loaded under braking/entry; "platform" = ride height/pitch stability controlling aero; "pitch/heave" = braking/accel and downforce-driven vertical motion (damper, bump-stop, spring territory); "rotation" = willingness to yaw into the corner; "traction" = ability to put power down on exit; "braking stability" = rear stays behind the front under hard braking.
- For a radio-listening assistant: parse (symptom word) + (phase) + (corner or speed class) + (severity); if any missing, ask one clarifying question.

### Gaps
- No authoritative glossary from Rouelle, Haney, Milliken or Racecar Engineering was retrievable. Term definitions above are unsourced.
- No GTP/Hypercar driver-specific slang found.

## 2. Structuring driver feedback; what engineers ask; driver vs car

### Takeaway
Useful feedback is specific to corner/condition, listed and prioritised, with the driver reporting car behaviour rather than prescribing changes. Engineers use debriefs corner-by-corner and data to confirm. A sourced scale/A-B protocol was not found.

### Cited Findings
- Tom Long (driver): tie feedback to specific corners/conditions (e.g. unsettled entering a high-speed corner), write points as an organised list, give on-track feedback so changes happen at the next stop, use full pit debrief when time allows; short sessions favour on-the-fly feedback. — [Tom Long Racing](https://tomlongracing.com/2020/03/05/answering-your-questions-turning-feedback-into-adjustments/)
- Tom Long's mapping examples: rear unsettled in fast corners -> lower rear or more rear wing; understeer -> lower/soften front. (Single source, generic.) — same page. The page does not address ruling out driver technique first.
- Engineers want how the car feels and what the driver wants changed, then check data for why. Debriefs: engineer questions driver corner by corner. — [Winding Road via search summary](https://windingroad.com/articles/features/speed-secrets-getting-the-most-out-of-driver-feedback/)
- Ferrari WEC driver Pier Guidi: feedback after simulator sessions mirrors track feedback, including setup/component suggestions. — [Ferrari Hypercar](https://ferrari.com/en-ES/hypercar/articles/wec-cota-2024-tech?amp=true) (search summary only; fetch empty)
- Renault (F1) drivers take turns leading feedback sessions so all voices are heard; many drivers are distracted by engineer talk mid-corner. — via search summary of [Autocar](https://www.autocar.co.uk/node/87210) / [getcarcurious](https://getcarcurious.com/episodes/the-art-of-communicating-with-f1-drivers-a-race-engineer-shares-his-secrets) (unverified detail; single-source)
- iRacing GTP guide (SIM): feedback becomes useful when it is repeatable: same phase in same corner type, front lock under heavy braking consistently, rear nervous every brake release; do not change several parameters at once. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- Same guide (SIM): "Car feels fine but lap times don't come" means work on technique first; avoid reacting to one corner rather than several braking zones. — same page.

### Inferences
- 1-10 scales and A/B comparisons are standard engineer practice but not sourced here; for the assistant, accept "bit/lot/massive" and numeric scales and normalise.
- Driver vs car test: is the issue repeatable across laps and corners of the same type, does data (steering angle, brake release rate, throttle trace) show a driver input cause, and does it vary with driver? One-off errors should not trigger a change.
- Assistant rule: one change per request, confirm result next lap(s), and ask "which corner/phase?" when absent.

### Gaps
- No sourced engineer question lists, no sourced 1-10 scale protocol.
- Jeff Braun / Bentley article text not retrieved.

## 3. Mapping feedback to changes

### Takeaway
Sourced mapping is thin and mostly sim-guide level. In-car adjustable items on modern prototypes are brake bias (with migration), ARBs, TC and similar; direction rules below for brake bias/ARB/TC are sourced to sim guides only.

### Cited Findings
- Setup requests in WEC go through track engineer/lead mechanic; engineers cannot change engine settings via telemetry; driver makes in-car changes via wheel/dash controls. — [24h-lemans.com](https://24h-lemans.com/en/news/from-chalk-to-talk-how-driver-pit-communications-have-evolved-at-the-24-hours-of-le-mans-57062)
- (SIM, iRacing GTP) Bias forward = more braking stability; rearward = more rotation on entry. Front locks first -> bias rearward; rear locks first -> bias forward. Bias is driver-specific, do not copy teammates' numbers; small corrections as tyres wear. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- (SIM) Brake bias migration: more stable at peak pedal pressure, more rotation as pressure drops; example values -3 to -5; use once braking is consistent. — same.
- (SIM) Softer front ARB increases rotation; stiffer favours stability/understeer; some run conservative ARB on cold tyres then change. Rule of thumb: softer front or firmer rear ARB reduces understeer. — same; [Box This Lap cheatsheets](https://boxthislap.org/cheatsheets/amp/)
- (SIM) TC: too much intervention hurts acceleration, too little gives exit wheelspin; use lowest intervention you can drive consistently; start conservative, loosen when tyres warm, tighten with wear; TC cuts over bumps/kerbs cost fuel. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- (SIM, LMU LMGT3, not Hypercar) bias forward on cold tyres then rearward when warm; higher TC on cold tyres; lowering TC slip/power helps on-throttle rotation. — [SimRacingCockpit](https://simracingcockpit.gg/le-mans-ultimate-how-to-drive-the-lmgt3-and-hypercar/)
- (SIM, GT title forum, anecdotal) once ABS is active, bias has little effect; bias changes can alter perceived mid-corner balance. — [GTPlanet](https://www.gtplanet.net/forum/threads/brake-balance.372919/), [GTPlanet](https://www.gtplanet.net/forum/threads/is-brake-bias-faked.369707)

### Inferences
(Unsourced general knowledge.)
- Suggested step sizes for an assistant: brake bias 0.5-1.0% per change; ARB one click/step per request; TC one step; wing/springs/dampers/ride height are garage-only (not in-race except at stop where rules allow, and in iRacing generally not changeable on pit stop beyond tyres/fuel/wing in some cars: verify per car).
- Symptom table (starting point): entry understeer -> bias rearward (if front locking) or softer front ARB; entry oversteer/rear unstable on braking -> bias forward; mid-corner understeer low speed -> soften front ARB/stiffen rear; mid-corner high speed push -> aero (front wing/rake) not ARB; exit oversteer -> TC up or stiffer front/softer rear ARB; exit wheelspin -> TC up.
- Typical misreads: treating technique-driven symptoms as setup; changing bias to cure mid-corner balance; chasing a cold-tyre issue with a permanent change; treating "loose" as the same on entry and exit.

### Gaps
- No sourced real-world GTP/Hypercar ARB or TC adjustment ranges; no sourced damper mapping (pitch/heave); iRacing GTP guide does not cover ABS or dampers.

## 4. Changes over a stint/race; combining feeling with data

### Takeaway
Grip falls with tyre wear so bias/TC/ARB need small stint updates; sourced detail is sim-level. Data-combination specifics (understeer angle, balance index) were not found.

### Cited Findings
- (SIM) Grip drops as tyres wear, settings may need small updates; practise full-stint runs; prefer a setup that is not tiring over a full stint. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- Onboard data logs suspension/damper action, tyre temps, driver inputs matched to track position within about a metre; real-time telemetry streams in-stint. — [24h-lemans.com](https://24h-lemans.com/en/news/from-chalk-to-talk-how-driver-pit-communications-have-evolved-at-the-24-hours-of-le-mans-57062)
- Engineers tell drivers per turn whether laps are consistent/slower. — same.
- Engineers use data to see why the car does what the driver describes. — Winding Road via search summary (above).
- OptimumG courses cover relating driver feedback to logged data and driver KPI analysis (grip, balance, control, stability). — [Auto123](https://www.auto123.com/en/news/amp/optimumgs-vehicle-dynamics-and-data-acquisition-3-day-seminar-in-montreal/34798/) (search summary)

### Inferences
- Fuel burn lightens the car and shifts balance (usually less understeer/more rotation); tyre wear typically moves balance by axle depending on which degrades faster; track temperature/rubbering changes entry vs exit. Assistant should ask "different from the start of the stint?" and bias toward small, reversible changes.
- Data cross-checks to compute from iRacing telemetry: steering angle vs expected from yaw rate (understeer gradient), per-corner min speed, brake pressure vs lock-up, tyre temp/pressure by axle, fatigue indicators (rising lap-time variance, steering corrections).

### Gaps
- No sourced balance-index or understeer-angle definitions; no fatigue or traffic studies found.

## 5. Multi-driver programmes and debriefs

### Takeaway
Sourced evidence: fewer drivers = less setup compromise and more engineer time; teams factor in drivers' feedback style and setup preferences when forming crews. Handover note practice not found.

### Cited Findings
- Porsche's Urs Kuratle: two-driver crews mean "one less opinion when setting up the car, so there's less compromise"; WEC weekend has four hours of free practice. — [The Race](https://www.the-race.com/endurance/the-dilemma-surrounding-wec-driver-crews/)
- Third driver may arrive less prepared; experienced drivers can keep developing the car, but the third must be integrated (Tarquini). — same.
- Genesis analysed drivers' test feedback including how they gave it; Peugeot grouped drivers by setup preference. — [Racer.com](https://www.racer.com/2025/12/05/genesis-confirms-driver-combinations-for-inaugural-hypercar-season) and [Pit Debrief](https://www.pitdebrief.com/?p=100730) (search summaries)
- (SIM) Brake bias is driver-specific; do not copy another driver's setting. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- Radio lets drivers warn the next driver and flag problems for the next stop. — [24h-lemans.com](https://24h-lemans.com/en/news/from-chalk-to-talk-how-driver-pit-communications-have-evolved-at-the-24-hours-of-le-mans-57062)

### Inferences
- For a sim assistant: store per-driver profiles (preferred bias, TC, ARB) separately from the shared setup; on handover, report current in-car settings, tyre state, and the last 2-3 notable behaviours.

### Gaps
- No sourced handover-note formats, written debrief templates, or video-debrief practice.

## 6. Giving feedback to the driver

### Takeaway
Sourced points are limited: keep radio calm, avoid talking mid-corner, give consistency/pace updates. One-point-per-message is inferred.

### Cited Findings
- Engineers avoid talking during corners because many drivers are distracted. — search summary of [Autocar](https://www.autocar.co.uk/node/87210) (not verified in full)
- Hamelin (Racing Bulls engineer) episode topics: timing and content of radio messages, lap/gap updates, filtering technical detail, keeping radio calm, structured debriefs, building trust. Specific advice not accessible (transcript behind sign-in). — [Get Car Curious](https://getcarcurious.com/episodes/the-art-of-communicating-with-f1-drivers-a-race-engineer-shares-his-secrets)
- Track engineers give per-turn feedback on consistency, push/hold, track position and traffic calls. — [24h-lemans.com](https://24h-lemans.com/en/news/from-chalk-to-talk-how-driver-pit-communications-have-evolved-at-the-24-hours-of-le-mans-57062)
- Bentley's Speed Secrets 4 targets those supporting the driver on communicating to bring out best performance (listing only). — [Barnes & Noble listing](https://www-test.barnesandnoble.com/w/speed-secrets-4-ross-bentley/1112011253)
- (SIM) Chasing setup tenths while large gaps remain in braking, releases, throttle is a common mistake. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)

### Inferences
- Rules for the coaching assistant: one actionable point per message; deliver on straights, not in braking zones or corners; short imperative ("Brake a touch later into T1") plus one reason; positive framing ("good exit, now carry more speed"); never contradict a prior instruction without retracting it; defer detail to a post-stint debrief; limit frequency to avoid overload.
- Failure modes: info overload mid-corner, contradictory advice, nagging repeated cues, blaming driver when data points to car.

### Gaps
- No sourced examples of phrasing or evidence on what sticks; no transcripts of real radio compilations retrieved; no quotes included to avoid invention.
