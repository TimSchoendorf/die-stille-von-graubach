param(
    [ValidateSet('setup','prompts','status','import','all')]
    [string]$Action = 'all',
    [string]$ManifestPath = 'assets_pipeline/manifest.json',
    [string]$InboxDir = 'assets_pipeline/inbox',
    [string]$ChatGptDir = 'assets_pipeline/chatgpt',
    [switch]$IncludeAlreadyExisting,
    [string]$PlaceholderPngDir = 'assets_pipeline/chatgpt/name_placeholders_png'
)

$ErrorActionPreference = 'Stop'

$Root = (Get-Location).Path
$PipelineScript = Join-Path $Root 'scripts_assets/vn_asset_pipeline.ps1'
$ManifestAbs = Join-Path $Root $ManifestPath
$InboxAbs = Join-Path $Root $InboxDir
$ChatGptAbs = Join-Path $Root $ChatGptDir
$PlaceholderPngAbs = Join-Path $Root $PlaceholderPngDir

$StyleAnchor = 'Painterly realism, oil-on-canvas texture, muted desaturated palette, cinematic chiaroscuro lighting, subtle fog, 1920s German horror visual novel, no anime, no cartoon, no neon, no text, no watermark.'

$BackgroundBriefs = @{
    berlin_apartment = 'small 1920s Berlin apartment, books, desk, rain on window, cramped scholarly space'
    blacksmith_shop = '1920s blacksmith interior, forge embers, iron tools, worn wood and metal'
    church_basement = 'hidden stone chamber under church, carved symbols, damp walls, torchlight'
    church_corrupted = 'same village church but reality-distorted, warped pews, impossible shadows'
    church_exterior = 'old black forest village church exterior, fog, cemetery, overcast sky'
    church_interior = 'old church interior, pews, altar, dim stained glass light'
    forest_corrupted = 'black forest with surreal geometry and subtle cosmic corruption'
    forest_path = 'dense black forest path, pine trees, fog, late autumn'
    grandmother_house = 'interior of old german cottage, candlelit bedroom, herbal details'
    grandmother_house_night = 'same cottage interior at night, moonlit, unnerving shadows'
    hilde_cottage = 'herbalist cottage interior, jars, dried herbs, rustic textures'
    ritual_chamber = 'ancient underground ritual chamber, carved circle and altar, oppressive atmosphere'
    train_interior = '1920s European train compartment, wood and leather, journey mood'
    village_corrupted = 'same village square area but subtly corrupted by cosmic horror'
    village_entrance = 'entrance to black forest village, timber houses, heavy fog, silence'
    village_night = 'village streets at night, moonlight, deep fog, deserted'
    village_school = '1920s village classroom, wooden desks, chalkboard, empty room'
    village_square = 'village square with fountain, timber houses, church in distance'
}

$CharacterIdentity = @{
    anna = 'Anna, female, 19, pale blonde hair, very pale skin, light blue eyes, ethereal and fragile look, simple white dress'
    elise = 'Elise, female, 24, dark-brown bob hair, round glasses, brown eyes, slim build, serious intellectual demeanor, 1920s coat and blouse'
    georg = 'Georg, male, 45, broad blacksmith build, dark hair with gray, weathered skin, moustache, work clothes with leather apron'
    hilde = 'Hilde, female, 68, white braided hair, weathered wise face, green eyes, herbalist clothing in earth tones'
    konrad = 'Konrad, male, 30, handsome, wavy dark hair, warm brown eyes, teacher attire from the 1920s'
    margarethe = 'Margarethe, female, 78, white hair tied back, stern but kind face, old black forest villager attire'
    otto = 'Otto, male, 60, heavyset, slicked-back gray hair, thick moustache, formal mayor suit, imposing presence'
    voss = 'Voss, male, 55, gaunt pastor, thin gray hair, hollow cheeks, dark tired eyes, black clerical robes with white collar'
}

