"""Tick 112: rq_112 industrial reduced gas rate FFS multi-year + inland waterways."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T02:40:00Z"

with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_gas_reduced_t16,FFS 2026 Table16 aardgas verlaagd tarief multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"Table16: 1091/1031/1191/1295/1052/903 mEUR 2019-24; 13.54 TWh 2024; ~352 firms 2019 PQ; raw fps_ffs_2026_nl_full.pdf"\n'
    )

with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    gas = [
        (2019, 1091000000),
        (2020, 1031100000),
        (2021, 1190600000),
        (2022, 1295200000),
        (2023, 1052100000),
        (2024, 903000000),
    ]
    for y, a in gas:
        f.write(
            f"tx_ffs_gas_reduced_ind_{y},Natural gas reduced industrial rate FFS bench1,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_gas_reduced_t16,strong,7,"
            f'"Table16: {a/1e6:.1f} mEUR EBO/sector agreements class"\n'
        )
    gasolie = [
        (2019, 415600000),
        (2020, 383700000),
        (2021, 375000000),
        (2022, 412500000),
        (2023, 377100000),
        (2024, 365900000),
    ]
    for y, a in gasolie:
        f.write(
            f"tx_ffs_gasolie_indcom_{y},Gas oil industrial commercial use FFS,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_stookolie_t16,strong,6,"
            f'"Table16: {a/1e6:.1f} mEUR industrial/commercial gasoil"\n'
        )
    bv = [
        (2020, 84300000),
        (2021, 86100000),
        (2022, 90500000),
        (2023, 82700000),
        (2024, 84300000),
    ]
    for y, a in bv:
        f.write(
            f"tx_ffs_binnenvaart_{y},Inland waterway intermediate energy FFS,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_intermed_t19,strong,6,"
            f'"Table19: {a/1e6:.1f} mEUR"\n'
        )

new_cmts = [
    {
        "commitment_id": "cmt_gas_reduced_industrial_ebo",
        "title": "Industrial reduced natural gas excise rate (EBO/sector agreements)",
        "entity_id": "fod_finance",
        "beneficiary": "Firms with energy policy agreements / sectoral deals (~352 permits 2019)",
        "legal_basis": "Special excise tiers for EBO/sector agreement firms; energy contribution reduction",
        "decision_date": "2022-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "6565000000",
        "cash_by_year": (
            '{"2019":1091000000,"2020":1031100000,"2021":1190600000,"2022":1295200000,'
            '"2023":1052100000,"2024":903000000,"mwh_2024":13539664,"firms_2019_pq":352}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Industrial competitiveness + energy efficiency via EBO commitments",
        "cut_option": "NEKP continuous improvement; decouple support from fossil volume; phase reduced rate with EU level playing field",
        "source_id": "src_fps_ffs_2026_gas_reduced_t16",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>industrial_gas_reduced",
        "notes": (
            "tick112: FFS eval — sector agreement static efficiency vs reduced dynamic tax signal; "
            "dual-use/CHP fully exempt on top; NEKP 2025 continues refined EBO support with FFS phase-out language"
        ),
    },
    {
        "commitment_id": "cmt_binnenvaart_energy_ffs",
        "title": "Inland waterway fossil energy intermediate FFS",
        "entity_id": "fod_finance",
        "beneficiary": "Inland shipping operators",
        "legal_basis": "Excise exemptions intermediate consumption inland navigation",
        "decision_date": "2005-01-01",
        "start_year": "2020",
        "end_year": "2024",
        "total_envelope_eur": "427900000",
        "cash_by_year": (
            '{"2020":84300000,"2021":86100000,"2022":90500000,"2023":82700000,"2024":84300000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Modal shift / sector competitiveness",
        "cut_option": "Align with regional modal-shift goals without fossil price distortion; regional RA language noted in FFS",
        "source_id": "src_fps_ffs_2026_intermed_t19",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>binnenvaart",
        "notes": "tick112 Table19 stable ~84m; FFS cites VL/WAL RA modal ambitions as reform context",
    },
]

with (DATA / "commitments.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
ids = {x["commitment_id"] for x in rows}
for c in new_cmts:
    if c["commitment_id"] not in ids:
        rows.append({k: c.get(k, "") for k in fields})
with (DATA / "commitments.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("commitments", len(rows))

with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

if "lb_gas_reduced_industrial" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_gas_reduced_industrial",
            "name": "Industrial reduced natural gas excise (EBO)",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>industrial_gas_reduced",
            "annual_cost_eur": "903000000",
            "total_cost_eur": "6565000000",
            "tco_notes": "FFS 903m 2024; path 1091→1295 peak 2022→903; 13.54 TWh; ~352 firms 2019",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_gas_reduced_t16",
            "beneficiaries": "EBO/sector agreement energy-intensive firms",
            "stated_goal": "Competitiveness + efficiency agreements",
            "measured_outcome": "Static EBO targets vs weakened dynamic price signal; dual-use/CHP extra exemptions",
            "absurdity_score": "6",
            "cost_score": "8",
            "difficulty": "7",
            "priority_index": "6.9",
            "cut_proposal": "Tighten EBO additionality; phase reduced rate; EU level playing field; publish firm list L5",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick112; FOI candidate for firm-level EUR if not public",
        }
    )
    lb_rows.append(row)

if "lb_binnenvaart_ffs" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_binnenvaart_ffs",
            "name": "Inland waterway fossil energy FFS",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>binnenvaart",
            "annual_cost_eur": "84300000",
            "total_cost_eur": "421500000",
            "tco_notes": "FFS 84.3m 2024; path stable 84-91m 2020-24",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_intermed_t19",
            "beneficiaries": "Inland shipping",
            "stated_goal": "Modal shift / sector support",
            "measured_outcome": "FFS: decouple sector support from fuel use",
            "absurdity_score": "5",
            "cost_score": "4.5",
            "difficulty": "6",
            "priority_index": "4.85",
            "cut_proposal": "Fuel-neutral sector aid; green shipping incentives",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick112",
        }
    )
    lb_rows.append(row)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

# FOI for firm list if opaque - 352 firms mentioned but no public L5 EUR list
gap_id = "gap_fed_gas_reduced_firms"
draft = ROOT / "foi" / "drafts" / f"{gap_id}.md"
if not draft.exists():
    draft.write_text(
        f"""# FOI draft — {gap_id}

