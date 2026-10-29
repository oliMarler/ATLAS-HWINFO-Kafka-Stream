# Steering technique for race cars (endurance focus) and how coaches/engineers give steering feedback

Labels: **PRO** = real-world professional coaching, engineering or driver testimony. **SIM** = iRacing or other sim coaching/tool content. **[single-source]** = only one source found for the claim. **[snippet]** = taken from a search-result summary; the page itself was not fetched or could not be fetched, so the wording is unverified. Anything under "Inferences" is my reasoning, not a sourced claim.

Overall source caveat: there is a lot of coaching blog content on steering and very little measured, published data. Most real "numbers" (reversal thresholds, peak-lock tolerances) are not published by race coaches. I found **no** GTP/Hypercar- or LMP2-specific steering guidance, either PRO or SIM. Everything below is general race-car technique that applies to those cars, not car-specific.

## 1. What good steering looks like (one input to the apex, one unwind, turn-in rate, minimum steering, feeling the front limit)

### Takeaway
Good steering is one deliberate build to the needed lock and one progressive unwind, with no mid-corner additions. The *rate* of turn-in should differ by corner: generally gentle and progressive in fast corners, quicker and crisper in tight ones. "Minimum steering" really means using no more lock than the front tyres' peak-grip slip angle needs. Past that point, extra lock adds scrub but no lateral g. The limit announces itself as falling self-aligning torque (lighter steering) slightly before the fronts peak.

