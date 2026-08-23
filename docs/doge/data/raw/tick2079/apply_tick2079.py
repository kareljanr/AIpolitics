# tick 2079 — rq_2079 WoonZorgcentrum H. Vander Stokken Pepingen YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T00:50:00Z"
TICK = 2079
ENTITY = "vzw_wzc_vander_stokken_pepingen"
GAP = "gap_vander_stokken_nbb_pdf_assets_debt_equity_jump_matrix_l5"
LB = "lb_vander_stokken_omzet_jump_8_87m_equity_jump_72pct_jr2025"
COMM = "comm_vander_stokken_jr2025_statutory_wzc"

OMZET = 8873269
PNL = 1092351
EQUITY = 2594672
BRUTO = 9211921
FTE = 97.7
OMZET24 = 8763961
PNL24 = 1027865
EQUITY24 = 1502322
BRUTO24 = 8918218
FTE24 = 98.9
OMZET_YOY = "+1.25%"
PNL_YOY = "+6.27%"
EQUITY_YOY = "+72.71%"
BRUTO_YOY = "+3.29%"
FTE_YOY = "-1.21%"
FILED = "02.07.2026"
KBO = "0414.678.562"
EMAIL = "centrum@wzchvanderstokken.be"
ADDR = "Palokenstraat 17, 1670 Pepingen"
SITE = "https://www.vanderstokken.be/"
CW_NL = "https://www.companyweb.be/nl/0414678562/woon-zorgcentrum-h-vander-stokken"
CW_EN = "https://www.companyweb.be/en/0414678562/woon-zorgcentrum-h-vander-stokken"
CW_FR = "https://www.companyweb.be/fr/0414678562/woon-zorgcentrum-h-vander-stokken"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414678562"
PI = "5.0"

