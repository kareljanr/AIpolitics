# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T22:00:00Z"
TICK = 2156
RQ = "rq_2156"
NEXT_RQ = "rq_2157"
ENTITY = "bv_mrs_le_hanois_fontaine_leveque"
GAP = "gap_le_hanois_nbb_pdf_assets_debt_omzet_empty_bellechasse_absorption_matrix_l5"
COMM = "comm_le_hanois_jr2025_statutory_mrs_bruto_bellechasse_absorption"
LB = "lb_le_hanois_bruto_2_47m_pnl_flat_bellechasse_absorption_jr2025"
SRC_EN = "src_le_hanois_jr2025_cw_en"
KBO = "0421.479.153"
KBO_DIGITS = "0421479153"
OMZET = ""  # unpublished
BRUTO = "2472077"
BRUTO_PRIOR = "2335656"
BRUTO_YOY = "+5.84%"
PNL = "53631"
PNL_PRIOR = "52977"
PNL_YOY = "+1.23%"
EQUITY = "3383175"
EQUITY_PRIOR = "3329543"
EQUITY_YOY = "+1.61%"
FTE = "39"
FTE_PRIOR = "37"
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
                "leftover dual — MRS Le Hanois Fontaine-l'Évêque YE2025 Medium "
                "(bruto JUMP 2.47m / omzet empty / Belle Chasse absorbed)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Le Hanois Medium bruto JUMP 2.47m ({BRUTO_YOY}) pnl JUMP 53.6k ({PNL_YOY}) "
                f"equity JUMP 3.38m ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); omzet unpublished; "
                f"KBO Actief BV 2 VE NACE 87.301; absorbed Château Belle Chasse 0454.971.669 since 28.01.2026; "
                f"FOI ready; skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed leftover MRS Le Hanois YE2025 Medium CW after Eycken Brug; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; omzet empty; FOI {GAP}"
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
                    "leftover dual hole-fill after Le Hanois — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after MRS Le Hanois Fontaine-l'Évêque YE2025 Medium "
                    "(bruto JUMP 2.47m / omzet empty / Belle Chasse absorbed 28.01.2026). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                    "(prefer sourced € over opaque ZS FTE-only; Hainaut-Est still FTE-only deferred; "
                    "Parc de Forest Ixelles 0452.587.548 YE2026 live deferred). "
                    "Do NOT redo MRS Le Hanois Fontaine-l'Évêque, WZC d'Eycken Brug Bierbeek, "
                    "WZC Sint-Felix Pajottegem/Herne, Zone de secours Brabant wallon, Zone de secours Vesdre, "
                    "WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, "
                    "Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, "
                    "Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, "
                    "Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, "
                    "Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, "
                    "Cassiers, OLV Lourdes, Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, "
                    "Van Lierde, Sint-Augustinus Halle."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Le Hanois; "
                    "FARO/AIESH/REW still YE2024; Hainaut-Est opaque deferred; "
                    "Parc de Forest deferred; next every-10 2160"
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
        f"tick{TICK} leftover MRS Le Hanois Fontaine-l'Évêque {KBO} Medium "
        f"(bruto JUMP 2.47m pnl JUMP +1.23% equity JUMP +1.61% FTE JUMP {FTE}; omzet empty; "
        "Actief BV 2 VE; absorbed Belle Chasse 28.01.2026); "
        "skipped opaque ZS Hainaut-Est; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        f"next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
    )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_le_hanois_jr2025_cw",
        "title": "Companyweb NL MRS Le Hanois Fontaine-l'Évêque YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/maison-de-repos-et-de-soins-le-hanois",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet unpublished; bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY} vs YE2024 {PNL_PRIOR}) equity JUMP {EQUITY} ({EQUITY_YOY}) "
            f"FTE JUMP {FTE} (vs {FTE_PRIOR}); neerlegging 28.07.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2156/hanois_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN MRS Le Hanois Fontaine-l'Évêque YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-et-de-soins-le-hanois",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 28-07-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; raw docs/doge/data/raw/tick2156/hanois_en.html"
        ),
    },
    {
        "source_id": "src_le_hanois_jr2025_cw_fr",
        "title": "Companyweb FR MRS Le Hanois Fontaine-l'Évêque YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/maison-de-repos-et-de-soins-le-hanois",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2156/hanois_fr.html",
    },
    {
        "source_id": f"src_le_hanois_kbo_{TICK}",
        "title": f"KBO MRS Le Hanois {KBO} Actief Fontaine-l'Évêque BV 2 VE",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; BV/SRL sinds 22.09.2023; "
            "Rue du Hanois(F-E) 1 6140 Fontaine-l'Évêque sinds 01.02.1981; 2 VE; "
            "RSZ NACE 87.301 ROB; dagelijks bestuur Pachioli Patrizia; "
            "absorbed Château Belle Chasse 0454.971.669 since 28.01.2026; "
            "also absorbed SOCIETE CORBISIER 0450.052.779 since 21.12.2011; "
            "KBO email empty"
        ),
    },
    {
        "source_id": f"src_le_hanois_site_{TICK}",
        "title": "Maisons de repos Fontaine — Le Hanois / Belle Chasse FOI",
        "url": "https://www.maisonsdereposfontaine.be/",
        "publisher": "Château Belle Chasse – Résidence Le Hanois",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Rue du Hanois 1 Fontaine-l'Évêque; shared site after Belle Chasse absorption; "
            "FOI direction@lehanois.be (AViQ path) + info@bellechasse.be (site); "
            "~84 places class; raw docs/doge/data/raw/tick2156/hanois_site.html"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Maison de Repos et de Soins Le Hanois (Fontaine-l'Évêque)",
        "name_fr": "Maison de Repos et de Soins Le Hanois (Fontaine-l'Évêque)",
        "name_en": "Le Hanois nursing home (Fontaine-l'Évêque)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.maisonsdereposfontaine.be/",
        "foi_email": "direction@lehanois.be",
        "foi_postal": "Rue du Hanois 1, 6140 Fontaine-l'Évêque",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV; "
            f"omzet unpublished; bruto JUMP 2.47m ({BRUTO_YOY}) pnl JUMP 53.6k ({PNL_YOY}) "
            f"equity JUMP 3.38m ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
            f"assets/debt Unknown; filed 28.07.2026; 2 VE NACE 87.301; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS Hainaut-Est; "
            "absorbed Château Belle Chasse 0454.971.669 since 28.01.2026; "
            "DISTINCT En Famille Vaux / Prestige Chaudfontaine / Corolles / Peupliers / Comte d'Egmont"
        ),
    },
)

