# Pit strategy in endurance and sportscar racing (IMSA, WEC, 24h; GTP/Hypercar, LMP2, GT3)

Research status: coverage is partial. Several primary sources (IMSA sporting regs PDF, IMSA virtual-energy article, FIA WEC PDF, Racer article) could not be fetched (403/429/binary), so some claims rest on search-result summaries rather than full-page reads; those are marked "(search summary only)". Little hard pit-loss data was found.

## 1. Elements of a stop, timing costs, rules, pit loss per circuit

### Takeaway
A stop is fuel/energy + tyres + (often) driver change, with fixed pit-lane speed and, in GTP/Hypercar, a refill governed by virtual energy rather than litres. Published numeric pit-loss per circuit was NOT found; only qualitative and a few rule numbers.

### Cited Findings
- Pit lane speed limit: IMSA consumer guide says 60 km/h strictly enforced, drive-through penalty for speeding (page dated; confirm vs current regs; search summary only) — [IMSA Understanding the Sport](https://www.imsa.com/weathertech/discover/understanding-the-sport/)
- The same IMSA guide calls changing four tyres in under 25 s "typical"; this is description, not a rule (search summary only) — [IMSA Understanding the Sport](https://www.imsa.com/weathertech/discover/understanding-the-sport/)
- WEC Hypercar pit lane limit 60 km/h; refueler is the only person allowed to operate the fuel line; Genesis GMR-001 takes 80 L over about 40 s; after hose disconnects, pneumatic jacks lift all four wheels in about 1 s — [Genesis Magma Racing 2026 season guide pt 3](https://newsroom.genesis.com/genesis-magma-racings-2026-wec-season-guide-part-3-pit-stops/) (search summary only)
- Refuelling and tyre changing are not done simultaneously in WEC (forbidden to change tyres while refuelling); a fuel+tyre stop can take about 20 s; fresh set costs about 15 s extra; driver swaps are generally done at tyre stops because the longer stop hides the swap (secondary Le Mans explainer; "20 s"/"15 s" are approximate journalism) — [24h-lemans.com pit stop tactics](https://www.24h-lemans.com/en/news/pit-stop-tactics-a-major-factor-at-the-24-hours-of-le-mans-60740)
- 2025 Rolex 24: BMW #24 penalised with a drive-through for refuelling while the car was on its jacks (illustrates work-area/sequence rules and their penalties) — [Racer](https://racer.com/2025/01/25/rolex-24-hour-2-pit-error-costs-bmw)
- IMSA 2018 bulletin: minimum refuelling times to fill from empty were 30 s prototypes, 34 s GTLM, 40 s GTD; the bulletin said there was no minimum pit stop time and short fills were legal. Dated (2018), pre-GTP; current values not confirmed — [Frontstretch](https://frontstretch.com/2018/03/01/imsa-mandates-refueling-times-land-motorsport-penalty)
- IMSA now controls refuel rate via restrictors tuned in BoP (secondary) — [Sportscar365](https://sportscar365.com/imsa/iwsc/land-explains-daytona-refueling-bop-penalty/) (search summary only)
- WEC 2021 Hypercar refuelling decision: refuelling time must exceed 35 s x (energy used in previous stint / max stint energy), special rule under safety car; superseded by later decisions (see Q4) — [FIA WEC 2021 D0025](https://www.fia.com/sites/default/files/wec_2021_d0025_hypercar_refuelling_23042021_0.pdf) (search summary only)
- IMSA GTP: longer pit time mandated for the energy fill; stints about 50 min in GTP vs about 35 min in DPi (strategist quote via search summary) — [IMSA article](https://www.imsa.com/news/2023/09/27/high-tech-pit-stops-how-does-gtp-virtual-energy-replenishment-work/) (fetch blocked)
- Pit timing factors listed by Racer/Michelin: in-lap and out-lap times, pit lane length and speed limit, pit box location, fuel/service time; teams use a "ghost car" on the pit stand screen to predict where they rejoin — [Sportscar365 Michelin Insider pit stop math](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Long Beach 2023: #10 WTR Acura lost 10 s in the pits to a driver-change issue while taking tyres — [Motorsport.com](https://www.motorsport.com/imsa/news/porsche-963-inspired-long-beach-no-tires-call/10600176/) (search summary; also see Sportscar365 p=114708)

### Inferences
- Pit loss = pit lane transit at 60 km/h versus racing speed (track-specific, depends on pit lane length) + stationary time + out-lap tyre warm-up. The app should measure pit loss from its own data per track (in-lap + stop + out-lap minus 2 flying laps) rather than rely on a table. (inference)

### Gaps
- No per-circuit pit-loss seconds (Daytona, Sebring, Road America, Le Mans etc.) found in any source.
- Exact current IMSA minimum refuel/stop times, work-area rules (crew count, tyres/fuel sequencing) and penalty list not retrieved; Articles 32 and 36 of the IMSA Sporting Regs reportedly cover pit entry/exit and wheel/tyre changes but text not read (2026 PDF returned 403).
- Seconds per litre not found: only the WEC 80 L/40 s Genesis figure (about 2 L/s, single source, derived by me; inference).

## 2. How teams decide when to stop

### Takeaway
Fuel/energy window sets the earliest/latest stop; within it teams choose among stint patterns and react to FCYs. Pit-sequence/traffic and tyre state shape the choice.

### Cited Findings
- 2h40 sprint (VIR example, GTLM/GTD era): full fuel is about 60 min, so 160/3 gives a window of about 53-54 min; GTD min drive time 45 min (GTLM 10 min). Named patterns: Keep It Simple (equal stints), Long-Long-Short, Long-Short-Long (short middle stint gains track position if yellow), Ohio (short first, long middle), Plus One (extra stop; risk of losing a lap) — [Sportscar365 Michelin Insider](https://sportscar365.com/imsa/iwsc/michelin-imsa-insider-pit-stop-math/)
- Last-stop gamble: some teams pit as soon as the window opens expecting a caution to shuffle order; others wait for shorter fill and fresher tyres, risking no caution — same source.
- Mosport 2h40 GTD example: AO Racing pitted when the first FCY came out two minutes after (search summary; fetch not done) — [Sportscar365 p=81567](https://sportscar365.com/?p=81567)
- Road America 2024: late yellow with about 40 min left opened a fuel gamble; Conquest finished GTD PRO on a single fuel stop with a final stint of just over 92 min; Vasser Sullivan tried a 90+ min stint but had to stop inside the final five minutes — [Motorsport.com](https://www.motorsport.com/imsa/news/road-america-imsa-braun-bennett-win-after-brave-fuel-gamble/3154559/), [Endurance-Info](https://en.endurance-info.com/auto/article/112975-conquest-ferrari-and-turner-bmw-capture-first-wins-season) (search summaries)
- Le Mans 2026 race report: BMW consistently did 13-lap stints vs Toyota mostly 12; Alpine manager: "We are banking on one more pit stop than Toyota per stint" (search summary) — [FIA WEC headlines after 8 hours](https://www.fiawec.com/en/news/the-headlines-after-8-hours-at-le-mans/13628), [24h-lemans.com Sinault](https://www.24h-lemans.com/en/news/24-hours-of-le-mans-philippe-sinault-alpine-its-anybodys-game-56415)
- Drivers stretch tyres over two to four stints at Le Mans (secondary) — [24h-lemans.com](https://www.24h-lemans.com/en/news/pit-stop-tactics-a-major-factor-at-the-24-hours-of-le-mans-60740)

### Inferences
- Undercut/overcut, class pit sequencing and traffic at pit exit: no specific sourced numbers found. The ghost-car tool (above) shows teams predict rejoin traffic. Undercut value = (old-tyre lap time loss over the window) minus (out-lap warm-up loss); needs measured degradation. (inference)

### Gaps
- No strategist interview with numeric undercut/overcut sizes; no class pit-sequencing (GTP vs GTD) source; Racer GTP strategy article fetch returned 429.

## 3. Fuel-only vs tyre-and-fuel stops

### Takeaway
Only anecdotal sourced examples; no break-even formula or numbers published in what I could access.

### Cited Findings
- Long Beach 2023 (100 min, one mandatory stop): Porsche #6 skipped tyres and double-stinted a set, exploiting GTP tyre warm-up problems; stop was much faster than rivals', gaining track position; Tandy: pace deficit drove the call and the final 40 min were guesswork; Diuguid: "Our strategy last year was born out of a performance deficit"; with a softer compound and extra set in 2024 a no-tyre call was "less likely", traffic a bigger concern — [Motorsport.com](https://www.motorsport.com/imsa/news/porsche-963-inspired-long-beach-no-tires-call/10600176/), [Sportscar365 p=114708](https://sportscar365.com/?p=114708)
- Sebring 2026 (search summary): lead changed in pits when #7 Porsche took fuel only and #6 took tyres; #7 won — [Porsche race report](https://racing.porsche.com/articles/imsa-sebring-race-report-2026)
- Rule context: the Michelin Insider piece notes IMSA does not mandate minimum stop time (2018) so short fills are legal — [Frontstretch](https://frontstretch.com/2018/03/01/imsa-mandates-refueling-times-land-motorsport-penalty)

### Inferences
- Break-even (inference, no source): fuel-only wins when (tyre change time + new-tyre warm-up loss, if tyre change is serial after fuel) < (old-tyre lap-time penalty x laps remaining on that set) + track position value. Because tyre work is serial after fuel in WEC (see Q1), a short fuel fill leaves the tyre time as pure extra, so in the tyre-always rule of the app's driver the 35 L threshold is the driver's own heuristic, not found in sources.

### Gaps
- No numbers for old-tyre grip loss, out-lap warm-up loss, or seconds saved by skipping tyres (Motorsport.com article states none). No per-litre fuel time.

## 4. Fuel / virtual energy in stop planning; stop counts

### Takeaway
GTP/Hypercar stints are limited by BoP-set stint energy (MJ) tracked in a virtual tank; refill rate is fixed by the regulations, so stop length scales with energy added, and fuel-saving also saves energy.

### Cited Findings
- Virtual tank = fuel energy + hybrid torque integrated from driveshaft sensors; stint energy set by BoP per car/track (BMW and Cadillac 920 MJ at season start to 902 MJ at Indianapolis); BoP also sets refill rate; exceeding limit costs 100 s hold plus stop first offence, +100 s each further; tank depletes only once racing starts and pit lane driving is exempt; teams needn't fill fully (Watt: about 25 s worth of energy, roughly two-thirds tank); cars can stay connected to the probe to finish energy replenishment; a side sensor detecting fuel flow triggers the top-up (Action Express failure at Sebring cost time); lift-and-coast saves both fuel and energy — [Motorsport.com virtual energy](https://www.motorsport.com/imsa/news/how-virtual-energy-has-become-a-defining-principle-in-hypercar-racing/10531672/)
- 2023 Petit Le Mans stint energy: 915 MJ Acura, 907 Porsche, 903 Cadillac/BMW (search summary) — [IMSA article](https://www.imsa.com/news/2023/09/27/high-tech-pit-stops-how-does-gtp-virtual-energy-replenishment-work/)
- WEC 2025 Hypercar technical decision: refill rate PPUEnergyFlow = PPUEnergyStint / 40 s (full stint energy in 40 s), plus a BoP-defined docking time before the refill triggers; negative tank incurs penalty and must be repaid at the next stop at the flow rate (same in 2023/2024) (search summary; PDF unreadable via fetch) — [FIA WEC 2025 D06](https://api.fia.com/sites/default/files/wec_2025_d06_hypercar_technical_information_12022025.pdf), [FIA WEC 2023 D0026](https://api.fia.com/sites/default/files/wec_2023_d0026_hypercar_refuelling_01032023.pdf)
- Le Mans cars refuel about 30 times in 24 h (old secondary figure); 2026 Le Mans stints 12-13 laps (see Q2) — [24h-lemans.com](https://www.24h-lemans.com/en/news/pit-stop-tactics-a-major-factor-at-the-24-hours-of-le-mans-60740)
- 2h40 GTD/GTP-era sprint: 2-3 stints (so 2 stops) typical in the Michelin example; Road America single-stop fuel gamble possible with 90+ min stints — Sportscar365/Motorsport.com above.

### Inferences
- IMSA is not confirmed to use the exact 40 s rule (WEC doc only); IMSA energy flow is BoP-set per the Motorsport.com piece. Stop counts for 6 h/12 h/24 h: not found; only inferable from stint of about 50 min (GTP, single-source quote) -> roughly 7-8 stops at 6 h, 14-16 at 12 h, 28-30 at 24 h (inference, ignores cautions).

### Gaps
- Exact IMSA 2026 energy refill rule; stop counts per race length; fuel-tank size vs energy in GTP; LMP2/GT3 refuelling flow rates not found.

## 5. Reacting to FCYs; decision rules

### Takeaway
FCY procedure keeps pits closed during pack-up; pit lane opens later by class, so a "pit now" call is limited by when it opens and by position in the queue. Strategists weigh fuel window, caution length and track position.

### Cited Findings
- IMSA FCY sequence (Watkins Glen/Sebring 2025-26 briefings): pits closed, safety car to leader, pack up, pass-around, pits open by class (prototype first at Sebring 2026 briefing, then GT), final wave-by, class split, restart; short FCY variant keeps pits closed through the pass-around; Pit Exit Closed is a separate signal — [IMSA Sebring 2026 driver briefing](https://imsa.results.alkamelcloud.com/Results_NoticeBoard/26-2026/06_Sebring%20International%20Raceway/09_Briefing%20Photos/01_IWSC%20DRIVER%20BRIEFING.pdf), [Watkins Glen 2025 briefing](https://imsa.results.alkamelcloud.com/Results_NoticeBoard/25_2025/14_Watkins%20Glen%20International/09_Briefing%20Photos/01_IWSC%20DRIVER%20BRIEFING.pdf) (search summaries)
- Procedure change: with single prototype class, pits open for it after pack-up while GT cars still pass-around; no lap-down wave-by in races under 2h30 (age unclear, bulletin not found) — [Motorsport.com](https://www.motorsport.com/imsa/news/imsa-introduces-modifications-to-competition-procedures/448443/)
- 2019 Daytona: Ford GT penalised for entering a closed pit when the race went red — [Autosport](https://www.autosport.com/imsa/news/ford-daytona-loss-after-comeback-from-five-laps-down-a-kick-in-teeth-5283250/5283250/)
- Pit-now-under-yellow rationale: Mosport AO Racing example (Q2); short middle stint helps if a yellow comes; virtual tank does not deplete in pit lane, but pace laps under yellow burn energy less than fuel, so energy may not limit after long cautions (Motorsport.com virtual energy article) enabling stay-out gambles.

### Inferences
- Rules of thumb (inference, unsourced): stop under FCY if within the fuel window and the pit lane opens before the queue is packed; stay out if just pitted or if traffic/lap-down cars would cost position; cover a rival whose stop would undercut.

### Gaps
- No strategist quotes on staying out vs pitting at specific thresholds; pit-open timing rules by class in current regs; no sourced "cover a rival" rule.

## 6. Numeric rules of thumb found

- Pit lane 60 km/h (IMSA guide, WEC Genesis).
- 80 L in 40 s (Genesis GMR-001, single source) implies about 2 L/s (my division).
- Hypercar refill: full stint energy in 40 s (FIA 2025 decision, summary).
- Four-tyre change typical under 25 s (IMSA guide).
- Stint lengths: GTP about 50 min (strategist), GTD/GTLM about 60 min full tank, Le Mans 12-13 laps.
- Virtual energy violation: 100 s hold, +100 s repeated.
- Not found: fuel-save-per-lap vs stop-saved trade, tyre warm-up loss, seconds per litre for IMSA classes.
