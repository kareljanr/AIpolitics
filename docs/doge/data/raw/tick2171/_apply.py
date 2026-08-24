# -*- coding: utf-8 -*-
"""tick2171 Woonzorg Het Dorp YE2025 Medium — omzet empty / FTE50 / equity NEG emeis shell."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T03:00:00Z"
ENTITY = "vzw_woonzorg_het_dorp"
EQUITY = -11976420
EQUITY_ABS = 11976420
PNL = -3557
BRUTO = -3557
FTE = 50.0
OMZET_PY = 4327853
PNL_PY = -2305763
BRUTO_PY = 1751348
EQUITY_PY = -11972862


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
        if row.get("task_id") == "rq_2171":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "leftover dual — Woonzorg Het Dorp YE2025 Medium "
                "(omzet empty / FTE 50 / equity NEG -12.0m / emeis)"
            )
            row["notes"] = (
                "tick2171 Het Dorp 0835.884.236 Medium; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2172; next every-10 2180"
            )
            row["entity_id"] = ENTITY
    ids = {row.get("task_id") for row in rows}
    if "rq_2172" not in ids:
        rows.append(
            {
                "task_id": "rq_2172",
                "title": (
                    "leftover dual hole-fill after Het Dorp — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2172 after Het Dorp YE2025 Medium (omzet empty / FTE 50 / "
                    "equity NEG -12m / emeis board). Prefer leftover AGB/APB if JR2025 "
                    "PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo Het Dorp/"
                    "Abdij Affligem/Aaigem/Sint Lodewijk/Lork Hoeselt/Anima stack/"
                    "Zorg-Saam/emeis Belgium. Optional: Ben Woonzorgnetwerk if YE2025; "
                    "Hof ter Lande/Stil Geluk/WZN Edegem if JR2025."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2171 Het Dorp; FARO/AIESH/REW still YE2024; "
                    "next every-10 2180"
                ),
            }
        )
        print("spawn rq_2172")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2171=done")


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
        "last_unit_id": "rq_2171",
        "ticks_completed": "2171",
        "paused": "no",
        "notes": (
            "tick2171 leftover Het Dorp 0835.884.236 Medium (omzet empty; bruto -3.6k; "
            "pnl -3.6k; equity NEG -12.0m; FTE 50; emeis board 0887.690.451); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2172; next every-10 2180; "
            "continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2171")


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_het_dorp_jr2025_cw_nl",
            title="Companyweb NL Woonzorg Het Dorp YE2025 statutory",
            url="https://www.companyweb.be/nl/0835884236",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2171; YE2025 omzet empty pnl -3557 equity -11976420 bruto -3557 "
                "FTE 50; YE2024 omzet 4327853 pnl -2305763; neerlegging 08.07.2026"
            ),
        ),
        dict(
            source_id="src_het_dorp_jr2025_cw_en",
            title="Companyweb EN Woonzorg Het Dorp YE2025 statutory",
            url="https://www.companyweb.be/en/0835884236",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2171; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025",
        ),
        dict(
            source_id="src_het_dorp_jr2025_cw_fr",
            title="Companyweb FR Woonzorg Het Dorp YE2025 statutory",
            url="https://www.companyweb.be/fr/0835884236",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2171; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_het_dorp_kbo_2171",
            title="KBO Woonzorg Het Dorp 0835.884.236 Actief VZW Ukkel emeis board",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0835884236",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2171; Actief VZW; Alsembergsesteenweg 1037 1180 Ukkel; 0 VE; "
                "bestuurder emeis Belgium 0887.690.451 since 08.12.2015"
            ),
        ),
        dict(
            source_id="src_het_dorp_foi_contact_2171",
            title="Woonzorg Het Dorp FOI contact hetdorp@emeis.com",
            url="https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
            publisher="emeis / Het Dorp",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2171; hetdorp@emeis.com; tel +32 11 60 98 00 (Helchteren site twin); Ukkel Alsembergsesteenweg 1037",
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Woonzorg Het Dorp VZW (Ukkel / emeis)",
            name_fr="Woonzorg Het Dorp ASBL (Uccle / emeis)",
            name_en="Het Dorp residential care non-profit (Uccle / emeis)",
            level="parastatal",
            parent_id="brussels_gov",
            community_language="bi",
            website="https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
            foi_email="hetdorp@emeis.com",
            foi_postal="Alsembergsesteenweg 1037, 1180 Ukkel",
            notes=(
                "tick2171 YE2025 Medium CW NL+EN+FR + Strong KBO 0835.884.236 Actief VZW "
                "0 VE; bestuurder emeis Belgium 0887.690.451; omzet empty (YE2024 4.33m) "
                "bruto -3557 pnl -3557 equity NEG -11976420 FTE 50; assets/debt Unknown; "
                "FOI gap_het_dorp_nbb_pdf_assets_debt_omzet_empty_fte50_equity_neg_emeis_matrix_l5; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "DISTINCT mined emeis Belgium holding"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_het_dorp_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025 NEG",
        "tick2171; Medium CW; equity NEG -11976420 flat vs YE2024 -11972862",
    ),
    (
        "bud_het_dorp_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2171; Medium CW; pnl -3557 narrowed from YE2024 LOSS -2305763",
    ),
    (
        "bud_het_dorp_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2171; Medium CW; bruto -3557 collapse from YE2024 1751348",
    ),
    (
        "bud_het_dorp_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 50",
        "tick2171; Medium CW; FTE 50 vs KBO 0 VE; assets/debt Unknown",
    ),
    (
        "bud_het_dorp_omzet_jr2024_comparative",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative (YE2025 unpublished)",
        "tick2171; Medium CW; YE2025 omzet empty; YE2024 omzet 4327853 scale reference",
    ),
]:
    append_csv(
        ROOT / "budgets.csv",
        [
            dict(
                budget_id=bid,
                entity_id=ENTITY,
                year="2025" if "jr2024" not in bid else "2024",
                amount_eur=str(amount),
                amount_min_eur=str(amount),
                amount_max_eur=str(amount),
                basis=basis,
                source_id="src_het_dorp_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_het_dorp_jr2025_statutory_emeis_shell_equity_neg_12m",
            title=(
                "Woonzorg Het Dorp YE2025 leftover dual "
                "(omzet empty / FTE 50 / equity NEG -12.0m / emeis)"
            ),
            entity_id=ENTITY,
            beneficiary="WZC clients Ukkel / emeis Belgium path",
            legal_basis=(
                "VZW (KBO 0835.884.236; Actief; 0 VE; bestuurder emeis Belgium 0887.690.451)"
            ),
            decision_date="2026-07-08",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(EQUITY_ABS),
            cash_by_year=(
                '{"2025_omzet":"empty","2025_bruto":-3557,"2025_pnl":-3557,'
                '"2025_equity":-11976420,"2025_fte":50,'
                '"2024_omzet":4327853,"2024_bruto":1751348,"2024_pnl":-2305763,'
                '"2024_equity":-11972862}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0835884236",
            stated_goal="Residential elderly care Ukkel (emeis shell)",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; explain omzet collapse + FTE 50 vs 0 VE; "
                "emeis related-party / wind-down matrix"
            ),
            source_id="src_het_dorp_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Brussel>Ukkel>WoonzorgHetDorp>JR2025_statutory_L5",
            notes=(
                "tick2171; Medium CW; equity ABS primary envelope (NEG stock); YE2025 flow "
                "near-zero; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn; DISTINCT emeis Belgium holding"
            ),
        )
    ],
)

# pi = 0.55*5.5 + 0.35*7.5 + 0.10*6.5 = 3.025+2.625+0.65 = 6.3
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_het_dorp_equity_neg_12m_omzet_empty_fte50_jr2025",
            name="Het Dorp equity NEG -12.0m / omzet empty / FTE 50 (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Brussel>Ukkel>WoonzorgHetDorp>JR2025",
            annual_cost_eur=str(EQUITY_ABS),
            total_cost_eur=str(EQUITY_ABS),
            tco_notes=(
                "CW equity NEG envelope 12.0m / FTE 50 / omzet empty; bruto -3.6k; "
                "pnl -3.6k; YE2024 omzet was 4.33m; emeis board; assets/debt Unknown"
            ),
            confidence="medium",
            source_id="src_het_dorp_jr2025_cw_en",
            beneficiaries="WZC clients Ukkel / emeis path",
            stated_goal="Residential elderly care Ukkel",
            measured_outcome=(
                "omzet empty vs YE2024 4.33m; bruto collapse -3.6k; pnl -3.6k; "
                "equity NEG -12.0m flat; FTE 50"
            ),
            absurdity_score="7.5",
            cost_score="5.5",
            difficulty="3.5",
            priority_index="6.3",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose wind-down vs emeis "
                "0887.690.451; explain FTE 50 with empty omzet / 0 VE"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2171; Medium CW; FOI gap_het_dorp_nbb_pdf_assets_debt_omzet_empty_"
                "fte50_equity_neg_emeis_matrix_l5; stall FARO/AIESH/REW YE2024"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_het_dorp_nbb_pdf_assets_debt_omzet_empty_fte50_equity_neg_emeis_matrix_l5",
            hierarchy_path="Brussel>Ukkel>WoonzorgHetDorp>NBB_PDF_assets_debt_emeis",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "omzet empty vs YE2024 EUR4.33m path; FTE 50 vs KBO 0 VE payroll; "
                "equity NEG EUR-11.98m related-party vs emeis Belgium 0887.690.451; "
                "Iriscare/RIZIV residual flows"
            ),
            why_it_matters=(
                "Medium CW shows emeis Ukkel WZC shell with 50 FTE + -EUR12m equity and "
                "empty omzet — balanstotaal/assets/debt unpublished; wind-down opacity"
            ),
            priority="8",
            recipient_body="Woonzorg Het Dorp VZW / emeis Belgium",
            recipient_email="hetdorp@emeis.com",
            recipient_postal="Alsembergsesteenweg 1037, 1180 Ukkel",
            draft_letter_path=(
                "docs/doge/foi/drafts/gap_het_dorp_nbb_pdf_assets_debt_omzet_empty_"
                "fte50_equity_neg_emeis_matrix_l5.md"
            ),
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_het_dorp_jr2025_statutory_emeis_shell_equity_neg_12m",
            linked_leaderboard_id="lb_het_dorp_equity_neg_12m_omzet_empty_fte50_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2171; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        )
    ],
)

update_rq()
write_loop_state()
print("DONE apply")
