# tick 1951 — Vivaqua YE2025 Medium CW+Upswitch (rq_1951 after Belgoprocess EVERY-10)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T22:30:00Z"
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
        "source_id": "src_vivaqua_jr2025_cw",
        "title": "Companyweb Vivaqua YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0202962701/vivaqua",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1951; Laatste balansjaar 2025; neerlegging 11.06.2026; "
            "omzet 355999963 JUMP +9.23pct; bruto 313200862 +6.84pct; "
            "pnl 4638914 JUMP turnaround vs -860069; equity 569707719 +1.82pct; FTE 1260.3"
        ),
    },
    {
        "source_id": "src_vivaqua_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO Vivaqua YE2025 assets EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/vivaqua-0202962701",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1951; YE2025 assets 1759637813 / equity 569707719 / revenue 355999963 / "
            "EBITDA 131058980 / operating result 31301868; YE2024 assets 1803925994; archive 2026-06-30"
        ),
    },
    {
        "source_id": "src_vivaqua_kbo_1951",
        "title": "KBO Vivaqua 0202.962.701 Actief CV pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0202962701",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1951; Actief CV; zetel Keizerinlaan 17-19 1000 Brussel; NBB consult pointer",
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
        "budget_id": "bud_vivaqua_omzet_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "355999963",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet",
        "source_id": "src_vivaqua_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1951; YE2025 omzet 355999963 JUMP +9.23pct vs 325924635",
    },
    {
        "budget_id": "bud_vivaqua_bruto_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "313200862",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived brutomarge",
        "source_id": "src_vivaqua_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1951; YE2025 bruto 313200862 +6.84pct vs 293161044",
    },
    {
        "budget_id": "bud_vivaqua_pnl_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "4638914",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9904",
        "source_id": "src_vivaqua_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1951; YE2025 pnl 4638914 JUMP turnaround vs -860069 YE2024",
    },
    {
        "budget_id": "bud_vivaqua_equity_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "569707719",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW/Upswitch NBB-derived equity",
        "source_id": "src_vivaqua_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1951; YE2025 equity 569707719 +1.82pct vs 559497068",
    },
    {
        "budget_id": "bud_vivaqua_assets_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "1759637813",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB/CBSO total assets",
        "source_id": "src_vivaqua_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1951; YE2025 assets 1759637813 DROP vs YE2024 1803925994",
    },
    {
        "budget_id": "bud_vivaqua_ebitda_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "131058980",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB/CBSO EBITDA",
        "source_id": "src_vivaqua_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1951; YE2025 EBITDA 131058980; operating result 31301868",
    },
    {
        "budget_id": "bud_vivaqua_fte_jr2025",
        "entity_id": "vivaqua",
        "year": "2025",
        "amount_eur": "1260",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived FTE 1260.3",
        "source_id": "src_vivaqua_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1951; YE2025 FTE 1260.3 (stored 1260); was 1262.1 YE2024",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

existing_comm = set()
with (DATA / "commitments.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_comm.add(row.get("commitment_id") or "")

if "comm_vivaqua_jr2025_omzet" not in existing_comm:
    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_vivaqua_jr2025_omzet",
                "title": "Vivaqua YE2025 leftover BCR water dual (omzet JUMP 356.0m / pnl JUMP 4.64m turnaround / assets 1.76bn)",
                "entity_id": "vivaqua",
                "beneficiary": "BCR communes / Brussels water users / Hydria assainissement path",
                "legal_basis": "CV intercommunale; Brugel tariffs; NBB neerlegging; BCR openbaarheid",
                "decision_date": "2026-06-11",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": "355999963",
                "cash_by_year": (
                    "2025:omzet=355999963;bruto=313200862;pnl=4638914;equity=569707719;"
                    "assets=1759637813;ebitda=131058980;fte=1260.3;debt=Unknown"
                ),
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": "https://www.companyweb.be/nl/0202962701/vivaqua",
                "stated_goal": "BCR drinking water production/distribution + assainissement path",
                "cut_option": "FOI NBB PDF + debt/BEI + Hydria redevances 2025 + Brugel MFC/FRT",
                "source_id": "src_vivaqua_jr2025_cw",
                "confidence": "medium",
                "hierarchy_path": "Belgie>BCR>Water>Vivaqua>JR2025_L5",
                "notes": (
                    "tick1951; Medium CW+Upswitch YE2025 refresh after YE2024-only; "
                    "do not redo Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/AIEG/Synergrid/Synatom/Atrias/RESA/Fluxys*/ETB/Elia/Enodia/BNO/SWDE"
                ),
            }
        ],
    )

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

