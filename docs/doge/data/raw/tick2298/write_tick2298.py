import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T17:15:00Z"
Path("docs/doge/data/raw/tick2298").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
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
    if row["task_id"] == "rq_2298" and row["status"] == "done":
        raise SystemExit("rq_2298 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_stobbe_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_stobbe_jr2025_cw_nl",
            "Companyweb NL De Stobbe YE2025 statutory",
            "https://www.companyweb.be/nl/0435316303/de-stobbe",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2298; YE2025 empty omzet bruto 2908874 pnl DROP 199594 equity 3474700 FTE 34.3",
        ),
        (
            "src_stobbe_jr2025_cw_en",
            "Companyweb EN De Stobbe YE2025 statutory",
            "https://www.companyweb.be/en/0435316303/de-stobbe",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2298; EN Medium; filed 05-06-2026; Gross margin 2908874 Profit/Loss 199594 Equity 3474700 FTE 34.3",
        ),
        (
            "src_stobbe_jr2025_cw_fr",
            "Companyweb FR De Stobbe YE2025 statutory",
            "https://www.companyweb.be/fr/0435316303/de-stobbe",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2298; FR mirror",
        ),
        (
            "src_stobbe_kbo_2298",
            "KBO De Stobbe 0435.316.303",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435316303",
            "KBO FOD Economie",
            "official_register",
            "tick2298; Actief CIG Antwerpen",
        ),
        (
            "src_stobbe_site_contact_2298",
            "De Stobbe FOI destobbe@cigdestobbe.be",
            "https://www.cigdestobbe.be/nl/contact-gezinnen/",
            "CIG De Stobbe VZW",
            "foi_contact",
            "tick2298; destobbe@cigdestobbe.be",
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

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_de_stobbe_antwerpen"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_de_stobbe_antwerpen",
            name_nl="De Stobbe VZW / CIG De Stobbe (Antwerpen)",
            name_fr="De Stobbe ASBL / CIG De Stobbe (Anvers)",
            name_en="De Stobbe VZW / CIG De Stobbe (Antwerp)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.cigdestobbe.be/",
            foi_email="destobbe@cigdestobbe.be",
            foi_postal="Julius De Geyterstraat 57, 2020 Antwerpen",
            notes=(
                "tick2298 YE2025 Medium CW + Strong KBO 0435.316.303; empty omzet; bruto JUMP 2908874; "
                "pnl DROP 199594; equity JUMP 3474700; FTE 34.3; FOI gap_stobbe_*; after SOBO@2297; not TE-additive"
            ),
        ),
    )

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_stobbe_bruto_jr2025_statutory"):
    for bid, amt, basis, notes in [
        (
            "bud_stobbe_bruto_jr2025_statutory",
            2908874,
            "CW statutory bruto_marge YE2025 (empty omzet)",
            "tick2298; Medium CW; bruto +0.84% vs 2884677",
        ),
        (
            "bud_stobbe_pnl_jr2025_statutory",
            199594,
            "CW statutory winst/verlies YE2025 DROP",
            "tick2298; Medium CW; pnl -45.9% vs 368920",
        ),
        (
            "bud_stobbe_equity_jr2025_statutory",
            3474700,
            "CW statutory eigen_vermogen YE2025 JUMP",
            "tick2298; Medium CW; equity +5.58% vs 3291058",
        ),
        (
            "bud_stobbe_fte_jr2025_statutory",
            34.3,
            "CW social-balance FTE 34.3",
            "tick2298; Medium CW; FTE 34.3 vs 33.6",
        ),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(
                budget_id=bid,
                entity_id="vzw_de_stobbe_antwerpen",
                year="2025",
                amount_eur=str(amt),
                amount_min_eur=str(amt),
                amount_max_eur=str(amt),
                basis=basis,
                source_id="src_stobbe_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

if not has_id(
    "docs/doge/data/commitments.csv",
    "commitment_id",
    "comm_stobbe_jr2025_statutory_cig_bruto_2_91m_pnl_drop",
):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_stobbe_jr2025_statutory_cig_bruto_2_91m_pnl_drop",
            title="De Stobbe YE2025 leftover dual (bruto 2.91m / empty omzet / pnl DROP -46% / FTE 34.3 / Medium)",
            entity_id="vzw_de_stobbe_antwerpen",
            beneficiary="gezinnen Antwerpen / CIG",
            legal_basis="VZW CIG De Stobbe (KBO 0435.316.303)",
            decision_date="2026-06-05",
            start_year="2025",
            end_year="2025",
            total_envelope_eur="2908874",
            cash_by_year=(
                '{"2025_omzet":null,"2025_bruto":2908874,"2025_pnl":199594,"2025_equity":3474700,"2025_fte":34.3,'
                '"2024_bruto":2884677,"2024_pnl":368920,"2024_equity":3291058,"2024_fte":33.6}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0435316303/de-stobbe",
            stated_goal="CIG De Stobbe",
            cut_option="Publish NBB PDF assets/debt FOI",
            source_id="src_stobbe_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Antwerpen>De_Stobbe_CIG>JR2025_statutory_L5",
            notes="tick2298; Medium CW; after SOBO@2297; not TE-additive",
        ),
    )

if not has_id(
    "docs/doge/data/leaderboard.csv",
    "item_id",
    "lb_stobbe_bruto_2_91m_empty_omzet_pnl_drop_46pct_jr2025",
):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_stobbe_bruto_2_91m_empty_omzet_pnl_drop_46pct_jr2025",
            name="De Stobbe bruto 2.91m / empty omzet / pnl DROP -46% / FTE 34.3 (YE2025 CIG Antwerpen)",
            level="L5",
            type="cig_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Antwerpen>De_Stobbe_CIG>JR2025",
            annual_cost_eur="2908874",
            total_cost_eur="2908874",
            tco_notes="CW empty omzet / bruto 2908874 / pnl DROP 199594 / equity JUMP 3474700 / FTE 34.3",
            confidence="medium",
            source_id="src_stobbe_jr2025_cw_en",
            beneficiaries="gezinnen Antwerpen",
            stated_goal="CIG De Stobbe",
            measured_outcome="empty omzet; bruto +0.84%; pnl DROP -46%; FTE 34.3; filed 05.06.2026",
            absurdity_score="5.8",
            cost_score="3.5",
            difficulty="3.0",
            priority_index="4.65",
            cut_proposal="Publish NBB PDF assets/debt FOI",
            status="open",
            struck_reason="",
            notes="tick2298; Medium CW; FOI gap_stobbe_*; after SOBO@2297",
        ),
    )

