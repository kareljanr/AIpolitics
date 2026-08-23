# tick 2087 — rq_2087 WZC Lindelo Lille YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T02:50:00Z"
TICK = 2087
ENTITY = "vzw_wzc_lindelo_lille"
GAP = "gap_lindelo_nbb_pdf_assets_debt_pnl_deeper_loss_fte_jump_matrix_l5"
LB = "lb_lindelo_omzet_jump_10_43m_pnl_deeper_loss_fte_jump_jr2025"
COMM = "comm_lindelo_jr2025_statutory_wzc"

OMZET = 10431746
PNL = -225489
EQUITY = 9429339
BRUTO = 11726653
FTE = 166.9
OMZET24 = 10247309
PNL24 = -12877
EQUITY24 = 9946153
BRUTO24 = 11390217
FTE24 = 158.3
OMZET_YOY = "+1.80%"
PNL_YOY = "DEEPER LOSS"
EQUITY_YOY = "-5.19%"
BRUTO_YOY = "+2.95%"
FTE_YOY = "+5.43%"
FILED = "17.06.2026"
KBO = "0418.352.387"
EMAIL = "info@lindelo.be"
ADDR = "Kerkplein 20, 2275 Lille"
SITE = "https://www.lindelo.be/"
CW_NL = "https://www.companyweb.be/nl/0418352387/woonzorgcentrum-lindelo"
CW_EN = "https://www.companyweb.be/en/0418352387/woonzorgcentrum-lindelo"
CW_FR = "https://www.companyweb.be/fr/0418352387/woonzorgcentrum-lindelo"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418352387"
PI = "5.4"
ABSURD = "5.0"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
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
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Prefer deferred Ocura 0443.072.838 / De Lovie 0410.853.396 if unused."
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
        if r["task_id"] == "rq_2087":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2087 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — WZC Lindelo Lille YE2025 Medium"
            r["instructions"] = (
                "Completed leftover WZC Lindelo Lille YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "deferred Ocura/De Lovie"
            )
            r["notes"] = (
                f"tick{TICK} Lindelo Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl DEEPER LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2088; next every-10 2090; deferred Ocura/De Lovie"
            )
    if not any(r["task_id"] == "rq_2088" for r in rows):
        rows.append(
            {
                "task_id": "rq_2088",
                "title": "leftover dual hole-fill after Lindelo — prefer AGB/FARO-YE2025/AIESH-REW/Ocura-Lovie",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2087 after WZC Lindelo Lille YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Ocura 0443.072.838 / "
                    "De Lovie 0410.853.396 if unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2087 Lindelo; next every-10 2090; prefer Ocura/De Lovie deferred",
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
                "last_unit_id": "rq_2087",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover WZC Lindelo Lille {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl DEEPER LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; deferred Ocura/De Lovie; "
                    "next rq_2088; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_lindelo_jr2025_cw",
                "title": "Companyweb NL — WZC Lindelo Lille YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_lindelo_jr2025_cw_en",
                "title": "Companyweb EN — WZC Lindelo Lille YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_lindelo_jr2025_cw_fr",
                "title": "Companyweb FR — WZC Lindelo Lille YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_lindelo_kbo_{TICK}",
                "title": "KBO — Woonzorgcentrum Lindelo 0418.352.387",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende 1 VE; NACE 87.101; zetel Kerkplein 20 Lille; {EMAIL}",
            },
            {
                "source_id": f"src_lindelo_site_{TICK}",
                "title": "WZC Lindelo website (Lille)",
                "url": SITE,
                "publisher": "WZC Lindelo",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; Kerkplein 20 Lille; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_lindelo_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_lindelo_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_lindelo_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_lindelo_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DEEPER LOSS vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_lindelo_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_lindelo_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_lindelo_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_lindelo_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_lindelo_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_lindelo_jr2025_cw_en",
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
                "title": "WZC Lindelo Lille YE2025 leftover dual (omzet JUMP 10.43m / pnl DEEPER LOSS)",
                "entity_id": ENTITY,
                "beneficiary": "Lille elderly residents (WZC Lindelo / aanbestedende VZW)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg / aanbestedende overheid (KBO {KBO})",
                "decision_date": "2026-06-17",
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
                "stated_goal": "WZC residential elderly care Lille (Kerkplein 20)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain deeper LOSS with FTE JUMP",
                "source_id": "src_lindelo_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Antwerpen>Lille>Lindelo>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "WZC Lindelo Lille omzet JUMP 10.43m / pnl DEEPER LOSS + FTE JUMP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>Antwerpen>Lille>Lindelo>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; deeper LOSS with FTE JUMP",
                "confidence": "medium",
                "source_id": "src_lindelo_jr2025_cw_en",
                "beneficiaries": "WZC clients Lille (Lindelo)",
                "stated_goal": "Residential elderly care Lille",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl DEEPER LOSS vs YE2024 {PNL24}; equity DROP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE JUMP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DEEPER LOSS (EUR-12877→EUR-225489) with FTE JUMP 158.3→166.9 and omzet JUMP +1.80pct; map IFIC/Alivia vs dagprijs",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Antwerpen aanbestedende WZC VZW",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Woonzorgcentrum Lindelo vzw (Lille)",
                "name_fr": "MRS Lindelo ASBL (Lille)",
                "name_en": "WZC Lindelo VZW (Lille)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl DEEPER LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Kerkplein 20 Lille; NACE 87.101"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Antwerpen>Lille>Lindelo>NBB_PDF_assets_debt_pnl_deeper_loss_fte_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    "explanation of pnl DEEPER LOSS from EUR-12877 (YE2024) to EUR-225489 (YE2025) with "
                    f"FTE JUMP {FTE24}→{FTE} ({FTE_YOY}) and omzet JUMP {OMZET_YOY}"
                ),
                "why_it_matters": (
                    "Medium CW shows 10.43m omzet aanbestedende-overheid WZC VZW with deepening losses despite "
                    "rising omzet/FTE without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "Woonzorgcentrum Lindelo vzw",
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
        f"""# FOI draft — WZC Lindelo Lille (NBB PDF / assets-debt / pnl-deeper-loss / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Lindelo VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** DEEPER vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **1 VE**; zetel Kerkplein 20 Lille; NACE 87.101; email {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred next: Ocura / De Lovie.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Lindelo vzw — Kerkplein 20, 2275 Lille
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Lindelo + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de verdieping van het verlies van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025) bij omzetgroei {OMZET_YOY} en FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
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

## Tick {TICK} - {UTC} - rq_2087 WZC Lindelo Lille (omzet JUMP 10.43m / pnl DEEPER LOSS 0.23m / Medium)

- Unit: **rq_2087** leftover dual after **rq_2086 Medemens** (in_progress claim for Lindelo/Ocura/Lovie). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **WZC Lindelo** YE2025 (KBO **{KBO}**; Kerkplein 20 Lille; Antwerpen **aanbestedende-overheid VZW** WZC / **1 VE**). Deferred Ocura / De Lovie remain live unused. Do not redo Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** DEEPER vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2087=done + rq_2088 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2087/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2088 (AGB/FARO-if-YE2025 / AIESH-REW / Ocura-Lovie deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()
