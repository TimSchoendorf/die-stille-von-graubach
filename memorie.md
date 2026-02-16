# Project Memory

## Purpose
Quick operational memory for this repository so coding agents can act without re-discovering the project setup.

## Stack
- Engine: Godot 4.5
- Language: GDScript
- Genre: Horror visual novel (1920s Germany)

## Core Systems
- Autoloads: `GameManager`, `SaveManager`, `AudioManager`, `SceneManager`
- Dialogue source: `data/dialogue/` (JSON)
- Dialogue loader: `dialogue_loader.gd`
- Branching state: flat flag map (`String -> int`) in `GameManager`

## Dialogue Node Types
`narration`, `dialogue`, `choice`, `background`, `character`, `transition`, `scene_end`, `flag_check`, `set_flag`, `effect`, `journal`, `wait`, `sound`

## Conventions
- Use `snake_case` in GDScript.
- Prefer signal-based decoupling between systems.
- Keep paths under `res://assets/`, `res://data/`, `res://scenes/`, `res://scripts/`.
- Target display: 1920x1080 with `canvas_items` stretch.

## Local Run Command
```powershell
"C:\Users\Timmy\Downloads\Godot_v4.5.1-stable_win64.exe(1)\Godot_v4.5.1-stable_win64_console.exe" --path "C:\Games\VisualNovel"
```