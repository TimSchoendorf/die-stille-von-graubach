# Die Stille von Graubach - Visual Novel

## Projekt
Horror-Visual-Novel in Godot 4.5 (GDScript), 1920er Deutschland.
JSON-basiertes Dialogsystem, Flag-System fuer Branching, 6 Enden.

## Architektur
- Autoloads: `GameManager`, `SaveManager`, `AudioManager`, `SceneManager`
- Dialogsystem: JSON-Dateien in `data/dialogue/`, geladen durch `dialogue_loader.gd`
- Node-Typen: `narration`, `dialogue`, `choice`, `background`, `character`, `transition`, `scene_end`, `flag_check`, `set_flag`, `effect`, `journal`, `wait`, `sound`
- Flags: Flaches Dictionary (`String -> int`) in `GameManager`, gesteuert durch Dialog-JSON

## Konventionen
- GDScript in `snake_case`
- Signale fuer lose Kopplung zwischen Systemen
- Pfade: `res://assets/`, `res://data/`, `res://scenes/`, `res://scripts/`
- Display: 1920x1080, `canvas_items` stretch

## Asset-Pipeline
- Charaktere: Animagine XL 3.1 (Oil Painting), 832x1216 -> rembg (`isnet-anime`) -> 600x900
- Hintergruende: juggernautXL, 1344x768 -> 1920x1080
- SD API: `http://127.0.0.1:7860`
- Generierungsskript: `scripts_sd/generate_all_characters_v2.py`
- Prompt-Regel: Pose-Lock + white BG + CFG 7, kein `dark atmosphere`

## Testen
```powershell
"C:\Users\Timmy\Downloads\Godot_v4.5.1-stable_win64.exe(1)\Godot_v4.5.1-stable_win64_console.exe" --path "C:\Games\VisualNovel"
```