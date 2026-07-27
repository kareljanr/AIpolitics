# Proposal Radar research loop

Recurring agent protocol. Goal: **each tick leaves the proposal dataset richer** — either a cleaner ingest queue or one fully truth-checked, scored proposal.

Sister of [`docs/doge/LOOP.md`](../doge/LOOP.md). Design: [`docs/09-proposal-radar.md`](../09-proposal-radar.md).

## Cadence

- **Manual:** `/proposal-radar` anytime.  
- **Scheduled (optional):** 6h–24h interval once DOGE-style thrash is understood. Not 60s — analysis is heavier than one budget line.  
- **Tick budget:** one primary unit; stop after ~20–25 min.

## Pause rule

- Pause only if `paused=yes` **by human**.  
- Idle is fine: empty open queue + no weekly pack due → log and exit without empty commit.

## State files (read every tick)

| File | Role |
|------|------|
| `data/loop_state.csv` | Cursor / mode |
| `data/ingest_queue.csv` | Unscored candidates |
| `data/proposals.csv` | Master scores |
| `data/sources.csv` | Provenance |
| `loop_log.md` | Append-only diary |
| `public/*` | Showcase (refresh when scores change) |

## Priority (pick first match)

1. `ingest_queue` status=`in_progress` (finish)  
2. `proposals` with blank scores / `analysis_version` bump requested in notes  
3. `ingest_queue` status=`open` highest `priority` then oldest  
4. If Monday/Friday and weekly pack stale → unit = `weekly_pack`  
5. Opportunistic: agent search for 1–3 new BE proposals if queue empty (seed only, do not full-score all)  
6. Else: mode=`idle`, exit  

## Tick steps (mandatory order)

### 1. Bootstrap

- Read `loop_state.csv`, queues.  
- If `paused=yes`: log idle, stop.  
- Append tick header to `loop_log.md` (ISO timestamp).

### 2. Select ONE primary unit

| Unit type | Done when |
|-----------|-----------|
| `ingest` | Candidate promoted or rejected; sources noted |
| `analyse` | Full memo + scores written; `proposals.csv` row complete |
| `rescore` | Version bumped + history row + memo delta |
| `weekly_pack` | `public/weekly_latest.md` refreshed |
| `seed_search` | 1–5 ingest rows from BE sources (no full scores) |

### 3. Gather (Belgium only)

- Prefer primary: bill text, government notice, budget annex.  
- Press OK to discover; not sole € source when avoidable.  
- Web search / open page allowed.  
- **Never invent amounts or poll numbers.**

### 4. Analyse (if unit = analyse / rescore)

1. Load **truth-policy** discipline + template `templates/analysis-memo.md`.  
2. Fill problem → mechanism → options A–F → evidence → distribution → fiscal → competence → recommendation → falsifier.  
3. Compute subscores + `clownpoints` + `genius_score` + `policy_index`.  
4. Steelman the proponent in writing.  
5. Set `score_confidence`; if only press paraphrase → max `weak`.  
6. `publish_ok=needs_human` until human has calibrated ~10 scores (then agents may set `yes` for medium+ confidence).  
7. Link `doge_item_ids` if relevant.

### 5. Write

- Update CSVs.  
- New source → `sources.csv`.  
- Memo → `analyses/{proposal_id}.md`.  
- If scores published tier: refresh leaderboard MD snippets.  
- Optional: seed DOGE `research_queue` if proposal implies large new opaque spend.

### 6. Close unit

- Update `loop_state.csv`: `last_tick_utc`, `last_unit_id`, `ticks_completed++`, counters.  
- Log 3–8 lines.

### 7. Commit and push (if files changed)

```text
git add docs/proposal-radar/ docs/09-proposal-radar.md   # as relevant
git commit -m "radar(loop): tick N — <unit_id> <summary>"
git push origin HEAD
```

No empty commits. On push failure: note in `loop_log.md`.

### 8. Stop

One unit or ~25 min. Do not score a whole news day in one fire.

## Weekly pack unit

When selected:

1. Rank publishable rows by clownpoints / genius / policy_index.  
2. Write `public/weekly_latest.md` + archive `public/weekly/YYYY-Www.md`.  
3. Refresh `public/leaderboard_clowns.md` and `public/leaderboard_genius.md` (top 15).  
4. Draft X thread bullets in weekly file (human posts).

## Modes

| Mode | Meaning |
|------|---------|
| `ingest` | Filling queue from feeds/search |
| `analyse` | Deep scoring |
| `weekly_pack` | Public pack |
| `idle` | Nothing open |
| `paused` | Human stop |

## Failure handling

| Problem | Action |
|---------|--------|
| Paywall | Use official primary; note press secondary |
| Only vague slogan | Reject noise or keep watch status; no clown theatre |
| Conflicting € | Range + confidence; both sources |
| Temptation to dunk on outgroup only | Force at least one same-bloc harsh score in weekly when data allows |

## Red lines (same as project)

- No FOI send without human.  
- No hate / violence.  
- No fake party registration claims.  
- Critique instruments and incentives.
