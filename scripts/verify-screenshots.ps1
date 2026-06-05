# Verify screenshot references in projects.json against files on disk.
param(
    [string]$HubRoot = (Split-Path $PSScriptRoot -Parent)
)

$jsonPath = Join-Path $HubRoot "Portfolio Website\data\projects.json"
$assetsBase = Join-Path $HubRoot "Portfolio Website\assets\screenshots"
$data = Get-Content $jsonPath -Raw | ConvertFrom-Json

$refs = [System.Collections.Generic.HashSet[string]]::new()
foreach ($repo in $data.repos) {
    foreach ($s in ($repo.screenshots | Where-Object { $_ })) { [void]$refs.Add($s) }
    if ($repo.heroScreenshot -and $repo.screenshotFolder) {
        [void]$refs.Add("assets/screenshots/$($repo.screenshotFolder)/$($repo.heroScreenshot)")
    }
}
# SQL workbook map in main.js — hardcoded list from manifest
@(
    'assets/screenshots/SQL-Excel/sql-excel-ai-evaluator-dashboard.png',
    'assets/screenshots/SQL-Excel/sql-excel-investment-workbook-dashboard.png',
    'assets/screenshots/SQL-Excel/sql-excel-quant-claims.png',
    'assets/screenshots/SQL-Excel/sql-excel-real-world-credit-risk.png'
) | ForEach-Object { [void]$refs.Add($_) }

$missing = @()
$found = @()
foreach ($ref in ($refs | Sort-Object)) {
    $full = Join-Path $HubRoot ("Portfolio Website\" + ($ref -replace '/', '\'))
    if (Test-Path $full) { $found += $ref } else { $missing += $ref }
}

Write-Host "Screenshot verification - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Host "Found: $($found.Count)  Missing: $($missing.Count)"
if ($missing.Count) {
    Write-Host "`nMISSING:"
    $missing | ForEach-Object { Write-Host "  $_" }
    exit 1
}
Write-Host "All $($found.Count) referenced screenshots present."
exit 0
