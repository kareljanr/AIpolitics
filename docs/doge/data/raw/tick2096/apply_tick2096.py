# tick 2096 — rq_2096 Familiezorg Gent YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T05:05:00Z"
TICK = 2096
ENTITY = "vzw_familiezorg_gent"
GAP = "gap_familiezorg_gent_nbb_pdf_assets_debt_bruto_vs_omzet_pnl_drop_matrix_l5"
LB = "lb_familiezorg_gent_bruto_jump_70_04m_pnl_drop_jr2025"
COMM = "comm_familiezorg_gent_jr2025_statutory_thuiszorg"

OMZET = 14782023
PNL = 639579
EQUITY = 24209880
BRUTO = 70038917
FTE = 1237.4
OMZET24 = 14043597
PNL24 = 1644314
EQUITY24 = 23575744
BRUTO24 = 68312158
FTE24 = 1240.6
OMZET_YOY = "+5.26%"
PNL_YOY = "DROP -61.10%"
EQUITY_YOY = "+2.69%"
BRUTO_YOY = "+2.53%"
FTE_YOY = "DROP -0.26%"
FILED = "14.07.2026"
KBO = "0412.914.845"
EMAIL = "info@familiezorg.be"
ADDR = "Vogelenzang 29, 9000 Gent"
SITE = "https://www.familiezorg.be/"
CW_NL = "https://www.companyweb.be/nl/0412914845/familiezorg"
CW_EN = "https://www.companyweb.be/en/0412914845/familiezorg"
CW_FR = "https://www.companyweb.be/fr/0412914845/familiezorg"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412914845"
PI = "5.8"
ABSURD = "5.6"
COST = "6.0"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Familiezorg Gent, Begralim / Grauwzusters Limburg, Sint-Lucia Turnhout, "
    "Lidwina Mol, Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, "
    "Familiezorg West-Vlaanderen, De Lovie Poperinge, Ocura Beringen, WZC Lindelo Lille, "
    "De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
    "Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, "
    "WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, "
    "De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, "
    "Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, "
    "VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, "
    "WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, "
    "Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, "
    "Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, "
    "OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, "
    "Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, "
    "Armonea, WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, "
    "Solidum, emeis Belgium, SLG Operaties Vlaanderen, IPFBW, IGRETEC, Aquiris, SPGE, "
    "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, "
    "ETB, Elia, BNO, SWDE, BRUGEL."
)


