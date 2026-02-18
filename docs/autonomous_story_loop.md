# Autonomous Story Improvement Loop (VN)

## Per-run checklist
1. Identify one bottleneck (content or process).
2. Run mandatory cross-act coherence pass (setup -> escalation -> payoff across neighboring acts).
3. Apply one high-impact narrative change.
4. Add/expand scene if density or pacing is thin.
5. Run `python3 scripts_locale/validate_dialogue.py`.
6. Commit with compact message (no push).

## This run's process improvement
- Added explicit **branch-prep -> ritual payoff handshake** flags (`*_prepared`) so approach decisions in Act 3 are guaranteed to echo in Act 4.
- This creates a reusable pattern for future edits: any new branch setup should set a prep flag and consume it with a short payoff check in the next act.
