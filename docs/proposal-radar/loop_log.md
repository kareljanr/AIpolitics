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


---

## 2026-07-27 — daily scheduler armed

- Created durable Grok task **019fa3e112ab** interval **1d** (Proposal Radar).
- Fire: run_pipeline RSS when possible + one LOOP unit + commit/push.
- fire_immediately=false (first run after ~24h).
- Radar system already on main (Werkminuten + 10 v2 memos). This commit documents scheduler only.
- Pause: loop_state paused=yes and/or scheduler_delete 019fa3e112ab.


---

## 2026-07-27T18:09Z — tick analyse prop_2026_volvo_gent_119m

- Unit: full thorough+fair score of Volvo Car Gent up to €119m support (Flanders offer Jun + federal/Flanders MoU 15 Jul 2026).
- Sources: VRT, Volvo Car Gent MoU page, newmobility context (megacasting/Slovakia/history).
- Scores: clown 5.5 / genius 3.5 / index -2.0 / amend.
- Pain ceiling: 6134 Belasting-FTE / 4034 nettoloon-jaren / 50 werkminuten per employee.
- Not pure clown (real plant, conditionality); not genius (no structural fix; exit-threat aid; BE auto history).
- Commit radar paths only.



---

## 2026-07-28T14:30Z — tick 3 — analyse prop_2026_energy_commute_taxcredit_80m

### Unit
nalyse — federal energy support package (Apr 2026): temporary commute km tax credit + OCMW funds, EUR 80m / 3 months; ex-post take-up.

### Ingest
- Ran 
un_pipeline.py: 110 RSS entries, +6 enqueued (queue 19 total).
- Promoted ing_520ff7c6de -> scored.
- Rejected clear noise (lifestyle, gocarts, local fair noise, swim op-ed, Groen talking-point).

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 6.5 |
| genius_score | 3.0 |
| policy_index | -3.5 |
| recommendation | reject |
| pain (envelope 80m) | ~4124 Belasting-FTE / ~2712 nettoloon-jaren / ~34 werkminuten |

### Why
Real energy-price problem; instrument is temporary complex employer tax credit with pre-finance -> ~4% firm take-up (Attentia/SD Worx). Near-crisis for a dead letter. Pattern: do not recycle.

### Writes
- analyses/prop_2026_energy_commute_taxcredit_80m.md
- proposals.csv (+1), sources, score_history, ingest_queue, loop_state
- public leaderboards refreshed (12 publishable)

### Next queue head (open, priority)
1. ing_2e3d500c89 — Jambon fraudeplan delayed (EUR 300m revenue claim) prio 7
2. ing_9298c20c68 — Van Bossuyt voluntary return premium prio 7
3. ing_5541d28301 / ing_e9d812276c — admin lasagne / doofpotdecreet prio 6

Scheduler 019fa3e112ab still daily.


---

## 2026-07-29T14:30Z — tick 4 — analyse prop_2026_jambon_antifraud_300m

### Unit
nalyse — federal antifraud revenue path (EUR 300m/2026, >1.2bn legislature, 300 investigators); plan delayed.

### Ingest
- Ran 
un_pipeline.py: 110 RSS entries, +7 enqueued (4 dupes).
- Promoted ing_2e3d500c89 -> scored.
- Rejected noise (non-BE robots, FR wildfire dups, local swim ban, personality profile).

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 6.0 |
| genius_score | 4.0 |
| policy_index | -2.0 |
| recommendation | amend |
| pain | blank (unverified revenue claim) |

### Why
Right problem (tax gap); wrong packaging: book 300m while comprehensive plan delayed, IF doubted draft yield, BBI yield press-down. Hard amend: fund capacity + unbook fantasy until lawed.

### Writes
- analyses/prop_2026_jambon_antifraud_300m.md
- proposals.csv (+1 to 13), sources, score_history, ingest, loop_state
- public leaderboards refreshed

### Next queue head (open, priority)
1. ing_9298c20c68 — Van Bossuyt voluntary return premium prio 7
2. ing_5541d28301 — administrative lasagne op-ed prio 6
3. ing_e9d812276c — doofpotdecreet prio 6
4. ing_d2bf2bb637 — De Ridder IF advices prio 6 (possible DOGE-adjacent)

Scheduler 019fa3e112ab still daily.


---

