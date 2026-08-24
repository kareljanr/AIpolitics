# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)
UTC = "2026-08-25T10:10:00Z"
ENTITY = "bv_strebo_services_jolimont"
GAP = "gap_strebo_nbb_pdf_assets_debt_pnl_drop_near_zero_matrix_l5"
COMM = "comm_strebo_jr2025_statutory_mrs"
LB = "lb_strebo_omzet_jump_2_41m_pnl_drop_near_zero_jr2025"
SRC_EN = "src_strebo_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_strebo_jr2025_cw",
        "title": "Companyweb NL Strebo Services YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0899812184/strebo-services",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2119; YE2025 omzet JUMP 2407319 pnl DROP 8892 equity JUMP 453285 bruto JUMP 2252638 FTE 26.5; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2119/strebo_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Strebo Services YE2025 statutory",
        "url": "https://www.companyweb.be/en/0899812184/strebo-services",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2119; EN mirror YE2025 Medium; filed 10-07-2026; Last balance sheet year 2025; FTE 26.5; raw docs/doge/data/raw/tick2119/strebo_en.html",
    },
    {
        "source_id": "src_strebo_jr2025_cw_fr",
        "title": "Companyweb FR Strebo Services YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0899812184/strebo-services",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2119; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2119/strebo_fr.html",
    },
    {
        "source_id": "src_strebo_kbo_2119",
        "title": "KBO Strebo Services 0899.812.184 Actief La Louviere",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0899812184",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2119; Actief SRL/BV; Rue Ferrer(PAU) 159 7100 La Louviere; 2 VE; NACE 87.101/87.301; aanbestedende overheid; absorbed DE SARS 0454.385.018 since 06.01.2022; same board path as Entraide Fraternelle",
    },
    {
        "source_id": "src_strebo_site_2119",
        "title": "Jolimont Pole Senior maisons de repos (Strebo Le Rambour / Le Planty)",
        "url": "https://jolimont.be/maisons-de-repos",
        "publisher": "Groupe Jolimont",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": "tick2119; Le Rambour + Le Planty under Strebo SRL; FOI via secretariat.general@jolimont.be",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Strebo Services (Jolimont / Le Rambour)",
        "name_fr": "Strebo Services SRL (Jolimont / Le Rambour / Le Planty)",
        "name_en": "Strebo Services nursing-home SRL (Jolimont Pole Senior)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://jolimont.be/maisons-de-repos",
        "foi_email": "secretariat.general@jolimont.be",
        "foi_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "notes": "tick2119 YE2025 Medium CW NL+EN+FR + Strong KBO 0899.812.184 Actief SRL/BV 2 VE NACE 87.101/87.301 aanbestedende overheid; omzet JUMP 2.41m (+5.88%) bruto JUMP 2.25m (+7.16%) pnl DROP 8892 (-86.06% near-zero) equity JUMP 0.45m (+1.66%) FTE JUMP 26.5 (vs 25.8); assets/debt Unknown; filed 10.07.2026; FOI gap_strebo_nbb_pdf_assets_debt_pnl_drop_near_zero_matrix_l5; Le Rambour+Le Planty; dual Entraide Fraternelle ASBL; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Entraide/La Charmille",
    },
)

