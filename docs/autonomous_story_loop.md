# Autonomous Story Improvement Loop (VN)

## Per-run checklist
1. Identify one bottleneck (content or process).
2. Run mandatory cross-act coherence pass (setup -> escalation -> payoff across neighboring acts).
3. Apply one high-impact narrative change.
4. Add/expand scene if density or pacing is thin.
5. Run `python3 scripts_locale/validate_dialogue.py`.
6. Commit with compact message (no push).

## This run's process improvement
- **Bottleneck identified:** Approach choices (Siegel / Verstehen / Zerstören / Pakt) had strong strategic text but weak *pre-commitment embodiment* right before the finale; in play this can flatten branch identity at ritual start.
- **Process improvement applied:** Added a **"commitment token" pass** to the loop: after every major approach choice, require one concrete physical action (token) in Act 3 and one explicit recall payoff in Act 4.
- Implemented with four new Act-3 commitment micro-events (one per approach), four new flags, and mirrored Act-4 payoff checks before ritual escalation.
- Result: better setup->escalation continuity and stronger branch differentiation through tactile memory anchors.
