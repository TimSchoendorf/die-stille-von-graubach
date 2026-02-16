param(
    [ValidateSet('init-manifest','run','verify','rewrite')]
    [string]$Action = 'run',
    [string]$ManifestPath = 'assets_pipeline/manifest.json',
    [string]$InboxDir = 'assets_pipeline/inbox',
    [string]$ProcessedDir = 'assets_pipeline/processed',
    [string]$ReportDir = 'assets_pipeline/reports',
    [switch]$ImportToAssets,
    [switch]$RewriteDialogue,
    [switch]$StrictTransparency
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$Root = (Get-Location).Path
$DialogueDir = Join-Path $Root 'data/dialogue'
$BackgroundDir = Join-Path $Root 'assets/sprites/backgrounds'
$CharacterDir = Join-Path $Root 'assets/sprites/characters'

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $enc = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $enc)
}

function Normalize-BaseName([string]$Name) {
    if ($null -eq $Name) { return '' }
    if ($Name.EndsWith('_v2')) { return $Name.Substring(0, $Name.Length - 3) }
    return $Name
}

function Get-DialogueFiles() {
    return Get-ChildItem -Path $DialogueDir -Recurse -File -Filter '*.json'
}

function Get-DialogueUsage() {
    $backgrounds = New-Object 'System.Collections.Generic.HashSet[string]'
    $characterExpressions = @{}

    $characterFolders = New-Object 'System.Collections.Generic.HashSet[string]'
    if (Test-Path $CharacterDir) {
        Get-ChildItem -Path $CharacterDir -Directory | ForEach-Object {
            [void]$characterFolders.Add($_.Name)
        }
    }

    foreach ($file in (Get-DialogueFiles)) {
        $json = Get-Content -Raw $file.FullName | ConvertFrom-Json
        if ($null -eq $json.nodes) { continue }

        foreach ($prop in $json.nodes.PSObject.Properties) {
            $node = $prop.Value

            if ($null -ne $node.background -and "$($node.background)" -ne '') {
                [void]$backgrounds.Add((Normalize-BaseName ([string]$node.background)))
            }

            if ($null -ne $node.character -and $null -ne $node.expression -and "$($node.character)" -ne '' -and "$($node.expression)" -ne '') {
                $charId = [string]$node.character
                if (-not $characterExpressions.ContainsKey($charId)) {
                    $characterExpressions[$charId] = New-Object 'System.Collections.Generic.HashSet[string]'
                }
                [void]$characterExpressions[$charId].Add((Normalize-BaseName ([string]$node.expression)))
            }

            if ($null -ne $node.speaker -and $null -ne $node.expression -and "$($node.speaker)" -ne '' -and "$($node.expression)" -ne '') {
                $speaker = [string]$node.speaker
                if ($characterFolders.Contains($speaker)) {
                    if (-not $characterExpressions.ContainsKey($speaker)) {
                        $characterExpressions[$speaker] = New-Object 'System.Collections.Generic.HashSet[string]'
                    }
                    [void]$characterExpressions[$speaker].Add((Normalize-BaseName ([string]$node.expression)))
                }
            }
        }
    }

    return @{
        backgrounds = $backgrounds
        character_expressions = $characterExpressions
    }
}

