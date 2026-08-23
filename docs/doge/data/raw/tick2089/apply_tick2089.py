# tick 2089 — rq_2089 De Lovie Poperinge YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T03:20:00Z"
TICK = 2089
ENTITY = "vzw_de_lovie_poperinge"
GAP = "gap_lovie_nbb_pdf_assets_debt_bruto_vs_omzet_pnl_drop_matrix_l5"
LB = "lb_lovie_bruto_jump_67_01m_omzet_8_51m_pnl_drop_jr2025"
COMM = "comm_lovie_jr2025_statutory_disability_care"

OMZET = 8507490
PNL = 5372235
EQUITY = 58139102
BRUTO = 67006189
FTE = 732.6
OMZET24 = 8097494
PNL24 = 7060159
EQUITY24 = 52489430
BRUTO24 = 63414583
FTE24 = 708.4
OMZET_YOY = "+5.06%"
PNL_YOY = "DROP -23.91%"
EQUITY_YOY = "+10.76%"
BRUTO_YOY = "+5.66%"
FTE_YOY = "+3.42%"
FILED = "11.06.2026"
KBO = "0410.853.396"
EMAIL = "info@delovie.be"
ADDR = "Krombeekseweg 82, 8970 Poperinge"
SITE = "https://delovie.be/"
CW_NL = "https://www.companyweb.be/nl/0410853396/de-lovie"
CW_EN = "https://www.companyweb.be/en/0410853396/de-lovie"
CW_FR = "https://www.companyweb.be/fr/0410853396/de-lovie"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410853396"
PI = "5.5"
ABSURD = "5.2"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo De Lovie Poperinge, VZW Woonzorgcentra Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, "
    "WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, "
    "WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, "
    "Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, "
    "Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, IPFBW, IGRETEC, Aquiris, "
    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
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
    for r in rows:
        if r["task_id"] == "rq_2089":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2089 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — De Lovie Poperinge YE2025 Medium"
            r["instructions"] = (
                "Completed leftover De Lovie Poperinge YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.202 disability care 33 VE"
            )
            r["notes"] = (
                f"tick{TICK} Lovie Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2090 EVERY-10; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2090" for r in rows):
        rows.append(
            {
                "task_id": "rq_2090",
                "title": "EVERY-10 + leftover dual hole-fill after De Lovie — prefer AGB/FARO-YE2025/AIESH-REW/unused",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2090 EVERY-10 mandatory: refresh progress_every_10_ticks.md + doge_waste_top10_current.md, "
                    "THEN hole-fill one unit after De Lovie Poperinge YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2089 De Lovie; EVERY-10 mandatory this tick",
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
                "last_unit_id": "rq_2089",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover De Lovie Poperinge {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; NACE 87.202 33 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2090 EVERY-10; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_lovie_jr2025_cw",
                "title": "Companyweb NL — De Lovie Poperinge YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_lovie_jr2025_cw_en",
                "title": "Companyweb EN — De Lovie Poperinge YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_lovie_jr2025_cw_fr",
                "title": "Companyweb FR — De Lovie Poperinge YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_lovie_kbo_{TICK}",
                "title": "KBO — De Lovie 0410.853.396",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende 33 VE; NACE 87.202 disability residential; zetel Krombeekseweg 82 Poperinge; {EMAIL}",
            },
            {
                "source_id": f"src_lovie_site_{TICK}",
                "title": "De Lovie website (Poperinge)",
                "url": SITE,
                "publisher": "De Lovie",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; disability care multi-site West-Vlaanderen; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_lovie_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (commercial-ish; bruto much larger)",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; bruto {BRUTO} is better spend proxy",
            },
            {
                "budget_id": "bud_lovie_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin (incl. subsidies)",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}; primary operating-scale proxy",
            },
            {
                "budget_id": "bud_lovie_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_lovie_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_lovie_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE JUMP {FTE} ({FTE_YOY}) vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "De Lovie Poperinge YE2025 leftover dual (bruto JUMP 67.01m / omzet 8.51m / pnl DROP)",
                "entity_id": ENTITY,
                "beneficiary": "Persons with disabilities / residential care West-Vlaanderen (De Lovie 33 VE)",
                "legal_basis": f"VZW disability residential care / publiek gesubsidieerde zorg / aanbestedende overheid (KBO {KBO}; NACE 87.202)",
                "decision_date": "2026-06-11",
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
                "stated_goal": "Multi-site disability residential care (De Lovie / Poperinge)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs omzet split FOI; explain bruto 67m vs omzet 8.5m and pnl DROP",
                "source_id": "src_lovie_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Poperinge>De_Lovie>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; bruto>>omzet typical VZW subsidy path; "
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
                "name": "De Lovie bruto JUMP 67.01m / omzet 8.51m / pnl DROP (YE2025)",
                "level": "L5",
                "type": "disability_care_vzw_statutory",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Poperinge>De_Lovie>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": "CW bruto proxy (incl. subsidies); omzet only 8.51m; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_lovie_jr2025_cw_en",
                "beneficiaries": "Disability residential care clients West-Vlaanderen (De Lovie 33 VE)",
                "stated_goal": "Multi-site disability residential care",
                "measured_outcome": (
                    f"bruto JUMP {BRUTO_YOY}; omzet JUMP {OMZET_YOY}; pnl DROP vs YE2024 {PNL24}; "
                    f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; map code73/74 subsidies vs omzet 8.51m; explain pnl DROP -23.91pct with equity JUMP +10.76pct and bruto 67m scale",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; NACE 87.202 aanbestedende 33 VE; bruto>>omzet opacity",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "De Lovie vzw (Poperinge)",
                "name_fr": "De Lovie ASBL (Poperinge)",
                "name_en": "De Lovie VZW (Poperinge)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende 33 VE; "
                    f"NACE 87.202 disability residential; omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; "
                    f"neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Krombeekseweg 82 Poperinge"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Poperinge>De_Lovie>NBB_PDF_assets_debt_bruto_vs_omzet_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); split subsidies (code73/74 / VAPH / other) "
                    f"vs commercial omzet; explanation of bruto EUR{BRUTO} vs omzet EUR{OMZET} and pnl DROP "
                    f"from EUR{PNL24} to EUR{PNL} ({PNL_YOY}) with equity JUMP {EQUITY_YOY}"
                ),
                "why_it_matters": (
                    "Medium CW shows disability-care VZW with bruto 67.01m vs omzet 8.51m and large equity stock "
                    "without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "De Lovie vzw",
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
                "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2090",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — De Lovie Poperinge (NBB PDF / assets-debt / bruto-vs-omzet / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Lovie VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **33 VE**; NACE **87.202** (disability residential); zetel Krombeekseweg 82 Poperinge; email {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.
- Note: bruto ≫ omzet — FOI must map subsidy vs commercial turnover.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Lovie vzw — Krombeekseweg 82, 8970 Poperinge
{EMAIL}
cc: Departement Zorg / VAPH indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 De Lovie + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde zorg / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (VAPH, IFIC, andere code73/74) vs omzet/eigen bijdragen 2025 (bruto EUR{BRUTO} vs omzet EUR{OMZET}).
4. Toelichting van de winstdaling van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025; -23.91%) bij equity-stijging {EQUITY_YOY} en bruto-stijging {BRUTO_YOY}.
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

## Tick {TICK} - {UTC} - rq_2089 De Lovie (bruto JUMP 67.01m / omzet JUMP 8.51m / pnl DROP 5.37m / Medium)

- Unit: **rq_2089** leftover dual after **rq_2088 Ocura**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **De Lovie** YE2025 (KBO **{KBO}**; Krombeekseweg 82 Poperinge; West-Vlaanderen **aanbestedende-overheid VZW** disability residential NACE **87.202** / **33 VE**). Do not redo Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 33 VE NACE 87.202; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} bruto proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2089=done + rq_2090 open (EVERY-10); loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2089/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090 THIS next tick**). Next: rq_2090 (EVERY-10 mandatory + AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()
