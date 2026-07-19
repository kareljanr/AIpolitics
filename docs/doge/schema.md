# DOGE data schema

All tables live under `docs/doge/data/` as CSV (UTF-8, header row).  
IDs: `snake_case`, stable, never reuse.

## entities.csv

| Column | Type | Notes |
|--------|------|-------|
| entity_id | string | PK |
| name_nl | string | |
| name_fr | string | optional |
| name_en | string | optional |
| level | enum | `l0_general` `l1_sector` `federal` `social_security` `community` `region` `province` `local` `parastatal` `eu` `other` |
| parent_id | string | FK entities |
| community_language | enum | `nl` `fr` `de` `bi` `na` |
| website | string | URL |
| foi_email | string | openbaarheid contact if known |
| foi_postal | string | |
| notes | string | |

## budgets.csv

| Column | Type | Notes |
|--------|------|-------|
| budget_id | string | PK |
| entity_id | string | FK |
| year | int | |
| amount_eur | number | blank if unknown |
| amount_min_eur | number | optional range |
| amount_max_eur | number | |
| basis | enum | `budgeted` `executed` `esa` `estimate` |
| source_id | string | FK sources |
| confidence | enum | `strong` `medium` `weak` `speculative` |
| notes | string | |

## programmes.csv

| Column | Type | Notes |
|--------|------|-------|
| programme_id | string | PK |
| entity_id | string | FK |
| parent_programme_id | string | optional tree |
| code | string | official budget code if any |
| name | string | |
| cofog | string | optional |
| year | int | |
| amount_eur | number | |
| source_id | string | |
| confidence | enum | |
| hierarchy_path | string | e.g. Flanders>Dept Cultuur>… |
| notes | string | |

## flows.csv

Single-year money movement (can link to multi-year).

| Column | Type | Notes |
|--------|------|-------|
| flow_id | string | PK |
| year | int | |
| amount_eur | number | |
| flow_type | enum | `grant` `procurement` `personnel` `ops` `transfer` `tax_expenditure` `guarantee` `in_kind` `other` |
| from_entity_id | string | |
| to_name | string | beneficiary label |
| programme_id | string | |
| commitment_id | string | if multi-year slice |
| source_id | string | |
| confidence | enum | |
| double_count_risk | enum | `none` `possible` `likely` |
| attribution_key | string | shared key for same euro |
| notes | string | |

## commitments.csv

Multi-year subsidies / contracts / envelopes.

| Column | Type | Notes |
|--------|------|-------|
| commitment_id | string | PK |
| title | string | |
| entity_id | string | granting body |
| beneficiary | string | |
| legal_basis | string | |
| decision_date | date | ISO |
| start_year | int | |
| end_year | int | |
| total_envelope_eur | number | |
| cash_y1_eur … or cash_json | string | prefer `cash_by_year` JSON `{"2024":100000}` |
| remaining_eur | number | |
| status | enum | `planned` `active` `ended` `renewed` `unknown` |
| evaluation_url | string | |
| stated_goal | string | |
| cut_option | string | |
| source_id | string | |
| confidence | enum | |
| hierarchy_path | string | |
| notes | string | |

## tax_expenditures.csv

| Column | Type | Notes |
|--------|------|-------|
| taxex_id | string | PK |
| name | string | |
| level | string | federal/regional |
| year | int | |
| amount_eur | number | |
| tax_type | string | PIT/CIT/VAT/… |
| source_id | string | |
| confidence | enum | |
| absurdity_seed | int | 1–10 optional |
| notes | string | |

## overhead_nodes.csv

| Column | Type | Notes |
|--------|------|-------|
| overhead_id | string | PK |
| name | string | |
| kind | enum | `cabinet` `dual_structure` `advice_body` `platform` `intercommunale` `other` |
| entity_ids | string | pipe-separated |
| estimated_cost_eur | number | |
| cost_year | int | |
| confidence | enum | |
| source_id | string | |
| notes | string | |

## leaderboard.csv

| Column | Type | Notes |
|--------|------|-------|
| item_id | string | PK |
| name | string | |
| level | string | |
| type | string | |
| hierarchy_path | string | L2>…>L5 |
| annual_cost_eur | number | run-rate |
| total_cost_eur | number | multi-year TCO if known |
| tco_notes | string | |
| confidence | enum | |
| source_id | string | |
| beneficiaries | string | |
| stated_goal | string | |
| measured_outcome | string | |
| absurdity_score | number | 1–10 |
| cost_score | number | 0–10 |
| difficulty | number | 1–10 |
| priority_index | number | computed |
| cut_proposal | string | |
| status | enum | `seed` `active` `struck` |
| struck_reason | string | |
| notes | string | |

## sources.csv

| Column | Type | Notes |
|--------|------|-------|
| source_id | string | PK |
| title | string | |
| url | string | |
| publisher | string | |
| accessed_date | date | ISO |
| source_class | string | nbb, fps, budget, audit, press, foi, … |
| notes | string | |

## research_queue.csv

| Column | Type | Notes |
|--------|------|-------|
| task_id | string | PK |
| title | string | |
| sprint | string | sprint1… or continuous |
| priority | int | 1–10 |
| status | enum | `open` `in_progress` `done` `blocked_foi` `cancelled` |
| hierarchy_target | string | |
| entity_id | string | |
| instructions | string | what to do |
| blocked_gap_id | string | FK foi if blocked |
| created_utc | string | |
| updated_utc | string | |
| notes | string | |

## foi_queue.csv

| Column | Type | Notes |
|--------|------|-------|
| gap_id | string | PK |
| hierarchy_path | string | |
| entity_id | string | |
| what_is_missing | string | |
| why_it_matters | string | |
| priority | int | 1–10 |
| recipient_body | string | |
| recipient_email | string | |
| recipient_postal | string | |
| draft_letter_path | string | relative path |
| status | enum | `draft` `ready` `sent` `waiting` `partial` `answered` `refused` `overdue` `appealed` `cancelled` |
| date_ready | date | |
| date_sent | date | |
| date_due | date | legal/custom |
| date_answered | date | |
| response_summary | string | |
| linked_commitment_id | string | |
| linked_leaderboard_id | string | |
| created_utc | string | |
| updated_utc | string | |
| notes | string | |

## loop_state.csv

Single logical row (or latest row wins).

| Column | Type | Notes |
|--------|------|-------|
| state_id | string | e.g. `main` |
| mode | string | see LOOP.md |
| current_sprint | string | |
| last_tick_utc | string | |
| last_unit_id | string | |
| ticks_completed | int | |
| paused | enum | `yes` `no` |
| notes | string | |
