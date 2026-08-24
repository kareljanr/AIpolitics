# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T21:40:00Z"
TICK = 2155
RQ = "rq_2155"
NEXT_RQ = "rq_2156"
ENTITY = "vzw_wzc_eycken_brug_bierbeek"
GAP = "gap_eycken_brug_nbb_pdf_assets_debt_pnl_jump_643pct_fte_drop_matrix_l5"
COMM = "comm_eycken_brug_jr2025_statutory_wzc_pnl_jump_fte_drop"
LB = "lb_eycken_brug_omzet_5_90m_pnl_jump_643pct_fte_drop_jr2025"
SRC_EN = "src_eycken_brug_jr2025_cw_en"
KBO = "0861.157.387"
KBO_DIGITS = "0861157387"
OMZET = "5899139"
OMZET_PRIOR = "5791906"
OMZET_YOY = "+1.85%"
BRUTO = "5348995"
BRUTO_PRIOR = "5108481"
BRUTO_YOY = "+4.71%"
PNL = "653314"
PNL_PRIOR = "87906"
PNL_YOY = "+643.2%"
EQUITY = "3504322"
EQUITY_PRIOR = "3069774"
EQUITY_YOY = "+14.16%"
FTE = "63.2"
FTE_PRIOR = "69.3"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI_DIR = ROOT / "foi" / "drafts"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = (
                "leftover dual — WZC d'Eycken Brug Bierbeek YE2025 Medium "
                "(omzet JUMP 5.90m / pnl JUMP +643% / FTE DROP 63.2)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Eycken Brug Medium omzet JUMP 5.90m ({OMZET_YOY}) bruto JUMP 5.35m ({BRUTO_YOY}) "
                f"pnl JUMP 0.65m ({PNL_YOY}) equity JUMP 3.50m ({EQUITY_YOY}) FTE DROP {FTE} (vs {FTE_PRIOR}); "
                f"KBO Actief VZW 1 VE NACE 87.301 Bierbeek Solidum; FOI ready; "
                f"skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed leftover WZC d'Eycken Brug YE2025 Medium CW after Sint-Felix; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Eycken Brug — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after WZC d'Eycken Brug Bierbeek YE2025 Medium "
                    "(omzet JUMP 5.90m / pnl JUMP +643% / FTE DROP 63.2). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                    "(prefer sourced € over opaque ZS FTE-only; Hainaut-Est still FTE-only deferred). "
                    "Do NOT redo WZC d'Eycken Brug Bierbeek, WZC Sint-Felix Pajottegem/Herne, "
                    "Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, "
                    "Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, "
                    "Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, "
                    "Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, "
                    "Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, "
                    "Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, Cassiers, OLV Lourdes, "
                    "Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, Van Lierde, Sint-Augustinus Halle."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Eycken Brug; "
                    "FARO/AIESH/REW still YE2024; Hainaut-Est opaque deferred; next every-10 2160"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def update_loop_state():
    path = DATA / "loop_state.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    rows[0]["mode"] = "continuous"
    rows[0]["current_sprint"] = "hole_fill"
    rows[0]["last_tick_utc"] = UTC
    rows[0]["last_unit_id"] = RQ
    rows[0]["ticks_completed"] = str(TICK)
    rows[0]["paused"] = "no"
    rows[0]["notes"] = (
        f"tick{TICK} leftover WZC d'Eycken Brug Bierbeek {KBO} Medium "
        f"(omzet JUMP 5.90m pnl JUMP +643% equity JUMP +14% FTE DROP {FTE}; Actief VZW 1 VE Solidum); "
        "skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        f"next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
    )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_eycken_brug_jr2025_cw",
        "title": "Companyweb NL WZC d'Eycken Brug Bierbeek YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/woonzorgcentrum-deycken-brug",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY} vs YE2024 {PNL_PRIOR}) equity JUMP {EQUITY} ({EQUITY_YOY}) "
            f"FTE DROP {FTE} (vs {FTE_PRIOR}); neerlegging 02.07.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2155/eycken_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC d'Eycken Brug Bierbeek YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/woonzorgcentrum-deycken-brug",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; raw docs/doge/data/raw/tick2155/eycken_en.html"
        ),
    },
    {
        "source_id": "src_eycken_brug_jr2025_cw_fr",
        "title": "Companyweb FR WZC d'Eycken Brug Bierbeek YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/woonzorgcentrum-deycken-brug",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2155/eycken_fr.html",
    },
    {
        "source_id": f"src_eycken_brug_kbo_{TICK}",
        "title": f"KBO WZC d'Eycken Brug {KBO} Actief Bierbeek VZW 1 VE",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; VZW Woonzorgcentrum d'Eycken Brug; "
            "Bergenlaan 5 3360 Bierbeek sinds 01.09.2013; 1 VE; "
            "RSZ NACE 87.301 ROB; Solidum Groep + OCMW Bierbeek path; "
            "dagelijks bestuur Engelen/Ryngaert"
        ),
    },
    {
        "source_id": f"src_eycken_brug_site_{TICK}",
        "title": "WZC d'Eycken Brug site FOI algemeen@deyckenbrug.be",
        "url": "https://www.deyckenbrug.be/",
        "publisher": "WZC d'Eycken Brug VZW / Solidum Groep",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Bergenlaan 5 3360 Bierbeek; FOI algemeen@deyckenbrug.be; "
            "~87 beds + 3 kortverblijf + dagverzorging; Solidum Groep / OCMW Bierbeek PPS"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Woonzorgcentrum d'Eycken Brug (Bierbeek)",
        "name_fr": "Maison de repos et de soins d'Eycken Brug (Bierbeek)",
        "name_en": "WZC d'Eycken Brug nursing home (Bierbeek)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.deyckenbrug.be/",
        "foi_email": "algemeen@deyckenbrug.be",
        "foi_postal": "Bergenlaan 5, 3360 Bierbeek",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW; "
            f"omzet JUMP 5.90m ({OMZET_YOY}) bruto JUMP 5.35m ({BRUTO_YOY}) pnl JUMP 0.65m ({PNL_YOY}) "
            f"equity JUMP 3.50m ({EQUITY_YOY}) FTE DROP {FTE} (vs {FTE_PRIOR}); "
            f"assets/debt Unknown; filed 02.07.2026; 1 VE NACE 87.301; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
            "Solidum Groep + OCMW Bierbeek; DISTINCT Sint-Felix / Sint-Augustinus Halle / Vander Stokken / "
            "Hof ter Waarbeek / Sint-Carolus Ternat / Van Lierde / OLV Lourdes"
        ),
    },
)

