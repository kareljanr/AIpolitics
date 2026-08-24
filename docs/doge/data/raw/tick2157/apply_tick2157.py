# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T22:20:00Z"
TICK = 2157
RQ = "rq_2157"
NEXT_RQ = "rq_2158"
ENTITY = "bv_mrs_parc_de_forest_ixelles"
GAP = "gap_parc_de_forest_nbb_pdf_assets_debt_negative_equity_omzet_drop_matrix_l5"
COMM = "comm_parc_de_forest_jr2026_statutory_mrs_omzet_drop_neg_equity"
LB = "lb_parc_de_forest_omzet_drop_880k_pnl_jump_neg_equity_jr2026"
SRC_EN = "src_parc_de_forest_jr2026_cw_en"
KBO = "0452.587.548"
KBO_DIGITS = "0452587548"
OMZET = "880253"
OMZET_PRIOR = "972603"
OMZET_YOY = "-9.5%"
BRUTO = "488720"
BRUTO_PRIOR = "510110"
BRUTO_YOY = "-4.19%"
PNL = "61950"
PNL_PRIOR = "14378"
PNL_YOY = "+330.86%"
EQUITY = "-385222"
EQUITY_PRIOR = "-447172"
EQUITY_YOY = "+13.85%"
FTE = "12"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"


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
                "leftover dual — MRS Parc de Forest Ixelles YE2026 Medium "
                "(omzet DROP 880k / pnl JUMP +331% / equity NEG -385k)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Parc de Forest Medium omzet DROP 880k ({OMZET_YOY}) "
                f"bruto DROP 489k ({BRUTO_YOY}) pnl JUMP 62.0k ({PNL_YOY}) "
                f"equity NEG -385k improved ({EQUITY_YOY}) FTE {FTE}; "
                f"fiscal YE ends 30.04; filed 20.07.2026; KBO Actief BV 1 VE NACE 87.301; "
                f"FOI ready; skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed leftover MRS Parc de Forest YE2026 Medium CW after Le Hanois; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"skipped opaque ZS Hainaut-Est; took deferred Parc de Forest 0452.587.548 "
                f"now live YE2026; Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet DROP {OMZET} pnl JUMP {PNL} equity NEG {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Parc de Forest — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after MRS Parc de Forest Ixelles YE2026 Medium "
                    "(omzet DROP 880k / pnl JUMP +331% / equity NEG -385k; fiscal YE ends 30.04). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                    "(prefer sourced € over opaque ZS FTE-only; Hainaut-Est still FTE-only deferred). "
                    "Do NOT redo MRS Parc de Forest Ixelles/Saint-Gilles, MRS Le Hanois Fontaine-l'Évêque, "
                    "WZC d'Eycken Brug Bierbeek, WZC Sint-Felix Pajottegem/Herne, "
                    "Zone de secours Brabant wallon, Zone de secours Vesdre, "
                    "WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, "
                    "Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, "
                    "Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, "
                    "Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, "
                    "Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, "
                    "Cassiers, OLV Lourdes, Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, "
                    "Van Lierde, Sint-Augustinus Halle, WZC De Verlosser Dilbeek, WZC Sint-Jozef Rumst."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Parc de Forest; "
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
        f"tick{TICK} leftover MRS Parc de Forest Ixelles {KBO} Medium "
        f"(omzet DROP 880k pnl JUMP +331% equity NEG -385k improved FTE {FTE}; "
        "Actief BV 1 VE; fiscal YE ends 30.04; filed 20.07.2026); "
        "skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        f"next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
    )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_parc_de_forest_jr2026_cw",
        "title": "Companyweb NL MRS Parc de Forest Ixelles YE2026 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/maison-de-repos-du-parc-de-forest",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2026 (fiscal end 30.04) omzet DROP {OMZET} ({OMZET_YOY}) "
            f"bruto DROP {BRUTO} ({BRUTO_YOY}) pnl JUMP {PNL} ({PNL_YOY} vs YE2025 {PNL_PRIOR}) "
            f"equity NEG {EQUITY} ({EQUITY_YOY} vs {EQUITY_PRIOR}) FTE {FTE}; "
            "neerlegging 20.07.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2157/parc_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN MRS Parc de Forest Ixelles YE2026 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-du-parc-de-forest",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2026 Medium; filed 20-07-2026; Last balance sheet year 2026; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; commercial name RESIDENCE DU PARC; Small 12 FTE; "
            "raw docs/doge/data/raw/tick2157/parc_en.html"
        ),
    },
    {
        "source_id": "src_parc_de_forest_jr2026_cw_fr",
        "title": "Companyweb FR MRS Parc de Forest Ixelles YE2026 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/maison-de-repos-du-parc-de-forest",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2026 Medium; raw docs/doge/data/raw/tick2157/parc_fr.html",
    },
    {
        "source_id": f"src_parc_de_forest_kbo_{TICK}",
        "title": f"KBO MRS Parc de Forest {KBO} Actief Ixelles BV 1 VE",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; BV/SRL sinds 05.04.2023; "
            "Generaal Jacqueslaan 100 1050 Elsene sinds 01.03.2012; 1 VE; "
            "RSZ NACE 87.301 ROB; bestuurder Barhdadi Kamil; "
            "boekjaar eindigt 30 april; JV september; KBO email empty"
        ),
    },
    {
        "source_id": f"src_parc_de_forest_guidesocial_{TICK}",
        "title": "Guide Social — Résidence du Parc de Forest FOI contact",
        "url": "https://annuaire.guidesocial.be/fr-BE/organismes/residence-du-parc-de-forest__126066",
        "publisher": "Annuaire Guide Social",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_directory",
        "notes": (
            f"tick{TICK}; site Rue Antoine Bréart 131 1060 Saint-Gilles; "
            "FOI resduparc@hotmail.fr; tel 02 538 38 45; privé SRL; 10+ ETP class"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Maison de Repos du Parc de Forest (Elsene / Sint-Gillis)",
        "name_fr": "Maison de Repos du Parc de Forest (Ixelles / Saint-Gilles)",
        "name_en": "Parc de Forest nursing home (Ixelles / Saint-Gilles)",
        "level": "other",
        "parent_id": "brussels_gov",
        "community_language": "fr",
        "website": "https://annuaire.guidesocial.be/fr-BE/organismes/residence-du-parc-de-forest__126066",
        "foi_email": "resduparc@hotmail.fr",
        "foi_postal": "Generaal Jacqueslaan 100, 1050 Elsene (site: Rue Antoine Bréart 131, 1060 Saint-Gilles)",
        "notes": (
            f"tick{TICK} YE2026 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV; "
            f"omzet DROP 880k ({OMZET_YOY}) bruto DROP 489k ({BRUTO_YOY}) "
            f"pnl JUMP 62.0k ({PNL_YOY}) equity NEG -385k ({EQUITY_YOY}) FTE {FTE}; "
            f"assets/debt Unknown; filed 20.07.2026; fiscal YE ends 30.04; 1 VE NACE 87.301; "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est; commercial name RESIDENCE DU PARC; "
            "DISTINCT Care-Ion / En Famille / Prestige / Corolles / Peupliers / Le Hanois"
        ),
    },
)

