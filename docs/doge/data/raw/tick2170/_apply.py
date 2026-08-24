# -*- coding: utf-8 -*-
"""tick2170 EVERY-10 + Abdij Affligem YE2025 Medium leftover dual."""
import csv
from pathlib import Path
from datetime import datetime, timezone

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T02:40:00Z"
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


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
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
    print("append", path.name, "+", added)


def update_rq():
    path = ROOT / "research_queue.csv"
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        rows = list(r)
        cols = r.fieldnames
    for row in rows:
        if row.get("task_id") == "rq_2170":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "EVERY-10 + leftover dual — Abdij Affligem YE2025 Medium "
                "(omzet DROP 565k / pnl DROP -67%)"
            )
            row["notes"] = (
                "tick2170 EVERY-10 + Abdij Affligem 0400.371.161 Medium; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis retail skip; "
                "next rq_2171; next every-10 2180"
            )
            row["entity_id"] = ENTITY
    # spawn rq_2171 if missing
    ids = {row.get("task_id") for row in rows}
    if "rq_2171" not in ids:
        rows.append(
            {
                "task_id": "rq_2171",
                "title": (
                    "leftover dual hole-fill after Abdij Affligem — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2171 after EVERY-10@2170 Abdij Affligem YE2025 Medium "
                    "(omzet DROP 565k / pnl DROP -67%). Prefer leftover AGB/APB if "
                    "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
                    "if YE2025, else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT "
                    "redo Abdij Affligem/Sint-Vincentius Aaigem/Sint Lodewijk/"
                    "Lork Hoeselt/Anima stack/Zorg-Saam/Sint-Bernardus/Ruggeveld/"
                    "Salvator/Boterlaarhof. Skip Melis Home (retail NACE 47)."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2170 EVERY-10 Abdij Affligem; "
                    "FARO/AIESH/REW still YE2024; next every-10 2180"
                ),
            }
        )
        print("spawn rq_2171")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2170=done")


def write_loop_state():
    path = ROOT / "loop_state.csv"
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)
        cols = r.fieldnames
    rows[0] = {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": TS,
        "last_unit_id": "rq_2170",
        "ticks_completed": "2170",
        "paused": "no",
        "notes": (
            "tick2170 EVERY-10 + leftover Abdij Affligem 0400.371.161 Medium "
            "(omzet DROP 565k; bruto DROP 335k; pnl DROP 43k; equity JUMP 6.15m; "
            "FTE 2.8; heritage VZW wine/flour); AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2171; next every-10 2180; "
            "continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2170")


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
            notes=(
                "tick2170 EVERY-10; YE2025 omzet 564963 pnl 42658 equity 6149175 "
                "bruto 335127 FTE 2.8; neerlegging 02.07.2026; assets/debt Unknown"
            ),
        ),
        dict(
            source_id="src_abdij_affligem_jr2025_cw_en",
            title="Companyweb EN Abdij Affligem YE2025 statutory",
            url="https://www.companyweb.be/en/0400371161",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2170 EVERY-10; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025",
        ),
        dict(
            source_id="src_abdij_affligem_jr2025_cw_fr",
            title="Companyweb FR Abdij Affligem YE2025 statutory",
            url="https://www.companyweb.be/fr/0400371161",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2170 EVERY-10; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_abdij_affligem_kbo_2170",
            title="KBO Abdij Affligem 0400.371.161 Actief VZW Affligem",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0400371161",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2170; Actief VZW; Abdijstraat 6 1790 Affligem; 1 VE; "
                "RSZ 94.999; BTW 11.020 wine + 10.610 flour; email empty"
            ),
        ),
        dict(
            source_id="src_abdij_affligem_foi_contact_2170",
            title="Abdij Affligem FOI contact info@abdijaffligem.be",
            url="https://abdijaffligem.wordpress.com/contact/",
            publisher="Abdij Affligem",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2170; info@abdijaffligem.be; tel +32 53 66 70 25; Abdijstraat 6 Affligem",
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Abdij Affligem VZW (Benedictijnen / Hekelgem)",
            name_fr="Abbaye d'Affligem ASBL (Bénédictins / Hekelgem)",
            name_en="Affligem Abbey non-profit (Benedictine / Hekelgem)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://abdijaffligem.wordpress.com/",
            foi_email="info@abdijaffligem.be",
            foi_postal="Abdijstraat 6, 1790 Affligem",
            notes=(
                "tick2170 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0400.371.161 "
                "Actief VZW 1 VE RSZ 94.999 BTW wine/flour; omzet DROP 564963 (-15.37%) "
                "bruto DROP 335127 (-27.72%) pnl DROP 42658 (-66.52%) equity JUMP 6149175 "
                "FTE 2.8; assets/debt Unknown; FOI gap_abdij_affligem_nbb_pdf_assets_debt_"
                "omzet_drop_pnl_drop_subsidy_matrix_l5; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; Melis retail skip; not TE-additive of 348bn"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_abdij_affligem_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2170; Medium CW; omzet DROP -15.37% vs YE2024 667571",
    ),
    (
        "bud_abdij_affligem_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2170; Medium CW; bruto DROP -27.72% vs YE2024 463679",
    ),
    (
        "bud_abdij_affligem_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2170; Medium CW; pnl DROP -66.52% vs YE2024 127418",
    ),
    (
        "bud_abdij_affligem_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2170; Medium CW; equity JUMP +0.70% vs YE2024 6106517",
    ),
    (
        "bud_abdij_affligem_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 2.8",
        "tick2170; Medium CW; assets/debt Unknown pending NBB PDF",
    ),
]:
    append_csv(
        ROOT / "budgets.csv",
        [
            dict(
                budget_id=bid,
                entity_id=ENTITY,
                year="2025",
                amount_eur=str(amount),
                amount_min_eur=str(amount),
                amount_max_eur=str(amount),
                basis=basis,
                source_id="src_abdij_affligem_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_abdij_affligem_jr2025_statutory_heritage_omzet_drop_565k",
            title=(
                "Abdij Affligem YE2025 leftover dual "
                "(omzet DROP 565k / pnl DROP -67%)"
            ),
            entity_id=ENTITY,
            beneficiary="Abbey visitors / heritage / wine-flour residual Affligem",
            legal_basis="VZW (KBO 0400.371.161; Actief; 1 VE; RSZ 94.999; BTW 11.020/10.610)",
            decision_date="2026-07-02",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=(
                '{"2025_omzet":564963,"2025_bruto":335127,"2025_pnl":42658,'
                '"2025_equity":6149175,"2025_fte":2.8,'
                '"2024_omzet":667571,"2024_bruto":463679,"2024_pnl":127418,'
                '"2024_equity":6106517}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0400371161",
            stated_goal="Benedictine abbey heritage + wine/flour residual Affligem",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; disclose subsidy vs commercial "
                "wine/flour split; Affligem municipality/VL heritage matrix"
            ),
            source_id="src_abdij_affligem_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>JR2025_statutory_L5",
            notes=(
                "tick2170 EVERY-10; Medium CW; omzet primary envelope; assets/debt Unknown; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "named deferred leftover after Aaigem"
            ),
        )
    ],
)

