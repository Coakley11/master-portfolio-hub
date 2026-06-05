# Start the portfolio site from the correct folder (required for resume & asset paths).
param(
    [int]$Port = 9890,
    [string]$HubRoot = (Split-Path $PSScriptRoot -Parent)
)

$siteDir = Join-Path $HubRoot "Portfolio Website"
if (-not (Test-Path $siteDir)) {
    Write-Error "Portfolio Website folder not found: $siteDir"
    exit 1
}

Write-Host ""
Write-Host "Daniel Cohen Portfolio — local server" -ForegroundColor Cyan
Write-Host "Serving: $siteDir"
Write-Host "Port:    $Port"
Write-Host ""
Write-Host "Open these URLs:" -ForegroundColor Green
Write-Host "  http://127.0.0.1:$Port/"
Write-Host "  http://127.0.0.1:$Port/resume-preview.html   (formatted resume)"
Write-Host "  http://127.0.0.1:$Port/resume.html            (resume hub)"
Write-Host "  http://127.0.0.1:$Port/career-profile.html"
Write-Host "  http://127.0.0.1:$Port/executive-summary.html"
Write-Host "  http://127.0.0.1:$Port/contact.html"
Write-Host ""
Write-Host "IMPORTANT: Do not run http.server from the Hub root — resume paths will 404." -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop." -ForegroundColor DarkGray
Write-Host ""

Set-Location $siteDir
python -m http.server $Port