if "lb_vivaqua_omzet_jump_356_0m_pnl_jump_4_64m_assets_1_76bn_jr2025" not in existing_lb:
    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_vivaqua_omzet_jump_356_0m_pnl_jump_4_64m_assets_1_76bn_jr2025",
                "name": "Vivaqua omzet JUMP 356.0m / pnl JUMP 4.64m turnaround / assets 1.76bn (BCR water YE2025)",
                "level": "L5",
                "type": "water_igs_dual",
                "hierarchy_path": "Belgie>BCR>Water>Vivaqua>JR2025_L5",
                "annual_cost_eur": "355999963",
                "total_cost_eur": "355999963",
                "tco_notes": (
                    "omzet 355999963 JUMP +9.23pct bruto 313200862 pnl JUMP 4638914 turnaround "
                    "equity 569707719 assets 1759637813 DROP EBITDA 131058980 FTE 1260.3; debt Unknown"
                ),
                "confidence": "medium",
                "source_id": "src_vivaqua_jr2025_cw",
                "beneficiaries": "BCR communes / Brussels water users",
                "stated_goal": "BCR water production distribution assainissement",
                "measured_outcome": "CW+Upswitch YE2025 live; pnl turnaround after YE2024 loss; primary NBB PDF unresolved",
                "absurdity_score": "4.5",
                "cost_score": "7.5",
                "difficulty": "4.0",
                "priority_index": "5.4",
                "cut_proposal": "Publish NBB PDF + debt/BEI + Hydria redevances + Brugel MFC/FRT recon",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1951; Medium CW+Upswitch; leftover after Belgoprocess EVERY-10; not TE-additive pure-waste top10",
            }
        ],
    )

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "vivaqua": {
            "foi_postal": "Keizerinlaan 17-19 1000 Brussel",
            "website": "https://www.vivaqua.be",
            "notes": (
                "tick172 YE2024; tick1951 YE2025 Medium CW+Upswitch KBO 0202.962.701 Actief CV; "
                "omzet JUMP 356.0m pnl JUMP 4.64m turnaround equity 569.7m assets 1.760bn DROP "
                "EBITDA 131.1m FTE 1260.3; FOI gap_vivaqua_nbb_pdf_debt_bei_hydria_l5; "
                "dual SWDE/Aquafin/CILE; Brugel MFC"
            ),
        }
    },
)

existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

if "gap_vivaqua_nbb_pdf_debt_bei_hydria_l5" not in existing_foi:
    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": "gap_vivaqua_nbb_pdf_debt_bei_hydria_l5",
                "hierarchy_path": "Belgie>BCR>Water>Vivaqua>nbb_pdf_debt_L5",
                "entity_id": "vivaqua",
                "what_is_missing": (
                    "NBB deposit PDF body for YE2025; debt/BEI/BCR guarantee update recon to "
                    "assets 1759637813 / equity 569707719; Hydria assainissement redevances 2025; "
                    "Brugel MFC/FRT vs omzet 355999963; FTE/wage aggregate"
                ),
                "why_it_matters": (
                    "Largest BCR water dual YE2025 refresh after Belgoprocess — "
                    "356m omzet / 1.76bn assets with pnl turnaround needs statutory PDF + debt path"
                ),
                "priority": "8",
                "recipient_body": "Vivaqua CV",
                "recipient_email": "",
                "recipient_postal": "Keizerinlaan 17-19 1000 Brussel (cc Brugel / BCR)",
                "draft_letter_path": "docs/doge/foi/drafts/gap_vivaqua_nbb_pdf_debt_bei_hydria_l5.md",
                "status": "ready",
                "date_ready": "2026-08-27",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_vivaqua_jr2025_omzet",
                "linked_leaderboard_id": "lb_vivaqua_omzet_jump_356_0m_pnl_jump_4_64m_assets_1_76bn_jr2025",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1951; human-send only; Medium CW+Upswitch; next every-10 1960",
            }
        ],
    )

