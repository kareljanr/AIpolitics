# tick 2081 — rq_2081 leftover dual WZC Mater Dei Heikruis YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T01:20:00Z"
TICK = 2081
ENTITY = "vzw_wzc_mater_dei_heikruis_pepingen"
GAP = "gap_mater_dei_nbb_pdf_assets_debt_pnl_flip_fte_jump_matrix_l5"
LB = "lb_mater_dei_omzet_jump_5_81m_pnl_flip_fte_jump_jr2025"
COMM = "comm_mater_dei_jr2025_statutory_wzc"

OMZET = 5806028
PNL = 222850
EQUITY = 4184416
BRUTO = 6204899
FTE = 101.9
OMZET24 = 5437353
PNL24 = -455010
EQUITY24 = 3961566
BRUTO24 = 5930849
FTE24 = 94.6
OMZET_YOY = "+6.78%"
PNL_YOY = "FLIP PROFIT vs YE2024 LOSS"
EQUITY_YOY = "+5.63%"
BRUTO_YOY = "+4.62%"
FTE_YOY = "+7.72%"
FILED = "19.06.2026"
KBO = "0428.659.430"
EMAIL = "info@materdei-wzc.be"
ADDR = "Molenhofstraat 31, 1670 Pepingen (Heikruis)"
SITE = "https://www.materdei-wzc.be/"
CW_NL = "https://www.companyweb.be/nl/0428659430/woonzorgcentrum-mater-dei-heikruis"
CW_EN = "https://www.companyweb.be/en/0428659430/woonzorgcentrum-mater-dei-heikruis"
CW_FR = "https://www.companyweb.be/fr/0428659430/woonzorgcentrum-mater-dei-heikruis"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0428659430"
PI = "5.3"
ABSURD = "4.8"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, "
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
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, Home Stuyvenberg, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
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
        if r["task_id"] == "rq_2081":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2081 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — WZC Mater Dei Heikruis Pepingen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover WZC Mater Dei Heikruis Pepingen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl FLIP PROFIT {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; DISTINCT Vander Stokken Pepingen; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Mater Dei Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2082; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2082" for r in rows):
        rows.append(
            {
                "task_id": "rq_2082",
                "title": "leftover dual hole-fill after Mater Dei — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2081 after Mater Dei Heikruis Pepingen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2081 Mater Dei; next every-10 2090",
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
                "last_unit_id": "rq_2081",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover WZC Mater Dei Heikruis Pepingen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2082; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def write_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    text = f"""# FOI draft — WZC Mater Dei Heikruis Pepingen (NBB PDF / assets-debt / pnl-flip / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC Mater Dei Heikruis VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** {PNL_YOY} EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; aanbestedende overheid; **2 VE**; zetel Molenhofstraat(H) 31 Pepingen-Heikruis; NACE 87.301 ROB; email {EMAIL}.
- Site: materdei-wzc.be — ~94 places; nieuwbouw path (werf 2025 → 2027).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. DISTINCT from Vander Stokken Pepingen.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC Mater Dei Heikruis vzw — Molenhofstraat 31, 1670 Pepingen
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Mater Dei Heikruis + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de resultaatsomslag van LOSS EUR{abs(PNL24)} (YE2024) naar PROFIT EUR{PNL} (YE2025) bij omzetgroei {OMZET_YOY} en FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
5. Link nieuwbouw/CAPEX (werf okt 2025 → oplevering 2027) vs YE2025 resultaat indien materieel.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
"""
    (FOI / f"{GAP}.md").write_text(text, encoding="utf-8")


def append_log():
    block = f"""

## Tick {TICK} - {UTC} - rq_2081 Mater Dei Heikruis (omzet JUMP 5.81m / pnl FLIP PROFIT 0.22m / Medium)

- Unit: **rq_2081** leftover dual after **rq_2080 Den Akker**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **WZC Mater Dei Heikruis** YE2025 (KBO **{KBO}**; Molenhofstraat 31 Pepingen-Heikruis; Vlaams-Brabant **aanbestedende-overheid VZW** WZC / **2 VE**; ~94 places; nieuwbouw path). DISTINCT from Vander Stokken Pepingen. Do not redo Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** FLIP vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 2 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2081=done + rq_2082 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2081/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2082 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(block)


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_mater_dei_jr2025_cw",
                "title": "Companyweb NL — WZC Mater Dei Heikruis YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_mater_dei_jr2025_cw_en",
                "title": "Companyweb EN — WZC Mater Dei Heikruis YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_mater_dei_jr2025_cw_fr",
                "title": "Companyweb FR — WZC Mater Dei Heikruis YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_mater_dei_kbo_{TICK}",
                "title": "KBO — WZC Mater Dei Heikruis 0428.659.430",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende overheid 2 VE; NACE 87.301; zetel Molenhofstraat 31 Pepingen; email via site {EMAIL}",
            },
            {
                "source_id": f"src_mater_dei_site_{TICK}",
                "title": "WZC Mater Dei Heikruis website",
                "url": SITE,
                "publisher": "WZC Mater Dei Heikruis",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; Molenhofstraat 31 Pepingen-Heikruis; {EMAIL}; nieuwbouw path",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_mater_dei_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_mater_dei_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLIP PROFIT vs YE2024 LOSS {PNL24}",
            },
            {
                "budget_id": "bud_mater_dei_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_mater_dei_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_mater_dei_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_mater_dei_jr2025_cw_en",
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
                "title": "WZC Mater Dei Heikruis Pepingen YE2025 leftover dual (omzet JUMP 5.81m / pnl FLIP)",
                "entity_id": ENTITY,
                "beneficiary": "Pepingen-Heikruis elderly residents (~94 places; nieuwbouw path)",
                "legal_basis": f"VZW WZC / aanbestedende overheid (KBO {KBO})",
                "decision_date": "2026-06-19",
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
                "stated_goal": "WZC residential elderly care Pepingen-Heikruis (Mater Dei)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl FLIP LOSS→PROFIT with FTE JUMP; map nieuwbouw CAPEX",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pepingen>Mater_Dei_Heikruis>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; DISTINCT Vander Stokken Pepingen; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "WZC Mater Dei Heikruis omzet JUMP 5.81m / pnl FLIP PROFIT + FTE JUMP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pepingen>Mater_Dei_Heikruis>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; pnl FLIP with FTE JUMP + nieuwbouw path",
                "confidence": "medium",
                "source_id": "src_mater_dei_jr2025_cw_en",
                "beneficiaries": "WZC clients Pepingen-Heikruis (~94 places)",
                "stated_goal": "Residential elderly care Pepingen-Heikruis",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl FLIP PROFIT vs YE2024 LOSS {PNL24}; "
                    f"equity JUMP {EQUITY_YOY}; bruto JUMP {BRUTO_YOY}; FTE JUMP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS→PROFIT "
                    f"({PNL24}→{PNL}) with FTE JUMP {FTE24}→{FTE} and omzet JUMP {OMZET_YOY}; "
                    "map IFIC/Alivia vs dagprijs; nieuwbouw CAPEX transparency"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                    "Vlaams-Brabant WZC VZW dual; DISTINCT Vander Stokken Pepingen"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "WZC Mater Dei Heikruis vzw (Pepingen)",
                "name_fr": "MR Mater Dei Heikruis ASBL (Pepingen)",
                "name_en": "WZC Mater Dei Heikruis VZW (Pepingen)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende overheid 2 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "DISTINCT Vander Stokken Pepingen; Molenhofstraat 31 Heikruis; ~94 places + nieuwbouw"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pepingen>Mater_Dei_Heikruis>NBB_PDF_assets_debt_pnl_flip_fte_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    f"explanation of pnl FLIP LOSS EUR{abs(PNL24)} (YE2024) → PROFIT EUR{PNL} (YE2025) with "
                    f"FTE JUMP {FTE24}→{FTE} ({FTE_YOY}) and omzet JUMP {OMZET_YOY}; nieuwbouw CAPEX link if material"
                ),
                "why_it_matters": (
                    "Medium CW shows 5.81m omzet erkende WZC VZW (aanbestedende) with sharp LOSS→PROFIT flip "
                    "and FTE JUMP without balanstotaal/assets/debt; material L5 residual for FOI; same gemeente as Vander Stokken"
                ),
                "priority": "8",
                "recipient_body": "WZC Mater Dei Heikruis vzw",
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

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print(f"OK tick{TICK} {ENTITY} omzet={OMZET} pnl={PNL} gap={GAP}")


if __name__ == "__main__":
    main()
