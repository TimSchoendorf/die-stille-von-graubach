# Prompt Consistency Sheet (Manual Generation)

Use this same style anchor in every generation prompt:

"Painterly realism, oil-on-canvas texture, muted desaturated palette, cinematic chiaroscuro lighting, subtle fog, 1920s German horror visual novel, no anime, no cartoon, no neon, no text, no watermark."

## Background Prompt Template
[STYLE ANCHOR]
Environment-only scene, no people.
Location: <manifest background base id meaning>.
Mood: oppressive quiet, late autumn black forest.
Framing: wide visual novel background.

## Portrait Prompt Template
[STYLE ANCHOR]
Transparent background.
Upper-body visual novel sprite, centered.
Character identity fixed: <same identity description every time>.
Expression: <target expression>.
Keep same face structure, hair, age, and clothing as other expressions for this character.

## Output Mapping
Save each exported file to inbox with exact id from manifest.
Examples:
- `bg.church_interior_v2.png`
- `char.konrad.suspicious_v2.png`