# Story Review – 2026-02-17

## Scope
- Re-check of Chapter/Act 1 rework TODOs
- Quick consistency pass for next chapters (Act 2/3)
- Dialogue validation run (`scripts_locale/validate_dialogue.py`)

## Act 1 rework status (from TODO)

### Confirmed done in dialogue flow
- Candle logic/consequence + bell reaction context present in Act 1 texts.
- Georg night-watch motivation present.
- Dream escalation before knocking present (vibration/scream/silence/knock progression).
- Door scene includes questioning through closed door before open/deny branch.
- Conditional journal/notebook references are present.
- Wording `Schlafenden unter der Erde` present.

### Still open / not delivered yet
1. **Dedicated open-door background image**
   - Missing: `assets/sprites/backgrounds/grandmother_door_open_night.png`
   - Current available backgrounds: `grandmother_house_night.png` (+ raw variants)

2. **Proper knocking SFX**
   - Currently available relevant SFX: `door_creak.wav`
   - No dedicated 3-knock sample found yet.

3. **Umlaut consistency pass**
   - Started and applied targeted fixes in:
     - `data/dialogue/prologue.json`
     - `data/dialogue/act3/descent.json`
   - More micro-pass can still be done later across all acts.

## Next-chapter consistency findings (Act 2/3)

### Structural/logic health
- Structural validation: **OK**
- Expression validation: **OK**
- Endings reachable: **all 6 reachable**

### Potential narrative cleanup candidates (non-blocking)
- Some flags are set but never checked later (currently 50). Not a crash issue, but indicates opportunities for stronger reactivity and payoff.
- Candidate follow-up: add selective reactivity lines for high-value flags in Act 3/4 (e.g., trust-related and investigation-order flavor).

## Recommended next implementation chunk
1. Add missing door-open night background + integrate into first-night open-door branch.
2. Add dedicated knock SFX (`sfx_knock_3x.wav`) and wire it to the same branch.
3. Add 3–5 payoff checks in Act 3/4 for currently dead high-impact flags.
4. Run one final focused umlaut/style pass after content edits.