### Cited Findings
- PRO: Ross Bentley names three steering-rate profiles: **linear** (constant rotation rate), **progressive** ("The rate of rotation increases") and **digressive** ("The rate of rotation decreases"). He also separates **timing** ("When, in relation to a corner's Turn-in point, you begin rotating the steering wheel") from **rate**. — [Bentley, Speed Secrets Substack, Steering Part 1, 3 Jan 2024 (paywalled after intro)](https://rossbentley.substack.com/p/speed-secrets-timing-and-rate-of)
- PRO: Bentley says fast corners generally call for a gentle, usually progressive turn-in, and tighter corners generally reward a quick, crisp turn-in. The rate should change with radius, elevation/camber, track width and how the car handles. Quote: "It's impossible to be really fast while always turning the wheel the same way." — [Bentley, "How To Turn Your Steering Wheel", speedsecrets.com, 25 Mar 2016](https://speedsecrets.com/how-to-turn-the-steering-wheel/)
- PRO: Bentley lists typical faults he sees: some drivers turn abruptly, some too slowly, and some add steering mid-corner. Using the same input in every corner means "you're not maximizing the car's performance." — [Bentley Substack Part 1](https://rossbentley.substack.com/p/speed-secrets-timing-and-rate-of)
- PRO: Blayze coach Colin Mullan prefers a slower initial input that lets the weight shift, then a firmer one: "Then once the weight is set, the turn can be more aggressive." He criticises a steep, linear spike at turn-in as "a very fast turn in." [single-source] — [Blayze, "How To Analyze Your Steering Trace In Data", 26 Feb 2024](https://blayze.io/blog/car-racing/analyze-your-steering-traces)
  - Possible tension with Bentley's "quick, crisp" tight-corner advice. Mullan describes a progressive input; Bentley says the rate should depend on the corner. They are compatible if "quick" means a short overall time to full lock rather than an instant jolt (inference).
- PRO: For rotation, Bentley says to "Focus on the timing and rate of release of the brakes", which "will help the car rotate with a minimum of steering." A quicker turn-in combined with brake-release timing can help start rotation, but "not always." — [Bentley, Ask Ross: "How can I make my car rotate more into a corner?" (c. 2023–24)](https://speedsecrets.com/q-how-can-i-make-my-car-rotate-more-into-a-corner/)
- SIM: Coach Dave Academy says a good trace shows "smooth arcs as you corner", with "a gradual increase in steering input as you approach, followed by a smooth return to the centre as you exit." — [Coach Dave Academy, "Get A Grip On Your Steering with Delta AI", D. Sturdivant, 16 Sep 2024](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)
- SIM: Fanatec: "A smooth, progressive steering trace is typically more effective and shows better car control." Jerky, rapid inputs can destabilise the car, especially in fast corners. Consumer-level source. — [Fanatec Explorer, steering input telemetry](https://www.fanatec.com/us/en/explorer/products/steering-wheel/steering-input-telemetry/)
- PRO (data engineering): Plotted against steering, lateral g traces a curve shaped like the tyre's lateral-force vs slip-angle curve. They are different quantities but reflect the same tyre behaviour. The course gives a case where "even though the steering input is increasing, the lateral G is actually dropping off", meaning "we've passed the peak slip angle of the front tyres." — [HP Academy, Professional Motorsport Data Analysis: "Cornering performance – steering data and balance"](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (vehicle dynamics): The tyre's aligning moment drops before lateral force saturates because pneumatic trail shrinks as the contact patch deforms or slides. The drop can be felt through the wheel as a sign the car is near the limit. Large mechanical-to-pneumatic trail ratios and power assistance make it harder to feel. [snippet: page behind a bot check, not verified] — [SWOV publication listing, "Haptic feedback steering wheel near vehicle's handling limits using wheel load sensing"](https://swov.nl/en/publicatie/haptic-feedback-steering-wheel-near-vehicles-handling-limits-using-wheel-load-sensing)
- PRO (forum, engineering discussion): Sliding starts at the rear of the contact patch and spreads forward. Pneumatic trail falls while lateral force rises, so self-aligning torque (SAT) plateaus and then falls toward zero at peak cornering force. One poster: mechanical trail gives "a feel for the cornering force" and pneumatic trail "a feel for when the contact patch starts sliding." Another notes SAT = Fy × pneumatic trail, so the two are linked rather than separate cues. Forum-grade. [snippet] — [f1technical: Self aligning torque and steering feel](https://f1technical.net/forum/viewtopic.php?p=483385); [f1technical: Pneumatic trail](https://f1technical.net/forum/viewtopic.php?p=177992)
- PRO: Keep hands in one place on the wheel (9 and 3) and don't shuffle. "Keeping your hands in one spot on the wheel will help your subconscious mind correct small mistakes"; "the harder you grip the less sensitive your hands are to small vibrations." — [MotoIQ, "You're Doing it Wrong – Common Driver Errors Often Mistaken for Handling Issues" p.3](https://motoiq.com/youre-doing-it-wrong-common-driver-errors-often-mistaken-for-handling-issues/3)

### Inferences
- A practical test for "minimum steering" from the coaching assistant's channels: per corner, plot lateral g (or yaw rate × speed) against steering angle. The best lap should run up to the curve's knee and stop there. Steering that keeps rising after lateral g flattens or falls is lock beyond the fronts' peak (HP Academy finding above). This is better than "less is better" because a driver who never reaches the knee is under-using the fronts.
- For the shape of a good trace: one rising segment to a single peak or plateau, then one falling segment, with no sign change in steering rate inside each segment beyond noise. Turn-in rate (deg/s from turn-in to about 80% of peak) should be judged per corner against the driver's own best or a reference lap, not against a universal number. No published numeric rate targets were found.
- SAT is felt, not seen, in the listed telemetry. If iRacing's telemetry exposes a steering-column torque channel (I believe it does, but did not verify it here), a falling torque-per-steering-angle ratio could serve as a direct "fronts at the limit" marker. Unverified.

### Gaps
- No published numeric guidance on turn-in rate (deg/s) for any car class, PRO or SIM.
- Bentley's paid posts ("Time to Unwind", "A Tale of Two Steer-ers") were truncated, so his full guidance on when quick vs slow turn-in is right was not accessible.
- Carroll Smith (*Drive to Win*) and Skip Barber (*Going Faster*) texts were not reachable online, so nothing is cited from them.
- I found no source on how strongly iRacing GTP force feedback reproduces the SAT drop.

## 2. Steering corrections: what they mean, how to detect them in data, and what they cost

### Takeaway
Corrections are symptoms. Counter-steer or rapid reversals mean the rear stepped out, usually from entry speed or throttle. Adding lock mid-corner means understeer or a line that tightens because of an early turn-in. In data they show up as reversals in the steering trace, steering that rises while lateral g does not, and roughness or steering-integral channels. Road-safety research offers a formal reversal-counting method (filter, then count direction changes larger than a gap). Its parameters are published but were not retrievable here.

### Cited Findings
- SIM: Reversals appear as counter-steering spikes that "usually mean you're catching a slide or fixing instability." "Excessive corrections may point to a setup issue or a driving technique that's unsettling the rear of the car." Some counter-steer is normal. — [Fanatec](https://www.fanatec.com/us/en/explorer/products/steering-wheel/steering-input-telemetry/)
- SIM: Reversals show as rapid back-and-forth movement and signal instability. The goal is "minimising unnecessary corrections, particularly mid-corner." The fix: "Smoother throttle control on corner exits and avoiding excess speed going in will help reduce the need for overcorrection." — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)
- SIM: "Use tiny corrections instead of sawing at the wheel mid-corner." [snippet] — [SimXPro steering technique guide](https://simxpro.com/blogs/guides/steering-technique-in-sim-racing-smooth-inputs-micro-corrections-and-better-feel)
- PRO (data engineering): Extra mid-corner steering signals understeer. After an early turn-in, though, "it's not a case of genuine understeer it's just that the car needs to be turned sharper." A late, abrupt steering increase near the apex can be driver-caused, with peak lateral g arriving after the steering has already begun to unwind. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): Exit oversteer often follows entry or mid-corner understeer. The driver delays the throttle, then applies it aggressively, and the rear breaks away, showing as rapid counter-steer corrections. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): Engineers use **steering roughness** (smoothness, computable separately for entry and exit) and **steering integral** channels next to the raw trace. "A higher steering integral results from more total steering input over a lap", which indicates a shift toward understeer. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): HP Academy's data source note: steering usually comes from a column rotary pot or rack linear pot, with the convention "positive values, being left hand turns." Conventions vary, so check the sign. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (vehicle dynamics, via forum): Milliken & Milliken define understeer/oversteer angle as actual wheel angle minus the Ackermann steering angle. The same thread suggests comparing "commanded" yaw rate (from steering, wheelbase and speed) with measured yaw rate. [snippet: thread now redirects to a 403 page] — [MoTeC forum, "Oversteer maths formula"](https://forum.motec.com.au/viewtopic.php?p=7343)
- PRO (data tool vendor): AiM compares GPS-derived yaw rate with gyro yaw rate in a math channel. Positive difference = understeer, negative = oversteer, depending on sign conventions. [snippet] — [AiM application note (Adria)](https://support.aimshop.com/donloads/on-track-session/Adria.pdf)
- PRO (vehicle dynamics, forum): On a constant-radius test, plot steering-wheel angle against lateral acceleration. An upward-curving plot is understeer, and the gradient divided by steering ratio gives vehicle understeer. Forum-grade. [snippet] — [f1technical forum post](https://www.f1technical.net/forum/viewtopic.php?p=671264)
- PRO (road-safety research, not racing): The steering wheel reversal rate (SWRR) metric is defined in Markkula & Engström (2006), with filter settings and gap sizes "recommended in the Markkula and Engström (2006) paper." It is standardised in SAE J2944_201506. The reference implementation uses Butterworth low-pass filtering before counting reversals larger than a gap threshold. The numeric parameters are not on the repo landing page. — [gmarkkula/SteeringWheelReversalRate (GitHub)](https://github.com/gmarkkula/SteeringWheelReversalRate); [Markkula & Engström 2006, White Rose eprints](https://eprints.whiterose.ac.uk/id/eprint/131534/)
- PRO (road research): McLean & Hoffmann (1973) found reversal rates correlate with other measures of control frequency but "do not necessarily correlate with measures of absolute steering performance." [snippet] — [TRID record: "Steering reversals, measures of driver performance and steering task difficulty"](https://trid.trb.org/view/64028)
- SIM: Without a steering channel, lateral g gives the turn-in and unwind points, "But we can't see if the car has oversteer or understeer or exactly how a driver is manipulating the steering wheel." — [Blayze, Mullan 2024](https://blayze.io/blog/car-racing/analyze-your-steering-traces) (Blayze is PRO coaching; the statement is about data generally.)

### Inferences
- **Correction taxonomy for the assistant** (derived from the findings above):
  - **Counter-steer.** Steering sign is opposite to the corner direction (lateral g / yaw sign) → rear slide. If on exit with throttle, check the throttle step. If on entry, check brake release or downshift (HP Academy linked rear locking on downshifts to entry instability).
  - **Saw-tooth.** Small same-sign oscillations of steering rate at mid-corner → driver hunting for grip, nervous rear, or bumps. Low cost individually; a trend over a stint suggests rear deg (see Q3).
  - **Added lock after initial peak.** A second rise in steering before the unwind → understeer, or a tightening line from early turn-in or early throttle. Use the lateral-g response to separate them. If lateral g rises with the extra lock, it was line or tightening. If lateral g is flat or falling, the fronts were saturated.
  - **Late unwind.** Steering held near peak well past apex distance → "holding the apex" (see Q4).
- **Detection recipe** (inference, informed by SWRR): low-pass the steering signal (SWRR uses Butterworth filtering) and find local extrema. Count a reversal only when the swing between successive extrema exceeds a gap threshold, and do it per corner window by lap distance. Calibrate the threshold against the driver's own clean laps per car rather than inventing a fixed degree value. The McLean & Hoffmann caveat means reversal count measures control *activity*, not quality. Pair it with time loss.
- **Understeer angle from the listed channels** (standard kinematics, inference; check sign conventions): road-wheel angle δ ≈ steering-wheel angle / steering ratio. Kinematic (Ackermann) angle ≈ L/R, with path radius R = V/r (yaw rate) or V²/a_y (lateral g). Understeer angle ≈ δ − L·r/V. A positive and growing value means more steer than the path needs (understeer). The yaw-based and lateral-g-based versions diverge when the car has sideslip transients, and that divergence itself flags oversteer moments. This needs the GTP's steering ratio and wheelbase, which I did not find. A ratio-free proxy is steering angle per g, or per unit yaw rate × speed, compared lap to lap at the same corner.
- **Cost:** corrections cost time through scrubbed speed (see "steering as brake" in Q3) and delayed throttle (Q4). No source quantified time per reversal.

### Gaps
- Numeric SWRR gap size and filter cutoff (Markkula & Engström 2006, SAE J2944) not retrieved. They are also tuned for road driving, not racing.
- No published race-specific thresholds for "acceptable" reversals per corner, peak-lock tolerance or understeer angle.
- No sourced GTP steering ratio or wheelbase for iRacing.

## 3. Steering and tyre wear; "less steering is faster" and its limits

### Takeaway
Excess lock beyond the fronts' optimum slip angle scrubs the front tyres. It acts as a brake, heats the fronts and wears the outer front. Abrupt inputs spike tyre load. Over a stint, front degradation shows as rising mid-corner steering (understeer) and rear degradation as more exit corrections. "Less steering" holds only as "no more than the grip needs". Exceptions include low-grip surfaces, hesitant drivers and some tyre types, where a brisker input is faster.

### Cited Findings
- SIM: "the steering wheel acts as a kinetic brake". Once you exceed the optimal slip angle, the fronts "experience more scrub, sliding across the track." Coach Dave also says advanced drivers "begin to use the steering wheel to slow the car down and rely on the brakes for turning." That is an unusual, single-source claim; no data given. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)
- SIM: "Jerky inputs can overload the tyres, leading to reduced grip or even instability." — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)
- SIM: Over-driving the entry, by scrubbing the fronts in understeer, is a major tyre killer. "Use steering inputs that build progressively, not instantly." [snippet] — [SimXPro tyre management guide](https://simxpro.com/blogs/guides/tyre-management-in-sim-racing-driving-style-that-makes-tyres-last)
- SIM (forum, anecdotal): A wheel makes it easy to steer the fronts beyond what the car can use, so the fronts slide and "you get increased wear on outer front tire." [snippet] — [GTPlanet forum](https://www.gtplanet.net/forum/threads/why-do-steering-wheels-more-tire-wear.180266/)
- SIM: Straightening the wheel on exit aligns the tyres with the direction of travel, reducing scrub, rolling resistance and wear. — [Track Titan, "Accelerating – The Unwind"](https://www.tracktitan.io/study-plans/a4463edd-0169-4895-a7b8-644df1db64d1-accelerating-the-unwind)
- PRO (data engineering): Over a stint, front tyre overheating and degradation produced more mid-corner understeer. Rear degradation was linked to more corrections on exit. Balance observations are always relative to another driver, setup or tyre set. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): "Broadly speaking, a car that has more oversteer balance requires the driver to use less steering input." Less steering is partly a balance signature, not only a technique virtue. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO: Bentley ties correct brake-release timing and rate to rotating the car "with a minimum of steering." — [Bentley, Ask Ross](https://speedsecrets.com/q-how-can-i-make-my-car-rotate-more-into-a-corner/)
- SIM: "Smooth is fast" is "fundamentally correct in most driving scenarios", and smoother load transfer puts "less stress on your front tyres." Its limits:
  - over-deliberate drivers become "overly hesitant and slow to react", which can cause understeer through too little front load;
  - on slippery street circuits "cars can understeer if driven too smoothly", so "more abrupt steering inputs can help turn the car";
  - the right style depends on tyre type: smooth in F1 because Pirelli tyres degrade heavily, more sliding in Formula E on durable rubber.
  — [trophi.ai, "Why Smooth is Fast… Most of the Time", 5 Dec 2025](https://www.trophi.ai/post/why-smooth-is-fast-most-of-the-time)
- SIM (anecdote) [single-source]: the trophi author reports that a smoother style gave better front-tyre wear over a 65-minute ACC run at Kyalami and erased a late-stint pace deficit. No data shown. — [trophi.ai](https://www.trophi.ai/post/why-smooth-is-fast-most-of-the-time)
- PRO (F1, driver testimony): Leclerc, after losing pace late in stints, said he would analyse whether he was driving too aggressively and how that interacted with car balance. Driver style and balance are intertwined in degradation. [snippet] — [Motorsport.com: Leclerc "less aggressive" on tyres](https://www.motorsport.com/f1/news/leclerc-less-aggressive-tyres-vettel/4511018/)
- PRO (WEC Hypercar): Ferrari's Miguel Molina: "Degradation was the key of the race in Sebring"; "the less degradation we have in the race, the better." Ferrari reported the 499Ps "struggling in the last part of the second stint." — [Sportscar365, 13 Apr 2023](https://sportscar365.com/?p=114601)

### Inferences
- The defensible rule is "no more lock than the knee of the steering vs lateral-g curve" (Q1), not "less steering is always faster". Steering past the knee is pure front scrub: time loss now and wear later. Steering below it, with a slow or hesitant turn-in, leaves grip unused.
- Steering integral or steering-per-g rising lap over lap at the same corners, with no change in line, is a candidate front-degradation indicator. A rising exit-reversal count is a candidate rear-degradation indicator. Both follow the HP Academy pattern; I found no published thresholds for either.
- Because less steering is also a balance signature, compare a driver's steering only against references in the same car, setup and tyre state.

### Gaps
- No measured data, PRO or SIM, quantifying how much steering smoothness changes tyre temperature or degradation rate. The evidence is coaching opinion plus one sim anecdote.
- No source on how iRacing's tyre model in particular (GTP or otherwise) penalises front scrub vs rear sliding in wear.

## 4. Steering combined with brake and throttle (friction circle, trail braking, unwind before throttle, exits)

### Takeaway
Steering, braking and throttle share one grip budget. The coaching consensus: trail the brake into turn-in so the fronts stay loaded and the car rotates with less lock, and don't touch the throttle until you can start unwinding. Then add throttle in proportion to how far the wheel has straightened. Early throttle with lock still on unloads the fronts, causes understeer and forces more steering at the apex. Delaying and then stabbing the throttle causes exit oversteer.

### Cited Findings
- PRO (foundational physics): Braking, accelerating and cornering share a finite tyre grip budget, the "traction budget" or friction circle. — [Brian Beckman, "The Physics of Racing, Part 7: The Traction Budget" (1991)](https://miata.net/sport/Physics/07-Circle.html)
- SIM tool: On a g-g display, "A smooth arc from the top of the circle (braking) to the side (cornering) means you're trail braking well." Turning while braking too hard exceeds the budget and causes braking-induced understeer, and recovery is to release brake and steer. [snippet: attribution of the second point to this page not verified] — [RaceLab, G-force meter docs, Sep 2025](https://docs.racelab.app/news/2025/09/22/2025/g-force-meter)
- PRO: Trail braking (a slower, longer release) keeps load on the fronts, "resulting in more rotation", but "sometimes more trail braking overloads the front tires, resulting in understeer." On throttle: "to allow the car to finish rotating, you have to wait a moment before beginning to apply the throttle"; "if you apply it too soon, load is transferred to the rear, stopping the car from rotating." — [Bentley, Ask Ross](https://speedsecrets.com/q-how-can-i-make-my-car-rotate-more-into-a-corner/)
- PRO: "in almost any corner we don't want to touch the throttle until we can start to unwind the steering wheel." Early throttle is often a reaction to over-slowing, which should be fixed in the braking zone. "Professional race car drivers absolutely spend time coasting." — [Mazda Motorsports / Racers360 coaches, Driving Tip #1, 25 Feb 2020](https://www.mazdamotorsports.com/2020/02/25/driving-tip-1-the-top-mistakes-grassroots-race-car-drivers-make/)
- PRO: Throttle while still heading toward the apex shifts weight rearward, "inducing understeer", so "you are likely adding steering input right at the apex", just when the hands should open. Other causes of not being able to unwind:
  - early turn-in, after which you "will likely need to add steering wheel" after the apex;
  - not using the full track width on entry;
  - too much entry speed.
  — [Blayze, Dion von Moltke, "Why You Can't Open Your Hands At The Apex", 2024](https://blayze.io/blog/car-racing/why-you-cant-open-your-hands-at-corner-exit)
- PRO: Coaching cue during trail braking: ask "how early can I start to unwind the steering wheel." [snippet] — [Blayze, "Coaching a racecar driver champion", Feb 2023](https://blayze.io/blog/car-racing/coaching-a-racecar-driver-champion)
- PRO: Many drivers hold the apex too long: "The longer you hold your apex the longer you have to wait to get back to the throttle." "Instead of driving the car out to your exit point, let the car go out there." "If you end up in the middle of the track then start unwinding your steering a little earlier." If the car still doesn't reach the edge after unwinding at the apex, apex earlier. — [MotoIQ p.3](https://motoiq.com/youre-doing-it-wrong-common-driver-errors-often-mistaken-for-handling-issues/3)
- PRO: Corner exit taught as easing onto the throttle while reducing lock, with a string analogy: the more the wheel unwinds, the more throttle is available. [snippet] — [HP Academy, Race Driving Fundamentals: Corner exit](https://hpacademy.com/courses/race-driving-fundamentals/corner-exit-corner-exit)
- SIM: "Gradually increase throttle as you unwind the steering wheel." In telemetry, a sharp rise of wheel angle vs the reference lap on the "Diff to Ref" chart, "especially ... in the initial engagement of the throttle", indicates the driver isn't straightening the wheel enough. — [Track Titan, "Accelerating – The Unwind"](https://www.tracktitan.io/study-plans/a4463edd-0169-4895-a7b8-644df1db64d1-accelerating-the-unwind)
- PRO: The "unwind before throttle" rule is not absolute. *Ultimate Speed Secrets* says getting on the throttle a bit earlier helps some cars, and timing depends on the car. [snippet: reader's highlight notes on Goodreads, not the book itself] — [Goodreads notes on Ultimate Speed Secrets](https://www.goodreads.com/notes/19027835-ultimate-speed-secrets/69038094-teeranai-tananusin?page=6)
- PRO (data engineering): Delayed throttle followed by an aggressive application produces exit oversteer and counter-steer corrections (see Q2). — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)

### Inferences
- Metrics the assistant can compute, given throttle and brake channels (iRacing exposes them, though they are not in the listed channel set):
  - **throttle-on point minus steering-peak point**, in lap distance or time. Negative means throttle before unwind, which flags a likely cause of apex understeer. Look for a second steering rise after throttle-on.
  - **steering at throttle-on as a fraction of peak lock**.
  - **brake-release end vs steering-peak**. Brake still on at peak lock means deep trail. Brake fully off well before turn-in means a missed rotation aid.
  - **apex-hold duration**: time or distance steering stays within some band of peak.
- A combined-g view (√(a_x² + a_y²) vs time) shows whether the transition from brake to steer to throttle stays near the limit or dips (coasting gap) or spikes (overload). This adapts the friction-circle idea to the listed channels. No published GTP numbers were found.
- GTP and LMP2 rotation behaviour will differ from front-engined GT3. A GT3-oriented forum notes that engine placement changes how deep to trail brake vs how early to throttle for rotation [snippet; [r/iRacing thread](https://lr.us.psf.lt/r/iRacing/comments/1f2qar1/gt3_drivers_help)]. GTP cars are mid-engined hybrids, so "unwind before throttle" in iRacing GTP still needs checking per car (inference).

### Gaps
- No source on how GTP hybrid deployment, front-axle torque or regen braking (for cars where iRacing models it) changes the steering/throttle relationship.
- No numeric guidance on how much steering can remain applied when throttle reaches 100% for prototype or GT3 cars.

## 5. Endurance specifics (consistency, tyre fall-off, traffic, cold tyres after stops, night, fatigue)

### Takeaway
Endurance drivers describe stints as a trade between pace and tyre life. They deliberately ease off to hold consistent laps, and traffic pushes the tyres out of their window. Out-laps on cold tyres (WEC has had no tyre warmers since 2023) are a known hazard, with many spins and crashes. I found little that is steering-specific. These sources support the context a coach should apply: expect higher steering-per-g and more corrections on cold or worn tyres and in traffic, and judge those laps against a matching reference.

### Cited Findings
- PRO (WEC Hypercar, Le Mans 2026): Alpine's António Félix da Costa: "My first triple stint was quite tricky. I spent a lot of time stuck in traffic behind other Hypercars, which made it very difficult to keep the tyres within their optimal operating window." Jules Gounon: "a vibration issue following a slight flat spot on a tyre" forced "us to cut a stint short." Charles Milesi on the aim: "avoid making mistakes." — [Alpine, "A night full of challenges for Alpine", 14 Jun 2026](https://www.alpine-cars.co.uk/fia-wec/news/a-night-full-of-challenges-for-alpine-2026.html)
- PRO (WEC Hypercar, Spa 2023, after the tyre-warmer ban):
  - Kobayashi on cold-tyre out-laps: "Because it's crazy dangerous, as you see how many people [are] spinning"; "You can gain 10 seconds on the track when the tyre is ready, but you can gain 10 seconds on out-lap."
  - Molina: "we struggle with the cold tyres, you need to be really careful in the out-lap."
  - Hartley crashed on his first lap out of the pits, which Vasselon called "a classic off on cold tyres."
  — [Motorsport.com, Apr 2023](https://www.motorsport.com/wec/news/kobayashi-concerned-by-crazy-dangerous-wec-out-laps-on-cold-tyres-at-spa/10462097/)
- PRO (WEC Hypercar): Raffaele Marciello, adapting from GT3 to Hypercar: "At the end it's more like the tires, the degradation, sometimes the outlap is very, very tricky." — [Sportscar365, 23 May 2024](https://sportscar365.com/?p=125106)
- PRO (tyre supplier): The driver must add heat gradually over the out-lap so the compound can generate grip. Pirelli has linked fronts sliding on a cold track to slow-corner understeer. [snippet, F1 context] — [Pirelli press, 2014 Chinese GP practice](https://press.pirelli.com/2014-chinese-grand-prix---practice-sessions/)
- PRO (Le Mans, night stint): BMW's Augusto Farfus said he tried not to push too hard and saved the tyres a bit to run at a consistent pace, and that this worked well. [snippet: BMW press attachment not fetched] — [BMW Group press](https://www.press.bmwgroup.com/global/article/attachment/T0113233EN/164053)
- PRO (Le Mans, older era): Guy Smith described a "really fine balance between maintaining fast and consistent lap times and not taking too many stupid chances when you encounter traffic." Losing time behind a backmarker beats a risky pass. [snippet] — [Autosport, Guy Smith race diary](https://www.autosport.com/wec/news/guy-smith-race-diary-10am-5026665/5026665/)
- PRO (Le Mans, rookie Buemi, older era): judging time lost vs risk in traffic: "If you are too kind, you will lose too much time." [snippet] — [Autosport](https://www.autosport.com/wec/news/100360/buemi-no-doubts-about-night-pace)
- PRO (data engineering): front degradation over a stint shows as more mid-corner understeer, and rear degradation as more exit corrections (see Q3). — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)

### Inferences
- Stint-aware steering coaching should:
  - exclude or separately grade out-laps and the first flying lap after a stop. Expect more steering per g and more reversals while tyres come in. The coaching point is "build heat gradually, don't chase the reference";
  - track steering-per-g and exit-reversal trends across the stint to separate tyre fall-off from driver error;
  - tag laps with traffic, where line changes and dirty air will inflate lock and corrections. iRacing gives car positions, so traffic can be detected (not covered by these sources).
- As grip falls, the minimum-steering knee (Q1) moves to lower lateral g. A driver who keeps the same steering amplitude as on new tyres is past the knee and scrubbing more. Coaching should be relative to the current knee, not the fresh-tyre reference lap (inference).

### Gaps
- No PRO or SIM source specifically describing how steering technique should change as tyres degrade, beyond general "be smoother / look after tyres".
- No source on line changes when passing or being passed and their steering cost, or on night-time effects on steering (beyond visibility) or fatigue effects on steering smoothness and correction rate. A driver-physiology source would be needed.
- iRacing GTP-specific cold-tyre behaviour and tyre-warmer rules were not covered.

## 6. Telemetry markers and coaching practice; telling driver steering issues from car balance

### Takeaway
Engineers and coaches overlay the driver's steering against a faster reference on the same car and setup. They look at four things:
- apex steering level and how long it is held;
- turn-in timing and rate;
- reversals and roughness;
- steering against lateral g (or yaw), to see whether added lock buys any turning.

A balance problem is consistent: across laps, across corners of a type, and for other drivers in the same car. A driver problem varies, and correlates with turn-in point, entry speed and throttle timing. Data must always be read together with what the driver feels.

### Cited Findings
- PRO (data engineering): "One way to answer this is by using overlays from a faster lap", comparing apex steering input, hold duration and carried speed. Variance channels quantify the time lost to a given technique difference. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): Driver-induced examples: early turn-in forcing more steering and a lower apex speed; inconsistent throttle blips and unsteady brake modulation on downshifts causing rear locking and entry instability, judged "a driver technique issue." Car-induced causes include mechanical imbalance, rearward brake bias, aero centre of pressure moving forward, and tyre degradation. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- PRO (data engineering): "the analysis of the logged data must be interpreted in conjunction with the feedback we get from our driver." Balance is relative to another driver, setup or tyre set. — [HP Academy](https://www.hpacademy.com/courses/professional-motorsport-data-analysis/cornering-performance-steering-data-and-balance)
- SIM: "Overlay your steering trace with that of a faster driver on the same track and car setup." Compare smoothness, timing and input levels, and look across the whole lap for whether one corner stands out. Understeer reads as "high steering angles with little lateral G-force increase." — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/a-delta-guide-get-a-grip-on-your-steering)
- SIM: Steering angle that keeps rising "without speed increase" or matching direction change flags understeer zones. Overlay with speed, throttle and brake, and check gear/RPM in case a wrong gear forces corrections. — [Fanatec](https://www.fanatec.com/us/en/explorer/products/steering-wheel/steering-input-telemetry/)
- SIM: Use the "Diff to Ref" steering chart. A sharp positive excursion of wheel angle vs the reference at initial throttle means not unwinding enough. — [Track Titan](https://www.tracktitan.io/study-plans/a4463edd-0169-4895-a7b8-644df1db64d1-accelerating-the-unwind)
- PRO: The MotoIQ article title states the thesis that many "handling issues" reported by drivers are really driver errors: holding the apex, shuffling hands, and so on. — [MotoIQ](https://motoiq.com/youre-doing-it-wrong-common-driver-errors-often-mistaken-for-handling-issues/3)
- PRO: Blayze says it is usually best to analyse your own driving to find which error (early turn-in, track not used, early throttle) is happening, and only if none applies, reduce entry speed slightly. — [Blayze, von Moltke](https://blayze.io/blog/car-racing/why-you-cant-open-your-hands-at-corner-exit)
- PRO (WEC): BMW's view, reported in a search summary, is that tyre wear is a consequence of balance and the aim is stable lap times without fighting an edgy car. [snippet: the source article was not identified or fetched, so treat as unverified] — no verified URL
- **Coaching phrases found verbatim in sources** (usable as templates):
  - "It's impossible to be really fast while always turning the wheel the same way." (Bentley)
  - "Focus on the timing and rate of release of the brakes" to rotate "with a minimum of steering." (Bentley)
  - "don't want to touch the throttle until we can start to unwind the steering wheel." (Racers360/Mazda)
  - "how early can I start to unwind the steering wheel" (Blayze) [snippet]
  - "Instead of driving the car out to your exit point, let the car go out there." / "start unwinding your steering a little earlier." (MotoIQ)
  - "Gradually increase throttle as you unwind the steering wheel." (Track Titan)
  - "Then once the weight is set, the turn can be more aggressive." (Blayze, Mullan)
  - "Use tiny corrections instead of sawing at the wheel mid-corner." (SimXPro) [snippet]

### Inferences
- **Suggested per-corner steering metrics for the assistant**, computed over a lap-distance window per corner and compared with the driver's best clean lap or a reference. These synthesise the sources; none of the thresholds are published, so calibrate per car, track and driver.
  1. Turn-in point (lap distance where steering leaves straight-line noise) vs reference.
  2. Turn-in rate (deg/s to ~80% of peak) and shape (progressive/linear/digressive, after Bentley).
  3. Peak lock vs reference, plus lap distance of peak.
  4. Time or distance held within a band of peak (apex hold).
  5. Unwind start vs throttle-on, and steering fraction at throttle-on.
  6. Reversal count (filtered, gap-thresholded) split into entry, mid and exit, and counter-steer events (steering sign opposite to the yaw/lateral-g direction).
  7. Steering-per-g (or understeer angle, if ratio and wheelbase are known), at the apex and as a curve; flag "steering ↑, lateral g ↔/↓".
  8. Steering integral per corner and per lap, trended over the stint.
- **Driver vs car decision rules** (inference built on the HP Academy and Blayze reasoning):
  - It is likely **car balance** when the same understeer or oversteer signature appears at the same corner type (slow/medium/fast, entry/mid/exit) lap after lap, at similar entry speed and turn-in point. It is more likely still if the signature grows steadily over the stint (tyres) or shifts with speed band (aero vs mechanical), and if the reference driver in the same car shows it too.
  - It is likely **driver technique** when the signature appears at some laps or corners but not others. It is also likely when it correlates with an earlier turn-in point, higher entry speed than the reference, throttle-on before unwind start, or abrupt turn-in rate, or when it disappears on the driver's own best lap.
  - Mixed case: a driver over-slowing, then adding early throttle, then getting understeer, then delaying throttle and stabbing it into exit oversteer (HP Academy chain). Fix the first error (entry) before attributing any of it to setup.

### Gaps
- No public MoTeC/Pi guide with explicit understeer-angle channel formulas was fetchable: the MoTeC forum now returns 403 and the AiM PDF was seen only as a snippet. The formula in Q2 Inferences is standard kinematics, not a vendor recipe.
- No published coach or engineer benchmarks such as "a good GT3/GTP driver makes ≤ N reversals per corner" or "peak lock within X° of reference". These would need to be learned from the user's own data.
- No iRacing-official coaching content on steering was found in this pass.
