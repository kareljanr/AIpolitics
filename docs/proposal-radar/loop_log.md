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
