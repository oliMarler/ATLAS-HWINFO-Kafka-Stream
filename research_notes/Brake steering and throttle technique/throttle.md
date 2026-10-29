# Throttle Control for Endurance Racing (GTP/Hypercar, LMP2, GT3): Technique, Telemetry Markers and Coaching

Legend: **[PRO]** = real-world professional source (coach, engineer, driver, series/tyre/data-system maker). **[SIM]** = sim-racing source (iRacing manuals, sim coaching sites, sim forums). **[single-source]** = only one source found for the claim. **[snippet]** = taken from a search-result summary because the page was not fetched or the fetch failed (403/429); wording may not be verbatim. Everything under "Inferences" is my reasoning, not sourced. No numbers below are invented; where a source gives no number, none is given.

## 1. Corner exit: when to start the throttle, how fast to build it, maintenance throttle, earliest full throttle, exit speed down the straight

### Takeaway
The professional consensus is that the target is not the *earliest touch* of the throttle but the *earliest point of committed 100%* with no lift afterwards. Application should rise with steering unwind (more throttle as lock comes off), be progressive rather than a stab, and be built up lap by lap until the rear just begins to slide. An early pick-up that has to be backed off ("on-off-on") costs time, and a pick-up that has to wait until well past the apex usually points back to too much entry speed.

