import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T23:20:00Z"
Path("docs/doge/data/raw/tick2320").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


path_rq = "docs/doge/data/research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_2320" and row["status"] == "done":
        raise SystemExit("rq_2320 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_heder_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_heder_jr2025_cw_nl",
            "Companyweb NL Heder YE2025 statutory",
            "https://www.companyweb.be/nl/0538767692/heder",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2320; YE2025 omzet 1858609 bruto 32694121 ~17.59x pnl FLIP 719053 equity 4170158 FTE 421",
        ),
        (
            "src_heder_jr2025_cw_en",
            "Companyweb EN Heder YE2025 statutory",
            "https://www.companyweb.be/en/0538767692/heder",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2320; EN Medium; filed 10-07-2026; Turnover 1858609 Gross 32694121 P/L 719053 Equity 4170158 FTE 421",
        ),
        (
            "src_heder_jr2025_cw_fr",
            "Companyweb FR Heder YE2025 statutory",
            "https://www.companyweb.be/fr/0538767692/heder",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2320; FR mirror",
        ),
        (
            "src_heder_kbo_2320",
            "KBO Heder 0538.767.692",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0538767692",
            "KBO FOD Economie",
            "official_register",
            "tick2320; Actief 5 VE Heder Ekeren RSZ 87.201",
        ),
        (
            "src_heder_site_contact_2320",
            "Heder FOI info@heder.be",
            "https://heder.be/contact/",
            "Heder VZW",
            "foi_contact",
            "tick2320; info@heder.be; Herman Vosstraat 14 Ekeren",
        ),
    ]:
        append_csv(
            "docs/doge/data/sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-27",
                source_class=klass,
                notes=notes,
            ),
        )

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_heder_ekeren"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_heder_ekeren",
            name_nl="Heder VZW (Ekeren / VAPH MFC)",
            name_fr="Heder ASBL (Ekeren / MFC VAPH)",
            name_en="Heder VZW (Ekeren / VAPH MFC)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://heder.be/",
            foi_email="info@heder.be",
            foi_postal="Herman Vosstraat 14, 2180 Antwerpen (Ekeren)",
            notes=(
                "tick2320 EVERY-10 YE2025 Medium CW + Strong KBO 0538.767.692 Actief 5 VE RSZ 87.201; "
                "omzet JUMP 1858609; bruto JUMP 32694121 ~17.59x; pnl PROFIT FLIP 719053; equity JUMP 4170158; "
                "FTE DROP 421; FOI gap_heder_*; after Kindervriend@2319; not TE-additive"
            ),
        ),
    )

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_heder_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_heder_omzet_jr2025_statutory", 1858609, "CW statutory omzet YE2025 JUMP", "tick2320; Medium CW; omzet +20.86% vs 1537768"),
        ("bud_heder_bruto_jr2025_statutory", 32694121, "CW statutory bruto_marge YE2025 ~17.59x omzet", "tick2320; Medium CW; bruto +2.88% vs 31777356"),
        ("bud_heder_pnl_jr2025_statutory", 719053, "CW statutory winst/verlies YE2025 PROFIT FLIP", "tick2320; Medium CW; pnl FLIP vs -128406"),
        ("bud_heder_equity_jr2025_statutory", 4170158, "CW statutory eigen_vermogen YE2025 JUMP", "tick2320; Medium CW; equity +22.76% vs 3397072"),
        ("bud_heder_fte_jr2025_statutory", 421, "CW social-balance FTE 421", "tick2320; Medium CW; FTE DROP vs 439.1"),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(
                budget_id=bid,
                entity_id="vzw_heder_ekeren",
                year="2025",
                amount_eur=str(amt),
                amount_min_eur=str(amt),
                amount_max_eur=str(amt),
                basis=basis,
                source_id="src_heder_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

if not has_id("docs/doge/data/commitments.csv", "commitment_id", "comm_heder_jr2025_statutory_vaph_bruto_32_69m_17_59x"):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_heder_jr2025_statutory_vaph_bruto_32_69m_17_59x",
            title="Heder YE2025 EVERY-10 leftover dual (omzet 1.86m / bruto 32.69m ~17.59x / pnl PROFIT FLIP / FTE 421 / Medium)",
            entity_id="vzw_heder_ekeren",
            beneficiary="kinderen/jongeren motorische+verstandelijke beperking Antwerpen / VAPH",
            legal_basis="VZW Heder (KBO 0538.767.692)",
            decision_date="2026-07-10",
            start_year="2025",
            end_year="2025",
            total_envelope_eur="32694121",
            cash_by_year=(
                '{"2025_omzet":1858609,"2025_bruto":32694121,"2025_pnl":719053,"2025_equity":4170158,"2025_fte":421,'
                '"2024_omzet":1537768,"2024_bruto":31777356,"2024_pnl":-128406,"2024_equity":3397072,"2024_fte":439.1}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0538767692/heder",
            stated_goal="VAPH MFC Heder",
            cut_option="Publish NBB PDF assets/debt FOI; explain bruto~17.59x omzet",
            source_id="src_heder_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Ekeren>Heder_VAPH>JR2025_statutory_L5",
            notes="tick2320 EVERY-10; Medium CW; after Kindervriend@2319; not TE-additive",
        ),
    )

