# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)
UTC = "2026-08-25T11:10:00Z"
ENTITY = "nv_home_sebrechts"
GAP = "gap_sebrechts_nbb_pdf_assets_debt_bruto_drop_fte_drop_matrix_l5"
COMM = "comm_sebrechts_jr2025_statutory_mrs"
LB = "lb_sebrechts_omzet_jump_34_82m_bruto_drop_fte_drop_jr2025"
SRC_EN = "src_sebrechts_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_sebrechts_jr2025_cw",
        "title": "Companyweb NL Home Sebrechts YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0442694142/home-sebrechts",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2123; YE2025 omzet JUMP 34823710 pnl JUMP 930462 equity JUMP 4005858 bruto DROP 27145085 FTE DROP 462.9; neerlegging 11.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2123/sebrechts_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Home Sebrechts YE2025 statutory",
        "url": "https://www.companyweb.be/en/0442694142/home-sebrechts",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2123; EN mirror YE2025 Medium; filed 11-07-2026; Last balance sheet year 2025; FTE 462.9; raw docs/doge/data/raw/tick2123/sebrechts_en.html",
    },
    {
        "source_id": "src_sebrechts_jr2025_cw_fr",
        "title": "Companyweb FR Home Sebrechts YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0442694142/home-sebrechts",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2123; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2123/sebrechts_fr.html",
    },
    {
        "source_id": "src_sebrechts_kbo_2123",
        "title": "KBO Home Sebrechts 0442.694.142 Actief Mechelen Armonea path",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0442694142",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2123; Actief NV/SA; Stationsstraat 102 2800 Mechelen; 6 VE; NACE 87.101/87.301/87.302; email info@armonea.be; web www.armonea.be; absorbed HOME CASTEL 0451.026.442 since 31.07.2014; kapitaal 2462000",
    },
    {
        "source_id": "src_sebrechts_armonea_2123",
        "title": "Armonea site / Home Sebrechts FOI contact info@armonea.be",
        "url": "https://www.armonea.be",
        "publisher": "Armonea / Colisee",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": "tick2123; multi-site MRS NV under Armonea brand; FOI info@armonea.be; DISTINCT Armonea holding not retaken",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Home Sebrechts (Mechelen / Armonea-path MRS)",
        "name_fr": "Home Sebrechts SA (Malines / MRS Armonea)",
        "name_en": "Home Sebrechts nursing-home NV (Mechelen; Armonea path)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.armonea.be",
        "foi_email": "info@armonea.be",
        "foi_postal": "Stationsstraat 102, 2800 Mechelen",
        "notes": "tick2123 YE2025 Medium CW NL+EN+FR + Strong KBO 0442.694.142 Actief NV/SA 6 VE NACE 87.101/87.301/87.302; omzet JUMP 34.82m (+7.13%) bruto DROP 27.15m (-6.45%) pnl JUMP 0.93m (+1.7%) equity JUMP 4.01m (+30.26%) FTE DROP 462.9 (vs 495.6); assets/debt Unknown; filed 11.07.2026; FOI gap_sebrechts_nbb_pdf_assets_debt_bruto_drop_fte_drop_matrix_l5; Armonea brand multi-site; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Armonea holding / Unité Jolimont / 't Buurthuis / Le Bosquet",
    },
)