function Build-Manifest() {
    $usage = Get-DialogueUsage
    $entries = New-Object System.Collections.ArrayList

    foreach ($bg in ($usage.backgrounds | Sort-Object)) {
        if ([string]::IsNullOrWhiteSpace($bg)) { continue }
        [void]$entries.Add([ordered]@{
            id = "bg.$($bg)_v2"
            type = 'background'
            base = $bg
            target = "assets/sprites/backgrounds/$($bg)_v2.png"
            width = 1920
            height = 1080
            transparent = $false
        })
    }

    foreach ($charId in ($usage.character_expressions.Keys | Sort-Object)) {
        foreach ($expr in ([string[]]$usage.character_expressions[$charId] | Sort-Object)) {
            if ([string]::IsNullOrWhiteSpace($expr)) { continue }
            [void]$entries.Add([ordered]@{
                id = "char.$charId.$($expr)_v2"
                type = 'character'
                character = $charId
                expression = $expr
                base_expression = $expr
                target = "assets/sprites/characters/$charId/$($expr)_v2.png"
                width = 600
                height = 900
                transparent = $true
            })
        }
    }

    return [ordered]@{
        project = 'VisualNovel'
        version = 1
        generated_at = (Get-Date).ToString('s')
        naming_rule = 'Put source images in inbox using exact id as filename stem (id.png, id.jpg, or id.jpeg).'
        entries = $entries
    }
}

function Save-Manifest([object]$Manifest) {
    $json = $Manifest | ConvertTo-Json -Depth 100
    Write-Utf8NoBom -Path $ManifestPath -Content ($json + "`n")
}

function Load-Manifest() {
    if (-not (Test-Path $ManifestPath)) {
        throw "Manifest not found: $ManifestPath. Run with -Action init-manifest first."
    }
    return (Get-Content -Raw $ManifestPath | ConvertFrom-Json)
}

function Find-SourceForEntry([object]$Entry) {
    $exts = @('png','jpg','jpeg')
    foreach ($ext in $exts) {
        $candidate = Join-Path $InboxDir ($Entry.id + '.' + $ext)
        if (Test-Path $candidate) { return $candidate }
    }
    return $null
}

function Test-TransparentCorners([System.Drawing.Bitmap]$Bmp) {
    $corners = @(
        @(0,0),
        @($Bmp.Width - 1,0),
        @(0,$Bmp.Height - 1),
        @($Bmp.Width - 1,$Bmp.Height - 1)
    )

    foreach ($pair in $corners) {
        $x = [int]$pair[0]
        $y = [int]$pair[1]
        $p = $Bmp.GetPixel($x, $y)
        if ($p.A -gt 5) { return $false }
    }
    return $true
}

function New-Canvas([int]$Width, [int]$Height, [bool]$Transparent) {
    $bmp = New-Object System.Drawing.Bitmap($Width, $Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    try {
        if ($Transparent) {
            $g.Clear([System.Drawing.Color]::FromArgb(0,0,0,0))
        } else {
            $g.Clear([System.Drawing.Color]::Black)
        }
    } finally {
        $g.Dispose()
    }
    return $bmp
}

function Draw-Contain([System.Drawing.Bitmap]$Dest, [System.Drawing.Image]$Src) {
    $g = [System.Drawing.Graphics]::FromImage($Dest)
    try {
        $g.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceOver
        $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

        $scale = [Math]::Min($Dest.Width / $Src.Width, $Dest.Height / $Src.Height)
        $drawW = [int][Math]::Round($Src.Width * $scale)
        $drawH = [int][Math]::Round($Src.Height * $scale)
        $x = [int](($Dest.Width - $drawW) / 2)
        $y = [int](($Dest.Height - $drawH) / 2)
        $rect = New-Object System.Drawing.Rectangle($x, $y, $drawW, $drawH)
        $g.DrawImage($Src, $rect)
    } finally {
        $g.Dispose()
    }
}

function Draw-Cover([System.Drawing.Bitmap]$Dest, [System.Drawing.Image]$Src) {
    $g = [System.Drawing.Graphics]::FromImage($Dest)
    try {
        $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

        $scale = [Math]::Max($Dest.Width / $Src.Width, $Dest.Height / $Src.Height)
        $drawW = [int][Math]::Round($Src.Width * $scale)
        $drawH = [int][Math]::Round($Src.Height * $scale)
        $x = [int](($Dest.Width - $drawW) / 2)
        $y = [int](($Dest.Height - $drawH) / 2)
        $rect = New-Object System.Drawing.Rectangle($x, $y, $drawW, $drawH)
        $g.DrawImage($Src, $rect)
    } finally {
        $g.Dispose()
    }
}

function Normalize-EntryImage([object]$Entry, [string]$SourcePath, [string]$ProcessedPath) {
    $src = [System.Drawing.Image]::FromFile($SourcePath)
    try {
        $targetW = [int]$Entry.width
        $targetH = [int]$Entry.height
        $dest = New-Canvas -Width $targetW -Height $targetH -Transparent ([bool]$Entry.transparent)
        try {
            if ([bool]$Entry.transparent) {
                Draw-Contain -Dest $dest -Src $src
            } else {
                Draw-Cover -Dest $dest -Src $src
            }

            $outDir = Split-Path -Parent $ProcessedPath
            if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force $outDir | Out-Null }
            $dest.Save($ProcessedPath, [System.Drawing.Imaging.ImageFormat]::Png)

            $cornerTransparent = $true
            if ([bool]$Entry.transparent) {
                $cornerTransparent = Test-TransparentCorners -Bmp $dest
            }

            return @{
                width = $dest.Width
                height = $dest.Height
                transparent_corners = $cornerTransparent
            }
        } finally {
            $dest.Dispose()
        }
    } finally {
        $src.Dispose()
    }
}

