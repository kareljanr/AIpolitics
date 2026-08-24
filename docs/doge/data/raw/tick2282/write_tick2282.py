import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T13:00:00Z"
Path("docs/doge/data/raw/tick2282").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for sid, title, url, pub, klass, notes in [
    (
        "src_die_zukunft_jr2025_cw_nl",
        "Companyweb NL Die Zukunft YE2025 statutory",
        "https://www.companyweb.be/nl/0412748262",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2282; YE2025 omzet JUMP 1278800 bruto JUMP 2280706 (~1.78x) pnl JUMP 134370 equity JUMP 2728815 FTE DROP 73.5; neerlegging 08.05.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2282/",
    ),
    (
        "src_die_zukunft_jr2025_cw_en",
        "Companyweb EN Die Zukunft YE2025 statutory",
        "https://www.companyweb.be/en/0412748262",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2282; EN mirror YE2025 Medium; filed 08-05-2026; Last balance sheet year 2025; Turnover 1278800 Gross margin 2280706 Profit/Loss 134370 Equity 2728815 FTE 73.5",
    ),
    (
        "src_die_zukunft_jr2025_cw_fr",
        "Companyweb FR Die Zukunft YE2025 statutory",
        "https://www.companyweb.be/fr/0412748262",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2282; FR mirror; CA 1278800; Marge brute 2280706; Benefice 134370",
    ),
    (
        "src_die_zukunft_kbo_2282",
        "KBO Die Zukunft 0412.748.262 Actief Amel 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412748262",
        "KBO FOD Economie",
        "official_register",
        "tick2282; Actief VZW Beschutzende Werkstatte-Die Zukunft Amel/Bullingen/Burg Reuland/Butgenbach/Sankt-Vith; zetel Meyerode Jaseberg 12 4770 Amel; 1 VE; NACE 88.993 adapted-work; begindatum 03.11.1972",
    ),
    (
        "src_die_zukunft_site_contact_2282",
        "Die Zukunft FOI channel info@zukunft.be",
        "https://www.zukunft.be/",
        "Die Zukunft VZW",
        "foi_contact",
        "tick2282; info@zukunft.be; +32 80 34 82 10; Meyerode Jaseberg 12 Amel; Ostbelgien ETA DG",
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
        entity_id="vzw_die_zukunft_amel",
        name_nl="Die Zukunft VZW (Amel / Ostbelgien ETA maatwerk)",
        name_fr="Die Zukunft ASBL (Amel / entreprise de travail adapté Ostbelgien)",
        name_en="Die Zukunft adapted-work ASBL (Amel East Belgium ETA)",
        level="parastatal",
        parent_id="sec_wallonia",
        community_language="de",
        website="https://www.zukunft.be/",
        foi_email="info@zukunft.be",
        foi_postal="Meyerode, Jaseberg 12, 4770 Amel",
        notes="tick2282 YE2025 Medium CW NL+EN+FR + Strong KBO 0412.748.262 Actief 1 VE NACE 88.993; omzet JUMP 1278800 (+4.49%) bruto JUMP 2280706 (~1.78x / +4.45%) pnl JUMP 134370 (+116.87%) equity JUMP 2728815 (+2.03%) FTE DROP 73.5; neerlegging 08.05.2026; assets/debt Unknown; FOI gap_die_zukunft_nbb_pdf_assets_debt_bruto_gt_omzet_1_78x_pnl_jump_fte_drop_eta_matrix_l5; after Dageraad/A94/Azalee@2281; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_die_zukunft_omzet_jr2025_statutory",
        1278800,
        "CW statutory omzet YE2025",
        "tick2282; Medium CW; omzet JUMP +4.49% vs YE2024 1223791",
    ),
    (
        "bud_die_zukunft_bruto_jr2025_statutory",
        2280706,
        "CW statutory bruto_marge YE2025 (~1.78x omzet)",
        "tick2282; Medium CW; bruto JUMP +4.45% vs YE2024 2183624; ~1.78x omzet",
    ),
    (
        "bud_die_zukunft_pnl_jr2025_statutory",
        134370,
        "CW statutory winst/verlies YE2025 JUMP",
        "tick2282; Medium CW; pnl JUMP +116.87% vs YE2024 61958",
    ),
    (
        "bud_die_zukunft_equity_jr2025_statutory",
        2728815,
        "CW statutory eigen_vermogen YE2025",
        "tick2282; Medium CW; equity JUMP +2.03% vs YE2024 2674582",
    ),
    (
        "bud_die_zukunft_fte_jr2025_statutory",
        73.5,
        "CW social-balance FTE 73.5",
        "tick2282; Medium CW; FTE 73.5 vs YE2024 77.6; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_die_zukunft_amel",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_die_zukunft_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_die_zukunft_jr2025_statutory_eta_omzet_1_28m_bruto_1_78x",
        title="Die Zukunft YE2025 leftover dual (omzet 1.28m / bruto~1.78x / pnl JUMP / FTE DROP 73.5 / Medium)",
        entity_id="vzw_die_zukunft_amel",
        beneficiary="ETA workers Ostbelgien DG Amel/Bullingen/Burg Reuland/Butgenbach/Sankt-Vith",
        legal_basis="VZW ETA Die Zukunft (KBO 0412.748.262; Actief; 1 VE; NACE 88.993; Amel Meyerode; DG)",
        decision_date="2026-05-08",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="2280706",
        cash_by_year='{"2025_omzet":1278800,"2025_bruto":2280706,"2025_pnl":134370,"2025_equity":2728815,"2025_fte":73.5,"2024_omzet":1223791,"2024_bruto":2183624,"2024_pnl":61958,"2024_equity":2674582,"2024_fte":77.6}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0412748262",
        stated_goal="Ostbelgien ETA / Beschutzende Werkstatte Meyerode (adapted work / DG)",
        cut_option="Publish NBB PDF assets/debt; reconcile bruto>~1.78x omzet + FTE DROP vs ETA wage-subsidy matrix",
        source_id="src_die_zukunft_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Wallonie>DG>Amel>Die_Zukunft>JR2025_statutory_L5",
        notes="tick2282; Medium CW; bruto primary envelope 2280706 (omzet 1278800 ~1.78x); pnl JUMP 134370; equity JUMP 2728815; FTE DROP 73.5; 1 VE; after Dageraad/A94@2281; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn",
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_die_zukunft_omzet_1_28m_bruto_1_78x_pnl_jump_fte_drop_jr2025",
        name="Die Zukunft omzet 1.28m / bruto~1.78x / pnl JUMP / FTE DROP 73.5 (YE2025 Ostbelgien ETA Amel)",
        level="L5",
        type="eta_asbl_statutory",
        hierarchy_path="Wallonie>DG>Amel>Die_Zukunft>JR2025",
        annual_cost_eur="2280706",
        total_cost_eur="2280706",
        tco_notes="CW omzet 1278800 (+4.49%) / bruto 2280706 (~1.78x / +4.45%) / pnl JUMP 134370 (+116.87%) / equity JUMP 2728815 (+2.03%) / FTE DROP 73.5 (vs 77.6) / 1 VE Ostbelgien ETA",
        confidence="medium",
        source_id="src_die_zukunft_jr2025_cw_en",
        beneficiaries="ETA workers Ostbelgien DG Amel catchment",
        stated_goal="Ostbelgien Beschutzende Werkstatte / adapted work DG",
        measured_outcome="omzet JUMP +4.49%; bruto JUMP +4.45% (~1.78x); pnl JUMP +117%; equity JUMP +2%; FTE DROP 73.5; filed 08.05.2026",
        absurdity_score="5.9",
        cost_score="3.8",
        difficulty="3.0",
        priority_index="4.86",
        cut_proposal="Publish NBB PDF assets/debt FOI; disclose ETA wage-subsidy matrix behind bruto>~1.78x omzet + FTE DROP",
        status="open",
        struck_reason="",
        notes="tick2282; Medium CW; FOI gap_die_zukunft_nbb_pdf_assets_debt_bruto_gt_omzet_1_78x_pnl_jump_fte_drop_eta_matrix_l5; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Dageraad/A94@2281",
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_die_zukunft_nbb_pdf_assets_debt_bruto_gt_omzet_1_78x_pnl_jump_fte_drop_eta_matrix_l5",
        hierarchy_path="Wallonie>DG>Amel>Die_Zukunft>NBB_PDF_assets_debt_bruto_gt_omzet_1_78x",
        entity_id="vzw_die_zukunft_amel",
        what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR1278800; bruto EUR2280706 (~1.78x); pnl JUMP EUR134370; FTE DROP to 73.5; ETA wage-subsidy matrix DG; activity split metal/wood/packaging/rufbus",
        why_it_matters="Medium CW shows Ostbelgien ETA VZW (omzet 1.28m / bruto~1.78x / pnl JUMP / FTE DROP) under DG adapted-work path; assets/debt unpublished",
        priority="8",
        recipient_body="Die Zukunft VZW",
        recipient_email="info@zukunft.be",
        recipient_postal="Meyerode, Jaseberg 12, 4770 Amel",
        draft_letter_path="docs/doge/foi/drafts/gap_die_zukunft_nbb_pdf_assets_debt_bruto_gt_omzet_1_78x_pnl_jump_fte_drop_eta_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        linked_commitment_id="comm_die_zukunft_jr2025_statutory_eta_omzet_1_28m_bruto_1_78x",
        linked_leaderboard_id="lb_die_zukunft_omzet_1_28m_bruto_1_78x_pnl_jump_fte_drop_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2282; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Foes YE2024; AGB Bornem JR2024; after Dageraad/A94@2281; next EVERY-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("task_id") == "rq_2282":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["title"] = "leftover dual — Die Zukunft YE2025 Medium (omzet JUMP 1.28m / bruto~1.78x / pnl JUMP / FTE DROP 73.5)"
        row["notes"] = "tick2282 Die Zukunft Amel YE2025 Medium; omzet JUMP 1.28m / bruto~1.78x / pnl JUMP / FTE DROP 73.5"
rows.append({k: "" for k in fields})
rows[-1].update(
    dict(
        task_id="rq_2283",
        title="leftover dual after Die Zukunft — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
        sprint="hole_fill",
        priority="8",
        status="open",
        hierarchy_target="L5",
        instructions="leftover dual after rq_2282 Die Zukunft YE2025 Medium primary (omzet JUMP 1.28m / bruto~1.78x / pnl JUMP / FTE DROP 73.5). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, else unused ETA Roseau Vert/Ateliers Mons/Village Liegeois/Monceau or unused maatwerk WEBO/De Sprong/Aralea if YE2025. Do NOT redo Die Zukunft/De Dageraad/Ateliers du 94/Den Azalee/eurakor/Alternatief/Reset/Ateliers Avenir stack.",
        created_utc=utc,
        updated_utc=utc,
        notes="spawned after tick2282 Die Zukunft; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2290",
    )
)
seen_open = False
out = []
for row in rows:
    if row.get("task_id") == "rq_2283" and row.get("status") == "open":
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
            last_unit_id="rq_2282",
            ticks_completed="2282",
            paused="no",
            notes="tick2282 leftover dual Die Zukunft 0412.748.262 Medium (omzet JUMP 1278800 +4.49%; bruto JUMP 2280706 ~1.78x; pnl JUMP 134370; equity JUMP 2728815; FTE DROP 73.5; 1 VE Amel Ostbelgien ETA); after Dageraad/A94@2281; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2283; next EVERY-10 2290; continuous hole_fill",
        )
    )
print("CSV OK")
