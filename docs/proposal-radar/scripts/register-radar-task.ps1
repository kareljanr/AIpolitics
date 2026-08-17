# Register Windows Task Scheduler job for daily Proposal Radar + Telegram.
# Run once (no admin needed for CurrentUser tasks):
#   powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\register-radar-task.ps1
#   powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\register-radar-task.ps1 -At "07:30AM" -WithAgent

param(
    [string]$At = "8:00AM",
    [switch]$WithAgent,
    [switch]$Unregister
)

$ErrorActionPreference = "Stop"
$TaskName = "AIpoliticsProposalRadarDaily"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
$ps = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$script = Join-Path $Root "docs\proposal-radar\scripts\run_daily_windows.ps1"

if ($Unregister) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Unregistered $TaskName"
    exit 0
}

if (-not (Test-Path $script)) {
    throw "Missing $script"
}

$arg = "-NoProfile -ExecutionPolicy Bypass -File `"$script`""
if ($WithAgent) { $arg += " -WithAgent" }

$action = New-ScheduledTaskAction -Execute $ps -Argument $arg -WorkingDirectory $Root
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2)

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null

Write-Host "Registered: $TaskName"
Get-ScheduledTask -TaskName $TaskName | Format-Table TaskName, State
Get-ScheduledTaskInfo -TaskName $TaskName | Format-List LastRunTime, NextRunTime, LastTaskResult
Write-Host ""
Write-Host "Daily at $At local. Script: $script"
Write-Host "WithAgent: $WithAgent  (default off; Grok durable scheduler still does deep scores)"
Write-Host ""
Write-Host "BEFORE first real Telegram send:"
Write-Host "  1. Create SEPARATE Telegram group (or forum topic) for AIpolitics - not the finance chat"
Write-Host "  2. Add bot; python docs\proposal-radar\scripts\telegram_notify.py --setup-help"
Write-Host "  3. Copy config\telegram.env.example -> config\telegram.env and set TELEGRAM_CHAT_ID"
Write-Host "  4. Test: powershell -File docs\proposal-radar\scripts\run_daily_windows.ps1 -DryRunTelegram"
Write-Host "  5. Test send: python docs\proposal-radar\scripts\telegram_notify.py"
Write-Host ""
Write-Host "Manual run now:"
Write-Host "  $ps -NoProfile -ExecutionPolicy Bypass -File `"$script`" -DryRunTelegram"
