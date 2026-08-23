# tick 2075 — rq_2075 Sint-Jozef Brugge Sint-Michiels YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-24T23:50:00Z"
TICK = 2075
ENTITY = "vzw_wzc_sint_jozef_brugge_sint_michiels"
GAP = "gap_sj_brugge_nbb_pdf_assets_debt_bruto_fte_drop_matrix_l5"
LB = "lb_sj_brugge_omzet_jump_12_38m_bruto_fte_drop_jr2025"
COMM = "comm_sj_brugge_jr2025_statutory_wzc"

OMZET = 12384613
PNL = 684393
EQUITY = 17179643
BRUTO = 10400160
FTE = 115.4
OMZET24 = 11918670
PNL24 = 667220
EQUITY24 = 16802025
BRUTO24 = 10809249
FTE24 = 126.4
OMZET_YOY = "+3.91%"
PNL_YOY = "+2.57%"
EQUITY_YOY = "+2.25%"
BRUTO_YOY = "-3.78%"
FTE_YOY = "-8.70%"
FILED = "03.07.2026"
KBO = "0461.563.315"
EMAIL = "info@wooncentrum-st-jozef.be"
ADDR = "Spoorwegstraat 250, 8200 Brugge"
SITE = "https://www.sintjozef-wzc-sintmichiels.be/"
CW_NL = "https://www.companyweb.be/nl/0461563315/sint-jozef-wonen-leven-en-zorg-sint-michiels-brugge"
CW_EN = "https://www.companyweb.be/en/0461563315/sint-jozef-wonen-leven-en-zorg-sint-michiels-brugge"
CW_FR = "https://www.companyweb.be/fr/0461563315/sint-jozef-wonen-leven-en-zorg-sint-michiels-brugge"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461563315"
PI = "5.2"

