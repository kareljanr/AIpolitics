# -*- coding: utf-8 -*-
"""tick2171 leftover dual — De Vlietoever WZC Bornem YE2025 Medium."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T03:00:00Z"
ENTITY = "bv_de_vlietoever_wzc_bornem"
OMZET = 13320285
BRUTO = 8990392
PNL = -226420
EQUITY = 1427775
FTE = 124.3
OMZET_PY = 12384152
BRUTO_PY = 7827357
PNL_PY = -940240
EQUITY_PY = 1654194
GAP = "gap_vlietoever_nbb_pdf_assets_debt_pnl_loss_equity_drop_cura_matrix_l5"


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
                "leftover dual — De Vlietoever WZC Bornem YE2025 Medium "
                "(omzet JUMP 13.3m / pnl LOSS IMPROVED -226k / equity DROP)"
            )
            row["entity_id"] = ENTITY
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick2171 De Vlietoever 0898.596.122 Medium; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis mined/micro; "
                "next rq_2172; next every-10 2180"
            )
            row["instructions"] = (
                "Completed leftover De Vlietoever WZC after Abdij Affligem; "
                "preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
                "Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
    ids = {row.get("task_id") for row in rows}
    if "rq_2172" not in ids:
        rows.append(
            {
                "task_id": "rq_2172",
                "title": (
                    "leftover dual hole-fill after De Vlietoever — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2172 after rq_2171 De Vlietoever WZC Bornem YE2025 Medium "
                    "(omzet JUMP 13.3m / pnl LOSS IMPROVED -226k / equity DROP). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
                    "YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ "
                    "live euros. Do NOT redo De Vlietoever/Abdij Affligem/Sint-Vincentius "
                    "Aaigem/Sint Lodewijk/Lork Hoeselt/Anima stack/Avondvrede/Zorg-Saam/"
                    "Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/Mater Dei/Sint-Carolus/"
                    "Stuyvenberg. Skip Melis Home micro."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2171 De Vlietoever; "
                    "FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next every-10 2180"
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
            "tick2171 leftover De Vlietoever WZC Bornem 0898.596.122 Medium "
            "(omzet JUMP 13.32m; bruto JUMP 8.99m; pnl LOSS IMPROVED -226k; "
            "equity DROP 1.43m; FTE 124.3; NACE 87.101 BV 2 VE CuraCare); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2172; "
            "EVERY-10 next 2180; continuous hole_fill"
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
            source_id="src_vlietoever_jr2025_cw_nl",
            title="Companyweb NL De Vlietoever WZC YE2025 statutory",
            url="https://www.companyweb.be/nl/0898596122/de-vlietoever-wzc",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                "tick2171; YE2025 omzet 13320285 pnl -226420 equity 1427775 "
                "bruto 8990392 FTE 124.3; neerlegging 17.07.2026; assets/debt Unknown"
            ),
        ),
        dict(
            source_id="src_vlietoever_jr2025_cw_en",
            title="Companyweb EN De Vlietoever WZC YE2025 statutory",
            url="https://www.companyweb.be/en/0898596122",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2171; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025",
        ),
        dict(
            source_id="src_vlietoever_jr2025_cw_fr",
            title="Companyweb FR De Vlietoever WZC YE2025 statutory",
            url="https://www.companyweb.be/fr/0898596122",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2171; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_vlietoever_kbo_2171",
            title="KBO De Vlietoever WZC 0898.596.122 Actief BV Bornem",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0898596122",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2171; Actief BV sinds 02.10.2023; Egied De Jonghestraat(WIN) 74 "
                "2880 Bornem; 2 VE; RSZ NACE 87.101; begin 10.06.2008"
            ),
        ),
        dict(
            source_id="src_vlietoever_foi_contact_2171",
            title="De Vlietoever FOI contact info.vlietoever@cura-care.be",
            url="https://vlietoever.be/contact/",
            publisher="De Vlietoever / CuraCare",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2171; info.vlietoever@cura-care.be; tel 03 889 37 99; Egied De Jonghestraat 74 Bornem",
        ),
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="De Vlietoever WZC BV (Bornem / Wintam / CuraCare)",
            name_fr="De Vlietoever MRS SRL (Bornem / Wintam / CuraCare)",
            name_en="De Vlietoever nursing home Ltd (Bornem / Wintam / CuraCare)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://vlietoever.be/",
            foi_email="info.vlietoever@cura-care.be",
            foi_postal="Egied De Jonghestraat 74, 2880 Bornem",
            notes=(
                "tick2171 YE2025 Medium CW NL+EN+FR + Strong KBO 0898.596.122 "
                "Actief BV 2 VE NACE 87.101; omzet JUMP 13320285 (+7.56%) bruto JUMP "
                "8990392 pnl LOSS IMPROVED -226420 equity DROP 1427775 FTE 124.3; "
                "assets/debt Unknown; FOI " + GAP + "; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; dual Bornem municipal care map; not TE-additive of 348bn"
            ),
        )
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_vlietoever_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2171; Medium CW; omzet JUMP +7.56% vs YE2024 12384152",
    ),
    (
        "bud_vlietoever_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2171; Medium CW; bruto JUMP +14.86% vs YE2024 7827357",
    ),
    (
        "bud_vlietoever_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2171; Medium CW; LOSS IMPROVED vs YE2024 -940240",
    ),
    (
        "bud_vlietoever_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2171; Medium CW; equity DROP -13.69% vs YE2024 1654194",
    ),
    (
        "bud_vlietoever_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 124.3",
        "tick2171; Medium CW; assets/debt Unknown pending NBB PDF",
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
                source_id="src_vlietoever_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_vlietoever_jr2025_statutory_omzet_13_3m_pnl_loss_improved",
            title=(
                "De Vlietoever WZC YE2025 leftover dual "
                "(omzet JUMP 13.3m / pnl LOSS IMPROVED -226k / equity DROP)"
            ),
            entity_id=ENTITY,
            beneficiary="WZC residents Bornem-Wintam / CuraCare private care path",
            legal_basis="BV (KBO 0898.596.122; Actief; 2 VE; NACE 87.101 RVT; RSZ since 01.08.2008)",
            decision_date="2026-07-17",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=(
                '{"2025_omzet":13320285,"2025_bruto":8990392,"2025_pnl":-226420,'
                '"2025_equity":1427775,"2025_fte":124.3,'
                '"2024_omzet":12384152,"2024_bruto":7827357,"2024_pnl":-940240,'
                '"2024_equity":1654194}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0898596122",
            stated_goal="Residential elderly care (RVT) Bornem / Wintam",
            cut_option=(
                "Publish NBB PDF assets/debt FOI; disclose RIZIV/VL subsidy vs private "
                "fees; CuraCare fee/ownership matrix; Bornem municipal dual"
            ),
            source_id="src_vlietoever_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Bornem>DeVlietoeverWZC>JR2025_statutory_L5",
            notes=(
                "tick2171; Medium CW; omzet primary envelope; assets/debt Unknown; "
                "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "unused leftover WZC after Affligem stall"
            ),
        )
    ],
)

# pi = 0.55*5.9 + 0.35*6.0 + 0.10*6.5 = 3.245+2.1+0.65 = 5.995 ~ 6.0
append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_vlietoever_omzet_13_3m_pnl_loss_improved_equity_drop_jr2025",
            name="De Vlietoever omzet JUMP 13.3m / pnl LOSS IMPROVED -226k / equity DROP (YE2025)",
            level="L5",
            type="wzc_bv_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Bornem>DeVlietoeverWZC>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                "CW omzet envelope 13.3m / 124.3 FTE; LOSS IMPROVED -226k from -940k; "
                "equity DROP -13.7% to 1.43m; multi-year LOSS YE2022-25; assets/debt Unknown"
            ),
            confidence="medium",
            source_id="src_vlietoever_jr2025_cw_en",
            beneficiaries="WZC residents Bornem-Wintam / CuraCare",
            stated_goal="RVT residential elderly care Bornem",
            measured_outcome=(
                "omzet JUMP +7.56%; bruto JUMP +14.86%; pnl LOSS IMPROVED; "
                "equity DROP -13.69%; FTE 124.3"
            ),
            absurdity_score="6.0",
            cost_score="5.9",
            difficulty="3.5",
            priority_index="6.0",
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose RIZIV/VL subsidy vs "
                "private fees; CuraCare ownership/fee matrix; Bornem dual"
            ),
            status="open",
            struck_reason="",
            notes=(
                "tick2171; Medium CW; FOI " + GAP + "; stall FARO/AIESH/REW YE2024; "
                "AGB Bornem JR2024 dual"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Bornem>DeVlietoeverWZC>NBB_PDF_assets_debt_cura",
            entity_id=ENTITY,
            what_is_missing=(
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "explanation of LOSS IMPROVED EUR-226k vs YE2024 EUR-940k at omzet JUMP "
                "EUR13.3m; equity DROP -13.7%; RIZIV/VL/gemeente subsidy matrix ≥1k; "
                "CuraCare ownership/management-fee matrix"
            ),
            why_it_matters=(
                "Medium CW shows EUR13.3m private BV WZC with multi-year LOSS and equity "
                "bleed — no balanstotaal/assets/debt; public care-subsidy opacity + CuraCare "
                "path material for FOI; dual AGB Bornem still JR2024"
            ),
            priority="8",
            recipient_body="De Vlietoever WZC BV / CuraCare",
            recipient_email="info.vlietoever@cura-care.be",
            recipient_postal="Egied De Jonghestraat 74, 2880 Bornem",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_vlietoever_jr2025_statutory_omzet_13_3m_pnl_loss_improved",
            linked_leaderboard_id="lb_vlietoever_omzet_13_3m_pnl_loss_improved_equity_drop_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2171; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        )
    ],
)

update_rq()
write_loop_state()
print("DONE apply unit")