$ExpressionBriefs = @{
    afraid = 'frightened, tense eyes, fear visible'
    angry = 'anger, furrowed brows, jaw set'
    authoritative = 'commanding, strict authority'
    broken = 'emotionally broken, exhausted despair'
    charming = 'warm charming smile, charismatic'
    dark = 'sinister undertone, shadowed expression'
    desperate = 'desperate, near panic, strained face'
    determined = 'resolute, focused, determined gaze'
    dreamy = 'distant dreamy gaze, detached'
    ghostly = 'ghostlike presence, pale unsettling calm'
    jovial = 'jovial, hearty expression'
    kind = 'gentle kindness, warm eyes'
    lucid = 'sudden clarity, alert urgency'
    mysterious = 'enigmatic half-smile, guarded eyes'
    neutral = 'neutral expression, calm'
    possessed = 'unnatural possession, unsettling eyes'
    praying = 'prayerful, hands clasped, solemn'
    protective = 'protective sternness, defensive posture'
    ritual = 'focused ritual concentration'
    sad = 'sadness, heavy eyes'
    smiling = 'soft sincere smile'
    suspicious = 'narrowed eyes, suspicion'
    thinking = 'thoughtful, contemplative'
    threatening = 'cold threat, intimidating look'
    warning = 'urgent warning expression'
    worried = 'anxious concern, slight frown'
    young = 'younger appearance, same core facial identity'
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $enc = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $enc)
}