function Build-ProcessedPath([object]$Entry) {
    if ($Entry.type -eq 'background') {
        return (Join-Path $ProcessedDir ("backgrounds/$($Entry.base)_v2.png"))
    }
    return (Join-Path $ProcessedDir ("characters/$($Entry.character)/$($Entry.expression)_v2.png"))
}

function Write-Report([object]$Report) {
    if (-not (Test-Path $ReportDir)) { New-Item -ItemType Directory -Force $ReportDir | Out-Null }

    $stamp = (Get-Date).ToString('yyyyMMdd_HHmmss')
    $jsonPath = Join-Path $ReportDir ("pipeline_report_$stamp.json")
    $txtPath = Join-Path $ReportDir ("pipeline_report_$stamp.txt")

    $json = $Report | ConvertTo-Json -Depth 100
    Write-Utf8NoBom -Path $jsonPath -Content ($json + "`n")

    $lines = @()
    $lines += "Action: $($Report.action)"
    $lines += "Timestamp: $($Report.timestamp)"
    $lines += "Entries total: $($Report.total_entries)"
    $lines += "Processed: $($Report.processed_count)"
    $lines += "Missing source: $($Report.missing_count)"
    $lines += "Transparency warnings: $($Report.transparency_warning_count)"
    $lines += ''

    if ($Report.missing.Count -gt 0) {
        $lines += 'Missing source files:'
        foreach ($m in $Report.missing) { $lines += "- $m" }
        $lines += ''
    }

    if ($Report.transparency_warnings.Count -gt 0) {
        $lines += 'Transparency warnings:'
        foreach ($w in $Report.transparency_warnings) { $lines += "- $w" }
        $lines += ''
    }

    Write-Utf8NoBom -Path $txtPath -Content (($lines -join "`n") + "`n")

    return @{ json = $jsonPath; text = $txtPath }
}

function Rewrite-DialogueFromManifest([object]$Manifest) {
    $bgBases = New-Object 'System.Collections.Generic.HashSet[string]'
    $exprBases = New-Object 'System.Collections.Generic.HashSet[string]'

    foreach ($entry in $Manifest.entries) {
        if ($entry.type -eq 'background') {
            [void]$bgBases.Add([string]$entry.base)
        } elseif ($entry.type -eq 'character') {
            [void]$exprBases.Add([string]$entry.base_expression)
        }
    }

    $rewritten = 0
    foreach ($file in (Get-DialogueFiles)) {
        $content = Get-Content -Raw $file.FullName
        $updated = $content

        foreach ($bg in $bgBases) {
            $pattern = '("background"\s*:\s*")' + [Regex]::Escape($bg) + '("(?!_v2))'
            $updated = [Regex]::Replace($updated, $pattern, ('$1' + $bg + '_v2$2'))
        }

        foreach ($expr in $exprBases) {
            $pattern = '("expression"\s*:\s*")' + [Regex]::Escape($expr) + '("(?!_v2))'
            $updated = [Regex]::Replace($updated, $pattern, ('$1' + $expr + '_v2$2'))
        }

        if ($updated -ne $content) {
            Write-Utf8NoBom -Path $file.FullName -Content $updated
            $rewritten++
        }
    }

    return $rewritten
}

