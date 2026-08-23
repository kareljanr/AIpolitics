# tick 2092 — rq_2092 Lidwina Mol YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T04:05:00Z"
TICK = 2092
ENTITY = "vzw_lidwina_mol"
GAP = "gap_lidwina_nbb_pdf_assets_debt_bruto_vs_omzet_pnl_jump_matrix_l5"
LB = "lb_lidwina_bruto_jump_21_60m_omzet_10_94m_pnl_jump_jr2025"
COMM = "comm_lidwina_jr2025_statutory_maatwerk"

OMZET = 10939532
PNL = 999268
EQUITY = 24353329
BRUTO = 21595069
FTE = 515.1
OMZET24 = 9687935
PNL24 = 726326
EQUITY24 = 23226527
BRUTO24 = 20045974
FTE24 = 506.8
OMZET_YOY = "+12.92%"
PNL_YOY = "JUMP +37.58%"
EQUITY_YOY = "+4.85%"
BRUTO_YOY = "+7.73%"
FTE_YOY = "+1.64%"
FILED = "26.05.2026"
KBO = "0407.601.720"
EMAIL = "info@lidwina.be"
ADDR = "Postelarenweg 213, 2400 Mol"
SITE = "https://www.lidwina.be/"
CW_NL = "https://www.companyweb.be/nl/0407601720/lidwina-vzw"
CW_EN = "https://www.companyweb.be/en/0407601720/lidwina-vzw"
CW_FR = "https://www.companyweb.be/fr/0407601720/lidwina-vzw"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407601720"
PI = "5.2"
ABSURD = "4.5"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Lidwina Mol, CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, De Lovie Poperinge, "
    "Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
    "Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, "
    "Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, "
    "VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, "
    "WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, "
    "Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, "
    "Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, "
    "Always Home, Armonea, WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
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
        if r["task_id"] == "rq_2092":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2092 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Lidwina Mol YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Lidwina Mol YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 88.993 maatwerk 5 VE"
            )
            r["notes"] = (
                f"tick{TICK} Lidwina Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2093; next every-10 2100"
            )
    if not any(r["task_id"] == "rq_2093" for r in rows):
        rows.append(
            {
                "task_id": "rq_2093",
                "title": "leftover dual hole-fill after Lidwina — prefer AGB/FARO-YE2025/AIESH-REW/unused",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2092 after Lidwina Mol YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2092 Lidwina; next every-10 2100",
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
                "last_unit_id": "rq_2092",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Lidwina Mol {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; NACE 88.993 5 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2093; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_lidwina_jr2025_cw",
                "title": "Companyweb NL — Lidwina Mol YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_lidwina_jr2025_cw_en",
                "title": "Companyweb EN — Lidwina Mol YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_lidwina_jr2025_cw_fr",
                "title": "Companyweb FR — Lidwina Mol YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_lidwina_kbo_{TICK}",
                "title": "KBO — Lidwina 0407.601.720",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW 5 VE; NACE 88.993 maatwerk/social workshop; zetel Postelarenweg 213 Mol; {EMAIL}",
            },
            {
                "source_id": f"src_lidwina_site_{TICK}",
                "title": "Lidwina website (Mol)",
                "url": SITE,
                "publisher": "Lidwina",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; maatwerkbedrijf Mol; {EMAIL}; tel 014 33 06 60",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_lidwina_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_lidwina_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; bruto {BRUTO} better spend proxy",
            },
            {
                "budget_id": "bud_lidwina_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin (incl. subsidies)",
                "source_id": "src_lidwina_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}; primary operating-scale proxy",
            },
            {
                "budget_id": "bud_lidwina_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_lidwina_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_lidwina_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_lidwina_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_lidwina_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_lidwina_jr2025_cw_en",
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
                "title": "Lidwina Mol YE2025 leftover dual (bruto JUMP 21.60m / omzet 10.94m / pnl JUMP)",
                "entity_id": ENTITY,
                "beneficiary": "Persons with disabilities / maatwerk employees Kempen (Lidwina 5 VE)",
                "legal_basis": f"VZW maatwerkbedrijf / publiek gesubsidieerde sociale economie (KBO {KBO}; NACE 88.993)",
                "decision_date": "2026-05-26",
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
                "stated_goal": "Sheltered / customised employment (maatwerk) Mol",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs omzet split FOI; explain bruto 21.6m vs omzet 10.9m and pnl JUMP +37.6pct",
                "source_id": "src_lidwina_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Antwerpen>Mol>Lidwina>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; bruto>omzet subsidy path; "
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
                "name": "Lidwina bruto JUMP 21.60m / omzet 10.94m / pnl JUMP (YE2025)",
                "level": "L5",
                "type": "maatwerk_vzw_statutory",
                "hierarchy_path": "Vlaanderen>Antwerpen>Mol>Lidwina>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": "CW bruto proxy (incl. subsidies); omzet 10.94m; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_lidwina_jr2025_cw_en",
                "beneficiaries": "Maatwerk / sheltered employment clients Mol (Lidwina 5 VE)",
                "stated_goal": "Customised employment for persons with disabilities",
                "measured_outcome": (
                    f"bruto JUMP {BRUTO_YOY}; omzet JUMP {OMZET_YOY}; pnl JUMP vs YE2024 {PNL24}; "
                    f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; map ESF/VDAB/maatwerk subsidies vs omzet 10.94m; explain pnl JUMP +37.58pct with FTE JUMP 506.8→515.1",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; NACE 88.993 maatwerk 5 VE; bruto>omzet",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Lidwina vzw (Mol)",
                "name_fr": "Lidwina ASBL (Mol)",
                "name_en": "Lidwina VZW (Mol)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 5 VE; "
                    f"NACE 88.993 maatwerk/social workshop; omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; "
                    f"neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Postelarenweg 213 Mol"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Antwerpen>Mol>Lidwina>NBB_PDF_assets_debt_bruto_vs_omzet_pnl_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); split subsidies (maatwerk/VDAB/ESF/other code73/74) "
                    f"vs commercial omzet; explanation of bruto EUR{BRUTO} vs omzet EUR{OMZET} and pnl JUMP "
                    f"from EUR{PNL24} to EUR{PNL} ({PNL_YOY})"
                ),
                "why_it_matters": (
                    "Medium CW shows maatwerk VZW with bruto 21.60m vs omzet 10.94m and sharp pnl JUMP "
                    "without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "Lidwina vzw",
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
                "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2100",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Lidwina Mol (NBB PDF / assets-debt / bruto-vs-omzet / pnl-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Lidwina VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** JUMP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **5 VE**; NACE **88.993** (maatwerk / social workshop); zetel Postelarenweg 213 Mol; email {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.
- Note: bruto > omzet — FOI must map subsidy vs commercial turnover.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Lidwina vzw — Postelarenweg 213, 2400 Mol
{EMAIL}
cc: Departement Werk en Sociale Economie / VDAB indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Lidwina + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde maatwerkactiviteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (maatwerksteun, VDAB, ESF, andere code73/74) vs omzet 2025 (bruto EUR{BRUTO} vs omzet EUR{OMZET}).
4. Toelichting van de winststijging van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025; +37.58%) bij FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
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

## Tick {TICK} - {UTC} - rq_2092 Lidwina Mol (bruto JUMP 21.60m / omzet JUMP 10.94m / pnl JUMP 1.00m / Medium)

- Unit: **rq_2092** leftover dual after **rq_2091 Zilvervogel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **Lidwina** YE2025 (KBO **{KBO}**; Postelarenweg 213 Mol; Antwerpen **VZW** maatwerk NACE **88.993** / **5 VE**). Do not redo Zilvervogel/Familiezorg/Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** JUMP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE NACE 88.993; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} bruto proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2092=done + rq_2093 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2092/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2093 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()
