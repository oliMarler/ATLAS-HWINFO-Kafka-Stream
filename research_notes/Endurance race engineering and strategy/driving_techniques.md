# Endurance and Sportscar Driving Techniques (IMSA / WEC / Le Mans; transfer to sim)

Labels: [PRO] = real-world professional racing. [SIM] = sim coaching or sim game guide. [SIM-LMU] = Le Mans Ultimate guide (a different sim from iRacing; use as analogy only). Most coverage found is thin on hard numbers. Pro sources rarely publish per-lap savings; those are gaps, not invented.

## 1. Fuel and energy saving (lift and coast, shift points, line, virtual energy)

### Takeaway
In GTP/Hypercar the limit is a virtual energy tank (MJ per stint, set by BoP) that combines fuel and hybrid torque, and drivers save it mainly by lifting and coasting, which pros equate with saving fuel. The only hard per-lap number found is a sim one (LMU, about 1.45 L and 0.7 s per lap); no pro per-lap savings were found.

### Cited Findings
- [PRO] Virtual tank combines fuel used by the engine with hybrid torque, measured by rear-axle sensors (both axles on LMH). Stint energy in MJ and a replenishment rate in MJ are set by BoP, so they vary by car and track. — [Motorsport.com](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- [PRO] Example limit: Cadillac and BMW stint limit 920 MJ at start of the year, 902 MJ by the Indianapolis round. First violation = 100 s hold on top of the stop, each further offence adds another 100 s. Tank only depletes once the race begins; pit lane driving does not use it. — [Motorsport.com](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- [PRO] Philipp Eng (BMW): saving energy is "basically the same thing as to save fuel"; the main method is "lifting and coasting". Eng: "You definitely need that guidance on what to do" and engineers find it "quite a big challenge to always get the energy right". Sebastien Bourdais: drivers "mostly have to keep an eye on the energy you have left to finish the race." Iain Watt (Action Express): "We're governed by energy." — [Motorsport.com](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- [PRO] Teams can exploit knowledge of starting energy in races with many yellows (Bourdais: "tricks"); can be "plugged in" and replenish the virtual tank without taking fuel. — [Motorsport.com](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- [PRO, older LMP1 era] Anthony Davidson (Toyota TS050 era) described treating long Le Mans straights as drag strips then easing off once at speed to meet the per-lap fuel target (secondhand via search summary of RACER article; the RACER page itself returned HTTP 429 and was not read in full). — [RACER](https://racer.com/2016/06/18/lm24-lmp1-fuel-saving-101/)
- [SIM-LMU] Method: lift at a reference board, then brake later; Spa example lifts at the 200 m board and brakes "10 – 20 meters later than usual" for Turn 5. Keep normal apex speed; shift just before the shift light rather than revving to the limiter; fully lift before braking (throttle/brake overlap wastes fuel). — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/mastering-lift-and-coast-how-to-save-fuel-without-sacrificing-speed/)
- [SIM-LMU] Only hard numbers found: Spa, full fuel, default setup: flat out 2:22.5 using 3.45 L; lift and coast 2:23.2 using 2.0 L. That is about 1.45 L saved for 0.7 s lost per lap. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/mastering-lift-and-coast-how-to-save-fuel-without-sacrificing-speed/)
- [SIM-LMU] Clutch-pull coasting is sim-only, unrealistic, may be patched out; needs a button/analogue clutch. Same article. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/mastering-lift-and-coast-how-to-save-fuel-without-sacrificing-speed/)
- [SIM-iRacing] Fuel saving is pointless in races of an hour or less but critical in longer ones; stretching each stint by one lap can remove a splash-and-dash and a whole stop; do some lift and coast before refuelling stops even if a full lap is not saved; practise full-stint consumption. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/guide-to-strategy-in-iracing/), [Fanatec](https://www.fanatec.com/au/en/explorer/games/gaming-tips/how-to-get-ready-for-an-iracing-special-event/)
- [SIM-iRacing GTP] ERS maps listed as No Deploy, Qual, Attack, Balanced, Build; race on Balanced, switch to Attack to overtake; balance deployment against braking regen. Prototype tyre change budget about 30 s. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/guide-to-strategy-in-iracing/) (as extracted by fetch tool; verify against the iRacing car manual)
- [SIM-LMU] Lift and coast regenerates less under braking; battery at 100% loses regen help so it must also be drained on acceleration; front motor deploys above roughly 190 km/h (BoP-set); engineering "NRG" gauge hitting 0% gives a 100 s penalty in LMU. — [SimRacingCockpit / Traxion search summaries](https://traxion.gg/how-to-manage-virtual-energy-in-le-mans-ultimate/) (search snippet only, not fetched; treat as unverified)
- [SIM] Anti-sim claim worth noting: the Box This Lap guide says TC intervening over bumps/kerbs costs small power each event but adds up over hundreds of events and affects fuel use (single-source, plausible but unquantified). — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)

### Inferences
- A coaching assistant can express energy targets as "lift point moved N metres earlier, brake point N metres later, same apex speed" which is the teachable form; per-lap savings must come from the user's own stint data, since pro numbers are not public.
- Because pros equate energy saving with fuel saving, a fuel-per-lap target readout is a reasonable proxy for iRacing GTP, but iRacing's hybrid regen interaction (lifting earlier reduces regen) should be flagged.
- Likely call phrasing: "energy" / "target" / "plus/minus on energy" is inferred, not found; no source gave actual radio wording.

### Gaps
- No pro-published energy saved per lap (MJ or %) from lift and coast; no named engineer call wording found.
- No source on line choice or shift points for fuel in modern Hypercar/GTP (shift-early advice is sim-only).
- iRacing-specific GTP fuel numbers not found.

## 2. Tyres, brakes and in-car balance over a stint

### Takeaway
GTP stints are commonly double-stint tyres with long warm-up, so drivers manage tyre life through restraint and gradual adjustment; no pro source gave brake bias/ARB/TC change values over a stint. Sim guides give a qualitative pattern: conservative TC early, more slip when warm, more protective late; re-check bias as grip changes.

### Cited Findings
- [PRO] Connor De Phillippi (BMW), 2023: "Obviously you have to double-stint some tires but you want to avoid being on those tires as long as you can"; drivers have "some kinda scope to make a difference" in managing a stint, not "flat-out from beginning to end"; GTP cars "have a lot of power, the tire takes a lot longer to come up to speed and we have less downforce"; at Long Beach qualifying "it took everybody 11, 12, 13 laps to get the tires to really switch on"; wheelspin in 4th and 5th gear on his out-lap; on old tyres "It's going to be a handful". Recent driveability gains came from "traction control, braking, how the whole hybrid system is working". — [Motorsport.com](https://www.motorsport.com/imsa/news/gtp-tire-challenges-allow-drivers-to-make-a-difference/10467756/)
- [PRO] IMSA GTP double-stinting norm; Porsche Penske ran an entire 100-minute Long Beach race on one set and won (via search summary of Motorsport.com article; the 11-13 lap figure above is from the fetched page). — [Motorsport.com](https://www.motorsport.com/imsa/news/gtp-tire-challenges-allow-drivers-to-make-a-difference/10467756/)
- [PRO] Acura's TC is in-house developed and continuously learns rear/lateral grip (David Salters, HRC US); GTP wheels carry many driver-adjustable functions (Jenson Button). — [The Drive](https://www.thedrive.com/news/jenson-button-says-acura-imsa-gtp-is-more-complicated-than-an-f1-car-but-why)
- [SIM-iRacing GTP] Brake bias: about 44% cited as a value some drivers use (reference only; depends on master cylinder sizing); migration examples around -3 to -5 (illustrative); make small changes and judge over several zones; re-check bias during a stint as tyres wear. ARB: softer front bar helps rotation, stiffer favours stability; more conservative on cold tyres but do not change lap to lap. TC: use lowest intervention you can drive consistently; conservative early, more slip when warm, more protective as wear increases. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- [SIM] Downforce drops quickly approaching slow corners in GTP; balance aero and mechanical grip deliberately. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/iracing-guide-becoming-the-best-prototype-driver-possible/)
- Low-quality source (content farm), not relied upon: rear tyre wear may require bias forward to avoid rear lockup. Single-source, unverified. — [Repreve page](https://signup.repreve.com/?p=7109)

### Inferences
- Longer warm-up (about 11-13 laps to switch on in one qualifying case) implies out-laps on cold GTP tyres need traction-limited, gentle throttle; this is an extrapolation from one quote.
- As fuel burns the car gets lighter and tyres wear, so rear-limited exits plausibly need TC/bias re-checks; the direction of change is not confirmed by a pro source.

### Gaps
- No pro source on brake bias, ARB or TC change schedule through a stint; no brake temperature or wear numbers; no pressure/temperature window data; no traction-limited vs lateral-limited stint guidance from named drivers.

## 3. Traffic management (multi-class)

### Takeaway
Pros stress momentum, prediction of where slower cars will go, and clear communication; the faster class is responsible for safe passing and slower cars should hold their line. No numbers on time lost were found.

### Cited Findings
- [PRO] Anthony Davidson: "it's more about keeping momentum up in the traffic"; "it's a do-or-die manoeuvre and anything but to lift off is your option"; lapping is critical and "more mistakes will happen" (LMP1 era, 2011). — [Autosport](https://www.autosport.com/wec/news/davidson-rules-make-traffic-harder-4446267/4446267/)
- [PRO] Nick Tandy: GT3 cars have ABS so are better in slow-speed braking, making dive-bombing harder; decide between risking corner entry or waiting for a straight. Alex Riberas (Heart of Racing) said LMGT3 cars brake latest and hesitation after being passed can cause incidents; stressed communication. Rahel Frey: problem when Hypercars rejoin the line too quickly under braking; spotters and in-car traffic audio help. Brendon Hartley (2022): predict where slower GT cars will go; most passes on straights. — via search summary of [Motorsport Week](https://motorsportweek.com/?p=167996) and [Car Magazine](https://carmagazine.co.uk/features/car-culture/le-mans-2022-traffic) (Car Magazine page returned HTTP 402; quotes are search-summary level, not verified in full).
- [SIM-iRacing] Plan overtakes around slower cars to minimise time lost; when lapped hold your line and let faster cars pass ("letting the faster cars navigate themselves around you"); traffic luck evens out over long races; multi-class also gives drafting. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/guide-to-strategy-in-iracing/)
- [SIM-iRacing GTP] Wait for a better gap and use GTP acceleration after the apex rather than forcing a pass that compromises entry and exit; read traffic several corners ahead. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)

### Inferences
- A coaching rule consistent across sources: pass on straights/exits, avoid committing in braking zones against GT3; predictable lines for the car being passed.

### Gaps
- No quantified time lost per pass or per lap in traffic; no spotter-call vocabulary details; limited WEC/IMSA-specific etiquette beyond quotes.

## 4. Consistency, focus, night, rain, driver changes, stint length

### Takeaway
Pros describe endurance as risk-minimising with full effort within limits; night driving mostly shifts references and vision. Only fragments were found for hydration, rain, handovers and stint length.

### Cited Findings
- [PRO] Night: Marcel Fässler says drivers push back braking points and change lines in the dark; Stéphane Richelmi: fewer visual markers heighten sense of speed; Nicolas Lapierre: oil traces harder to see; Fässler: prototype headlights make judging distance to a faster car hard. — [24h-lemans.com](https://24h-lemans.com/en/news/out-of-the-darkness-and-into-the-light-night-driving-at-the-24-hours-of-le-mans-49490)
- [PRO] Norman Nato: tiredness is more physical/mental (stress, lack of sleep) than visual; Stoffel Vandoorne: body's adjustment to light is the main night difficulty; Martin Plowman: field of vision narrowed as adrenaline faded during a long safety car. — via [24h-lemans.com](https://24h-lemans.com/en/news/the-24-hours-of-le-mans-a-feast-for-the-eyes-59084) and [Autosport](https://www.autosport.com/wec/news/24-hours-vision-at-le-mans/6649178/) (search-summary level).
- [PRO] Nicolas Lapierre: modern Le Mans amounts to "six to eight stints full speed ahead"; no driver may drive more than four hours in a six-hour period. — [24h-lemans.com](https://24h-lemans.com/en/news/when-the-24-hours-of-le-mans-turns-into-a-sprint-for-drivers-50588) (search-summary level)
- [SIM-iRacing GTP] Practise full race-condition stints, not hot laps (lap 18 differs from lap 2); test: "could I drive this car for two hours without being afraid of it?"; use roughly 90-95% of potential over hundreds of laps; illustrative: a tenth per lap over 20 laps is about 2 s but a four-minute repair erases it. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- [SIM-iRacing] Practise double-stinting in varied conditions; stops with tyres and fuel are longer than fuel only; prototype tyre change about 30 s. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/guide-to-strategy-in-iracing/)
- [PRO] Driver changes can take as little as 10-15 s in endurance generally (generic page). — [Ross Bentley / Speed Secrets](https://speedsecrets.com/?p=38811)

### Inferences
- Lap-time target windows (e.g. within a few tenths of a target) are standard practice but no source quantified them; the Box This Lap 90-95% figure is a sim coach's heuristic.

### Gaps
- Nothing on hydration, rain/drying technique, out-lap/handover technique, or double-stint driver rules beyond the above. Ross Bentley's Endurance Racing Guide eBook was mentioned but not obtained.

## 5. Sprint/qualifying vs endurance driving: what drivers say

### Takeaway
Named drivers frame endurance as risk minimisation and mechanical sympathy while still extracting the car; big kerbs and one-lap aggression are the things to drop. Counterpoint: modern WEC stints are near-sprint.

### Cited Findings
- [PRO] Robert Kubica: comparing F1 to endurance is like "comparing sprint race runners to marathons"; in endurance you "have to minimize your risks" while extracting maximum; finishing without "the big issues – technical, sporting or driving" comes first. — [PlanetF1](https://www.planetf1.com/news/robert-kubica-f1-sprinters-le-mans-marathons)
- [PRO] Top Gear interviewee (driver not identified in my summary): a good endurance driver controls aggression and knows when to conserve; hitting big kerbs chasing a lap can hurt the car. — [Top Gear](https://www.topgear.com/car-news/british/how-become-endurance-driver) (search summary; single-source, speaker not verified)
- [PRO] Nicolas Lapierre (counterpoint): Le Mans is now six to eight full-speed stints. — [24h-lemans.com](https://24h-lemans.com/en/news/when-the-24-hours-of-le-mans-turns-into-a-sprint-for-drivers-50588)
- [PRO] De Phillippi (see section 2): not "flat-out from beginning to end". — [Motorsport.com](https://www.motorsport.com/imsa/news/gtp-tire-challenges-allow-drivers-to-make-a-difference/10467756/)

### Inferences
- Teachable contrasts: fewer kerb strikes, no overdriving cold tyres, earlier lifts for energy, smoother inputs; all consistent with sources but "smoothness" as a stated driver claim was not directly quoted from a named driver.

### Gaps
- No Ross Bentley "Speed Secrets" endurance chapter text obtained; no named-coach quantification.

## 6. Sim-specific coaching (iRacing and others)

### Takeaway
Sim coaches (Coach Dave Academy, Box This Lap) teach: practise full stints, fuel-per-lap spreadsheets, lift-and-coast with reference boards, conservative TC/ARB early, and small single changes. Nothing found on iRacing tyre-wear model internals.

### Cited Findings
- [SIM-iRacing] Fuel use per lap and laps per stint should be computed pre-race with a spreadsheet and full practice stints. — [Fanatec](https://www.fanatec.com/au/en/explorer/games/gaming-tips/how-to-get-ready-for-an-iracing-special-event/)
- [SIM-iRacing GTP] Do not change multiple parameters at once; a 24-hour race brings changing temperatures, tyre state and fatigue so the car must be drivable over long stints. — [Box This Lap](https://boxthislap.org/iracing-gtp-endurance-guide-beginners/)
- [SIM-iRacing] Some iRacing series use smaller tanks than expected to force stops. — [Coach Dave Academy](https://coachdaveacademy.com/tutorials/guide-to-strategy-in-iracing/)
- [SIM-LMU] LMU virtual energy guides: NRG mechanics, 100 s penalty at 0% (see section 1). — [Traxion](https://traxion.gg/how-to-manage-virtual-energy-in-le-mans-ultimate/)

### Inferences
- iRacing GTP may not enforce a virtual-energy penalty the way LMU does; do not port LMU penalty rules without checking the iRacing GTP manual.

### Gaps
- No iRacing forum threads or official articles on tyre-wear model, Aston Martin Valkyrie / Porsche 963 specific stint technique, or sim fuel-saving numbers for iRacing GTP. Not searched: iRacing forums directly.
