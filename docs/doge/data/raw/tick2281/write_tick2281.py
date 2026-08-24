import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T12:45:00Z"
Path("docs/doge/data/raw/tick2281").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for sid, title, url, pub, klass, notes in [
    (
        "src_dageraad_jr2025_cw_nl",
        "Companyweb NL De Dageraad YE2025 statutory",
        "https://www.companyweb.be/nl/0412607613/de-dageraad",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2281; YE2025 empty omzet bruto DROP 2029973 pnl LOSS FLIP -98756 equity DROP 2030934 FTE DROP 58.8; neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2281/",
    ),
    (
        "src_dageraad_jr2025_cw_en",
        "Companyweb EN De Dageraad YE2025 statutory",
        "https://www.companyweb.be/en/0412607613/de-dageraad",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2281; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 2029973 Profit/Loss -98756 Equity 2030934 FTE 58.8",
    ),
    (
        "src_dageraad_jr2025_cw_fr",
        "Companyweb FR De Dageraad YE2025 statutory",
        "https://www.companyweb.be/fr/0412607613/de-dageraad",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2281; FR mirror; CA unpublished; Marge brute 2029973; Perte -98756",
    ),
    (
        "src_dageraad_kbo_2281",
        "KBO De Dageraad 0412.607.613 Actief Kontich 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412607613",
        "KBO FOD Economie",
        "official_register",
        "tick2281; Actief VZW De Dageraad; zetel Heiveldekens 7 2550 Kontich; 1 VE; RSZ NACE 88.993; BTW NACE 18.130/16.282; begindatum 02.08.1972",
    ),
    (
        "src_dageraad_site_contact_2281",
        "De Dageraad FOI channel directie@de-dageraad.be",
        "https://de-dageraad.be/",
        "De Dageraad VZW",
        "foi_contact",
        "tick2281; directie@de-dageraad.be; +32 3 238 29 56; Heiveldekens 7 Kontich; Flemish maatwerk zeefdruk/gravering/signalisatie",
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
        entity_id="vzw_de_dageraad_kontich",
        name_nl="De Dageraad VZW (Kontich / Flemish maatwerk zeefdruk-signalisatie)",
        name_fr="De Dageraad ASBL (Kontich / entreprise de travail adapté flamande)",
        name_en="De Dageraad adapted-work VZW (Kontich Flemish maatwerk print/signage)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://de-dageraad.be/",
        foi_email="directie@de-dageraad.be",
        foi_postal="Heiveldekens 7, 2550 Kontich",
        notes="tick2281 YE2025 Medium CW NL+EN+FR + Strong KBO 0412.607.613 Actief 1 VE NACE 88.993/18.130; empty omzet; bruto DROP 2029973 (-6.28%) pnl LOSS FLIP -98756 (-170.87%) equity DROP 2030934 (-4.28%) FTE DROP 58.8; neerlegging 03.07.2026; assets/debt Unknown; FOI gap_dageraad_nbb_pdf_assets_debt_empty_omzet_pnl_loss_flip_equity_drop_matrix_l5; after eurakor/Alternatief@2280; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_dageraad_bruto_jr2025_statutory",
        2029973,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2281; Medium CW; bruto DROP -6.28% vs YE2024 2165889; omzet unpublished",
    ),
    (
        "bud_dageraad_pnl_jr2025_statutory",
        -98756,
        "CW statutory winst/verlies YE2025 LOSS FLIP",
        "tick2281; Medium CW; pnl LOSS FLIP -170.87% vs YE2024 +139346",
    ),
    (
        "bud_dageraad_equity_jr2025_statutory",
        2030934,
        "CW statutory eigen_vermogen YE2025 DROP",
        "tick2281; Medium CW; equity DROP -4.28% vs YE2024 2121658",
    ),
    (
        "bud_dageraad_fte_jr2025_statutory",
        58.8,
        "CW social-balance FTE 58.8",
        "tick2281; Medium CW; FTE 58.8 vs YE2024 60.1; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_de_dageraad_kontich",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_dageraad_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_dageraad_jr2025_statutory_maatwerk_bruto_2_03m_pnl_loss_flip",
        title="De Dageraad YE2025 leftover dual (bruto 2.03m / empty omzet / pnl LOSS FLIP / equity DROP / FTE 58.8 / Medium)",
        entity_id="vzw_de_dageraad_kontich",
        beneficiary="maatwerk workers Kontich / zeefdruk gravering signalisatie / Flemish collectief maatwerk",
        legal_basis="VZW maatwerk De Dageraad (KBO 0412.607.613; Actief; 1 VE; NACE 88.993/18.130; Kontich)",
        decision_date="2026-07-03",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="2029973",
        cash_by_year='{"2025_omzet":null,"2025_bruto":2029973,"2025_pnl":-98756,"2025_equity":2030934,"2025_fte":58.8,"2024_omzet":null,"2024_bruto":2165889,"2024_pnl":139346,"2024_equity":2121658,"2024_fte":60.1}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0412607613/de-dageraad",
        stated_goal="Flemish maatwerk Kontich (zeefdruk / gravering / signalisatie / enclave montage)",
        cut_option="Publish NBB PDF assets/debt; reconcile empty omzet + LOSS FLIP + equity DROP vs maatwerk wage-subsidy matrix",
        source_id="src_dageraad_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Antwerpen>Kontich>De_Dageraad>JR2025_statutory_L5",
        notes="tick2281; Medium CW; bruto primary envelope 2029973 (empty omzet); pnl LOSS FLIP -98756; equity DROP 2030934; FTE 58.8; 1 VE; after eurakor/Alternatief@2280; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn",
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_dageraad_bruto_2_03m_empty_omzet_pnl_loss_flip_jr2025",
        name="De Dageraad bruto 2.03m / empty omzet / pnl LOSS FLIP / equity DROP / FTE 58.8 (YE2025 Flemish maatwerk Kontich)",
        level="L5",
        type="maatwerk_vzw_statutory",
        hierarchy_path="Vlaanderen>Antwerpen>Kontich>De_Dageraad>JR2025",
        annual_cost_eur="2029973",
        total_cost_eur="2029973",
        tco_notes="CW empty omzet / bruto 2029973 (-6.28%) / pnl LOSS FLIP -98756 (-170.87% vs profit 139346) / equity DROP 2030934 (-4.28%) / FTE 58.8 (vs 60.1) / 1 VE Flemish maatwerk Kontich",
        confidence="medium",
        source_id="src_dageraad_jr2025_cw_en",
        beneficiaries="maatwerk workers Kontich / zeefdruk gravering signalisatie",
        stated_goal="Flemish maatwerk Kontich (zeefdruk/gravering/signalisatie)",
        measured_outcome="empty omzet; bruto DROP -6.28%; pnl LOSS FLIP -171%; equity DROP -4.28%; FTE 58.8; filed 03.07.2026",
        absurdity_score="6.5",
        cost_score="3.8",
        difficulty="3.0",
        priority_index="5.07",
        cut_proposal="Publish NBB PDF assets/debt FOI; disclose empty-omzet + LOSS FLIP + equity DROP vs maatwerk wage-subsidy matrix",
        status="open",
        struck_reason="",
        notes="tick2281; Medium CW; FOI gap_dageraad_nbb_pdf_assets_debt_empty_omzet_pnl_loss_flip_equity_drop_matrix_l5; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after eurakor/Alternatief@2280",
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_dageraad_nbb_pdf_assets_debt_empty_omzet_pnl_loss_flip_equity_drop_matrix_l5",
        hierarchy_path="Vlaanderen>Antwerpen>Kontich>De_Dageraad>NBB_PDF_assets_debt_empty_omzet_pnl_loss_flip",
        entity_id="vzw_de_dageraad_kontich",
        what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR2029973; pnl LOSS FLIP EUR-98756 vs profit EUR139346; equity DROP to EUR2030934; maatwerk wage-subsidy matrix; FTE 58.8; activity split zeefdruk/gravering/signalisatie",
        why_it_matters="Medium CW shows Flemish maatwerk VZW (bruto 2.03m / empty omzet / pnl LOSS FLIP / equity DROP / FTE 58.8) under collectief maatwerk Kontich path; assets/debt unpublished",
        priority="8",
        recipient_body="De Dageraad VZW",
        recipient_email="directie@de-dageraad.be",
        recipient_postal="Heiveldekens 7, 2550 Kontich",
        draft_letter_path="docs/doge/foi/drafts/gap_dageraad_nbb_pdf_assets_debt_empty_omzet_pnl_loss_flip_equity_drop_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        linked_commitment_id="comm_dageraad_jr2025_statutory_maatwerk_bruto_2_03m_pnl_loss_flip",
        linked_leaderboard_id="lb_dageraad_bruto_2_03m_empty_omzet_pnl_loss_flip_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2281; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Foes YE2024; AGB Bornem JR2024; after eurakor/Alternatief@2280; next EVERY-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("task_id") == "rq_2281":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = "tick2281 De Dageraad Kontich YE2025 Medium; bruto DROP 2.03m / empty omzet / pnl LOSS FLIP / equity DROP / FTE 58.8"
rows.append({k: "" for k in fields})
rows[-1].update(
    dict(
        task_id="rq_2282",
        title="leftover dual after De Dageraad — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
        sprint="hole_fill",
        priority="8",
        status="open",
        hierarchy_target="L5",
        instructions="leftover dual after rq_2281 De Dageraad YE2025 Medium primary (bruto DROP 2.03m / empty omzet / pnl LOSS FLIP / FTE 58.8). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Aralea/Manupal/Posthoorn/De Ploeg/Vlotter/Buseloc YE2024). Do NOT redo De Dageraad/eurakor/Alternatief/Reset/Ateliers de l Avenir/IN-Z/m-accent/AMAB stack.",
        created_utc=utc,
        updated_utc=utc,
        notes="spawned after tick2281 De Dageraad; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2290",
    )
)
seen_open = False
out = []
for row in rows:
    if row.get("task_id") == "rq_2282" and row.get("status") == "open":
        if seen_open:
            continue
        seen_open = True
    out.append(row)
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(out)

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
        dict(
            state_id="main",
            mode="continuous",
            current_sprint="hole_fill",
            last_tick_utc=utc,
            last_unit_id="rq_2281",
            ticks_completed="2281",
            paused="no",
            notes="tick2281 leftover dual De Dageraad 0412.607.613 Medium (bruto DROP 2029973 -6.28%; empty omzet; pnl LOSS FLIP -98756; equity DROP 2030934 -4.28%; FTE 58.8; 1 VE Kontich maatwerk zeefdruk); after eurakor/Alternatief@2280; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2282; next EVERY-10 2290; continuous hole_fill",
        )
    )
print("CSV OK")