**Status:** ready for human send (fill requester identity first)  
**gap_id:** {gap_id}  
**Recipient:** FOD Financiën / IBZ openbaarheid  
**Form:** https://www.ibz.be/nl/openbaarheid-van-bestuur  

---

## Brief (NL)

```text
[NAAM]
[ADRES]
[E-MAIL]
[DATUM]

Aan: FOD Financiën — dienst openbaarheid van bestuur
(via IBZ-formulier of bevoegde informatieambtenaar)

Betreft: Openbaarmaking — verlaagd accijnstarief aardgas ondernemingen
(energiebeleidsovereenkomsten / sectorale overeenkomsten) 2022–2025
Intern: {gap_id}

Geachte,

Op grond van de wet van 11 april 1994 (openbaarheid van bestuur) vraag ik
openbaarmaking van:

1. Lijst van ondernemingen met vergunning/toepassing van het **verlaagd
   accijnstarief op aardgas** (verwarmingsbrandstof / EBO-sectorale regeling)
   voor de jaren **2022, 2023, 2024 en 2025**, met:
   - naam en KBO-nummer;
   - verbruik (MWh) aan verlaagd tarief indien bijgehouden;
   - geraamde of administratieve fiscale kost per dossier of aggregaat
     per schijf indien individuele kost niet beschikbaar.

2. Aantal vergunningen en totale MWh aan verlaagd tarief per jaar
   (FFS 2026 vermeldt 13.539.664 MWh in 2024; PQ 2019: 352 bedrijven).

3. Eventuele evaluatie- of NEKP-documenten die de voorzetting van deze
   regeling onderbouwen (titels + data).

Periode: 2022–2025.

Context: FFS-inventaris 2026 raamde de kost op ca. **€903 miljoen in 2024**
(pad 2019–2024: 1.091–1.295–903 m€). Individuele begunstigden zijn niet
publiek. Dit verzoek kadert in transparantieonderzoek naar publieke middelen.

Vorm: digitaal PDF/CSV naar [E-MAIL].

Identiteit: […]
Referentie: {gap_id}

Met vriendelijke groet,
[Naam]
```

