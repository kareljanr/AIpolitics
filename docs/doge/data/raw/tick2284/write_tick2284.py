import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T13:30:00Z"
Path("docs/doge/data/raw/tick2284").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for sid, title, url, pub, klass, notes in [
    (
        "src_mobiel_jr2025_cw_nl",
        "Companyweb NL Mobiel Sociale Werkplaats YE2025 statutory",
        "https://www.companyweb.be/nl/0860293493/mobiel-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2284; YE2025 empty omzet bruto JUMP 1650782 pnl PROFIT FLIP 49126 equity JUMP 156824 FTE JUMP 34; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2284/",
    ),
    (
        "src_mobiel_jr2025_cw_en",
        "Companyweb EN Mobiel Sociale Werkplaats YE2025 statutory",
        "https://www.companyweb.be/en/0860293493/mobiel-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2284; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 1650782 Profit/Loss 49126 Equity 156824 FTE 34",
    ),
    (
        "src_mobiel_jr2025_cw_fr",
        "Companyweb FR Mobiel Sociale Werkplaats YE2025 statutory",
        "https://www.companyweb.be/fr/0860293493/mobiel-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2284; FR mirror; CA unpublished; Marge brute 1650782; Benefice 49126",
    ),
    (
        "src_mobiel_kbo_2284",
        "KBO Mobiel Sociale Werkplaats 0860.293.493 Actief Kortrijk",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860293493",
        "KBO FOD Economie",
        "official_register",
        "tick2284; Actief VZW Mobiel Sociale Werkplaats; zetel Minister Tacklaan 57 8500 Kortrijk; NACE 88.993; begindatum 30.06.2003; part of Deltagroep cluster",
    ),
    (
        "src_mobiel_site_contact_2284",
        "Mobiel FOI channel info@mobiel.be",
        "https://mobiel.be/",
        "Mobiel Sociale Werkplaats VZW",
        "foi_contact",
        "tick2284; info@mobiel.be; +32 56 24 99 10; Minister Tacklaan 57 Kortrijk; fietsencentrum/maatwerk Deltagroep",
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
        entity_id="vzw_mobiel_sociale_werkplaats_kortrijk",
        name_nl="Mobiel Sociale Werkplaats VZW (Kortrijk / Flemish maatwerk fietsencentrum)",
        name_fr="Mobiel Sociale Werkplaats ASBL (Courtrai / entreprise de travail adapté / vélos)",
        name_en="Mobiel Sociale Werkplaats adapted-work VZW (Kortrijk Flemish maatwerk bike centre)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://mobiel.be/",
        foi_email="info@mobiel.be",
        foi_postal="Minister Tacklaan 57, 8500 Kortrijk",
        notes=(
            "tick2284 YE2025 Medium CW NL+EN+FR + Strong KBO 0860.293.493 Actief NACE 88.993; empty omzet; "
            "bruto JUMP 1650782 (+10.19%) pnl PROFIT FLIP 49126 equity JUMP 156824 (+16.24%) FTE JUMP 34; "
            "neerlegging 02.07.2026; assets/debt Unknown; FOI "
            "gap_mobiel_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_equity_jump_matrix_l5; "
            "after Ateljee@2283; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_mobiel_bruto_jr2025_statutory",
        1650782,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2284; Medium CW; bruto JUMP +10.19% vs YE2024 1498125; omzet unpublished",
    ),
    (
        "bud_mobiel_pnl_jr2025_statutory",
        49126,
        "CW statutory winst/verlies YE2025 PROFIT FLIP",
        "tick2284; Medium CW; pnl PROFIT FLIP +213.45% vs YE2024 -43301",
    ),
    (
        "bud_mobiel_equity_jr2025_statutory",
        156824,
        "CW statutory eigen_vermogen YE2025 JUMP",
        "tick2284; Medium CW; equity JUMP +16.24% vs YE2024 134908",
    ),
    (
        "bud_mobiel_fte_jr2025_statutory",
        34,
        "CW social-balance FTE 34",
        "tick2284; Medium CW; FTE 34 vs YE2024 31.4; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_mobiel_sociale_werkplaats_kortrijk",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_mobiel_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_mobiel_jr2025_statutory_maatwerk_bruto_1_65m_pnl_profit_flip",
        title=(
            "Mobiel Sociale Werkplaats YE2025 leftover dual (bruto 1.65m / empty omzet / "
            "pnl PROFIT FLIP / equity JUMP / FTE 34 / Medium)"
        ),
        entity_id="vzw_mobiel_sociale_werkplaats_kortrijk",
        beneficiary="maatwerk workers Kortrijk / fietsencentrum / Deltagroep social-economy cluster",
        legal_basis="VZW maatwerk Mobiel Sociale Werkplaats (KBO 0860.293.493; Actief; NACE 88.993; Kortrijk)",
        decision_date="2026-07-02",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="1650782",
        cash_by_year=(
            '{"2025_omzet":null,"2025_bruto":1650782,"2025_pnl":49126,"2025_equity":156824,"2025_fte":34,'
            '"2024_omzet":null,"2024_bruto":1498125,"2024_pnl":-43301,"2024_equity":134908,"2024_fte":31.4}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0860293493/mobiel-sociale-werkplaats",
        stated_goal="Flemish maatwerk Kortrijk (fietsencentrum / mobility social workshop)",
        cut_option=(
            "Publish NBB PDF assets/debt; reconcile empty omzet + PROFIT FLIP + equity JUMP vs maatwerk wage-subsidy matrix"
        ),
        source_id="src_mobiel_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Mobiel>JR2025_statutory_L5",
        notes=(
            "tick2284; Medium CW; bruto primary envelope 1650782 (empty omzet); pnl PROFIT FLIP 49126; "
            "equity JUMP 156824; FTE 34; after Ateljee@2283; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            "not TE-additive of 348bn"
        ),
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_mobiel_bruto_1_65m_empty_omzet_pnl_profit_flip_equity_jump_jr2025",
        name=(
            "Mobiel Sociale Werkplaats bruto 1.65m / empty omzet / pnl PROFIT FLIP / equity JUMP / FTE 34 "
            "(YE2025 Flemish maatwerk Kortrijk)"
        ),
        level="L5",
        type="maatwerk_vzw_statutory",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Mobiel>JR2025",
        annual_cost_eur="1650782",
        total_cost_eur="1650782",
        tco_notes=(
            "CW empty omzet / bruto 1650782 (+10.19%) / pnl PROFIT FLIP 49126 (+213% vs loss -43301) / "
            "equity JUMP 156824 (+16.24%) / FTE JUMP 34 (vs 31.4) / Kortrijk fietsencentrum maatwerk"
        ),
        confidence="medium",
        source_id="src_mobiel_jr2025_cw_en",
        beneficiaries="maatwerk workers Kortrijk / bike-centre clients",
        stated_goal="Flemish maatwerk Kortrijk (fietsencentrum)",
        measured_outcome=(
            "empty omzet; bruto JUMP +10.19%; pnl PROFIT FLIP; equity JUMP +16%; FTE JUMP 34; filed 02.07.2026"
        ),
        absurdity_score="6.0",
        cost_score="3.2",
        difficulty="3.0",
        priority_index="4.60",
        cut_proposal=(
            "Publish NBB PDF assets/debt FOI; disclose empty-omzet + PROFIT FLIP vs maatwerk wage-subsidy matrix"
        ),
        status="open",
        struck_reason="",
        notes=(
            "tick2284; Medium CW; FOI gap_mobiel_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_equity_jump_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Ateljee@2283"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_mobiel_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_equity_jump_matrix_l5",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Mobiel>NBB_PDF_assets_debt_empty_omzet_pnl_profit_flip",
        entity_id="vzw_mobiel_sociale_werkplaats_kortrijk",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR1650782; "
            "pnl PROFIT FLIP EUR49126 vs loss EUR-43301; equity JUMP to EUR156824; maatwerk wage-subsidy matrix; "
            "FTE 34; Deltagroep related-party map"
        ),
        why_it_matters=(
            "Medium CW shows Flemish maatwerk VZW (bruto 1.65m / empty omzet / pnl PROFIT FLIP / equity JUMP / FTE 34) "
            "under Kortrijk fietsencentrum path; assets/debt unpublished"
        ),
        priority="8",
        recipient_body="Mobiel Sociale Werkplaats VZW",
        recipient_email="info@mobiel.be",
        recipient_postal="Minister Tacklaan 57, 8500 Kortrijk",
        draft_letter_path="docs/doge/foi/drafts/gap_mobiel_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_equity_jump_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id="comm_mobiel_jr2025_statutory_maatwerk_bruto_1_65m_pnl_profit_flip",
        linked_leaderboard_id="lb_mobiel_bruto_1_65m_empty_omzet_pnl_profit_flip_equity_jump_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2284; ready NOT sent; Medium CW + Strong KBO; FOI email Strong org site; next every-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2284":
        row.update(
            {
                "title": (
                    "leftover dual — Mobiel Sociale Werkplaats YE2025 Medium "
                    "(bruto JUMP 1.65m / empty omzet / pnl PROFIT FLIP / equity JUMP / FTE 34)"
                ),
                "status": "done",
                "entity_id": "vzw_mobiel_sociale_werkplaats_kortrijk",
                "blocked_gap_id": "gap_mobiel_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_equity_jump_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "leftover dual Mobiel YE2025 FREE Flemish maatwerk Kortrijk after Ateljee@2283; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2284; Mobiel Sociale Werkplaats VZW Kortrijk 0860.293.493 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet unpublished; bruto JUMP 1650782 (+10.19%); pnl PROFIT FLIP 49126; equity JUMP 156824 (+16.24%); "
                    "FTE JUMP 34; NACE 88.993; neerlegging 02.07.2026; assets/debt Unknown; FOI ready NOT sent; "
                    "stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Ateljee@2283; next EVERY-10 2290"
                ),
            }
        )
if not any(row["task_id"] == "rq_2285" for row in rows):
    rows.append(
        {
            "task_id": "rq_2285",
            "title": (
                "leftover dual after Mobiel — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after rq_2284 Mobiel YE2025 Medium primary (bruto JUMP 1.65m / empty omzet / "
                "pnl PROFIT FLIP / FTE 34). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/Posthoorn/De Ploeg/Vlotter/Buseloc YE2024; WEBO/De Sprong/Roseau Vert/Village Liegeois if YE2025). "
                "Do NOT redo Mobiel/Ateljee/TWI/Die Zukunft/De Dageraad/Ateliers du 94/eurakor/Alternatief stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2284 Mobiel; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2290"
            ),
        }
    )
with open(path, "w", newline="", encoding="utf-8") as f:
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
            "last_unit_id": "rq_2284",
            "ticks_completed": "2284",
            "paused": "no",
            "notes": (
                "tick2284 leftover dual Mobiel Sociale Werkplaats 0860.293.493 Medium "
                "(bruto JUMP 1650782 +10.19%; empty omzet; pnl PROFIT FLIP 49126; equity JUMP 156824; FTE JUMP 34; "
                "Kortrijk fietsencentrum maatwerk); after Ateljee@2283; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "next rq_2285; next EVERY-10 2290; continuous hole_fill"
            ),
        }
    )

print("tick2284 OK")
