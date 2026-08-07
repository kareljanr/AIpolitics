# DOGE research loop

Recurring agent protocol. Goal: **each tick leaves the dataset richer** until **every material public euro is either accounted (sourced) or queued as FOI-ready**.

## Cadence

- **Orchestration:** Grok **durable scheduled task** (interval-based; there is no native “start next when previous finishes”).  
- **Target interval:** **60 seconds** (scheduler minimum). Prefer this over 15m while hole-filling.  
- **Not 30s:** platform min is **60s**.  
- **Overlap:** a tick often needs 2–15 min of tools. If the previous tick is still running, the next fire may start a **second concurrent agent** — accept for throughput, or raise interval to 2–3m if git thrash appears.  
- **Tick time budget:** still stop after **one primary unit** (don’t thrash 15 fronts in one fire).  
- Manual `/doge-loop` anytime is fine and does not wait for the timer.

## Anti-stuck (mandatory)

Agents and sessions hang. Treat that as normal; recover, do not idle.

- **No keep-alive / empty shell loops.** Never `sleep`, poll-wait, or run no-op shell just to “stay alive”.
- **One unit, then exit.** After CSV+log+commit+push (or honest FOI-block), **stop**. Do not open a second municipality “while you’re here”.
- **Hard wall ~12–15 min.** If PDF/OCR stalls: FOI-ready the gap, log, commit, exit. Partial primary fill beats a hung agent.
- **Git thrash:** if `git pull`/`push` conflicts with a concurrent tick, rebase/retry once or leave commit local + log — do not spin.
- **Huge CSVs:** do **not** load all of `research_queue.csv` into memory. Prefer `loop_state` next id, `rg`/line tools, or Python with raised `csv.field_size_limit` and early stop.
- **Scheduler drop:** if user says `paused=no` or “continue/retry” and no watcher exists → recreate durable 60s task with `fire_immediately`. Never assume the old task id still lives.
- **Try again:** a failed tick is not pause. Next fire (or manual `/doge-loop`) picks the same open unit or the next highest open. Only human `paused=yes` / `stop` cancels the watcher.

## Pause rule (strict)

- **Do not auto-pause** while open `research_queue` public work remains **or** new public fills can still reduce FOI opacity.  
- Prefer **hole-fill**: equality/HR bodies, dual structures, large FOI-adjacent programmes (NMBS, De Lijn, VDAB/FOREM), city/province L5 when new PDFs appear.  
- Pause only if `paused=yes` **by human** — or if truly nothing public left **and** all material gaps are already `foi_queue` status `ready`/`sent`/`answered` **and** human confirmed idle.  
- `idle_waiting_foi` is a **mode**, not automatic pause of the scheduler.

## Progress report (every 10 ticks)

When `ticks_completed` is a multiple of **10** (or human asks “progress / % / waste top”):

1. Update **`docs/doge/data/progress_every_10_ticks.md`** — layers A–E % of €347.956 bn TE (honest order-of-magnitude for L2/L5).  
2. Refresh **`docs/doge/data/doge_waste_top10_current.md`** — top **10** by `priority_index` + short high-absurdity list.  
3. Append 5–10 lines to `loop_log.md`.  
4. Commit: `doge(loop): tick N — progress coverage % + waste top10`.

Do **not** claim L5 near-complete of €348 bn. Taxex/FFS sit **off** the TE pie unless labelled.

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
**Sending, follow-ups, and response intake** are a separate human-gated pipeline: [`foi/SYSTEM.md`](foi/SYSTEM.md) + `scripts/foi_ops.py` + skill `/foi-ops`. Loop ticks still never send.

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
