---
name: proposal-radar
description: >
  Run one Proposal Radar tick: ingest or truth-score Belgian policy proposals
  (media + official), fill CSVs under docs/proposal-radar/data, write analysis
  memos with clownpoints/genius scores, refresh public leaderboards, then commit
  and push. Use when user says /proposal-radar, "clownpoints", "score this
  proposal", "Clowns & Genius", or when a scheduled proposal-radar task fires.
metadata:
  short-description: "Score Belgian policy proposals (clown→genius)"
---

# Proposal Radar tick

Work in the AIpolitics repo. Follow `docs/proposal-radar/LOOP.md` and doctrine in `docs/09-proposal-radar.md`.

Also apply **truth-policy** discipline (`.grok/skills/truth-policy/SKILL.md`) and the pipeline in `docs/04-policy-framework.md`.

## Do now

1. Read `docs/proposal-radar/data/loop_state.csv`, `ingest_queue.csv`, `proposals.csv`.  
2. If `paused=yes`, log idle and stop (no empty commit).  
3. Select **one** unit by LOOP.md priority (`ingest` | `analyse` | `rescore` | `weekly_pack` | `seed_search`).  
4. **Belgium only** (EU only if it binds BE law/cash).  
5. Prefer primary sources; never invent € or polls.  
6. If analysing: copy `templates/analysis-memo.md` → `analyses/{proposal_id}.md`; fill all steps including steelman, options A–F, falsifier.  
7. Write scores into `proposals.csv` (`clownpoints`, `genius_score`, `policy_index`, all subscores, `score_confidence`).  
8. Default `publish_ok=needs_human` until human calibrated ~10 diverse scores (see loop_state notes).  
9. Link DOGE IDs when the proposal creates/expands known waste.  
10. Append `loop_log.md`; update `loop_state.csv`.  
11. Refresh public MD if publishable scores changed.  
12. **Commit and push** when files changed:  
    - `git commit -m "radar(loop): tick N — <unit> <summary>"`  
    - `git push origin HEAD`  
    - On push failure: note in `loop_log.md`

## Scoring reminders

- `policy_index = genius_score − clownpoints`  
- Clownpoints score the **instrument**, not the person’s identity.  
- Same rubric for every party; **extensive** steelman + ambition/ROI fact-check (Smaakhaven v2 depth is the bar).  
- Weak evidence → low `score_confidence`, not fake precision.  
- “Do nothing / abolish” must appear in options.  
- **Taxpayer pain (mandatory):** when public € known, fill `pain_tax_fte` (Belasting-FTE) and `pain_net_years` (Nettoloon-jaren) per `docs/proposal-radar/TAXPAYER_UNIT.md`. Savings → negative. Never invent € for pain.

## Hard rules

- No FOI send unless user explicitly orders.  
- No hate content; critique incentives/institutions.  
- Do not claim the project is a registered party with seats.  
- One primary unit per tick.  
- Do not force-push.

## Done criteria

Files updated + log entry + commit pushed (or idle with no changes).  
Brief summary: unit, proposal_id if any, scores, commit SHA, next queue head.