for bid, amt, basis in [
    ("bud_strebo_omzet_jr2025_statutory", "2407319", "CW YE2025 omzet / Turnover (primary envelope MRS SRL)"),
    ("bud_strebo_bruto_jr2025_statutory", "2252638", "CW YE2025 Brutomarge / Gross margin"),
    ("bud_strebo_pnl_jr2025_statutory", "8892", "CW YE2025 Profit/Loss"),
    ("bud_strebo_equity_jr2025_statutory", "453285", "CW YE2025 Eigen vermogen / Equity"),
    ("bud_strebo_fte_jr2025_statutory", "26.5", "CW social-balance FTE / Employees"),
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
            "notes": "tick2119; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Strebo Services YE2025 leftover dual (omzet JUMP 2.41m / pnl DROP near-zero)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Le Rambour / Le Planty (Jolimont Pole Senior)",
        "legal_basis": "SRL/BV maison de repos RVT/ROB (KBO 0899.812.184; NACE 87.101/87.301; 2 VE; aanbestedende overheid; AViQ)",
        "decision_date": "2026-07-10",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2407319",
        "cash_by_year": '{"2025_omzet":2407319,"2025_bruto":2252638,"2025_pnl":8892,"2025_equity":453285,"2025_fte":26.5}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0899812184/strebo-services",
        "stated_goal": "Public-interest nursing-home care (Le Rambour / Le Planty; Jolimont; AViQ-path)",
        "cut_option": "Publish NBB PDF assets/debt FOI; explain pnl DROP -86% near-zero despite omzet JUMP; map AViQ/INAMI vs omzet; 2 VE + Entraide dual",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>StreboServices>JR2025_statutory_L5",
        "notes": "tick2119; Medium CW; omzet primary envelope; assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Entraide Fraternelle / La Charmille",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "Strebo Services omzet JUMP 2.41m / pnl DROP 8.9k near-zero -86% (YE2025)",
        "level": "L5",
        "type": "mrs_statutory_srl_jolimont",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>StreboServices>JR2025",
        "annual_cost_eur": "2407319",
        "total_cost_eur": "2407319",
        "tco_notes": "CW YE2025 omzet 2407319 JUMP +5.88% (primary); bruto 2252638 JUMP +7.16%; pnl 8892 DROP -86.06% vs 63787 (near-zero); equity 453285 JUMP +1.66%; FTE 26.5; assets/debt Unknown pending NBB PDF; 2 VE Le Rambour/Le Planty",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Le Rambour / Le Planty (2 VE)",
        "stated_goal": "Public-interest nursing-home care (AViQ-path Jolimont Strebo)",
        "measured_outcome": "omzet JUMP +5.88%; bruto JUMP +7.16%; pnl DROP -86.06% near-zero; equity JUMP +1.66%; FTE JUMP 26.5",
        "absurdity_score": "7.3",
        "cost_score": "4.0",
        "difficulty": "3.5",
        "priority_index": "5.9",
        "cut_proposal": "FOI NBB PDF + AViQ/INAMI split + explain pnl DROP -86% near-zero at rising omzet; dual Entraide Fraternelle / La Charmille continuum",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2119; Medium CW; FOI gap_strebo_nbb_pdf_assets_debt_pnl_drop_near_zero_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT Entraide ASBL",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>StreboServices>NBB_PDF_assets_debt_pnl_drop_near_zero",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP near-zero path; AViQ/INAMI vs omzet split; 2 VE matrix (Le Rambour/Le Planty); dual Entraide Fraternelle ASBL / La Charmille ASBL / Groupe Jolimont",
        "why_it_matters": "Medium CW shows 2.41m omzet Jolimont Strebo MRS SRL (aanbestedende overheid) with pnl DROP -86% to near-zero despite omzet JUMP — care-margin transparency gap on AViQ-path Jolimont continuum sister to Entraide",
        "priority": "8",
        "recipient_body": "Strebo Services SRL / Groupe Jolimont",
        "recipient_email": "secretariat.general@jolimont.be",
        "recipient_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "draft_letter_path": "docs/doge/foi/drafts/gap_strebo_nbb_pdf_assets_debt_pnl_drop_near_zero_matrix_l5.md",
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
        "notes": "tick2119; human-send only; Medium CW; next every-10 2120",
    },
)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2119":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed: leftover dual Strebo Services after Entraide Jolimont; preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
            "live YE2025 Medium CW NL+EN+FR + Strong KBO 0899.812.184; omzet JUMP 2.41m pnl DROP 8892 near-zero equity JUMP 0.45m FTE 26.5; "
            "FOI ready NBB PDF assets/debt; DISTINCT Entraide/La Charmille"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2119 Strebo Services YE2025 Medium CW; FOI ready not sent; next rq_2120 every-10; next every-10 2120"
rows.append(
    {
        "task_id": "rq_2120",
        "title": "leftover dual hole-fill after Strebo + every-10 progress — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 2120 EVERY-10 after Strebo Services YE2025 Medium. Refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
            "Do NOT redo Strebo Services, Entraide Fraternelle Jolimont, La Charmille Pont-a-Celles, Residence Les Charmilles Sambreville, Les Sittelles Chastre, "
            "Les Buissons / Chateau Sous Bois Spa, Residence 3 / Saphir, Elisabeth Aan Zee Oostende, Maison de Repos du XXe Aout / PLIMCO, "
            "Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX*, INTRADEL, Korian Belgium, Comnexio, "
            "ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, "
            "Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, emeis."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick2119 Strebo; EVERY-10 tick; FARO/AIESH/REW still YE2024; next every-10 2130",
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
            "last_unit_id": "rq_2119",
            "ticks_completed": "2119",
            "paused": "no",
            "notes": (
                "tick2119 leftover Strebo Services 0899.812.184 Medium CW "
                "(omzet JUMP 2.41m bruto JUMP 2.25m pnl DROP 8892 near-zero equity JUMP 0.45m FTE 26.5; "
                "assets/debt Unknown; 2 VE NACE 87.101/87.301 Le Rambour/Le Planty Jolimont); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Entraide taken; next rq_2120 every-10; continuous hole_fill"
            ),
        }
    )

print("OK tick2119 writes")
