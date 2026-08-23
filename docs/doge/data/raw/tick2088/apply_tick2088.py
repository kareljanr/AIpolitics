# tick 2088 — rq_2088 VZW Woonzorgcentra Ocura Beringen YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T03:05:00Z"
TICK = 2088
ENTITY = "vzw_woonzorgcentra_ocura_beringen"
GAP = "gap_ocura_nbb_pdf_assets_debt_pnl_loss_narrow_equity_drop_matrix_l5"
LB = "lb_ocura_omzet_jump_25_97m_pnl_loss_narrow_fte_drop_jr2025"
COMM = "comm_ocura_jr2025_statutory_wzc_netwerk"

OMZET = 25967828
PNL = -458394
EQUITY = 12438749
BRUTO = 26614138
FTE = 375.3
OMZET24 = 25860977
PNL24 = -949903
EQUITY24 = 13590528
BRUTO24 = 25634759
FTE24 = 376.7
OMZET_YOY = "+0.41%"
PNL_YOY = "LOSS NARROW vs YE2024 LOSS -949903"
EQUITY_YOY = "-8.47%"
BRUTO_YOY = "+3.82%"
FTE_YOY = "-0.37%"
FILED = "13.06.2026"
KBO = "0443.072.838"
EMAIL = "info.beringen@ocura.be"
ADDR = "Havenlaan 7, 3582 Beringen"
SITE = "https://www.ocura.be/"
CW_NL = "https://www.companyweb.be/nl/0443072838/ocura"
CW_EN = "https://www.companyweb.be/en/0443072838/ocura"
CW_FR = "https://www.companyweb.be/fr/0443072838/ocura"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443072838"
PI = "5.4"
ABSURD = "4.7"
COST = "5.8"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, "
    "Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, "
    "WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
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
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum. "
    "Deferred live unused: De Lovie. "
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
        if r["task_id"] == "rq_2088":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2088 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Ocura Beringen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover VZW Woonzorgcentra Ocura Beringen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "deferred De Lovie"
            )
            r["notes"] = (
                f"tick{TICK} Ocura Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl LOSS NARROW {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2089; next every-10 2090; deferred De Lovie"
            )
    if not any(r["task_id"] == "rq_2089" for r in rows):
        rows.append(
            {
                "task_id": "rq_2089",
                "title": "leftover dual hole-fill after Ocura — prefer AGB/FARO-YE2025/AIESH-REW/De Lovie",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2088 after Ocura Beringen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred De Lovie 0410.853.396 "
                    "if unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2088 Ocura; next every-10 2090; prefer De Lovie deferred",
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
                "last_unit_id": "rq_2088",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Ocura Beringen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl LOSS NARROW {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; deferred De Lovie; "
                    "next rq_2089; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_ocura_jr2025_cw",
                "title": "Companyweb NL — Ocura Beringen YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_ocura_jr2025_cw_en",
                "title": "Companyweb EN — Ocura Beringen YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_ocura_jr2025_cw_fr",
                "title": "Companyweb FR — Ocura Beringen YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_ocura_kbo_{TICK}",
                "title": "KBO — VZW Woonzorgcentra Ocura 0443.072.838",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende 5 VE; NACE 87.101 RVT; zetel Havenlaan 7 Beringen; site {EMAIL}",
            },
            {
                "source_id": f"src_ocura_site_{TICK}",
                "title": "Ocura Woonzorgcentra website",
                "url": SITE,
                "publisher": "Ocura",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; multi-site Limburg WZC netwerk; HQ Havenlaan 7 Beringen; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_ocura_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_ocura_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_ocura_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_ocura_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; LOSS vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_ocura_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_ocura_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_ocura_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_ocura_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_ocura_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_ocura_jr2025_cw_en",
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
                "title": "Ocura Beringen YE2025 leftover dual (omzet JUMP 25.97m / pnl LOSS narrow)",
                "entity_id": ENTITY,
                "beneficiary": "Limburg elderly-care clients (Ocura multi-site WZC netwerk, 5 VE)",
                "legal_basis": f"VZW care netwerk / publiek gesubsidieerde zorg / aanbestedende overheid (KBO {KBO})",
                "decision_date": "2026-06-13",
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
                "stated_goal": "Multi-site elderly care Limburg (Ocura Woonzorgcentra)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain loss narrow with equity drop -8.47pct",
                "source_id": "src_ocura_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Limburg>Beringen>Ocura>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn; deferred De Lovie"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Ocura Beringen omzet JUMP 25.97m / pnl LOSS narrow + equity DROP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>Limburg>Beringen>Ocura>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; ongoing loss with equity erosion",
                "confidence": "medium",
                "source_id": "src_ocura_jr2025_cw_en",
                "beneficiaries": "Ocura multi-site WZC clients Limburg (5 VE)",
                "stated_goal": "Elderly care network Limburg",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl LOSS narrow vs YE2024 {PNL24}; equity DROP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidy vs fees across 5 VE; explain equity -8.47pct while loss narrowed -0.95m→-0.46m",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; aanbestedende 5 VE; deferred De Lovie",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "VZW Woonzorgcentra Ocura (Beringen)",
                "name_fr": "ASBL Centres de soins Ocura (Beringen)",
                "name_en": "Ocura Care Homes VZW (Beringen)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende 5 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl LOSS NARROW {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "multi-site Limburg WZC Havenlaan 7 Beringen; NACE 87.101"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Limburg>Beringen>Ocura>NBB_PDF_assets_debt_pnl_loss",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split across 5 VE; "
                    f"explanation of pnl LOSS narrow {PNL} vs YE2024 {PNL24} with equity DROP {EQUITY_YOY} / "
                    f"omzet JUMP {OMZET_YOY} / FTE DROP {FTE24}→{FTE} ({FTE_YOY})"
                ),
                "why_it_matters": (
                    "Medium CW shows 25.97m omzet aanbestedende multi-site WZC VZW with ongoing loss and equity erosion "
                    "without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "VZW Woonzorgcentra Ocura",
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
        f"""# FOI draft — Ocura Beringen (NBB PDF / assets-debt / pnl-loss-narrow / equity-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** VZW Woonzorgcentra Ocura — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** narrow vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **5 VE**; zetel Havenlaan 7 Beringen; NACE 87.101; site email {EMAIL}.
- Site: multi-site Limburg WZC netwerk (Ocura).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live unused: De Lovie.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: VZW Woonzorgcentra Ocura — Havenlaan 7, 3582 Beringen
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Ocura + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde zorg / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, andere code73/74) vs dagprijzen/supplementen 2025, per VE indien beschikbaar.
4. Toelichting van het vernauwende verlies van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025) bij equity-daling {EQUITY_YOY}, omzetstijging {OMZET_YOY} en FTE-daling van {FTE24} naar {FTE} ({FTE_YOY}).
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


## Tick {TICK} - {UTC} - rq_2088 Ocura Beringen (omzet JUMP 25.97m / pnl LOSS narrow 0.46m / Medium)

- Unit: **rq_2088** leftover dual after **rq_2087 Lindelo**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **VZW Woonzorgcentra Ocura** YE2025 (KBO **{KBO}**; Havenlaan 7 Beringen; Limburg **aanbestedende-overheid VZW** WZC netwerk / **5 VE**). Deferred live unused: De Lovie. Do not redo Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** narrow vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 5 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2088=done + rq_2089 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2088/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2089 (AGB/FARO-if-YE2025 / AIESH-REW / De Lovie deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()