### Cited Findings
- [PRO] Ross Bentley, *Speed Secrets 365*, Day #186: "Apply the throttle at the point where you don't have to ease off it when exiting the corner. If you begin applying the throttle too soon, resulting in having to ease back up off of it before going to full throttle, you will lose a tenth of a second." The "tenth" is Bentley's rule of thumb, not a measured figure. [snippet] — [Speed Secrets 365 PDF](https://speedsecrets.com/wp-content/uploads/2025/07/Speed-Secrets-365-v1.1-6-1-25.pdf)
- [PRO] Bentley's "If-Then" rules on throttle timing (verbatim from the fetched page):
  - "If you can begin to apply the throttle early in the corner" then "you probably over-slowed."
  - "If you have to wait until you're well beyond the apex before starting to apply the throttle…" then "you probably (but there are exceptions to this) carried too much entry speed."
  - "If someone tells you that you should always begin applying the throttle at the apex of a corner… then ignore them."
  - "If you're inconsistent with where you begin to apply the throttle in corners…" then "you probably don't have enough references and/or your braking is inconsistent." — [Speed Secrets: If-Then… Revisited (Substack)](https://rossbentley.substack.com/p/speed-secrets-if-then-revisited)
- [PRO] A search summary credits Bentley with the line "It isn't how early you touch the gas pedal, but how soon you can get to full throttle," and with saying early partial throttle helps only if it does not delay full throttle. The fetched If-Then page listed only the four rules above, so where this line comes from is unconfirmed. [snippet] — [Speed Secrets: If-Then… Revisited](https://rossbentley.substack.com/p/speed-secrets-if-then-revisited)
- [PRO] Bentley on point-and-shoot corners: "your min speed is not as important as how early you can get to full throttle when exiting out of corners." [snippet] — [Hagerty: Racing 101 #1, Ross Bentley on momentum](https://www.hagerty.com/media/motorsports/racing-101-1-ross-bentley-on-momentum/)
- [PRO, coaching theory] Driver61 (exit phase), all quoted:
  - The brake-to-throttle handover comes just before the apex: move "very gently from the brake pedal to the throttle."
  - Throttle is tied to steering unwind: "Continue to add more throttle as you open up the steering angle."
  - Against stabbing: "any sharp inputs will cause a premature loss of traction."
  - Finding the limit lap by lap: "increasing your throttle input each lap until you feel the car begin to break traction". The slide should be "progressive and more importantly, predictable."
  - Exit speed: the exit phase "controls how much speed we carry onto the following straight," and "any extra momentum we take onto the straight accumulates to a significant reduction in lap time."
  - The article gives no numeric timing or percentages. — [Driver61: Maximising the Exit Phase](https://driver61.com/uni/corner-exit/)
- [SIM] Coach Dave Academy (Delta throttle-trace guide):
  - "The goal is to get to full throttle as soon as possible, where you do not have to release the throttle again."
  - Applying power with steering lock still on can cause understeer. The warning sign is a trace that rises earlier than the reference lap while the delta is still growing.
  - "If you see an acceleration trace that rises, dips, and then rises again," the power is going on in the wrong phase of the corner.
  - A late trace can mean top speed is never reached on long straights.
  - Compare three things against a reference: when the pedal moves, the slope (aggression) and the smoothness (efficiency).
  - No numeric thresholds are given. — [Coach Dave: How To Use Throttle Traces To Improve](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)
- [SIM] Mental Apex Racing:
  - Recommends a smooth, progressive ramp back to 100% on exit, and says the faster lap usually has the smoother trace.
  - A "jagged or stepped line" signals stabbing or abrupt corrections.
  - "Partial throttle (15-40%) through mid-corner" is described as normal in low-power cars (MX-5, Formula Vee). This is not GTP-specific. [single-source for the 15–40% band] — [Mental Apex: How to Read iRacing Telemetry Charts](https://mentalapexracing.com/telemetry-guide/)
- [SIM] VRS treats maintenance throttle as a balance tool. After an abrupt mid-corner lift, "quickly reapply some maintenance throttle to shift the weight transfer back to its original balance." VRS calls reducing throttle "the most effective method" for correcting understeer. — [VRS 3.3: Fundamentals: Car control](https://virtualracingschool.com/academy/iracing-career-guide/second-season/car-control/)
- [SIM] iRacing Cadillac V-Series.R GTP manual, Throttle Shape setting:
  - "Setting '1' is purely linear, with a given percent of throttle delivering a similar percentage of max torque (25% throttle = 25% torque)."
  - Higher settings behave "similar to a butterfly-style throttle: less torque increase at very low and very high throttle percentage and more torque increase in the throttle's mid-range."
  - It "will change the feel of the car when throttle is initially applied."
  - The dash shows "PEDAL: Current throttle pedal torque map setting." — [iRacing Cadillac V-Series.R GTP User Manual (PDF)](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)
- [SIM] iRacing Porsche 963 GTP guide on exits: "Patience then is a virtue before asking for the power to accelerate from the bend." The guide relates this to the car's heavy nose. — [Coach Dave: iRacing Porsche 963 GTP Guide](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)

### Inferences
- For the assistant, the primary exit metric should be the distance (or time) from the apex to sustained ≥~95% throttle with no subsequent lift until the braking zone. Time to first throttle is secondary. Use the minimum-speed point as the apex proxy, and take the steering-unwind start from the moment |steering| begins to fall after its peak. Bentley's rule implies an early first touch is only good if the time to committed full throttle does not get worse.
- Diagnosis follows Bentley's If-Then logic. A very early first touch suggests over-slowing on entry. A first touch well past the apex suggests too much entry speed or a late apex. Scattered pick-up points lap to lap suggest weak reference points or inconsistent braking, so check brake-release consistency before coaching the throttle itself.
- Throttle % is not torque % on a GTP with a non-linear Throttle Shape. When throttle traces are compared across setups, cars or drivers, the pedal-map setting must match or be accounted for. A 40% hold on a high Throttle Shape setting produces more torque than 40% on setting 1.
- Exit speed carry can be measured as speed at fixed lap-distance offsets after the corner (e.g. +100 m and +300 m) against the reference lap. A deficit that persists or grows down the straight is an exit loss. One that closes is just a different line. The offsets are illustrative, not sourced.

### Gaps
- No source gave quantitative targets for throttle application rate (%/s), or for the typical apex-to-full-throttle distance, in GTP/Hypercar, LMP2 or GT3 cars. Any thresholds the assistant uses must come from the driver's own best laps or reference laps, not from literature.
- No prototype or GT pro driver interview describing exit throttle technique in their own words was found. Carroll Smith (*Drive to Win*) and Skip Barber (*Going Faster*) were not reachable in full text, so nothing is quoted from them.

## 2. Wheelspin and traction: how it shows in data, what it costs the rear tyres, how TC interacts with the driver, hybrid deployment effects

### Takeaway
Wheelspin shows up as driven-wheel speed (or engine rpm divided by the gear ratio) running above the undriven-wheel or vehicle speed. Sources disagree on the optimal slip figure (6–7% on road tyres vs about 10%), and small slip values include normal tyre creep. iRacing GTP traction control has two settings: Gain (how hard it cuts) and Slip (how much spin it allows before acting). Sim coaching advises adjusting TC through the stint as fuel burns, the tyres wear and the track rubbers in. The claim that TC pulsing wears tyres more than a smooth roll-on has only one source (a Michelin remark about motorcycles), and sim sources contradict it. iRacing's GTPs are LMDh cars, whose hybrid drives the rear axle, so deployment adds to the torque the rear tyres must put down on exit.

### Cited Findings
- [PRO] Traction-control logic compares driven and undriven wheel speeds: the ECU "can look at the difference and calculate the percentage of slip." Maximum acceleration is "achieved with somewhere around 10% wheel slip." [snippet] — [HP Academy: How Traction Control Works](https://www.hpacademy.com/blog/how-traction-control-works/)
- [PRO] Hondata puts optimum dry slip at about 6–7%, which conflicts with HP Academy's ~10%. It warns that "slip ratio is not the same as wheel spin": tyre creep under torque produces a few percent of slip with no real spin, so a 1–3% driven-vs-undriven difference on a street tyre may not be wheelspin. These are road-car figures, not race slicks. [snippet] — [Hondata: Traction Control, slip ratio](https://www.hondata.com/help/tractioncontrol/theory_of_operation.htm)
- [PRO, data-system practice] A MoTeC M1 example computes the "zero slip" RPM from undriven wheel speed and gearing, then sets a rev limit slightly above it to target a chosen slip. This is the same rpm-vs-ground-speed comparison a coach can run after the fact. The search summary did not tie this cleanly to one URL; it appeared alongside the HP Academy result. [snippet] — [HP Academy: How Traction Control Works](https://www.hpacademy.com/blog/how-traction-control-works/)
- [SIM] A forum MoTeC i2 analysis computes slip as (wheel speed − vehicle speed) / vehicle speed, positive under acceleration, with the undriven fronts taken as vehicle speed (zero slip = free rolling). The poster also saw driven-wheel slip dip below zero under acceleration and blamed a measurement artefact. That is a forum hypothesis. — [GTPlanet: Tire analysis with MoTeC i2](https://www.gtplanet.net/forum/threads/tire-analysis-with-motec-i2.325922/)
- [SIM] iRacing Cadillac GTP manual, TC definitions (verbatim):
  - Gain is "the amount of intervention the Traction Control will exert when wheel spin is detected. Higher values result in a more aggressive throttle cut to control wheelspin."
  - Slip is "how sensitive the Traction Control system will be to wheelspin. Higher values will activate the Traction Control system with smaller amounts of wheelspin, while lower values will allow slightly more wheelspin prior to activating the system."
  - The dash shows "TC A: Current Traction Control Gain setting" and "TC B: Current Traction Control Slip setting."
  - The manual recommends mapping Brake Bias, Traction Control and ABS adjustments to controls before driving. — [iRacing Cadillac V-Series.R GTP User Manual (PDF)](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)
- [SIM] Coach Dave (Cadillac GTP) advises mapping TC to the wheel "to allow for in-race adjustments as the fuel burns off, the tyres wear, and the track rubbers in." [snippet] — [Coach Dave: Cadillac V-Series.R GTP guide](https://coachdaveacademy.com/tutorials/under-the-hood-tips-and-tricks-to-driving-the-cadillac-v-series-r-gtp/)
- [SIM] Coach Dave (Porsche 963 GTP): "Running the TC at around level five or six can give good results." The twin-turbo V8 plus hybrid "can spike power when you least expect it exiting corners." [single-source] — [Coach Dave: iRacing Porsche 963 GTP Guide](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)
- [SIM] Coach Dave says "interruptions in the slope" of the throttle trace may mean TC is intervening. No definition is given. — [Coach Dave: Throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)
- [PRO, motorcycle, single-source] A Michelin remark quoted by DriveTribe says riders who rely on TC all the time can wear tyres faster, because "all those pulses of power on, power off, power on do cause more wear than a smooth controlled winding on of power." [snippet; page returned 403] — [DriveTribe/Medium: How traction control could be prematurely wearing out your tyre](https://medium.com/@drivetribe/how-traction-control-could-be-prematurely-wearing-out-your-tyre-8e221e333e4e)
- [SIM] Sim sources contradict that framing:
  - Driver61 (GT Sport) says drivers with TC off "can better control the amount of wheel spin they are getting and can therefore slow the tyre ware process." — [Driver61: Faster without TC in GT Sport](https://driver61.com/sim-racing/how-to-be-faster-without-traction-control-in-gran-turismo-sport/)
  - Another sim guide says a high TC setting "will help save tyre life," but a skilled driver with TC off can manage tyres through throttle. [snippet] — [Trophi.ai: Driving without TC in F1 24](https://www.trophi.ai/post/how-to-drive-without-traction-control-in-f1-24)
  - An ACC forum says lower TC is generally faster but costs "higher tyre wear and degradation." [forum] — [Steam ACC discussion](https://steamcommunity.com/app/805550/discussions/0/2967272951896758149/)
- [PRO, fan-site level] On F1 since the 2008 TC ban: the fastest exit comes from "a smooth throttle application at just below the wheelspin threshold," and chasing the throttle risks wheelspin, lost lap time and premature tyre wear. [snippet] — [F1-Fansite: Traction glossary](https://www.f1-fansite.com/glossary/traction/)
- [PRO, fan-site level] Degraded rears show as wheelspin, with the rear stepping sideways on throttle, and controlled sliding is part of tyre management at some points of a stint. [snippet] — [GrandPrixPal: Spotting tyre degradation](https://www.grandprixpal.com/blog/f1-tyre-degradation-from-grandstand)
- [PRO] A MegaRide tyre simulation (Monaco 2026 preview) says the real challenge is managing rear surface temperatures under repeated traction demands on slow-corner exits. [snippet, F1 context] — [Scuderia Fans: Monaco GP tyre preview](https://scuderiafans.com/monaco-gp-tyre-preview-minimal-degradation-but-traction-remains-a-challenge/)
- [PRO] Racer (2023, IMSA GTP cold tyres): engineers and drivers found some gains by optimising traction control in the early laps on fresh tyres to get heat into them, "but that's a small percentage." IMSA teams mostly have one tyre compound. Pipo Derani is quoted: "there's not much we can do to make that particular issue much better." [snippet; page returned 429] — [Racer: Solving GTP's cold tire conundrum](https://racer.com/2023/09/16/solving-gtps-cold-tire-conundrum)
- [PRO] Hybrid architecture:
  - LMDh cars (the class of all iRacing GTPs: Cadillac, Porsche 963, BMW M Hybrid V8, Acura ARX-06) have a spec rear-axle hybrid of 50 kW maximum.
  - Sources conflict on a deployment speed floor. Some say LMDh can deploy at any speed (from 0 km/h); one 2026 guide says it is restricted to speeds above 120 kph.
  - LMH front-axle deployment is BoP-set: 190 km/h for Ferrari and Toyota, 150 km/h for Peugeot in one source.
  - These figures should be checked against current regulations. [conflicting; snippet] — [Motorsport.com: What are LMH and LMDh](https://www.motorsport.com/wec/news/what-are-lmh-and-lmdh-the-top-le-mans-24-hours-series-explained/10480126/); [Car Racing Reporter: LMH and LMDh in short](https://www.carracingreporter.com/home/lmh-lmdh-in-short); [a-e.li: Le Mans Hypercar 2026 guide](https://a-e.li/reports/le-mans-hypercar-lmdh/)
- [SIM] iRacing Cadillac GTP hybrid modes:
  - "Balanced" is "the primary Race mode", which deploys to cut lap time "while still maintaining a reasonable State of Charge over the duration of a lap". It "will take a few flying laps for the Hybrid system to learn the track."
  - With "Attack", "the laptime gain from this mode is not enough to offset the loss in pace from having to recharge."
  - "Build" will "compromise lap times significantly."
  - A sim guide says the deployment mode can change only four times per lap. [snippet for the four-times rule] — [iRacing Cadillac GTP Manual (PDF)](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf); [Coach Dave: Cadillac GTP guide](https://coachdaveacademy.com/tutorials/under-the-hood-tips-and-tricks-to-driving-the-cadillac-v-series-r-gtp/)

### Inferences
- Detecting wheelspin from the iRacing channels available:
  - **Primary method:** rear slip = (mean rear wheel speed − mean front wheel speed) / mean front wheel speed. Use only on-throttle, off-brake samples above a minimum speed, because slip ratios blow up at low speed. Average left and right on each axle to cancel the inner/outer wheel speed difference in corners.
  - **Fallback:** rpm ÷ speed is constant in a given gear with no slip. Learn a per-gear baseline from steady straight-line samples and flag on-throttle excursions above it, the same idea as MoTeC's zero-slip RPM.
  - **Caveats:** given the creep caveat, only slip clearly above the driver's own clean-exit baseline should count as "wheelspin". The 6–7% and 10% figures are road/ECU reference points, not GTP slick targets.
- TC action probably does not show in the throttle-pedal channel if that channel records the driver's pedal, because TC cuts engine torque downstream of the pedal. In that case TC intervention would look like pedal at or near 100% while longitudinal acceleration or the rpm rise flattens and rear slip plateaus. Coach Dave's "interruptions in the slope" more plausibly reflect the *driver* reacting to spin or TC. Whether iRacing's throttle channel is the raw pedal or the post-TC value should be verified per channel.
- Coaching stance on TC: the iRacing Slip setting chooses how much spin is allowed and Gain chooses how hard the cut is. When rear slip is clipped at the TC threshold for long stretches of every exit, the driver is "driving on TC". The trade-off between pace and tyre wear there is contested in the sources: the single-source Michelin pulse-wear claim against the sim claims that higher TC saves tyres. The assistant should present it as a trade-off to be checked against the driver's own stint data (rear temperatures and lap-time fade), not as a settled fact.
- Hybrid on exit: on an LMDh, electric torque is added at the rear axle. Any step in deployment during the exit adds rear torque the driver did not ask for with the pedal. Coach Dave's "spike power" remark is consistent with this. Wheelspin events that cluster at the same lap-distance point on every lap, independent of throttle rate, may point to deployment or turbo behaviour rather than to driver input.

### Gaps
- No quantified link between wheelspin (slip %, duration) and rear tyre temperature or wear rate was found for any endurance class.
- No real-world GTP/Hypercar, LMP2 or GT3 driver or engineer interview on adjusting TC through a stint was found. Only sim guides say to do so, plus the Racer note that teams use TC on fresh tyres to generate heat.
- A circulating sim claim (a "sawtooth" 60% → 40% → 100% trace meaning over-driving and correcting wheelspin) appeared in a search summary but was **not** found on the Mental Apex or Fanatec pages checked. It is unverified and should not be used.
- The exact current LMDh deployment speed floor and the iRacing implementation of deployment timing are unconfirmed.

## 3. Throttle mistakes: mid-corner lifts and lift-off oversteer, double application, stabbing, coasting, brake-throttle overlap; detection and coaching

### Takeaway
Sources agree on the main faults. An abrupt mid-corner lift shifts load forward and unloads the rear, which causes lift-off or snap oversteer; the fix is to re-apply maintenance throttle smoothly or not lift at all. "On, off, on" means the pick-up came too early, and Bentley estimates it costs about a tenth. Small rapid stabs signal uncertainty about grip. A gradual roll-off before braking means coasting. A throttle lift on exit should prompt the question "why": check the steering trace for understeer (more lock) or oversteer (counter-steer), and if the steering is clean, the line is probably wrong. No source covering brake-throttle overlap or left-foot braking was found.

### Cited Findings
- [PRO] Lift-off oversteer mechanism: the sudden deceleration shifts vertical load from the rear to the front tyres, which reduces rear lateral grip and tightens the car's line. — [Wikipedia: Lift-off oversteer](https://en.wikipedia.org/wiki/Lift-off_oversteer)
- [SIM] VRS:
  - Lift-off oversteer follows an abrupt mid-corner lift. The fix is to "quickly reapply some maintenance throttle."
  - "An abrupt throttle change" is listed as a snap-oversteer trigger.
  - "Oversteer can be caused by using too much throttle in rear wheel driven cars," and "reducing throttle input in this situation will help reduce the oversteer." — [VRS 3.3: Car control](https://virtualracingschool.com/academy/iracing-career-guide/second-season/car-control/)
- [PRO, coaching] Oversteer guides advise: if you are on the power mid-corner and close to the limit, do not lift off the throttle; if you must reduce it, release it gradually. Which page said which was not separated in the search summary. [snippet] — [DrivingFast.net: Oversteer](https://www.drivingfast.net/oversteer/); [Driver61: Oversteer](https://driver61.com/uni/oversteer/)
- [PRO] Double application (on-off-on): Bentley says pick-up "too soon, resulting in having to ease back up off of it before going to full throttle" costs "a tenth of a second." [snippet] — [Speed Secrets 365 PDF](https://speedsecrets.com/wp-content/uploads/2025/07/Speed-Secrets-365-v1.1-6-1-25.pdf)
- [SIM] Coach Dave:
  - A trace that "rises, dips, and then rises again" means power is going on in the wrong phase of the corner.
  - Stabs: "Small, rapid mid-corner inputs suggest uncertainty about balance or grip." The remedy is to "hold a steady throttle through the corner and add power only on exit."
  - Coasting: a gradual reduction before braking suggests coasting too much, while "an abrupt or late lift can unsettle the car."
  - A trace dropping earlier than the reference suggests braking too early. — [Coach Dave: Throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)
- [SIM] Fanatec:
  - A steep 0% → 100% jump in a low-grip corner "could be a sign of over-aggression, leading to wheelspin."
  - A jagged or erratic graph "typically indicates overcorrection or unstable driving."
  - Stepped or segmented curves indicate hesitation or low confidence in grip.
  - Brief lifts "can help with car rotation or stability," but overusing them signals excess caution. — [Fanatec: Throttle graph telemetry](https://www.fanatec.com/us/en/explorer/games/gaming-tips/how-throttle-graph-telemetry-can-improve-your-sim-racing-lap-times/)
- [SIM] A small dip below 100% on a straight may be a lift the driver doesn't realise they made. — [Mental Apex: telemetry guide](https://mentalapexracing.com/telemetry-guide/)
- [PRO] Bentley's diagnostic sequence for a lift on exit:
  - "If you see where you've had to ease up on the throttle exiting a turn, ask yourself 'Why?'"
  - Then check the steering: "Are you having to turn more (understeer), or use some counter-steer (oversteer)?"
  - "If there isn't much change in the steering angle, it might be as simple as you're on the wrong line," i.e. "aimed slightly in the wrong direction when you're trying to go to full throttle." — [Speed Secrets: Use data acquisition to be a better driver](https://speedsecrets.com/use-data-acquisition-be-better-driver/)
- [PRO, engineering guide] When the rear steps out despite smooth, progressive inputs, engineers turn their attention to the car. Steering reversals and opposite lock show as rapid back-and-forth motion on the steering trace, and a mid-corner dip in the speed trace can mean a correction or an exit lift. [snippet] — [ACI Motorsports: Race data analysis explained](https://www.acimotorsports.com/post/race-data-analysis-explained-from-telemetry-to-lap-time-gains)
- [SIM] Setup-side fixes for lift-off rotation: "move brake bias forward, add rear toe-in for stability, and stay smoother off the brake". Low rear mechanical grip is listed as a cause of a mid-corner loose rear. [snippet] — [SimRacingManual: Fixing understeer and oversteer with setup](https://simracingmanual.com/setups/understeer-oversteer-fixes/)

### Inferences
Detection rules for the assistant. The thresholds are placeholders to tune against the driver's own data, not sourced values:
- **Double application:** inside a corner window (brake release → sustained full throttle), throttle rises above a low level, falls by more than a set amount, then rises again before reaching ~95%. Report the count per corner and the time lost against the reference.
- **Mid-corner lift:** throttle falls while |steering| is near its corner peak, i.e. before steering unwind. If counter-steer (a steering sign reversal) follows within a short window, tag it lift-off oversteer. If extra lock follows instead, tag it a throttle-induced push.
- **Stab:** the throttle derivative exceeds a high rate and is quickly followed by a reduction, or there are several small up-down oscillations under 100% mid-corner.
- **Coasting:** brake ≈ 0 and throttle ≈ 0 at the same time for longer than a set duration, either between brake release and throttle pick-up or before a braking zone. Coasting before braking may be deliberate fuel saving (see section 4) and should not be flagged as an error when fuel saving is in effect.
- **Brake-throttle overlap:** both pedals above small thresholds at once. Legitimate uses are not established by any source I found. Possible explanations, all unverified: left-foot-braking stabilisation, or keeping turbo boost on the turbocharged GTPs. The assistant should report overlap neutrally, tied to its cost (speed lost, fuel used) rather than labelling it a mistake.
- **Car vs driver:** Bentley's and ACI's logic together suggest a rule. If rear-slip or counter-steer events happen with a smooth, monotonic throttle (no stab, no lift), lean towards car or setup (rear grip, diff, TC). If they happen right after a stab or lift, lean towards driver input. Recurrence at the same corner on every lap with varied inputs also points at the car.

### Gaps
- No source discussing brake-throttle overlap or left-foot braking use and abuse in GTP, LMP2 or GT3 was found.
- No quantified cost of stabbing or coasting was found, beyond Bentley's "a tenth" heuristic for on-off-on.
- The exact phrase "double application" was not found in any coaching source. The concept appears as "on, off, on" or "rises, dips, rises".

## 4. Endurance specifics: protecting rear tyres over a double stint, consistency, fuel/energy saving via throttle and its lap-time cost, cold tyres after a stop, wet/damp

### Takeaway
In real Hypercar/GTP racing, stint length is governed by a per-stint deployed-energy cap measured at the driveshafts. Lift and coast is described as the primary saving technique, with short-shifting secondary. A modelled F1-type example put a 10% fuel saving at about +0.41 s/lap, but that is a generic simulation, not a GTP figure. Fresh tyres after a stop do not tolerate sudden power. IMSA teams use TC on fresh tyres to help generate heat, with small gains. Michelin's 2026 Hypercar tyre is designed for multi-stinting (up to four stints on a set), and warm-up is now largely in the driver's hands. Wet guidance from coaches is to straighten exits, add power gradually, short-shift, and ease off when spin starts.

### Cited Findings
- [PRO] WEC Hypercar rules: "the maximum cumulative deployed energy per stint must stay below the value listed in the BOP table," and "Energy consumption is calculated from the integral of the driveshaft torque sensors." — [FIA WEC 2024 Hypercar Technical Information (decision PDF)](https://fiawec.alkamelsystems.com/Results_NoticeBoard/12_2024/committee/WEC_2024_D05_Hypercar_Technical_information_08012024.pdf)
- [PRO] IMSA GTP virtual energy (Motorsport.com, Oct 2023):
  - "lifting and coasting being the primary method."
  - Philipp Eng (BMW): "To save energy is basically the same thing as to save fuel." and "You definitely need that guidance on what to do."
  - Iain Watt (Action Express): "We're governed by energy; we want to make sure that we have to pit because of virtual energy."
  - The 2023 limit was 920 MJ, later 902 MJ for BMW and Cadillac. Exceeding it brings a 100-second hold, rising in 100-second steps.
  - No lap-time cost is quantified. The figures are dated. — [Motorsport.com: How virtual energy has become a defining principle in Hypercar racing](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- [SIM, lap-time model] A lift-and-coast lap at Circuit de Catalunya saved 10% fuel against a maximum-attack lap: "Overall, the driver loses +0.411s." The author extrapolates "+4.110s" to save an entire extra lap of fuel, a linear ×10 extrapolation. The method is to lift earlier before heavy braking zones and let engine braking and drag slow the car "for a few hundred meters." The vehicle model is not stated in the excerpt. [single-source] — [Fastest-lap: Lift-and-coast blog](https://fastest-lap.readthedocs.io/en/latest/blogs/blog_lift_and_coast.html)
- [SIM] Le Mans Ultimate hybrid guides say lift and coast saves ICE fuel but regenerates less electrical energy under braking, and that short-shifting saves more ICE energy. [snippet; which of the two pages said which was not separated] — [Traxion: Virtual Energy in LMU](https://traxion.gg/how-to-manage-virtual-energy-in-le-mans-ultimate/); [Trophi.ai: LMU hybrid systems](https://www.trophi.ai/post/how-to-make-the-most-of-le-mans-ultimates-hybrid-systems)
- [SIM] iRacing Cadillac GTP fuel tools: dash "DELTA (fuel): Difference between current per-lap fuel usage and the pre-set fuel usage target", "LAPS (fuel): Estimated number of laps remaining", "TRGT: Target per-lap fuel usage". The Fuel Target garage setting "will have no effect on the chassis handling and only changes what is shown on the dash." — [iRacing Cadillac GTP Manual (PDF)](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)
- [PRO] Michelin 2026 Hypercar tyre:
  - Many cars are expected to run up to four stints on a single set, and the carcass is meant to reduce the penalty of double- or multi-stinting.
  - Heating "is now entirely dependent on the driver: quick with Softs, slower with Hards."
  - The medium's operating window is "significantly wider" than the 2025 tyre. [snippet] — [RacerViews: Inside Michelin's 2026 Pilot Sport Endurance Tyre](https://www.racerviews.com/2026/06/06/a-new-look-for-le-mans-inside-michelins-2026-pilot-sport-endurance-tyre); [DailySportscar: Michelin's 2026 Hypercar Tyres](https://www.dailysportscar.com/2026/06/03/michelins-2026-tyres-set-for-crucial-le-mans-test.html)
- [PRO] IMSA GTP on fresh tyres: TC optimisation in the early laps helps get heat in, but the gain is "a small percentage." [snippet] — [Racer: Solving GTP's cold tire conundrum](https://racer.com/2023/09/16/solving-gtps-cold-tire-conundrum)
- [SIM] iRacing cold tyres: "cold tyres don't tolerate that sudden hit of power," and the car often ends up sideways. The advice is to apply power slowly. [snippet] — [BoxThisLap: iRacing, Mastering Cold Tyres](https://boxthislap.org/iracing-mastering-cold-tyres/)
- [SIM] iRacing GTP tyres: higher track temperature means more wear, weaving "can do is wear the tyre out quicker," and the wear figure can't be seen until the car is in the pit box. [snippet] — [OverTake: iRacing GTP Tyre Guide](https://www.overtake.gg/news/video-how-to-master-iracings-new-gtp-tyres.3022/)
- [PRO] Blayze (coach Ken Hill, 20+ years) on wet tracks:
  - Test grip by accelerating lightly right after the pit lane.
  - "If you feel wheel spin, easing off the throttle can help the tires regain grip." John Andretti is quoted: "just get out of the throttle."
  - Straighter entries and exits turn most cars into "point and shoot" machines.
  - The article does not cover gearing. — [Blayze: Finding the limit on a wet race track](https://blayze.io/blog/car-racing/finding-the-limit-on-a-wet-race-track)
- [SIM/other] Short-shifting in the wet: a sim guide says upshifting before the optimal rpm limits power to the rear wheels and suits wet tracks, and a motorcycle racer says he short-shifts in the wet. [snippet] — [BoxThisLap: F1 23 dry to wet starts](https://boxthislap.org/f1-23-from-dry-to-wet-tracks-unlocking-the-perfect-start-in-any-condition/); [MCN: Maintaining speed in the wet](https://motorcyclenews.com/news/2017/may/motorcycle-riding-wet-track)
- [PRO] Consistency: an inconsistent throttle pick-up point usually means "you don't have enough references and/or your braking is inconsistent." — [Bentley If-Then](https://rossbentley.substack.com/p/speed-secrets-if-then-revisited)

### Inferences
- The iRacing GTP manual describes fuel-target dash readouts and no virtual-energy readout. So in iRacing the stint limiter is probably fuel (plus battery state of charge within a lap), not the real-world per-stint virtual-energy cap. This should be verified against current iRacing GTP rules before the assistant phrases calls in MJ.
- To quantify a fuel-saving lift for the driver, compare the lap with and without the lift: fuel used per lap and lap time. Report seconds lost per litre saved per corner, so the driver can pick the cheapest corners. The fastest-lap model supports the idea that cost varies by braking zone, but gives no per-corner breakdown.
- For a double stint, the assistant can trend per lap: rear slip % on exits, TC setting (TC A/TC B, if logged), % full throttle, apex-to-full-throttle distance, and lap time. Rising rear slip at the same throttle rates, or a driver forced to delay full throttle later in the stint, is the data signature of rear degradation. This matches the fan-site description of degraded rears stepping out on throttle (section 2). It is the time to suggest smoother roll-on or a TC click, per the Coach Dave advice to adjust TC as tyres wear.
- After a stop, out-laps and the first flying laps should be coached and judged separately. Throttle aggression on cold tyres is a car-control risk, and exit-speed deficits there should not be compared with warm-tyre laps.

### Gaps
- No real-world quantified lap-time cost of lift and coast, short-shifting or partial throttle on straights for GTP/Hypercar, LMP2 or GT3 was found.
- No source found on partial throttle on straights as a fuel-saving method, or its cost relative to lift and coast.
- No pro source on throttle technique for rear-tyre protection over a double stint specifically. The only related item is Michelin's multi-stint tyre design and the single-source motorcycle remark on TC pulsing.
- No LMP2-specific (non-hybrid, single-make tyre) throttle or TC guidance was found.

## 5. Telemetry markers and coaching: metrics, example phrases, throttle-induced balance problem vs car problem

### Takeaway
Professional data practice uses throttle histograms (% of lap at each throttle position) and % full throttle per lap, often defined as throttle above ~95%. Bentley warns this is not a stand-alone performance measure: in his example, two drivers set the same lap time with 61% and 68% full throttle. The other markers are the timing, slope and smoothness of the exit trace against a reference lap, plus wheelspin from wheel-speed slip. Attributing a balance problem means reading the throttle and steering traces together: a smooth input that still produces a slide points at the car, and a stab or lift just before the slide points at the driver.

### Cited Findings
- [PRO] Bentley on throttle histograms (verbatim):
  - The histogram "indicates what percentage of the lap is spent at various throttle positions."
  - His example: "I spent 61% of the lap at full throttle – he was flat to the floor for 68% of the lap. But, we had turned the same lap time, to within a couple of hundredths of a second."
  - On the other driver: "My competitor's driving style was to use the throttle like an on-off switch," with "almost nothing between off-throttle and full-throttle." That driver "was at 0% throttle almost 14% more of the lap than I was."
  - Conclusion: "While more time at full throttle may seem to make you faster… if it's at the expense of some other benefits, perhaps it's not actually going to be faster."
  - Throttle position ranks second, after speed, in his channel priorities. — [Speed Secrets: Use data acquisition to be a better driver](https://speedsecrets.com/use-data-acquisition-be-better-driver/)
- [PRO] HP Academy explains full-throttle % as derived from a histogram that bins a lap's samples by throttle range. It cautions that "throttle application alone can't be used as a sole indicator of performance." [snippet] — [HP Academy: Throttle Histogram](https://hpacademy.com/courses/data-analysis-fundamentals/the-data-analysis-tool-box-throttle-histogram)
- [PRO, data tool] In MoTeC i2 Pro, % full throttle can be computed as stat_mean on a throttle-above-95% condition, reset each lap. [snippet; forum] — [MoTeC forum: % of time at 100% throttle](https://forum.motec.com.au/viewtopic.php?p=5149)
- [SIM] Coach Dave's method:
  - Compare pedal timing, slope (aggression) and smoothness (efficiency) against a reference.
  - First check pedal calibration (that the pedal reaches full throttle and fully releases).
  - Compare several laps to find patterns.
  - Set one corner-specific goal (e.g. smoother application, longer time at full throttle). — [Coach Dave: Throttle traces](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)
- [SIM] If the trace is not linear on a straight, you "may need to recalibrate your pedals". Smoother transitions to full throttle "help reduce lap time and tire wear." — [Fanatec: Throttle graph telemetry](https://www.fanatec.com/us/en/explorer/games/gaming-tips/how-throttle-graph-telemetry-can-improve-your-sim-racing-lap-times/)
- [PRO, engineering guide] Engineers focus on the point where the driver returns to the throttle, how quickly they reach full throttle, and whether the application is smooth or hesitant. When the rear steps out despite smooth, progressive inputs, they look at the car. [snippet] — [ACI Motorsports: Race data analysis explained](https://www.acimotorsports.com/post/race-data-analysis-explained-from-telemetry-to-lap-time-gains)
- [PRO] Bentley's lift diagnosis is "ask yourself 'Why?'", followed by the steering check for understeer, oversteer or a wrong line (quoted in section 3). — [Speed Secrets: data acquisition](https://speedsecrets.com/use-data-acquisition-be-better-driver/)
- Example coaching phrases found in sources (verbatim):
  - [PRO] "Apply the throttle at the point where you don't have to ease off it when exiting the corner." — [Speed Secrets 365](https://speedsecrets.com/wp-content/uploads/2025/07/Speed-Secrets-365-v1.1-6-1-25.pdf) [snippet]
  - [PRO] "Continue to add more throttle as you open up the steering angle." — [Driver61](https://driver61.com/uni/corner-exit/)
  - [PRO] "any sharp inputs will cause a premature loss of traction." — [Driver61](https://driver61.com/uni/corner-exit/)
  - [PRO] "just get out of the throttle" (John Andretti, on wet wheelspin) — [Blayze](https://blayze.io/blog/car-racing/finding-the-limit-on-a-wet-race-track)
  - [SIM] "hold a steady throttle through the corner and add power only on exit." — [Coach Dave](https://coachdaveacademy.com/tutorials/a-delta-guide-how-to-use-throttle-traces-to-improve/)
  - [SIM] "Patience then is a virtue before asking for the power to accelerate from the bend." (Porsche 963) — [Coach Dave](https://coachdaveacademy.com/tutorials/iracing-guide-porsche-963-gtp/)
  - [SIM] "quickly reapply some maintenance throttle" (after a lift-off slide) — [VRS](https://virtualracingschool.com/academy/iracing-career-guide/second-season/car-control/)

### Inferences
Proposed metric set for the coaching assistant. The definitions are mine; only the >95% full-throttle threshold has a source (MoTeC forum):

| Metric | Definition | How to read it |
|---|---|---|
| T_on | Time/distance from apex (min speed) to throttle >~5% | Secondary metric; read with Bentley's If-Then rules |
| T_full | Time/distance from apex to sustained ≥95% with no lift until braking | Primary exit metric; compare with best/reference lap |
| Application rate | Throttle %/s between ~10% and ~90% on exit | Compare with the driver's own clean exits and the reference; no literature target exists |
| Smoothness | Number of throttle reversals (decrease > a set amount) before T_full, plus a stab count | Lower is better; ties to "on-off-on" costing ~a tenth (Bentley heuristic) |
| % full throttle per lap | Share of lap with throttle >95% | Trend metric only. Bentley's 61% vs 68% case shows it can't rank drivers alone. Pair with % at 0% and the histogram shape |
| Wheelspin % | Share of on-throttle samples where rear slip exceeds the driver's clean baseline by a margin, plus peak slip per corner | Trend over the stint against rear tyre temperatures and lap time |
| Exit speed carry | Speed delta against the reference at fixed distances after each exit | Shows whether the T_full gain turns into straight-line time |
| Coast time | Both pedals ≈0 between brake and throttle | Separate fuel-save coasting (intended) from hesitation |

- Telling a throttle-induced balance problem from a car problem:
  - The input before the event matters most. A slide or counter-steer within a short window after a stab, a lift or an application faster than the driver's baseline is driver-induced. A slide under a monotonic, baseline-rate application is car-induced: rear grip, diff drive ramp or preload, TC Slip/Gain, or tyre degradation.
  - Consistency across laps matters too. A car problem recurs at the same corner whatever the variation in input.
  - Stint trend. If the same input produces more slip as the stint goes on, the tyre is the cause, not the technique.
  - In section 1, Coach Dave notes on-throttle understeer from applying power with lock still on. If steering lock *increases* while the throttle rises, the driver is asking the front for both turning and drive.
  - The Cadillac manual says diff preload and lower drive ramp angles increase on-throttle understeer. So a persistent exit push under good throttle technique is a setup item, not a coaching item. [manual wording from the Diff section: "more locking force increases understeer during braking and acceleration phases"] — [iRacing Cadillac GTP Manual (PDF)](https://s100.iracing.com/wp-content/uploads/2023/07/Cadillac-V-Series.R-GTP-Manual-V2.pdf)

### Gaps
- No throttle-specific metric definitions from YourDataDriven, Track Titan, Blayze or iRacing's own coaching were found. Any claim about how those tools define "time to full throttle" or "wheelspin %" would be unsourced.
- No published threshold for what counts as "excessive" wheelspin % per lap in a GTP was found.
- No MoTeC, Pi or Cosworth official data-analysis manual passage on throttle-trace analysis was retrieved. Only the MoTeC forum and HP Academy course pages were found.