## 2026-07-30T14:30Z — tick 5 — analyse prop_2026_vanbossuyt_return_reintegration

### Unit
nalyse — Fedasil/Van Bossuyt 2026 degressive voluntary-return reintegration reform (Syria priority; cut Brazil/Moldova/Balkan support).

### Ingest
- Ran 
un_pipeline.py: 110 entries, +2 enqueued (5 dupes).
- Promoted ing_9298c20c68 -> scored.
- Rejected noise (travel tips, local shop hours, De Lijn ops note).

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 3.0 |
| genius_score | 6.5 |
| policy_index | +3.5 |
| recommendation | support |
| pain | blank aggregate (unit ~5k; EU co-finance) |

### Why
Mechanism-aware: earlier exit = higher top-up; stop paying reintegration to visa-free misuse destinations; primary Fedasil PDF. Residual: elasticity and deadweight unproven.

### Writes
- analyses/prop_2026_vanbossuyt_return_reintegration.md
- proposals (+1 = 14), sources, history, ingest, state, leaderboards

### Next queue head
1. ing_5541d28301 — admin lasagne prio 6
2. ing_e9d812276c — doofpotdecreet prio 6
3. ing_d2bf2bb637 — De Ridder IF advices / secret dadies prio 6
4. ing_ddd0a86892 — Free-Time vzw subsidies prio 6 (DOGE-adjacent)

Scheduler 019fa3e112ab still daily.


---

## 2026-07-31T14:30Z — tick 6 — analyse prop_2026_vl_klokkenluiders_bestuursdecreet

### Unit
nalyse — Flanders Bestuursdecreet whistleblower reform (Crevits); critics: doofpotdecreet.

### Ingest
- Ran 
un_pipeline.py: 110 entries, +4 enqueued.
- Promoted ing_e9d812276c -> scored.
- Rejected: schenkingen 700m outturn (not proposal), Ceuta Spain, Woningfonds explainer.

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 4.5 |
| genius_score | 5.5 |
| policy_index | +1.0 |
| recommendation | amend |
| pain | blank (budget-neutral claim) |

### Why
Primary VR nota: channel simplify + Ombuds support + criminal sanctions + GO!/Xperta scope is solid admin. Amend: ring-fence openbaarheid so confidentiality protects identity not wrongdoing facts.

### Next queue head
1. ing_5541d28301 — admin lasagne prio 6
2. ing_d2bf2bb637 — De Ridder IF dading prio 6
3. ing_ddd0a86892 — Free-Time vzw 229k (DOGE-adjacent)
4. ing_ba222759d0 — Brussels deelfietsen
5. ing_5d2990aa80 — warmtenetten op-ed

Note: Friday — weekly_pack still optional next if queue thin; weekly_latest was regenerated by export today.

Scheduler 019fa3e112ab still daily.


---

## 2026-08-01T14:30Z — tick 7 — analyse prop_2026_regeringsdienst_beleidscordinatie

### Unit
nalyse — federal Regeringsdienst voor Beleidscoordinatie (admin lasagne / super-cabinet).

### Ingest
- Ran 
un_pipeline.py: 110 entries, +5 enqueued.
- Promoted ing_5541d28301 -> scored.
- Rejected noise (local police, swans, human interest, dup EU letter).

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 7.0 |
| genius_score | 2.5 |
| policy_index | -4.5 |
| recommendation | reject |
| pain | blank (no FTE/euro table) |

### Why
Coordination problem real; instrument is new layer + cabinet profiles + dual FODs while selling saneren. Reject unless net-zero FTE sunset delivery unit.

### Next queue head
1. ing_d2bf2bb637 — De Ridder IF dading prio 6
2. ing_ddd0a86892 — Free-Time vzw 229k (DOGE-adjacent)
3. ing_ba222759d0 — Brussels e-bikes
4. ing_5d2990aa80 — warmtenetten
5. ing_e48f01c225 — De Wever+21 premiers EU migration letter

Scheduler 019fa3e112ab still daily.


---

## 2026-08-02T14:30Z — tick 8 — analyse prop_2026_de_ridder_egis_luchthaven_dading

### Unit
nalyse — Flanders-Egis secret dading Deurne/Ostend airports; IF 3x negative; subsidies to 2039.