function Ensure-Dir([string]$Path) {
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

function Write-TinyPng([string]$Path) {
    $tinyPngBase64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+X6t8AAAAASUVORK5CYII='
    $bytes = [Convert]::FromBase64String($tinyPngBase64)
    [System.IO.File]::WriteAllBytes($Path, $bytes)
}

function Require-PipelineScript() {
    if (-not (Test-Path $PipelineScript)) {
        throw "Missing pipeline script: $PipelineScript"
    }
}

function Load-Manifest() {
    if (-not (Test-Path $ManifestAbs)) {
        throw "Manifest not found: $ManifestPath. Run setup first."
    }
    return (Get-Content -Raw $ManifestAbs | ConvertFrom-Json)
}

function Make-BackgroundPrompt([string]$BaseName) {
    $brief = $BackgroundBriefs[$BaseName]
    if ([string]::IsNullOrWhiteSpace($brief)) {
        $brief = "$BaseName, black forest village horror setting"
    }

    return @(
        $StyleAnchor
        'Environment-only scene, no people.'
        "Location: $brief."
        'Mood: oppressive quiet, late autumn black forest.'
        'Framing: widescreen visual novel background.'
        'Output: one PNG image, no text, no logos, no watermark.'
    ) -join ' '
}

function Make-CharacterPrompt([string]$CharId, [string]$Expr) {
    $identity = $CharacterIdentity[$CharId]
    if ([string]::IsNullOrWhiteSpace($identity)) {
        $identity = "$CharId, human character in 1920s Germany"
    }

    $mood = $ExpressionBriefs[$Expr]
    if ([string]::IsNullOrWhiteSpace($mood)) {
        $mood = $Expr
    }

    return @(
        $StyleAnchor
        'Transparent background only.'
        'Upper-body visual novel sprite, centered.'
        "Character identity fixed: $identity."
        "Expression: $mood."
        'Keep same face structure, hair, age, and clothing as this character''s other expressions.'
        'Output: one PNG image with transparent background, no text, no logos, no watermark.'
    ) -join ' '
}

function Build-PromptEntry([object]$Entry) {
    $targetAbs = Join-Path $Root ([string]$Entry.target)
    $targetExists = Test-Path $targetAbs
    $filename = "$($Entry.id).png"
    $inboxAbs = Join-Path $InboxAbs $filename
    $inboxExists = Test-Path $inboxAbs

    $prompt = ''
    if ($Entry.type -eq 'background') {
        $prompt = Make-BackgroundPrompt -BaseName ([string]$Entry.base)
    } else {
        $prompt = Make-CharacterPrompt -CharId ([string]$Entry.character) -Expr ([string]$Entry.expression)
    }

    return [ordered]@{
        id = [string]$Entry.id
        type = [string]$Entry.type
        target = [string]$Entry.target
        target_exists = [bool]$targetExists
        inbox_filename = $filename
        inbox_exists = [bool]$inboxExists
        width = [int]$Entry.width
        height = [int]$Entry.height
        transparent = [bool]$Entry.transparent
        prompt = $prompt
    }
}

function Run-Setup() {
    Require-PipelineScript
    Ensure-Dir $InboxAbs
    Ensure-Dir (Join-Path $Root 'assets_pipeline/processed')
    Ensure-Dir (Join-Path $Root 'assets_pipeline/reports')
    Ensure-Dir $ChatGptAbs

    & powershell -ExecutionPolicy Bypass -File $PipelineScript -Action init-manifest -ManifestPath $ManifestPath
    if ($LASTEXITCODE -ne 0) {
        throw "Manifest initialization failed with exit code $LASTEXITCODE"
    }

    $dropNotePath = Join-Path $InboxAbs '_DROP_FILES_HERE.txt'
    $dropNote = @(
        'Drop ChatGPT-generated files here.'
        ''
        'Required naming: exact id from manifest + .png'
        'Examples:'
        'bg.village_square_v2.png'
        'char.elise.afraid_v2.png'
        ''
        'Then run:'
        'powershell -ExecutionPolicy Bypass -File scripts_assets/vn_assets_easy.ps1 -Action import'
    ) -join "`n"
    Write-Utf8NoBom -Path $dropNotePath -Content ($dropNote + "`n")
}

function Run-Prompts() {
    Ensure-Dir $ChatGptAbs
    Ensure-Dir $PlaceholderPngAbs
    $manifest = Load-Manifest

    $promptEntries = New-Object System.Collections.ArrayList
    foreach ($entry in $manifest.entries) {
        $p = Build-PromptEntry -Entry $entry
        if (-not $IncludeAlreadyExisting -and $p.target_exists) {
            continue
        }
        [void]$promptEntries.Add($p)
    }

    $stamp = (Get-Date).ToString('yyyyMMdd_HHmmss')
    $mdPath = Join-Path $ChatGptAbs 'chatgpt_prompt_pack.md'
    $jsonPath = Join-Path $ChatGptAbs 'chatgpt_prompt_pack.json'
    $listPath = Join-Path $ChatGptAbs 'chatgpt_filenames.txt'
    $copyPromptPath = Join-Path $ChatGptAbs 'chatgpt_copy_prompts.txt'
    $batchPath = Join-Path $ChatGptAbs 'chatgpt_batch_request.txt'
    $snapshotPath = Join-Path $ChatGptAbs ("chatgpt_prompt_pack_$stamp.json")

    $lines = @()
    $lines += '# ChatGPT Asset Prompt Pack (v2)'
    $lines += ''
    $lines += "Generated: $([DateTime]::Now.ToString('yyyy-MM-dd HH:mm:ss'))"
    $lines += "Entries in this pack: $($promptEntries.Count)"
    $lines += ''
    $lines += 'Use this loop:'
    $lines += '1. Copy a prompt block below into ChatGPT image generation.'
    $lines += '2. Download result as PNG.'
    $lines += '3. Rename file to exact `inbox_filename`.'
    $lines += "4. Place file in `$InboxDir`."
    $lines += ''

    $filenames = @()
    foreach ($p in $promptEntries) {
        $filenames += $p.inbox_filename
        $lines += "## $($p.id)"
        $lines += "- Type: $($p.type)"
        $lines += "- Target: $($p.target)"
        $lines += "- Size target in game: $($p.width)x$($p.height)"
        $lines += "- Transparent required: $($p.transparent)"
        $lines += "- Save as: $($p.inbox_filename)"
        $lines += ''
        $lines += '```text'
        $lines += $p.prompt
        $lines += '```'
        $lines += ''
    }

    if ($promptEntries.Count -eq 0) {
        $lines += 'All manifest targets already exist. Use `-IncludeAlreadyExisting` to regenerate a full prompt pack.'
        $lines += ''
    }

    Write-Utf8NoBom -Path $mdPath -Content (($lines -join "`n") + "`n")

    $json = $promptEntries | ConvertTo-Json -Depth 8
    Write-Utf8NoBom -Path $jsonPath -Content ($json + "`n")
    Write-Utf8NoBom -Path $snapshotPath -Content ($json + "`n")
    Write-Utf8NoBom -Path $listPath -Content (($filenames -join "`n") + $(if ($filenames.Count -gt 0) { "`n" } else { '' }))

    $copyLines = @()
    foreach ($p in $promptEntries) {
        $copyLines += $p.inbox_filename
        $copyLines += $p.prompt
        $copyLines += ''
    }
    if ($copyLines.Count -eq 0) {
        $copyLines += 'No missing entries found for prompt generation.'
    }
    Write-Utf8NoBom -Path $copyPromptPath -Content (($copyLines -join "`n") + "`n")

    $placeholderCount = 0
    foreach ($name in $filenames) {
        $placeholderPath = Join-Path $PlaceholderPngAbs $name
        if (-not (Test-Path $placeholderPath)) {
            Write-TinyPng -Path $placeholderPath
            $placeholderCount++
        }
    }

    $batchText = @(
        'Create visual novel art using this style for every image:'
        $StyleAnchor
        ''
        'For each item below, create one image and keep exact file names after download:'
        ($filenames -join "`n")
        ''
        "After generation, save PNGs and drop them into: $InboxDir"
    ) -join "`n"
    Write-Utf8NoBom -Path $batchPath -Content ($batchText + "`n")

    Write-Host "Prompt pack written: $mdPath"
    Write-Host "Prompt json written: $jsonPath"
    Write-Host "Snapshot written: $snapshotPath"
    Write-Host "Filename list written: $listPath"
    Write-Host "Copy/paste prompt text: $copyPromptPath"
    Write-Host "Batch request text: $batchPath"
    Write-Host "Placeholder PNG folder: $PlaceholderPngAbs"
    Write-Host "Placeholder PNG files created: $placeholderCount"
}

function Run-Status() {
    Require-PipelineScript
    & powershell -ExecutionPolicy Bypass -File $PipelineScript -Action run -ManifestPath $ManifestPath -InboxDir $InboxDir
    if ($LASTEXITCODE -ne 0) {
        throw "Status run failed with exit code $LASTEXITCODE"
    }
}

function Run-Import() {
    Require-PipelineScript
    & powershell -ExecutionPolicy Bypass -File $PipelineScript -Action run -ManifestPath $ManifestPath -InboxDir $InboxDir -ImportToAssets -RewriteDialogue
    if ($LASTEXITCODE -ne 0) {
        throw "Import run failed with exit code $LASTEXITCODE"
    }

    & powershell -ExecutionPolicy Bypass -File $PipelineScript -Action verify -ManifestPath $ManifestPath
    if ($LASTEXITCODE -ne 0) {
        throw "Verify failed with exit code $LASTEXITCODE"
    }
}

switch ($Action) {
    'setup' {
        Run-Setup
        Write-Host 'Setup complete.'
    }
    'prompts' {
        Run-Prompts
    }
    'status' {
        Run-Status
    }
    'import' {
        Run-Import
        Write-Host 'Import + dialogue rewrite + verify complete.'
    }
    'all' {
        Run-Setup
        Run-Prompts
        Write-Host 'Setup + prompt pack complete.'
        Write-Host "Next: generate images in ChatGPT, save to $InboxDir, then run -Action import"
    }
    default {
        throw "Unsupported action: $Action"
    }
}
