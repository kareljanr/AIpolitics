# tick 2095 — rq_2095 Begralim / Grauwzusters Limburg YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T04:50:00Z"
TICK = 2095
ENTITY = "vzw_begralim_grauwzusters_limburg"
GAP = "gap_begralim_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
LB = "lb_begralim_omzet_jump_22_67m_pnl_drop_jr2025"
COMM = "comm_begralim_jr2025_statutory_wzc"

OMZET = 22668926
PNL = 1062496
EQUITY = 34324320
BRUTO = 24676423
FTE = 295.8
OMZET24 = 21764395
PNL24 = 1508079
EQUITY24 = 33688838
BRUTO24 = 23759100
FTE24 = 297.5
OMZET_YOY = "+4.16%"
PNL_YOY = "DROP -29.55%"
EQUITY_YOY = "+1.89%"
BRUTO_YOY = "+3.86%"
FTE_YOY = "DROP -0.57%"
FILED = "23.07.2026"
KBO = "0428.374.764"
EMAIL = "info@begralim.be"
ADDR = "Demerstraat 80, 3500 Hasselt"
SITE = "https://begralim.be/"
CW_NL = "https://www.companyweb.be/nl/0428374764/bejaardenzorg-grauwzusters-limburg"
CW_EN = "https://www.companyweb.be/en/0428374764/bejaardenzorg-grauwzusters-limburg"
CW_FR = "https://www.companyweb.be/fr/0428374764/bejaardenzorg-grauwzusters-limburg"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0428374764"
PI = "5.4"
ABSURD = "5.2"
COST = "5.6"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Begralim / Grauwzusters Limburg, Sint-Lucia Turnhout, Lidwina Mol, "
    "Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, "
    "De Lovie Poperinge, Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, "
    "WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, "
    "WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, "
    "Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, "
    "WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, "
    "Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, "
    "Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, "
    "Always Home, Armonea, WZC Sint-Barbara Herselt, Molenheide, De Vaeren, "
    "WoonZorgGroep Arendonk, Solidum, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
    "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
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
        if r["task_id"] == "rq_2095":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2095 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Begralim / Grauwzusters Limburg YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Begralim / Bejaardenzorg Grauwzusters Limburg YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.301 ROB 5 VE"
            )
            r["notes"] = (
                f"tick{TICK} Begralim Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2096; next every-10 2100"
            )
            found = True
    if not found:
        raise SystemExit("rq_2095 missing")
    if not any(r["task_id"] == "rq_2096" for r in rows):
        rows.append(
            {
                "task_id": "rq_2096",
                "title": (
                    "leftover dual hole-fill after Begralim — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC-zorg"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2095 after Begralim / Grauwzusters Limburg YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2095 Begralim; next every-10 2100; "
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
                "last_unit_id": "rq_2095",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Begralim {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; NACE 87.301 5 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2096; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_begralim_jr2025_cw",
                "title": "Companyweb NL — Begralim / Grauwzusters Limburg YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_begralim_jr2025_cw_en",
                "title": "Companyweb EN — Begralim / Grauwzusters Limburg YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_begralim_jr2025_cw_fr",
                "title": "Companyweb FR — Begralim / Grauwzusters Limburg YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_begralim_kbo_{TICK}",
                "title": "KBO — Begralim 0428.374.764",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 5 VE; NACE 87.301 ROB; "
                    f"zetel Demerstraat 80 Hasselt; {EMAIL}"
                ),
            },
            {
                "source_id": f"src_begralim_site_{TICK}",
                "title": "Begralim website / contact",
                "url": SITE,
                "publisher": "Begralim",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; WZC Hasselt/Tongeren/Riemst; Demerstraat 80 Hasselt; {EMAIL}"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_begralim_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_begralim_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; bruto {BRUTO}",
            },
            {
                "budget_id": "bud_begralim_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_begralim_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_begralim_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_begralim_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_begralim_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_begralim_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_begralim_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_begralim_jr2025_cw_en",
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
                    "Begralim YE2025 leftover dual (omzet JUMP 22.67m / pnl DROP 1.06m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "WZC residents Begralim campuses Hasselt/Tongeren/Riemst"
                ),
                "legal_basis": (
                    f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO}; NACE 87.301)"
                ),
                "decision_date": "2026-07-23",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": (
                    "Residential elderly care Limburg (Begralim / Grauwzusters)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl DROP -29.55pct "
                    "with omzet JUMP +4.16pct"
                ),
                "source_id": "src_begralim_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>Limburg>Hasselt>Begralim_Grauwzusters>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Begralim omzet JUMP 22.67m / pnl DROP (YE2025)",
                "level": "L5",
                "type": "entity_statutory",
                "hierarchy_path": (
                    "Vlaanderen>Limburg>Hasselt>Begralim_Grauwzusters>JR2025_statutory_L5"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO}; "
                    f"pnl PROFIT {PNL} {PNL_YOY}; equity {EQUITY}; FTE {FTE} {FTE_YOY}; "
                    "assets/debt Unknown"
                ),
                "confidence": "medium",
                "source_id": "src_begralim_jr2025_cw_en",
                "beneficiaries": "WZC residents Limburg (3 campuses)",
                "stated_goal": "Non-profit residential elderly care",
                "measured_outcome": (
                    f"PROFIT {PNL} after DROP from {PNL24}; omzet still JUMP"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "FOI NBB PDF + subsidy/omzet split + campus matrix; "
                    "hold until balance sheet"
                ),
                "status": "watch",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; preferred FARO/AIESH/REW still YE2024; "
                    f"FOI {GAP} ready not sent"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Begralim / Bejaardenzorg Grauwzusters Limburg",
                "name_fr": "Begralim / Soins aux personnes âgees Grauwzusters Limbourg",
                "name_en": "Begralim / Grauwzusters Limburg elderly care",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 5 VE; "
                    f"NACE 87.301 ROB; omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; "
                    f"assets/debt Unknown; neerlegging {FILED}; FOI {GAP}; "
                    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "campuses Sint-Elisabeth Hasselt / Sint-Franciscus Tongeren / Eyckendael Riemst"
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
                    "Vlaanderen>Limburg>Hasselt>Begralim>NBB_PDF_assets_debt_pnl_drop"
                ),
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); "
                    "public subsidy vs omzet split; campus Hasselt/Tongeren/Riemst matrix; "
                    "pnl DROP path despite omzet JUMP"
                ),
                "why_it_matters": (
                    "Medium CW shows 22.67m omzet public Limburg WZC group with pnl DROP "
                    "-29.55% to 1.06m without balance sheet"
                ),
                "priority": "8",
                "recipient_body": "Begralim VZW / Bejaardenzorg Grauwzusters Limburg",
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
                    f"tick{TICK}; human-send only; Medium CW; next every-10 2100"
                ),
            }
        ],
    )

    update_research_queue()
    write_loop_state()

    entry = f"""

## Tick {TICK} - {UTC} - rq_2095 Begralim (omzet JUMP 22.67m / pnl DROP 1.06m / Medium)

- Unit: **rq_2095** leftover dual after **rq_2094 Sint-Lucia**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Begralim / Bejaardenzorg Grauwzusters Limburg** YE2025 (KBO **{KBO}**; Demerstraat 80 Hasselt; Limburg **VZW** WZC NACE **87.301** ROB / **5 VE**; campuses Sint-Elisabeth Hasselt / Sint-Franciscus Tongeren / Eyckendael Riemst). Do not redo Sint-Lucia/Lidwina/SED Zoutleeuw/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE NACE 87.301; email {EMAIL}; site {SITE}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} omzet proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2095=done + rq_2096 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2095/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2096 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "gap", GAP)


if __name__ == "__main__":
    main()