for bid, amt, basis in [
    ("bud_le_hanois_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin JUMP +5.84%"),
    ("bud_le_hanois_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss JUMP +1.23%"),
    ("bud_le_hanois_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity JUMP +1.61%"),
    ("bud_le_hanois_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees JUMP 39"),
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
            "notes": (
                "tick2156; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF; "
                "BV ROB/MRS Fontaine; Belle Chasse absorbed 28.01.2026"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "MRS Le Hanois Fontaine-l'Évêque YE2025 leftover dual "
            "(bruto JUMP 2.47m / omzet empty / Belle Chasse absorbed)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "MRS/ROB residents Le Hanois Fontaine-l'Évêque (~84 places; + Belle Chasse path)",
        "legal_basis": f"BV/SRL ROB/MRS (KBO {KBO}; Actief; 2 VE; NACE 87.301; absorbed Belle Chasse 0454.971.669)",
        "decision_date": "2026-07-28",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-et-de-soins-le-hanois"
        ),
        "stated_goal": "Residential elderly care Fontaine-l'Évêque (post Belle Chasse absorption)",
        "cut_option": (
            "Publish NBB PDF assets/debt + omzet code70 FOI; map INAMI/AViQ vs dagprijs; "
            "publish Belle Chasse absorption matrix (activa/schulden/places/FTE)"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Fontaine-lEveque>MRS_Le_Hanois>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet empty so bruto primary envelope; assets/debt Unknown; "
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
            "MRS Le Hanois Fontaine bruto JUMP 2.47m / omzet empty / "
            "Belle Chasse absorbed (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_bv_statutory",
        "hierarchy_path": "Wallonie>Hainaut>Fontaine-lEveque>MRS_Le_Hanois>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            "CW bruto proxy (omzet unpublished); assets/debt Unknown pending NBB PDF FOI; "
            "Belle Chasse 0454.971.669 absorbed 28.01.2026 — dual-site opacity"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS/ROB clients Fontaine-l'Évêque (~84 places; Belle Chasse path)",
        "stated_goal": "Residential elderly care Fontaine-l'Évêque",
        "measured_outcome": (
            f"omzet unpublished; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE} (vs {FTE_PRIOR}); Belle Chasse absorbed"
        ),
        "absurdity_score": "5.4",
        "cost_score": "3.8",
        "difficulty": "4.0",
        "priority_index": "5.4",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash/omzet FOI; map INAMI/AViQ vs dagprijs; "
            "disclose Belle Chasse absorption euros + VE matrix after 28.01.2026"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est; BV MRS Fontaine; DISTINCT En Famille/Prestige/Corolles"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>Fontaine-lEveque>MRS_Le_Hanois>"
            "NBB_PDF_assets_debt_omzet_empty_bellechasse_absorption"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/omzet code70); "
            "INAMI/AViQ vs dagprijs split; Belle Chasse 0454.971.669 absorption matrix "
            "(activa/schulden/places/FTE) since 28.01.2026; 2 VE euro matrix; AV notulen"
        ),
        "why_it_matters": (
            "Medium CW shows 2.47m bruto BV ROB/MRS (~84 places) with unpublished omzet and "
            "no balanstotaal/assets/debt while KBO shows mid-2026 absorption of Belle Chasse — "
            "material L5 residual for FOI"
        ),
        "priority": "8",
        "recipient_body": "Maison de Repos et de Soins Le Hanois BV / Château Belle Chasse path",
        "recipient_email": "direction@lehanois.be",
        "recipient_postal": "Rue du Hanois 1, 6140 Fontaine-l'Évêque",
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
            "alt FOI info@bellechasse.be; preferred stall FARO/AIESH/REW YE2024; "
            "skipped opaque ZS Hainaut-Est"
        ),
    },
)

update_rq()
update_loop_state()
print("OK tick2156 Le Hanois")
