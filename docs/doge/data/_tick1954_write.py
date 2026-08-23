# tick 1954 — EURIDICE YE2025 Medium CW+Upswitch (rq_1954 after BRUGEL)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T13:20:00Z"
csv.field_size_limit(10**7)


def append_csv(path, rows):
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        for r in rows:
            w.writerow(r)


def update_csv_rows(path, key, updates_by_key):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        k = row[key]
        if k in updates_by_key:
            row.update(updates_by_key[k])
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


existing_src = set()
with (DATA / "sources.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_src.add(row.get("source_id") or "")

sources_new = [
    {
        "source_id": "src_euridice_jr2025_cw",
        "title": "Companyweb EURIDICE YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0455635823/european-underground-research-infrastructure-for-disposal-of-nuclear-waste-in-clay-environment",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1954; Laatste balansjaar 2025; neerlegging 24.03.2026; "
            "omzet 3391272 JUMP +6.13pct; bruto 3606 JUMP +114.9pct; FTE empty/0"
        ),
    },
    {
        "source_id": "src_euridice_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO EURIDICE YE2025 assets operating",
        "url": "https://www.upswitch.app/en/companies/be/euridice-0455635823",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1954; YE2025 revenue 3391272 / assets 1700427 DROP / operating result 35; "
            "YE2024 revenue 3195367 / assets 1933108 / operating 47; archive 2026-06-30; equity Unknown"
        ),
    },
    {
        "source_id": "src_euridice_kbo_1954",
        "title": "KBO EURIDICE 0455.635.823 Actief VOF pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455635823",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1954; Actief VOF sinds 12.12.2023; zetel Boeretang 190 2400 Mol; "
            "aanbestedende overheid; email info@euridice.be; NIRAS 0222.116.241 vaste vertegenwoordiger/"
            "dagelijks bestuur; NACE 38.320+72.109; NBB consult pointer"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

ent_notes = (
    "tick1954 YE2025 Medium CW+Upswitch KBO 0455.635.823 Actief VOF; "
    "omzet JUMP 3.39m bruto micro 3.6k operating 35 assets DROP 1.70m FTE 0; "
    "FOI gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5; NIRAS-managed Hadron/HADES dual; "
    "nuclear clay disposal R&D"
)

if "vof_euridice" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "vof_euridice",
                "name_nl": "EURIDICE",
                "name_fr": "EURIDICE",
                "name_en": "EURIDICE (European Underground Research Infrastructure for Disposal of Nuclear Waste in Clay Environment)",
                "level": "company",
                "parent_id": "niras",
                "community_language": "nl",
                "website": "https://www.euridice.be",
                "foi_email": "info@euridice.be",
                "foi_postal": "Boeretang 190 2400 Mol",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "vof_euridice": {
                "foi_email": "info@euridice.be",
                "foi_postal": "Boeretang 190 2400 Mol",
                "website": "https://www.euridice.be",
                "parent_id": "niras",
                "notes": ent_notes,
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_euridice_omzet_jr2025",
        "entity_id": "vof_euridice",
        "year": "2025",
        "amount_eur": "3391272",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet",
        "source_id": "src_euridice_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1954; YE2025 omzet 3391272 JUMP +6.13pct vs 3195367",
    },
    {
        "budget_id": "bud_euridice_bruto_jr2025",
        "entity_id": "vof_euridice",
        "year": "2025",
        "amount_eur": "3606",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived brutomarge",
        "source_id": "src_euridice_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1954; YE2025 bruto 3606 JUMP +114.9pct vs 1678; pass-through thin margin",
    },
    {
        "budget_id": "bud_euridice_operating_jr2025",
        "entity_id": "vof_euridice",
        "year": "2025",
        "amount_eur": "35",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB/CBSO operating result",
        "source_id": "src_euridice_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1954; YE2025 operating 35 vs YE2024 47; near-zero after 3.39m omzet",
    },
    {
        "budget_id": "bud_euridice_assets_jr2025",
        "entity_id": "vof_euridice",
        "year": "2025",
        "amount_eur": "1700427",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB/CBSO total assets",
        "source_id": "src_euridice_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1954; YE2025 assets 1700427 DROP vs YE2024 1933108",
    },
    {
        "budget_id": "bud_euridice_fte_jr2025",
        "entity_id": "vof_euridice",
        "year": "2025",
        "amount_eur": "0",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW/KBO FTE empty (0 reported)",
        "source_id": "src_euridice_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1954; YE2025 FTE empty/0; NIRAS/SCK path staffing off-books likely",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

existing_comm = set()
with (DATA / "commitments.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_comm.add(row.get("commitment_id") or "")

if "comm_euridice_jr2025_omzet" not in existing_comm:
    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_euridice_jr2025_omzet",
                "title": "EURIDICE YE2025 leftover nuclear clay R&D dual (omzet JUMP 3.39m / assets DROP 1.70m / FTE 0)",
                "entity_id": "vof_euridice",
                "beneficiary": "NIRAS / SCK CEN / nuclear waste R&D path (Hadron/HADES)",
                "legal_basis": "VOF; aanbestedende overheid; NBB neerlegging; openbaarheid",
                "decision_date": "2026-03-24",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": "3391272",
                "cash_by_year": (
                    "2025:omzet=3391272;bruto=3606;operating=35;assets=1700427;"
                    "equity=Unknown;fte=0;debt=Unknown"
                ),
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": "https://www.companyweb.be/nl/0455635823/european-underground-research-infrastructure-for-disposal-of-nuclear-waste-in-clay-environment",
                "stated_goal": "Underground clay nuclear-waste disposal research infrastructure",
                "cut_option": "FOI NBB PDF + equity/debt + NIRAS/SCK billing/staffing matrix",
                "source_id": "src_euridice_jr2025_cw",
                "confidence": "medium",
                "hierarchy_path": "Belgie>Federaal>Nucleair>EURIDICE>JR2025_L5",
                "notes": (
                    "tick1954; Medium CW+Upswitch YE2025; preferred AGB Bornem JR2024 / FARO YE2024 / "
                    "AIESH YE2024 / REW YE2024; do not redo Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/"
                    "NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/BRUGEL"
                ),
            }
        ],
    )

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

