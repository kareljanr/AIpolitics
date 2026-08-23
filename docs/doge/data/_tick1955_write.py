# tick 1955 — SCK CEN YE2025 statutory Medium CW+Upswitch (rq_1955 after EURIDICE)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T14:00:00Z"
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
        "source_id": "src_sck_jr2025_cw",
        "title": "Companyweb SCK CEN YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0406568867/studiecentrum-voor-kernenergie",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1955; Laatste balansjaar 2025; omzet 99270182 DROP -5.6pct; "
            "pnl LOSS -11360315; equity 52666129 DROP; bruto 156483763 JUMP; FTE 883.6"
        ),
    },
    {
        "source_id": "src_sck_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO SCK CEN YE2025 assets operating EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/studiecentrum-voor-kernenergie-0406568867",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1955; YE2025 revenue 99270182 / assets 405049418 / operating -12739851 / "
            "EBITDA 1350522 / equity 52666129 / depr 14090374; YE2024 revenue 105161036 / "
            "assets 401321968 / operating 6459033 / EBITDA 19811605; archive 2026-06-30; debt Unknown"
        ),
    },
    {
        "source_id": "src_sck_kbo_1955",
        "title": "KBO SCK CEN 0406.568.867 Actief SON pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406568867",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1955; Actief SON sinds 28.05.1969; zetel Herrmann-Debrouxlaan 40 1160 Oudergem; "
            "aanbestedende overheid; email caroline.poortmans@sckcen.be; NACE 72.109; "
            "NBB consult pointer; Mol Boeretang campus dual EURIDICE"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1955 YE2025 statutory Medium CW+Upswitch KBO 0406.568.867 Actief SON; "
    "omzet DROP 99.27m bruto JUMP 156.48m pnl LOSS 11.36m operating LOSS 12.74m "
    "assets 405.05m equity DROP 52.67m EBITDA DROP 1.35m FTE 883.6; "
    "Highlights turnover 102.29m conflict vs statutory; FOI gap_sck_nbb_pdf_debt_cash_"
    "euridice_billing_l5; Mol/EURIDICE dual; prior Highlights charges 291.5m still seed"
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "sck_cen": {
            "foi_email": "caroline.poortmans@sckcen.be",
            "foi_postal": "Herrmann-Debrouxlaan 40 1160 Oudergem (campus Boeretang 190 2400 Mol)",
            "website": "https://www.sckcen.be",
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
        "budget_id": "bud_sck_omzet_jr2025_statutory",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "99270182",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_sck_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1955; YE2025 statutory omzet 99270182 DROP -5.6pct vs 105161036; Highlights turnover 102291000 conflict",
    },
    {
        "budget_id": "bud_sck_bruto_jr2025_statutory",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "156483763",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto",
        "source_id": "src_sck_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1955; YE2025 bruto 156483763 JUMP +6.26pct vs 147262173",
    },
    {
        "budget_id": "bud_sck_pnl_jr2025_statutory",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "-11360315",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived net PnL",
        "source_id": "src_sck_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1955; YE2025 pnl LOSS -11360315 vs +14221001; Upswitch operating -12739851 distinct line",
    },
    {
        "budget_id": "bud_sck_operating_jr2025_upswitch",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "-12739851",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived operating result",
        "source_id": "src_sck_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1955; YE2025 operating LOSS -12739851 vs +6459033 YE2024",
    },
    {
        "budget_id": "bud_sck_equity_jr2025_statutory",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "52666129",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Upswitch NBB-derived equity",
        "source_id": "src_sck_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1955; YE2025 equity 52666129 DROP -14.37pct vs 61504638",
    },
    {
        "budget_id": "bud_sck_assets_jr2025_upswitch",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "405049418",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived assets",
        "source_id": "src_sck_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1955; YE2025 assets 405049418 vs 401321968 YE2024; equity ~13pct BS; debt Unknown",
    },
    {
        "budget_id": "bud_sck_ebitda_jr2025_upswitch",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "1350522",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived EBITDA",
        "source_id": "src_sck_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1955; YE2025 EBITDA 1350522 DROP vs 19811605 YE2024; ~1.4pct of omzet",
    },
    {
        "budget_id": "bud_sck_fte_jr2025_statutory",
        "entity_id": "sck_cen",
        "year": "2025",
        "amount_eur": "883.6",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_sck_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1955; YE2025 FTE 883.6 vs 872.9 YE2024; Highlights headcount 999 distinct metric",
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
    "commitment_id": "comm_sck_jr2025_statutory_omzet",
    "title": "SCK CEN YE2025 leftover nuclear R&D dual statutory (omzet DROP 99.27m / pnl LOSS 11.36m / assets 405.05m)",
    "entity_id": "sck_cen",
    "beneficiary": "Federal nuclear science / MYRRHA RECUMO SMR / EURIDICE-Mol dual / industry isotopes",
    "legal_basis": "SON; aanbestedende overheid; NBB neerlegging; wet openbaarheid bestuur",
    "decision_date": "2026-03-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "405049418",
    "cash_by_year": (
        "2025:omzet=99270182;bruto=156483763;pnl=-11360315;operating=-12739851;"
        "assets=405049418;equity=52666129;ebitda=1350522;fte=883.6;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0406568867/studiecentrum-voor-kernenergie",
    "stated_goal": "Nuclear research services education isotopes MYRRHA path",
    "cut_option": "FOI NBB PDF + debt/cash + Highlights vs statutory recon + EURIDICE billing dual",
    "source_id": "src_sck_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Federaal>Nucleair>SCK_CEN>JR2025_statutory_L5",
    "notes": (
        "tick1955; Medium CW+Upswitch YE2025 statutory after EURIDICE; preferred AGB Bornem JR2024 / "
        "FARO YE2024 NBB unpublished / AIESH YE2024 / REW YE2024; do not redo EURIDICE/BRUGEL/Hydria/"
        "Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92; Highlights charges 291.5m separate seed"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_sck_omzet_drop_99_27m_pnl_loss_11_36m_assets_405m_jr2025",
    "name": "SCK CEN omzet DROP 99.27m / pnl LOSS 11.36m / assets 405.05m (statutory YE2025)",
    "level": "L5",
    "type": "nuclear_research_dual",
    "hierarchy_path": "Belgie>Federaal>Nucleair>SCK_CEN>JR2025_statutory_L5",
    "annual_cost_eur": "99270182",
    "total_cost_eur": "405049418",
    "tco_notes": (
        "statutory omzet 99270182 DROP bruto 156483763 pnl LOSS -11360315 operating -12739851 "
        "assets 405049418 equity DROP 52666129 EBITDA DROP 1350522 fte 883.6 debt Unknown; "
        "Highlights turnover 102.29m / charges 291.5m conflict vs statutory"
    ),
    "confidence": "medium",
    "source_id": "src_sck_jr2025_cw",
    "beneficiaries": "Federal energy research / industry / EURIDICE-Mol dual",
    "stated_goal": "Nuclear R&D services education medical isotopes",
    "measured_outcome": (
        "CW+Upswitch YE2025 live; LOSS turnaround from +14.2m; assets 405m; "
        "primary NBB PDF + debt unresolved; Highlights vs statutory omzet gap"
    ),
    "absurdity_score": "5.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.0",
    "cut_proposal": "Publish NBB PDF + debt/cash + reconcile Highlights vs statutory + EURIDICE billing",
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1955; Medium CW+Upswitch; leftover nuclear dual after EURIDICE; "
        "not TE-additive pure-waste top10; prior Highlights lbs remain"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_sck_nbb_pdf_debt_cash_euridice_billing_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Belgie>Federaal>Nucleair>SCK_CEN>nbb_pdf_debt_cash_L5",
    "entity_id": "sck_cen",
    "what_is_missing": (
        "NBB deposit PDF body for YE2025; debt/cash schedule recon to assets 405049418; "
        "reconcile Highlights turnover 102291000 vs statutory omzet 99270182; "
        "EURIDICE/NIRAS billing + staffing dual matrix"
    ),
    "why_it_matters": (
        "SON with 99.27m statutory omzet / 405m assets / LOSS 11.36m — Highlights vs NBB framing "
        "and Mol EURIDICE dual-count risk need primary PDF"
    ),
    "priority": "8",
    "recipient_body": "SCK CEN (cc EURIDICE / NIRAS)",
    "recipient_email": "caroline.poortmans@sckcen.be",
    "recipient_postal": "Herrmann-Debrouxlaan 40 1160 Oudergem (cc Boeretang 190 2400 Mol)",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_sck_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_sck_omzet_drop_99_27m_pnl_loss_11_36m_assets_405m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1955; human-send only; Medium CW+Upswitch; next every-10 1960",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — SCK CEN (NBB PDF / debt-cash / EURIDICE billing)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** SCK CEN SON — KBO **0406.568.867**  
**recipient:** caroline.poortmans@sckcen.be / Herrmann-Debrouxlaan 40 1160 Oudergem / cc EURIDICE+NIRAS  
**sources:** [Companyweb](https://www.companyweb.be/nl/0406568867/studiecentrum-voor-kernenergie) · [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/studiecentrum-voor-kernenergie-0406568867) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406568867) · [sckcen.be](https://www.sckcen.be)  
**tick:** 1955 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW + Upswitch; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025**: omzet **EUR99,270,182** (**DROP -5.6%**); bruto **EUR156,483,763**; pnl **LOSS EUR-11,360,315**; operating **LOSS EUR-12,739,851**; assets **EUR405,049,418**; equity **EUR52,666,129** (**DROP**); EBITDA **EUR1,350,522**; FTE **883.6**; **debt Unknown**.
- **Conflict:** Highlights 2025 turnover **EUR102.291m** / charges **EUR291.538m** vs statutory CW/Upswitch framing.
- **Public dual:** Mol Boeretang campus with EURIDICE VOF (KBO 0455.635.823); NIRAS/FANC/Bel V nuclear stack.
- Preferred leftover paths stalled: AGB Bornem **JR2024-only**; FARO NBB YE2025 unpublished; AIESH/REW **YE2024**. Do not redo EURIDICE / BRUGEL / Hydria / Vivaqua / Belgoprocess / Laborelec / CILE / NIRAS / Bel V.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: SCK CEN
t.a.v. openbaarheid / informatieambtenaar
Herrmann-Debrouxlaan 40
1160 Oudergem

cc: EURIDICE VOF
Boeretang 190
2400 Mol

cc: NIRAS/ONDRAF
Koning Albert II-laan 32
1000 Brussel

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
schulden/cash en EURIDICE-facturatie (KBO 0406.568.867)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF).
2. Schuldenrooster LT/ST en cash,
   reconcilieerbaar met assets EUR405.049.418 en equity EUR52.666.129.
3. Reconciliatie Highlights-turnover EUR102.291.000 vs statutaire omzet
   EUR99.270.182 (en charges/income vs PnL LOSS).
4. Facturatie-/bijdragematrix EURIDICE en NIRAS 2025
   (pass-through vs eigen kosten / detachering).
5. Actueel overzicht federale dotaties vs eigen omzet 2025
   (werkingsdotatie / MYRRHA / RECUMO / SMR / fysieke bescherming).

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (SCK CEN SON)
- [x] Concrete documenten (NBB PDF + debt/cash + dual billing)
- [x] Periode en bedragen gevraagd
- [x] Meerjarigheid / dual EURIDICE expliciet
- [ ] Contactgegevens verzoeker (human)
- [x] foi_queue.csv ready — **NOT sent**
""",
        encoding="utf-8",
    )

# research_queue: close rq_1955, spawn rq_1956
update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1955": {
            "status": "done",
            "entity_id": "sck_cen",
            "updated_utc": TS,
            "title": "leftover dual hole-fill after EURIDICE — SCK CEN YE2025 statutory Medium",
            "notes": (
                "tick1955 SCK CEN after EURIDICE; Medium CW+Upswitch omzet DROP 99.27m pnl LOSS 11.36m "
                "assets 405.05m equity DROP 52.67m; FOI ready not sent; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_1956; next every-10 1960"
            ),
        }
    },
)

existing_rq = set()
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_rq.add(row.get("task_id") or "")

if "rq_1956" not in existing_rq:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1956",
                "title": "leftover dual hole-fill after SCK CEN",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 1956 after 1955 SCK CEN statutory. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy. "
                    "Do NOT redo SCK CEN, EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
                    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "spawned after tick1955; next every-10 1960",
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
            "last_unit_id": "rq_1955",
            "ticks_completed": "1955",
            "paused": "no",
            "notes": (
                "tick1955 leftover SCK CEN 0406.568.867 Medium CW (omzet DROP 99.27m pnl LOSS 11.36m "
                "assets 405.05m equity DROP 52.67m FTE 883.6); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1956; next every-10 1960; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = """

## Tick 1955 - 2026-08-23T14:00:00Z - rq_1955 SCK CEN (omzet DROP 99.27m / pnl LOSS 11.36m / assets 405.05m / Medium)

- Unit: **rq_1955** leftover dual after EURIDICE. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (NBB YE2025 unpublished); AIESH still **YE2024** (filed 17.07.2025); REW still **YE2024**. Took leftover **SCK CEN** statutory YE2025 (KBO **0406.568.867**; Herrmann-Debrouxlaan 40 Oudergem / Mol Boeretang campus; SON nuclear R&D; **EURIDICE dual**). Do not redo EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92.
- Primary hunt: NBB deposit PDF unresolved (consult SPA). **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0406568867/studiecentrum-voor-kernenergie) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/studiecentrum-voor-kernenergie-0406568867) + Strong KBO: omzet **EUR99,270,182** (**DROP -5.6%**); bruto **EUR156,483,763**; PnL **LOSS EUR-11,360,315**; operating **LOSS EUR-12,739,851**; assets **EUR405,049,418**; equity **EUR52,666,129** (**DROP**); EBITDA **EUR1,350,522**; FTE **883.6**; debt **Unknown**. Conflict: Highlights turnover **102.291m** / charges **291.538m** vs statutory framing.
- Wrote: sources (+3); budgets (+8 statutory); commitments (+1); leaderboard (+1); entities (updated sck_cen); foi + draft gap_sck_nbb_pdf_debt_cash_euridice_billing_l5; rq_1955=done + rq_1956 open; loop_state ticks=1955.
- FOI opened: NBB PDF + debt/cash + Highlights vs statutory + EURIDICE billing (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1956 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1955 write OK; sources", len(sources_new), "budgets", len(budgets_new))
