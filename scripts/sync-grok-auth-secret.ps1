# Push the local Grok login to the Actions secret when grok models accepts it.
# The access token lasts about six hours. This keeps GROK_AUTH_JSON ahead of
# expiry while this PC is on, so Actions does not have to rotate the refresh token.
$ErrorActionPreference = "Stop"
$grok = Join-Path $env:USERPROFILE ".grok\bin\grok.exe"
$gh = "C:\Program Files\GitHub CLI\gh.exe"
if (-not (Test-Path $grok)) { throw "grok.exe not found" }
if (-not (Test-Path $gh)) { throw "gh.exe not found" }

$first = (& $grok models 2>&1 | Select-Object -First 1 | Out-String).Trim()
if ($first -notmatch "logged in" -or $first -match "not authenticated" -or $first -match "Not signed in") {
  Write-Output "Grok login not accepted. Secret unchanged."
  exit 0
}

cmd /c "gh secret set GROK_AUTH_JSON --repo kareljanr/AIpolitics < %USERPROFILE%\.grok\auth.json"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Output "GROK_AUTH_JSON updated from local login."
