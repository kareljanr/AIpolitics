# tick 1959 — SPGE YE2025 Medium CW+Upswitch+KBO (rq_1959 after IRE FUP)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T16:00:00Z"
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
        "source_id": "src_spge_jr2025_cw",
        "title": "Companyweb SPGE YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0420651980/societe-publique-de-gestion-de-l-eau",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1959; Laatste balansjaar 2025; neergelegd 10-07-2026; "
            "omzet 450223607 JUMP +9.29pct; pnl JUMP 27301169 turnaround vs LOSS 8137478; "
            "equity 2141950395; bruto 147515571; FTE 65; Groot; KBO 0420.651.980"
        ),
    },
    {
        "source_id": "src_spge_jr2025_cw_en",
        "title": "Companyweb EN twin SPGE YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0420651980/societe-publique-de-gestion-de-l-eau",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1959; Last balance sheet year 2025; Turnover 450223607; "
            "Profit/Loss 27301169; Equity 2141950395; Gross margin 147515571; FTE 65"
        ),
    },
    {
        "source_id": "src_spge_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO SPGE YE2025 assets EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/societe-publique-de-gestion-de-l-eau-0420651980",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1959; YE31.12.2025; revenue 450223607; EBITDA 149189634; equity 2141950395; "
            "assets CONFLICT 3833590128 vs 4058962696 — FOI NBB PDF; not used as Strong"
        ),
    },
    {
        "source_id": "src_spge_kbo_1959",
        "title": "KBO SPGE 0420.651.980 Actief SA de droit public",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420651980",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1959; Actief NV/SA de droit public; zetel Rue des Ecoles 17-19 4800 Verviers; "
            "NACE 37.000 afvalwater; emails info@spge.be / sa@spge.be; aanbestedende overheid path"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1959 YE2025 Medium CW NL+EN + Upswitch + Strong KBO 0420.651.980 Actief SA droit public; "
    "omzet JUMP 450.22m pnl JUMP turnaround 27.30m equity 2.142bn bruto JUMP 147.52m "
    "EBITDA 149.19m FTE 65; assets Unknown (Upswitch conflict 3.834bn vs 4.059bn); debt Unknown; "
    "official RA site still 2024-only; FOI gap_spge_nbb_pdf_assets_debt_oaa_matrix_l5; "
    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; dual Aquafin VL; do not redo SWDE/Vivaqua/Hydria/CILE"
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "spge": {
            "notes": ent_notes,
            "foi_email": "info@spge.be",
            "foi_postal": "Rue des Ecoles 17-19 4800 Verviers",
            "website": "https://www.spge.be",
        },
    },
)

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_spge_omzet_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "450223607",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_spge_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1959; YE2025 omzet 450223607 JUMP +9.29pct vs 411939131",
    },
    {
        "budget_id": "bud_spge_pnl_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "27301169",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies",
        "source_id": "src_spge_jr2025_cw",
        "confidence": "medium",
        "notes": (
            "tick1959; YE2025 pnl JUMP 27301169 turnaround vs LOSS -8137478 YE2024"
        ),
    },
    {
        "budget_id": "bud_spge_bruto_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "147515571",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_spge_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1959; YE2025 bruto 147515571 JUMP +36.1pct vs 108361275",
    },
    {
        "budget_id": "bud_spge_equity_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "2141950395",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_spge_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1959; YE2025 equity 2141950395 JUMP +2.92pct vs 2081268063",
    },
    {
        "budget_id": "bud_spge_ebitda_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "149189634",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived EBITDA",
        "source_id": "src_spge_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1959; YE2025 EBITDA 149189634 (~33.1pct of omzet); FOI NBB PDF confirm",
    },
    {
        "budget_id": "bud_spge_fte_jr2025_statutory",
        "entity_id": "spge",
        "year": "2025",
        "amount_eur": "65",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_spge_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1959; YE2025 FTE 65 vs ~58 YE2024 class",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

existing_comm = set()
with (DATA / "commitments.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_comm.add(row.get("commitment_id") or "")

comm_row = {
    "commitment_id": "comm_spge_jr2025_statutory_omzet",
    "title": (
        "SPGE YE2025 leftover Walloon sanitation dual statutory "
        "(omzet JUMP 450.22m / pnl JUMP 27.30m / equity 2.142bn)"
    ),
    "entity_id": "spge",
    "beneficiary": "Walloon municipalities OAA / wastewater users / Aquafin dual path",
    "legal_basis": (
        "SA de droit public decret RW 15.04.1999; NBB neerlegging; "
        "decret wallon openbaarheid / Code de l Eau"
    ),
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2141950395",
    "cash_by_year": (
        "2025:omzet=450223607;bruto=147515571;pnl=27301169;"
        "equity=2141950395;ebitda=149189634;fte=65;assets=Unknown;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0420651980/societe-publique-de-gestion-de-l-eau",
    "stated_goal": "Finance and coordinate Walloon wastewater sanitation / catchment protection",
    "cut_option": "FOI NBB PDF + assets/debt + OAA transfer matrix + dual unit-cost Aquafin",
    "source_id": "src_spge_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Eau>SPGE>JR2025_statutory_L5",
    "notes": (
        "tick1959; Medium CW NL+EN+Upswitch after IRE FUP; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo SWDE/Vivaqua/Hydria/CILE/"
        "IRE/FANC/SCK/EURIDICE/BRUGEL/Belgoprocess; not TE-additive of 348bn"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_spge_omzet_jump_450_22m_pnl_jump_27_30m_jr2025",
    "name": (
        "SPGE omzet JUMP 450.22m / pnl JUMP turnaround 27.30m / equity 2.142bn "
        "(statutory YE2025)"
    ),
    "level": "L5",
    "type": "walloon_sanitation_finance_dual",
    "hierarchy_path": "Wallonie>Eau>SPGE>JR2025_statutory_L5",
    "annual_cost_eur": "450223607",
    "total_cost_eur": "2141950395",
    "tco_notes": (
        "statutory omzet 450223607 JUMP bruto 147515571 pnl JUMP 27301169 "
        "equity 2141950395 EBITDA 149189634 fte 65; assets/debt Unknown; "
        "dual Aquafin VL sanitation stack"
    ),
    "confidence": "medium",
    "source_id": "src_spge_jr2025_cw",
    "beneficiaries": "Walloon households / municipalities OAA / catchment protection",
    "stated_goal": "Finance wastewater sanitation and coordinate Walloon water sector",
    "measured_outcome": (
        "CW NL+EN YE2025 live after long 2024-only seed; turnover JUMP and LOSS-to-profit "
        "turnaround; primary NBB PDF + BS + OAA matrix unresolved; official RA still 2024"
    ),
    "absurdity_score": "4.0",
    "cost_score": "8.5",
    "difficulty": "4.0",
    "priority_index": "6.5",
    "cut_proposal": (
        "Publish NBB PDF + assets/debt + per-OAA transfer matrix + dual unit-cost vs Aquafin"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1959; Medium CW; leftover water dual after nuclear IRE cluster; "
        "not TE-additive pure-waste top10; refreshes 2024 CA 418m seed"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_spge_nbb_pdf_assets_debt_oaa_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>Eau>SPGE>nbb_pdf_assets_debt_oaa_L5",
    "entity_id": "spge",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (CW neerlegging 10.07.2026); "
        "assets / debt LT-ST / cash exact (Upswitch conflict 3.834bn vs 4.059bn); "
        "per-OAA / intercommunale transfer + CSU envelope matrix 2025; "
        "reconcile statutory omzet 450.22m vs prior RA2024 CA 418m class; "
        "official Rapport annuel 2025 + dual unit-cost vs Aquafin VL"
    ),
    "why_it_matters": (
        "Walloon public sanitation finance SA: omzet JUMP to 450.22m and pnl turnaround "
        "27.30m with only 65 FTE and 2.14bn equity — BS and OAA euro flows opaque vs Aquafin dual"
    ),
    "priority": "8",
    "recipient_body": "SPGE Societe publique de Gestion de l Eau (cc SPW Environnement)",
    "recipient_email": "info@spge.be",
    "recipient_postal": "Rue des Ecoles 17-19 4800 Verviers",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_spge_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_spge_omzet_jump_450_22m_pnl_jump_27_30m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1959; human-send only; Medium CW; next EVERY-10 required at 1960",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — SPGE (NBB PDF / assets-debt / OAA matrix)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** Société publique de Gestion de l'Eau (SPGE) — KBO **0420.651.980**  
**recipient:** info@spge.be / Rue des Ecoles 17-19 4800 Verviers / cc SPW Environnement  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0420651980/societe-publique-de-gestion-de-l-eau) · [Companyweb EN](https://www.companyweb.be/en/0420651980/societe-publique-de-gestion-de-l-eau) · [Upswitch](https://www.upswitch.app/en/companies/be/societe-publique-de-gestion-de-l-eau-0420651980) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420651980) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0420651980) · [spge.be](https://www.spge.be)  
**tick:** 1959 (NOT every-10; next tick **1960 MUST run EVERY-10** progress + waste top10)  
**confidence on table euros:** Medium (NBB-derived CW NL+EN + Upswitch EBITDA; primary deposit PDF unresolved; assets conflict)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **10.07.2026**): omzet **EUR450,223,607** (**JUMP +9.29%**); bruto **EUR147,515,571**; pnl **EUR27,301,169** (**JUMP turnaround** vs LOSS 8.14m); equity **EUR2,141,950,395**; EBITDA **EUR149,189,634**; FTE **65**.
- Assets **Unknown** (Upswitch conflict EUR3.834bn vs EUR4.059bn). Debt/cash Unknown.
- Official [rapportannuelspge.be](https://rapportannuelspge.be/) still **2024**-facing. Prior seed CA **EUR418m** / debt **EUR1.58bn** (2024).
- Preferred leftover paths stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo SWDE / Vivaqua / Hydria / CILE / IRE cluster / BRUGEL.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Société publique de Gestion de l'Eau (SPGE)
t.a.v. openbaarheid / information officer
Rue des Ecoles 17-19
4800 Verviers

cc: SPW Environnement — transparence@spw.wallonie.be

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
balansposten en OAA-transfermatrix (KBO 0420.651.980)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / Bestuursdecreet-analoog)
vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF; Companyweb noemt neerlegging 10.07.2026).
2. Balanstotaal / schulden LT-ST / cash reconcilieerbaar met publieke
   aggregators (CW omzet EUR450.223.607; equity EUR2.141.950.395;
   Upswitch assets conflict EUR3.834bn vs EUR4.059bn).
3. Per-OAA / intercommunale transfer- en CSU-enveloppe-matrix 2025
   (bedragen per operator; koppeling Horizon 2030 / epuration).
4. Officieel Rapport annuel 2025 (of publicatiekalender indien nog niet live)
   + reconciliatie statutaire omzet vs eerdere CA 418m-klasse 2024.
5. Dual unit-cost vs Aquafin Vlaanderen (sanitation €/IE of €/m³) indien beschikbaar.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (SPGE + SPW cc)
- [x] Concrete documenten (NBB PDF / BS / OAA matrix / RA2025)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; took leftover **SPGE** YE2025 live. Not an every-10 tick (**EVERY-10 required at 1960**).
""",
        encoding="utf-8",
    )

# research_queue: close rq_1959, spawn rq_1960 with EVERY-10 required
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1960 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1959":
        row["status"] = "done"
        row["entity_id"] = "spge"
        row["updated_utc"] = TS
        row["notes"] = (
            "tick1959; SPGE YE2025 Medium omzet JUMP 450.22m pnl JUMP 27.30m equity 2.142bn; "
            "FOI ready; next rq_1960 EVERY-10 required"
        )
        row["title"] = (
            "leftover dual hole-fill after IRE Fleurus parent — SPGE YE2025 Medium"
        )
    if row.get("task_id") == "rq_1960":
        have_1960 = True

if not have_1960:
    rq_rows.append(
        {
            "task_id": "rq_1960",
            "title": "EVERY-10 progress + leftover dual hole-fill after SPGE",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1960 after 1959 SPGE YE2025 statutory. "
                "**EVERY-10 REQUIRED:** refresh progress_every_10_ticks.md (layers A–E) "
                "+ doge_waste_top10_current.md (top10 by priority_index) then commit note. "
                "Also prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy "
                "(Aquiris YE2025 live deferred; Hedera N/A). "
                "Do NOT redo SPGE, IRE parent, IRE ELiT, FANC, SCK CEN, EURIDICE, BRUGEL, "
                "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1959; EVERY-10 mandatory this tick",
        }
    )

with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1959",
            "ticks_completed": "1959",
            "paused": "no",
            "notes": (
                "tick1959 leftover SPGE 0420.651.980 Medium CW NL+EN+Upswitch "
                "(omzet JUMP 450.22m pnl JUMP 27.30m equity 2.142bn bruto 147.52m "
                "EBITDA 149.19m FTE 65); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1960 EVERY-10 required; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = """

## Tick 1959 - 2026-08-23T16:00:00Z - rq_1959 SPGE (omzet JUMP 450.22m / pnl JUMP 27.30m / Medium)

- Unit: **rq_1959** leftover dual after **rq_1958 IRE FUP**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (NBB YE2025 unpublished); AIESH still **YE2024**; REW still **YE2024**. Took leftover **SPGE** YE2025 (KBO **0420.651.980**; Rue des Ecoles 17-19 Verviers; Walloon sanitation finance SA de droit public; **Aquafin dual**). Do not redo IRE/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/SWDE.
- Found: Companyweb NL+EN + Upswitch YE2025 — omzet **EUR450,223,607** JUMP +9.29%; bruto **EUR147,515,571**; pnl **EUR27,301,169** JUMP turnaround vs LOSS 8.14m; equity **EUR2,141,950,395**; EBITDA **EUR149,189,634**; FTE **65**; neerlegging **10.07.2026**. Assets Unknown (Upswitch conflict 3.834bn vs 4.059bn). Official RA site still 2024-only. Medium confidence.
- Wrote: sources (+4); budgets (+6); commitments (+1); leaderboard (+1); entities (updated spge x2); foi + draft gap_spge_nbb_pdf_assets_debt_oaa_matrix_l5; rq_1959=done + rq_1960 open (**EVERY-10 required**); loop_state ticks=1959.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next tick 1960 MUST run EVERY-10** progress coverage % + waste top10). Next: rq_1960 (EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / Aquiris-deferred / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1959 write OK: SPGE YE2025 Medium omzet 450223607")