if not has_id(
    "docs/doge/data/foi_queue.csv",
    "gap_id",
    "gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5",
):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id="gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>Antwerpen>De_Stobbe_CIG>NBB_PDF",
            entity_id="vzw_de_stobbe_antwerpen",
            what_is_missing="NBB PDF YE2025 assets/debt; empty omzet; bruto 2908874; pnl DROP 199594; subsidy matrix; FTE 34.3",
            why_it_matters="Medium CW CIG Antwerp bruto 2.91m empty omzet pnl DROP -46%; assets/debt unknown",
            priority="8",
            recipient_body="De Stobbe VZW / CIG De Stobbe",
            recipient_email="destobbe@cigdestobbe.be",
            recipient_postal="Julius De Geyterstraat 57, 2020 Antwerpen",
            draft_letter_path="docs/doge/foi/drafts/gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5.md",
            status="ready",
            date_ready="2026-08-27",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_stobbe_jr2025_statutory_cig_bruto_2_91m_pnl_drop",
            linked_leaderboard_id="lb_stobbe_bruto_2_91m_empty_omzet_pnl_drop_46pct_jr2025",
            created_utc=utc,
            updated_utc=utc,
            notes="tick2298; ready NOT sent",
        ),
    )

for row in rows:
    if row["task_id"] == "rq_2298":
        row.update(
            {
                "title": "leftover dual — De Stobbe YE2025 Medium (bruto JUMP 2.91m / empty omzet / pnl DROP -46% / FTE 34.3)",
                "status": "done",
                "entity_id": "vzw_de_stobbe_antwerpen",
                "blocked_gap_id": "gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5",
                "updated_utc": utc,
                "instructions": "leftover dual De Stobbe CIG YE2025 after SOBO@2297",
                "notes": "tick2298; De Stobbe 0435.316.303 YE2025 Medium; bruto 2908874 empty omzet; pnl DROP 199594; equity JUMP 3474700; FTE 34.3; FOI ready NOT sent; next EVERY-10 2300",
            }
        )

if not any(row["task_id"] == "rq_2299" for row in rows):
    rows.append(
        {
            "task_id": "rq_2299",
            "title": "leftover dual after De Stobbe — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "After De Stobbe. Prefer AGB/FARO YE2025 else unused. Do NOT redo De Stobbe/SOBO/Ryhove/Rozemarijn stack.",
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned after tick2298 De Stobbe; next every-10 2300",
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
            "last_unit_id": "rq_2298",
            "ticks_completed": "2298",
            "paused": "no",
            "notes": (
                "tick2298 leftover dual De Stobbe 0435.316.303 Medium (bruto JUMP 2908874; empty omzet; "
                "pnl DROP 199594 -45.9%; equity JUMP 3474700; FTE 34.3; CIG Antwerpen); after SOBO@2297; "
                "AGB Bornem JR2024; FARO YE2024; next rq_2299; next EVERY-10 2300; continuous hole_fill"
            ),
        }
    )

p = Path(
    "docs/doge/foi/drafts/gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5.md"
)
if p.exists():
    t = p.read_text(encoding="utf-8")
    for old in ("**tick:** 2295", "**tick:** 2296"):
        t = t.replace(old, "**tick:** 2298")
    p.write_text(t, encoding="utf-8")

print("tick2298 OK")