if not has_id("docs/doge/data/leaderboard.csv", "item_id", "lb_heder_bruto_32_69m_gt_omzet_17_59x_pnl_flip_jr2025"):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_heder_bruto_32_69m_gt_omzet_17_59x_pnl_flip_jr2025",
            name="Heder bruto 32.69m / ~17.59x omzet 1.86m / pnl PROFIT FLIP / FTE 421 (YE2025 VAPH Ekeren)",
            level="L5",
            type="vaph_mfc_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Ekeren>Heder_VAPH>JR2025",
            annual_cost_eur="32694121",
            total_cost_eur="32694121",
            tco_notes="CW omzet 1858609 / bruto 32694121 ~17.59x / pnl FLIP 719053 / equity JUMP 4170158 / FTE DROP 421",
            confidence="medium",
            source_id="src_heder_jr2025_cw_en",
            beneficiaries="kinderen/jongeren met beperking Antwerpen",
            stated_goal="VAPH MFC",
            measured_outcome="bruto~17.59x omzet; pnl PROFIT FLIP; FTE 421; filed 10.07.2026",
            absurdity_score="7.6",
            cost_score="5.8",
            difficulty="3.0",
            priority_index="6.7",
            cut_proposal="Publish NBB PDF assets/debt FOI; VAPH subsidy matrix",
            status="open",
            struck_reason="",
            notes="tick2320 EVERY-10; Medium CW; FOI gap_heder_*",
        ),
    )

if not has_id(
    "docs/doge/data/foi_queue.csv",
    "gap_id",
    "gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_flip_vaph_matrix_l5",
):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id="gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_flip_vaph_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>Ekeren>Heder_VAPH>NBB_PDF",
            entity_id="vzw_heder_ekeren",
            what_is_missing="NBB PDF YE2025 assets/debt; bruto 32694121 ~17.59x omzet 1858609; pnl FLIP 719053; VAPH subsidy matrix; FTE 421",
            why_it_matters="Medium CW VAPH MFC Ekeren bruto~17.59x omzet; assets/debt unknown; FTE 421",
            priority="8",
            recipient_body="Heder VZW",
            recipient_email="info@heder.be",
            recipient_postal="Herman Vosstraat 14, 2180 Antwerpen (Ekeren)",
            draft_letter_path="docs/doge/foi/drafts/gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_flip_vaph_matrix_l5.md",
            status="ready",
            date_ready="2026-08-27",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_heder_jr2025_statutory_vaph_bruto_32_69m_17_59x",
            linked_leaderboard_id="lb_heder_bruto_32_69m_gt_omzet_17_59x_pnl_flip_jr2025",
            created_utc=utc,
            updated_utc=utc,
            notes="tick2320 EVERY-10; ready NOT sent",
        ),
    )

for row in rows:
    if row["task_id"] == "rq_2320":
        row.update(
            {
                "title": "EVERY-10 + leftover dual — Heder YE2025 Medium (bruto JUMP 32.69m / ~17.59x omzet / pnl PROFIT FLIP / FTE 421)",
                "status": "done",
                "entity_id": "vzw_heder_ekeren",
                "blocked_gap_id": "gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_flip_vaph_matrix_l5",
                "updated_utc": utc,
                "instructions": "EVERY-10 + leftover dual Heder VAPH YE2025 after Kindervriend@2319",
                "notes": "tick2320 EVERY-10; Heder 0538.767.692 YE2025 Medium; omzet JUMP 1858609; bruto JUMP 32694121 ~17.59x; pnl PROFIT FLIP 719053; equity JUMP 4170158; FTE DROP 421; FOI ready NOT sent; progress+waste top10 refreshed; next EVERY-10 2330",
            }
        )

if not any(row["task_id"] == "rq_2321" for row in rows):
    rows.append(
        {
            "task_id": "rq_2321",
            "title": "leftover dual after Heder — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "After Heder. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae/De Ploeg if YE2025). Do NOT redo Heder/Kindervriend/Homevil/Olo-Rotonde/Havenzate stack.",
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned after tick2320 Heder EVERY-10; next every-10 2330",
        }
    )

with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fields})

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
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
            "last_tick_utc": utc,
            "last_unit_id": "rq_2320",
            "ticks_completed": "2320",
            "paused": "no",
            "notes": (
                "tick2320 EVERY-10 leftover dual Heder 0538.767.692 Medium (omzet JUMP 1858609; bruto JUMP 32694121 ~17.59x; "
                "pnl PROFIT FLIP 719053; equity JUMP 4170158; FTE DROP 421; 5 VE Ekeren VAPH); after Kindervriend@2319; "
                "progress+waste top10 refreshed; AGB Bornem JR2024; FARO/AIESH YE2024; next rq_2321; next EVERY-10 2330"
            ),
        }
    )

print("tick2320 OK")
