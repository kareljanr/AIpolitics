# -*- coding: utf-8 -*-
"""tick2173 Langerheide WZC Haacht YE2025 Medium — omzet DROP 1.84m / pnl JUMP +60%."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T03:40:00Z"
ENTITY = "vzw_wzc_langerheide_haacht"
OMZET = 1842966
BRUTO = 3143509
PNL = 106076
EQUITY = 931790
FTE = 43.2
OMZET_PY = 1873019
BRUTO_PY = 3089043
PNL_PY = 66122
EQUITY_PY = 825714


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
        if row.get("task_id") == "rq_2173":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "leftover dual — Langerheide WZC Haacht YE2025 Medium "
                "(omzet DROP 1.84m / pnl JUMP +60%)"
            )
            row["notes"] = (
                "tick2173 Langerheide 0864.332.554 Medium; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2174; next every-10 2180"
            )
            row["entity_id"] = ENTITY
            row["blocked_gap_id"] = (
                "gap_langerheide_nbb_pdf_assets_debt_omzet_drop_pnl_jump_bruto_gt_omzet_matrix_l5"
            )
    ids = {row.get("task_id") for row in rows}
    if "rq_2174" not in ids:
        rows.append(
            {
                "task_id": "rq_2174",
                "title": (
                    "leftover dual hole-fill after Langerheide — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2174 after Langerheide YE2025 Medium (omzet DROP 1.84m / "
                    "pnl JUMP +60% / bruto 3.14m). Prefer leftover AGB/APB if JR2025 PDF "
                    "live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                    "unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo Langerheide/"
                    "Cur@-Z/Het Dorp/De Vlietoever/Abdij Affligem/Aaigem/Anima*/"
                    "Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis. Optional: Hof ter "
                    "Lande/Stil Geluk/WZN Edegem if JR2025."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2173 Langerheide; FARO/AIESH/REW still YE2024; "
                    "next every-10 2180"
                ),
            }
        )
        print("spawn rq_2174")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2173=done")


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
        "last_unit_id": "rq_2173",
        "ticks_completed": "2173",
        "paused": "no",
        "notes": (
            "tick2173 leftover Langerheide WZC Haacht 0864.332.554 Medium (omzet DROP "
            "1.84m -1.6%; bruto JUMP 3.14m; pnl JUMP 106k +60%; equity JUMP 932k; FTE "
            "43.2; 1 VE ROB 87.301); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next "
            "rq_2174; next every-10 2180; continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2173")


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_langerheide_jr2025_cw_nl",
            title="Companyweb NL Langerheide Woon En Zorgcentrum YE2025 statutory",
            url="https://www.companyweb.be/nl/0864332554/langerheide-woon-en-zorgcentrum",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2173; YE2025 omzet 1842966 pnl 106076 equity 931790 bruto 3143509 "
                "FTE 43.2; neerlegging 04.07.2026; assets/debt Unknown"
            ),
        ),
        dict(
            source_id="src_langerheide_jr2025_cw_en",
            title="Companyweb EN Langerheide Woon En Zorgcentrum YE2025 statutory",
            url="https://www.companyweb.be/en/0864332554",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2173; EN mirror YE2025 Medium; filed 04-07-2026; Last balance sheet year 2025",
        ),
        dict(
            source_id="src_langerheide_jr2025_cw_fr",
            title="Companyweb FR Langerheide Woon En Zorgcentrum YE2025 statutory",
            url="https://www.companyweb.be/fr/0864332554",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2173; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_langerheide_kbo_2173",
            title="KBO Langerheide Woon En Zorgcentrum 0864.332.554 Actief VZW Haacht 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0864332554",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2173; Actief VZW sinds 27.06.2003; Langerheide 7 3150 Haacht; 1 VE; "
                "RSZ/BTW NACE 87.301 ROB; KBO email/web empty"
            ),
        ),
        dict(
            source_id="src_langerheide_foi_contact_2173",
            title="Langerheide FOI contact postal + tel +32 16 60 01 04 (Goudengids)",
            url="https://www.goudengids.be/bedrijven/Haacht/woonzorgcentra/",
            publisher="Goudengids / Langerheide WZC",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes=(
                "tick2173; postal Langerheide 7 3150 Haacht; tel +3216600104; KBO email "
                "empty; secondary directory phone Medium"
            ),
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Langerheide Woon En Zorgcentrum VZW (Haacht)",
            name_fr="Langerheide Woon En Zorgcentrum ASBL (Haacht)",
            name_en="Langerheide residential care centre non-profit (Haacht)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="",
            foi_email="",
            foi_postal="Langerheide 7, 3150 Haacht",
            notes=(
                "tick2173 YE2025 Medium CW NL+EN+FR + Strong KBO 0864.332.554 Actief VZW "
                "1 VE NACE 87.301 ROB; omzet DROP 1.84m (−1.60%) bruto JUMP 3.14m "
                "pnl JUMP 106076 (+60.42%) equity JUMP 932k FTE 43.2; assets/debt Unknown; "
                "FOI gap_langerheide_nbb_pdf_assets_debt_omzet_drop_pnl_jump_bruto_gt_omzet_"
                "matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                "TE-additive of 348bn; tel +32 16 60 01 04 (Goudengids Medium)"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_langerheide_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2173; Medium CW; omzet DROP -1.60% vs YE2024 1873019; bruto > omzet",
    ),
    (
        "bud_langerheide_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2173; Medium CW; bruto JUMP +1.76% vs YE2024 3089043; exceeds omzet",
    ),
    (
        "bud_langerheide_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2173; Medium CW; pnl JUMP +60.42% vs YE2024 66122",
    ),
    (
        "bud_langerheide_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2173; Medium CW; equity JUMP +12.85% vs YE2024 825714",
    ),
    (
        "bud_langerheide_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 43.2",
        "tick2173; Medium CW; FTE 43.2; assets/debt Unknown; YE2024 FTE not extracted",
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
                source_id="src_langerheide_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_langerheide_jr2025_statutory_wzc_omzet_drop_pnl_jump",
            title=(
                "Langerheide WZC Haacht YE2025 leftover dual "
                "(omzet DROP 1.84m / pnl JUMP +60%)"
            ),
            entity_id=ENTITY,
            beneficiary="WZC/ROB clients Haacht Langerheide",
            legal_basis="VZW ROB (KBO 0864.332.554; Actief; 1 VE; NACE 87.301)",
            decision_date="2026-07-04",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=(
                '{"2025_omzet":1842966,"2025_bruto":3143509,"2025_pnl":106076,'
                '"2025_equity":931790,"2025_fte":43.2,'
                '"2024_omzet":1873019,"2024_bruto":3089043,"2024_pnl":66122,'
                '"2024_equity":825714}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0864332554",
            stated_goal="Residential elderly care ROB Haacht (~68 beds secondary)",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; explain bruto>omzet other-income; "
                "RIZIV/dagprijs/gemeente toelage matrix"
            ),
            source_id="src_langerheide_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Haacht>Langerheide>JR2025_statutory_L5",
            notes=(
                "tick2173; Medium CW; omzet primary envelope; bruto 3.14m > omzet; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        )
    ],
)

# pi = 0.55*4.2 + 0.35*4.5 + 0.10*5.0 = 2.31+1.575+0.5 = 4.385 ≈ 4.4
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_langerheide_omzet_drop_1_84m_pnl_jump_jr2025",
            name="Langerheide omzet DROP 1.84m / pnl JUMP +60% / bruto>omzet (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Haacht>Langerheide>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                "CW omzet envelope 1.84m / bruto 3.14m / 43.2 FTE; pnl JUMP +60% with "
                "slight omzet DROP; equity JUMP +12.9%; assets/debt Unknown pending NBB PDF"
            ),
            confidence="medium",
            source_id="src_langerheide_jr2025_cw_en",
            beneficiaries="WZC clients Haacht Langerheide",
            stated_goal="Residential elderly care ROB Haacht",
            measured_outcome=(
                "omzet DROP -1.60%; bruto JUMP +1.76%; pnl JUMP +60.42%; "
                "equity JUMP +12.85%; FTE 43.2; bruto>omzet"
            ),
            absurdity_score="4.5",
            cost_score="4.2",
            difficulty="3.5",
            priority_index="4.4",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose other-income behind "
                "bruto>omzet; RIZIV/toelage split"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2173; Medium CW; FOI gap_langerheide_nbb_pdf_assets_debt_omzet_drop_"
                "pnl_jump_bruto_gt_omzet_matrix_l5; stall FARO/AIESH/REW YE2024"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_langerheide_nbb_pdf_assets_debt_omzet_drop_pnl_jump_bruto_gt_omzet_matrix_l5",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Haacht>Langerheide>NBB_PDF_assets_debt_bruto_gt_omzet",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "explain bruto EUR3.14m > omzet EUR1.84m (other operating income / 73 codes); "
                "omzet DROP −1.6% with pnl JUMP +60%; RIZIV/dagprijs/gemeente Haacht toelage "
                "split; capacity (~68 beds secondary) vs FTE 43.2"
            ),
            why_it_matters=(
                "Medium CW shows Haacht ROB VZW with published omzet 1.84m but bruto 3.14m "
                "and no balanstotaal/assets/debt — public care euro opacity"
            ),
            priority="8",
            recipient_body="Langerheide Woon En Zorgcentrum VZW",
            recipient_email="",
            recipient_postal="Langerheide 7, 3150 Haacht (tel +32 16 60 01 04 Goudengids Medium)",
            draft_letter_path=(
                "docs/doge/foi/drafts/gap_langerheide_nbb_pdf_assets_debt_omzet_drop_"
                "pnl_jump_bruto_gt_omzet_matrix_l5.md"
            ),
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_langerheide_jr2025_statutory_wzc_omzet_drop_pnl_jump",
            linked_leaderboard_id="lb_langerheide_omzet_drop_1_84m_pnl_jump_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "tick2173; ready NOT sent; Medium CW + Strong KBO; postal FOI (KBO email "
                "empty); next every-10 2180"
            ),
        )
    ],
)

update_rq()
write_loop_state()
print("DONE apply")
