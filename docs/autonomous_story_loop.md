# Autonomous Story Improvement Loop (VN)

## Per-run checklist
1. Identify one bottleneck (content or process).
2. Run mandatory cross-act coherence pass (setup -> escalation -> payoff across neighboring acts).
3. Apply one high-impact narrative change.
4. Add/expand scene if density or pacing is thin.
5. Run `python3 scripts_locale/validate_dialogue.py`.
6. Commit with compact message (no push).

## This run's process improvement
- **Bottleneck identified:** Escape ending branches were emotionally similar at the collapse beat, especially around ally fallout resolution.
- **Process improvement applied:** Added a "branch identity anchor" check in the loop: for each ending branch touched, enforce one unique physical evidence token and one explicit emotional callback to Day-6 fallout.
- Applied here by adding a Voss-only archive-rescue event (`voss_archive_ledgers_saved`) plus direct reconciliation lines in Georg/Hilde escape beats.
- This creates clearer branch differentiation while preserving setup->escalation->payoff continuity.
