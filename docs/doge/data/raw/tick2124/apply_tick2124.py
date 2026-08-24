# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)
UTC = "2026-08-25T11:25:00Z"
ENTITY = "nv_residence_le_castel"
GAP = "gap_le_castel_nbb_pdf_assets_debt_pnl_jump_equity_drop_matrix_l5"
COMM = "comm_le_castel_jr2025_statutory_mrs"
LB = "lb_le_castel_bruto_jump_3_76m_pnl_jump_equity_drop_jr2025"
SRC_EN = "src_le_castel_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_le_castel_jr2025_cw",
        "title": "Companyweb NL Residence Le Castel YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0462316153/residence-le-castel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2124; YE2025 omzet unpublished bruto JUMP 3764669 pnl JUMP 426911 equity DROP 1129091 FTE DROP 44.9; neerlegging 23.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2124/castel_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Residence Le Castel YE2025 statutory",
        "url": "https://www.companyweb.be/en/0462316153/residence-le-castel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2124; EN mirror YE2025 Medium; filed 23-06-2026; Last balance sheet year 2025; Turnover unpublished; Gross margin 3764669; FTE 44.9; raw docs/doge/data/raw/tick2124/castel_en.html",
    },
    {
        "source_id": "src_le_castel_jr2025_cw_fr",
        "title": "Companyweb FR Residence Le Castel YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0462316153/residence-le-castel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2124; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2124/castel_fr.html",
    },
    {
        "source_id": "src_le_castel_kbo_2124",
        "title": "KBO Residence Le Castel 0462.316.153 Actief Ham-sur-Heure",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0462316153",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2124; Actief NV/SA; Allee des Ecureuils(HSH) 60 6120 Ham-sur-Heure-Nalinnes; 1 VE; NACE 87.301; kapitaal 62000; bestuurders Beelen Stephanie + Vallery Benedicte sinds 28.03.2025; email/web empty in KBO",
    },
    {
        "source_id": "src_le_castel_contact_2124",
        "title": "Residence Le Castel FOI contact info@residencelecastel.be (Hainaut DI)",
        "url": "https://websoc.hainaut.be/DI00296.htm",
        "publisher": "Province de Hainaut / websoc",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2124; Tel 071/214394; Mail info@residencelecastel.be; siege Allee des Ecureuils 60 6120 Ham-sur-Heure",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Residence Le Castel (Ham-sur-Heure)",
        "name_fr": "Residence Le Castel SA (Ham-sur-Heure-Nalinnes)",
        "name_en": "Residence Le Castel nursing-home NV (Ham-sur-Heure)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "",
        "foi_email": "info@residencelecastel.be",
        "foi_postal": "Allee des Ecureuils(HSH) 60, 6120 Ham-sur-Heure-Nalinnes",
        "notes": "tick2124 YE2025 Medium CW NL+EN+FR + Strong KBO 0462.316.153 Actief NV/SA 1 VE NACE 87.301; omzet unpublished bruto JUMP 3.76m (+10.78%) pnl JUMP 0.43m (+78.73%) equity DROP 1.13m (-29.53%) FTE DROP 44.9 (vs 46.6); assets/debt Unknown; filed 23.06.2026; FOI gap_le_castel_nbb_pdf_assets_debt_pnl_jump_equity_drop_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Home Sebrechts/Armonea/Jolimont continuum",
    },
)

