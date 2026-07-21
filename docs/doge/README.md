# DOGE data workspace

Operational engine for the Belgium waste map.

| Path | Purpose |
|------|---------|
| [../06b-doge-discovery-strategy.md](../06b-doge-discovery-strategy.md) | Full discovery strategy |
| [LOOP.md](LOOP.md) | 15-minute research loop protocol |
| [schema.md](schema.md) | CSV schemas |
| [foi-template-nl.md](foi-template-nl.md) | Openbaarheid letter template |
| [data/](data/) | Live tables (queues, budgets, leaderboard, …) |
| [foi/drafts/](foi/drafts/) | Letters ready to human-send |
| [foi/archive/](foi/archive/) | Sent + answered copies |
| [loop_log.md](loop_log.md) | Tick diary |

## Quick start

1. Read `LOOP.md`  
2. Run one tick (agent or human): highest priority `research_queue` row  
3. Any opacity → row in `foi_queue.csv` + draft in `foi/drafts/`  
4. Human send day: filter `status=ready`  

## Completeness

Asymptotic. Loop until high-priority public work is done; then FOI waiting; then new sprints forever.
