# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T21:20:00Z"
TICK = 2154
RQ = "rq_2154"
NEXT_RQ = "rq_2155"
ENTITY = "vzw_wzc_sint_felix_pajottegem"
GAP = "gap_sint_felix_nbb_pdf_assets_debt_pnl_equity_jump_matrix_l5"
COMM = "comm_sint_felix_jr2025_statutory_wzc_pnl_equity_jump"
LB = "lb_sint_felix_omzet_4_94m_pnl_jump_131pct_equity_jump_81pct_jr2025"
SRC_EN = "src_sint_felix_jr2025_cw_en"
KBO = "0409.583.092"
KBO_DIGITS = "0409583092"
OMZET = "4943135"
OMZET_PRIOR = "4889080"
OMZET_YOY = "+1.11%"
BRUTO = "4529268"
BRUTO_PRIOR = "4380496"
BRUTO_YOY = "+3.40%"
PNL = "370966"
PNL_PRIOR = "160421"
PNL_YOY = "+131.25%"
EQUITY = "1894755"
EQUITY_PRIOR = "1047908"
EQUITY_YOY = "+80.81%"
FTE = "48.5"
FTE_PRIOR = "48.1"
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
                "leftover dual — WZC Sint-Felix Pajottegem YE2025 Medium "
                "(omzet JUMP 4.94m / pnl JUMP +131% / equity JUMP +81%)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Sint-Felix Medium omzet JUMP 4.94m ({OMZET_YOY}) bruto JUMP 4.53m ({BRUTO_YOY}) "
                f"pnl JUMP 0.37m ({PNL_YOY}) equity JUMP 1.89m ({EQUITY_YOY}) FTE JUMP {FTE}; "
                f"KBO Actief VZW 1 VE NACE 87.101 Pajottegem/Herne; FOI ready; "
                f"skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed leftover WZC Sint-Felix YE2025 Medium CW after Brabant wallon; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Sint-Felix — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after WZC Sint-Felix Pajottegem YE2025 Medium "
                    "(omzet JUMP 4.94m / pnl JUMP +131% / equity JUMP +81%). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                    "(prefer sourced € over opaque ZS FTE-only; Hainaut-Est still FTE-only deferred). "
                    "Do NOT redo WZC Sint-Felix Pajottegem/Herne, Zone de secours Brabant wallon, "
                    "Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, "
                    "Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, "
                    "Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, "
                    "Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, Brandweerzone Antwerpen, "
                    "Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, "
                    "Heilig Hart Grimbergen, Maria's Rustoord, Cassiers, OLV Lourdes, Vander Stokken, "
                    "Hof ter Waarbeek, Sint-Carolus Ternat, Van Lierde, Sint-Augustinus Halle."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Sint-Felix; "
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
        f"tick{TICK} leftover WZC Sint-Felix Pajottegem {KBO} Medium "
        f"(omzet JUMP 4.94m pnl JUMP +131% equity JUMP +81% FTE {FTE}; Actief VZW 1 VE); "
        "skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        f"next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
    )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_sint_felix_jr2025_cw",
        "title": "Companyweb NL WZC Sint-Felix Pajottegem YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/woonzorgcentrum-sint-felix",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY} vs YE2024 {PNL_PRIOR}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2154/sint_felix_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Felix Pajottegem YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/woonzorgcentrum-sint-felix",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; raw docs/doge/data/raw/tick2154/sint_felix_en.html"
        ),
    },
    {
        "source_id": "src_sint_felix_jr2025_cw_fr",
        "title": "Companyweb FR WZC Sint-Felix Pajottegem YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/woonzorgcentrum-sint-felix",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2154/sint_felix_fr.html",
    },
    {
        "source_id": f"src_sint_felix_kbo_{TICK}",
        "title": f"KBO WZC Sint-Felix {KBO} Actief Pajottegem VZW 1 VE",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; VZW WoonZorgcentrum Sint-Felix; "
            "Lindestraat(HN) 3 1540 Pajottegem sinds 01.01.2025; 1 VE; "
            "RSZ NACE 87.101 RVT; sinds 27.07.1922; Solidum Groep path"
        ),
    },
    {
        "source_id": f"src_sint_felix_site_{TICK}",
        "title": "WZC Sint-Felix site FOI wzc@sintfelix.be",
        "url": "https://www.sintfelix.be/",
        "publisher": "WZC Sint-Felix VZW / Solidum Groep",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Lindestraat 3 1540 Pajottegem (ex Herne); FOI wzc@sintfelix.be; "
            "~60 beds + assistentiewoningen; Solidum Groep WZC cluster"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "WoonZorgcentrum Sint-Felix (Pajottegem / Herne)",
        "name_fr": "Maison de repos et de soins Sint-Felix (Pajottegem / Herne)",
        "name_en": "WZC Sint-Felix nursing home (Pajottegem / Herne)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.sintfelix.be/",
        "foi_email": "wzc@sintfelix.be",
        "foi_postal": "Lindestraat 3, 1540 Pajottegem",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW; "
            f"omzet JUMP 4.94m ({OMZET_YOY}) bruto JUMP 4.53m ({BRUTO_YOY}) pnl JUMP 0.37m ({PNL_YOY}) "
            f"equity JUMP 1.89m ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
            f"assets/debt Unknown; filed 02.07.2026; 1 VE NACE 87.101; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
            "Solidum Groep; DISTINCT Sint-Augustinus Halle / Vander Stokken / Hof ter Waarbeek / "
            "Sint-Carolus Ternat / Van Lierde / OLV Lourdes"
        ),
    },
)

