# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)
UTC = "2026-08-25T10:25:00Z"
ENTITY = "asbl_le_bosquet_jolimont"
GAP = "gap_le_bosquet_nbb_pdf_assets_debt_pnl_flip_bruto_matrix_l5"
COMM = "comm_le_bosquet_jr2025_statutory_creche"
LB = "lb_le_bosquet_omzet_jump_3_88m_pnl_flip_bruto_9_95m_jr2025"
SRC_EN = "src_le_bosquet_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_le_bosquet_jr2025_cw",
        "title": "Companyweb NL Le Bosquet YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0463961490/le-bosquet",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2120 EVERY-10; YE2025 omzet JUMP 3879202 pnl FLIP 49091 equity JUMP 5057760 bruto JUMP 9949859 FTE JUMP 161.4; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2120/bosquet_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Le Bosquet YE2025 statutory",
        "url": "https://www.companyweb.be/en/0463961490/le-bosquet",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2120 EVERY-10; EN mirror YE2025 Medium; filed 10-07-2026; Last balance sheet year 2025; FTE 161.4; raw docs/doge/data/raw/tick2120/bosquet_en.html",
    },
    {
        "source_id": "src_le_bosquet_jr2025_cw_fr",
        "title": "Companyweb FR Le Bosquet YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0463961490/le-bosquet",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2120 EVERY-10; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2120/bosquet_fr.html",
    },
    {
        "source_id": "src_le_bosquet_kbo_2120",
        "title": "KBO ASBL Le Bosquet 0463.961.490 Actief La Louviere",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463961490",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2120 EVERY-10; Actief ASBL; Rue Ferrer(PAU) 159 7100 La Louviere; 13 VE; NACE 88.911/86.109; aanbestedende overheid; email secretariat.general@jolimont.be; absorbed Centre de Sante/L Esperance/ABAE/Home des Tout Petits",
    },
    {
        "source_id": "src_le_bosquet_site_2120",
        "title": "Jolimont Pole Enfance (Le Bosquet creches continuum)",
        "url": "https://jolimont.be/enfance",
        "publisher": "Groupe Jolimont",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": "tick2120 EVERY-10; Pôle Enfance creches under Le Bosquet ASBL; FOI via secretariat.general@jolimont.be",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Le Bosquet (Jolimont / Pole Enfance)",
        "name_fr": "ASBL Le Bosquet (Jolimont / Pole Enfance creches)",
        "name_en": "Le Bosquet childcare ASBL (Jolimont Pole Enfance)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://jolimont.be/enfance",
        "foi_email": "secretariat.general@jolimont.be",
        "foi_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "notes": "tick2120 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0463.961.490 Actief ASBL 13 VE NACE 88.911/86.109 aanbestedende overheid; omzet JUMP 3.88m (+10.65%) bruto JUMP 9.95m (+18.01%) pnl FLIP 49k from LOSS -327k equity JUMP 5.06m (+29.96%) FTE JUMP 161.4 (vs 136.3); assets/debt Unknown; filed 10.07.2026; FOI gap_le_bosquet_nbb_pdf_assets_debt_pnl_flip_bruto_matrix_l5; Jolimont Pôle Enfance; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Entraide/Strebo/La Charmille MRS path",
    },
)

