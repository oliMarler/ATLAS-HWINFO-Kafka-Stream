# Endurance and sportscar race strategy (IMSA, WEC, Le Mans) for a sim race-engineer app

Research status: about 13 tool calls. Many fetches failed (HTTP 429/503/403), so most items below come from search-result summaries, not full article reads. Items marked [single-source] rest on one page; items marked [snippet-only] were not confirmed by reading the full page. Inferences are kept in the Inferences subsections.

## 1. How is a race plan built (stint lengths, fuel/energy/tyre models, stops, driver plan, scenarios) and how often is it revised?

### Takeaway
A plan starts from the longest legal/possible stint (fuel or virtual energy, tyre life) and splits race time into stints, then tests variants such as even, long-long-short, plus-one-stop and driver minimum times. In GTP the limit is energy, not litres, and stints are about 50 min.

### Cited Findings
- Meyer Shank Racing strategist Ryan McCarthy said GTP stints grew from about 35 min (DPi) to about 50 min, and that GTP strategy is energy management rather than fuel alone. [snippet-only] — [Racer, Jan 2023](https://racer.com/2023/01/28/insight-alternate-strategies-and-new-thinking-for-gtp-race-plans/)
- Same piece: IMSA mandated a longer pit stop to replenish the virtual energy tank, and up to eight tyre sets need to go two stints, with teams choosing how to double-stint them. [snippet-only] — [Racer, Jan 2023](https://racer.com/2023/01/28/insight-alternate-strategies-and-new-thinking-for-gtp-race-plans/)
- IMSA explainer exists on GTP virtual energy replenishment (page blocked to me, content not read). — [IMSA](https://imsa.com/news/2023/september/27/high-tech-pit-stops-how-does-gtp-virtual-energy-replenishment-work)
- Classic (GTLM/GTD era, 160-minute sprint-endurance races, i.e. same race length as the app target): GTLM and GTD cars run roughly 60 min on a full fuel load, so races split into about three stints. GTD needs at least 45 min of driver time, GTLM only 10 min. [single-source, older era] — [Sportscar365, Michelin IMSA Insider](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Same source lists the named stint-pattern options: Even split (pit every ~53-54 min; maximises time for the faster driver in GTD); Long-Long-Short (smaller last fill, fresher tyres at the end); Long-Short-Long (short middle stint gains track position when others pit or on a yellow); "Ohio" (slightly short first stint then long middle, tyre compound changes at each end); Plus One (extra stop, four shorter stints, risks a lap down but fresher tyres pay off with high wear or cautions). [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Same source: pit-wall screens run a programmed "ghost" car to predict where a clean stop rejoins in traffic; inputs are in-lap/out-lap times, pit lane length and speed limit, box location, service time; other variables are weather, fuel economy, traffic, track position, tyre wear, driver rotation. [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Same source: final-stop choice of "LIFO/FIFO": pit as soon as the fuel window opens (hoping a late caution shuffles you forward) or wait for a shorter fill and fresher tyres, accepting no-caution risk. [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Same source: green-flag runs have been long (5 h 34 min before VIR), so plans that bank on cautions often fail; Ford GT's one-stop fuel gamble at Lime Rock lost when the race ran green (Richard Westbrook: "It was a fuel game for us"). [snippet-only for Lime Rock] — [Motorsport.com](https://www.motorsport.com/imsa/news/ford-gt-lime-rock-strategy-933832/)

### Inferences
- For a 2h40 sim race, a baseline GTP plan is roughly 3 to 4 stints of about 40-50 min, with the tyre double-stint rule and energy cap as constraints. The numbers are from real-world IMSA, not iRacing, and iRacing fuel/tyre rules should be checked separately.
- The stint-pattern vocabulary above maps directly to app scenario A/B/C generation (even, short-middle, extra stop).
- Revision cadence: no source found stating how often teams formally re-plan. Practice implied by sources is a re-plan after every caution/incident and at each stop (inference).

### Gaps
- No source found on how teams quantify tyre degradation models, energy per lap targets, or scenario trees (A/B/C) in GTP.
- Revision frequency not sourced.
- Racer and IMSA energy pages could not be read in full.

## 2. Multi-class traffic: where time is lost, how GTP passes GTD/LMP2, how slower classes yield, pit-cycle traffic windows

### Takeaway
I found no authoritative real-world source on multi-class tactics in this research. What exists is sim-league etiquette plus the ghost-car pit-rejoin concept.

### Cited Findings
- Pit-wall "ghost" car projects the rejoin position and traffic after a stop. [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Sim-league conventions (not IMSA rules): the faster car initiates a clean pass; the slower car stays predictable on its normal line, does not defend under blue flags, may lift slightly on straights or brake earlier only if the lapping car is alongside; blue flags in GT are informational. [snippet-only, hobbyist rule sets] — [TheSimGrid rules (example)](https://www.thesimgrid.com/championships/14534/rules)

### Inferences
- A pit-cycle traffic window is the rejoin position relative to the slower-class pack; the ghost-car idea is directly implementable from lap data (inference).
- Hard-to-pass sections: the app already has a per-track traffic map (task #42); no sourced real-world list for Long Beach, Le Mans, Suzuka, Sebring was found.

### Gaps
- No driver/strategist interview on how GTP cars lose time in GTD/LMP2 traffic or how many seconds per pass.
- No source on IMSA/WEC rules for yielding to faster classes.

## 3. Safety cars, FCY, red flags and weather

### Takeaway
Cautions reshuffle the order via pit timing; the decisive factor is whether you have already pitted when the pits close, and whether you leave a car out to deny rivals a wave-around.

### Cited Findings
- Le Mans 2025: after a long wet safety-car period, cars that had not switched to slicks before pit closure before the restart were stuck, and cars that had pitted for slicks gained. Fuel difference of one stop per stint was also cited by Alpine's team manager, with slow zones and safety cars able to shift that gap. [snippet-only] — [24h-lemans.com, Sinault](https://www.24h-lemans.com/en/news/24-hours-of-le-mans-philippe-sinault-alpine-its-anybodys-game-56415); [DailySportsCar](https://www.dailysportscar.com/2025/09/07/heavy-rain-safety-car-confusion-sees-lone-star-le-mans-red-flagged.html)
- Le Mans safety-car procedure: pit exit closed (red light) while pit entry stays open; overtaking prohibited from procedure start until the line; ACO revised the procedure since 2023 (merge/pass-around trials, drop-back dropped for 2024). [snippet-only] — [Endurance-Info](https://en.endurance-info.com/auto/article/105876-24-h-le-mans-safety-car-procedure-completely-revised)
- Pit lane limit 60 km/h at Le Mans 2026 briefing notes. — [FIA WEC briefing notes](https://fiawec.alkamelsystems.com/Results_NoticeBoard/14_2026/03_24%20Hours%20of%20Le%20Mans/006_Doc%206%20-%20BRIEFING%20NOTES.pdf)
- Rolex 24 2025: Porsche Penske reportedly used a late FCY by pitting the second-place car and leaving the leader out, denying rivals a wave-around back onto the lead lap; the race had 14 FCYs. [single-source, snippet-only, unverified detail] — [Speedsport](https://speedsport.com/sports-cars/imsa/three-takeaways-63rd-rolex-24-at-daytona/)
- Classic examples: JDC-Miller lost a ~20 s lead when Acura rivals (MSR, WTR) pitted just before a caution; AXR/Whelen's Derani led after staying out while others pitted under caution. [snippet-only, undated] — [Motorsport.com](https://www.motorsport.com/all/news/jdc-cadillac-rolex-daytona-bittersweet/7763083/); [Sportscar365](https://sportscar365.com/imsa/iwsc/axr-pit-call-puts-derani-in-front-after-six-hours/)
- Petit Le Mans 2025: many cautions; all front-runners needed a late fuel-saving effort/splash-and-dash; Aston Martin stopped early and was rewarded with P2-P3 when others pitted; Lamborghini made its splash with ~5 min left and finished P4. [snippet-only] — [The Race](https://www.the-race.com/endurance/winners-and-losers-from-imsas-fraught-2025-finale/); [Motorsport.com](https://www.motorsport.com/imsa/news/2025-imsa-petit-le-mans-results-cadillac/10766956/)
- Petit Le Mans (earlier year, unverified): Lamborghini extended a stint hoping for a late caution; none came and Grosjean pitted again with under 5 min left. [snippet-only] — [Only Endurance](https://www.onlyendurance.com/petit-le-mans-imsa-final-hour-strategy-analysis)
- Lone Star Le Mans 2025 (COTA): most of the field followed the leading safety car into the pits during a planned swap and the race was red-flagged. [snippet-only] — [DailySportsCar](https://www.dailysportscar.com/2025/09/07/heavy-rain-safety-car-confusion-sees-lone-star-le-mans-red-flagged.html)

### Inferences
- Decision rule for the app: when a caution is called, compare (a) fuel/energy window open, (b) rival pit status in class, (c) pit-closed risk; stop if the stop cost under yellow is much less than green.
- Splitting strategy between two same-team cars (one stays out) is a documented tactic but not widely sourced here.

### Gaps
- No sourced tyre-choice guidance in changing conditions beyond the Le Mans 2025 snippets.
- Rolex 2025 winner detail conflicted: one low-quality page named car #2 as winner; treat as unreliable; the Speedsport page is about Penske but I did not read it.
- Red-flag strategy (refuelling rules, tyre changes) not found.

## 4. Risk management, consistency vs pace

### Takeaway
Little sourced here. Evidence is that late-race fuel margins and gambles on cautions decide results, and that no-caution outcomes punish gamblers.

### Cited Findings
- Ford GT Lime Rock and Lamborghini Petit gambles failed when no caution came (see above). [snippet-only]
- Porsche Penske at Rolex 2025: team director credited a two-car approach, cars combined to lead 517 of 781 laps. [snippet-only, single-source] — [Speedsport](https://speedsport.com/sports-cars/imsa/three-takeaways-63rd-rolex-24-at-daytona/)
- Michelin's Ken Payne described IMSA teams as "creative, opportunistic and aggressive." [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)

### Inferences
- A 2h40 race is closer to a sprint-endurance: less car preservation, more track position and incident avoidance. Not sourced.

### Gaps
- No source on championship-context risk, car preservation or when to push/hold. Needs targeted interviews.

## 5. Classic mistakes, famous calls, and simulation tools in practice

### Takeaway
Documented failure pattern: banking on a caution that does not come (Lime Rock, Petit). Simulation: academic WEC work uses Monte Carlo and stochastic dynamic programming; teams in F1 describe Monte Carlo practice; no IMSA/WEC team-specific tooling source found.

### Cited Findings
- 2022 paper "Competitors-Aware Stochastic Lap Strategy Optimisation for Race Hybrid Vehicles": Monte Carlo simulation of rival positions from past sector-time and overtaking statistics, genetic-algorithm candidate energy strategies, stochastic dynamic programming picking the strategy each lap; validated on real race stint data per the authors. [snippet-only] — [arXiv/ar5iv 2203.00084](https://ar5iv.labs.arxiv.org/html/2203.00084)
- F1 context: Rob Smedley says teams moved from deterministic tools to Monte Carlo statistical methods; Oracle Red Bull Racing describes large-scale simulation. [snippet-only, F1 not endurance] — [Oracle](https://blogs.oracle.com/cloud-infrastructure/oracle-red-bull-racing-increases-simulations-and-sharpens-decision-making-on-the-track-with-oracle-cloud-infrastructure)
- Hobbyist sim tool "Simulator Controller" has a Monte Carlo traffic analysis for endurance strategy. [single-source, forum] — [Reiza forum](https://forum.reizastudios.com/threads/simulator-controller-with-ai-based-virtual-assistants-race-engineer-and-race-strategist.19026/page-2)

### Inferences
- The repo already has a Monte Carlo race plan simulation (task #35); the paper suggests including rival-position distributions and caution probability as inputs.

### Gaps
- No post-race IMSA/Le Mans analyses with numbers beyond summaries; famous Le Mans decisions (e.g. 2016 Toyota, 2011 Audi/Peugeot) not researched.

## 6. KPIs a strategist watches live

### Takeaway
Only the pit-wall list from the Sportscar365 piece is sourced; the rest is inferred.

### Cited Findings
- Inputs to live pit decisions: in/out lap times, pit-lane time loss, fuel economy, traffic, track position, tyre wear, driver rotation, weather, projected rejoin ("ghost car"). [single-source] — [Sportscar365](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)

### Inferences
- Candidate KPIs for the app: in-class gap and pit-cycle position (virtual order after everyone stops); fuel/energy delta vs plan in laps; tyre deg trend; rejoin traffic; time-to-caution-window. Not sourced.

### Gaps
- No strategist interview listing KPIs; searches returned race reports, not method.