for bid, amt, basis in [
    ("bud_sint_felix_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover JUMP +1.11%"),
    ("bud_sint_felix_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin JUMP +3.40%"),
    ("bud_sint_felix_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss JUMP +131.25%"),
    ("bud_sint_felix_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity JUMP +80.81%"),
    ("bud_sint_felix_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees JUMP 48.5"),
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
            "notes": "tick2154; Medium CW; assets/debt Unknown pending NBB PDF; VZW RVT/WZC Solidum",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "WZC Sint-Felix Pajottegem YE2025 leftover dual "
            "(omzet JUMP 4.94m / pnl JUMP +131% / equity JUMP +81%)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "WZC/RVT residents Sint-Felix Pajottegem (~60 beds + assistentiewoningen)",
        "legal_basis": f"VZW RVT/WZC (KBO {KBO}; Actief; 1 VE; NACE 87.101; Solidum Groep)",
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
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/woonzorgcentrum-sint-felix",
        "stated_goal": "Residential elderly care Pajottegem/Herne (Solidum Groep)",
        "cut_option": (
            "Publish NBB PDF assets/debt + public Zorgkas/RIZIV/Vlaamse middelen vs dagprijs FOI; "
            "explain pnl JUMP +131% and equity JUMP +81% vs modest omzet +1.11%"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pajottegem>WZC_Sint_Felix>JR2025_statutory_L5",
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
            "WZC Sint-Felix Pajottegem omzet JUMP 4.94m / pnl JUMP +131% / "
            "equity JUMP +81% (YE2025)"
        ),
        "level": "L5",
        "type": "wzc_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pajottegem>WZC_Sint_Felix>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; "
            "pnl/equity surge vs modest turnover growth"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC/RVT clients Pajottegem (~60 beds; Solidum Groep)",
        "stated_goal": "Residential elderly care Pajottegem/Herne",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE}"
        ),
        "absurdity_score": "5.0",
        "cost_score": "4.2",
        "difficulty": "4.0",
        "priority_index": "5.8",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; map IFIC/Zorgkas vs dagprijs; "
            "explain pnl JUMP 160k→371k (+131%) and equity JUMP 1.05m→1.89m (+81%) "
            "with only +1.11% omzet"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est; Solidum Groep VZW; DISTINCT Sint-Augustinus Halle"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>Vlaams-Brabant>Pajottegem>WZC_Sint_Felix>"
            "NBB_PDF_assets_debt_pnl_equity_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/omzet detail); "
            "public subsidy vs dagprijs split; explanation of pnl JUMP EUR160421→EUR370966 "
            f"(+131.25%) and equity JUMP EUR1047908→EUR1894755 (+80.81%) "
            "with only modest omzet JUMP +1.11%"
        ),
        "why_it_matters": (
            "Medium CW shows 4.94m omzet VZW RVT/WZC (~60 beds) with large pnl/equity surge "
            "without balanstotaal/assets/debt; material L5 residual for FOI"
        ),
        "priority": "8",
        "recipient_body": "WoonZorgcentrum Sint-Felix VZW / Solidum Groep",
        "recipient_email": "wzc@sintfelix.be",
        "recipient_postal": "Lindestraat 3, 1540 Pajottegem",
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
print("OK tick2154 Sint-Felix")
