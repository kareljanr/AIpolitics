# tick 1945 — Dijk92 YE2025 Medium CW (rq_1945; 1944 AIEG already on main; preferred leftover)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T19:45:00Z"
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


# skip duplicate sources if already present from aborted 1944 write
existing_src = set()
with (DATA / "sources.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_src.add(row.get("source_id") or "")

sources_new = [
    {
        "source_id": "src_dijk92_jr2025_cw",
        "title": "Companyweb Projectvereniging Dijk 92 YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0806383071/projectvereniging-dijk-92",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1945; Laatste balansjaar 2025; bruto 633379 JUMP +29.39pct; "
            "pnl NEG -5895 IMPROVED +82.49pct vs -33657; equity 340407 DROP -1.7pct; "
            "FTE 8.1; omzet/assets Unknown on free CW; NBB deposit PDF body still SPA/403"
        ),
    },
    {
        "source_id": "src_dijk92_jr2025_cw_en",
        "title": "Companyweb EN Projectvereniging Dijk 92 YE2025",
        "url": "https://www.companyweb.be/en/0806383071/projectvereniging-dijk-92",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1945; EN confirms Gross margin 633379 / Profit-Loss -5895 / Equity 340407 / Employees 8.1 / last balance sheet year 2025",
    },
    {
        "source_id": "src_dijk92_nbb_deposit_pointer_1945",
        "title": "NBB CBSO consult deposit pointer 2026-00377886 Dijk92",
        "url": "https://consult.cbso.nbb.be/consultationserver/viewDocument/2026-00377886",
        "publisher": "NBB CBSO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1945; HTTP 200 SPA shell only (no PDF bytes); SBM CDN mirror still 403; deposit id retained from prior FOI hunt",
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_dijk92_bruto_jr2025",
        "entity_id": "igs_dijk92",
        "year": "2025",
        "amount_eur": "633379",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived brutomarge",
        "source_id": "src_dijk92_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1945; YE2025 bruto 633379 JUMP +29.39pct vs 489501",
    },
    {
        "budget_id": "bud_dijk92_pnl_jr2025",
        "entity_id": "igs_dijk92",
        "year": "2025",
        "amount_eur": "-5895",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9904",
        "source_id": "src_dijk92_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1945; YE2025 pnl NEG -5895 IMPROVED +82.49pct vs -33657",
    },
    {
        "budget_id": "bud_dijk92_equity_jr2025",
        "entity_id": "igs_dijk92",
        "year": "2025",
        "amount_eur": "340407",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 10/15",
        "source_id": "src_dijk92_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1945; YE2025 equity 340407 DROP -1.7pct vs 346301",
    },
    {
        "budget_id": "bud_dijk92_fte_jr2025",
        "entity_id": "igs_dijk92",
        "year": "2025",
        "amount_eur": "8",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived FTE 8.1",
        "source_id": "src_dijk92_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1945; YE2025 FTE 8.1 (stored 8); was 7.5 YE2024",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

update_csv_rows(
    DATA / "commitments.csv",
    "commitment_id",
    {
        "comm_dijk92_jr2025_pending_nbb": {
            "title": "Dijk92 YE2025 leftover IGS IOED dual (bruto JUMP 0.63m / pnl LOSS 5.9k IMPROVED / equity 0.34m)",
            "entity_id": "igs_dijk92",
            "beneficiary": "Berlare Buggenhout Dendermonde Hamme Laarne Lebbeke Wetteren Wichelen Zele / Erfgoedcel Land van Dendermonde",
            "legal_basis": "Decreet intergemeentelijke samenwerking; Projectvereniging; Bestuursdecreet openbaarheid; NBB neerlegging",
            "decision_date": "2026-08-27",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "633379",
            "cash_by_year": "2025:bruto=633379;pnl=-5895;equity=340407;fte=8.1;omzet=Unknown;assets=Unknown",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/nl/0806383071/projectvereniging-dijk-92",
            "stated_goal": "Bovenlokaal cultuur / erfgoedcel / archief IOED Dendermonde-belt",
            "cut_option": "FOI NBB PDF + omzet/assets/debt + per-gemeente bijdragen matrix + AV vaststelling",
            "source_id": "src_dijk92_jr2025_cw",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>IGS>IOED>Dijk92>JR2025_L5",
            "notes": (
                "tick1945; Medium CW after long CDN stall; preferred leftover after AIEG 1944; "
                "AGB Bornem still JR2024; FARO YE2024; do not redo AIEG/Synatom/Synergrid/Atrias/RESA/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink"
            ),
        }
    },
)

update_csv_rows(
    DATA / "leaderboard.csv",
    "item_id",
    {
        "lb_dijk92_jr2025_nbb_foi_l5": {
            "name": "Dijk92 bruto JUMP 0.63m / pnl LOSS 5.9k IMPROVED / equity 0.34m (IOED YE2025)",
            "level": "L5",
            "type": "igs_ioed_dual",
            "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>IGS>IOED>Dijk92>JR2025_L5",
            "annual_cost_eur": "633379",
            "total_cost_eur": "633379",
            "tco_notes": "bruto 633379 JUMP +29pct pnl NEG -5895 IMPROVED equity 340407 FTE 8.1; omzet/assets Unknown; NBB PDF SPA/403",
            "confidence": "medium",
            "source_id": "src_dijk92_jr2025_cw",
            "beneficiaries": "Berlare Buggenhout Dendermonde Hamme Laarne Lebbeke Wetteren Wichelen Zele",
            "stated_goal": "Bovenlokaal cultuur / erfgoedcel / archief IOED",
            "measured_outcome": "CW YE2025 live after long CDN stall; bruto JUMP with micro LOSS; municipal contrib matrix still FOI",
            "absurdity_score": "3.5",
            "cost_score": "2.5",
            "difficulty": "3.0",
            "priority_index": "3.3",
            "cut_proposal": "Publish NBB PDF + omzet/assets/debt + per-gemeente bijdragen + AV vaststelling",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1945; Medium CW; preferred leftover after AIEG; was weak FOI-only at tick1809; not TE-additive",
        }
    },
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "igs_dijk92": {
            "website": "https://www.dijk92.be/",
            "foi_email": "info@egclandvandendermonde.be",
            "foi_postal": "Nijverheidsstraat 3 9200 Dendermonde",
            "notes": (
                "tick1809 FOI-only stall; tick1945 YE2025 Medium CW KBO 0806.383.071 Actief Projectvereniging; "
                "bruto 633379 JUMP pnl NEG -5895 IMPROVED equity 340407 FTE 8.1 omzet/assets Unknown; "
                "NBB consult 2026-00377886 HTTP200 SPA / SBM CDN 403; FOI gap updated; "
                "aanbestedende overheid; 9 Dendermonde-belt gemeenten"
            ),
        }
    },
)

update_csv_rows(
    DATA / "foi_queue.csv",
    "gap_id",
    {
        "gap_dijk92_nbb_ye2025_deposit_l5": {
            "what_is_missing": (
                "NBB deposit PDF body for YE2025 (consult 2026-00377886 SPA shell / SBM CDN 403); "
                "omzet code70 + assets/debt/cash exact; per-gemeente bijdragen matrix; AV vaststelling; "
                "recon CW bruto 633379 / pnl -5895 / equity 340407 / FTE 8.1"
            ),
            "why_it_matters": (
                "Preferred leftover IOED long-blocked — now Medium CW YE2025 euros live but primary PDF still opaque; "
                "municipal money path for 9 gemeenten needs statutory confirm"
            ),
            "priority": "8",
            "draft_letter_path": "docs/doge/foi/drafts/gap_dijk92_nbb_ye2025_deposit_l5.md",
            "status": "ready",
            "date_ready": "2026-08-27",
            "linked_commitment_id": "comm_dijk92_jr2025_pending_nbb",
            "linked_leaderboard_id": "lb_dijk92_jr2025_nbb_foi_l5",
            "updated_utc": TS,
            "notes": (
                "tick1945; human-send only; Medium CW YE2025 fill; NBB PDF still blocked; "
                "AGB Bornem JR2024; FARO YE2024; next every-10 1950"
            ),
        }
    },
)

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1945": {
            "status": "done",
            "entity_id": "igs_dijk92",
            "title": "Leftover dual residual hole-fill after AIEG — Dijk92 YE2025 Medium",
            "instructions": (
                "Completed: Dijk92 Projectvereniging leftover IGS IOED dual after AIEG; "
                "KBO 0806.383.071; YE2025 Medium Companyweb; sourced euros bruto 633379 JUMP "
                "pnl NEG -5895 IMPROVED equity 340407 FTE 8.1 omzet/assets Unknown; "
                "FOI ready gap_dijk92_nbb_ye2025_deposit_l5 (updated); "
                "NOT AIEG/Synatom/Synergrid/Atrias/RESA/Sibelga/ORES/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink"
            ),
            "blocked_gap_id": "gap_dijk92_nbb_ye2025_deposit_l5",
            "updated_utc": TS,
            "notes": (
                "tick1945 Dijk92 preferred leftover after AIEG (CDN consult 200 SPA; CW YE2025); "
                "KBO 0806.383.071; Medium CW bruto JUMP 0.63m pnl LOSS 5.9k IMPROVED equity 0.34m FTE 8.1; "
                "FOI ready not sent; AGB Bornem JR2024; FARO YE2024; next rq_1946; next every-10 1950"
            ),
        }
    },
)