**Niet verzonden door agent.**
""",
        encoding="utf-8",
    )

with (DATA / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    foi_fields = r.fieldnames
    foi_rows = list(r)
if not any(x["gap_id"] == gap_id for x in foi_rows):
    row = {k: "" for k in foi_fields}
    row.update(
        {
            "gap_id": gap_id,
            "hierarchy_path": "Federal>FFS>industrial_gas_reduced>firms_L5",
            "entity_id": "fod_finance",
            "what_is_missing": (
                "Named firms with reduced industrial gas excise permit MWh and EUR 2022-2025"
            ),
            "why_it_matters": "FFS 903m 2024; only count 352 firms 2019 public; L5 opacity",
            "priority": "7",
            "recipient_body": "FOD Financiën / IBZ FOI",
            "recipient_email": "",
            "recipient_postal": "https://www.ibz.be/nl/openbaarheid-van-bestuur",
            "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
            "status": "ready",
            "date_ready": "2026-07-27",
            "linked_commitment_id": "cmt_gas_reduced_industrial_ebo",
            "linked_leaderboard_id": "lb_gas_reduced_industrial",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "rq_112 draft ready human send only",
        }
    )
    foi_rows.append(row)
with (DATA / "foi_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=foi_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(foi_rows)

with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_112":
        row["status"] = "done"
        row["blocked_gap_id"] = gap_id
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick112: gas reduced 903m 2024 path from 1295 peak; 13.54 TWh; 352 firms 2019; "
            "binnenvaart 84m; FOI firm L5 ready"
        )
if not any(r["task_id"] == "rq_113" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_113",
            "title": "Natural gas product rate-diff FFS 4.09bn multi-year or social tariff path",
            "sprint": "continuous",
            "priority": "3",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "From FFS Table3: aardgas product differences 4089m 2024 path; or social tariff "
                "gas multi-year Table1. One unit only."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "Largest single FFS product-diff line after package totals",
        }
    )
with (DATA / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rq_rows)

with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "continuous",
            UTC,
            "rq_112",
            112,
            "no",
            "tick112 industrial gas reduced 903m. Next: rq_113 gas product-diff or rq_107 SWA; FOI firm list ready.",
        ]
    )

with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 112
- Unit: **rq_112** (Industrial reduced gas rate + inland waterways FFS)
- Found (strong FFS 2026 Table16/19 + §4.3.3):
  - **Aardgas verlaagd tarief** (EBO/sector agreements, bench1): **2019–24 €1,091 / 1,031 / 1,191 / 1,295 / 1,052 / 903 m**. Peak energy-crisis 2022; declining 2023–24.
  - **2024**: **13.54 TWh** declared at reduced rate; **~352 firms** with permit (PQ 2019).
  - FFS eval: sector agreements give static efficiency; reduced rate weakens dynamic price signal; dual-use + CHP full exemptions stack on top. NEKP 2025 continues refined EBO support with FFS phase-out language.
  - **Binnenvaart** intermediate: **€84.3m** 2024 (path 84–91m).
  - Gasolie industrial/commercial: **€365.9m** 2024 (path ~366–416m).
- Wrote: sources +1; taxex multi-year gas reduced + gasolie + binnenvaart; commitments +2; leaderboard +2; **FOI gap_fed_gas_reduced_firms ready**; rq_112=done; spawned **rq_113**; ticks=112
- FOI opened: **gap_fed_gas_reduced_firms** → ready (human send)
- Next: **rq_113** aardgas product-diff €4.09bn or low **rq_107** SWA
"""
    )
print("DONE tick112")