for bid, amt, basis in [
    ("bud_parc_de_forest_omzet_jr2026_statutory", OMZET, "CW YE2026 Omzet / Turnover DROP -9.5%"),
    ("bud_parc_de_forest_bruto_jr2026_statutory", BRUTO, "CW YE2026 Brutomarge / Gross margin DROP -4.19%"),
    ("bud_parc_de_forest_pnl_jr2026_statutory", PNL, "CW YE2026 Profit/Loss JUMP +330.86%"),
    ("bud_parc_de_forest_equity_jr2026_statutory", EQUITY, "CW YE2026 Eigen vermogen / Equity NEG improved +13.85%"),
    ("bud_parc_de_forest_fte_jr2026_statutory", FTE, "CW social-balance FTE / Employees 12"),
]:
    append_csv(
        DATA / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2026",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": (
                "tick2157; Medium CW; fiscal YE ends 30.04.2026; assets/debt Unknown pending NBB PDF; "
                "BV ROB/MRS Ixelles seat / Saint-Gilles site; NEG equity residual"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "MRS Parc de Forest Ixelles YE2026 leftover dual "
            "(omzet DROP 880k / pnl JUMP +331% / equity NEG -385k)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "MRS/ROB residents Résidence du Parc (Saint-Gilles site; Ixelles seat)",
        "legal_basis": f"BV/SRL ROB/MRS (KBO {KBO}; Actief; 1 VE; NACE 87.301; fiscal YE ends 30.04)",
        "decision_date": "2026-07-20",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2026_omzet":{OMZET},"2026_bruto":{BRUTO},"2026_pnl":{PNL},'
            f'"2026_equity":{EQUITY},"2026_fte":{FTE},"2025_omzet":{OMZET_PRIOR},'
            f'"2025_pnl":{PNL_PRIOR},"2025_equity":{EQUITY_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-du-parc-de-forest"
        ),
        "stated_goal": "Residential elderly care Ixelles/Saint-Gilles (Résidence du Parc)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; map INAMI/Iriscare vs dagprijs; "
            "explain sustained NEG equity path despite pnl JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "BHG>Ixelles>MRS_Parc_de_Forest>JR2026_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; NEG equity; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
            "not TE-additive of 348bn"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "MRS Parc de Forest omzet DROP 880k / pnl JUMP +331% / "
            "equity NEG -385k (YE2026 fiscal)"
        ),
        "level": "L5",
        "type": "mrs_bv_statutory",
        "hierarchy_path": "BHG>Ixelles>MRS_Parc_de_Forest>JR2026",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            "CW omzet envelope; assets/debt Unknown pending NBB PDF FOI; "
            "sustained NEG equity (-385k) despite pnl JUMP — solvency opacity"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS/ROB clients Résidence du Parc (Saint-Gilles site)",
        "stated_goal": "Residential elderly care Ixelles/Saint-Gilles",
        "measured_outcome": (
            f"omzet DROP {OMZET_YOY}; bruto DROP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity NEG improved {EQUITY_YOY}; FTE {FTE}"
        ),
        "absurdity_score": "5.8",
        "cost_score": "3.2",
        "difficulty": "4.0",
        "priority_index": "5.6",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; map INAMI/Iriscare vs dagprijs; "
            "disclose NEG equity remediation plan after multi-year deficit path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est; BV MRS BHG; DISTINCT Care-Ion/Le Hanois"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "BHG>Ixelles>MRS_Parc_de_Forest>"
            "NBB_PDF_assets_debt_negative_equity_omzet_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening fiscal YE2026 (ends 30.04.2026) full "
            "(assets/debt LT-ST/cash/balanstotaal); INAMI/Iriscare vs dagprijs split; "
            "NEG equity remediation / AV notulen; 1 VE euro matrix; prior FTE series"
        ),
        "why_it_matters": (
            "Medium CW shows 880k omzet BV ROB/MRS with sustained NEG equity (-385k) "
            "and pnl JUMP +331% after multi-year losses — no balanstotaal/assets/debt "
            "published; material L5 residual for FOI"
        ),
        "priority": "8",
        "recipient_body": "Maison de Repos du Parc de Forest BV / Résidence du Parc",
        "recipient_email": "resduparc@hotmail.fr",
        "recipient_postal": (
            "Generaal Jacqueslaan 100, 1050 Elsene "
            "(site: Rue Antoine Bréart 131, 1060 Saint-Gilles)"
        ),
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
print("OK tick2157 Parc de Forest")
