# Deploy Master Portfolio Hub website to GitHub Pages under Coakley11.
# Prerequisites: gh auth login

$ErrorActionPreference = "Stop"
$Hub = Split-Path -Parent $PSScriptRoot
Set-Location $Hub

$RepoName = "master-portfolio-hub"
$Owner = "Coakley11"
$ExpectedUrl = "https://$Owner.github.io/$RepoName/"

Write-Host "Checking GitHub auth..."
gh auth status
if ($LASTEXITCODE -ne 0) {
  Write-Host "Run: gh auth login --web --git-protocol https"
  exit 1
}

$exists = gh repo view "$Owner/$RepoName" 2>$null
if (-not $exists) {
  Write-Host "Creating public repo $Owner/$RepoName ..."
  gh repo create "$Owner/$RepoName" --public --source=. --remote=origin --description "Daniel Cohen — Analytics, Quantitative Modeling & AI Portfolio Website"
} else {
  $remote = git remote get-url origin 2>$null
  if (-not $remote) {
    git remote add origin "https://github.com/$Owner/$RepoName.git"
  }
}

Write-Host "Pushing master..."
git push -u origin master

Write-Host "Configuring GitHub Pages from /Portfolio Website on master..."
gh api -X POST "repos/$Owner/$RepoName/pages" -f build_type=legacy -f source='{"branch":"master","path":"/Portfolio Website"}' 2>$null
if ($LASTEXITCODE -ne 0) {
  # update existing pages config
  gh api -X PUT "repos/$Owner/$RepoName/pages" -f build_type=legacy -f source='{"branch":"master","path":"/Portfolio Website"}'
}

Write-Host ""
Write-Host "Public portfolio URL (after Pages builds ~1-3 min):"
Write-Host $ExpectedUrl
Write-Host ""
Write-Host "Verify with:"
Write-Host "  Start-Sleep 90; Invoke-WebRequest $ExpectedUrl"
