import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T16:15:00Z"
Path("docs/doge/data/raw/tick2295").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


path_rq = "docs/doge/data/research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2295" and row["status"] == "done":
        raise SystemExit(f"rq_2295 already done: {row.get('title','')[:90]}")

for sid, title, url, pub, klass, notes in [
    (
        "src_stobbe_jr2025_cw_nl",
        "Companyweb NL De Stobbe YE2025 statutory",
        "https://www.companyweb.be/nl/0435316303/de-stobbe",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2295; YE2025 empty omzet bruto JUMP 2908874 pnl DROP 199594 equity JUMP 3474700 FTE 34.3; neerlegging 05.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2295/",
    ),
    (
        "src_stobbe_jr2025_cw_en",
        "Companyweb EN De Stobbe YE2025 statutory",
        "https://www.companyweb.be/en/0435316303/de-stobbe",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2295; EN mirror YE2025 Medium; filed 05-06-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 2908874 Profit/Loss 199594 Equity 3474700 FTE 34.3",
    ),
    (
        "src_stobbe_jr2025_cw_fr",
        "Companyweb FR De Stobbe YE2025 statutory",
        "https://www.companyweb.be/fr/0435316303/de-stobbe",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2295; FR mirror; CA unpublished; Marge brute 2908874; Benefice 199594",
    ),
    (
        "src_stobbe_kbo_2295",
        "KBO De Stobbe 0435.316.303 Actief Antwerpen",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435316303",
        "KBO FOD Economie",
        "official_register",
        "tick2295; Actief VZW De Stobbe; zetel Julius De Geyterstraat 57 2020 Antwerpen; CIG integrale gezinszorg; NACE welzijnswerk met huisvesting",
    ),
    (
        "src_stobbe_site_contact_2295",
        "De Stobbe FOI channel destobbe@cigdestobbe.be",
        "https://www.cigdestobbe.be/nl/contact-gezinnen/",
        "CIG De Stobbe VZW",
        "foi_contact",
        "tick2295; destobbe@cigdestobbe.be; +32 3 260 68 60; Julius De Geyterstraat 57 2020 Antwerpen",
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

append_csv(
    "docs/doge/data/entities.csv",
    dict(
        entity_id="vzw_de_stobbe_antwerpen",
        name_nl="De Stobbe VZW / CIG De Stobbe (Antwerpen / integrale gezinszorg)",
        name_fr="De Stobbe ASBL / CIG De Stobbe (Anvers / soins familiaux integraux)",
        name_en="De Stobbe VZW / CIG De Stobbe (Antwerp integral family care centre)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.cigdestobbe.be/",
        foi_email="destobbe@cigdestobbe.be",
        foi_postal="Julius De Geyterstraat 57, 2020 Antwerpen",
        notes=(
            "tick2295 YE2025 Medium CW NL+EN+FR + Strong KBO 0435.316.303 Actief CIG; empty omzet; "
            "bruto JUMP 2908874 (+0.84%) pnl DROP 199594 (-45.9%) equity JUMP 3474700 (+5.58%) FTE 34.3; "
            "neerlegging 05.06.2026; assets/debt Unknown; FOI gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5; "
            "after Mo-Clean@2294; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_stobbe_bruto_jr2025_statutory",
        2908874,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2295; Medium CW; bruto JUMP +0.84% vs YE2024 2884677; omzet unpublished",
    ),
    (
        "bud_stobbe_pnl_jr2025_statutory",
        199594,
        "CW statutory winst/verlies YE2025 DROP",
        "tick2295; Medium CW; pnl DROP -45.9% vs YE2024 368920",
    ),
    (
        "bud_stobbe_equity_jr2025_statutory",
        3474700,
        "CW statutory eigen_vermogen YE2025 JUMP",
        "tick2295; Medium CW; equity JUMP +5.58% vs YE2024 3291058",
    ),
    (
        "bud_stobbe_fte_jr2025_statutory",
        34.3,
        "CW social-balance FTE 34.3",
        "tick2295; Medium CW; FTE 34.3 vs YE2024 33.6; assets/debt Unknown",
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

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_stobbe_jr2025_statutory_cig_bruto_2_91m_pnl_drop",
        title=(
            "De Stobbe YE2025 leftover dual (bruto 2.91m / empty omzet / pnl DROP -46% / equity JUMP / FTE 34.3 / Medium)"
        ),
        entity_id="vzw_de_stobbe_antwerpen",
        beneficiary="gezinnen / ouders-kinderen Antwerpen / CIG trajecten",
        legal_basis="VZW CIG De Stobbe (KBO 0435.316.303; Actief; Antwerpen; welzijnswerk met huisvesting)",
        decision_date="2026-06-05",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="2908874",
        cash_by_year=(
            '{"2025_omzet":null,"2025_bruto":2908874,"2025_pnl":199594,"2025_equity":3474700,"2025_fte":34.3,'
            '"2024_omzet":null,"2024_bruto":2884677,"2024_pnl":368920,"2024_equity":3291058,"2024_fte":33.6}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0435316303/de-stobbe",
        stated_goal="Centrum integrale gezinszorg Antwerpen (ouders/kinderen begeleiding)",
        cut_option=(
            "Publish NBB PDF assets/debt; reconcile empty omzet + pnl DROP -46% vs Opgroeien/VAPH/gemeente subsidy matrix"
        ),
        source_id="src_stobbe_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Antwerpen>Antwerpen>De_Stobbe_CIG>JR2025_statutory_L5",
        notes=(
            "tick2295; Medium CW; bruto primary envelope 2908874 (empty omzet); pnl DROP 199594; equity JUMP 3474700; "
            "FTE 34.3; after Mo-Clean@2294; AGB Bornem JR2024; FARO YE2024; not TE-additive of 348bn"
        ),
    ),
)

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
        tco_notes=(
            "CW empty omzet / bruto 2908874 (+0.84%) / pnl DROP 199594 (-45.9% vs 368920) / "
            "equity JUMP 3474700 (+5.58%) / FTE 34.3 / CIG gezinszorg"
        ),
        confidence="medium",
        source_id="src_stobbe_jr2025_cw_en",
        beneficiaries="gezinnen / ouders-kinderen Antwerpen",
        stated_goal="CIG De Stobbe integrale gezinszorg",
        measured_outcome=(
            "empty omzet; bruto flat +0.84%; pnl DROP -46%; equity JUMP +5.58%; FTE 34.3; filed 05.06.2026"
        ),
        absurdity_score="5.8",
        cost_score="3.5",
        difficulty="3.0",
        priority_index="4.65",
        cut_proposal=(
            "Publish NBB PDF assets/debt FOI; disclose empty-omzet + pnl DROP vs Opgroeien/gemeente subsidy matrix"
        ),
        status="open",
        struck_reason="",
        notes=(
            "tick2295; Medium CW; FOI gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Mo-Clean@2294"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5",
        hierarchy_path="Vlaanderen>Antwerpen>Antwerpen>De_Stobbe_CIG>NBB_PDF_assets_debt_empty_omzet_pnl_drop",
        entity_id="vzw_de_stobbe_antwerpen",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR2908874; "
            "pnl DROP EUR199594 vs EUR368920; equity JUMP EUR3474700; Opgroeien/VAPH/gemeente Antwerpen subsidy matrix; "
            "FTE 34.3; CIG activity split"
        ),
        why_it_matters=(
            "Medium CW shows Antwerp CIG VZW (bruto 2.91m / empty omzet / pnl DROP -46% / FTE 34.3) "
            "under integrale gezinszorg path; assets/debt unpublished"
        ),
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
        notes="tick2295; ready NOT sent; Medium CW + Strong KBO; next every-10 2300",
    ),
)

for row in rows:
    if row["task_id"] == "rq_2295":
        row.update(
            {
                "title": (
                    "leftover dual — De Stobbe YE2025 Medium "
                    "(bruto JUMP 2.91m / empty omzet / pnl DROP -46% / FTE 34.3)"
                ),
                "status": "done",
                "entity_id": "vzw_de_stobbe_antwerpen",
                "blocked_gap_id": "gap_stobbe_nbb_pdf_assets_debt_empty_omzet_pnl_drop_cig_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "leftover dual De Stobbe CIG YE2025 FREE Antwerpen after Mo-Clean@2294; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2295; De Stobbe VZW Antwerpen 0435.316.303 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet unpublished; bruto JUMP 2908874 (+0.84%); pnl DROP 199594 (-45.9%); equity JUMP 3474700 (+5.58%); "
                    "FTE 34.3; CIG; neerlegging 05.06.2026; assets/debt Unknown; FOI ready NOT sent; "
                    "stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Mo-Clean@2294; next EVERY-10 2300"
                ),
            }
        )

if not any(row["task_id"] == "rq_2296" for row in rows):
    rows.append(
        {
            "task_id": "rq_2296",
            "title": (
                "leftover dual after De Stobbe — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after rq_2295 De Stobbe YE2025 Medium primary "
                "(bruto JUMP 2.91m / empty omzet / pnl DROP -46% / FTE 34.3). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/De Ploeg/Vlotter YE2024; AKSI if unused). "
                "Do NOT redo De Stobbe/Mo-Clean/NLZ/Labor/Intro Schoonmaak/Op Maat stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2295 De Stobbe; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2300"
            ),
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
            "last_unit_id": "rq_2295",
            "ticks_completed": "2295",
            "paused": "no",
            "notes": (
                "tick2295 leftover dual De Stobbe 0435.316.303 Medium (bruto JUMP 2908874 +0.84%; empty omzet; "
                "pnl DROP 199594 -45.9%; equity JUMP 3474700; FTE 34.3; CIG Antwerpen); after Mo-Clean@2294; "
                "AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2296; next EVERY-10 2300; continuous hole_fill"
            ),
        }
    )

print("tick2295 OK")
