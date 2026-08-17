# Proposal Radar scripts

## Live schedule

### A) Grok durable (deep scores)

- **Daily Grok durable task:** `019fa3e112ab` (interval `1d`) — RSS + one analyse unit + commit/push.
- Pause: set `data/loop_state.csv` → `paused=yes`.

### B) Windows Task Scheduler (RSS + Telegram digest)

Keeps finance Telegram **separate** — uses portfolio bot **token** only; politics needs its **own chat/topic**.

```powershell
cd C:\Users\karel\dev\AIpolitics

# 1) Telegram setup help
python docs\proposal-radar\scripts\telegram_notify.py --setup-help

# 2) Create NEW group "AIpolitics Radar" (recommended) OR new forum topic in an existing supergroup
#    Add the same BotFather bot; post once; resolve ids:
python docs\proposal-radar\scripts\telegram_notify.py --resolve-chats

# 3) Config (gitignored)
copy docs\proposal-radar\config\telegram.env.example docs\proposal-radar\config\telegram.env
# edit TELEGRAM_CHAT_ID=...  (token can stay empty → loads from portfolio signals\.env)

# 4) Dry-run digest
powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\run_daily_windows.ps1 -DryRunTelegram

# 5) Register daily 08:00 local
powershell -ExecutionPolicy Bypass -File docs\proposal-radar\scripts\register-radar-task.ps1 -At 8:00AM

# Optional: also run grok agent on Windows (usually leave OFF — durable scheduler already scores)
# powershell -File docs\proposal-radar\scripts\register-radar-task.ps1 -At 8:00AM -WithAgent
```

Task name: **`AIpoliticsProposalRadarDaily`**. Unregister: `register-radar-task.ps1 -Unregister`.

Manual anytime: `/proposal-radar` or pipeline below.

## Full auto path (ingest + export)

```powershell
cd C:\Users\karel\dev\AIpolitics
pip install feedparser requests   # once
python docs/proposal-radar/scripts/run_pipeline.py
# scoring: agent /proposal-radar (or daily scheduler)
python docs/proposal-radar/scripts/export_leaderboard.py
```

| Script | Purpose |
|--------|---------|
| `config_feeds.json` | Allowlisted RSS + keywords |
| `rss_harvest.py` | Poll feeds → `ingest_queue.csv` + `sources.csv` + raw TSV dump |
| `export_leaderboard.py` | Regenerate public leaderboards + weekly pack |
| `run_pipeline.py` | harvest + export |
| `seed_score_batch.py` | Write scored calibration proposals (re-run only when intentional) |

## Filter logic

- Keyword hits (NL/FR/EN policy lexicon)  
- **BE signal** required for high priority (België, Vlaanderen, ministers, parties, …)  
- Hard foreign/sport noise rejected  
- Gov feeds boosted  

## Rules

Rate-limit; store URL + access date; no illegal paywall bypass; `discovered_via=rss`.
