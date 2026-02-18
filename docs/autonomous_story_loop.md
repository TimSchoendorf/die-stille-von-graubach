# Autonomous Story Improvement Loop (VN)

## Per-run checklist
1. Identify one bottleneck (content or process).
2. Run mandatory cross-act coherence pass (setup -> escalation -> payoff across neighboring acts).
3. Apply one high-impact narrative change.
4. Add/expand scene if density or pacing is thin.
5. Run `python3 scripts_locale/validate_dialogue.py`.
6. Commit with compact message (no push).

## This run's process improvement
- **Bottleneck identified:** Voss' grounding advice in Act 2 had low player agency (generic line, no committed anchor), so later pressure moments in Act 3/4 paid off emotionally but not *personally*.
- **Process improvement applied:** Added an **"anchor commitment" pass** to the loop: if a mentor gives coping protocol, force an immediate commitment choice (who/what the anchor is), then require explicit callback during escalation and finale.
- Implemented via a new Act-2 anchor choice event (Margarethe / Anna / Georg), new commitment flags, and mirrored payoff checks in both Act 3 (`descent`) and Act 4 (`ritual_night`).
- Result: stronger setup->escalation->payoff coherence and clearer branch identity under stress without bloating core route structure.
