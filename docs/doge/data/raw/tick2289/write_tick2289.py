import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T14:45:00Z"
Path("docs/doge/data/raw/tick2289").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for sid, title, url, pub, klass, notes in [
    (
        "src_op_maat_jr2025_cw_nl",
        "Companyweb NL Op Maat YE2025 statutory",
        "https://www.companyweb.be/nl/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2289; YE2025 empty omzet bruto JUMP 2347442 pnl JUMP 88925 equity JUMP 914553 FTE JUMP 50.5; neerlegging 13.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2289/",
    ),
    (
        "src_op_maat_jr2025_cw_en",
        "Companyweb EN Op Maat YE2025 statutory",
        "https://www.companyweb.be/en/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2289; EN mirror YE2025 Medium; filed 13-06-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 2347442 Profit/Loss 88925 Equity 914553 FTE 50.5",
    ),
    (
        "src_op_maat_jr2025_cw_fr",
        "Companyweb FR Op Maat YE2025 statutory",
        "https://www.companyweb.be/fr/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2289; FR mirror; CA unpublished; Marge brute 2347442; Benefice 88925",
    ),
    (
        "src_op_maat_kbo_2289",
        "KBO Op Maat 0841.138.864 Actief Kuurne 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0841138864",
        "KBO FOD Economie",
        "official_register",
        "tick2289; Actief VZW OP MAAT; zetel Twaalfde-Liniestraat 4 bus 1 8520 Kuurne; 1 VE; RSZ NACE 88.999; geen BTW; dienst persoonlijke assistentie W-Vl",
    ),
    (
        "src_op_maat_site_contact_2289",
        "Op Maat FOI channel info@vzwopmaat.be",
        "https://vzwopmaat.be/",
        "Op Maat VZW",
        "foi_contact",
        "tick2289; info@vzwopmaat.be; +32 56 72 73 06; Twaalfde-Liniestraat 4/1 Kuurne; PAB/persoonlijke assistentie West-Vlaanderen",
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
        entity_id="vzw_op_maat_kuurne",
        name_nl="Op Maat VZW (Kuurne / persoonlijke assistentie W-Vl)",
        name_fr="Op Maat ASBL (Kuurne / assistance personnelle Flandre occidentale)",
        name_en="Op Maat VZW (Kuurne / personal assistance West Flanders disability support)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://vzwopmaat.be/",
        foi_email="info@vzwopmaat.be",
        foi_postal="Twaalfde-Liniestraat 4/1, 8520 Kuurne",
        notes=(
            "tick2289 YE2025 Medium CW NL+EN+FR + Strong KBO 0841.138.864 Actief 1 VE NACE 88.999; empty omzet; "
            "bruto JUMP 2347442 (+10.86%) pnl JUMP 88925 (+29.3%) equity JUMP 914553 (+10.77%) FTE JUMP 50.5; "
            "neerlegging 13.06.2026; assets/debt Unknown; FOI "
            "gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5; "
            "after Village Liegeois@2288; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_op_maat_bruto_jr2025_statutory",
        2347442,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2289; Medium CW; bruto JUMP +10.86% vs YE2024 2117574; omzet unpublished",
    ),
    (
        "bud_op_maat_pnl_jr2025_statutory",
        88925,
        "CW statutory winst/verlies YE2025 JUMP",
        "tick2289; Medium CW; pnl JUMP +29.3% vs YE2024 68775",
    ),
    (
        "bud_op_maat_equity_jr2025_statutory",
        914553,
        "CW statutory eigen_vermogen YE2025 JUMP",
        "tick2289; Medium CW; equity JUMP +10.77% vs YE2024 825628",
    ),
    (
        "bud_op_maat_fte_jr2025_statutory",
        50.5,
        "CW social-balance FTE 50.5",
        "tick2289; Medium CW; FTE 50.5 vs YE2024 46.7; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_op_maat_kuurne",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_op_maat_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_op_maat_jr2025_statutory_pab_bruto_2_35m_empty_omzet",
        title=(
            "Op Maat YE2025 leftover dual (bruto 2.35m / empty omzet / pnl JUMP / equity JUMP / FTE 50.5 / Medium)"
        ),
        entity_id="vzw_op_maat_kuurne",
        beneficiary="personen met handicap W-Vl / persoonlijke assistentie (PAB) clients",
        legal_basis="VZW Op Maat (KBO 0841.138.864; Actief; 1 VE; NACE 88.999; Kuurne; PAB/dienstverlening)",
        decision_date="2026-06-13",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="2347442",
        cash_by_year=(
            '{"2025_omzet":null,"2025_bruto":2347442,"2025_pnl":88925,"2025_equity":914553,"2025_fte":50.5,'
            '"2024_omzet":null,"2024_bruto":2117574,"2024_pnl":68775,"2024_equity":825628,"2024_fte":46.7}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0841138864/op-maat",
        stated_goal="Persoonlijke assistentie West-Vlaanderen (disability home support)",
        cut_option=(
            "Publish NBB PDF assets/debt; reconcile empty omzet + bruto JUMP vs PAB/VAPH subsidy matrix"
        ),
        source_id="src_op_maat_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>JR2025_statutory_L5",
        notes=(
            "tick2289; Medium CW; bruto primary envelope 2347442 (empty omzet); pnl JUMP 88925; equity JUMP 914553; "
            "FTE JUMP 50.5; 1 VE; after Village Liegeois@2288; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            "not TE-additive of 348bn"
        ),
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_op_maat_bruto_2_35m_empty_omzet_pnl_jump_fte_jump_jr2025",
        name=(
            "Op Maat bruto 2.35m / empty omzet / pnl JUMP / FTE JUMP 50.5 "
            "(YE2025 PAB persoonlijke assistentie Kuurne)"
        ),
        level="L5",
        type="pab_vzw_statutory",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>JR2025",
        annual_cost_eur="2347442",
        total_cost_eur="2347442",
        tco_notes=(
            "CW empty omzet / bruto 2347442 (+10.86%) / pnl JUMP 88925 (+29.3%) / equity JUMP 914553 (+10.77%) / "
            "FTE JUMP 50.5 (vs 46.7) / 1 VE PAB W-Vl"
        ),
        confidence="medium",
        source_id="src_op_maat_jr2025_cw_en",
        beneficiaries="personen met handicap West-Vlaanderen / PAB clients",
        stated_goal="Persoonlijke assistentie W-Vl (home disability support)",
        measured_outcome=(
            "empty omzet; bruto JUMP +10.86%; pnl JUMP +29.3%; equity JUMP +10.77%; FTE JUMP 50.5; filed 13.06.2026"
        ),
        absurdity_score="5.5",
        cost_score="3.6",
        difficulty="3.0",
        priority_index="4.55",
        cut_proposal=(
            "Publish NBB PDF assets/debt FOI; disclose empty-omzet + bruto JUMP vs PAB/VAPH subsidy matrix"
        ),
        status="open",
        struck_reason="",
        notes=(
            "tick2289; Medium CW; FOI gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Village Liegeois@2288"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>NBB_PDF_assets_debt_empty_omzet_bruto_jump",
        entity_id="vzw_op_maat_kuurne",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR2347442; "
            "pnl JUMP EUR88925; equity JUMP EUR914553; PAB/VAPH subsidy matrix; FTE 50.5; client/activity split"
        ),
        why_it_matters=(
            "Medium CW shows W-Vl PAB VZW (bruto 2.35m / empty omzet / pnl JUMP / FTE JUMP 50.5) "
            "under persoonlijke-assistentie path; assets/debt unpublished"
        ),
        priority="8",
        recipient_body="Op Maat VZW",
        recipient_email="info@vzwopmaat.be",
        recipient_postal="Twaalfde-Liniestraat 4/1, 8520 Kuurne",
        draft_letter_path="docs/doge/foi/drafts/gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id="comm_op_maat_jr2025_statutory_pab_bruto_2_35m_empty_omzet",
        linked_leaderboard_id="lb_op_maat_bruto_2_35m_empty_omzet_pnl_jump_fte_jump_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2289; ready NOT sent; Medium CW + Strong KBO; FOI email Strong org/Facebook; next every-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_2289":
        if row["status"] == "done" and row.get("entity_id") and row["entity_id"] != "vzw_op_maat_kuurne":
            raise SystemExit(f"rq_2289 already done by other unit: {row.get('title','')[:80]}")
        row.update(
            {
                "title": (
                    "leftover dual — Op Maat YE2025 Medium (bruto JUMP 2.35m / empty omzet / "
                    "pnl JUMP / equity JUMP / FTE 50.5)"
                ),
                "status": "done",
                "entity_id": "vzw_op_maat_kuurne",
                "blocked_gap_id": "gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "leftover dual Op Maat YE2025 FREE W-Vl PAB/persoonlijke assistentie after Village Liegeois@2288; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2289; Op Maat VZW Kuurne 0841.138.864 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet unpublished; bruto JUMP 2347442 (+10.86%); pnl JUMP 88925 (+29.3%); equity JUMP 914553 (+10.77%); "
                    "FTE JUMP 50.5; 1 VE; NACE 88.999; neerlegging 13.06.2026; assets/debt Unknown; FOI ready NOT sent; "
                    "stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Village Liegeois@2288; next EVERY-10 2290"
                ),
            }
        )

if not any(row["task_id"] == "rq_2290" for row in rows):
    rows.append(
        {
            "task_id": "rq_2290",
            "title": (
                "EVERY-10 + leftover dual after Op Maat — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "10",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "EVERY-10 MANDATORY: refresh progress_every_10_ticks.md + doge_waste_top10_current.md then hole-fill ONE unit. "
                "leftover dual after rq_2289 Op Maat YE2025 Medium primary (bruto JUMP 2.35m / empty omzet / pnl JUMP / FTE 50.5). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/De Ploeg/Vlotter/Buseloc YE2024; Roseau Vert/Ateliers Mons/Monceau if YE2025). "
                "Do NOT redo Op Maat/Village Liegeois/De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2289 Op Maat; MUST every-10 at 2290; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024"
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
            "last_unit_id": "rq_2289",
            "ticks_completed": "2289",
            "paused": "no",
            "notes": (
                "tick2289 leftover dual Op Maat 0841.138.864 Medium (bruto JUMP 2347442 +10.86%; empty omzet; "
                "pnl JUMP 88925; equity JUMP 914553; FTE JUMP 50.5; 1 VE Kuurne PAB W-Vl); "
                "after Village Liegeois@2288; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "next rq_2290 EVERY-10; continuous hole_fill"
            ),
        }
    )

print("tick2289 OK")
