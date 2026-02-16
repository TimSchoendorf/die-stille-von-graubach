# Asset Drop Pipeline

## Goal
Automate import of manually generated images into the game while keeping old assets untouched.

## Fastest ChatGPT v2 Workflow
### 1) One-time setup + prompt pack
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_assets_easy.ps1 -Action all
```

This creates:
- `assets_pipeline/chatgpt/chatgpt_prompt_pack.md` (copy/paste prompts)
- `assets_pipeline/chatgpt/chatgpt_filenames.txt` (exact required filenames)
- `assets_pipeline/inbox/_DROP_FILES_HERE.txt` (drop folder reminder)

### 2) Generate in ChatGPT
- Open `assets_pipeline/chatgpt/chatgpt_prompt_pack.md`
- For each asset, generate an image in ChatGPT
- Save as PNG with exact filename shown (`bg..._v2.png` or `char..._v2.png`)
- Drop files into `assets_pipeline/inbox/`

### 3) Import into game + rewrite dialogue + verify
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_assets_easy.ps1 -Action import
```

### 4) Check what is still missing from inbox
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_assets_easy.ps1 -Action status
```

## What This Pipeline Does
- Reads `assets_pipeline/manifest.json` (required assets inferred from dialogue).
- Loads source images from `assets_pipeline/inbox/`.
- Normalizes images to game sizes:
  - Backgrounds: `1920x1080` (cover fit)
  - Character portraits: `600x900` (contain fit on transparent canvas)
- Writes normalized outputs to `assets_pipeline/processed/`.
- Optionally copies final files into game asset paths as `*_v2.png`.
- Optionally rewrites dialogue references from old assets to `*_v2`.
- Writes a report to `assets_pipeline/reports/`.

## Naming Rule For Inbox Files
Use exact manifest id as filename stem:
- `bg.village_square_v2.png`
- `char.elise.afraid_v2.png`

Supported inbox file extensions: `.png`, `.jpg`, `.jpeg`

## Commands
### 1) Build / refresh manifest
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action init-manifest
```

### 2) Validate what's missing (no imports)
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action run
```

### 3) Import processed files into assets + rewrite dialogue references
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action run -ImportToAssets -RewriteDialogue
```

### 4) Verify all manifest targets exist in game assets
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action verify
```

### 5) Rewrite dialogue references only (no image work)
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action rewrite
```

## Transparency Check
Portrait entries are expected to be transparent. The pipeline checks corner alpha and reports warnings.
Use strict mode to fail on non-transparent corners:
```powershell
powershell -ExecutionPolicy Bypass -File scripts_assets/vn_asset_pipeline.ps1 -Action run -ImportToAssets -StrictTransparency
```

## Recommended Loop
1. Generate a batch (5-10 images) and drop in `inbox/`.
2. Run `-Action run` and fix missing/warnings from report.
3. Once clean, run with `-ImportToAssets -RewriteDialogue`.
4. Test in Godot.