# priority_index = 0.55*5.0 + 0.35*4.0 + 0.10*(10-4.0) = 2.75+1.4+0.6 = 4.75 -> 4.8
if "lb_euridice_omzet_jump_3_39m_assets_drop_1_70m_fte0_jr2025" not in existing_lb:
    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_euridice_omzet_jump_3_39m_assets_drop_1_70m_fte0_jr2025",
                "name": "EURIDICE omzet JUMP 3.39m / assets DROP 1.70m / FTE 0 (NIRAS clay R&D VOF)",
                "level": "L5",
                "type": "nuclear_research_dual",
                "hierarchy_path": "Belgie>Federaal>Nucleair>EURIDICE>JR2025_L5",
                "annual_cost_eur": "3391272",
                "total_cost_eur": "3391272",
                "tco_notes": (
                    "omzet 3391272 JUMP +6.13pct bruto 3606 operating 35 assets 1700427 DROP "
                    "fte 0; equity/debt Unknown; NIRAS-managed VOF pass-through"
                ),
                "confidence": "medium",
                "source_id": "src_euridice_jr2025_cw",
                "beneficiaries": "NIRAS / SCK CEN / nuclear waste R&D path",
                "stated_goal": "Underground clay disposal research infrastructure",
                "measured_outcome": (
                    "CW+Upswitch YE2025 live; 3.39m omzet with micro bruto and ~0 operating; "
                    "FTE empty; primary NBB PDF + equity unresolved"
                ),
                "absurdity_score": "5.0",
                "cost_score": "4.0",
                "difficulty": "4.0",
                "priority_index": "4.8",
                "cut_proposal": "Publish NBB PDF + equity/debt + NIRAS/SCK billing and staffing matrix",
                "status": "active",
                "struck_reason": "",
                "notes": (
                    "tick1954; Medium CW+Upswitch; leftover after BRUGEL; deferred YE2025 unit; "
                    "not TE-additive pure-waste top10"
                ),
            }
        ],
    )

existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

if "gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5" not in existing_foi:
    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": "gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5",
                "hierarchy_path": "Belgie>Federaal>Nucleair>EURIDICE>nbb_pdf_equity_debt_L5",
                "entity_id": "vof_euridice",
                "what_is_missing": (
                    "NBB deposit PDF body for YE2025; equity/debt/cash recon to assets 1700427; "
                    "NIRAS/SCK CEN billing + staffing matrix explaining FTE 0 with omzet 3391272; "
                    "partner contribution split / pass-through contracts"
                ),
                "why_it_matters": (
                    "NIRAS-managed VOF with 3.39m omzet / micro bruto / ~0 operating / empty FTE — "
                    "pass-through and dual-count risk vs NIRAS/Belgoprocess perimeter needs statutory PDF"
                ),
                "priority": "8",
                "recipient_body": "EURIDICE VOF (cc NIRAS)",
                "recipient_email": "info@euridice.be",
                "recipient_postal": "Boeretang 190 2400 Mol (cc NIRAS Koning Albert II-laan 32 1000 Brussel)",
                "draft_letter_path": "docs/doge/foi/drafts/gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5.md",
                "status": "ready",
                "date_ready": "2026-08-23",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_euridice_jr2025_omzet",
                "linked_leaderboard_id": "lb_euridice_omzet_jump_3_39m_assets_drop_1_70m_fte0_jr2025",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1954; human-send only; Medium CW+Upswitch; next every-10 1960",
            }
        ],
    )

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_1954":
        row.update(
            {
                "status": "done",
                "entity_id": "vof_euridice",
                "title": "leftover dual hole-fill after BRUGEL — EURIDICE YE2025 Medium",
                "hierarchy_target": "Belgie>Federaal>Nucleair>EURIDICE>JR2025_L5",
                "instructions": (
                    "Completed: EURIDICE leftover nuclear clay R&D VOF after BRUGEL; "
                    "KBO 0455.635.823; YE2025 Medium Companyweb+Upswitch; sourced euros omzet 3391272 JUMP "
                    "bruto 3606 operating 35 assets 1700427 DROP FTE 0; FOI ready "
                    "gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5; NOT Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/"
                    "ETB/Elia/BNO/BRUGEL"
                ),
                "blocked_gap_id": "gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5",
                "updated_utc": TS,
                "notes": (
                    "tick1954 EURIDICE after BRUGEL; Medium CW+Upswitch omzet JUMP 3.39m assets DROP 1.70m "
                    "FTE 0; FOI ready not sent; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_1955; next every-10 1960"
                ),
            }
        )

with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

has_1955 = any(row["task_id"] == "rq_1955" for row in rows)
if not has_1955:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1955",
                "title": "leftover dual hole-fill after EURIDICE",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "Belgie>leftover_dual>AGB_APB_IOED_IGS",
                "entity_id": "",
                "instructions": (
                    "Tick 1955 after 1954 EURIDICE. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
                    "TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy. Do NOT redo "
                    "EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                    "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "spawned after tick1954; next every-10 1960",
            }
        ],
    )

