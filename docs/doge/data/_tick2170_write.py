# -*- coding: utf-8 -*-
"""Tick 2170 EVERY-10 + Abdij Affligem YE2025 leftover dual."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
TS = "2026-08-26T02:40:00Z"
TICK = 2170

ENTITY = "vzw_abdij_affligem"
OMZET = 564963
BRUTO = 335127
PNL = 42658
EQUITY = 6149175
FTE = 2.8
OMZET_PY = 667571
BRUTO_PY = 463679
PNL_PY = 127418
EQUITY_PY = 6106517
FTE_PY = 2.2


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added, "total", len(existing))


def update_csv_rows(path, key, updates):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    n = 0
    for row in rows:
        if row.get(key) in updates:
            row.update(updates[row[key]])
            n += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("update", path.name, n)


# --- sources ---
append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_abdij_affligem_jr2025_cw_nl",
            title="Companyweb NL Abdij Affligem YE2025 statutory",
            url="https://www.companyweb.be/nl/0400371161/abdij-affligem",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2170 EVERY-10; YE2025 omzet 564963 DROP pnl DROP 42658 equity 6149175 bruto 335127 FTE 2.8; neerlegging 02.07.2026; assets/debt Unknown; raw tick2170/",
        ),
        dict(
            source_id="src_abdij_affligem_jr2025_cw_en",
            title="Companyweb EN Abdij Affligem YE2025 statutory",
            url="https://www.companyweb.be/en/0400371161/abdij-affligem",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2170; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; Medium-sized 2.8 FTE; raw tick2170/",
        ),
        dict(
            source_id="src_abdij_affligem_jr2025_cw_fr",
            title="Companyweb FR Abdij Affligem YE2025 statutory",
            url="https://www.companyweb.be/fr/0400371161/abdij-affligem",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2170; FR mirror YE2025 Medium; Dernier bilan 2025; raw tick2170/",
        ),
        dict(
            source_id="src_abdij_affligem_kbo_2170",
            title="KBO Abdij Affligem 0400.371.161 Actief VZW Affligem",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0400371161",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2170; Actief VZW; Abdijstraat 6 1790 Affligem; 1 VE; NACE BTW 11.020/10.610 + RSZ 94.999; sinds 01.01.1968",
        ),
        dict(
            source_id="src_abdij_affligem_site_contact_2170",
            title="Abdij Affligem site contact info@abdijaffligem.be FOI channel",
            url="https://abdijaffligem.wordpress.com/",
            publisher="Abdij Affligem",
            accessed_date="2026-08-26",
            source_class="official_org",
            notes="tick2170; FOI info@abdijaffligem.be; tel 053 66 70 25; Abdijstraat 6 1790 Affligem",
        ),
    ],
)

# --- budgets ---
budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_abdij_affligem_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2170; Medium CW; omzet DROP -15.37% vs YE2024 667571",
    ),
    (
        "bud_abdij_affligem_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2170; Medium CW; bruto DROP -27.72% vs YE2024 463679",
    ),
    (
        "bud_abdij_affligem_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2170; Medium CW; pnl DROP -66.52% vs YE2024 127418",
    ),
    (
        "bud_abdij_affligem_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2170; Medium CW; equity JUMP +0.70% vs YE2024 6106517",
    ),
    (
        "bud_abdij_affligem_fte_jr2025_statutory",
        "2025",
        FTE,
        "CW social-balance FTE / Employees 2.8",
        "tick2170; Medium CW; FTE JUMP vs YE2024 2.2; assets/debt Unknown pending NBB PDF",
    ),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year=year,
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id="src_abdij_affligem_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

# --- commitments ---
append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_abdij_affligem_jr2025_statutory_omzet_drop_pnl_drop",
            title="Abdij Affligem YE2025 leftover dual (omzet DROP 565k / pnl DROP 43k / Medium)",
            entity_id=ENTITY,
            beneficiary="Abdij Affligem Benedictine community / gastenverblijf / religieus centrum",
            legal_basis="VZW/ASBL (KBO 0400.371.161; Actief; 1 VE; NACE wine/milling + 94.999 associations)",
            decision_date="2026-07-02",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": OMZET,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": OMZET_PY,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0400371161/abdij-affligem",
            stated_goal="Benedictine abbey Affligem — hospitality / religious centre / heritage",
            cut_option="Publish NBB PDF assets/debt FOI; map public erfgoed/cultuur subsidies vs commercial omzet DROP",
            source_id="src_abdij_affligem_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>JR2025_statutory_L5",
            notes="tick2170 EVERY-10; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis Home FREE deferred retail micro; not TE-additive of 348bn; DISTINCT Sint-Vincentius Aaigem/Sint Lodewijk/Anima*/Avondvrede/Zorg-Saam",
        )
    ],
)

# pi = 0.55*1.5 + 0.35*5.8 + 0.10*6.5 = 0.825 + 2.03 + 0.65 = 3.505
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_abdij_affligem_omzet_drop_565k_pnl_drop_jr2025",
            name="Abdij Affligem omzet DROP 565k / pnl DROP -67% / equity 6.15m (YE2025)",
            level="L5",
            type="vzw_abbey_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 565k DROP -15.4% with pnl DROP -66.5%; equity stable 6.15m; FTE 2.8; assets/debt Unknown; public subsidy matrix FOI",
            confidence="medium",
            source_id="src_abdij_affligem_jr2025_cw_en",
            beneficiaries="Abdij Affligem community / guests / heritage visitors",
            stated_goal="Benedictine abbey hospitality and religious centre Affligem",
            measured_outcome="omzet DROP -15.37%; bruto DROP -27.72%; pnl DROP -66.52%; equity JUMP +0.70%; FTE JUMP 2.8",
            absurdity_score="5.8",
            cost_score="1.5",
            difficulty="3.5",
            priority_index="3.51",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; map erfgoed/cultuur/gemeente subsidies vs omzet DROP path",
            status="open",
            struck_reason="",
            notes="tick2170 EVERY-10; Medium CW; FOI gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Abdij Affligem VZW (Benedictijnen / Affligem)",
            name_fr="Abbaye d'Affligem ASBL",
            name_en="Affligem Abbey non-profit (Benedictine)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://abdijaffligem.wordpress.com/",
            foi_email="info@abdijaffligem.be",
            foi_postal="Abdijstraat 6, 1790 Affligem",
            notes="tick2170 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0400.371.161 Actief VZW 1 VE; omzet DROP 565k (-15.37%) bruto DROP 335k pnl DROP 43k (-66.52%) equity JUMP 6.15m FTE JUMP 2.8; assets/debt Unknown; neerlegging 02.07.2026; NACE wine/milling + 94.999; FOI gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis Home FREE deferred; DISTINCT Sint-Vincentius Aaigem/Sint Lodewijk/Anima*/Avondvrede/Zorg-Saam",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>NBB_PDF_assets_debt_omzet_drop_pnl_drop_subsidy",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); public erfgoed/cultuur/gemeente subsidy matrix; omzet DROP and pnl DROP explanation; code70 split gastenverblijf vs subsidies",
            why_it_matters="Medium CW shows abbey VZW with material omzet/pnl DROP and no balanstotaal/assets/debt published — residual dual/public-adjacent opacity",
            priority="8",
            recipient_body="Abdij Affligem VZW",
            recipient_email="info@abdijaffligem.be",
            draft_path="docs/doge/foi/drafts/gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5.md",
            status="ready",
            filed_utc="",
            due_utc="",
            answer_utc="",
            notes="tick2170 EVERY-10; ready NOT sent; Medium CW YE2025; Strong KBO; Melis Home FREE deferred; stall FARO/AIESH/REW YE2024",
            created_utc=TS,
            updated_utc=TS,
        )
    ],
)

# --- research_queue: close 2170, open 2171 ---
update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2170": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": "gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5",
            "updated_utc": TS,
            "instructions": "Completed EVERY-10@2170 + leftover Abdij Affligem after Sint-Vincentius Aaigem; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Melis Home FREE deferred retail micro; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": "tick2170 EVERY-10 + Abdij Affligem Medium omzet DROP 565k (-15.37%) bruto DROP 335k pnl DROP 43k (-66.52%) equity JUMP 6.15m FTE 2.8; KBO Actief VZW 1 VE; FOI info@abdijaffligem.be; next rq_2171",
            "title": "EVERY-10 + leftover dual — Abdij Affligem YE2025 Medium (omzet DROP 565k / pnl DROP 43k)",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2171",
            title="leftover dual hole-fill after Abdij Affligem — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions="Tick 2171 leftover dual after rq_2170 Abdij Affligem YE2025 Medium (omzet DROP 565k). Prefer NON-stall live: AGB Bornem if JR2025; FARO/AIESH/REW if YE2025; else unused IGS-DSO-WZC-MRS with live sourced €. Melis Home FREE deferred (retail micro). Do not redo Affligem/Sint-Vincentius Aaigem/Sint Lodewijk/Anima*/Avondvrede/Zorg-Saam/Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork. Next EVERY-10 at 2180.",
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2170 EVERY-10 + Abdij Affligem; FARO/AIESH/REW still YE2024; next EVERY-10 at 2180",
        )
    ],
)

# --- loop_state ---
with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = "rq_2170"
        row["ticks_completed"] = "2170"
        row["paused"] = "no"
        row["notes"] = (
            "tick2170 EVERY-10 + leftover Abdij Affligem 0400.371.161 Medium (omzet DROP 565k; bruto DROP 335k; pnl DROP 43k; equity JUMP 6.15m; FTE 2.8); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis FREE deferred; next rq_2171; EVERY-10 next 2180; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2170")

print("DONE tick2170 CSV core")
