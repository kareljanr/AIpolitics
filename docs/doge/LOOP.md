# DOGE research loop

Recurring agent protocol. Goal: **each tick leaves the dataset richer** until public sources are exhausted and remaining gaps are only FOI-waiting.

## Cadence

- **Target:** every **30 minutes** while the project is in active discovery.  
- **Orchestration:** Grok scheduled task and/or manual `/doge-loop` run.  
- **Tick time budget:** ~10–20 minutes of tool work; then stop and log (don’t thrash).

## State files (read every tick)

| File | Role |
|------|------|
| `data/research_queue.csv` | What to investigate next |
| `data/foi_queue.csv` | Missing info → letters |
| `data/leaderboard.csv` | Public waste ranking |
| `data/commitments.csv` | Multi-year money |
| `data/entities.csv` | Institutional map |
| `data/sources.csv` | Provenance |
| `data/loop_state.csv` | Cursor / last tick / mode |
| `loop_log.md` | Append-only tick diary |

## Priority (pick first match)

1. `research_queue` status=`in_progress` (finish started work)  
2. `foi_queue` status=`draft` with priority≥8 (finish letter draft)  
3. `research_queue` status=`open` highest `priority` then oldest  
4. Sprint default from `loop_state.csv` → `current_sprint`  
5. If nothing public left: set mode=`idle_waiting_foi` and exit tick early  

## Tick steps (mandatory order)

### 1. Bootstrap

- `git pull` if in a git-capable agent environment (optional).  
- Read `loop_state.csv` and queues.  
- Append tick header to `loop_log.md` with ISO timestamp.

### 2. Select unit of work (ONE primary unit per tick)

Examples of a unit:

- Map one L1 sector total for one year  
- Open one budget PDF/XLSX and extract top 10 lines  
- Flesh one multi-year commitment  
- Draft one FOI letter for one gap  
- Promote one verified L5 to leaderboard  

### 3. Gather

- Prefer primary sources (budget, NBB, FPS, official portals).  
- Web search / open pages allowed.  
- **Never invent amounts.**

### 4. Write

- Update the relevant CSV row(s).  
- New source → `sources.csv`.  
- If amount or output still missing after honest search → **create/update `foi_queue` row** + draft letter under `foi/drafts/`.  
- If L5 solid (name + € range + source + absurdity note) → `leaderboard.csv`.

### 5. Close unit

- Research item → `done` or `blocked_foi` (if waiting on administration).  
- Update `loop_state.csv`: `last_tick_utc`, `last_unit_id`, `ticks_completed++`.  
- Log 3–8 lines: what found, what written, what’s next.

### 6. Commit and push (mandatory end of tick)

If the tick changed any files under the repo:

1. `git status` / `git diff` / `git log -3 --oneline`  
2. Stage relevant paths (usually `docs/doge/` and any docs touched).  
3. Commit with message: `doge(loop): tick N — <unit_id> <short summary>`  
4. `git push origin HEAD` (or current branch)  

If nothing changed (idle / paused): **do not** create an empty commit.  
If push fails (auth/network): log failure in `loop_log.md` and leave commit local.

### 7. Stop conditions for this tick

Stop after **one** primary unit **or** ~20 min, whichever first.  
Do not open 15 fronts in one tick.

## FOI behaviour inside the loop

| Allowed | Not allowed without human OK |
|---------|------------------------------|
| Detect gap | Sending email/post as if from the party |
| Fill `foi_queue` | Legal threats |
| Write draft letter from template | Publishing unverified fraud claims |
| Mark `ready` when draft complete | Marking `sent` unless human confirms |

When drafting FOI: use [`foi-template-nl.md`](foi-template-nl.md); save as `foi/drafts/{gap_id}.md`.

## Modes (`loop_state.csv` → `mode`)

| Mode | Meaning |
|------|---------|
| `sprint1_map` | L0–L1 big map |
| `sprint2_taxex` | Tax expenditures |
| `sprint3_flanders` | Flanders deep dive |
| `sprint4_federal` | Federal discretionary |
| `sprint5_local` | Cities |
| `sprint6_overhead` | Complexity tax |
| `l5_hunt` | Opportunistic L5 |
| `foi_backlog` | Clear draft/ready FOI queue |
| `idle_waiting_foi` | Only waiting on admins |
| `paused` | Human paused loop |

## Definition of “complete”

**Never absolute.** A coverage milestone is:

- L1 sectors have sourced totals for latest available year  
- Top N entities listed  
- Tax expenditure table seeded  
- ≥K leaderboard L5 rows with sources  
- Every high-€ Unknown has an FOI row  

Then continue forever at lower intensity (weekly is fine).

## Failure handling

| Problem | Action |
|---------|--------|
| Source 404 | Note in log; try archive; FOI if material |
| Conflicting figures | Keep both + confidence; prefer official |
| Agent hallucination risk | Prefer quote/table extract; leave Unknown |
| Empty queues | idle_waiting_foi or spawn new research from next sprint |

## Manual run

```text
/doge-loop
# or: open LOOP.md and execute one tick
```

## Scheduled run (Grok)

Prompt must instruct: work only in `C:\Users\karel\dev\AIpolitics` (or repo root), follow this file, one unit per tick, then **commit and push** changes to the remote (see §6).
