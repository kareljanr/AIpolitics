import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-28T00:25:00Z"
Path("docs/doge/data/raw/tick2325").mkdir(parents=True, exist_ok=True)


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
    if row["task_id"] == "rq_2325" and row["status"] == "done":
        raise SystemExit("rq_2325 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_mivalti_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        ("src_mivalti_jr2025_cw_nl", "Companyweb NL Mivalti YE2025 statutory", "https://www.companyweb.be/nl/0416406548/mivalti", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2325; YE2025 omzet 1683253 bruto 11487628 ~6.82x pnl JUMP 470626 equity 8134829 FTE 134.9"),
        ("src_mivalti_jr2025_cw_en", "Companyweb EN Mivalti YE2025 statutory", "https://www.companyweb.be/en/0416406548/mivalti", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2325; EN Medium; filed 16-06-2026; Turnover 1683253 Gross 11487628 P/L 470626 Equity 8134829 FTE 134.9"),
        ("src_mivalti_jr2025_cw_fr", "Companyweb FR Mivalti YE2025 statutory", "https://www.companyweb.be/fr/0416406548/mivalti", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2325; FR mirror"),
        ("src_mivalti_kbo_2325", "KBO Mivalti 0416.406.548", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416406548", "KBO FOD Economie", "official_register", "tick2325; Actief 2 VE Tielt RSZ 87.202"),
        ("src_mivalti_site_contact_2325", "Mivalti FOI info@mivalti.be", "https://www.mivalti.be/", "Mivalti VZW", "foi_contact", "tick2325; info@mivalti.be; Gruuthusestraat 36 Tielt"),
    ]:
        append_csv("docs/doge/data/sources.csv", dict(source_id=sid, title=title, url=url, publisher=pub, accessed_date="2026-08-28", source_class=klass, notes=notes))

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_mivalti_tielt"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_mivalti_tielt",
            name_nl="Mivalti VZW (Tielt / VAPH woonondersteuning)",
            name_fr="Mivalti ASBL (Tielt / hébergement VAPH)",
            name_en="Mivalti VZW (Tielt / VAPH residential care)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.mivalti.be/",
            foi_email="info@mivalti.be",
            foi_postal="Gruuthusestraat 36, 8700 Tielt",
            notes="tick2325 YE2025 Medium CW + Strong KBO 0416.406.548 Actief 2 VE RSZ 87.202; omzet JUMP 1683253; bruto JUMP 11487628 ~6.82x; pnl JUMP 470626; equity JUMP 8134829; FTE 134.9; FOI gap_mivalti_*; after Ritmica@2324; not TE-additive",
        ),
    )

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_mivalti_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_mivalti_omzet_jr2025_statutory", 1683253, "CW statutory omzet YE2025 JUMP", "tick2325; Medium CW; omzet +4.55% vs 1609944"),
        ("bud_mivalti_bruto_jr2025_statutory", 11487628, "CW statutory bruto_marge YE2025 ~6.82x omzet", "tick2325; Medium CW; bruto +8% vs 10636440"),
        ("bud_mivalti_pnl_jr2025_statutory", 470626, "CW statutory winst/verlies YE2025 JUMP", "tick2325; Medium CW; pnl +26.88% vs 370928"),
        ("bud_mivalti_equity_jr2025_statutory", 8134829, "CW statutory eigen_vermogen YE2025 JUMP", "tick2325; Medium CW; equity +6.19% vs 7660758"),
        ("bud_mivalti_fte_jr2025_statutory", 134.9, "CW social-balance FTE 134.9", "tick2325; Medium CW; FTE 134.9 vs 133.1"),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(budget_id=bid, entity_id="vzw_mivalti_tielt", year="2025", amount_eur=str(amt), amount_min_eur=str(amt), amount_max_eur=str(amt), basis=basis, source_id="src_mivalti_jr2025_cw_en", confidence="medium", notes=notes),
        )

if not has_id("docs/doge/data/commitments.csv", "commitment_id", "comm_mivalti_jr2025_statutory_vaph_bruto_11_49m_6_82x"):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_mivalti_jr2025_statutory_vaph_bruto_11_49m_6_82x",
            title="Mivalti YE2025 leftover dual (omzet 1.68m / bruto 11.49m ~6.82x / pnl JUMP / FTE 134.9 / Medium)",
            entity_id="vzw_mivalti_tielt",
            beneficiary="volwassenen met mentale handicap Tielt / VAPH",
            legal_basis="VZW Mivalti (KBO 0416.406.548)",
            decision_date="2026-06-16",
            start_year="2025",
            end_year="2025",
            total_envelope_eur="11487628",
            cash_by_year='{"2025_omzet":1683253,"2025_bruto":11487628,"2025_pnl":470626,"2025_equity":8134829,"2025_fte":134.9,"2024_omzet":1609944,"2024_bruto":10636440,"2024_pnl":370928,"2024_equity":7660758,"2024_fte":133.1}',
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0416406548/mivalti",
            stated_goal="VAPH woonondersteuning Mivalti",
            cut_option="Publish NBB PDF assets/debt FOI; explain bruto~6.82x omzet",
            source_id="src_mivalti_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Tielt>Mivalti_VAPH>JR2025_statutory_L5",
            notes="tick2325; Medium CW; after Ritmica@2324; not TE-additive",
        ),
    )

