import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-28T02:30:00Z"
Path("docs/doge/data/raw/tick2336").mkdir(parents=True, exist_ok=True)


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
    if row["task_id"] == "rq_2336" and row["status"] == "done":
        raise SystemExit("rq_2336 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_cirkel_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        ("src_cirkel_jr2025_cw_nl", "Companyweb NL De Cirkel Maatwerk YE2025", "https://www.companyweb.be/nl/0470413079/de-cirkel-maatwerkbedrijf", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2336; YE2025 empty omzet bruto 2375418 pnl JUMP 188524 equity 3118706 FTE 54.3"),
        ("src_cirkel_jr2025_cw_en", "Companyweb EN De Cirkel Maatwerk YE2025", "https://www.companyweb.be/en/0470413079/de-cirkel-maatwerkbedrijf", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2336; EN Medium; filed 16-06-2026"),
        ("src_cirkel_jr2025_cw_fr", "Companyweb FR De Cirkel Maatwerk YE2025", "https://www.companyweb.be/fr/0470413079/de-cirkel-maatwerkbedrijf", "Companyweb (NBB-derived)", "secondary_aggregator", "tick2336; FR mirror"),
        ("src_cirkel_kbo_2336", "KBO De Cirkel 0470.413.079", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0470413079", "KBO FOD Economie", "official_register", "tick2336; Actief Lokeren maatwerk"),
        ("src_cirkel_site_contact_2336", "De Cirkel FOI info@kringwinkeldecirkel.be", "https://www.desocialekaart.be/de-kringwinkel-de-cirkel-sociale-werkplaats-de-cirkel-lokeren-521576", "Kringwinkel De Cirkel", "foi_contact", "tick2336; info@kringwinkeldecirkel.be"),
    ]:
        append_csv("docs/doge/data/sources.csv", dict(source_id=sid, title=title, url=url, publisher=pub, accessed_date="2026-08-28", source_class=klass, notes=notes))

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_de_cirkel_lokeren"):
    append_csv("docs/doge/data/entities.csv", dict(
        entity_id="vzw_de_cirkel_lokeren",
        name_nl="De Cirkel - Maatwerkbedrijf VZW (Lokeren / Kringwinkel)",
        name_fr="De Cirkel - Entreprise de travail adapté ASBL (Lokeren)",
        name_en="De Cirkel - Adapted work enterprise VZW (Lokeren)",
        level="parastatal", parent_id="sec_flanders", community_language="nl",
        website="https://www.kringwinkel.be/", foi_email="info@kringwinkeldecirkel.be", foi_postal="Bobijnerslaan 3, 9160 Lokeren",
        notes="tick2336 YE2025 Medium CW + Strong KBO 0470.413.079; empty omzet; bruto JUMP 2375418; pnl JUMP 188524; equity JUMP 3118706; FTE JUMP 54.3; FOI gap_cirkel_*; after WWPA@2335; not TE-additive",
    ))

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_cirkel_bruto_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_cirkel_bruto_jr2025_statutory", 2375418, "CW statutory bruto_marge YE2025 (empty omzet)", "tick2336; Medium CW; bruto +7.8% vs 2203456"),
        ("bud_cirkel_pnl_jr2025_statutory", 188524, "CW statutory winst/verlies YE2025 JUMP", "tick2336; Medium CW; pnl +32.33% vs 142468"),
        ("bud_cirkel_equity_jr2025_statutory", 3118706, "CW statutory eigen_vermogen YE2025 JUMP", "tick2336; Medium CW; equity +6.16% vs 2937731"),
        ("bud_cirkel_fte_jr2025_statutory", 54.3, "CW social-balance FTE 54.3", "tick2336; Medium CW; FTE JUMP vs 51"),
    ]:
        append_csv("docs/doge/data/budgets.csv", dict(budget_id=bid, entity_id="vzw_de_cirkel_lokeren", year="2025", amount_eur=str(amt), amount_min_eur=str(amt), amount_max_eur=str(amt), basis=basis, source_id="src_cirkel_jr2025_cw_en", confidence="medium", notes=notes))

if not has_id("docs/doge/data/commitments.csv", "commitment_id", "comm_cirkel_jr2025_statutory_maatwerk_bruto_2_38m"):
    append_csv("docs/doge/data/commitments.csv", dict(
        commitment_id="comm_cirkel_jr2025_statutory_maatwerk_bruto_2_38m",
        title="De Cirkel YE2025 leftover dual (bruto JUMP 2.38m / empty omzet / pnl JUMP +32% / FTE 54.3 / Medium)",
        entity_id="vzw_de_cirkel_lokeren", beneficiary="doelgroepwerknemers Waasland / kringloop",
        legal_basis="VZW De Cirkel - Maatwerkbedrijf (KBO 0470.413.079)",
        decision_date="2026-06-16", start_year="2025", end_year="2025", total_envelope_eur="2375418",
        cash_by_year='{"2025_omzet":null,"2025_bruto":2375418,"2025_pnl":188524,"2025_equity":3118706,"2025_fte":54.3,"2024_bruto":2203456,"2024_pnl":142468,"2024_equity":2937731,"2024_fte":51}',
        remaining_eur="0", status="active", evaluation_url="https://www.companyweb.be/en/0470413079/de-cirkel-maatwerkbedrijf",
        stated_goal="maatwerk + kringwinkel De Cirkel", cut_option="Publish NBB PDF assets/debt FOI",
        source_id="src_cirkel_jr2025_cw_en", confidence="medium",
        hierarchy_path="Vlaanderen>Oost-Vlaanderen>Lokeren>De_Cirkel_maatwerk>JR2025_statutory_L5",
        notes="tick2336; Medium CW; after WWPA@2335; not TE-additive",
    ))

if not has_id("docs/doge/data/leaderboard.csv", "item_id", "lb_cirkel_bruto_2_38m_empty_omzet_pnl_jump_jr2025"):
    append_csv("docs/doge/data/leaderboard.csv", dict(
        item_id="lb_cirkel_bruto_2_38m_empty_omzet_pnl_jump_jr2025",
        name="De Cirkel bruto JUMP 2.38m / empty omzet / pnl JUMP +32% / FTE 54.3 (YE2025 maatwerk Lokeren)",
        level="L5", type="maatwerk_vzw_statutory", hierarchy_path="Vlaanderen>Oost-Vlaanderen>Lokeren>De_Cirkel_maatwerk>JR2025",
        annual_cost_eur="2375418", total_cost_eur="2375418",
        tco_notes="CW empty omzet / bruto JUMP 2375418 / pnl JUMP 188524 / equity JUMP 3118706 / FTE JUMP 54.3",
        confidence="medium", source_id="src_cirkel_jr2025_cw_en", beneficiaries="doelgroepwerknemers Waasland",
        stated_goal="maatwerk kringwinkel", measured_outcome="empty omzet; bruto +7.8%; pnl JUMP +32%; FTE 54.3; filed 16.06.2026",
        absurdity_score="5.0", cost_score="3.5", difficulty="3.0", priority_index="4.25",
        cut_proposal="Publish NBB PDF assets/debt FOI; maatwerk subsidy matrix", status="open", struck_reason="",
        notes="tick2336; Medium CW; FOI gap_cirkel_*; after WWPA@2335",
    ))

if not has_id("docs/doge/data/foi_queue.csv", "gap_id", "gap_cirkel_nbb_pdf_assets_debt_empty_omzet_pnl_jump_maatwerk_matrix_l5"):
    append_csv("docs/doge/data/foi_queue.csv", dict(
        gap_id="gap_cirkel_nbb_pdf_assets_debt_empty_omzet_pnl_jump_maatwerk_matrix_l5",
        hierarchy_path="Vlaanderen>Oost-Vlaanderen>Lokeren>De_Cirkel_maatwerk>NBB_PDF", entity_id="vzw_de_cirkel_lokeren",
        what_is_missing="NBB PDF YE2025 assets/debt; empty omzet; bruto 2375418; pnl JUMP 188524; maatwerk subsidy matrix; FTE 54.3",
        why_it_matters="Medium CW maatwerk Lokeren bruto 2.38m empty omzet; assets/debt unknown",
        priority="8", recipient_body="De Cirkel - Maatwerkbedrijf VZW", recipient_email="info@kringwinkeldecirkel.be",
        recipient_postal="Bobijnerslaan 3, 9160 Lokeren",
        draft_letter_path="docs/doge/foi/drafts/gap_cirkel_nbb_pdf_assets_debt_empty_omzet_pnl_jump_maatwerk_matrix_l5.md",
        status="ready", date_ready="2026-08-28", date_sent="", date_due="", date_answered="", response_summary="",
        linked_commitment_id="comm_cirkel_jr2025_statutory_maatwerk_bruto_2_38m",
        linked_leaderboard_id="lb_cirkel_bruto_2_38m_empty_omzet_pnl_jump_jr2025",
        created_utc=utc, updated_utc=utc, notes="tick2336; ready NOT sent",
    ))

for row in rows:
    if row["task_id"] == "rq_2336":
        row.update({
            "title": "leftover dual — De Cirkel Lokeren YE2025 Medium (empty omzet / bruto JUMP 2.38m / pnl JUMP +32% / FTE 54.3)",
            "status": "done", "entity_id": "vzw_de_cirkel_lokeren",
            "blocked_gap_id": "gap_cirkel_nbb_pdf_assets_debt_empty_omzet_pnl_jump_maatwerk_matrix_l5",
            "updated_utc": utc, "instructions": "leftover dual De Cirkel maatwerk YE2025 after WWPA@2335",
            "notes": "tick2336; De Cirkel 0470.413.079 YE2025 Medium; empty omzet; bruto JUMP 2375418; pnl JUMP 188524; equity JUMP 3118706; FTE JUMP 54.3; FOI ready NOT sent; next EVERY-10 2340",
        })

if not any(row["task_id"] == "rq_2337" for row in rows):
    rows.append({
        "task_id": "rq_2337",
        "title": "leftover dual after De Cirkel — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
        "instructions": "After De Cirkel. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae/Konekt if YE2025). Do NOT redo De Cirkel/WWPA/GielsBos/VierNotelaars stack.",
        "blocked_gap_id": "", "created_utc": utc, "updated_utc": utc, "notes": "spawned after tick2336 De Cirkel; next every-10 2340",
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
        "last_unit_id": "rq_2336", "ticks_completed": "2336", "paused": "no",
        "notes": "tick2336 leftover dual De Cirkel 0470.413.079 Medium (empty omzet; bruto JUMP 2375418; pnl JUMP 188524 +32%; equity JUMP 3118706; FTE JUMP 54.3; Lokeren maatwerk); after WWPA@2335; AGB Bornem JR2024; FARO YE2024; next rq_2337; next EVERY-10 2340",
    })

print("tick2336 OK")