def append_csv(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        existing = list(reader)
    ids = set()
    id_key = None
    for cand in (
        "source_id",
        "budget_id",
        "commitment_id",
        "item_id",
        "entity_id",
        "gap_id",
        "task_id",
    ):
        if cand in (fieldnames or []):
            id_key = cand
            break
    if id_key:
        ids = {r.get(id_key) for r in existing}
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
        for r in rows:
            if id_key and r.get(id_key) in ids:
                continue
            out = {k: r.get(k, "") for k in fieldnames}
            w.writerow(out)


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == "rq_2096":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2096 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Familiezorg Gent YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Familiezorg Gent YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "NACE 88.101 thuiszorg 2 VE aanbestedende; distinct Familiezorg WV"
            )
            r["notes"] = (
                f"tick{TICK} Familiezorg Gent Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2097; next every-10 2100"
            )
            found = True
    if not found:
        raise SystemExit("rq_2096 missing")
    if not any(r["task_id"] == "rq_2097" for r in rows):
        rows.append(
            {
                "task_id": "rq_2097",
                "title": (
                    "leftover dual hole-fill after Familiezorg Gent — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC-zorg"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2096 after Familiezorg Gent YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2096 Familiezorg Gent; next every-10 2100; "
                    "prefer FARO/AIESH/REW if YE2025 else unused WZC-zorg"
                ),
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
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
                "last_unit_id": "rq_2096",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Familiezorg Gent {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; NACE 88.101 2 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2097; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_familiezorg_gent_jr2025_cw",
                "title": "Companyweb NL — Familiezorg Gent YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "title": "Companyweb EN — Familiezorg Gent YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_familiezorg_gent_jr2025_cw_fr",
                "title": "Companyweb FR — Familiezorg Gent YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_familiezorg_gent_kbo_{TICK}",
                "title": "KBO — Familiezorg Gent 0412.914.845",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW aanbestedende 2 VE; NACE 88.101; "
                    f"zetel Vogelenzang 29 Gent; {EMAIL} / directeur@familiezorg.be"
                ),
            },
            {
                "source_id": f"src_familiezorg_gent_site_{TICK}",
                "title": "Familiezorg website / contact",
                "url": SITE,
                "publisher": "Familiezorg",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; thuiszorg Gent e.o.; Vogelenzang 29 Gent; {EMAIL}"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_familiezorg_gent_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; bruto {BRUTO} primary envelope",
            },
            {
                "budget_id": "bud_familiezorg_gent_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin (primary envelope thuiszorg)",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}; omzet<<bruto",
            },
            {
                "budget_id": "bud_familiezorg_gent_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_familiezorg_gent_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_familiezorg_gent_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} {FTE_YOY} vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Familiezorg Gent YE2025 leftover dual (bruto JUMP 70.04m / pnl DROP 0.64m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "Home-care / elderly clients Familiezorg Gent e.o."
                ),
                "legal_basis": (
                    f"VZW thuiszorg / publiek gesubsidieerde zorg (KBO {KBO}; NACE 88.101; aanbestedende)"
                ),
                "decision_date": "2026-07-14",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": (
                    "Non-profit home care / elderly care East Flanders (Familiezorg Gent)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain bruto>>omzet gap and pnl DROP -61pct"
                ),
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>OostVlaanderen>Gent>Familiezorg_Gent>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope (thuiszorg); assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "distinct Familiezorg WV 0405.112.085"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Familiezorg Gent bruto JUMP 70.04m / pnl DROP (YE2025)",
                "level": "L5",
                "type": "entity_statutory",
                "hierarchy_path": (
                    "Vlaanderen>OostVlaanderen>Gent>Familiezorg_Gent>JR2025_statutory_L5"
                ),
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW YE2025 bruto {BRUTO} JUMP {BRUTO_YOY} (primary); omzet {OMZET} JUMP {OMZET_YOY}; "
                    f"pnl PROFIT {PNL} {PNL_YOY}; equity {EQUITY}; FTE {FTE} {FTE_YOY}; "
                    "assets/debt Unknown; omzet<<bruto thuiszorg"
                ),
                "confidence": "medium",
                "source_id": "src_familiezorg_gent_jr2025_cw_en",
                "beneficiaries": "Home-care / elderly clients Gent e.o.",
                "stated_goal": "Non-profit home care / elderly care",
                "measured_outcome": (
                    f"PROFIT {PNL} after DROP from {PNL24}; bruto still JUMP; omzet<<bruto"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "FOI NBB PDF + subsidy/omzet/bruto split + service matrix; "
                    "hold until balance sheet"
                ),
                "status": "watch",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; preferred FARO/AIESH/REW still YE2024; "
                    f"FOI {GAP} ready not sent; distinct Familiezorg WV"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Familiezorg (Gent) VZW",
                "name_fr": "Familiezorg (Gand) ASBL",
                "name_en": "Familiezorg Gent home / elderly care VZW",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende 2 VE; "
                    f"NACE 88.101 thuiszorg; omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; "
                    f"assets/debt Unknown; neerlegging {FILED}; FOI {GAP}; "
                    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "DISTINCT from Familiezorg West-Vlaanderen 0405.112.085 (tick2090)"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": (
                    "Vlaanderen>OostVlaanderen>Gent>Familiezorg_Gent>NBB_PDF_assets_debt_bruto_omzet_pnl_drop"
                ),
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); "
                    "public subsidy vs omzet vs bruto split; service matrix; "
                    "pnl DROP path despite omzet/bruto JUMP"
                ),
                "why_it_matters": (
                    "Medium CW shows 70.04m bruto public Gent thuiszorg VZW with pnl DROP "
                    "-61.10% to 0.64m and omzet<<bruto without balance sheet"
                ),
                "priority": "8",
                "recipient_body": "Familiezorg VZW Gent",
                "recipient_email": EMAIL,
                "recipient_postal": ADDR,
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
                    f"tick{TICK}; human-send only; Medium CW; next every-10 2100; "
                    "also directeur@familiezorg.be"
                ),
            }
        ],
    )

    update_research_queue()
    write_loop_state()

    entry = f"""

## Tick {TICK} - {UTC} - rq_2096 Familiezorg Gent (bruto JUMP 70.04m / omzet JUMP 14.78m / pnl DROP 0.64m / Medium)

- Unit: **rq_2096** leftover dual after **rq_2095 Begralim**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Familiezorg Gent** YE2025 (KBO **{KBO}**; Vogelenzang 29 Gent; Oost-Vlaanderen **aanbestedende-overheid VZW** thuiszorg NACE **88.101** / **2 VE**). Distinct from Familiezorg WV. Deferred private chains emeis/SLG. Do not redo Begralim/Sint-Lucia/Lidwina/SED Zoutleeuw/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum/emeis/SLG.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 2 VE NACE 88.101; email {EMAIL}; site {SITE}. Bruto used as primary envelope (thuiszorg VZW omzet<<bruto).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} bruto proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2096=done + rq_2097 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2096/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2097 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("OK tick", TICK, "bruto", BRUTO, "omzet", OMZET, "pnl", PNL, "gap", GAP)


if __name__ == "__main__":
    main()