# priority ~ 0.55*3.5 + 0.35*5.2 + 0.10*(10-3.5) = 1.925 + 1.82 + 0.65 = 4.395 ~ 4.4
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_abdij_affligem_omzet_565k_pnl_drop_jr2025",
            name="Abdij Affligem omzet DROP 565k / pnl DROP -67% (YE2025)",
            level="L5",
            type="heritage_vzw_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                "CW omzet envelope 565k / 2.8 FTE; pnl DROP -66.5%; bruto DROP -27.7%; "
                "equity JUMP 0.7% to 6.15m; assets/debt Unknown pending NBB PDF"
            ),
            confidence="medium",
            source_id="src_abdij_affligem_jr2025_cw_en",
            beneficiaries="Abbey / heritage / Affligem visitors",
            stated_goal="Benedictine abbey operations Affligem",
            measured_outcome=(
                "omzet DROP -15.37%; bruto DROP -27.72%; pnl DROP -66.52%; "
                "equity JUMP +0.70%; FTE 2.8"
            ),
            absurdity_score="5.2",
            cost_score="3.5",
            difficulty="3.5",
            priority_index="4.4",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose public subsidy vs "
                "wine/flour commercial split; Affligem/VL heritage matrix"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2170 EVERY-10; Medium CW; FOI gap_abdij_affligem_nbb_pdf_assets_debt_"
                "omzet_drop_pnl_drop_subsidy_matrix_l5; stall FARO/AIESH/REW YE2024"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Affligem>AbdijAffligem>NBB_PDF_assets_debt_subsidy",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "omzet split wine/flour vs giften vs subsidies; explanation of omzet DROP "
                "EUR565k (−15%) / bruto DROP (−28%) / pnl DROP EUR43k (−67%); named "
                "overheidssteun/toelagen Affligem/VL/erfgoed ≥1k YE2024-25"
            ),
            why_it_matters=(
                "Medium CW shows EUR565k heritage VZW with sharp pnl DROP and 6.15m equity "
                "— no balanstotaal/assets/debt; subsidy vs commercial opacity material for FOI"
            ),
            priority="8",
            recipient_body="Abdij Affligem VZW",
            recipient_email="info@abdijaffligem.be",
            recipient_postal="Abdijstraat 6, 1790 Affligem",
            draft_letter_path="docs/doge/foi/drafts/gap_abdij_affligem_nbb_pdf_assets_debt_omzet_drop_pnl_drop_subsidy_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_abdij_affligem_jr2025_statutory_heritage_omzet_drop_565k",
            linked_leaderboard_id="lb_abdij_affligem_omzet_565k_pnl_drop_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2170 EVERY-10; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        )
    ],
)

update_rq()
write_loop_state()
print("DONE apply unit")
