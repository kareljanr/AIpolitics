# Daily Proposal Radar job for Windows Task Scheduler.
# - git pull
# - RSS harvest + leaderboard export
# - optional Grok agent tick (if grok on PATH and -WithAgent)
# - Telegram digest (politics chat only)
#
# Manual:
#   powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\run_daily_windows.ps1
#   powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\run_daily_windows.ps1 -WithAgent
#   powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\run_daily_windows.ps1 -DryRunTelegram

param(
    [switch]$WithAgent,
    [switch]$DryRunTelegram,
    [switch]$SkipGit,
    [switch]$SkipRss
)

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
Set-Location $Root

$LogDir = Join-Path $Root "docs\proposal-radar\raw"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir ("windows_daily_{0:yyyyMMdd_HHmmss}.log" -f (Get-Date))

function Write-Log([string]$msg) {
    $line = "{0:u}  {1}" -f (Get-Date).ToUniversalTime(), $msg
    Add-Content -Path $LogFile -Value $line -Encoding utf8
    Write-Host $line
}

Write-Log "=== Proposal Radar Windows daily start ==="
Write-Log "Root=$Root"

$python = (Get-Command python -ErrorAction SilentlyContinue | Select-Object -First 1).Source
if (-not $python) {
    $python = "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe"
}
if (-not (Test-Path $python)) {
    Write-Log "ERROR: python not found"
    exit 1
}
Write-Log "Python=$python"

# --- git pull ---
if (-not $SkipGit) {
    try {
        & git -C $Root pull --ff-only origin main 2>&1 | ForEach-Object { Write-Log $_ }
    } catch {
        Write-Log "WARN: git pull failed: $_"
    }
}

# --- RSS pipeline ---
if (-not $SkipRss) {
    try {
        & $python -m pip install --quiet feedparser requests 2>&1 | Out-Null
        Write-Log "Running run_pipeline.py"
        & $python (Join-Path $Root "docs\proposal-radar\scripts\run_pipeline.py") 2>&1 | ForEach-Object { Write-Log $_ }
        if ($LASTEXITCODE -ne 0) { Write-Log "WARN: pipeline exit $LASTEXITCODE" }
    } catch {
        Write-Log "WARN: RSS pipeline: $_"
    }
}

# --- optional Grok agent tick (default off: Grok durable scheduler already analyses) ---
$agentOk = $false
if ($WithAgent) {
    $grok = (Get-Command grok -ErrorAction SilentlyContinue | Select-Object -First 1).Source
    if ($grok) {
        Write-Log "Running grok proposal-radar tick"
        $prompt = @"
AIpolitics Proposal Radar — Windows daily tick.
Repo: $Root. Follow docs/proposal-radar/LOOP.md and .grok/skills/proposal-radar/SKILL.md.
1) If loop_state paused=yes: log idle and stop.
2) Prefer one analyse/seed unit from ingest_queue (Belgium only). Smaakhaven depth bar. Taxpayer pain mandatory when euro known.
3) Commit+push if files changed. Brief summary at end.
"@
        try {
            & $grok -p $prompt --cwd $Root --max-turns 40 2>&1 | ForEach-Object { Write-Log $_ }
            $agentOk = ($LASTEXITCODE -eq 0)
        } catch {
            Write-Log "WARN: grok tick failed: $_"
        }
    } else {
        Write-Log "WARN: -WithAgent set but grok not on PATH"
    }
} else {
    Write-Log "Skip agent tick (use Grok durable 019fa3e112ab, or pass -WithAgent)"
}

# --- Telegram ---
$tgArgs = @()
if ($DryRunTelegram) { $tgArgs += "--dry-run" }
try {
    Write-Log "Telegram notify"
    & $python (Join-Path $Root "docs\proposal-radar\scripts\telegram_notify.py") @tgArgs 2>&1 | ForEach-Object { Write-Log $_ }
    $tgCode = $LASTEXITCODE
} catch {
    Write-Log "ERROR: telegram: $_"
    $tgCode = 1
}

Write-Log "=== done agentOk=$agentOk telegramExit=$tgCode log=$LogFile ==="
# Non-zero only if telegram hard-failed without dry-run (RSS failures are soft)
if ($tgCode -ne 0 -and -not $DryRunTelegram) { exit $tgCode }
exit 0