# dedupe any duplicate open rq_1945 rows left from race
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
seen_1945 = False
deduped = []
for row in rows:
    if row["task_id"] == "rq_1945":
        if seen_1945:
            continue
        seen_1945 = True
    deduped.append(row)
with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(deduped)

rq1946 = {
    "task_id": "rq_1946",
    "title": "Leftover dual residual hole-fill after Dijk92 (AGB/APB-if-live / FARO-if-YE2025 / AIESH-energy-IGS-if-live)",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "Vlaanderen>leftover_dual",
    "entity_id": "",
    "instructions": (
        "Tick 1946 after 1945 Dijk92. Prefer leftover AGB/APB if PDF live, else FARO if TRUE NBB YE2025, "
        "else AIESH / unused energy/DSO/IGS/HVZ if live YE2025 euros. Do NOT redo Dijk92, AIEG, Synatom, "
        "Synergrid, Atrias, RESA, Sibelga, ORES, BNO, Fluxys holding/LNG/c-grid/c-grid Antwerp/hydrogen, "
        "ETB, Elia Group, Pipelink, Enodia, Publi-T, Publigas, Interfin, Fluvius."
    ),
    "blocked_gap_id": "",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "spawned after tick1945; next every-10 1950",
}
# avoid duplicate spawn
has_1946 = any(row["task_id"] == "rq_1946" for row in deduped)
if not has_1946:
    append_csv(DATA / "research_queue.csv", [rq1946])

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
            "last_unit_id": "rq_1945",
            "ticks_completed": "1945",
            "paused": "no",
            "notes": (
                "tick1945 leftover Dijk92 0806.383.071 Medium CW (bruto JUMP 633k pnl NEG -5.9k IMPROVED "
                "equity 340k FTE 8.1 omzet/assets Unknown); NBB PDF FOI updated; AGB Bornem JR2024; "
                "FARO YE2024; next rq_1946; next every-10 1950; continuous hole_fill"
            ),
        }
    )