for bid, amt, basis in [
    ("bud_eycken_brug_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover JUMP +1.85%"),
    ("bud_eycken_brug_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin JUMP +4.71%"),
    ("bud_eycken_brug_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss JUMP +643.2%"),
    ("bud_eycken_brug_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity JUMP +14.16%"),
    ("bud_eycken_brug_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees DROP 63.2"),
]:
    append_csv(
        DATA / "budgets.csv",
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
            "notes": "tick2155; Medium CW; assets/debt Unknown pending NBB PDF; VZW ROB/WZC Solidum Bierbeek",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "WZC d'Eycken Brug Bierbeek YE2025 leftover dual "
            "(omzet JUMP 5.90m / pnl JUMP +643% / FTE DROP)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "WZC/ROB residents d'Eycken Brug Bierbeek (~87 beds + kortverblijf/dagverzorging)",
        "legal_basis": f"VZW ROB/WZC (KBO {KBO}; Actief; 1 VE; NACE 87.301; Solidum Groep + OCMW Bierbeek)",
        "decision_date": "2026-07-02",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/woonzorgcentrum-deycken-brug",
        "stated_goal": "Residential elderly care Bierbeek (Solidum Groep / OCMW Bierbeek PPS)",
        "cut_option": (
            "Publish NBB PDF assets/debt + public Zorgkas/RIZIV/Vlaamse middelen vs dagprijs FOI; "
            "explain pnl JUMP +643% with FTE DROP 69.3→63.2 vs modest omzet +1.85%"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Bierbeek>WZC_Eycken_Brug>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; not TE-additive of 348bn"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "WZC d'Eycken Brug Bierbeek omzet JUMP 5.90m / pnl JUMP +643% / "
            "FTE DROP 63.2 (YE2025)"
        ),
        "level": "L5",
        "type": "wzc_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Bierbeek>WZC_Eycken_Brug>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; "
            "pnl surge +643% with FTE DROP vs modest turnover growth"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC/ROB clients Bierbeek (~87 beds; Solidum Groep)",
        "stated_goal": "Residential elderly care Bierbeek (Solidum / OCMW PPS)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE DROP {FTE} (vs {FTE_PRIOR})"
        ),
        "absurdity_score": "6.2",
        "cost_score": "4.4",
        "difficulty": "4.0",
        "priority_index": "6.2",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; map IFIC/Zorgkas vs dagprijs; "
            "explain pnl JUMP 88k→653k (+643%) with FTE DROP 69.3→63.2 "
            "and only +1.85% omzet"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est; Solidum Groep VZW Bierbeek; DISTINCT Sint-Felix"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>Vlaams-Brabant>Bierbeek>WZC_Eycken_Brug>"
            "NBB_PDF_assets_debt_pnl_jump_fte_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/omzet detail); "
            "public subsidy vs dagprijs split; explanation of pnl JUMP EUR87906→EUR653314 "
            f"(+643.2%) with FTE DROP {FTE_PRIOR}→{FTE} and only modest omzet JUMP +1.85%"
        ),
        "why_it_matters": (
            "Medium CW shows 5.90m omzet VZW ROB/WZC (~87 beds Solidum+OCMW) with extreme pnl surge "
            "and staffing drop without balanstotaal/assets/debt; material L5 residual for FOI"
        ),
        "priority": "8",
        "recipient_body": "Woonzorgcentrum d'Eycken Brug VZW / Solidum Groep / OCMW Bierbeek",
        "recipient_email": "algemeen@deyckenbrug.be",
        "recipient_postal": "Bergenlaan 5, 3360 Bierbeek",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
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
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; "
            "preferred stall FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est"
        ),
    },
)

update_rq()
update_loop_state()
print("OK tick2155 Eycken Brug")
