# tick 1956 — FANC YE2025 statutory Medium CW+Upswitch (rq_1956 after SCK CEN)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T14:20:00Z"
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
        "source_id": "src_fanc_jr2025_cw",
        "title": "Companyweb FANC YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0254487220/agence-federale-de-controle-nucleaire",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1956; Laatste balansjaar 2025; omzet 34359867 JUMP +7.2pct; "
            "pnl JUMP 5216442; equity JUMP 53793129; bruto 26837708; FTE 142.9"
        ),
    },
    {
        "source_id": "src_fanc_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO FANC YE2025 assets equity EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/agence-federale-de-controle-nucleaire-0254487220",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1956; YE2025 revenue 34359867 / assets 59811395 / EBITDA 5575879 / "
            "equity 53793129; YE2024 revenue 32051111 / assets 54241394 / EBITDA 4223275 / "
            "equity 48576687; archive 2026-06-30; debt recon assets-equity ~6018266"
        ),
    },
    {
        "source_id": "src_fanc_kbo_1956",
        "title": "KBO FANC 0254.487.220 Actief OI pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0254487220",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1956; Actief OI sinds 15.04.1994; zetel Markiesstraat 1 1000 Brussel; "
            "aanbestedende overheid; email pointcontact@fanc.fgov.be; NACE 71.209/84.249; "
            "NBB consult pointer; Bel V TSO dual"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1956 YE2025 statutory Medium CW+Upswitch KBO 0254.487.220 Actief OI; "
    "omzet JUMP 34.36m bruto JUMP 26.84m pnl JUMP 5.22m assets JUMP 59.81m "
    "equity JUMP 53.79m EBITDA JUMP 5.58m FTE 142.9 debt ~6.02m recon; "
    "FOI gap_fanc_nbb_pdf_debt_belv_fee_recon_l5; Bel V/NIRAS/SCK dual; "
    "prior Kamer 1281/023 fees 30.8m 2026 budget seed remains"
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "fanc": {
            "foi_email": "pointcontact@fanc.fgov.be",
            "foi_postal": "Markiesstraat 1 1000 Brussel",
            "website": "https://www.fanc.fgov.be",
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
        "budget_id": "bud_fanc_omzet_jr2025_statutory",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "34359867",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_fanc_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1956; YE2025 statutory omzet 34359867 JUMP +7.2pct vs 32051111",
    },
    {
        "budget_id": "bud_fanc_bruto_jr2025_statutory",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "26837708",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto",
        "source_id": "src_fanc_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1956; YE2025 bruto 26837708 JUMP +8.82pct vs 24663425",
    },
    {
        "budget_id": "bud_fanc_pnl_jr2025_statutory",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "5216442",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived net PnL",
        "source_id": "src_fanc_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1956; YE2025 pnl JUMP 5216442 +26.71pct vs 4116898",
    },
    {
        "budget_id": "bud_fanc_equity_jr2025_statutory",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "53793129",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Upswitch NBB-derived equity",
        "source_id": "src_fanc_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1956; YE2025 equity 53793129 JUMP +10.74pct vs 48576687; ~90pct BS",
    },
    {
        "budget_id": "bud_fanc_assets_jr2025_upswitch",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "59811395",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived assets",
        "source_id": "src_fanc_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1956; YE2025 assets 59811395 vs 54241394 YE2024; debt recon ~6018266",
    },
    {
        "budget_id": "bud_fanc_ebitda_jr2025_upswitch",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "5575879",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived EBITDA",
        "source_id": "src_fanc_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1956; YE2025 EBITDA 5575879 JUMP vs 4223275 YE2024; ~16.2pct of omzet",
    },
    {
        "budget_id": "bud_fanc_debt_jr2025_recon",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "6018266",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "assets-equity recon Medium (NBB-derived)",
        "source_id": "src_fanc_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1956; YE2025 debt ~6018266 = assets 59811395 - equity 53793129; FOI LT/ST split",
    },
    {
        "budget_id": "bud_fanc_fte_jr2025_statutory",
        "entity_id": "fanc",
        "year": "2025",
        "amount_eur": "142.9",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_fanc_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1956; YE2025 FTE 142.9 vs 143.8 YE2024",
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
    "commitment_id": "comm_fanc_jr2025_statutory_omzet",
    "title": "FANC YE2025 leftover nuclear regulator dual statutory (omzet JUMP 34.36m / pnl JUMP 5.22m / assets 59.81m)",
    "entity_id": "fanc",
    "beneficiary": "Nuclear licensees / public safety / Bel V TSO dual / NIRAS-SCK stack",
    "legal_basis": "Wet 15.04.1994 AFCN; OI; aanbestedende overheid; NBB neerlegging; wet openbaarheid bestuur",
    "decision_date": "2026-05-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "59811395",
    "cash_by_year": (
        "2025:omzet=34359867;bruto=26837708;pnl=5216442;assets=59811395;"
        "equity=53793129;ebitda=5575879;debt~6018266;fte=142.9"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0254487220/agence-federale-de-controle-nucleaire",
    "stated_goal": "Independent nuclear safety regulation fee/tax financed",
    "cut_option": "FOI NBB PDF + debt LT/ST + Bel V recovery + fee vs Kamer budget recon",
    "source_id": "src_fanc_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Federaal>Nucleair>FANC>JR2025_statutory_L5",
    "notes": (
        "tick1956; Medium CW+Upswitch YE2025 statutory after SCK CEN; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo SCK CEN/EURIDICE/BRUGEL/Hydria/"
        "Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92; prior Kamer fees seed remains"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_fanc_omzet_jump_34_36m_pnl_jump_5_22m_assets_59_81m_jr2025",
    "name": "FANC omzet JUMP 34.36m / pnl JUMP 5.22m / assets 59.81m (statutory YE2025)",
    "level": "L5",
    "type": "nuclear_regulator_dual",
    "hierarchy_path": "Belgie>Federaal>Nucleair>FANC>JR2025_statutory_L5",
    "annual_cost_eur": "34359867",
    "total_cost_eur": "59811395",
    "tco_notes": (
        "statutory omzet 34359867 JUMP bruto 26837708 pnl JUMP 5216442 assets 59811395 "
        "equity JUMP 53793129 EBITDA JUMP 5575879 debt~6018266 fte 142.9; "
        "fee-financed dual Bel V; Kamer 2026 fees 30.8m budget distinct line"
    ),
    "confidence": "medium",
    "source_id": "src_fanc_jr2025_cw",
    "beneficiaries": "Nuclear licensees / public / Bel V TSO dual",
    "stated_goal": "Independent nuclear safety regulation",
    "measured_outcome": (
        "CW+Upswitch YE2025 live; first full statutory NBB-derived euros after FOI residual; "
        "primary NBB PDF + Bel V fee matrix unresolved"
    ),
    "absurdity_score": "4.5",
    "cost_score": "6.5",
    "difficulty": "3.5",
    "priority_index": "5.5",
    "cut_proposal": "Publish NBB PDF + debt split + Bel V recovery + reconcile Kamer fee budget",
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1956; Medium CW+Upswitch; leftover nuclear dual after SCK CEN/Bel V; "
        "not TE-additive pure-waste top10; fee-financed category C"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_fanc_nbb_pdf_debt_belv_fee_recon_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Belgie>Federaal>Nucleair>FANC>nbb_pdf_debt_belv_L5",
    "entity_id": "fanc",
    "what_is_missing": (
        "NBB deposit PDF body for YE2025; LT/ST debt + cash recon to assets 59811395; "
        "Bel V delegation/recovery fee matrix 2025; reconcile statutory omzet 34359867 vs "
        "Kamer DOC 56 1281/023 fee/tax receipts schedule"
    ),
    "why_it_matters": (
        "Fee-financed nuclear regulator with 34.36m omzet / 59.81m assets / Bel V TSO dual — "
        "primary PDF and fee path still needed after Medium CW fill"
    ),
    "priority": "8",
    "recipient_body": "FANC / AFCN (cc Bel V)",
    "recipient_email": "pointcontact@fanc.fgov.be",
    "recipient_postal": "Markiesstraat 1 1000 Brussel (cc Bel V Walcourtstraat 148 1070 Anderlecht)",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_fanc_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_fanc_omzet_jump_34_36m_pnl_jump_5_22m_assets_59_81m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1956; human-send only; Medium CW+Upswitch; next every-10 1960; prior gap_fanc_budget partial remains",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — FANC (NBB PDF / debt / Bel V fee recon)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** FANC / AFCN OI — KBO **0254.487.220**  
**recipient:** pointcontact@fanc.fgov.be / Markiesstraat 1 1000 Brussel / cc Bel V  
**sources:** [Companyweb](https://www.companyweb.be/nl/0254487220/agence-federale-de-controle-nucleaire) · [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/agence-federale-de-controle-nucleaire-0254487220) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0254487220) · [fanc.fgov.be](https://www.fanc.fgov.be)  
**tick:** 1956 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW + Upswitch; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025**: omzet **EUR34,359,867** (**JUMP +7.2%**); bruto **EUR26,837,708**; pnl **EUR5,216,442** (**JUMP +26.7%**); assets **EUR59,811,395**; equity **EUR53,793,129** (**JUMP**); EBITDA **EUR5,575,879**; FTE **142.9**; debt **~EUR6,018,266** (assets−equity recon).
- **Public dual:** Bel V TSO (KBO 0892.419.202) + NIRAS/SCK CEN nuclear stack; fee/tax financed category C.
- Preferred leftover paths stalled: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024** (filed 17.07.2025); REW **YE2024**. Do not redo SCK CEN / EURIDICE / BRUGEL / Hydria / Vivaqua / Belgoprocess / Laborelec / CILE / NIRAS / Bel V / Dijk92.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Federaal Agentschap voor Nucleaire Controle (FANC/AFCN)
t.a.v. openbaarheid / informatieambtenaar
Markiesstraat 1
1000 Brussel

cc: Bel V
Walcourtstraat 148
1070 Anderlecht

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
schulden/cash en Bel V-recuperatie (KBO 0254.487.220)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF).
2. Schuldenrooster LT/ST en cash,
   reconcilieerbaar met assets EUR59.811.395 en equity EUR53.793.129.
3. Recuperatie-/delegatiematrix Bel V 2025
   (uurfacturatie / fee-pass-through vs FANC eigen kosten).
4. Reconciliatie statutaire omzet EUR34.359.867 vs Kamer DOC 56 1281/023
   heffingen/redevances-schema (NPP vs overige).
5. Actueel FTE-overzicht en personeelskosten vs Kamer personeelskrediet.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (FANC / AFCN)
- [x] Concrete documenten (NBB PDF + debt/cash + Bel V dual)
- [x] Periode en bedragen gevraagd
- [x] Meerjarigheid / dual Bel V expliciet
- [ ] Contactgegevens verzoeker (human)
- [x] foi_queue.csv ready — **NOT sent**
""",
        encoding="utf-8",
    )

# research_queue: close rq_1956, spawn rq_1957
update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1956": {
            "status": "done",
            "entity_id": "fanc",
            "updated_utc": TS,
            "title": "leftover dual hole-fill after SCK CEN — FANC YE2025 statutory Medium",
            "notes": (
                "tick1956 FANC after SCK CEN; Medium CW+Upswitch omzet JUMP 34.36m pnl JUMP 5.22m "
                "assets 59.81m equity JUMP 53.79m; FOI ready not sent; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_1957; next every-10 1960"
            ),
        }
    },
)

existing_rq = set()
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_rq.add(row.get("task_id") or "")

if "rq_1957" not in existing_rq:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1957",
                "title": "leftover dual hole-fill after FANC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 1957 after 1956 FANC statutory. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy "
                    "(IRE Fleurus if YE2025 live unused). "
                    "Do NOT redo FANC, SCK CEN, EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
                    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "spawned after tick1956; next every-10 1960",
            }
        ],
    )

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1956",
            "ticks_completed": "1956",
            "paused": "no",
            "notes": (
                "tick1956 leftover FANC 0254.487.220 Medium CW (omzet JUMP 34.36m pnl JUMP 5.22m "
                "assets 59.81m equity JUMP 53.79m FTE 142.9); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1957; next every-10 1960; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = """

## Tick 1956 - 2026-08-23T14:20:00Z - rq_1956 FANC (omzet JUMP 34.36m / pnl JUMP 5.22m / assets 59.81m / Medium)

- Unit: **rq_1956** leftover dual after SCK CEN. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (filed 17.07.2025); REW still **YE2024**. Took leftover **FANC/AFCN** statutory YE2025 (KBO **0254.487.220**; Markiesstraat 1 Brussel; OI nuclear regulator; **Bel V dual**). Do not redo SCK CEN/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92.
- Primary hunt: NBB deposit PDF unresolved (consult SPA). **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0254487220/agence-federale-de-controle-nucleaire) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/agence-federale-de-controle-nucleaire-0254487220) + Strong KBO: omzet **EUR34,359,867** (**JUMP +7.2%**); bruto **EUR26,837,708**; PnL **EUR5,216,442** (**JUMP +26.7%**); assets **EUR59,811,395**; equity **EUR53,793,129** (**JUMP**); EBITDA **EUR5,575,879**; FTE **142.9**; debt **~EUR6,018,266** (assets−equity).
- Wrote: sources (+3); budgets (+8 statutory); commitments (+1); leaderboard (+1); entities (updated fanc); foi + draft gap_fanc_nbb_pdf_debt_belv_fee_recon_l5; rq_1956=done + rq_1957 open; loop_state ticks=1956.
- FOI opened: NBB PDF + debt/cash + Bel V recovery + Kamer fee recon (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1957 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / IRE-if-unused / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1956 write OK; sources", len(sources_new), "budgets", len(budgets_new))