draft = ROOT / "docs/doge/foi/drafts/gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5.md"
draft.write_text(
    """# FOI draft — EURIDICE (NBB PDF / equity-debt / NIRAS-SCK billing)

**gap_id:** `gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5`  
**status:** ready (NOT sent)  
**entity:** EURIDICE VOF — KBO **0455.635.823**  
**recipient:** info@euridice.be / Boeretang 190 2400 Mol / cc NIRAS  
**sources:** [Companyweb](https://www.companyweb.be/nl/0455635823/european-underground-research-infrastructure-for-disposal-of-nuclear-waste-in-clay-environment) · [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/euridice-0455635823) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455635823) · [euridice.be](https://www.euridice.be)  
**tick:** 1954 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW + Upswitch; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **24.03.2026**): omzet **EUR3,391,272** (**JUMP +6.13%**); bruto **EUR3,606**; operating **EUR35**; assets **EUR1,700,427** (**DROP** vs 1.93m); FTE **0/empty**; **equity/debt Unknown**.
- **Public dual:** NIRAS-managed VOF (KBO 0222.116.241 vaste vertegenwoordiger / dagelijks bestuur); clay nuclear-waste R&D (Hadron/HADES path with SCK CEN).
- Preferred leftover paths stalled: AGB Bornem **JR2024-only**; FARO/AIESH/REW **YE2024**. Do not redo BRUGEL / Hydria / Vivaqua / Belgoprocess / NIRAS / Bel V / Laborelec / CILE.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: EURIDICE VOF
t.a.v. openbaarheid / zaakvoerders
Boeretang 190
2400 Mol

cc: NIRAS/ONDRAF
Koning Albert II-laan 32
1000 Brussel

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
eigen vermogen/schulden en NIRAS/SCK-facturatie (KBO 0455.635.823)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF).
2. Eigen vermogen, schuldenrooster LT/ST en cash,
   reconcilieerbaar met assets EUR1.700.427.
3. Facturatie-/bijdragematrix NIRAS en SCK CEN 2025
   (pass-through vs eigen kosten) die omzet EUR3.391.272 verklaart.
4. Toelichting FTE 0 / empty bij omzet EUR3.391.272
   (gedetacheerd personeel / off-books staffing).
5. Actueel overzicht zaakvoerders / vaste vertegenwoordiger NIRAS
   en eventuele partnercontracten.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Draft complete
- [ ] Human review
- [ ] Human send (agent must NOT send)
- [ ] Track response in foi_queue.csv
""",
    encoding="utf-8",
)

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1954",
            "ticks_completed": "1954",
            "paused": "no",
            "notes": (
                "tick1954 leftover EURIDICE 0455.635.823 Medium CW (omzet JUMP 3.39m bruto 3.6k "
                "operating 35 assets DROP 1.70m FTE 0); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1955; next every-10 1960; continuous hole_fill"
            ),
        }
    )

log_path = ROOT / "docs/doge/loop_log.md"
log_block = """
## Tick 1954 - 2026-08-23T13:20:00Z - rq_1954 EURIDICE (omzet JUMP 3.39m / assets DROP 1.70m / Medium)

- Unit: **rq_1954** leftover dual after concurrent **rq_1953 BRUGEL** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (filed 17.07.2025); REW still **YE2024**. Took deferred leftover **EURIDICE VOF** (KBO **0455.635.823**; Boeretang 190 Mol; NIRAS-managed clay nuclear-waste R&D; YE2025 live CW). Do not redo BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO.
- Primary hunt: NBB deposit PDF unresolved (consult SPA). **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0455635823/european-underground-research-infrastructure-for-disposal-of-nuclear-waste-in-clay-environment) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/euridice-0455635823) + Strong KBO (neerlegging **24.03.2026**; YE **31.12.2025**): omzet **EUR3,391,272** (**JUMP +6.13%**); bruto **EUR3,606**; operating **EUR35**; assets **EUR1,700,427** (**DROP**); FTE **0**; equity/debt **Unknown**.
- Wrote: sources (+3); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vof_euridice); foi + draft gap_euridice_nbb_pdf_equity_debt_niras_sck_billing_l5; rq_1954=done + rq_1955 open; loop_state ticks=1954.
- FOI opened: NBB PDF + equity/debt + NIRAS/SCK billing/staffing (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1955 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1954 write OK")
