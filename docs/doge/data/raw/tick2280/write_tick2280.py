import csv
csv.field_size_limit(10**7)
utc = "2026-08-27T12:20:00Z"

def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)

for sid, title, url, pub, klass, notes in [
    (
        "src_alternatief_jr2025_cw_nl",
        "Companyweb NL Atelier Alternatief YE2025 statutory",
        "https://www.companyweb.be/nl/0465227440/atelier-alternatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2280; YE2025 empty omzet bruto JUMP 4105167 pnl LOSS NARROW -123412 equity DROP 201770 FTE JUMP 137; neerlegging 30.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2280/",
    ),
    (
        "src_alternatief_jr2025_cw_en",
        "Companyweb EN Atelier Alternatief YE2025 statutory",
        "https://www.companyweb.be/en/0465227440/atelier-alternatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2280; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 4105167 Profit/Loss -123412 Equity 201770 FTE 137",
    ),
    (
        "src_alternatief_jr2025_cw_fr",
        "Companyweb FR Atelier Alternatief YE2025 statutory",
        "https://www.companyweb.be/fr/0465227440/atelier-alternatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2280; FR mirror; CA unpublished; Marge brute 4105167; Perte -123412",
    ),
    (
        "src_alternatief_kbo_2280",
        "KBO Atelier Alternatief 0465.227.440 Actief Genk 9 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465227440",
        "KBO FOD Economie",
        "official_register",
        "tick2280; Actief VZW Atelier Alternatief; zetel Lucien Londotstraat 3 3600 Genk; 9 VE; RSZ NACE 88.993; BTW NACE 88.999; begindatum 15.12.1998",
    ),
    (
        "src_alternatief_site_contact_2280",
        "Atelier Alternatief FOI channel info@alternatiefvzw.be",
        "https://alternatiefvzw.be/",
        "Atelier Alternatief VZW",
        "foi_contact",
        "tick2280; info@alternatiefvzw.be; Lucien Londotstraat 3 Genk; Flemish maatwerk/circular textile Limburg",
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
        entity_id="vzw_atelier_alternatief_genk",
        name_nl="Atelier Alternatief VZW (Genk / Flemish maatwerk/circular textile)",
        name_fr="Atelier Alternatief ASBL (Genk / entreprise de travail adapté flamande)",
        name_en="Atelier Alternatief adapted-work VZW (Genk Flemish maatwerk/circular textile)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://alternatiefvzw.be/",
        foi_email="info@alternatiefvzw.be",
        foi_postal="Lucien Londotstraat 3, 3600 Genk",
        notes="tick2280 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0465.227.440 Actief 9 VE NACE 88.993/88.999; empty omzet; bruto JUMP 4105167 (+3.35%) pnl LOSS NARROW -123412 (+51.22%) equity DROP 201770 (-30.5%) FTE JUMP 137; neerlegging 30.06.2026; assets/debt Unknown; FOI gap_alternatief_nbb_pdf_assets_debt_empty_omzet_equity_drop_30pct_pnl_loss_narrow_matrix_l5; after Ateliers Avenir@2279; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Reset already mined@2225; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_alternatief_bruto_jr2025_statutory",
        4105167,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2280; Medium CW; bruto JUMP +3.35% vs YE2024 3972247; omzet unpublished",
    ),
    (
        "bud_alternatief_pnl_jr2025_statutory",
        -123412,
        "CW statutory winst/verlies YE2025 LOSS NARROW",
        "tick2280; Medium CW; pnl LOSS NARROW +51.22% vs YE2024 -253001",
    ),
    (
        "bud_alternatief_equity_jr2025_statutory",
        201770,
        "CW statutory eigen_vermogen YE2025 DROP",
        "tick2280; Medium CW; equity DROP -30.5% vs YE2024 290331",
    ),
    (
        "bud_alternatief_fte_jr2025_statutory",
        137,
        "CW social-balance FTE 137",
        "tick2280; Medium CW; FTE 137 vs YE2024 134.3; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_atelier_alternatief_genk",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_alternatief_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_alternatief_jr2025_statutory_maatwerk_bruto_4_11m_equity_drop_30pct",
        title="Atelier Alternatief YE2025 leftover dual (bruto 4.11m / empty omzet / equity DROP -30.5% / LOSS NARROW / FTE 137 / Medium)",
        entity_id="vzw_atelier_alternatief_genk",
        beneficiary="maatwerk workers Genk Limburg / circular textile / linnenzorg / Flemish collectief maatwerk",
        legal_basis="VZW maatwerk Atelier Alternatief (KBO 0465.227.440; Actief; 9 VE; NACE 88.993/88.999; Genk)",
        decision_date="2026-06-30",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="4105167",
        cash_by_year='{"2025_omzet":null,"2025_bruto":4105167,"2025_pnl":-123412,"2025_equity":201770,"2025_fte":137,"2024_omzet":null,"2024_bruto":3972247,"2024_pnl":-253001,"2024_equity":290331,"2024_fte":134.3}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0465227440/atelier-alternatief",
        stated_goal="Flemish maatwerk Genk (circular textile / linnenzorg / maintenance / social employment)",
        cut_option="Publish NBB PDF assets/debt; reconcile empty omzet + equity DROP -30.5% + sustained LOSS vs maatwerk wage-subsidy matrix",
        source_id="src_alternatief_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Limburg>Genk>Atelier_Alternatief>JR2025_statutory_L5",
        notes="tick2280 EVERY-10; Medium CW; bruto primary envelope 4105167 (empty omzet); pnl LOSS NARROW -123412; equity DROP 201770 (-30.5%); FTE 137; 9 VE; after Ateliers Avenir@2279; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn",
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_alternatief_bruto_4_11m_empty_omzet_equity_drop_30pct_pnl_loss_narrow_jr2025",
        name="Atelier Alternatief bruto 4.11m / empty omzet / equity DROP -30.5% / LOSS NARROW / FTE 137 (YE2025 Flemish maatwerk Genk)",
        level="L5",
        type="maatwerk_vzw_statutory",
        hierarchy_path="Vlaanderen>Limburg>Genk>Atelier_Alternatief>JR2025",
        annual_cost_eur="4105167",
        total_cost_eur="4105167",
        tco_notes="CW empty omzet / bruto 4105167 (+3.35%) / pnl LOSS NARROW -123412 (+51.22% vs deeper loss) / equity DROP 201770 (-30.5%) / FTE 137 (vs 134.3) / 9 VE Flemish maatwerk Genk",
        confidence="medium",
        source_id="src_alternatief_jr2025_cw_en",
        beneficiaries="maatwerk workers Genk Limburg / circular textile / linnenzorg",
        stated_goal="Flemish maatwerk Genk (circular textile/linnenzorg/maintenance)",
        measured_outcome="empty omzet; bruto JUMP +3.35%; pnl LOSS NARROW +51%; equity DROP -30.5%; FTE 137; filed 30.06.2026",
        absurdity_score="6.2",
        cost_score="4.2",
        difficulty="3.0",
        priority_index="5.18",
        cut_proposal="Publish NBB PDF assets/debt FOI; disclose empty-omzet + equity DROP -30.5% + sustained LOSS vs maatwerk wage-subsidy matrix",
        status="open",
        struck_reason="",
        notes="tick2280 EVERY-10; Medium CW; FOI gap_alternatief_nbb_pdf_assets_debt_empty_omzet_equity_drop_30pct_pnl_loss_narrow_matrix_l5; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Ateliers Avenir@2279; Reset already@2225",
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_alternatief_nbb_pdf_assets_debt_empty_omzet_equity_drop_30pct_pnl_loss_narrow_matrix_l5",
        hierarchy_path="Vlaanderen>Limburg>Genk>Atelier_Alternatief>NBB_PDF_assets_debt_empty_omzet_equity_drop",
        entity_id="vzw_atelier_alternatief_genk",
        what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR4105167; pnl LOSS NARROW EUR-123412; equity DROP to EUR201770 (-30.5%); maatwerk wage-subsidy matrix; FTE 137; activity split textile/linnenzorg/maintenance",
        why_it_matters="Medium CW shows Flemish maatwerk VZW (bruto 4.11m / empty omzet / equity DROP -30.5% / sustained LOSS / FTE 137) under collectief maatwerk Genk path; assets/debt unpublished",
        priority="8",
        recipient_body="Atelier Alternatief VZW",
        recipient_email="info@alternatiefvzw.be",
        recipient_postal="Lucien Londotstraat 3, 3600 Genk",
        draft_letter_path="docs/doge/foi/drafts/gap_alternatief_nbb_pdf_assets_debt_empty_omzet_equity_drop_30pct_pnl_loss_narrow_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        linked_commitment_id="comm_alternatief_jr2025_statutory_maatwerk_bruto_4_11m_equity_drop_30pct",
        linked_leaderboard_id="lb_alternatief_bruto_4_11m_empty_omzet_equity_drop_30pct_pnl_loss_narrow_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2280 EVERY-10; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Foes YE2024; AGB Bornem JR2024; after Ateliers Avenir@2279; next EVERY-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("task_id") == "rq_2280":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = "tick2280 EVERY-10 + Atelier Alternatief Genk YE2025 Medium; bruto JUMP 4.11m / empty omzet / equity DROP -30.5% / LOSS NARROW / FTE 137; progress refresh done"
rows.append({k: "" for k in fields})
rows[-1].update(
    dict(
        task_id="rq_2281",
        title="leftover dual after Atelier Alternatief — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
        sprint="hole_fill",
        priority="8",
        status="open",
        hierarchy_target="L5",
        instructions="leftover dual after rq_2280 Atelier Alternatief YE2025 Medium primary (bruto JUMP 4.11m / empty omzet / equity DROP -30.5% / LOSS NARROW / FTE 137). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Aralea/Manupal/Posthoorn/De Ploeg/Vlotter YE2024; Buseloc YE2024). Do NOT redo Alternatief/Reset/Ateliers de l Avenir/IN-Z/m-accent/AMAB/C.A.R.P. stack.",
        created_utc=utc,
        updated_utc=utc,
        notes="spawned after tick2280 Atelier Alternatief EVERY-10; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2290",
    )
)
seen_open = False
out = []
for row in rows:
    if row.get("task_id") == "rq_2281" and row.get("status") == "open":
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
            last_unit_id="rq_2280",
            ticks_completed="2280",
            paused="no",
            notes="tick2280 EVERY-10 + leftover dual Atelier Alternatief 0465.227.440 Medium (bruto JUMP 4105167 +3.35%; empty omzet; pnl LOSS NARROW -123412; equity DROP 201770 -30.5%; FTE 137; 9 VE Genk maatwerk); after Ateliers Avenir@2279; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2281; next EVERY-10 2290; continuous hole_fill",
        )
    )
print("CSV OK")
