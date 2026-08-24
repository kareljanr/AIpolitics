import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T15:30:00Z"
Path("docs/doge/data/raw/tick2292").mkdir(parents=True, exist_ok=True)


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
    if row["task_id"] == "rq_2292" and row["status"] == "done":
        raise SystemExit(f"rq_2292 already done: {row.get('title','')[:90]}")

for sid, title, url, pub, klass, notes in [
    (
        "src_labor_jr2025_cw_nl",
        "Companyweb NL Labor Arbeidskansen YE2025 statutory",
        "https://www.companyweb.be/nl/0432385616/labor-arbeidskansen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2292; YE2025 omzet JUMP 4277919 bruto DROP 4812113 pnl LOSS FLIP -1408630 equity DROP 3899262 FTE JUMP 144; neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2292/",
    ),
    (
        "src_labor_jr2025_cw_en",
        "Companyweb EN Labor Arbeidskansen YE2025 statutory",
        "https://www.companyweb.be/en/0432385616/labor-arbeidskansen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2292; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; Turnover 4277919 Profit/Loss -1408630 Equity 3899262 Gross margin 4812113 FTE 144",
    ),
    (
        "src_labor_jr2025_cw_fr",
        "Companyweb FR Labor Arbeidskansen YE2025 statutory",
        "https://www.companyweb.be/fr/0432385616/labor-arbeidskansen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2292; FR mirror; CA 4277919; Marge brute 4812113; Perte -1408630",
    ),
    (
        "src_labor_kbo_2292",
        "KBO Labor Arbeidskansen 0432.385.616 Actief As",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432385616",
        "KBO FOD Economie",
        "official_register",
        "tick2292; Actief VZW Labor Arbeidskansen; zetel Bilzerweg 88 3665 As; NACE 88.993; maatwerk Limburg",
    ),
    (
        "src_labor_site_contact_2292",
        "Labor Arbeidskansen FOI channel info@arbeidskansen.be",
        "https://www.arbeidskansen.be/",
        "Labor Arbeidskansen VZW",
        "foi_contact",
        "tick2292; info@arbeidskansen.be; +32 89 56 85 65; Bilzerweg 88 3665 As; catering/zaalverhuur/maatwerk",
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
        entity_id="vzw_labor_arbeidskansen_as",
        name_nl="Labor Arbeidskansen VZW (As / Flemish maatwerk Limburg)",
        name_fr="Labor Arbeidskansen ASBL (As / entreprise de travail adapté limbourgeoise)",
        name_en="Labor Arbeidskansen adapted-work VZW (As Limburg Flemish maatwerk)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.arbeidskansen.be/",
        foi_email="info@arbeidskansen.be",
        foi_postal="Bilzerweg 88, 3665 As",
        notes=(
            "tick2292 YE2025 Medium CW NL+EN+FR + Strong KBO 0432.385.616 Actief NACE 88.993; "
            "omzet JUMP 4277919 (+58.58%) bruto DROP 4812113 (~1.12x / -3.77%) pnl LOSS FLIP -1408630 "
            "equity DROP 3899262 (-26.63%) FTE JUMP 144; neerlegging 03.07.2026; assets/debt Unknown; "
            "FOI gap_labor_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_equity_drop_matrix_l5; "
            "after Intro Schoonmaak@2291; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_labor_omzet_jr2025_statutory",
        4277919,
        "CW statutory omzet YE2025 JUMP",
        "tick2292; Medium CW; omzet JUMP +58.58% vs YE2024 2697698",
    ),
    (
        "bud_labor_bruto_jr2025_statutory",
        4812113,
        "CW statutory bruto_marge YE2025 DROP",
        "tick2292; Medium CW; bruto DROP -3.77% vs YE2024 5000528; bruto~omzet ~1.12x",
    ),
    (
        "bud_labor_pnl_jr2025_statutory",
        -1408630,
        "CW statutory winst/verlies YE2025 LOSS FLIP",
        "tick2292; Medium CW; pnl LOSS FLIP -390.13% vs YE2024 +485525",
    ),
    (
        "bud_labor_equity_jr2025_statutory",
        3899262,
        "CW statutory eigen_vermogen YE2025 DROP",
        "tick2292; Medium CW; equity DROP -26.63% vs YE2024 5314515",
    ),
    (
        "bud_labor_fte_jr2025_statutory",
        144,
        "CW social-balance FTE 144",
        "tick2292; Medium CW; FTE 144 vs YE2024 120.2; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_labor_arbeidskansen_as",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_labor_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_labor_jr2025_statutory_maatwerk_omzet_4_28m_pnl_loss_flip",
        title=(
            "Labor Arbeidskansen YE2025 leftover dual (omzet JUMP 4.28m / bruto~1.12x / "
            "pnl LOSS FLIP -1.41m / equity DROP -27% / FTE 144 / Medium)"
        ),
        entity_id="vzw_labor_arbeidskansen_as",
        beneficiary="maatwerk workers Limburg As / catering-zaalverhuur clients",
        legal_basis="VZW maatwerk Labor Arbeidskansen (KBO 0432.385.616; Actief; NACE 88.993; As)",
        decision_date="2026-07-03",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="4277919",
        cash_by_year=(
            '{"2025_omzet":4277919,"2025_bruto":4812113,"2025_pnl":-1408630,"2025_equity":3899262,"2025_fte":144,'
            '"2024_omzet":2697698,"2024_bruto":5000528,"2024_pnl":485525,"2024_equity":5314515,"2024_fte":120.2}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0432385616/labor-arbeidskansen",
        stated_goal="Flemish maatwerk As (catering / zaalverhuur / inclusive workplaces)",
        cut_option=(
            "Publish NBB PDF assets/debt; reconcile omzet JUMP +58% with LOSS FLIP -1.41m and equity DROP -27% vs maatwerk wage-subsidy matrix"
        ),
        source_id="src_labor_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Limburg>As>Labor_Arbeidskansen>JR2025_statutory_L5",
        notes=(
            "tick2292; Medium CW; omzet primary envelope 4277919; bruto 4812113 (~1.12x); pnl LOSS FLIP -1408630; "
            "equity DROP 3899262; FTE JUMP 144; after Intro Schoonmaak@2291; AGB Bornem JR2024; FARO YE2024; not TE-additive of 348bn"
        ),
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_labor_omzet_4_28m_pnl_loss_flip_equity_drop_27pct_jr2025",
        name=(
            "Labor Arbeidskansen omzet JUMP 4.28m / pnl LOSS FLIP -1.41m / equity DROP -27% / FTE JUMP 144 "
            "(YE2025 Flemish maatwerk As)"
        ),
        level="L5",
        type="maatwerk_vzw_statutory",
        hierarchy_path="Vlaanderen>Limburg>As>Labor_Arbeidskansen>JR2025",
        annual_cost_eur="4277919",
        total_cost_eur="4277919",
        tco_notes=(
            "CW omzet JUMP 4277919 (+58.58%) / bruto 4812113 (~1.12x / -3.77%) / pnl LOSS FLIP -1408630 "
            "(-390% vs profit 485525) / equity DROP 3899262 (-26.63%) / FTE JUMP 144 (vs 120.2)"
        ),
        confidence="medium",
        source_id="src_labor_jr2025_cw_en",
        beneficiaries="maatwerk workers Limburg As",
        stated_goal="Flemish maatwerk As (catering/zaalverhuur)",
        measured_outcome=(
            "omzet JUMP +59%; bruto DROP -4%; pnl LOSS FLIP -1.41m; equity DROP -27%; FTE JUMP 144; filed 03.07.2026"
        ),
        absurdity_score="7.8",
        cost_score="4.5",
        difficulty="3.0",
        priority_index="6.15",
        cut_proposal=(
            "Publish NBB PDF assets/debt FOI; disclose omzet JUMP + LOSS FLIP + equity DROP vs maatwerk wage-subsidy matrix"
        ),
        status="open",
        struck_reason="",
        notes=(
            "tick2292; Medium CW; FOI gap_labor_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_equity_drop_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Intro Schoonmaak@2291"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_labor_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_equity_drop_matrix_l5",
        hierarchy_path="Vlaanderen>Limburg>As>Labor_Arbeidskansen>NBB_PDF_assets_debt_omzet_jump_pnl_loss_flip",
        entity_id="vzw_labor_arbeidskansen_as",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet JUMP EUR4277919; bruto EUR4812113; "
            "pnl LOSS FLIP EUR-1408630 vs profit EUR485525; equity DROP to EUR3899262 (-26.63%); "
            "maatwerk wage-subsidy matrix; FTE JUMP 144; restructuring/capital publications 2025-2026"
        ),
        why_it_matters=(
            "Medium CW shows Flemish maatwerk VZW with omzet JUMP +59% coinciding with LOSS FLIP -1.41m and equity DROP -27%; "
            "assets/debt unpublished under public loonkost path"
        ),
        priority="8",
        recipient_body="Labor Arbeidskansen VZW",
        recipient_email="info@arbeidskansen.be",
        recipient_postal="Bilzerweg 88, 3665 As",
        draft_letter_path="docs/doge/foi/drafts/gap_labor_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_equity_drop_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id="comm_labor_jr2025_statutory_maatwerk_omzet_4_28m_pnl_loss_flip",
        linked_leaderboard_id="lb_labor_omzet_4_28m_pnl_loss_flip_equity_drop_27pct_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2292; ready NOT sent; Medium CW + Strong KBO; next every-10 2300",
    ),
)

for row in rows:
    if row["task_id"] == "rq_2292":
        row.update(
            {
                "title": (
                    "leftover dual — Labor Arbeidskansen YE2025 Medium "
                    "(omzet JUMP 4.28m / pnl LOSS FLIP -1.41m / equity DROP -27% / FTE 144)"
                ),
                "status": "done",
                "entity_id": "vzw_labor_arbeidskansen_as",
                "blocked_gap_id": "gap_labor_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_equity_drop_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "leftover dual Labor Arbeidskansen YE2025 FREE Flemish maatwerk As after Intro Schoonmaak@2291; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2292; Labor Arbeidskansen VZW As 0432.385.616 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet JUMP 4277919 (+58.58%); bruto DROP 4812113 (~1.12x); pnl LOSS FLIP -1408630; "
                    "equity DROP 3899262 (-26.63%); FTE JUMP 144; NACE 88.993; neerlegging 03.07.2026; "
                    "assets/debt Unknown; FOI ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; "
                    "after Intro Schoonmaak@2291; next EVERY-10 2300"
                ),
            }
        )

if not any(row["task_id"] == "rq_2293" for row in rows):
    rows.append(
        {
            "task_id": "rq_2293",
            "title": (
                "leftover dual after Labor — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after rq_2292 Labor Arbeidskansen YE2025 Medium primary "
                "(omzet JUMP 4.28m / pnl LOSS FLIP -1.41m / equity DROP -27% / FTE 144). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/De Ploeg/Vlotter YE2024; Roseau Vert/Ateliers Mons if YE2025). "
                "Do NOT redo Labor/Intro Schoonmaak/Op Maat/REW/Buseloc/Village Liegeois/De Sprong stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2292 Labor; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2300"
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
            "last_unit_id": "rq_2292",
            "ticks_completed": "2292",
            "paused": "no",
            "notes": (
                "tick2292 leftover dual Labor Arbeidskansen 0432.385.616 Medium (omzet JUMP 4277919 +58.58%; "
                "bruto DROP 4812113 ~1.12x; pnl LOSS FLIP -1408630; equity DROP 3899262 -26.63%; FTE JUMP 144; "
                "As Limburg maatwerk); after Intro Schoonmaak@2291; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "next rq_2293; next EVERY-10 2300; continuous hole_fill"
            ),
        }
    )

print("tick2292 OK")