### Ingest
- Ran 
un_pipeline.py: 110 entries, +2 enqueued.
- Promoted ing_d2bf2bb637 -> scored.
- Rejected local noise (Londerzeel, Pepingen).

### Scores
| Field | Value |
|-------|------:|
| clownpoints | 7.5 |
| genius_score | 2.0 |
| policy_index | -5.5 |
| recommendation | reject |
| pain (12.1m forgone claim) | ~624 Belasting-FTE / ~410 nettoloon-jaren / ~5.1 werkminuten |

### Why
Litigation steelman real; secret mutual wipe + triple IF no + 2039 lock is fiscal-governance clown. Related 96m envelope disputed separately.

### Next queue head
1. ing_ddd0a86892 — Free-Time vzw 229k (DOGE-adjacent)
2. ing_ba222759d0 — Brussels e-bikes
3. ing_5d2990aa80 — warmtenetten
4. ing_e48f01c225 — De Wever+21 EU migration letter

Scheduler 019fa3e112ab still daily.
## 2026-10-13T23:10:25Z — tick 9 — analyse prop_2026_de_wever_btw_hervorming
- Scored ing_3db59e7ee9 as prop_2026_de_wever_btw_hervorming (federal VAT reform; Belgium; press-only).
- Scores: clown 4.0, genius 5.2, policy_index +1.2, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain left blank: Nieuwsblad €4.5bn is a gross yield partly pledged to tax cuts and investment, so it is not a labour-tax FTE basis; recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=9, proposals_scored=18, last_unit_id=prop_2026_de_wever_btw_hervorming, paused=no. No commit.
## 2026-10-13T23:23:57Z — tick 10 — analyse prop_2026_vrt_extra_besparing
- Scored ing_fbdeaeca8e as prop_2026_vrt_extra_besparing (Flanders VRT extra saving; Belgium; press-only).
- Scores: clown 3.5, genius 5.4, policy_index +1.9, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: 2029 annual range €7m–€10m, midpoint −€8.5m saving; Belasting-FTE −438.1; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=10, proposals_scored=19, last_unit_id=prop_2026_vrt_extra_besparing, paused=no. No commit.
## 2026-10-15T17:33:25Z — tick 11 — analyse prop_2026_gent_topevenement_1m
- Scored ing_a90a04d543 as prop_2026_gent_topevenement_1m (Ghent one-off €1m flagship cultural event in 2029; Belgium; local).
- Scores: clown 6.0, genius 3.0, policy_index -3.0, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain basis is the stated €1,000,000 one-off, not the unlabelled MJP feasts-service spike; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=11, proposals_scored=20, last_unit_id=prop_2026_gent_topevenement_1m, paused=no. No commit.
## 2026-10-15T21:57:17Z — tick 12 — analyse prop_2026_vl_finocas_pause_317m
- Scored ing_09ce734f50 as prop_2026_vl_finocas_pause_317m (Flanders pauses Finocas capital calls for ArcelorMittal Gent; Belgium; press plus parliamentary answer).
- Scores: clown 3.5, genius 5.6, policy_index +2.1, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: paused envelope EUR 317.5m, fiscal_is_saving yes; Belasting-FTE -16366.0; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=12, proposals_scored=21, last_unit_id=prop_2026_vl_finocas_pause_317m, paused=no. No commit.
## 2026-10-15T22:08:24Z — tick 13 — analyse prop_2026_acv_gesloten_centra_pakket
- Scored ing_342913aad7 as prop_2026_acv_gesloten_centra_pakket (ACV closed-centre package: staff floor, profile cap, risk premiums; Belgium; federal).
- Scores: clown 4.5, genius 4.1, policy_index -0.4, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain left blank: no public euro amount; minister headcount claim is not a euro basis; recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=13, proposals_scored=22, last_unit_id=prop_2026_acv_gesloten_centra_pakket, paused=no. No commit.
## 2026-10-25T21:13:36Z — tick 14 — analyse prop_2026_gent_opex_150m
- Scored ing_a43e945d16 as prop_2026_gent_opex_150m (Ghent operating-search ceiling and investment haircut; Belgium; local).
- Scores: clown 4.0, genius 5.6, policy_index +1.6, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: annual ceiling EUR 150m, fiscal_is_saving yes; EUR 400m 2027-2038 envelope excluded from the pain basis; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=14, proposals_scored=23, last_unit_id=prop_2026_gent_opex_150m, paused=no. No commit.
## 2026-10-25T21:24:13Z — tick 15 — analyse prop_2026_de_lijn_uitbreiding_half
- Scored ing_fe0a1ae991 as prop_2026_de_lijn_uitbreiding_half (Flanders De Lijn 2027 expansion euro halved to EUR 25m for the operating gap; Belgium).
- Scores: clown 4.5, genius 4.0, policy_index -0.5, recommendation amend, score_confidence medium, publish_ok yes.
- Pain: 2027 foregone EUR 25m versus the coalition expansion line, fiscal_is_saving yes; Belasting-FTE -1288.7; residual EUR 25m gap-fill excluded; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=15, proposals_scored=24, last_unit_id=prop_2026_de_lijn_uitbreiding_half, paused=no. No commit.
## 2026-10-25T21:27:57Z — tick 16 — reject ing_0a18647698
- Unit ing_0a18647698 is a Knack/L'Echo opinion column by Toon Van Overbeke (Vrijdaggroep), not a Belgian policy proposal.
- Public text diagnoses fiscally favoured robotics investment and says reform the tax system, with a glance at South Korea; no bill, rate, envelope or euro. Paywalled body not used. Not scored.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=16, proposals_scored=24 unchanged, last_unit_id=ing_0a18647698, paused=no. No commit.
## 2026-10-29T23:06:20Z — tick 17 — analyse prop_2026_bru_hotspot_politiebesluit
- Scored ing_9c3812b222 as prop_2026_bru_hotspot_politiebesluit (Brussels one-year police order: e-scooter ban in 19 drug hotspots; Belgium; press-only).
- Scores: clown 5.5, genius 3.85, policy_index -1.65, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain left blank: no public euro amount on this order; a same-week commissioner figure is a different instrument; recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=17, proposals_scored=25, last_unit_id=ing_9c3812b222, paused=no. No commit.
## 2026-10-29T23:09:39Z — tick 18 — reject ing_c7bdc81abd
- Unit ing_c7bdc81abd is a Knack reaction piece on the Brussels hotspot e-scooter ban, not a new Belgian policy proposal.
- Public excerpt: Dilliès (MR) bans e-steps in 19 drug hotspots; criminologist Mattias De Backer calls that order incredibly disproportionate and says it widens the gap between police and young people. Headline quote is criticism, not an instrument. Paywalled body not used. Same order already scored as prop_2026_bru_hotspot_politiebesluit.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=18, proposals_scored=25 unchanged, last_unit_id=ing_c7bdc81abd, paused=no. No commit.
## 2026-10-29T23:13:50Z — tick 19 — reject ing_f1be4352f9
- Unit ing_f1be4352f9 is an HLN clarification by Caroline Gennez (Vooruit), not a new Belgian policy proposal.
- RSS text: after the disability-sector reform, people can still use their persoonsvolgend budget for personal transport, service vouchers, family care and home care. That restates surviving uses of an already decided instrument. Paywalled HLN body not used. No new bill, envelope or euro.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=19, proposals_scored=25 unchanged, last_unit_id=ing_f1be4352f9, paused=no. No commit.
## 2026-10-30T22:44:39Z — tick 20 — analyse prop_2026_de_lovie_469m
- Scored ing_4f57158b8e as prop_2026_de_lovie_469m (Flemish €4.69 million heritage premium for Kasteel De Lovie in Poperinge; Belgium).
- Scores: clown 4.5, genius 4.35, policy_index -0.15, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: multi-year envelope €4,690,000, fiscal_is_saving no; Belasting-FTE 241.8; Werkminuten 1.98; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=20, proposals_scored=26, last_unit_id=ing_4f57158b8e, paused=no. No commit.
## 2026-10-30T22:49:10Z — tick 21 — reject ing_12b73c476a
- Unit ing_12b73c476a is a Knack news item on the closed-centre strike, not a new Belgian policy proposal.
- Public excerpt (De Krantenkoppen, 13 Oct 2026): ACV says the minister offers solutions but nothing short-term; staff strike over aggression; Kelly De Wilde says the action continues Wednesday. Headline quote is a removal diagnosis, not an instrument. Paywalled Knack body not used. Same strike package already scored as prop_2026_acv_gesloten_centra_pakket.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=21, proposals_scored=26 unchanged, last_unit_id=ing_12b73c476a, paused=no. No commit.
## 2026-10-30T22:51:28Z — tick 22 — reject ing_17eb650774
- Unit ing_17eb650774 is an HLN opinion column (/opinie/) written as a State of the Union by premier Bart De Wever's cat Maximus, not a Belgian policy proposal.
- Public headline: the prime minister was not in the Chamber and "sent his cat"; "Tot u spreekt de kater van de eerste minister". RSS hit on begroting|premie. DPG consent wall; body not used. No bill, rate, envelope or euro.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=22, proposals_scored=26 unchanged, last_unit_id=ing_17eb650774, paused=no. No commit.
## 2026-10-31T21:51:25Z — tick 23 — reject ing_79e7348d6e
- Unit ing_79e7348d6e is a VRT/Belga report on one teacher's appeal against dismissal, not a Belgian policy proposal.
- Public text: Hadija Amajoud of Assenede appeals her dismissal by the province of East Flanders for wearing a headscarf; the religious-sign ban in provincial schools is already in force this school year; her lawyer asks the appeal chamber to annul the disciplinary measure. Individual procedure, no new bill, rate, envelope or euro.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=23, proposals_scored=26 unchanged, last_unit_id=ing_79e7348d6e, paused=no. No commit.
## 2026-10-31T21:53:09Z — tick 24 — reject ing_1e3391b8c5
- Unit ing_1e3391b8c5 is an HLN report on one teacher's appeal against dismissal, not a Belgian policy proposal.
- Public text (VRT NWS, De Standaard, GVA, 14 Oct 2026): Hadija Amajoud of Assenede appeals her dismissal by the province of East Flanders for wearing a headscarf; religious signs are already banned in provincial schools this school year; lawyer Timo Lehaen asks the Kamer van Beroep to annul the disciplinary measure. HLN body behind a DPG consent wall. Same story already rejected as ing_79e7348d6e. No new bill, rate, envelope or euro.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=24, proposals_scored=26 unchanged, last_unit_id=ing_1e3391b8c5, paused=no. No commit.
## 2026-10-31T22:04:41Z — tick 25 — analyse prop_2026_leuven_busstation_quickwins
- Scored ing_69ba9b95c7 as prop_2026_leuven_busstation_quickwins (Leuven and De Lijn autumn 2026 bus-station safety package: blue strip, rails, route shift off platform 1).
- Scores: clown 4.0, genius 5.15, policy_index +1.15, recommendation amend, score_confidence weak, publish_ok needs_human.
- No public euro amount. Pain columns blank. recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=25, proposals_scored=27, last_unit_id=ing_69ba9b95c7, paused=no. No commit.
## 2026-11-01T13:53:28Z — tick 26 — analyse prop_2026_de_wever_2027_pakket_3_4mrd
- Scored ing_4680f63da5 as prop_2026_de_wever_2027_pakket_3_4mrd (federal 2027 fallback freeze of €3–4bn, labelled schuldenrem; Belgium; press-only).
- Scores: clown 5.0, genius 3.55, policy_index -1.45, recommendation reject, score_confidence weak, publish_ok needs_human.
- Pain: 2027 package range €3bn–€4bn, midpoint −€3.5bn, fiscal_is_saving yes; Belasting-FTE -180412.4; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=26, proposals_scored=28, last_unit_id=ing_4680f63da5, paused=no. No commit.
## 2026-11-01T13:55:31Z — tick 27 — reject ing_dc1ed6f3f5
- Unit ing_dc1ed6f3f5 is a Knack live-blog headline, “Federale begroting: premier De Wever komt met nieuw voorstel”, not a new Belgian policy instrument.
- Same-day press (VRT 14 Oct 19:03, Nieuwsblad and De Standaard that evening) is the 2027-only pivot already scored as prop_2026_de_wever_2027_pakket_3_4mrd. Knack body not read (human verification). VAT withdrawal is not rescored.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=27, proposals_scored=28 unchanged, last_unit_id=ing_dc1ed6f3f5, paused=no. No commit.
## 2026-11-01T13:59:40Z — tick 28 — reject ing_1c54de0e7a
- Unit ing_1c54de0e7a is the VRT NWS piece “Waarom De Wevers voorstel voor een 'schuldenrem' nu al de wenkbrauwen doet fronsen” (15 Oct 2026), not a new Belgian policy instrument.
- The same URL is already source src_1c54de0e7a for prop_2026_de_wever_2027_pakket_3_4mrd (2027 fallback freeze of €3–4bn). No second score.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=28, proposals_scored=28 unchanged, last_unit_id=ing_1c54de0e7a, paused=no. No commit.
## 2026-11-01T22:27:57Z — tick 29 — analyse prop_2026_les_engages_kapitaalmenu
- Scored ing_ec6fc98a68 as prop_2026_les_engages_kapitaalmenu (Les Engagés November 2026 capital-tax menu in the federal budget talks; Belgium; press-only).
- Scores: clown 6.0, genius 2.60, policy_index -3.40, recommendation reject, score_confidence weak, publish_ok needs_human.
- Press states a political revenue floor of at least or more than €1bn. Periodicity and base are unstated, so no CSV static and no pain. recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=29, proposals_scored=29, last_unit_id=ing_ec6fc98a68, paused=no. No commit.
## 2026-11-01T22:31:47Z — tick 30 — reject ing_d9f22db1f1
- Unit ing_d9f22db1f1 is an HLN foreign-desk report that EU member states are still far from agreement on the multiannual budget, not a Belgian policy proposal.
- URL is /buitenland/, jurisdiction_guess=multi, queued 2026-10-15. Same-week coverage is the EU MFF 2028–2034 deadlock. DPG consent wall; body not used. No Belgian bill, rate, envelope or instrument.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=30, proposals_scored=29 unchanged, last_unit_id=ing_d9f22db1f1, paused=no. No commit.
## 2026-11-01T22:34:50Z — tick 31 — reject ing_747c33da98
- Unit ing_747c33da98 is a VRT NWS report on a symbolic heritage auction in the Ghent Boekentoren, not a Belgian policy proposal.
- Public text (15 Oct 2026): staff staged a playful sale of collection pieces that do not change owner, to protest Flemish culture cuts. A sector spokesperson says Ghent must save about €3.5 million a year. That figure paraphrases cuts already announced; this item has no new bill, rate or envelope.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=31, proposals_scored=29 unchanged, last_unit_id=ing_747c33da98, paused=no. No commit.
## 2026-11-04T23:55:48Z — tick 32 — reject ing_453ea045b7
- Unit ing_453ea045b7 is a Knack process story on the Arizona budget deadlock, not a Belgian policy proposal.
- Public RSS text (3 Nov 2026): by offering his resignation to the king, Bart De Wever confirms the pistols are drawn; after Sunday evening's last meeting the vice-premiers still had no budget agreement. Cowboy headline is coalition infighting. Body behind human verification, not used. No bill, rate, envelope or new instrument.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=32, proposals_scored=29 unchanged, last_unit_id=ing_453ea045b7, paused=no. No commit.
## 2026-11-04T23:58:33Z — tick 33 — reject ing_0dd9767052
- Unit ing_0dd9767052 is an HLN opinion column on De Wever’s plan B, not a new Belgian policy proposal.
- Public headline (queued 15 Oct 2026, /opinie/): Timmie van Diepen says a schuldenrem is de facto a large index jump and asks how De Wever will convince Vooruit and CD&V. DPG consent wall; body not used. Same 2027 fallback of €3–4bn already scored as prop_2026_de_wever_2027_pakket_3_4mrd.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=33, proposals_scored=29 unchanged, last_unit_id=ing_0dd9767052, paused=no. No commit.
## 2026-11-05T00:00:28Z — tick 34 — reject ing_86f820c138
- Unit ing_86f820c138 is a VRT NWS foreign-desk report on violent protests in Albania, not a Belgian policy proposal.
- Public text (Kathleen Heylen, 16 Oct 2026): students and the flamingo movement demand the resignation of Albanian prime minister Edi Rama and education reforms; clashes in Tirana and other cities. Keyword hit was hervorming. No Belgian bill, rate, envelope or euro.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=34, proposals_scored=29 unchanged, last_unit_id=ing_86f820c138, paused=no. No commit.
## 2026-11-11T14:42:25Z — tick 35 — reject ing_fd664fba1e
- Unit ing_fd664fba1e is a Knack/Trends podcast promo (Tussen Wetstraat en Wall Street), not a Belgian policy proposal.
- Public show notes (Apple Podcasts, episode 77, published 6 Nov 2026): hosts Bert Bultinck and Jan De Meulemeester ask whether US midterm euphoria is justified and whether premier Bart De Wever can bridge the gap between new taxes and savings in the federal budget talks. Knack page hit a human-verification wall. No bill, rate, envelope or new instrument.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=35, proposals_scored=29 unchanged, last_unit_id=ing_fd664fba1e, paused=no. No commit.
## 2026-11-11T14:44:35Z — tick 36 — reject ing_5ed37af33b
- Unit ing_5ed37af33b is a VRT NWS foreign-desk report on a German child-pension deposit, not a Belgian policy proposal.
- Public text (Stefan Grommen, 16 Oct 2026, rubriek Buitenland/Duitsland): the Bundestag approved Friedrich Merz's Frühstart-Rente; the German state pays 10 euro a month from age 6 to 18 into a pension account for children living in Germany with a German tax ID. Costs cited are German (about 198 million euro in 2027). No Belgian bill, rate, envelope or actor.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=36, proposals_scored=29 unchanged, last_unit_id=ing_5ed37af33b, paused=no. No commit.
## 2026-11-11T14:57:46Z — tick 37 — analyse prop_2026_vl_bov_lov_stop
- Scored ing_3ceb74f61d as prop_2026_vl_bov_lov_stop: Gennez lets Bewegen op Verwijzing expire on 31 Dec 2026 and does not start Leefstijl op Verwijzing (Flanders). Knack body unread; instrument matched from the headline, the budget keyword and the 8 Oct 2026 decision.
- Scores: clown 4.5, genius 4.58, policy_index +0.08, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: annual saving €1,109,070–€1,620,000 (ministerial 2026 BOV budget to LOV call ceiling), midpoint −€1,364,535, fiscal_is_saving yes; recompute_pain.py run. Beneficiary €2.1m claim excluded.
- loop_state: mode=analyse, ticks_completed=37, proposals_scored=30, last_unit_id=ing_3ceb74f61d, paused=no. No commit.
## 2026-11-12T00:59:07Z — tick 38 — reject ing_852bf6f643
- Unit ing_852bf6f643 is a VRT NWS foreign-desk report on a Dutch budget fight, not a Belgian policy proposal.
- Public text (Jens Van Reet, 11 Nov 2026, rubriek Buitenland/Nederland): D66 and CDA agreed a tax package with PRO and Volt without VVD (higher rate on large investment income, worker-tax cut, exit levy). Belgium appears only as a comparison. No Belgian bill, rate, envelope or actor.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=38, proposals_scored=30 unchanged, last_unit_id=ing_852bf6f643, paused=no. No commit.
## 2026-11-12T01:08:05Z — tick 39 — analyse prop_2026_de_wever_10mrd_2029
- Scored ing_1e5815f534 as prop_2026_de_wever_10mrd_2029 (federal multi-year envelope of €10 billion by 2029; Belgium; press-only).
- Scores: clown 4.5, genius 3.70, policy_index -0.80, recommendation amend, score_confidence weak, publish_ok needs_human.
- Pain: path-to-2029 envelope €10 billion once, fiscal_is_saving yes; Belasting-FTE -515463.9; recompute_pain.py run.
- loop_state: mode=analyse, ticks_completed=39, proposals_scored=31, last_unit_id=ing_1e5815f534, paused=no. No commit.
## 2026-11-12T01:13:06Z — tick 40 — reject ing_013373a105
- Unit ing_013373a105 is a Knack opinion column by Jean-Marie Dedecker (LDD), not a Belgian policy proposal with an instrument.
- Public text (Wayback 20 Oct 2026 of the 18 Oct 2026 column): the state has “belastingsboulimie”; the obese government should take Ozempic; “scheiding van tafel en bed.” No bill, rate, or envelope he tables. The €10bn path is the government’s exercise, already scored as prop_2026_de_wever_10mrd_2029.
- ingest_queue status set to rejected_noise. No analysis memo, no proposals.csv row, recompute_pain.py not run.
- loop_state: mode=analyse, ticks_completed=40, proposals_scored=31 unchanged, last_unit_id=ing_013373a105, paused=no. No commit.
