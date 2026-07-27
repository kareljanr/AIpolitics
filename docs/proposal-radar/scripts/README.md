# Proposal Radar scripts

## Live schedule

- **Daily Grok durable task:** `019fa3e112ab` (interval `1d`) — RSS harvest + one Proposal Radar tick (score/seed/weekly), then commit/push.
- Pause: set `data/loop_state.csv` → `paused=yes`.
- Manual anytime: `/proposal-radar` or pipeline below.

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
