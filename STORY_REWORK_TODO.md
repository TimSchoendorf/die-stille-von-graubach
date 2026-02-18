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

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Sought-Konrad route carried strong emotional setup, but lacked a player-owned tactical rehearsal beat before ritual night; payoff text in Act 4 therefore converged too early and weakened branch differentiation.
- **Fix applied:** Added a "trusted-ally tactical rehearsal checkpoint" to the loop: if an Act-2 diagnostic branch feeds Act-4 ritual handling, Act-3 sought path must include one explicit practice choice with a distinct Act-4 execution callback.
- **Applied now:** inserted a new Konrad grounding rehearsal choice in `act3/allies_choice.json` (voice rhythm vs hand-anchor) and paid both variants off in `act4/ritual_night.json` with distinct pre-appearance narration + crisis callout lines.

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

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Sought-Konrad path had less tactical prep texture than the avoided-Konrad path, so branch differentiation depended mostly on emotion and less on actionable ritual technique.
- **Fix applied:** Added a "branch parity checkpoint" for ship-block runs: if one branch gains a concrete pre-ritual tactic, the neighboring branch must get an equivalent (not identical) tactical beat with its own flag + downstream payoff.
- **Applied now:** introduced a new sought-Konrad mini-scene in `act3/allies_choice.json` (Anna's Drei-Anker identity tactic, flag `konrad_anchor_phrase_prepared`) and paid it off in both `act3/descent.json` and `act4/ritual_night.json`.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Konrad's Act-2 trust path still front-loaded key vessel symptoms in long monologue blocks, so player agency and memory retention weakened before Act-3 escalation.
- **Fix applied:** Added a "symptom probe checkpoint" to ship-block loops: when a branch introduces crucial possession data, force one player-led diagnostic choice and require a downstream callback in the next act.
- **Applied now:** inserted a new investigative micro-choice in `act2/konrad_encounter.json` (missing-time vs spiral-sign focus; flags `asked_konrad_missing_time` / `asked_konrad_spiral_signs`) and paid it off in `act3/allies_choice.json` during Konrad's relapse scene.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** The new Act-2 Konrad diagnostic probe (`asked_konrad_missing_time` vs `asked_konrad_spiral_signs`) had escalation payoff in Act 3, but ritual-night execution still converged too early, so the setup lost tactical identity in Act 4.
- **Fix applied:** Added a "probe-to-ritual continuity checkpoint" to the loop: any investigative branch introduced before Act 3 must get at least one distinct ritual handling beat (not just memory text) in Act 4.
- **Applied now:** extended `act4/ritual_night.json` with probe-dependent pre-appearance tactics and callout dialogue (bell-gap control vs spiral-hand cue), plus continuity flags (`ritual_timing_from_missing_time`, `ritual_spiral_tell_prepared`).

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Avoided-Konrad command choice in `act4/ritual_night.json` (`issued_schoolhouse_hold_order` vs tempo discipline) had immediate tension flavor, but little/no end-state memory payoff in the Escape ending, weakening setup→escalation→payoff continuity.
- **Fix applied:** Added an "end-state tactical memory checkpoint" rule: any late-ritual command/tactics flag must get at least one explicit epilog reflection in the corresponding ending branch.
- **Applied now:** extended `act4/ending_escape.json` with a new schoolhouse-order epilog gate (`check_schoolhouse_order_escape_memory`) and differentiated aftermath text for hold-order vs tempo-only choices.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Escape ending still lacked explicit Act-3 ally-fallout closure (`ally_fallout_payoff_pending`) while other major endings resolved it on-screen, weakening setup→escalation→payoff parity for this branch.
- **Fix applied:** Added an "escape fallout closure checkpoint" to the loop: if `ally_fallout_payoff_pending=1`, Escape must include hurt-flag reconciliation beats and clear the pending fallout flag before aftermath epilog.
- **Applied now:** extended `act4/ending_escape.json` with a new post-collapse reconciliation micro-sequence (`georg_hurt_day6` / `hilde_hurt_day6` / `voss_hurt_day6`) and explicit cleanup via `ally_fallout_payoff_pending=0`.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** The Awakening failure route had strong cosmic spectacle but weak tactical memory payoff from Night-6 rehearsal/contingency setup, so setup→escalation→payoff continuity lagged behind other endings.
- **Fix applied:** Added an "awakening tactical echo checkpoint" for ship-block loops: failure endings must still pay at least one rehearsal decision and one contingency memory beat before collapse fully takes over.
- **Applied now:** expanded `act4/ending_awakening.json` with a new fallback-signal micro-sequence (rehearsed vs skipped cadence) plus contingency callbacks (`contingency_counter_chant`, `contingency_iron_hook`, `contingency_chalk_route`, `contingency_bell_protocol`) before final failure escalation.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Konrad trust route still delivered key regulation tactics mostly as one-off exposition; without an early mnemonic hook, the setup from Act 2 could fade before Act-3/Act-4 possession spikes.
- **Fix applied:** Added a "mnemonic carryover checkpoint" to ship-block loops: when a branch introduces psychological self-regulation, add one compact player-owned cue in setup and require explicit callbacks in escalation and ritual payoff beats.
- **Applied now:** inserted a new Act-2 micro-choice in `act2/konrad_encounter.json` (Notfall-Stoppwort "Mittwoch", flag `prepared_konrad_interrupt_word`) and paid it off in `act3/allies_choice.json` + `act4/ritual_night.json` with distinct recall/callout narration.

## Process improvement (implemented in current autonomous loop)
- **Bottleneck identified:** Voss-alliance path in Act 3 delivered emotional confession but almost no player-owned tactical prep, so Act-4 priest support beats converged into generic prayer lines and undercut branch differentiation.
- **Fix applied:** Added a "confession-to-technique checkpoint" to ship-block loops: when an ally confesses high-stakes guilt in setup, require one actionable co-regulation choice in the same scene and a direct execution callback in ritual escalation.
- **Applied now:** inserted a new Voss prep micro-scene + choice in `act3/preparation.json` (`voss_breath_litany_prepared` vs `voss_truth_litany_prepared`) and paid both variants off in `act4/ritual_night.json` with distinct ritual callout lines.

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
