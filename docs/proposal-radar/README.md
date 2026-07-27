# Proposal Radar workspace

Operational engine for scoring **new Belgian policy proposals** (media + official). Sister of DOGE.

| Path | Purpose |
|------|---------|
| [../09-proposal-radar.md](../09-proposal-radar.md) | Full design + doctrine |
| [LOOP.md](LOOP.md) | Tick protocol |
| [schema.md](schema.md) | CSV schemas |
| [templates/analysis-memo.md](templates/analysis-memo.md) | Per-proposal memo |
| [data/](data/) | Live tables |
| [analyses/](analyses/) | Full scored memos |
| [public/](public/) | Leaderboards & weekly packs |
| [raw/](raw/) | Feed dumps / snapshots |
| [scripts/](scripts/) | Optional RSS/portal helpers |

## Quick start

1. Read `../09-proposal-radar.md` + `LOOP.md`  
2. Seed a URL into `data/ingest_queue.csv` **or** run `/proposal-radar`  
3. Agent analyses **one** proposal → memo + scores  
4. Refresh `public/leaderboard_clowns.md` and `public/leaderboard_genius.md` when scores change  

## Relation to DOGE

| DOGE | Proposal Radar |
|------|----------------|
| Existing spend / waste | Proposed rules & money |
| `docs/doge/` | `docs/proposal-radar/` |
| Absurdity of **paid** L5 | Clownpoints of **idea** |
| FOI for opacity | Optional FOI after adoption |

Link IDs across systems when a proposal funds a known waste line.
