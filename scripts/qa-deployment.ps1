# Final deployment QA — run from Master Portfolio Hub with local server on $Port
param(
    [int]$Port = 9890,
    [string]$HubRoot = (Split-Path $PSScriptRoot -Parent)
)

$base = "http://127.0.0.1:$Port"
$siteRoot = Join-Path $HubRoot "Portfolio Website"
$failures = @()
$passes = @()

function Test-Url($path, $label, $minBytes = 500) {
    try {
        $r = Invoke-WebRequest -Uri "$base/$path" -UseBasicParsing -TimeoutSec 10
        if ($r.StatusCode -ne 200) { $script:failures += "$label : HTTP $($r.StatusCode)"; return $false }
        if ($r.RawContentLength -lt $minBytes -and $path -notmatch '\.pdf$') {
            $script:failures += "$label : suspicious size $($r.RawContentLength)b"; return $false
        }
        $script:passes += "$label : OK ($($r.RawContentLength)b)"
        return $true
    } catch {
        $script:failures += "$label : $($_.Exception.Message)"
        return $false
    }
}

function Test-Png($path) {
    try {
        $r = Invoke-WebRequest -Uri "$base/$path" -UseBasicParsing -TimeoutSec 10
        $bytes = $r.Content
        if ($bytes.Length -ge 4 -and $bytes[0] -eq 137 -and $bytes[1] -eq 80 -and $bytes[2] -eq 78 -and $bytes[3] -eq 71) {
            $script:passes += "PNG $path : OK ($($bytes.Length)b)"
            return $true
        }
        $script:failures += "PNG $path : invalid header"
        return $false
    } catch {
        $script:failures += "PNG $path : $($_.Exception.Message)"
        return $false
    }
}

Write-Host "=== Final Deployment QA ===" -ForegroundColor Cyan
Write-Host "Server: $base`n"

# Core pages
$pages = @(
    @{ p = 'index.html'; l = 'Home'; min = 3000 },
    @{ p = 'career-profile.html'; l = 'Career'; min = 1000 },
    @{ p = 'executive-summary.html'; l = 'Summary'; min = 1000 },
    @{ p = 'resume.html'; l = 'Resume Hub'; min = 1000 },
    @{ p = 'resume-preview.html'; l = 'Resume Preview'; min = 1000 },
    @{ p = 'sql-excel.html'; l = 'SQL & Excel'; min = 2000 },
    @{ p = 'contact.html'; l = 'Contact'; min = 1000 },
    @{ p = 'summary.html'; l = 'Summary alias'; min = 200 },
    @{ p = 'career.html'; l = 'Career alias'; min = 200 },
    @{ p = 'projects.html'; l = 'Projects alias'; min = 200 },
    @{ p = 'project.html?id=investment-portfolio-analyzer'; l = 'Project Detail'; min = 1000 },
    @{ p = 'data/projects.json'; l = 'projects.json'; min = 30000 }
)
foreach ($pg in $pages) { Test-Url $pg.p $pg.l $pg.min | Out-Null }

# Resume assets
Test-Url 'assets/docs/daniel-cohen-resume.pdf' 'Resume PDF' 1000 | Out-Null
Test-Url 'assets/docs/resume-project-descriptions.md' 'Resume MD' 500 | Out-Null

# Resume paths from JSON
$json = Get-Content (Join-Path $siteRoot 'data\projects.json') -Raw | ConvertFrom-Json
Test-Url $json.site.resumeView.Replace('\','/') 'Resume View path' 1000 | Out-Null
Test-Url $json.site.resumePdf.Replace('\','/') 'Resume PDF path' 1000 | Out-Null

# Homepage email check (static HTML only)
$index = Get-Content (Join-Path $siteRoot 'index.html') -Raw
if ($index -match 'daniel\.cohen11@yahoo|mailto:') {
    $failures += 'Homepage static HTML: email exposed'
} else {
    $passes += 'Homepage static HTML: no email'
}

# main.js homepage CTA check — inspect renderCtaSection body only
$mainJs = Get-Content (Join-Path $siteRoot 'js\main.js') -Raw
if ($mainJs -match 'function renderCtaSection\(data\)\s*\{([\s\S]*?)\n\}') {
    $ctaBody = $Matches[1]
    if ($ctaBody -match 'mailto:|site\.email') {
        $failures += 'main.js renderCtaSection: email exposed on homepage'
    } else {
        $passes += 'main.js renderCtaSection: no email on homepage'
    }
} else {
    $failures += 'main.js: renderCtaSection not found'
}

# P0 hero PNGs
$heroes = @(
    'assets/screenshots/Investment/investment-overview-demo.png',
    'assets/screenshots/Baseball/baseball-draft-assistant-demo.png',
    'assets/screenshots/Applied-Math/applied-math-betting-ev-demo.png',
    'assets/screenshots/NBA/nba-home-dashboard-demo.png',
    'assets/screenshots/Music/music-practice-demo.png'
)
foreach ($h in $heroes) { Test-Png $h | Out-Null }

# Nav link files exist on disk
$navPaths = @(
    'index.html','career-profile.html','executive-summary.html',
    'resume.html','sql-excel.html','contact.html'
)
foreach ($n in $navPaths) {
    $disk = Join-Path $siteRoot $n
    if (Test-Path $disk) { $passes += "Nav target exists: $n" }
    else { $failures += "Nav target missing: $n" }
}

Write-Host "`nPASSED ($($passes.Count)):" -ForegroundColor Green
$passes | ForEach-Object { Write-Host "  $_" }

if ($failures.Count) {
    Write-Host "`nFAILED ($($failures.Count)):" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "  $_" }
    exit 1
}
Write-Host "`nAll QA checks passed." -ForegroundColor Green
exit 0
