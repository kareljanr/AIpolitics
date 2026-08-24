# -*- coding: utf-8 -*-
"""tick2172 Cur@-Z YE2025 Medium — omzet JUMP 18.0m / pnl DROP -63% / FTE JUMP."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T03:20:00Z"
ENTITY = "vzw_zorgnetwerk_curaz"
OMZET = 17978378
BRUTO = 18458106
PNL = 171555
EQUITY = 9245699
FTE = 246.4
OMZET_PY = 12186670
BRUTO_PY = 13637238
PNL_PY = 464714
EQUITY_PY = 6699589
FTE_PY = 185.7


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
        if row.get("task_id") == "rq_2172":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "leftover dual — Zorgnetwerk Cur@-Z YE2025 Medium "
                "(omzet JUMP 18.0m / pnl DROP -63% / FTE JUMP)"
            )
            row["notes"] = (
                "tick2172 Cur@-Z 0433.217.935 Medium; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; Ben already mined; next rq_2173; next every-10 2180"
            )
            row["entity_id"] = ENTITY
    ids = {row.get("task_id") for row in rows}
    if "rq_2173" not in ids:
        rows.append(
            {
                "task_id": "rq_2173",
                "title": (
                    "leftover dual hole-fill after Cur@-Z — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2173 after Cur@-Z YE2025 Medium (omzet JUMP 18.0m / pnl DROP "
                    "-63% / FTE JUMP 246). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo Cur@-Z/Het Dorp/Abdij/"
                    "Aaigem/Ben Woonzorgnetwerk/Sint Lodewijk/Lork Hoeselt/Anima/"
                    "Zorg-Saam/emeis. Optional: Hof ter Lande/Stil Geluk/WZN Edegem if JR2025."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2172 Cur@-Z; FARO/AIESH/REW still YE2024; "
                    "next every-10 2180"
                ),
            }
        )
        print("spawn rq_2173")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2172=done")


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
        "last_unit_id": "rq_2172",
        "ticks_completed": "2172",
        "paused": "no",
        "notes": (
            "tick2172 leftover Cur@-Z 0433.217.935 Medium (omzet JUMP 18.0m +47.5%; "
            "bruto JUMP 18.5m; pnl DROP 172k -63%; equity JUMP 9.25m; FTE JUMP 246.4; "
            "3 VE RVT); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2173; "
            "next every-10 2180; continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2172")


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_curaz_jr2025_cw_nl",
            title="Companyweb NL Zorgnetwerk Cur@-Z YE2025 statutory",
            url="https://www.companyweb.be/nl/0433217935/zorgnetwerk-cur-z",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2172; YE2025 omzet 17978378 pnl 171555 equity 9245699 bruto 18458106 "
                "FTE 246.4; neerlegging 11.06.2026; assets/debt Unknown"
            ),
        ),
        dict(
            source_id="src_curaz_jr2025_cw_en",
            title="Companyweb EN Zorgnetwerk Cur@-Z YE2025 statutory",
            url="https://www.companyweb.be/en/0433217935",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2172; EN mirror YE2025 Medium; filed 11-06-2026; Last balance sheet year 2025",
        ),
        dict(
            source_id="src_curaz_jr2025_cw_fr",
            title="Companyweb FR Zorgnetwerk Cur@-Z YE2025 statutory",
            url="https://www.companyweb.be/fr/0433217935",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2172; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_curaz_kbo_2172",
            title="KBO Zorgnetwerk Cur@-Z 0433.217.935 Actief VZW Kluisbergen 3 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0433217935",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2172; Actief VZW; Kwaremontplein 41 9690 Kluisbergen; 3 VE; "
                "RSZ 87.101 RVT; email klaus.vanhoecke@cura-z.be"
            ),
        ),
        dict(
            source_id="src_curaz_foi_contact_2172",
            title="Cur@-Z FOI contact klaus.vanhoecke@cura-z.be",
            url="https://www.cura-z.be/contact/",
            publisher="Zorgnetwerk Cur@-Z",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2172; klaus.vanhoecke@cura-z.be; info@homestfranciscus.be; tel 055 38 86 86 / 055 49 61 66",
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Zorgnetwerk Cur@-Z VZW (Kluisbergen / Maarkedal)",
            name_fr="Zorgnetwerk Cur@-Z ASBL (Kluisbergen / Maarkedal)",
            name_en="Cur@-Z care network non-profit (Kluisbergen / Maarkedal)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.cura-z.be/",
            foi_email="klaus.vanhoecke@cura-z.be",
            foi_postal="Kwaremontplein 41, 9690 Kluisbergen",
            notes=(
                "tick2172 YE2025 Medium CW NL+EN+FR + Strong KBO 0433.217.935 Actief VZW "
                "3 VE NACE 87.101 RVT; omzet JUMP 17.98m (+47.52%) bruto JUMP 18.46m "
                "pnl DROP 171555 (-63.08%) equity JUMP 9.25m FTE JUMP 246.4; sites "
                "Sint-Franciscus/Haagwinde/Casteelbosch; assets/debt Unknown; FOI "
                "gap_curaz_nbb_pdf_assets_debt_omzet_jump_pnl_drop_fte_jump_matrix_l5; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_curaz_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2172; Medium CW; omzet JUMP +47.52% vs YE2024 12186670",
    ),
    (
        "bud_curaz_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2172; Medium CW; bruto JUMP +35.35% vs YE2024 13637238",
    ),
    (
        "bud_curaz_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2172; Medium CW; pnl DROP -63.08% vs YE2024 464714",
    ),
    (
        "bud_curaz_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2172; Medium CW; equity JUMP +38.00% vs YE2024 6699589",
    ),
    (
        "bud_curaz_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 246.4",
        "tick2172; Medium CW; FTE JUMP from YE2024 185.7; assets/debt Unknown",
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
                source_id="src_curaz_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_curaz_jr2025_statutory_wzc_netwerk_omzet_jump_18m",
            title=(
                "Zorgnetwerk Cur@-Z YE2025 leftover dual "
                "(omzet JUMP 18.0m / pnl DROP -63% / FTE JUMP)"
            ),
            entity_id=ENTITY,
            beneficiary="WZC/RVT clients Kluisbergen Maarkedal Cur@-Z network",
            legal_basis="VZW RVT (KBO 0433.217.935; Actief; 3 VE; NACE 87.101)",
            decision_date="2026-06-11",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=(
                '{"2025_omzet":17978378,"2025_bruto":18458106,"2025_pnl":171555,'
                '"2025_equity":9245699,"2025_fte":246.4,'
                '"2024_omzet":12186670,"2024_bruto":13637238,"2024_pnl":464714,'
                '"2024_equity":6699589,"2024_fte":185.7}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0433217935",
            stated_goal="Residential elderly care network Vlaamse Ardennen",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; explain omzet+FTE JUMP with pnl DROP; "
                "per-site Sint-Franciscus/Haagwinde matrix"
            ),
            source_id="src_curaz_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Kluisbergen>Curaz>JR2025_statutory_L5",
            notes=(
                "tick2172; Medium CW; omzet primary envelope; assets/debt Unknown; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "Ben Woonzorgnetwerk already mined concurrent"
            ),
        )
    ],
)

# pi = 0.55*5.5 + 0.35*6.0 + 0.10*6.5 = 5.775 ≈ 5.8
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_curaz_omzet_jump_18_0m_pnl_drop_fte_jump_jr2025",
            name="Cur@-Z omzet JUMP 18.0m / pnl DROP -63% / FTE JUMP (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Kluisbergen>Curaz>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                "CW omzet envelope 18.0m / 246.4 FTE; pnl DROP -63% despite omzet JUMP "
                "+47.5%; equity JUMP +38%; assets/debt Unknown pending NBB PDF"
            ),
            confidence="medium",
            source_id="src_curaz_jr2025_cw_en",
            beneficiaries="WZC clients Kluisbergen/Maarkedal Cur@-Z",
            stated_goal="Residential elderly care network Vlaamse Ardennen",
            measured_outcome=(
                "omzet JUMP +47.52%; bruto JUMP +35.35%; pnl DROP -63.08%; "
                "equity JUMP +38.00%; FTE JUMP 185.7→246.4"
            ),
            absurdity_score="6.0",
            cost_score="5.5",
            difficulty="3.5",
            priority_index="5.8",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose perimeter JUMP path "
                "(Haagwinde fusion?); per-site RIZIV/toelage matrix"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2172; Medium CW; FOI gap_curaz_nbb_pdf_assets_debt_omzet_jump_pnl_drop_"
                "fte_jump_matrix_l5; stall FARO/AIESH/REW YE2024"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_curaz_nbb_pdf_assets_debt_omzet_jump_pnl_drop_fte_jump_matrix_l5",
            hierarchy_path="Vlaanderen>OostVlaanderen>Kluisbergen>Curaz>NBB_PDF_assets_debt_pnl_drop",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "omzet JUMP EUR18.0m (+47.5%) perimeter/Haagwinde fusion path; pnl DROP "
                "EUR172k (−63%) despite FTE JUMP 185.7→246.4; per-site Sint-Franciscus/"
                "Haagwinde/Casteelbosch + RIZIV/dagprijs/gemeente toelage split"
            ),
            why_it_matters=(
                "Medium CW shows EUR18.0m Vlaamse Ardennen WZC network with sharp pnl DROP "
                "while omzet+FTE jump — no balanstotaal/assets/debt; perimeter opacity"
            ),
            priority="8",
            recipient_body="Zorgnetwerk Cur@-Z VZW",
            recipient_email="klaus.vanhoecke@cura-z.be",
            recipient_postal="Kwaremontplein 41, 9690 Kluisbergen",
            draft_letter_path="docs/doge/foi/drafts/gap_curaz_nbb_pdf_assets_debt_omzet_jump_pnl_drop_fte_jump_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_curaz_jr2025_statutory_wzc_netwerk_omzet_jump_18m",
            linked_leaderboard_id="lb_curaz_omzet_jump_18_0m_pnl_drop_fte_jump_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2172; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        )
    ],
)

update_rq()
write_loop_state()
print("DONE apply")
