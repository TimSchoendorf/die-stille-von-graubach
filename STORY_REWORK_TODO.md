# Story Rework TODO (Chapter 1)

## Already implemented in this pass
- Better motivation for Elise's 10-year absence (study + inflation + family burden).
- Candle line clarified: not "don't extinguish" but "cannot be extinguished permanently".
- Added in-world consequence when candle was extinguished attempt (bell reaction).
- Georg's bell reaction now has a concrete reason (night watch signal).
- Removed awkward line "Morgen, Morgen fange ich an zu verstehen".
- Conditionalized notebook-memory line so it only references Georg's quote if player asked him.
- Reworded "Schläfenden" to "Schlafenden unter der Erde".
- Improved transition into sleep/dream and made wake-state ambiguity stronger.
- Added dream-specific background + ambience.
- Added escalation before knocking (vibration -> scream -> abrupt silence -> knocks).
- Door scene now supports extra option: ask through closed door before deciding.
- Konrad now references Elise's scream as reason for checking in.

## Process improvement (implemented this run)
- **Bottleneck identified:** Rewrite passes were scattered across files without a fixed "impact pass" checklist, causing uneven quality and missed Act 2/3/4 beats.
- **Fix applied:** Adopted a per-ship-block loop: (a) one tension beat, (b) one character-truth beat, (c) one consequence-choice wording upgrade, then validation + commit.
- **Fix applied now:** added `scripts_locale/dialogue_impact_lint.py` to flag generic fallback phrases (e.g., "So oder so", "Ich weiß") in Act 2/3/4.
- **Next concrete automation step:** wire this lint into ship-block validation (`validate_dialogue.py && dialogue_impact_lint.py`) and track down the top 10 recurring weak patterns each pass.

## Process improvement (implemented in latest autonomous loop)
- **Bottleneck identified:** Act bridges often delivered consequences only as narration, with limited player agency right before major escalation scenes.
- **Fix applied:** Added a "bridge agency checkpoint" rule for ship-block loops: each transition scene (especially end-of-act bridges) should include at least one actionable choice that changes downstream emotional/pacing payoff.
- **Applied now:** inserted a new rehearsal micro-scene + choice in `act3/ally_fallout_bridge.json` and paid it off in `act3/descent.json` via new flags (`rehearsed_signal_night6`, `skipped_rehearsal_night6`).

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** The Seal ending resolved the cosmic plot but underpaid ally-fallout emotion flags (`*_hurt_day6`) set in Act 3, so setup→escalation→payoff coherence weakened in this branch.
- **Fix applied:** Added an "ending fallout closure checkpoint" rule: every ending that can follow `ally_fallout_payoff_pending=1` must include explicit reconciliation beats and clear the pending flag.
- **Applied now:** extended `act4/ending_seal.json` with a new post-ritual reconciliation event on the church steps, conditional lines for Georg/Hilde/Voss hurt states, and cleanup via `ally_fallout_payoff_pending=0`.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Branch-specific ending polish drifted: some endings explicitly resolved `ally_fallout_payoff_pending`, while others relied on implicit emotional closure. This weakens setup→escalation→payoff coherence across routes.
- **Fix applied:** Added an "ending parity checkpoint" for ship-block runs: every ending reachable after ally fallout must either clear `ally_fallout_payoff_pending` on-screen or justify why it intentionally remains open.
- **Applied now:** extended `act4/ending_pact.json` with a dedicated fallout-resolution beat + explicit flag cleanup (`ally_fallout_payoff_pending=0`) before ally epilog reactions.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Late-Act branch differentiation flattened during failure routes: the rehearsal decision in `act3/ally_fallout_bridge.json` had immediate descent payoff, but little/no visible consequence in the Act-4 escape climax.
- **Fix applied:** Added a "carry-forward contingency checkpoint" to the loop: any new tactical choice introduced in Act 3 must be checked for at least one explicit Act-4 consequence beat (success cadence or failure cost).
- **Applied now:** extended `act4/ending_escape.json` with rehearsal-dependent crisis beats (`rehearsed_signal_night6` vs `skipped_rehearsal_night6`) before ally-arrival branching.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Sacrifice route had strong core emotion but weak bridge-to-ending continuity: Act-3 rehearsal/fallout flags were underpaid compared with other endings, flattening branch differentiation.
- **Fix applied:** Added a "sacrifice continuity checkpoint" to the loop: before shipping, verify Sacrifice also resolves `ally_fallout_payoff_pending` on-screen and pays rehearsal choice (`rehearsed_signal_night6` vs `skipped_rehearsal_night6`) with concrete cadence/cost.
- **Applied now:** inserted a new fallout-reconciliation mini-scene in `act4/ending_sacrifice.json` (includes rehearsal payoff/cost lines, hurt-flag reconciliations, explicit cleanup `ally_fallout_payoff_pending=0`).

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Truth ending resolved cosmic stakes, but Act-3 rehearsal and hurt-state fallout had weaker on-screen payoff than other endings, reducing branch differentiation at the finale.
- **Fix applied:** Added a "truth-route closure checkpoint" to ship-block runs: if `ally_fallout_payoff_pending=1`, Truth ending must (a) pay rehearsal vs skipped-rehearsal cadence, (b) resolve hurt flags with explicit reconciliation beats, then (c) clear pending fallout on-screen.
- **Applied now:** expanded `act4/ending_truth.json` with a new church-steps reconciliation micro-scene (rehearsal/cost + hurt-flag payoffs) before the existing ally epilog branch.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Multi-ally investment flattened late pacing on Night 6: even when players built trust with several allies, the preparation scene often felt like a single-ally lane, so setup value from other relationships underpaid before Act 4.
- **Fix applied:** Added a "multi-ally carryover checkpoint" to the loop: if at least two allies are aligned, insert one concrete pre-ritual support event in Act 3 and require a mechanical/emotional payoff in Act 4 opening beats.
- **Applied now:** introduced a new Night-6 support-bundle micro-scene in `act3/preparation.json` (sets `extra_support_bundle`) and integrated direct tactical payoff text in `act4/ritual_night.json`.

## Open issues (next pass)
1. **Dedicated open-door background image needed**
   - Requested: opened door centered, exterior visible.
   - Current fallback still uses existing night house background.

2. **Knocking SFX quality**
   - Existing fallback uses `door_creak.wav` (better than glass, but still not ideal).
   - Need proper 3-knock SFX (single clean knock sample or precomposed triple knock).

### Asset batch for Tim (tomorrow generation)
- [ ] `assets/sprites/backgrounds/grandmother_door_open_night.png`
  - Composition: interior view, opened front door centered in frame, outside fog visible, moonlit contrast.
  - Mood: uncertain/surreal but realistic enough for VN dialogue scene.
  - Resolution target: 1920x1080.
- [ ] Optional variant: `grandmother_door_open_night_v2.png` (same framing, stronger contrast + colder tones)

3. **Umlaut consistency pass**
   - Some legacy lines still contain ae/oe/ue forms.
   - Run focused text cleanup across Act 1 + translation keys.

4. **Dialog naturalness pass for Konrad conversation**
   - Current conversation improved, but can still be made less exposition-heavy.

5. **Chapter continuity checks**
   - Validate that new bell/watch details align with later acts (especially church + night events).

## Optional expansion ideas
- Add short pre-knock internal monologue branch depending on `read_journal_night1`.
- Add alternate Konrad behavior if player repeatedly refuses to open.
- Add micro-choice: peek through keyhole (high paranoia route).
- Add notebook page snippets as collectible journal fragments.
