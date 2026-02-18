# Autonomous Story Improvement Loop (VN)

## Per-run checklist
1. Identify one bottleneck (content or process).
2. Run mandatory cross-act coherence pass (setup -> escalation -> payoff across neighboring acts).
3. Apply one high-impact narrative change.
4. Add/expand scene if density or pacing is thin.
5. Run `python3 scripts_locale/validate_dialogue.py`.
6. Commit with compact message (no push).

## This run's process improvement
- Introduced a **micro-prep handshake rule for optional branch events**: if a new side event is added in Act 3, it must set exactly one reusable `*_prepared` flag and must be consumed by an early Ritual-Nacht payoff node.
- Applied in this run with `ritual_breath_count_prepared` (Anna schoolyard tactic in Act 3 -> opening pressure-control payoff in Act 4).
- This keeps branch additions compact, testable, and coherence-safe without bloating later scenes.
