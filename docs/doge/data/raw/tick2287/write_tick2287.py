import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T14:15:00Z"
Path("docs/doge/data/raw/tick2287").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for sid, title, url, pub, klass, notes in [
    (
        "src_de_sprong_jr2025_cw_nl",
        "Companyweb NL De Sprong YE2025 statutory",
        "https://www.companyweb.be/nl/0466328686/de-sprong",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2287; YE2025 empty omzet bruto JUMP 4526068 pnl DROP 56628 equity JUMP 2621748 FTE JUMP 110.9; neerlegging 20.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2287/",
    ),
    (
        "src_de_sprong_jr2025_cw_en",
        "Companyweb EN De Sprong YE2025 statutory",
        "https://www.companyweb.be/en/0466328686/de-sprong",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2287; EN mirror YE2025 Medium; filed 20-06-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 4526068 Profit/Loss 56628 Equity 2621748 FTE 110.9",
    ),
    (
        "src_de_sprong_jr2025_cw_fr",
        "Companyweb FR De Sprong YE2025 statutory",
        "https://www.companyweb.be/fr/0466328686/de-sprong",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2287; FR mirror; CA unpublished; Marge brute 4526068; Benefice 56628",
    ),
    (
        "src_de_sprong_kbo_2287",
        "KBO De Sprong 0466.328.686 Actief Meerhout 9 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466328686",
        "KBO FOD Economie",
        "official_register",
        "tick2287; Actief VZW DE SPRONG; zetel Vaartstraat 1 2450 Meerhout; 9 VE; RSZ/BTW NACE 88.993; aanbestedende overheid; absorbed Fietsenatelier Mol 0465.589.508 18.12.2015",
    ),
    (
        "src_de_sprong_site_contact_2287",
        "De Sprong FOI channel info@desprongvzw.be",
        "https://www.desprongvzw.be/contact/",
        "De Sprong VZW",
        "foi_contact",
        "tick2287; info@desprongvzw.be; +32 14 86 98 45; Vaartstraat 1 2450 Meerhout; Kempens maatwerk / On Track Bikes",
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
        entity_id="vzw_de_sprong_meerhout",
        name_nl="De Sprong VZW (Meerhout / Kempens maatwerk)",
        name_fr="De Sprong ASBL (Meerhout / entreprise de travail adapté campinoise)",
        name_en="De Sprong adapted-work VZW (Meerhout Kempen Flemish maatwerk)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.desprongvzw.be/",
        foi_email="info@desprongvzw.be",
        foi_postal="Vaartstraat 1, 2450 Meerhout",
        notes=(
            "tick2287 YE2025 Medium CW NL+EN+FR + Strong KBO 0466.328.686 Actief 9 VE NACE 88.993; empty omzet; "
            "bruto JUMP 4526068 (+6.88%) pnl DROP 56628 (-3.62%) equity JUMP 2621748 (+1.82%) FTE JUMP 110.9; "
            "neerlegging 20.06.2026; assets/debt Unknown; FOI "
            "gap_de_sprong_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_drop_matrix_l5; "
            "after Borgerstein/WEBO@2286; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_de_sprong_bruto_jr2025_statutory",
        4526068,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2287; Medium CW; bruto JUMP +6.88% vs YE2024 4234619; omzet unpublished",
    ),
    (
        "bud_de_sprong_pnl_jr2025_statutory",
        56628,
        "CW statutory winst/verlies YE2025 DROP",
        "tick2287; Medium CW; pnl DROP -3.62% vs YE2024 58754",
    ),
    (
        "bud_de_sprong_equity_jr2025_statutory",
        2621748,
        "CW statutory eigen_vermogen YE2025 JUMP",
        "tick2287; Medium CW; equity JUMP +1.82% vs YE2024 2574854",
    ),
    (
        "bud_de_sprong_fte_jr2025_statutory",
        110.9,
        "CW social-balance FTE 110.9",
        "tick2287; Medium CW; FTE 110.9 vs YE2024 106.4; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_de_sprong_meerhout",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_de_sprong_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_de_sprong_jr2025_statutory_maatwerk_bruto_4_53m_empty_omzet",
        title=(
            "De Sprong YE2025 leftover dual (bruto 4.53m / empty omzet / pnl DROP / equity JUMP / FTE 110.9 / Medium)"
        ),
        entity_id="vzw_de_sprong_meerhout",
        beneficiary="maatwerk workers Kempen Meerhout / On Track Bikes / groen-techniek",
        legal_basis="VZW maatwerk De Sprong (KBO 0466.328.686; Actief; 9 VE; NACE 88.993; Meerhout; aanbestedende overheid)",
        decision_date="2026-06-20",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="4526068",
        cash_by_year=(
            '{"2025_omzet":null,"2025_bruto":4526068,"2025_pnl":56628,"2025_equity":2621748,"2025_fte":110.9,'
            '"2024_omzet":null,"2024_bruto":4234619,"2024_pnl":58754,"2024_equity":2574854,"2024_fte":106.4}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0466328686/de-sprong",
        stated_goal="Kempens maatwerk Meerhout (fiets/groen/techniek inclusive workplaces)",
        cut_option=(
            "Publish NBB PDF assets/debt; reconcile empty omzet + bruto JUMP vs maatwerk wage-subsidy matrix"
        ),
        source_id="src_de_sprong_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Antwerpen>Meerhout>De_Sprong>JR2025_statutory_L5",
        notes=(
            "tick2287; Medium CW; bruto primary envelope 4526068 (empty omzet); pnl DROP 56628; equity JUMP 2621748; "
            "FTE JUMP 110.9; 9 VE; after Borgerstein/WEBO@2286; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            "not TE-additive of 348bn"
        ),
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_de_sprong_bruto_4_53m_empty_omzet_pnl_drop_fte_jump_jr2025",
        name=(
            "De Sprong bruto 4.53m / empty omzet / pnl DROP / FTE JUMP 110.9 "
            "(YE2025 Kempens maatwerk Meerhout)"
        ),
        level="L5",
        type="maatwerk_vzw_statutory",
        hierarchy_path="Vlaanderen>Antwerpen>Meerhout>De_Sprong>JR2025",
        annual_cost_eur="4526068",
        total_cost_eur="4526068",
        tco_notes=(
            "CW empty omzet / bruto 4526068 (+6.88%) / pnl DROP 56628 (-3.62%) / equity JUMP 2621748 (+1.82%) / "
            "FTE JUMP 110.9 (vs 106.4) / 9 VE Kempens maatwerk Meerhout"
        ),
        confidence="medium",
        source_id="src_de_sprong_jr2025_cw_en",
        beneficiaries="maatwerk workers Kempen Meerhout",
        stated_goal="Kempens maatwerk Meerhout (fiets/groen/techniek)",
        measured_outcome=(
            "empty omzet; bruto JUMP +6.88%; pnl DROP -3.62%; equity JUMP +1.82%; FTE JUMP 110.9; filed 20.06.2026"
        ),
        absurdity_score="5.8",
        cost_score="4.4",
        difficulty="3.0",
        priority_index="5.10",
        cut_proposal=(
            "Publish NBB PDF assets/debt FOI; disclose empty-omzet + bruto JUMP vs maatwerk wage-subsidy matrix"
        ),
        status="open",
        struck_reason="",
        notes=(
            "tick2287; Medium CW; FOI gap_de_sprong_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_drop_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Borgerstein/WEBO@2286"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_de_sprong_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_drop_matrix_l5",
        hierarchy_path="Vlaanderen>Antwerpen>Meerhout>De_Sprong>NBB_PDF_assets_debt_empty_omzet_bruto_jump",
        entity_id="vzw_de_sprong_meerhout",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR4526068; "
            "pnl DROP EUR56628; equity JUMP EUR2621748; maatwerk wage-subsidy matrix; FTE 110.9; 9 VE cost allocation"
        ),
        why_it_matters=(
            "Medium CW shows Kempens maatwerk VZW (bruto 4.53m / empty omzet / pnl DROP / FTE JUMP 110.9) "
            "under Meerhout collectief maatwerk path; assets/debt unpublished"
        ),
        priority="8",
        recipient_body="De Sprong VZW",
        recipient_email="info@desprongvzw.be",
        recipient_postal="Vaartstraat 1, 2450 Meerhout",
        draft_letter_path="docs/doge/foi/drafts/gap_de_sprong_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_drop_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id="comm_de_sprong_jr2025_statutory_maatwerk_bruto_4_53m_empty_omzet",
        linked_leaderboard_id="lb_de_sprong_bruto_4_53m_empty_omzet_pnl_drop_fte_jump_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2287; ready NOT sent; Medium CW + Strong KBO; FOI email Strong org site; next every-10 2290",
    ),
)

path = "docs/doge/data/research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

# guard: if 2287 already done by race, abort
for row in rows:
    if row["task_id"] == "rq_2287" and row["status"] == "done":
        raise SystemExit(f"rq_2287 already done: {row.get('title','')[:80]}")

for row in rows:
    if row["task_id"] == "rq_2287":
        row.update(
            {
                "title": (
                    "leftover dual — De Sprong YE2025 Medium (bruto JUMP 4.53m / empty omzet / "
                    "pnl DROP / equity JUMP / FTE 110.9)"
                ),
                "status": "done",
                "entity_id": "vzw_de_sprong_meerhout",
                "blocked_gap_id": "gap_de_sprong_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_drop_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "leftover dual De Sprong YE2025 FREE Kempens maatwerk Meerhout after Borgerstein/WEBO@2286; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2287; De Sprong VZW Meerhout 0466.328.686 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet unpublished; bruto JUMP 4526068 (+6.88%); pnl DROP 56628 (-3.62%); equity JUMP 2621748 (+1.82%); "
                    "FTE JUMP 110.9; 9 VE; NACE 88.993; neerlegging 20.06.2026; assets/debt Unknown; FOI ready NOT sent; "
                    "stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Borgerstein/WEBO@2286; next EVERY-10 2290"
                ),
            }
        )

if not any(row["task_id"] == "rq_2288" for row in rows):
    rows.append(
        {
            "task_id": "rq_2288",
            "title": (
                "leftover dual after De Sprong — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after rq_2287 De Sprong YE2025 Medium primary (bruto JUMP 4.53m / empty omzet / "
                "pnl DROP / FTE 110.9). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/De Ploeg/Vlotter/Buseloc YE2024; Roseau Vert/Village Liegeois/Ateliers Mons if YE2025). "
                "Do NOT redo De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/TWI/Die Zukunft/De Dageraad stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2287 De Sprong; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next every-10 2290"
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
            "last_unit_id": "rq_2287",
            "ticks_completed": "2287",
            "paused": "no",
            "notes": (
                "tick2287 leftover dual De Sprong 0466.328.686 Medium (bruto JUMP 4526068 +6.88%; empty omzet; "
                "pnl DROP 56628; equity JUMP 2621748; FTE JUMP 110.9; 9 VE Meerhout Kempens maatwerk); "
                "after Borgerstein/WEBO@2286; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "next rq_2288; next EVERY-10 2290; continuous hole_fill"
            ),
        }
    )

print("tick2287 OK")