DO_NOT_REDO = (
    "Do NOT redo WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, "
    "Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, "
    "VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, "
    "Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, "
    "Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
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
        if r["task_id"] == "rq_2079":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2079 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — WZC H. Vander Stokken Pepingen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover WZC H. Vander Stokken Pepingen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Vander Stokken Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m (+72.71pct) bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2080; next every-10 2080"
            )
    if not any(r["task_id"] == "rq_2080" for r in rows):
        rows.append(
            {
                "task_id": "rq_2080",
                "title": "EVERY-10 + leftover dual hole-fill after Vander Stokken — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2080 EVERY-10 mandatory: refresh progress_every_10_ticks.md + doge_waste_top10_current.md, "
                    "THEN hole-fill one unit after Vander Stokken Pepingen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2079 Vander Stokken; EVERY-10 mandatory this tick",
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
                "last_unit_id": "rq_2079",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover WZC H. Vander Stokken Pepingen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m (+72.71pct) "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2080 EVERY-10; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_vander_stokken_jr2025_cw",
                "title": "Companyweb NL — WZC H. Vander Stokken Pepingen YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "title": "Companyweb EN — WZC H. Vander Stokken Pepingen YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}; equity JUMP {EQUITY_YOY}",
            },
            {
                "source_id": "src_vander_stokken_jr2025_cw_fr",
                "title": "Companyweb FR — WZC H. Vander Stokken Pepingen YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_vander_stokken_kbo_{TICK}",
                "title": "KBO — WoonZorgcentrum H. Vander Stokken 0414.678.562",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW 1 VE; NACE 87.101; zetel Palokenstraat 17 Pepingen; email via site {EMAIL}",
            },
            {
                "source_id": f"src_vander_stokken_site_{TICK}",
                "title": "WZC Henri Vander Stokken website (Pepingen)",
                "url": SITE,
                "publisher": "WZC H. Vander Stokken",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; ~127 beds + Residentie Paloken AW; {EMAIL}; tel 02 363 06 30",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_vander_stokken_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_vander_stokken_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {PNL_YOY} vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_vander_stokken_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24} (~retained earnings of pnl)",
            },
            {
                "budget_id": "bud_vander_stokken_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_vander_stokken_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE",
                "source_id": "src_vander_stokken_jr2025_cw_en",
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
                "title": "WZC H. Vander Stokken Pepingen YE2025 leftover dual (omzet JUMP 8.87m / equity JUMP +72.71pct)",
                "entity_id": ENTITY,
                "beneficiary": "Pepingen elderly residents (WZC Henri Vander Stokken ~127 beds + Residentie Paloken AW)",
                "legal_basis": f"VZW WZC / publiek erkende zorg (Departement Zorg) (KBO {KBO})",
                "decision_date": "2026-07-02",
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
                "stated_goal": "WZC residential elderly care Pepingen (~127 beds) + adjacent assistentiewoningen",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain equity JUMP +72.71pct vs near-flat omzet",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pepingen>Vander_Stokken>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; Den Akker YE2025 deferred; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "WZC H. Vander Stokken Pepingen omzet JUMP 8.87m / equity JUMP +72.71pct (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pepingen>Vander_Stokken>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; equity JUMP ~equals retained YE2025 pnl",
                "confidence": "medium",
                "source_id": "src_vander_stokken_jr2025_cw_en",
                "beneficiaries": "WZC clients Pepingen (~127 beds) + Residentie Paloken",
                "stated_goal": "Residential elderly care Pajottenland / Pepingen",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": "5.0",
                "cost_score": "4.8",
                "difficulty": "4.0",
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; reconcile equity JUMP EUR1.50m→2.59m with pnl EUR1.09m and near-flat omzet; map IFIC/Alivia vs dagprijs",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; VZW Pepingen",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "WoonZorgcentrum H. Vander Stokken (Pepingen)",
                "name_fr": "Maison de repos H. Vander Stokken (Pepingen)",
                "name_en": "WZC H. Vander Stokken (Pepingen)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m (+72.71pct) "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "~127 beds + Residentie Paloken AW; tel 02 363 06 30"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pepingen>Vander_Stokken>NBB_PDF_assets_debt_equity_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    "explanation of equity JUMP from EUR1502322 (YE2024) to EUR2594672 (YE2025, +72.71pct) with near-flat omzet (+1.25pct) and FTE DROP 98.9→97.7"
                ),
                "why_it_matters": (
                    "Medium CW shows 8.87m omzet erkende WZC VZW with large equity JUMP without balanstotaal/assets/debt; "
                    "material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "WoonZorgcentrum H. Vander Stokken vzw",
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
                "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2080",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — WZC H. Vander Stokken Pepingen (NBB PDF / assets-debt / equity-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WoonZorgcentrum H. Vander Stokken VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Palokenstraat 17 Pepingen; NACE 87.101; email {EMAIL} (site); tel 02 363 06 30.
- Site: WZC Henri Vander Stokken (~127 beds) + Residentie Paloken assistentiewoningen.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Den Akker YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WoonZorgcentrum H. Vander Stokken vzw — Palokenstraat 17, 1670 Pepingen
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC H. Vander Stokken + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek erkende WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de stijging van het eigen vermogen van EUR{EQUITY24} (YE2024) naar EUR{EQUITY} (YE2025, {EQUITY_YOY}) bij vrijwel vlakke omzet ({OMZET_YOY}) en lichte FTE-daling van {FTE24} naar {FTE} ({FTE_YOY}).
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

## Tick {TICK} - {UTC} - rq_2079 WZC H. Vander Stokken Pepingen (omzet JUMP 8.87m / equity JUMP +72.71pct / Medium)

- Unit: **rq_2079** leftover dual after **rq_2078 Ten Anker** (already on main; this fire found rq_2078 done). Prefer NON-stall live: AGB Bornem still **JR2024-only** (CW 404); FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **WZC H. Vander Stokken** YE2025 (KBO **{KBO}**; Palokenstraat 17 Pepingen; Vlaams-Brabant **VZW** WZC / **1 VE**; ~127 beds + Residentie Paloken). Den Akker YE2025 also live - deferred. Do not redo Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2079=done + rq_2080 open (EVERY-10); loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2079/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2080 THIS next tick**). Next: rq_2080 (EVERY-10 mandatory + AGB/FARO-if-YE2025 / AIESH-REW / Den-Akker deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "equity", EQUITY, "bruto", BRUTO, "fte", FTE)


if __name__ == "__main__":
    main()