# close stale open twin rq_1950 + finish rq_1951
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_1950" and (row.get("status") or "") == "open":
        row["status"] = "done"
        row["notes"] = (
            (row.get("notes") or "")
            + "; superseded twin — tick1950 EVERY-10+Belgoprocess already done on main"
        )
        row["updated_utc"] = TS
    if row["task_id"] == "rq_1951":
        row.update(
            {
                "status": "done",
                "entity_id": "vivaqua",
                "title": "Leftover dual residual hole-fill after Belgoprocess — Vivaqua YE2025 Medium",
                "instructions": (
                    "Completed: Vivaqua leftover BCR water dual after Belgoprocess EVERY-10; "
                    "KBO 0202.962.701; YE2025 Medium Companyweb+Upswitch; sourced euros omzet 355999963 JUMP "
                    "pnl 4638914 JUMP turnaround equity 569707719 assets 1759637813 EBITDA 131058980 FTE 1260.3; "
                    "FOI ready gap_vivaqua_nbb_pdf_debt_bei_hydria_l5; "
                    "NOT Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/AIEG/Synergrid/Synatom/Atrias/RESA/Fluxys*/ETB/Elia/Enodia/BNO/SWDE"
                ),
                "blocked_gap_id": "gap_vivaqua_nbb_pdf_debt_bei_hydria_l5",
                "updated_utc": TS,
                "notes": (
                    "tick1951 Vivaqua after Belgoprocess EVERY-10; Medium CW+Upswitch omzet JUMP 356.0m "
                    "pnl JUMP 4.64m assets 1.76bn; FOI ready not sent; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_1952; next every-10 1960"
                ),
            }
        )

with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

has_1952 = any(row["task_id"] == "rq_1952" for row in rows)
if not has_1952:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1952",
                "title": "Leftover dual residual hole-fill after Vivaqua (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / otherHVZ-IGS)",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "Vlaanderen>leftover_dual",
                "entity_id": "",
                "instructions": (
                    "Tick 1952 after 1951 Vivaqua. Prefer leftover AGB/APB if PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused HVZ/IGS/energy/water. Do NOT redo Vivaqua, Belgoprocess, "
                    "Laborelec, CILE, NIRAS, Bel V, Dijk92, AIEG, Synergrid, Synatom, Atrias, RESA, Sibelga, ORES, "
                    "Fluxys*, ETB, Elia, Enodia, BNO, Pipelink, SWDE."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "spawned after tick1951; next every-10 1960",
            }
        ],
    )

# FOI draft tick label
draft = ROOT / "docs/doge/foi/drafts/gap_vivaqua_nbb_pdf_debt_bei_hydria_l5.md"
if draft.exists():
    txt = draft.read_text(encoding="utf-8")
    txt = txt.replace("**tick:** 1950 EVERY-10", "**tick:** 1951 (NOT every-10; next every-10 is **1960**)")
    txt = txt.replace("after Laborelec EVERY-10", "after Belgoprocess EVERY-10")
    draft.write_text(txt, encoding="utf-8")

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
            "last_unit_id": "rq_1951",
            "ticks_completed": "1951",
            "paused": "no",
            "notes": (
                "tick1951 leftover Vivaqua 0202.962.701 Medium CW+Upswitch (omzet JUMP 356.0m "
                "pnl JUMP 4.64m turnaround equity 569.7m assets 1.760bn EBITDA 131.1m FTE 1260.3); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1952; next every-10 1960; continuous hole_fill"
            ),
        }
    )

log_block = """

## Tick 1951 - 2026-08-27T22:30:00Z - rq_1951 Vivaqua (omzet JUMP 356.0m / pnl JUMP 4.64m / Medium)

- Unit: **rq_1951** leftover dual after concurrent **rq_1950 EVERY-10 + Belgoprocess** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took leftover **Vivaqua** YE2025 refresh (KBO **0202.962.701**; Keizerinlaan 17-19 Brussel; BCR water dual; only YE2024 mined at tick172). Do not redo Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/AIEG/Synergrid/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE.
- Primary hunt: NBB deposit PDF unresolved. **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0202962701/vivaqua) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/vivaqua-0202962701) (neerlegging **11.06.2026**; YE **31.12.2025**): omzet **EUR355,999,963** (**JUMP +9.23%**); bruto **EUR313,200,862**; PnL **EUR4,638,914** (**JUMP turnaround** vs LOSS 0.86m); equity **EUR569,707,719**; assets **EUR1,759,637,813** (**DROP** vs 1.804bn); EBITDA **EUR131,058,980**; FTE **1260.3**; debt **Unknown**.
- Wrote: sources (+3); budgets (+7); commitments (+1); leaderboard (+1); entities (updated vivaqua); foi + draft gap_vivaqua_nbb_pdf_debt_bei_hydria_l5; rq_1951=done + stale open rq_1950 twin closed + rq_1952 open; loop_state ticks=1951.
- FOI opened: NBB PDF + debt/BEI + Hydria/Brugel (**ready**, human-send only).
- NOT every-10 (**1950 EVERY-10 already done with Belgoprocess**; next every-10 is **1960**). Next: rq_1952 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / otherHVZ-IGS).
"""
with (ROOT / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1951 write OK")