if not has_id("docs/doge/data/leaderboard.csv", "item_id", "lb_mivalti_bruto_11_49m_gt_omzet_6_82x_pnl_jump_jr2025"):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_mivalti_bruto_11_49m_gt_omzet_6_82x_pnl_jump_jr2025",
            name="Mivalti bruto 11.49m / ~6.82x omzet 1.68m / pnl JUMP / FTE 134.9 (YE2025 VAPH Tielt)",
            level="L5",
            type="vaph_vzw_statutory",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Tielt>Mivalti_VAPH>JR2025",
            annual_cost_eur="11487628",
            total_cost_eur="11487628",
            tco_notes="CW omzet 1683253 / bruto 11487628 ~6.82x / pnl JUMP 470626 / equity JUMP 8134829 / FTE 134.9",
            confidence="medium",
            source_id="src_mivalti_jr2025_cw_en",
            beneficiaries="volwassenen met handicap Tielt",
            stated_goal="VAPH woonondersteuning",
            measured_outcome="bruto~6.82x omzet; pnl JUMP +27%; FTE 134.9; filed 16.06.2026",
            absurdity_score="6.4",
            cost_score="5.5",
            difficulty="3.0",
            priority_index="5.95",
            cut_proposal="Publish NBB PDF assets/debt FOI; VAPH subsidy matrix",
            status="open",
            struck_reason="",
            notes="tick2325; Medium CW; FOI gap_mivalti_*; after Ritmica@2324",
        ),
    )

if not has_id("docs/doge/data/foi_queue.csv", "gap_id", "gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5"):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id="gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Tielt>Mivalti_VAPH>NBB_PDF",
            entity_id="vzw_mivalti_tielt",
            what_is_missing="NBB PDF YE2025 assets/debt; bruto 11487628 ~6.82x omzet 1683253; pnl JUMP 470626; VAPH subsidy matrix; FTE 134.9",
            why_it_matters="Medium CW VAPH Tielt bruto~6.82x omzet; assets/debt unknown",
            priority="8",
            recipient_body="Mivalti VZW",
            recipient_email="info@mivalti.be",
            recipient_postal="Gruuthusestraat 36, 8700 Tielt",
            draft_letter_path="docs/doge/foi/drafts/gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5.md",
            status="ready",
            date_ready="2026-08-28",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_mivalti_jr2025_statutory_vaph_bruto_11_49m_6_82x",
            linked_leaderboard_id="lb_mivalti_bruto_11_49m_gt_omzet_6_82x_pnl_jump_jr2025",
            created_utc=utc,
            updated_utc=utc,
            notes="tick2325; ready NOT sent",
        ),
    )

for row in rows:
    if row["task_id"] == "rq_2325":
        row.update(
            {
                "title": "leftover dual — Mivalti YE2025 Medium (omzet JUMP 1.68m / bruto~6.82x / pnl JUMP / FTE 134.9)",
                "status": "done",
                "entity_id": "vzw_mivalti_tielt",
                "blocked_gap_id": "gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5",
                "updated_utc": utc,
                "instructions": "leftover dual Mivalti VAPH YE2025 after Ritmica@2324; Het Eepos CW N/A stall",
                "notes": "tick2325; Mivalti 0416.406.548 YE2025 Medium; omzet JUMP 1683253; bruto JUMP 11487628 ~6.82x; pnl JUMP 470626; equity JUMP 8134829; FTE 134.9; FOI ready NOT sent; next EVERY-10 2330",
            }
        )

if not any(row["task_id"] == "rq_2326" for row in rows):
    rows.append(
        {
            "task_id": "rq_2326",
            "title": "leftover dual after Mivalti — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "After Mivalti. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae/Alma if YE2025). Do NOT redo Mivalti/Ritmica/DominiekSavio/EntreDeux stack.",
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned after tick2325 Mivalti; next every-10 2330",
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
        fieldnames=["state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id", "ticks_completed", "paused", "notes"],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": utc,
            "last_unit_id": "rq_2325",
            "ticks_completed": "2325",
            "paused": "no",
            "notes": "tick2325 leftover dual Mivalti 0416.406.548 Medium (omzet JUMP 1683253; bruto JUMP 11487628 ~6.82x; pnl JUMP 470626; equity JUMP 8134829; FTE 134.9; 2 VE Tielt VAPH); after Ritmica@2324; AGB Bornem JR2024; FARO/AIESH YE2024; next rq_2326; next EVERY-10 2330",
        }
    )

print("tick2325 OK")