function Verify-ManifestTargets([object]$Manifest) {
    $missingTargets = New-Object System.Collections.ArrayList
    foreach ($entry in $Manifest.entries) {
        $targetPath = Join-Path $Root $entry.target
        if (-not (Test-Path $targetPath)) {
            [void]$missingTargets.Add($entry.id)
        }
    }
    return $missingTargets
}

if ($Action -eq 'init-manifest') {
    $manifest = Build-Manifest
    Save-Manifest -Manifest $manifest
    Write-Host "Manifest created: $ManifestPath"
    Write-Host "Entries: $($manifest.entries.Count)"
    exit 0
}

$manifest = Load-Manifest

if ($Action -eq 'rewrite') {
    $rewritten = Rewrite-DialogueFromManifest -Manifest $manifest
    Write-Host "Dialogue files rewritten: $rewritten"
    exit 0
}

if ($Action -eq 'verify') {
    $missingTargets = Verify-ManifestTargets -Manifest $manifest
    if ($missingTargets.Count -eq 0) {
        Write-Host 'Verify OK: all manifest targets exist.'
    } else {
        Write-Host "Missing targets: $($missingTargets.Count)"
        foreach ($id in $missingTargets) { Write-Host "- $id" }
        exit 2
    }
    exit 0
}

$report = [ordered]@{
    action = 'run'
    timestamp = (Get-Date).ToString('s')
    total_entries = $manifest.entries.Count
    processed_count = 0
    missing_count = 0
    transparency_warning_count = 0
    missing = New-Object System.Collections.ArrayList
    transparency_warnings = New-Object System.Collections.ArrayList
}

foreach ($entry in $manifest.entries) {
    $src = Find-SourceForEntry -Entry $entry
    if ($null -eq $src) {
        [void]$report.missing.Add($entry.id)
        continue
    }

    $processedPath = Build-ProcessedPath -Entry $entry
    $meta = Normalize-EntryImage -Entry $entry -SourcePath $src -ProcessedPath $processedPath
    $report.processed_count++

    if ([bool]$entry.transparent -and -not [bool]$meta.transparent_corners) {
        $msg = "$($entry.id) has non-transparent corners after normalization"
        [void]$report.transparency_warnings.Add($msg)
        if ($StrictTransparency) {
            throw "Strict transparency failed: $msg"
        }
    }

    if ($ImportToAssets) {
        $targetPath = Join-Path $Root $entry.target
        $targetDir = Split-Path -Parent $targetPath
        if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Force $targetDir | Out-Null }
        Copy-Item -Force $processedPath $targetPath
    }
}

$report.missing_count = $report.missing.Count
$report.transparency_warning_count = $report.transparency_warnings.Count
$paths = Write-Report -Report $report

Write-Host "Processed: $($report.processed_count) / $($report.total_entries)"
Write-Host "Missing: $($report.missing_count)"
Write-Host "Transparency warnings: $($report.transparency_warning_count)"
Write-Host "Report JSON: $($paths.json)"
Write-Host "Report TXT:  $($paths.text)"

if ($ImportToAssets -and $RewriteDialogue) {
    $rewritten = Rewrite-DialogueFromManifest -Manifest $manifest
    Write-Host "Dialogue files rewritten: $rewritten"
}