for bid, amt, basis in [
    ("bud_le_bosquet_omzet_jr2025_statutory", "3879202", "CW YE2025 omzet / Turnover (primary envelope creche ASBL)"),
    ("bud_le_bosquet_bruto_jr2025_statutory", "9949859", "CW YE2025 Brutomarge / Gross margin (incl. other income)"),
    ("bud_le_bosquet_pnl_jr2025_statutory", "49091", "CW YE2025 Profit/Loss"),
    ("bud_le_bosquet_equity_jr2025_statutory", "5057760", "CW YE2025 Eigen vermogen / Equity"),
    ("bud_le_bosquet_fte_jr2025_statutory", "161.4", "CW social-balance FTE / Employees"),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2120 EVERY-10; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Le Bosquet YE2025 leftover dual (omzet JUMP 3.88m / pnl FLIP / bruto 9.95m)",
        "entity_id": ENTITY,
        "beneficiary": "Childcare / creche users Jolimont Pole Enfance (13 VE)",
        "legal_basis": "ASBL creches/day-care (KBO 0463.961.490; NACE 88.911/86.109; 13 VE; aanbestedende overheid; ONE/AViQ-path)",
        "decision_date": "2026-07-10",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3879202",
        "cash_by_year": '{"2025_omzet":3879202,"2025_bruto":9949859,"2025_pnl":49091,"2025_equity":5057760,"2025_fte":161.4}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0463961490/le-bosquet",
        "stated_goal": "Public-interest childcare / creche operations (Jolimont Pole Enfance)",
        "cut_option": "Publish NBB PDF assets/debt FOI; explain pnl FLIP from -327k + bruto vs omzet gap; map ONE/AViQ vs parent fees; 13 VE + absorption matrix",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>LeBosquet>JR2025_statutory_L5",
        "notes": "tick2120 EVERY-10; Medium CW; omzet primary envelope (bruto 9.95m secondary); assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Entraide/Strebo MRS",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "Le Bosquet omzet JUMP 3.88m / pnl FLIP + bruto 9.95m (YE2025)",
        "level": "L5",
        "type": "creche_statutory_asbl_jolimont",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>LeBosquet>JR2025",
        "annual_cost_eur": "3879202",
        "total_cost_eur": "9949859",
        "tco_notes": "CW YE2025 omzet 3879202 JUMP +10.65% (primary); bruto 9949859 JUMP +18.01%; pnl 49091 FLIP from LOSS -327448; equity 5057760 JUMP +29.96%; FTE 161.4 JUMP; assets/debt Unknown pending NBB PDF; 13 VE Jolimont Pole Enfance",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Creche / childcare users Jolimont Pole Enfance (13 VE)",
        "stated_goal": "Public-interest childcare (ONE/AViQ-path Jolimont)",
        "measured_outcome": "omzet JUMP +10.65%; bruto JUMP +18.01%; pnl FLIP from LOSS; equity JUMP +29.96%; FTE JUMP 161.4",
        "absurdity_score": "6.8",
        "cost_score": "4.2",
        "difficulty": "3.5",
        "priority_index": "5.9",
        "cut_proposal": "FOI NBB PDF + ONE/AViQ vs parent-fee split + explain bruto vs omzet gap and pnl FLIP; 13 VE absorption continuum",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2120 EVERY-10; Medium CW; FOI gap_le_bosquet_nbb_pdf_assets_debt_pnl_flip_bruto_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT Entraide/Strebo MRS",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>LeBosquet>NBB_PDF_assets_debt_pnl_flip_bruto",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP path; bruto vs omzet gap; ONE/AViQ vs parent fees; 13 VE + absorption matrix; dual Jolimont Entraide/Strebo",
        "why_it_matters": "Medium CW shows 3.88m omzet / 9.95m bruto Jolimont creche ASBL (aanbestedende overheid) with pnl FLIP from -327k LOSS and FTE JUMP +18% — childcare-subsidy transparency gap on Jolimont continuum",
        "priority": "8",
        "recipient_body": "ASBL Le Bosquet / Groupe Jolimont",
        "recipient_email": "secretariat.general@jolimont.be",
        "recipient_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "draft_letter_path": "docs/doge/foi/drafts/gap_le_bosquet_nbb_pdf_assets_debt_pnl_flip_bruto_matrix_l5.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick2120 EVERY-10; human-send only; Medium CW; next every-10 2130",
    },
)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2120":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed EVERY-10: progress+top10 refresh + leftover dual Le Bosquet after Strebo; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO 0463.961.490; "
            "omzet JUMP 3.88m bruto JUMP 9.95m pnl FLIP 49k equity JUMP 5.06m FTE JUMP 161.4; FOI ready NBB PDF; DISTINCT Entraide/Strebo"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2120 EVERY-10 Le Bosquet YE2025 Medium CW + progress/top10; FOI ready not sent; next rq_2121; next every-10 2130"
rows.append(
    {
        "task_id": "rq_2121",
        "title": "leftover dual hole-fill after Le Bosquet — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 2121 after Le Bosquet YE2025 Medium EVERY-10. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche. Do NOT redo Le Bosquet, "
            "Strebo Services, Entraide Fraternelle Jolimont, La Charmille Pont-a-Celles, Residence Les Charmilles Sambreville, "
            "Les Sittelles Chastre, Les Buissons / Chateau Sous Bois Spa, Residence 3 / Saphir, Elisabeth Aan Zee Oostende, "
            "Maison de Repos du XXe Aout / PLIMCO, Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, "
            "IDELUX*, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, "
            "AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, "
            "AGB Bornem, Armonea, emeis."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick2120 Le Bosquet EVERY-10; FARO/AIESH/REW still YE2024; next every-10 2130",
    }
)
with open(rq_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

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
            "last_tick_utc": UTC,
            "last_unit_id": "rq_2120",
            "ticks_completed": "2120",
            "paused": "no",
            "notes": (
                "tick2120 EVERY-10 leftover Le Bosquet 0463.961.490 Medium CW "
                "(omzet JUMP 3.88m bruto JUMP 9.95m pnl FLIP 49k equity JUMP 5.06m FTE JUMP 161.4; "
                "assets/debt Unknown; 13 VE NACE 88.911/86.109 Jolimont Pole Enfance) + progress/top10 refresh; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Strebo/Entraide taken; next rq_2121; next every-10 2130; continuous hole_fill"
            ),
        }
    )

print("OK tick2120 writes")
