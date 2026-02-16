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
