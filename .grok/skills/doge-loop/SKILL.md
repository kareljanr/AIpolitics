---
name: doge-loop
description: >
  Run one DOGE Belgium research loop tick: advance spending/subsidy discovery,
  fill CSVs under docs/doge/data, open FOI queue rows for missing money flows,
  draft openbaarheid letters, then commit and push. Use when user says
  /doge-loop, "DOGE tick", "research loop", "find subsidies", or when a
  scheduled DOGE discovery task fires.
metadata:
  short-description: "One DOGE research loop tick + commit/push"
---

# DOGE loop tick

Work in the AIpolitics repo. Follow `docs/doge/LOOP.md` exactly.

## Do now

1. Read `docs/doge/data/loop_state.csv`, `research_queue.csv`, `foi_queue.csv`.  
2. If `paused=yes`, log idle and stop (no empty commit).  
3. Select **one** unit of work by LOOP.md priority.  
4. Use web/search/open tools to gather **primary** sources only.  
5. Update CSVs (sourced € only; Unknown OK).  
6. If info missing after honest search → add/update `foi_queue.csv` + draft `docs/doge/foi/drafts/{gap_id}.md` from `foi-template-nl.md`.  
7. Promote solid L5 waste to `leaderboard.csv` when justified.  
8. Append `docs/doge/loop_log.md`; update `loop_state.csv`.  
9. **Commit and push** (required when files changed):  
   - `git add` relevant paths  
   - `git commit -m "doge(loop): tick N — <unit> <summary>"`  
   - `git push origin HEAD`  
   - On push failure: note in `loop_log.md`; leave commit local  

## Hard rules

- **No invented euros.**  
- **Do not send** FOI emails/letters unless the user explicitly orders send for a `ready` gap.  
- Do not mark `sent` without human confirmation.  
- One primary unit per tick; time-box.  
- Prefer understatement; tag confidence.  
- Truth-policy: mechanisms over scapegoats.  
- Do **not** force-push or rewrite history.  

## Done criteria for this tick

Files on disk updated + log entry + **commit pushed** (or idle with no changes). Brief summary: unit, writes, FOI, commit SHA if any, next queue head.
