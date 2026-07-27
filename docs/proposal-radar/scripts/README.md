# Proposal Radar scripts

Full auto path (no human required for ingest + export):

```powershell
cd C:\Users\karel\dev\AIpolitics
pip install feedparser requests   # once
python docs/proposal-radar/scripts/run_pipeline.py
# scoring of top candidates: agent /proposal-radar OR
python docs/proposal-radar/scripts/seed_score_batch.py   # calibration batch writer
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
