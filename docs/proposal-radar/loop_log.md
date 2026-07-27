# Proposal Radar loop log

Append-only. Newest ticks at bottom.

---

## 2026-07-27 â€” scaffold

- Created design `docs/09-proposal-radar.md`, schema, LOOP, skill, empty CSVs.
- Mode: idle. No proposals scored yet.

---

## 2026-07-27T12:30Z â€” tick 1 â€” calibration_batch_10 + RSS

### Unit
`calibration_batch_10` â€” full functionality online: RSS harvester, export, 10 live scores.

### Ingest
- Ran `rss_harvest.py` against 12 allowlisted feeds.
- Working feeds: VRT NWS (50), Knack (50), HLN (30). Several paywall/empty feeds noted.
- Enqueued 13 keyword hits; many false positives â†’ auto-rejected non-BE noise; filter tightened (BE signals + foreign hard block).
- Primary discovery for scoring also used: Belga Share VL ministerraad 17 Jul 2026, ING CoA note, FPB company-car paper, Arizona briefings, FWB budget press.

### Scored (10)

| ID | Clown | Genius | Index | Rec |
|----|-------|--------|-------|-----|
| prop_2022_smaakhaven_38m | 8.0 | 1.5 | âˆ’6.5 | reject |
| prop_2026_wk_veldrijden_ostend | 7.0 | 2.0 | âˆ’5.0 | reject |
| prop_2025_hybrid_car_rehab | 6.5 | 3.0 | âˆ’3.5 | reject |
| prop_2025_cgt_capital_gains | 4.5 | 4.0 | âˆ’0.5 | amend |
| prop_2026_vl_syntra_49m | 4.0 | 4.5 | +0.5 | watch |
| prop_2026_dolphin_ban_2036 | 3.5 | 3.5 | 0.0 | watch |
| prop_2026_fwb_budget_cuts_255m | 3.5 | 5.0 | +1.5 | amend |
| prop_2026_centenindex | 3.0 | 6.0 | +3.0 | amend |
| prop_2025_unemp_time_limit | 2.0 | 7.5 | +5.5 | support |
| prop_2021_company_car_ice_2026 | 1.5 | 7.0 | +5.5 | support |

### Writes
- `data/proposals.csv` (10 rows)
- `analyses/*.md` (10)
- `data/sources.csv`, `score_history.csv`, `loop_state.csv`
- `public/leaderboard_*.md`, `weekly_latest.md`
- Scripts: `rss_harvest.py`, `export_leaderboard.py`, `run_pipeline.py`, `seed_score_batch.py`, `config_feeds.json`

### Next
- Human review of scores/rubric calibration
- Fix empty RSS endpoints (De Tijd, news.belgium.be, RTBF)
- Optional durable schedule 6â€“24h for harvest-only ticks

---

## 2026-07-27 — rescore unit prop_2022_smaakhaven_38m v2

- Human feedback: clown 8 fair; analysis too short; fact-check ambition page.
- Scraped https://www.smaakhaven.be/nl/ambitie (+ tijdlijn, gebouw).
- Full steelman, claim-by-claim audit, ROI/break-even, options A–F, capture.
- **Scores unchanged** (8.0 / 1.5 / -6.5); analysis_version=2.
- Sources added: src_smaakhaven_ambitie, tijdlijn, gebouw.

---

## 2026-07-27 — all-10 deep v2 + taxpayer pain metrics

- Deep memos (Smaakhaven bar) for all 10 proposals; scores held.
- New doctrine TAXPAYER_UNIT.md: Belasting-FTE + Nettoloon-jaren (two different denominators).
- Unit: avg single FT employee labour tax ~€19.4k/yr; net ~€29.5k (Statbel gross + OECD TW 2025).
- Schema/template/skill/LOOP/export updated; future analyses must hit depth + pain.
- Pain filled where € known; blank for unquantified (UI, CGT, centenindex, hybrid delta).
