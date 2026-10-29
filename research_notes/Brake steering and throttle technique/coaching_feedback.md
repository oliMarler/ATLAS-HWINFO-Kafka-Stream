# Coaching Feedback From Telemetry: How Coaches Turn Brake, Steering and Throttle Traces Into One Instruction (PRO and SIM)

Labels used throughout:
- **[PRO]** means real-world racing or track-day coaching, or pro data tools.
- **[SIM]** means sim-racing platforms and coaches.
- **[RESEARCH]** means motor-learning science.
- **(single-source)** means only one source was found for the claim.
- **(snippet-only)** means the wording comes from a search-result summary. The page itself was not fetched or could not be fetched (HTTP 403 or empty), so the exact wording is unverified.
- **(vendor claim)** means a product describing its own features.

Fully read primary sources:
- Ross Bentley, "Coaching With Data" (Speed Secrets Weekly #350, January 2020).
- Bentley's "Ask Ross" piece on the theoretical best lap.
- Two Your Data Driven (YDD) articles.
- Track Titan's telemetry guide.
- The VRS academy analysis article.
- The Coach Dave Delta help centre and product page.

Everything else is labelled with the flags above.

## 1. Method: reference laps, distance alignment, finding the time, choosing the single biggest gain, separating technique from car or traffic

### Takeaway
Coaches and tools use the same basic pipeline:
1. Overlay laps against distance.
2. Read the delta (or the segment and minimum-speed tables) to find *where* time goes. Usually that is two or three corners.
3. Read the speed and input traces to find *why*.
4. Check the finding against several laps, and against the driver's own feel, before saying anything.

The pro coaches studied (Bentley, YDD) warn against using another driver's lap as the main reference, because it teaches copying. Sim tools default to a pro or "official" reference lap. Neither school gave a rigorous data-only method for separating car balance from technique; the practical guard is to ask the driver.

### Cited Findings
**Reference laps and alignment**
- [PRO] Bentley built a whole two-point plan from **one lap** (the fastest), using mainly the speed trace. Lateral and longitudinal g only "reinforced what I noticed in the Speed trace". — [Bentley, Coaching With Data (PDF)](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] Bentley then warns that one lap "can be dangerous because I might be missing some valuable information". He recommends comparing the fastest lap "to three or four of your next fastest laps. What you may think is a trend may be a one-time issue." — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] On references, Bentley writes: "I also didn't compare to another driver's data. Sure, that's the easiest way of finding speed, but it usually means you're just copying, and that doesn't lead to long-term learning and gains." (single-source, but an explicit and deliberate position) — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] For consistency work, Bentley says to "take five or so of your best laps, and overlay them on your data" and focus on the places where speed differs most between laps. — [Bentley, Ask Ross: theoretical best](https://speedsecrets.com/q-how-close-should-my-lap-time-be-to-the-data-systems-theoretical-best/)
- [SIM] Track Titan overlays the driver's lap (orange) on a reference lap (blue). The default reference is the "Track Titan Official Lap", and the driver can change it. Throttle and brake are plotted against **distance**, so both laps are compared at the same point on track. — [Track Titan: How to analyse telemetry](https://www.tracktitan.io/post/how-to-analyse-telemetry-for-sim-racing)
- [SIM] VRS suggests comparing against a VRS coach's datapack lap when one exists. When none exists, it suggests comparing your own slow laps with your own fast laps. — [VRS Academy: Practising efficiently: Analysing](https://virtualracingschool.com/academy/tag/replay/)
- [SIM] VRS notes that iRacing's own live delta bar can reference either a sector-by-sector optimal lap or the best continuous lap. — [VRS Academy](https://virtualracingschool.com/academy/tag/replay/)
- [SIM] Coach Dave Delta accepts several reference types: pro laps from a pro-lap folder (iRacing, ACC, GT7 and LMU, current-schedule combinations only), community leaderboard laps, or your own replays. It reports an "Optimal Lap Time" built from your best sectors. — [Coach Dave Delta Help Centre](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/)

**Finding where the time goes**
- [PRO] One data-analysis article says to open the delta first because it shows *where* the time is. A lap three tenths slower overall often loses most of that in two or three corners. The speed, brake and throttle traces then show *why*. (snippet-only; single-source) — [ACI Motorsports: Race data analysis explained](https://www.acimotorsports.com/post/race-data-analysis-explained-from-telemetry-to-lap-time-gains)
- [SIM] In a VRS case study, the time-delta graph showed that most time was lost through the apex and exit of the following corner, not in the braking zone. — [VRS Academy](https://virtualracingschool.com/academy/tag/replay/)
- [SIM] VRS says its Driving Analyzer "automatically highlights the part of the track in which you have the biggest opportunity" to improve. (snippet-only; vendor claim) — [VRS Academy: telemetry](https://virtualracingschool.com/academy/tag/telemetry/)
- [SIM] Delta splits a lap into "sequences" (one corner or a group of corners). Its AI reports where you're losing time, grouped into **Braking, Entry, Apex and Exit** phases, shown as coloured dots on the track map. (vendor claim) — [Coach Dave Delta Help Centre](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/)
- [SIM] Track Titan's "Timekiller" ranks which mistake costs the most time, and now covers corner *combinations*. In its Oulton Park example, the real fault began two corners earlier: the driver "didn't straighten up the car correctly for braking". (snippet-only; vendor claim) — [Track Titan December 2025 update](https://www.tracktitan.io/post/december-2025-track-titan-update-faster-coaching-flows-social-leaderboards-bigger-team)
- [PRO] YDD's structured prompt for AI analysis asked for the **"top three opportunities"** with corner names. YDD also relied on gSum (combined-g) peak heights ("the peaks should be the same height") and a variance channel showing time gained or lost between laps. — [YDD: How well can AI analyse your motorsport data?](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)

**Reading the trace shape (Bentley's checklist on the speed trace)** [PRO]
Source for all items below: [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- Check the acceleration and deceleration rate, signs of coasting before braking, whether the car is at full throttle between turns, throttle lifts "where they shouldn't be", and whether there is enough trail braking in slow- and mid-speed corners.
- Then ask "Why?" again, and use the other channels (g, throttle, brake pressure, steering) "to confirm one way or the other".
- In the speed trace, trail braking shows as a "hockey stick" at the bottom of a corner. A "square" bottom (speed falls, then abruptly flattens) means little or no trail braking.

**Separating technique from car, feel and context**
- [PRO] Before sharing an analysis with the driver, YDD wanted the driver's own view first ("good to get their input before sharing this analysis"). It recommends combining data with video and driver feedback. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)
- [PRO] YDD lists the failure modes of automated analysis:
  - noisy channels;
  - confident claims not checked against the trace;
  - an invented reference lap time carried into the conclusion;
  - unsupported speculation (that slow late laps "might indicate physical or mental fatigue");
  - gains that cannot be summed, because "gains in one corner can affect the approach and exit of subsequent corners".
  The article itself does **not** show how to rule out car balance from data alone; car-side causes appear only as questions for the driver. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)
- [PRO] "Good analysis separates driver technique from car setup before anything is changed." (snippet-only; no method given) — [ACI Motorsports](https://www.acimotorsports.com/post/race-data-analysis-explained-from-telemetry-to-lap-time-gains)
- [PRO] Bentley's remote coaching, from the article summary (snippet-only; the article returned 403):
  - With brake, throttle and steering-angle data, it might take him "10 seconds to find something compared to 10 minutes with video or the basic data".
  - Data cannot capture how the driver felt, which he treats as "as important or even more important than what the data is telling me".
  — [Grassroots Motorsports: IMSA coach Ross Bentley on remote coaching](https://grassrootsmotorsports.com/articles/imsa-coach-ross-bentley-remote-coaching/)
- [PRO] Bentley's standing question to drivers: "if you could have the car do one thing better, what would it be?" (snippet-only) — [YDD Ep3: Tips for racing faster with Ross Bentley](https://www.yourdatadriven.com/ep3-tips-for-racing-faster-with-ross-bentley/)

### Inferences
- In-race traffic laps, out-laps and in-laps contaminate both the reference and the comparison. None of the fetched sources gives a traffic-filter rule. A coaching assistant should exclude laps (or corners) that were flagged as traffic-affected before naming a "loss". (inferred)
- A practical car-versus-driver discriminator implied by the sources (inferred, not stated by any source):
  - A loss that is **consistent across laps with similar inputs** points to car balance or a fixed technique habit. The next step is to ask the driver how the car felt there.
  - A loss that **varies lap to lap** points to an execution or consistency problem.
- "Own best lap" as a reference matches Bentley's anti-copying stance and the VRS fallback. A sector-optimal lap (iRacing delta option, Delta "Optimal Lap") gives a reachable target made of the driver's own pieces. (inferred synthesis)

### Gaps
- No primary pro-team (F1, WEC or IMSA data engineer) source was found describing the step-by-step selection of the single biggest gain.
- Jorge Segers' *Analysis Techniques for Racecar Data Acquisition* (SAE, 2nd ed. 2014) was not accessible. Its method content is not represented here.
- The search summaries mention a Bentley "vMin table" (minimum speed per corner, "for identifying which corners you need to work on"), but the source page was not identified or retrieved.
- No source gave a data-only test for "car balance vs technique" (for example, steering-versus-yaw understeer checks used for coaching rather than setup).

## 2. Prioritisation: order of work, one point at a time, points per session, confirming a change

### Takeaway
There is **no single agreed order** across sources:
- VRS: exit first, then entry, then mid-corner.
- Bentley's worked example: full-throttle time and brake release.
- Krause: braking is "the greatest variable".

The sources do agree on three things:
- Work on very few items: Bentley used **two**, would ideally have split them across two sessions, and asked for small changes.
- Consistency (gap to theoretical best) is the precondition for judging whether a change worked.
- Confirm a change across several laps, not one.

### Cited Findings
**Few points, small changes**
- [PRO] Bentley: "From the data, I wanted the driver to focus on just two things." Ideally, "I would have split this up over two sessions", but the driver had only one session left, so "I took a chance that he'd be able to handle it all in one session." — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] Bentley's instruction "Spend 3% more of the lap at full throttle" came with the note "(Note, I wasn't asking for a big change)". — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] Reported result: a "little more than 3 seconds" improvement at Watkins Glen in one session, from a driver who had plateaued for years. The gains showed as:
  - higher minimum speed in Turn 1, the Bus Stop and Turn 11 ("7 MPH more" in T11);
  - better brake release in T6–T9;
  - one regression ("exit speed not as good" at T11), which became the next item to work on.

  This is a single anecdote on one track day, so treat the magnitude as illustrative. (single-source) — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] Across coaches quoted by YDD:
  - Scott Mansell: coaches "isolate basic techniques and repeat them many times", adding complexity in layers.
  - Bentley: the more a process is divided into "little chunks", the more likely the driver is to carry it out.
  - Perry McCarthy's instructor focused on "the big things *not* to do" rather than a long list of techniques.

  — [YDD: Learning to drive fast — skill development approaches](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)

**Order of work: sources conflict**
- [SIM] VRS: "the priority for speed should be on the exit of the corner, then the entry, and finally mid-corner." Mid-corner ranks lowest because the least time is spent there, and you may need to "sacrifice mid-corner speed for a faster entry and exit." — [VRS Academy](https://virtualracingschool.com/academy/tag/replay/)
- [PRO] Peter Krause: braking is "the greatest variable because people brake to what they think the car is capable of, not to what the car is capable of." (snippet-only) — [YDD: Mastering corner entry and braking](https://www.yourdatadriven.com/how-to-improve-braking-and-corner-entry/)
- [PRO] YDD's Motorsports Playbook lists where on track to prioritise, "not necessarily the corner onto the longest straight". The actual ranking was not visible. (snippet-only) — [YDD Motorsports Playbook](https://www.yourdatadriven.com/the-motorsports-playbook/)
- [PRO] Krause also advises leading the throttle out of corners and, for a wider exit, adding power "instead of opening the wheel". (snippet-only) — [Classic Motorsports: 10 steps to faster laps (Krause)](https://classicmotorsports.com/articles/basic-training-10-steps-faster-laps/); [Speed Secrets Podcast 161 (Krause)](https://speedsecrets.com/161-peter-krause-how-to-drive-fast-consistently/)
- [PRO] Mansell (via YDD) starts with **vision**, because he has rarely met a driver whose vision he couldn't improve. — [YDD skill development](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)

**Consistency as a gate, and confirming change**
- [PRO] Bentley on the gap to theoretical best:
  - "A half second off your theoretical is a good goal, but it depends on a few different factors" (session length, traffic).
  - "Being a second or more from your theoretical is starting to point at too many inconsistencies."
  - Being consistent makes it easier to judge whether a technique or setup change helps.
  - Warning: "one way to be more consistent is to drive slower… but that's not the point, right?!"

  — [Bentley, Ask Ross](https://speedsecrets.com/q-how-close-should-my-lap-time-be-to-the-data-systems-theoretical-best/)
- [PRO] John Kirkpatrick's benchmark (via YDD) is "the same thing, at the same place and to the same degree, each and every lap." — [YDD skill development](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)
- [PRO] Bentley judged the change by overlaying the original lap against the **best lap of the next session**, and he separately advises checking any trend against three or four other fast laps. — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO, karting vendor] A karting data vendor says a gap of more than a tenth to the theoretical best is a precision problem, not a speed problem. It suggests counting how many laps fall within a tenth of your best, excluding out-laps, in-laps and traffic laps. (snippet-only; single vendor; its threshold is much tighter than Bentley's) — [Purpl: lap consistency](https://purpl.app/blog/lap-consistency-karting/)
- [SIM] VRS recommends alternating "driving-analysis-driving-analysis", building awareness so the driver relies less on telemetry over time. — [VRS Academy](https://virtualracingschool.com/academy/tag/replay/)

### Inferences
- For a radio coach, "one point at a time" translates naturally to:
  - hold one active focus item per corner, or per stint phase, until it is confirmed or abandoned;
  - confirm across roughly 3–5 clean laps, matching Bentley's "three or four" and "five or so" laps;
  - not count a single good lap as success. (inferred)
- When the gap between actual and optimal lap is large (about 1 s or more, per Bentley), consistency should come before chasing a specific technique change. Otherwise any single-lap comparison is mostly noise. (inferred from Bentley)
- The VRS exit-first rule and a "biggest delta" rule can disagree. A reasonable tie-break is to weight corners leading onto long full-throttle sections (VRS's rationale), but YDD explicitly cautions this is "not necessarily" the right corner. (inferred; sources conflict)

### Gaps
- No source gave a quantified limit on points per *session* beyond Bentley's "two, ideally one per session".
- No source gave a statistical rule (for example, the number of laps or the size of a change) for declaring an instruction "worked".

## 3. Delivery: actionable wording, timing, framing, overload, adapting to the driver; radio versus debrief

### Takeaway
Two delivery philosophies coexist.
- **Prescriptive and specific**, in sim tools and in radio-style instructions: corner, phase and percentage.
- **Awareness and ownership**, from pro coaches: Bentley and Scott Gardner deliberately avoid telling the driver exactly what to do. They name the corner and the input to pay attention to, set a small numeric target, and let the driver find the change.

Pro radio practice is lean, comes from one voice, and happens on straights. The debrief is where questioning and explanation happen.

### Cited Findings
**Wording**
- [PRO] Bentley's two actual instructions were:
  - "Spend 3% more of the lap at full throttle." (a number, no location)
  - "Experiment with the timing & rate of release of the brakes – focus on Turns 6, 7, 8, 9." (a location, an input and an experiment, but no prescribed value)

  He adds: "I didn't actually tell him what exactly to do… I had simply made him aware of a few things, then asked him to be more aware of two things while driving." — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [PRO] Scott Gardner (via YDD) moves from directives to questions, asking "What are you going to do now?" rather than saying "Do this". He holds back the answer because "unless I've actually asked you" the driver won't learn, then offers his view as a suggestion ("How does that sound to you?"). — [YDD skill development](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)
- [PRO] A profile of Bentley's in-person sessions says they start with a lot of talking, the conversation thins as the session goes on, and he uses short cue words. (snippet-only; the exact source page was not pinned between these two results) — [RRDC: Ross Bentley](https://rrdc.org/?p=6674); [Motorsport Prospects: In conversation with Ross Bentley](https://www.motorsportprospects.com/whatever-it-takes-in-conversation-with-driver-coach-ross-bentley-part-1/)
- [SIM] Delta's tips are phase-structured (Braking, Entry, Apex, Exit) per sequence, and its throttle chart shows "too early or too late" with percentages when comparing two laps. (vendor claim) — [Coach Dave Delta Help Centre](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/); [Coach Dave Delta product page](https://coachdaveacademy.com/announcements/delta-data-telemetry-tool/)
- [SIM] Track Titan's prescriptive tips cover "braking markers, throttle modulation, corner entry/exit, and consistency". (snippet-only; third-party summary of vendor) — [Track Titan Review, Moore Podiums](https://moorepodiums.com/track-titan-review-iracing-ai-coaching/)

**Framing**
- [PRO] YDD's guidance includes "It's also important to celebrate the positives". It also says to give lap-time gains as rough ranges, not precise promises. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)
- [PRO] Bentley: when reviewing data, "it's easy to get defensive… Instead, pretend you're a detective, and look for your faults." — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [RESEARCH] A 2021 meta-analysis (Chua, Jimenez-Diaz, Lewthwaite, Kim and Wulf, *Psychological Bulletin*) found an **external** focus of attention (on the movement's effect, for example the car or a track point) superior to an **internal** focus (on body movements, for example the foot), for both performance and learning, across ages and skill levels. — [Chua et al. 2021, UNLV repository](https://digitalscholarship.unlv.edu/kns_fac_articles/424)
- [RESEARCH] One simulated-driving study found both an external and an internal focus improved performance under competitive pressure. The external-focus advantage was therefore less clear-cut in that driving context. (search-summary attribution; the page was not fetched; treat with caution) — [PMC3488937](https://pmc.ncbi.nlm.nih.gov/articles/PMC3488937)

**Timing and channel: radio versus debrief** [PRO]
- Red Bull's radio guide: "Radio comms between the team and the driver is kept as simple as possible, he generally has a lot to do in the car and focus is important." (snippet-only; the page fetch returned empty) — [Red Bull Racing: Bulls' Guide To Team Radio](https://www.redbullracing.com/int-en/bulls-guide-to-team-radio)
- Drivers prefer being spoken to on straights, because being spoken to at braking points can distract them. (snippet-only; secondary journalism) — [The SportsRush: How does F1 team radio work](https://thesportsrush.com/f1-news-how-does-f1-team-radio-work/)
- The race engineer is usually the single voice; other team members route their input through that person. (snippet-only; secondary) — [F1 Briefing: Who talks to F1 drivers](https://f1briefing.com/who-talks-to-f1-drivers-during-races/)
- Engineers decide in seconds what the driver needs now and what can wait, and some teams impose radio silence except for emergencies at high-pressure moments. (snippet-only; secondary) — [F1 Briefing: How F1 teams use radio](https://f1briefing.com/how-f1-teams-use-radio-for-strategy/)
- Mansell (via YDD): traffic and extra cars consume mental capacity. A driver consciously thinking about vision, steering or trail braking has no spare capacity for race decisions, so they revert to habit. — [YDD skill development](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)

**Where sim tools deliver**
- [SIM] Delta shows timing, tyre temperatures and basic lap information during a session. Full analysis and AI insights come **after returning to the pits or garage**, and it states it has no in-game overlays yet. (vendor) — [Coach Dave Delta Help Centre](https://coachdaveacademy.com/documentation/coach-dave-delta-help-centre-the-complete-faq-guide/)
- [SIM] Track Titan's live delta shows which corner or phase is costing time "immediately as you exit the corner". (snippet-only; vendor) — [Track Titan October 2025 update](https://www.tracktitan.io/post/october-2025-track-titan-update-new-live-overlays-for-all-sims)
- [SIM] Commercial voice "AI race engineer" products advertise cooldowns to avoid repeated calls and speaking "only when it matters, so you can keep focus". (snippet-only; vendor claims; the attribution between these two product pages was not pinned) — [AI Race Engineer](https://airaceengineer.com/); [PitWise](https://pitwise.net/)

### Inferences
These are synthesis for the assistant, not sourced practice:
- **Radio call shape:** corner + input + small target, delivered on a straight, and only one per lap or per few laps. Examples: "Turn 9, release the brake a touch earlier" or "Turn 9, brake marker one board later". This keeps the specificity sim tools use and the "small change" scale Bentley used.
- **Precise number or awareness cue:** use a precise number only where the data supports one (for example, a brake-point distance difference repeated over several laps). Otherwise use Bentley-style awareness cues ("focus on brake release in 6 to 9").
- **External wording:** phrasing a cue as an external target ("brake at the 100 board", "car to the exit kerb") rather than a body action ("ease your foot") follows the motor-learning evidence.
- **Debrief content:** the debrief, not the radio, is where to put the questions (Gardner and Bentley: "what would you want the car to do better?"), the explanation of *why*, positives, and the multi-corner picture.
- **When not to coach:** suppress technique calls in heavy traffic or during racing moments, in line with Mansell's capacity argument and F1 radio-silence practice.

### Gaps
- No primary source with verbatim pro *driver-coaching* radio calls (for example, a GT or IMSA coach on the radio) was found. The radio findings come from F1 strategy and engineering communication via secondary journalism.
- No source tested the "location + action + number" format against vague instructions. Its superiority is plausible but **unverified**.
- The YDD "AI analysis" post does not name its author.

## 4. Specific metrics per input, and how commercial sim tools present them

### Takeaway
The sources consistently report:
- **brake:** brake point, how quickly peak pressure is reached, and release shape (trail);
- **throttle:** application point, time to full throttle, lifts, coasting, and percentage of lap at full throttle;
- **speed:** minimum and exit speed.

Steering metrics are thinly covered.
- Sim tools mostly show overlaid traces against distance plus a delta.
- Delta and Track Titan add phase-tagged AI tips.
- Garage 61 is raw traces without AI.
- MoTeC i2 lets users build their own channels (for example, brake aggression as the derivative of brake pressure).

### Cited Findings
**Brake**
- [SIM] Track Titan's worked example compares the **braking point** and **how quickly full pressure is reached**. — [Track Titan: How to analyse telemetry](https://www.tracktitan.io/post/how-to-analyse-telemetry-for-sim-racing)
- [SIM] VRS's cockpit and chase views let you check car position at the **brake point, turn-in point and throttle point** against datapack or teammate laps. (snippet-only) — [VRS Academy: telemetry](https://virtualracingschool.com/academy/tag/telemetry/)
- [PRO tool] A MoTeC forum answer gives an i2 math channel for **brake aggression**: the derivative of front brake pressure, kept only above a threshold (100 in psi units). It also gives a **release-smoothness** channel built on `smooth('Brake Pressure Front' [psi],0.2)`. (snippet-only; thresholds need checking against your own data) — [MoTeC forum: Braking speed expression](https://forum.motec.com.au/viewtopic.php?p=22510)
- [PRO] Bentley reads trail braking from the *speed* trace shape: a "hockey stick" means trail braking, a "square" bottom means none. — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [SIM] Delta's Brake Chart shows "if you're braking too late for a corner" and whether you're trail braking correctly. — [Coach Dave Delta product page](https://coachdaveacademy.com/announcements/delta-data-telemetry-tool/)
- [SIM] Apex Sim Racing: brake traces show whether you are slowing the car more than necessary or releasing too early. (snippet-only) — [Apex Sim Racing: Understanding telemetry in iRacing](https://www.apexsimracing.com/en-es/blogs/sim-racing-blog/understanding-telemetry-iracing)

**Throttle**
- [PRO] Bentley's metric is **percentage of the lap at full throttle**: "Spend 3% more of the lap at full throttle". He also checks for coasting before braking, and throttle lifts on straights or in the Esses. — [Bentley, Coaching With Data](https://speedsecrets.com/wp-content/uploads/2021/03/COACHING-WITH-DATA.pdf)
- [SIM] Track Titan's example compares **how quickly each driver reaches full throttle on exit**. It links an early minimum speed to delayed throttle application and lower exit speed. — [Track Titan: How to analyse telemetry](https://www.tracktitan.io/post/how-to-analyse-telemetry-for-sim-racing)
- [SIM] Delta's Throttle Chart shows whether you're getting on the throttle too early or coming off it too late, "with percentages when comparing two laps". — [Coach Dave Delta product page](https://coachdaveacademy.com/announcements/delta-data-telemetry-tool/)
- [SIM] Apex Sim Racing: a delayed or cautious throttle shows as a flat section before acceleration begins. (snippet-only) — [Apex Sim Racing](https://www.apexsimracing.com/en-es/blogs/sim-racing-blog/understanding-telemetry-iracing)

**Steering**
- [SIM] Track Titan's worked example found "no major difference in the steering", so steering was not analysed in depth. — [Track Titan: How to analyse telemetry](https://www.tracktitan.io/post/how-to-analyse-telemetry-for-sim-racing)
- [PRO] In YDD's review of AI output, the AI flagged a driver "not maintaining a steady steering input". YDD shows this as an AI claim, not a verified finding. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)
- [PRO] Krause: for a wider exit, add power "instead of opening the wheel". (snippet-only) — [Classic Motorsports: Krause](https://classicmotorsports.com/articles/basic-training-10-steps-faster-laps/)
- [SIM] Track Titan's human 1:1 coaching covers "braking, throttle, steering, rotation, and racing line" in 60-minute live video sessions. (snippet-only; vendor) — [Track Titan 1:1 coaching](https://www.tracktitan.io/1-1-coaching)

**Speed, delta and combined channels**
- [SIM] Delta's Speed Reference Chart shows where top, minimum and corner speeds differ from the reference. Its Delta chart shows "time gained or lost at every point in the lap". — [Coach Dave Delta product page](https://coachdaveacademy.com/announcements/delta-data-telemetry-tool/)
- [PRO] YDD uses gSum peak heights and a variance channel. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)

**How the tools differ**
- [SIM] Garage 61 is iRacing-only and shows raw traces with no AI coaching. (vendor-biased: the comparison was written by competitor Coach Dave) — [Coach Dave: Delta vs Garage 61](https://coachdaveacademy.com/tutorials/coach-dave-delta-vs-garage-61-which-is-best-for-you/)
- [SIM] A third-party Firefox extension, RB Telemetry Coach, adds automated comparison inside Garage 61 for braking, throttle, steering, speed, gear, RPM and line. It is not affiliated with Garage 61. — [RB Telemetry Coach (Firefox add-on)](https://addons.mozilla.org/firefox/addon/rb-telemetry-coach/)
- [SIM] Track Titan: the free tier has unlimited telemetry and no AI, and AI tips need the $7.99/month Plus tier. An older review instead says the free tier includes AI tips capped at 50 laps a month. (sources conflict) — [Sim Racing Manual: AI driving coaches](https://simracingmanual.com/resources/ai-driving-coaches/)

### Inferences
Candidate per-corner metric set for an iRacing assistant (synthesis of the above; no source gives this exact list):

| Input | Metrics |
|---|---|
| Brake | brake-on distance; peak pressure; time or distance to peak; release length and rate (trail) |
| Throttle | first-application distance; distance to 100%; lifts after application; coast time between brake-off and throttle-on |
| Speed | minimum speed and where it occurs; exit speed at a fixed distance after the corner |
| Steering | number of correction reversals; peak angle relative to the reference |

### Gaps
- No official Garage 61 documentation was retrieved, so its exact channel set and delta presentation are unverified.
- No current VRS documentation on Driving Analyzer outputs was retrieved; the 2016-era descriptions may be outdated.
- No source defined steering-correction counts or peak-lock metrics as coaching KPIs.
- No standard MoTeC i2 iRacing workspace definitions were found for coasting time or full-throttle percentage. Users build these as math channels.

## 5. Endurance coaching: across a stint, across drivers sharing a car, consistency targets, risk, multi-class traffic

### Takeaway
Endurance guidance is sparse and mostly secondary. The common points are:
- Optimise repeatable stint pace, not peak laps.
- Practise full stints with traffic and judge total elapsed time.
- Identify corners where passing or being passed is not worth the risk.
- Lose as little time as possible when being lapped, since side-by-side racing usually costs more than yielding.

No source covered coaching method across co-drivers sharing a car.

### Cited Findings
- [SIM] Practise a full predicted stint with traffic and judge total elapsed time rather than one peak lap. Use AI-traffic practice in multi-class to identify corners where passing isn't worth the risk, and run a few laps in the other classes to learn their braking points. (snippet-only; the page returned 403) — [OverTake: Practising for endurance races](https://www.overtake.gg/news/no-hotlaps-practicing-for-endurance-races-and-the-right-approach.581/)
- [SIM/general] A race is decided by repeatable lap times. A driver who loses a couple of seconds on every pass, or every time they are passed, won't win even with a track-record lap. When being passed, the goal is to lose as little time as possible, and side-by-side through a corner usually costs more than yielding. (snippet-only) — [LVRY: Multi-class racecraft](https://lvry.co/multi-class-racecraft/)
- [PRO] Teams want a competitive lap time that still leaves a margin for error, unlike time-attack driving. (snippet-only) — [Petrel Data: What is endurance racing](https://www.petreldata.com/racing-disciplines/what-is-endurance-racing/)
- [PRO] Endurance engineers focus on tyre and fuel degradation over long stints; consistency and long-term thinking outweigh single-lap optimisation. (snippet-only) — [Track Team Driver: Race engineer by series](https://trackteamdriver.com/race-engineer-by-series/)
- [SIM pro team] Team GP Elite says its coaches work on braking points, lines and racecraft, with engineers and coaches reviewing data together between sessions. (snippet-only) — [GP Elite: Endurance racing](https://gp-elite.com/raceteam/endurance-racing)
- [PRO] Bentley's half-second gap to theoretical best is modulated by session length and traffic, so expect a larger gap in traffic-heavy running. — [Bentley, Ask Ross](https://speedsecrets.com/q-how-close-should-my-lap-time-be-to-the-data-systems-theoretical-best/)
- [PRO] Gardner (via YDD) says practice should include pressure, such as a car close behind. — [YDD skill development](https://www.yourdatadriven.com/learning-to-drive-fast-on-track-the-best-skill-development-approaches/)
- [PRO] YDD judged driver level on a novice-to-pro scale using consistency targets expressed as a percentage of best lap. The specific percentages were not extracted. — [YDD AI analysis](https://www.yourdatadriven.com/ai-accurately-analyse-your-motorsport-data/)

### Inferences
These are synthesis, not sourced practice:
- **Reference across a stint:** in an endurance stint, the useful reference is the driver's best *clean* lap on similar fuel and tyre state, not the session best on fresh tyres. Otherwise tyre degradation reads as a technique loss.
- **Which corners to coach:** technique calls should target corners where the loss repeats across clean laps. Corners where the variance is driven by traffic should be left alone.
- **Consistency window:** a radio-friendly consistency target could be "laps within X of your stint median". Bentley's ±0.5 s to theoretical best (relaxed for traffic) is the only pro anchor found.
- **Risk:** improvement calls should favour low-risk changes (brake release, throttle timing and percentage) over braking-point moves in multi-class phases. This combines the risk advice above with Bentley's "small change" scale.

### Gaps
- No source on coaching **across drivers sharing a car** (for example, using the faster co-driver's lap as a reference, or setup compromises between drivers).
- No published lap-time-window numbers from pro endurance teams were found.
- No source with verbatim engineer-to-driver traffic-management calls from WEC, IMSA or iRacing special events was found.
- Several endurance sources could only be read as search snippets (403 errors).