for bid, amt, basis in [
    ("bud_le_castel_bruto_jr2025_statutory", "3764669", "CW YE2025 Brutomarge / Gross margin (primary envelope; omzet unpublished)"),
    ("bud_le_castel_pnl_jr2025_statutory", "426911", "CW YE2025 Profit/Loss"),
    ("bud_le_castel_equity_jr2025_statutory", "1129091", "CW YE2025 Eigen vermogen / Equity"),
    ("bud_le_castel_fte_jr2025_statutory", "44.9", "CW social-balance FTE / Employees"),
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
            "notes": "tick2124; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Residence Le Castel YE2025 leftover dual (bruto JUMP 3.76m / pnl JUMP / equity DROP)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Ham-sur-Heure (1 VE)",
        "legal_basis": "NV/SA maison de repos ROB (KBO 0462.316.153; NACE 87.301; 1 VE; AViQ-path)",
        "decision_date": "2026-06-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3764669",
        "cash_by_year": '{"2025_bruto":3764669,"2025_omzet":"unpublished","2025_pnl":426911,"2025_equity":1129091,"2025_fte":44.9}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0462316153/residence-le-castel",
        "stated_goal": "Public-interest nursing-home care (AViQ-adjacent Wallonie)",
        "cut_option": "Publish NBB PDF assets/debt + omzet FOI; explain pnl JUMP +79% with equity DROP -30%; map AViQ/INAMI vs fees",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>HamSurHeure>ResidenceLeCastel>JR2025_statutory_L5",
        "notes": "tick2124; Medium CW; bruto primary envelope (omzet unpublished); assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Home Sebrechts",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "Residence Le Castel bruto JUMP 3.76m / pnl JUMP +79% / equity DROP -30% (YE2025)",
        "level": "L5",
        "type": "mrs_statutory_nv",
        "hierarchy_path": "Wallonie>Hainaut>HamSurHeure>ResidenceLeCastel>JR2025",
        "annual_cost_eur": "3764669",
        "total_cost_eur": "3764669",
        "tco_notes": "CW YE2025 omzet unpublished; bruto 3764669 JUMP +10.78% (primary); pnl 426911 JUMP +78.73%; equity 1129091 DROP -29.53%; FTE 44.9 DROP; assets/debt Unknown pending NBB PDF; 1 VE",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Ham-sur-Heure (1 VE)",
        "stated_goal": "Public-interest nursing-home care (AViQ-path)",
        "measured_outcome": "bruto JUMP +10.78%; pnl JUMP +78.73%; equity DROP -29.53%; FTE DROP 44.9; omzet unpublished",
        "absurdity_score": "7.2",
        "cost_score": "4.2",
        "difficulty": "3.5",
        "priority_index": "6.1",
        "cut_proposal": "FOI NBB PDF + omzet + explain pnl JUMP with equity DROP (dividends/impairment); AViQ/INAMI split",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2124; Medium CW; FOI gap_le_castel_nbb_pdf_assets_debt_pnl_jump_equity_drop_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT Home Sebrechts",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>HamSurHeure>ResidenceLeCastel>NBB_PDF_assets_debt_pnl_jump_equity_drop",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet unpublished; pnl JUMP +79% vs equity DROP -30% path; AViQ/INAMI vs fee split; official FOI email",
        "why_it_matters": "Medium CW shows Walloon MRS NV with bruto 3.76m JUMP and pnl JUMP +79% while equity DROP -30% and omzet unpublished — care-margin / extraction transparency gap",
        "priority": "8",
        "recipient_body": "Residence Le Castel SA",
        "recipient_email": "info@residencelecastel.be",
        "recipient_postal": "Allee des Ecureuils(HSH) 60, 6120 Ham-sur-Heure-Nalinnes",
        "draft_letter_path": "docs/doge/foi/drafts/gap_le_castel_nbb_pdf_assets_debt_pnl_jump_equity_drop_matrix_l5.md",
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
        "notes": "tick2124; human-send only; Medium CW; info@residencelecastel.be (Hainaut DI); next every-10 2130",
    },
)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2124":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed: leftover dual Residence Le Castel after Home Sebrechts; preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
            "live YE2025 Medium CW NL+EN+FR + Strong KBO 0462.316.153; bruto JUMP 3.76m pnl JUMP 0.43m equity DROP 1.13m omzet unpublished FTE DROP 44.9; "
            "FOI ready NBB PDF postal; DISTINCT Home Sebrechts/Armonea/Jolimont"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2124 Residence Le Castel YE2025 Medium CW; FOI ready not sent; next rq_2125; next every-10 2130"
rows.append(
    {
        "task_id": "rq_2125",
        "title": "leftover dual hole-fill after Residence Le Castel — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 2125 after Residence Le Castel YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. Do NOT redo Residence Le Castel, "
            "Home Sebrechts, Unite Jolimont, 't Buurthuis, Le Bosquet, Strebo, Entraide Fraternelle Jolimont, La Charmille, Les Charmilles Sambreville, "
            "Les Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, "
            "Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, AIEG, RESA, Enodia, "
            "Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, emeis, RSW."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick2124 Residence Le Castel; FARO/AIESH/REW still YE2024; next every-10 2130",
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
            "last_unit_id": "rq_2124",
            "ticks_completed": "2124",
            "paused": "no",
            "notes": (
                "tick2124 leftover Residence Le Castel 0462.316.153 Medium CW "
                "(bruto JUMP 3.76m pnl JUMP 0.43m equity DROP 1.13m omzet unpublished FTE DROP 44.9; "
                "assets/debt Unknown; 1 VE NACE 87.301 Ham-sur-Heure); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Home Sebrechts taken; next rq_2125; next every-10 2130; continuous hole_fill"
            ),
        }
    )

print("OK tick2124 writes")
