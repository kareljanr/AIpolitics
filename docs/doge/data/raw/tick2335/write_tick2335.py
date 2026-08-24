import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-28T02:00:00Z"
Path("docs/doge/data/raw/tick2335").mkdir(parents=True, exist_ok=True)


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
    if row["task_id"] == "rq_2335" and row["status"] == "done":
        raise SystemExit("rq_2335 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_konekt_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        ("src_konekt_jr2025_cw_nl", "Companyweb NL Konekt YE2025 statutory", "https://www.companyweb.be/nl/0524936680/konekt", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2335; YE2025 empty omzet bruto 1871902 pnl DROP 38075 equity JUMP 4726258 FTE 24.5"),
        ("src_konekt_jr2025_cw_en", "Companyweb EN Konekt YE2025 statutory", "https://www.companyweb.be/en/0524936680/konekt", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2335; EN Medium; filed 23-03-2026; Gross 1871902 P/L 38075 Equity 4726258 FTE 24.5"),
        ("src_konekt_jr2025_cw_fr", "Companyweb FR Konekt YE2025 statutory", "https://www.companyweb.be/fr/0524936680/konekt", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2335; FR mirror"),
        ("src_konekt_kbo_2335", "KBO Konekt 0524.936.680", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0524936680", "KBO FOD Economie", "official_register", "tick2335; Actief Gent inclusie/vorming handicap"),
        ("src_konekt_site_contact_2335", "Konekt FOI info@konekt.be", "https://konekt.be/nl/contact", "Konekt VZW", "foi_contact", "tick2335; info@konekt.be; Lijnmolenstraat 153 Gent"),
        ("src_konekt_donorinfo_subs_2024", "Donorinfo Konekt overheidssubsidies 2024 ~1.98m", "https://www.donorinfo.be/nl/doe-een-gift/konekt-vzw", "Donorinfo", "secondary_aggregator", "tick2335; Weak/Medium context: overheidssubsidies EUR1981991 in 2024; YE2025 split Unknown FOI"),
    ]:
        append_csv("docs/doge/data/sources.csv", dict(source_id=sid, title=title, url=url, publisher=pub, accessed_date="2026-08-28", source_class=klass, notes=notes))

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_konekt_gent"):
    append_csv("docs/doge/data/entities.csv", dict(
        entity_id="vzw_konekt_gent",
        name_nl="Konekt VZW (Gent / inclusie + vorming personen met handicap)",
        name_fr="Konekt ASBL (Gand / inclusion + formation personnes handicapées)",
        name_en="Konekt VZW (Ghent / inclusion + training for people with disabilities)",
        level="parastatal", parent_id="sec_flanders", community_language="nl",
        website="https://konekt.be/", foi_email="info@konekt.be", foi_postal="Lijnmolenstraat 153, 9040 Gent",
        notes="tick2335 YE2025 Medium CW + Strong KBO 0524.936.680; empty omzet; bruto 1871902; pnl DROP 38075; equity JUMP 4726258; FTE 24.5; public subsidies opacity (Donorinfo 2024 ~1.98m); FOI gap_konekt_*; after GielsBos@2334; not TE-additive",
    ))

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_konekt_bruto_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_konekt_bruto_jr2025_statutory", 1871902, "CW statutory bruto_marge YE2025 (empty omzet)", "tick2335; Medium CW; bruto +0.1% vs 1870020"),
        ("bud_konekt_pnl_jr2025_statutory", 38075, "CW statutory winst/verlies YE2025 DROP", "tick2335; Medium CW; pnl -33.01% vs 56835"),
        ("bud_konekt_equity_jr2025_statutory", 4726258, "CW statutory eigen_vermogen YE2025 JUMP", "tick2335; Medium CW; equity +10.5% vs 4277210"),
        ("bud_konekt_fte_jr2025_statutory", 24.5, "CW social-balance FTE 24.5", "tick2335; Medium CW; FTE 24.5 vs 25"),
    ]:
        append_csv("docs/doge/data/budgets.csv", dict(budget_id=bid, entity_id="vzw_konekt_gent", year="2025", amount_eur=str(amt), amount_min_eur=str(amt), amount_max_eur=str(amt), basis=basis, source_id="src_konekt_jr2025_cw_en", confidence="medium", notes=notes))

if not has_id("docs/doge/data/commitments.csv", "commitment_id", "comm_konekt_jr2025_statutory_inclusie_bruto_1_87m"):
    append_csv("docs/doge/data/commitments.csv", dict(
        commitment_id="comm_konekt_jr2025_statutory_inclusie_bruto_1_87m",
        title="Konekt YE2025 leftover dual (bruto 1.87m / empty omzet / pnl DROP -33% / FTE 24.5 / Medium)",
        entity_id="vzw_konekt_gent", beneficiary="personen met handicap + netwerk Vlaanderen",
        legal_basis="VZW Konekt (KBO 0524.936.680); overheidssubsidies inclusie/vorming",
        decision_date="2026-03-23", start_year="2025", end_year="2025", total_envelope_eur="1871902",
        cash_by_year='{"2025_omzet":null,"2025_bruto":1871902,"2025_pnl":38075,"2025_equity":4726258,"2025_fte":24.5,"2024_bruto":1870020,"2024_pnl":56835,"2024_equity":4277210,"2024_fte":25,"2024_overheidssubsidies_donorinfo":1981991}',
        remaining_eur="0", status="active", evaluation_url="https://www.companyweb.be/en/0524936680/konekt",
        stated_goal="inclusie + vorming personen met handicap", cut_option="Publish NBB PDF assets/debt FOI; subsidy matrix",
        source_id="src_konekt_jr2025_cw_en", confidence="medium",
        hierarchy_path="Vlaanderen>Oost-Vlaanderen>Gent>Konekt_inclusie>JR2025_statutory_L5",
        notes="tick2335; Medium CW; Donorinfo 2024 overheidssubsidies ~1.98m context; not TE-additive",
    ))

if not has_id("docs/doge/data/leaderboard.csv", "item_id", "lb_konekt_bruto_1_87m_empty_omzet_pnl_drop_jr2025"):
    append_csv("docs/doge/data/leaderboard.csv", dict(
        item_id="lb_konekt_bruto_1_87m_empty_omzet_pnl_drop_jr2025",
        name="Konekt bruto 1.87m / empty omzet / pnl DROP -33% / FTE 24.5 (YE2025 inclusie Gent)",
        level="L5", type="inclusie_vorming_statutory", hierarchy_path="Vlaanderen>Oost-Vlaanderen>Gent>Konekt_inclusie>JR2025",
        annual_cost_eur="1871902", total_cost_eur="1871902",
        tco_notes="CW empty omzet / bruto 1871902 / pnl DROP 38075 / equity JUMP 4726258 / FTE 24.5; Donorinfo 2024 overheidssubsidies ~1.98m",
        confidence="medium", source_id="src_konekt_jr2025_cw_en", beneficiaries="personen met handicap Vlaanderen",
        stated_goal="inclusie + vorming", measured_outcome="empty omzet; bruto flat; pnl DROP -33%; FTE 24.5; filed 23.03.2026",
        absurdity_score="5.2", cost_score="3.5", difficulty="3.0", priority_index="4.35",
        cut_proposal="Publish NBB PDF assets/debt FOI; overheidssubsidie matrix", status="open", struck_reason="",
        notes="tick2335; Medium CW; FOI gap_konekt_*; after GielsBos@2334",
    ))

if not has_id("docs/doge/data/foi_queue.csv", "gap_id", "gap_konekt_nbb_pdf_assets_debt_empty_omzet_pnl_drop_subsidy_matrix_l5"):
    append_csv("docs/doge/data/foi_queue.csv", dict(
        gap_id="gap_konekt_nbb_pdf_assets_debt_empty_omzet_pnl_drop_subsidy_matrix_l5",
        hierarchy_path="Vlaanderen>Oost-Vlaanderen>Gent>Konekt_inclusie>NBB_PDF", entity_id="vzw_konekt_gent",
        what_is_missing="NBB PDF YE2025 assets/debt; empty omzet; bruto 1871902; pnl DROP 38075; overheidssubsidie matrix (Donorinfo 2024 ~1.98m); FTE 24.5",
        why_it_matters="Medium CW inclusie Gent bruto 1.87m empty omzet; public subsidies opaque; assets/debt unknown",
        priority="8", recipient_body="Konekt VZW", recipient_email="info@konekt.be", recipient_postal="Lijnmolenstraat 153, 9040 Gent",
        draft_letter_path="docs/doge/foi/drafts/gap_konekt_nbb_pdf_assets_debt_empty_omzet_pnl_drop_subsidy_matrix_l5.md",
        status="ready", date_ready="2026-08-28", date_sent="", date_due="", date_answered="", response_summary="",
        linked_commitment_id="comm_konekt_jr2025_statutory_inclusie_bruto_1_87m",
        linked_leaderboard_id="lb_konekt_bruto_1_87m_empty_omzet_pnl_drop_jr2025",
        created_utc=utc, updated_utc=utc, notes="tick2335; ready NOT sent",
    ))

for row in rows:
    if row["task_id"] == "rq_2335":
        row.update({
            "title": "leftover dual — Konekt YE2025 Medium (bruto 1.87m / empty omzet / pnl DROP -33% / FTE 24.5)",
            "status": "done", "entity_id": "vzw_konekt_gent",
            "blocked_gap_id": "gap_konekt_nbb_pdf_assets_debt_empty_omzet_pnl_drop_subsidy_matrix_l5",
            "updated_utc": utc, "instructions": "leftover dual Konekt inclusie YE2025 after GielsBos@2334; AGB/FARO/Aralea still YE2024",
            "notes": "tick2335; Konekt 0524.936.680 YE2025 Medium; empty omzet; bruto 1871902; pnl DROP 38075; equity JUMP 4726258; FTE 24.5; FOI ready NOT sent; next EVERY-10 2340",
        })

if not any(row["task_id"] == "rq_2336" for row in rows):
    rows.append({
        "task_id": "rq_2336",
        "title": "leftover dual after Konekt — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
        "instructions": "After Konekt. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae if YE2025). Do NOT redo Konekt/GielsBos/VierNotelaars/Alma/DenBrand stack.",
        "blocked_gap_id": "", "created_utc": utc, "updated_utc": utc, "notes": "spawned after tick2335 Konekt; next every-10 2340",
    })

with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fields})

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id", "ticks_completed", "paused", "notes"], lineterminator="\n")
    w.writeheader()
    w.writerow({
        "state_id": "main", "mode": "continuous", "current_sprint": "hole_fill", "last_tick_utc": utc,
        "last_unit_id": "rq_2335", "ticks_completed": "2335", "paused": "no",
        "notes": "tick2335 leftover dual Konekt 0524.936.680 Medium (empty omzet; bruto 1871902; pnl DROP 38075 -33%; equity JUMP 4726258; FTE 24.5; Gent inclusie); after GielsBos@2334; AGB Bornem JR2024; FARO/AIESH YE2024; next rq_2336; next EVERY-10 2340",
    })

print("tick2335 OK")
