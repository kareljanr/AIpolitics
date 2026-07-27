# Proposal Radar data schema

All tables under `docs/proposal-radar/data/` as CSV (UTF-8, header row).  
IDs: `snake_case`, stable, never reuse for a different instrument.

---

## proposals.csv

Master index. One row per distinct policy instrument (or child of a package).

| Column | Type | Notes |
|--------|------|-------|
| proposal_id | string | PK e.g. `prop_20260715_wassalon_pilot` |
| title | string | Neutral short title |
| title_nl | string | Public Dutch title optional |
| summary_one_line | string | Steelman one-liner |
| actor_name | string | Person or body proposing |
| actor_role | string | minister, party, government, mayor, MP, social_partner, other |
| party_or_coalition | string | e.g. Vooruit, N-VA, Arizona, city college |
| jurisdiction | enum | `federal` `flanders` `wallonia` `brussels` `fwb` `dg` `province` `local` `eu_binds_be` `multi` |
| competence_notes | string | Why this level |
| instrument_type | enum | `law` `decree` `subsidy` `tax` `ban` `obligation` `pilot` `agency` `envelope` `procurement` `soft_target` `package` `other` |
| status | enum | `rumoured` `announced` `tabled` `adopted` `implemented` `evaluated` `killed` `expired` |
| first_seen_date | date | ISO |
| decision_date | date | if known |
| stated_goal | string | Proponent’s goal in their words (short) |
| mechanism_tag | string | price_distortion, entry_barrier, transfer, symbolism, … |
| fiscal_static_min_eur | number | annual or envelope — see fiscal_basis |
| fiscal_static_max_eur | number | |
| fiscal_basis | enum | `annual` `multi_year_envelope` `one_off` `unknown` |
| fiscal_confidence | enum | `strong` `medium` `weak` `speculative` |
| fiscal_is_saving | enum | `yes` / `no` / blank — if yes, pain columns are **negative** (relief) |
| pain_basis_eur | number | signed mid € used for pain (cost + / saving −) |
| pain_tax_fte | number | **Belasting-FTE** = pain_basis ÷ employee labour tax/year (~€19.4k) |
| pain_net_years | number | **Nettoloon-jaren** = pain_basis ÷ net take-home/year (~€29.5k) |
| pain_eur_per_employee | number | pain_basis ÷ N Belgian employees (~4.85m) |
| pain_work_minutes | number | **Werkminuten** = (€/employee) ÷ (gross € per work-minute). Minutes each employee worked for this to exist |
| pain_note | string | unit version + caveats |
| clownpoints | number | 0–10 |
| genius_score | number | 0–10 |
| policy_index | number | genius − clownpoints |
| truth_problem | number | 0–10 subscore |
| mechanism_fit | number | 0–10 |
| abundance_ev | number | 0–10 |
| fiscal_honesty | number | 0–10 |
| incentive_quality | number | 0–10 |
| competence_fit | number | 0–10 |
| evidence_quality | number | 0–10 |
| capture_risk | number | 0–10 (higher = worse) |
| score_confidence | enum | `strong` `medium` `weak` `speculative` |
| analysis_version | int | starts 1; bump on re-score |
| analysis_path | string | e.g. `analyses/prop_….md` |
| primary_source_id | string | FK sources |
| doge_item_ids | string | pipe-separated leaderboard/commitment IDs |
| parent_proposal_id | string | if child of package |
| recommendation | enum | `support` `amend` `reject` `ignore` `watch` |
| falsifier | string | one sentence |
| publish_ok | enum | `yes` `no` `needs_human` | default `needs_human` until calibrated |
| created_utc | string | |
| updated_utc | string | |
| notes | string | |

---

## sources.csv

| Column | Type | Notes |
|--------|------|-------|
| source_id | string | PK |
| title | string | |
| url | string | |
| publisher | string | |
| accessed_date | date | ISO |
| source_class | enum | `primary_law` `gov_press` `parliament` `budget` `audit` `press` `party` `social_official` `think_tank` `other` |
| language | enum | `nl` `fr` `de` `en` |
| proposal_ids | string | pipe-separated |
| notes | string | |

---

## ingest_queue.csv

Candidates not yet fully scored.

| Column | Type | Notes |
|--------|------|-------|
| ingest_id | string | PK |
| title_hint | string | |
| url | string | |
| discovered_via | enum | `human` `agent_search` `rss` `parliament_watch` `x` `other` |
| jurisdiction_guess | string | |
| priority | int | 1–10 |
| status | enum | `open` `in_progress` `promoted` `rejected_noise` `duplicate` |
| proposal_id | string | set when promoted |
| created_utc | string | |
| updated_utc | string | |
| notes | string | |

---

## loop_state.csv

Single logical row (latest wins).

| Column | Type | Notes |
|--------|------|-------|
| state_id | string | `main` |
| mode | string | `ingest` `analyse` `weekly_pack` `idle` `paused` |
| last_tick_utc | string | |
| last_unit_id | string | |
| ticks_completed | int | |
| proposals_scored | int | |
| paused | enum | `yes` `no` |
| notes | string | |

---

## score_history.csv (optional but recommended)

Append-only re-score log.

| Column | Type | Notes |
|--------|------|-------|
| history_id | string | PK |
| proposal_id | string | FK |
| analysis_version | int | |
| clownpoints | number | |
| genius_score | number | |
| policy_index | number | |
| score_confidence | enum | |
| changed_reason | string | |
| recorded_utc | string | |

---

## Computed fields

```text
policy_index = genius_score - clownpoints
pain_tax_fte = pain_basis_eur / tax_rounded_eur
pain_net_years = pain_basis_eur / net_rounded_eur
pain_eur_per_employee = pain_basis_eur / employees_be
pain_work_minutes = pain_eur_per_employee / (gross_eur_year / work_minutes_year)
```

Full doctrine: [`TAXPAYER_UNIT.md`](TAXPAYER_UNIT.md).

Public sort:

- Clowns leaderboard: highest `clownpoints` then lowest `policy_index` among `score_confidence` ∈ {medium,strong} and `publish_ok=yes`
- Genius leaderboard: highest `genius_score` / `policy_index` same filter