DO_NOT_REDO = (
    "Do NOT redo Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
    "WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)


def append_csv(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as fh:
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
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2075":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2075 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Sint-Jozef Brugge Sint-Michiels YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Sint-Jozef Brugge Sint-Michiels YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}; DISTINCT Huize SJ Ieper/Rumst/Rillaar; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} SJ Brugge Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2076; next every-10 2080"
            )
    if not any(r["task_id"] == "rq_2076" for r in rows):
        rows.append(
            {
                "task_id": "rq_2076",
                "title": "leftover dual hole-fill after SJ Brugge — prefer AGB/FARO-YE2025/AIESH-REW/ZorgWelzijn-Kuurne",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2075 after Sint-Jozef Brugge Sint-Michiels YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Zorg en Welzijn Kuurne 0412.703.029 YE2025 "
                    "(KBO confirms aanbestedende overheid — take as public WZC dual) / unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2075 SJ Brugge Sint-Michiels; next every-10 2080",
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
                "last_unit_id": "rq_2075",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover SJ Brugge Sint-Michiels {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Kuurne YE2025 aanbestedende deferred; "
                    "next rq_2076; next every-10 2080; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_sj_brugge_jr2025_cw",
                "title": "Companyweb NL — Sint-Jozef Brugge Sint-Michiels YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "title": "Companyweb EN — Sint-Jozef Brugge Sint-Michiels YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_sj_brugge_jr2025_cw_fr",
                "title": "Companyweb FR — Sint-Jozef Brugge Sint-Michiels YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_sj_brugge_kbo_{TICK}",
                "title": "KBO — Sint-Jozef Brugge Sint-Michiels 0461.563.315",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-24",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende overheid 1 VE; NACE 87.101; {EMAIL}",
            },
            {
                "source_id": f"src_sj_brugge_site_{TICK}",
                "title": "Sint-Jozef WZC Sint-Michiels Brugge website",
                "url": SITE,
                "publisher": "WZC Sint-Jozef Brugge vzw",
                "accessed_date": "2026-08-24",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; KBO email {EMAIL}; ~198 places / KV / dagverzorging Emaus / Seniorie 't Wallant",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_sj_brugge_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_sj_brugge_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {PNL_YOY} vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_sj_brugge_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_sj_brugge_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_sj_brugge_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE DROP {FTE} ({FTE_YOY}) vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Sint-Jozef Brugge YE2025 leftover dual (omzet JUMP 12.38m / bruto+FTE DROP)",
                "entity_id": ENTITY,
                "beneficiary": "Brugge Sint-Michiels elderly residents (WZC Sint-Jozef / KV / Emaus / 't Wallant)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO})",
                "decision_date": "2026-07-03",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                    f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": "WZC residential elderly care Brugge Sint-Michiels (~198 places + KV/dagverzorging/assistentiewoningen)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain bruto DROP -3.78pct and FTE DROP -8.7pct with omzet/pnl JUMP",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Brugge>Sint_Michiels>Sint_Jozef>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; DISTINCT Huize SJ Ieper/Rumst/Rillaar; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Sint-Jozef Brugge omzet JUMP 12.38m / bruto+FTE DROP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Brugge>Sint_Michiels>Sint_Jozef>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; bruto+FTE DROP vs omzet JUMP",
                "confidence": "medium",
                "source_id": "src_sj_brugge_jr2025_cw_en",
                "beneficiaries": "WZC/KV/dagverzorging/assistentiewoning clients Brugge Sint-Michiels (~198 beds class)",
                "stated_goal": "Residential elderly care Brugge Sint-Michiels",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
                    f"bruto DROP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": "5.2",
                "cost_score": "5.2",
                "difficulty": "4.0",
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain bruto DROP and FTE DROP -8.7pct with omzet/pnl JUMP; map IFIC/Alivia vs dagprijs split",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; DISTINCT Huize SJ Ieper",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Sint-Jozef, wonen, leven en zorg, Sint-Michiels Brugge vzw",
                "name_fr": "Sint-Jozef, habitation, vie et soins, Sint-Michiels Bruges ASBL",
                "name_en": "Sint-Jozef residential care VZW (Brugge Sint-Michiels)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende overheid 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "DISTINCT Huize Sint-Jozef Ieper / Sint-Jozef Rumst / Sint-Jozef Rillaar"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Brugge>Sint_Michiels>Sint_Jozef>NBB_PDF_assets_debt_bruto_fte_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    "explanation of bruto DROP -3.78pct and FTE DROP -8.70pct (126.4→115.4) with omzet JUMP +3.91pct and pnl JUMP +2.57pct"
                ),
                "why_it_matters": (
                    "Medium CW shows 12.38m omzet WZC VZW with margin/staffing compression without balanstotaal/assets/debt; "
                    "material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "Sint-Jozef wonen leven en zorg Sint-Michiels Brugge vzw",
                "recipient_email": EMAIL,
                "recipient_postal": ADDR,
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-24",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2080",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Sint-Jozef Brugge Sint-Michiels (NBB PDF / assets-debt / bruto-FTE-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sint-Jozef wonen leven en zorg Sint-Michiels Brugge VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY} vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **1 VE**; zetel Spoorwegstraat 250 Brugge; NACE 87.101; tel 050/30.33.11; email {EMAIL}.
- DISTINCT from Huize Sint-Jozef Ieper / Sint-Jozef Rumst / Sint-Jozef Rillaar.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Sint-Jozef, wonen, leven en zorg, Sint-Michiels Brugge vzw — Spoorwegstraat 250, 8200 Brugge
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint-Jozef Brugge + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling brutomarge van EUR{BRUTO24} (YE2024) naar EUR{BRUTO} (YE2025; {BRUTO_YOY}) en FTE van {FTE24} naar {FTE} ({FTE_YOY}) bij omzetgroei {OMZET_YOY} en winstgroei {PNL_YOY}.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )

    update_research_queue()
    write_loop_state()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2075 Sint-Jozef Brugge Sint-Michiels (omzet JUMP 12.38m / bruto+FTE DROP / Medium)

- Unit: **rq_2075** leftover dual after **rq_2074 HH Grimbergen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **Sint-Jozef Brugge Sint-Michiels** YE2025 (KBO **{KBO}**; Spoorwegstraat 250 Brugge; West-Vlaanderen **aanbestedende-overheid VZW** WZC / **1 VE**; ~198 places). Zorg en Welzijn Kuurne YE2025 also live (KBO confirms aanbestedende) - deferred. Do not redo HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY} vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2075=done + rq_2076 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2075/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2076 (AGB/FARO-if-YE2025 / AIESH-REW / ZorgWelzijn-Kuurne deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "bruto", BRUTO, "fte", FTE)


if __name__ == "__main__":
    main()