for bid, amt, basis in [
    ("bud_sebrechts_omzet_jr2025_statutory", "34823710", "CW YE2025 omzet / Turnover (primary envelope multi-site MRS NV)"),
    ("bud_sebrechts_bruto_jr2025_statutory", "27145085", "CW YE2025 Brutomarge / Gross margin"),
    ("bud_sebrechts_pnl_jr2025_statutory", "930462", "CW YE2025 Profit/Loss"),
    ("bud_sebrechts_equity_jr2025_statutory", "4005858", "CW YE2025 Eigen vermogen / Equity"),
    ("bud_sebrechts_fte_jr2025_statutory", "462.9", "CW social-balance FTE / Employees"),
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
            "notes": "tick2123; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Home Sebrechts YE2025 leftover dual (omzet JUMP 34.82m / bruto DROP / FTE DROP)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Armonea multi-site (6 VE Mechelen+Brussels belt+Marche)",
        "legal_basis": "NV/SA maison de repos RVT/ROB/service flats (KBO 0442.694.142; NACE 87.101/87.301/87.302; 6 VE; Armonea path)",
        "decision_date": "2026-07-11",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "34823710",
        "cash_by_year": '{"2025_omzet":34823710,"2025_bruto":27145085,"2025_pnl":930462,"2025_equity":4005858,"2025_fte":462.9}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0442694142/home-sebrechts",
        "stated_goal": "Public-interest multi-site nursing-home care (Armonea/Colisee path; RIZIV/Zorgkas/Iriscare-adjacent)",
        "cut_option": "Publish NBB PDF assets/debt FOI; explain bruto DROP -6.45% + FTE DROP at omzet JUMP; thin equity 4.01m vs 34.8m; 6 VE + Armonea holding dual",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>HomeSebrechts>JR2025_statutory_L5",
        "notes": "tick2123; Medium CW; omzet primary envelope; assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Armonea holding",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "Home Sebrechts omzet JUMP 34.82m / bruto DROP / FTE DROP (YE2025)",
        "level": "L5",
        "type": "mrs_statutory_nv_armonea_path",
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>HomeSebrechts>JR2025",
        "annual_cost_eur": "34823710",
        "total_cost_eur": "34823710",
        "tco_notes": "CW YE2025 omzet 34823710 JUMP +7.13% (primary); bruto 27145085 DROP -6.45%; pnl 930462 JUMP +1.7%; equity 4005858 JUMP +30.26% thin vs omzet; FTE 462.9 DROP vs 495.6; assets/debt Unknown pending NBB PDF; 6 VE Armonea path",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Armonea multi-site (6 VE)",
        "stated_goal": "Public-interest nursing-home care (Armonea path)",
        "measured_outcome": "omzet JUMP +7.13%; bruto DROP -6.45%; pnl JUMP +1.7%; equity JUMP +30.26% thin; FTE DROP 462.9",
        "absurdity_score": "6.0",
        "cost_score": "5.5",
        "difficulty": "3.5",
        "priority_index": "5.9",
        "cut_proposal": "FOI NBB PDF + RIZIV/Zorgkas/Iriscare split + explain bruto DROP and FTE DROP at rising omzet; thin equity vs 34.8m; Armonea holding dual",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2123; Medium CW; FOI gap_sebrechts_nbb_pdf_assets_debt_bruto_drop_fte_drop_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT Armonea holding",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>HomeSebrechts>NBB_PDF_assets_debt_bruto_drop_fte_drop",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); bruto DROP vs omzet JUMP path; FTE DROP 495.6→462.9; thin equity vs 34.8m omzet; RIZIV/Zorgkas/Iriscare vs dagprijs split; 6 VE + Armonea holding dual",
        "why_it_matters": "Medium CW shows 34.82m omzet Armonea-path multi-site MRS NV with bruto DROP -6.45% and FTE DROP at rising omzet and thin equity 4.01m — care-margin / staffing transparency gap",
        "priority": "8",
        "recipient_body": "Home Sebrechts NV / Armonea",
        "recipient_email": "info@armonea.be",
        "recipient_postal": "Stationsstraat 102, 2800 Mechelen",
        "draft_letter_path": "docs/doge/foi/drafts/gap_sebrechts_nbb_pdf_assets_debt_bruto_drop_fte_drop_matrix_l5.md",
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
        "notes": "tick2123; human-send only; Medium CW; next every-10 2130",
    },
)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2123":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed: leftover dual Home Sebrechts after Unite Jolimont; preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
            "live YE2025 Medium CW NL+EN+FR + Strong KBO 0442.694.142; omzet JUMP 34.82m bruto DROP 27.15m pnl JUMP 0.93m equity JUMP 4.01m FTE DROP 462.9; "
            "FOI ready NBB PDF; DISTINCT Armonea holding / Unite/'t Buurthuis/Le Bosquet"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2123 Home Sebrechts YE2025 Medium CW; FOI ready not sent; next rq_2124; next every-10 2130"
rows.append(
    {
        "task_id": "rq_2124",
        "title": "leftover dual hole-fill after Home Sebrechts — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 2124 after Home Sebrechts YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. Do NOT redo Home Sebrechts, "
            "Unite Jolimont, 't Buurthuis, Le Bosquet, Strebo, Entraide Fraternelle Jolimont, La Charmille, Les Charmilles Sambreville, "
            "Les Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, "
            "Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, AIEG, RESA, Enodia, "
            "Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, emeis, RSW."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick2123 Home Sebrechts; FARO/AIESH/REW still YE2024; next every-10 2130",
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
            "last_unit_id": "rq_2123",
            "ticks_completed": "2123",
            "paused": "no",
            "notes": (
                "tick2123 leftover Home Sebrechts 0442.694.142 Medium CW "
                "(omzet JUMP 34.82m bruto DROP 27.15m pnl JUMP 0.93m equity JUMP 4.01m FTE DROP 462.9; "
                "assets/debt Unknown; 6 VE NACE 87.101/87.301/87.302 Armonea-path Mechelen); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Unite/'t Buurthuis taken; next rq_2124; next every-10 2130; continuous hole_fill"
            ),
        }
    )

print("OK tick2123 writes")