# update FOI draft tick label if still says 1944
draft = ROOT / "docs/doge/foi/drafts/gap_dijk92_nbb_ye2025_deposit_l5.md"
if draft.exists():
    txt = draft.read_text(encoding="utf-8")
    txt = txt.replace("**tick:** 1944", "**tick:** 1945")
    txt = txt.replace("tick1944", "tick1945")
    draft.write_text(txt, encoding="utf-8")

log_block = """

## Tick 1945 - 2026-08-27T19:45:00Z - rq_1945 Dijk92 (bruto JUMP 0.63m / pnl LOSS 5.9k IMPROVED / Medium)

- Unit: **rq_1945** leftover dual after concurrent **rq_1944 AIEG** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; **Dijk92** NBB consult **HTTP 200** (SPA shell; SBM CDN still **403**) — took preferred leftover **Projectvereniging DIJK 92** (KBO **0806.383.071**; Nijverheidsstraat 3 Dendermonde; IOED cultuur/erfgoed/archief; 9 gemeenten; aanbestedende overheid). Do not redo AIEG/Synatom/Synergrid/Atrias/RESA/Sibelga/ORES/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink.
- Primary hunt: NBB deposit PDF body still unresolved (consult SPA / SBM 403). **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0806383071/projectvereniging-dijk-92) + EN twin + KBO (Laatste balansjaar **2025**): bruto **EUR633,379** (**JUMP +29.39%**); PnL **NEG EUR-5,895** (**IMPROVED +82.49%** vs -33,657); equity **EUR340,407** (**DROP -1.7%**); FTE **8.1**; omzet / assets **Unknown**.
- Wrote: sources (+3); budgets (+4); commitments (updated pending→Medium euros); leaderboard (updated weak FOI→Medium active); entities (updated igs_dijk92); foi gap+draft updated; rq_1945=done + rq_1946 open; loop_state ticks=1945.
- FOI updated: NBB PDF + omzet/assets/debt + gemeentelijke bijdragen (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1950**). Next: rq_1946 (AGB/APB-if-live / FARO-if-YE2025 / AIESH-energy-IGS).
"""
with (ROOT / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1945 write OK")
