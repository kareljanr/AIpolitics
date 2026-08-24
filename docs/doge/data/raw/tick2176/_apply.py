# -*- coding: utf-8 -*-
"""tick2176 De Springplank maatwerk Hasselt YE2025 Medium — omzet JUMP 3.78m / pnl LOSS FLIP."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T04:40:00Z"
ENTITY = "vzw_maatwerk_de_springplank"
GAP = "gap_springplank_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_matrix_l5"
COMM = "comm_springplank_jr2025_statutory_omzet_jump_pnl_loss_flip"
LB = "lb_springplank_omzet_jump_3_78m_pnl_loss_flip_jr2025"
SRC_EN = "src_springplank_jr2025_cw_en"
OMZET = 3780123
BRUTO = 5988844
PNL = -208710
EQUITY = 3748866
FTE = 148.8
OMZET_PY = 3527727
BRUTO_PY = 5960227
PNL_PY = 204752
EQUITY_PY = 3972097


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
        if row.get("task_id") == "rq_2176":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "leftover dual — De Springplank maatwerk Hasselt YE2025 Medium "
                "(omzet JUMP 3.78m / pnl LOSS FLIP -209k)"
            )
            row["notes"] = (
                "tick2176 Springplank 0465.794.592 Medium; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2177; next every-10 2180"
            )
            row["entity_id"] = ENTITY
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Completed leftover De Springplank after Senes; preferred AGB Bornem "
                "JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
                "FOI ready not sent"
            )
    ids = {row.get("task_id") for row in rows}
    if "rq_2177" not in ids:
        rows.append(
            {
                "task_id": "rq_2177",
                "title": (
                    "leftover dual hole-fill after Springplank — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2177 after De Springplank YE2025 Medium (omzet JUMP 3.78m / "
                    "pnl LOSS FLIP -209k / equity DROP). Prefer leftover AGB/APB if "
                    "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if "
                    "YE2025, else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo "
                    "Springplank/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/"
                    "Abdij/Aaigem/Anima*/Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2176 Springplank; FARO/AIESH/REW still YE2024; "
                    "next every-10 2180"
                ),
            }
        )
        print("spawn rq_2177")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2176=done")


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
        "last_unit_id": "rq_2176",
        "ticks_completed": "2176",
        "paused": "no",
        "notes": (
            "tick2176 leftover De Springplank 0465.794.592 Medium (omzet JUMP 3.78m "
            "+7.15%; bruto 5.99m; pnl LOSS FLIP -209k; equity DROP 3.75m; FTE 148.8; "
            "12 VE NACE 88.993 maatwerk); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2177; next every-10 2180; continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2176")


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_springplank_jr2025_cw_nl",
            title="Companyweb NL Maatwerkbedrijf De Springplank YE2025 statutory",
            url="https://www.companyweb.be/nl/0465794592/maatwerkbedrijf-de-springplank",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2176; YE2025 omzet 3780123 pnl -208710 equity 3748866 bruto 5988844 "
                "FTE 148.8; neerlegging 06.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2176/"
            ),
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Maatwerkbedrijf De Springplank YE2025 statutory",
            url="https://www.companyweb.be/en/0465794592",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2176; EN mirror YE2025 Medium; filed 06-07-2026; Last balance sheet "
                "year 2025; Turnover 3780123 Profit/Loss -208710 Equity 3748866"
            ),
        ),
        dict(
            source_id="src_springplank_jr2025_cw_fr",
            title="Companyweb FR Maatwerkbedrijf De Springplank YE2025 statutory",
            url="https://www.companyweb.be/fr/0465794592",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2176; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_springplank_kbo_2176",
            title="KBO Maatwerkbedrijf De Springplank 0465.794.592 Actief VZW Hasselt 12 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0465794592",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2176; Actief VZW sinds 29.01.1999; Stadsheide 6 3500 Hasselt; 12 VE; "
                "RSZ NACE 88.993 beschutte/sociale werkplaatsen; BTW 47.792; KBO email/web empty"
            ),
        ),
        dict(
            source_id="src_springplank_foi_contact_2176",
            title="De Springplank FOI contact info@okazi.be + tel 011 27 35 75 (Sociale Kaart)",
            url="https://www.desocialekaart.be/sociale-werkplaats-de-springplank-501380",
            publisher="Sociale Kaart / okazi.be",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes=(
                "tick2176; info@okazi.be; www.okazi.be; tel 011273575; KBO email empty; "
                "secondary directory Medium"
            ),
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Maatwerkbedrijf De Springplank VZW (Hasselt)",
            name_fr="Maatwerkbedrijf De Springplank ASBL (Hasselt)",
            name_en="De Springplank sheltered workshop non-profit (Hasselt)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.okazi.be",
            foi_email="info@okazi.be",
            foi_postal="Stadsheide 6, 3500 Hasselt",
            notes=(
                "tick2176 YE2025 Medium CW NL+EN+FR + Strong KBO 0465.794.592 Actief VZW "
                "12 VE RSZ NACE 88.993 maatwerk; omzet JUMP 3.78m (+7.15%) bruto 5.99m "
                "pnl LOSS FLIP -208710 equity DROP 3.75m FTE 148.8; assets/debt Unknown; "
                "FOI gap_springplank_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_matrix_l5; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "info@okazi.be Medium"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_springplank_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2176; Medium CW; omzet JUMP +7.15% vs YE2024 3527727",
    ),
    (
        "bud_springplank_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2176; Medium CW; bruto JUMP +0.48% vs YE2024 5960227; exceeds omzet",
    ),
    (
        "bud_springplank_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2176; Medium CW; pnl LOSS FLIP vs YE2024 204752",
    ),
    (
        "bud_springplank_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2176; Medium CW; equity DROP -5.62% vs YE2024 3972097",
    ),
    (
        "bud_springplank_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 148.8",
        "tick2176; Medium CW; FTE 148.8; assets/debt Unknown",
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
                source_id=SRC_EN,
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id=COMM,
            title=(
                "De Springplank maatwerk Hasselt YE2025 leftover dual "
                "(omzet JUMP 3.78m / pnl LOSS FLIP -209k)"
            ),
            entity_id=ENTITY,
            beneficiary="maatwerkers / social-economy clients Hasselt-Limburg",
            legal_basis="VZW maatwerk (KBO 0465.794.592; Actief; 12 VE; NACE 88.993)",
            decision_date="2026-07-06",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=(
                '{"2025_omzet":3780123,"2025_bruto":5988844,"2025_pnl":-208710,'
                '"2025_equity":3748866,"2025_fte":148.8,'
                '"2024_omzet":3527727,"2024_bruto":5960227,"2024_pnl":204752,'
                '"2024_equity":3972097}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0465794592",
            stated_goal="Sheltered employment / maatwerk for hard-to-place workers",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie/GESCO/ESF "
                "matrix; explain LOSS FLIP with omzet JUMP"
            ),
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>DeSpringplank>JR2025_statutory_L5",
            notes=(
                "tick2176; Medium CW; omzet primary envelope; bruto>omzet; assets/debt "
                "Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                "TE-additive of 348bn"
            ),
        )
    ],
)

# pi ≈ 0.4*5.5 + 0.4*5.0 + 0.2*6.5 = 2.2+2.0+1.3 = 5.5
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="De Springplank omzet JUMP 3.78m / pnl LOSS FLIP -209k (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>DeSpringplank>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                "CW omzet envelope 3.78m / bruto 5.99m / 148.8 FTE; pnl LOSS FLIP -209k "
                "with omzet JUMP; equity DROP -5.6%; assets/debt Unknown pending NBB PDF; "
                "public maatwerk wage-cost subsidies opaque"
            ),
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Hasselt-Limburg / public loonkostsubsidie path",
            stated_goal="Sheltered employment maatwerk",
            measured_outcome=(
                "omzet JUMP +7.15%; bruto JUMP +0.48%; pnl LOSS FLIP; equity DROP -5.62%; "
                "FTE 148.8"
            ),
            absurdity_score="5.5",
            cost_score="5.0",
            difficulty="3.5",
            priority_index="5.5",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/"
                "ESF/gemeente split; explain LOSS FLIP vs omzet JUMP"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2176; Medium CW; FOI gap_springplank_nbb_pdf_assets_debt_pnl_loss_"
                "flip_equity_drop_matrix_l5; stall FARO/AIESH/REW YE2024"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Limburg>Hasselt>DeSpringplank>NBB_PDF_assets_debt_pnl_flip",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl LOSS FLIP EUR-208710 vs YE2024 winst EUR204752 recon; omzet JUMP "
                "EUR3.78m path; loonkostsubsidie/GESCO/ESF/gemeente Hasselt/provincie "
                "Limburg toelage matrix; FTE 148.8 vs ~200 maatwerkers public claims"
            ),
            why_it_matters=(
                "Medium CW shows Hasselt maatwerk VZW flipping to EUR209k LOSS while "
                "omzet jumps — balanstotaal/assets/debt and public wage-cost subsidies "
                "unpublished"
            ),
            priority="8",
            recipient_body="Maatwerkbedrijf De Springplank VZW",
            recipient_email="info@okazi.be",
            recipient_postal="Stadsheide 6, 3500 Hasselt (tel 011 27 35 75 Sociale Kaart Medium)",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "tick2176; ready NOT sent; Medium CW + Strong KBO; FOI email Medium "
                "secondary; next every-10 2180"
            ),
        )
    ],
)

update_rq()
write_loop_state()

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick 2176 - {TS} - rq_2176 De Springplank (omzet JUMP 3.78m / pnl LOSS FLIP -209k / Medium)

- Unit: **rq_2176** leftover dual after **rq_2175 Senes**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Skipped Residentie Oudenburg NACE 68 RE brokerage; Melis Home micro retail. Took unused leftover **Maatwerkbedrijf De Springplank VZW** YE2025 (KBO **0465.794.592**; Stadsheide 6 Hasselt; **VZW** RSZ NACE **88.993** beschutte werkplaats / **12 VE**). Do not redo Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Abdij/Aaigem/Anima*/Zorg-Saam/emeis.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR3780123** JUMP +7.15% vs YE2024 EUR3527727; bruto **EUR5988844** JUMP +0.48%; pnl **EUR-208710** LOSS FLIP vs YE2024 EUR204752; equity **EUR3748866** DROP -5.62% vs YE2024 EUR3972097; FTE **148.8**; neerlegging **06.07.2026**. Assets/debt Unknown. Medium. Strong KBO Actief VZW 12 VE. FOI via info@okazi.be (tel 011 27 35 75 Sociale Kaart Medium).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.5); entities (+1 vzw_maatwerk_de_springplank); foi + draft gap_springplank_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_matrix_l5; rq_2176=done + rq_2177 open; loop_state ticks=2176; raw docs/doge/data/raw/tick2176/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2170**; next **2180**). Next: rq_2177 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS-HVZ).
"""
with open(log, "a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick2176 Springplank applied")
