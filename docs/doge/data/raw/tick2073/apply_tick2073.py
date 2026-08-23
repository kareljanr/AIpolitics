# tick 2073 — rq_2073 Mater Amabilis Wervik YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-24T23:20:00Z"
TICK = 2073
ENTITY = "vzw_mater_amabilis_wervik"
GAP = "gap_mater_amabilis_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
LB = "lb_mater_amabilis_omzet_jump_7_97m_pnl_drop_jr2025"
COMM = "comm_mater_amabilis_jr2025_statutory_wzc"

OMZET = 7965730
PNL = 211456
EQUITY = 9654142
BRUTO = 8333283
FTE = 100.1
OMZET_YOY = "+3.85%"
PNL_YOY = "-60.48%"
EQUITY_YOY = "+1.12%"
BRUTO_YOY = "+2.66%"
FILED = "25.06.2026"
KBO = "0417.430.293"
EMAIL = "info@mater-amabilis.be"
ADDR = "Sint Jorisstraat 3, 8940 Wervik"
SITE = "http://www.mater-amabilis.be"
CW_NL = "https://www.companyweb.be/nl/0417430293/mater-amabilis-woon-en-zorgcentrum"
CW_EN = "https://www.companyweb.be/en/0417430293/mater-amabilis-woon-en-zorgcentrum"
CW_FR = "https://www.companyweb.be/fr/0417430293/mater-amabilis-woon-en-zorgcentrum"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417430293"


def append_csv(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        existing = list(reader)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
        for r in rows:
            out = {k: r.get(k, "") for k in fieldnames}
            w.writerow(out)


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2073":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Mater Amabilis Wervik YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Mater Amabilis Wervik YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}; "
                "HH Grimbergen deferred; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Mater Amabilis Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m; "
                "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2074; next every-10 2080"
            )
    # spawn rq_2074
    if not any(r["task_id"] == "rq_2074" for r in rows):
        rows.append(
            {
                "task_id": "rq_2074",
                "title": "leftover dual hole-fill after Mater Amabilis — prefer AGB/FARO-YE2025/AIESH-REW/HH-Grimbergen",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2073 after Mater Amabilis Wervik YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heilig Hart Grimbergen 0409.724.238 YE2025 live unused / "
                    "unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    "Do NOT redo Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
                    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
                    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
                    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
                    "Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
                    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
                    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
                    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
                    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
                    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
                    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
                    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
                    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear. "
                    "Leftover Heilig Hart Grimbergen 0409.724.238 YE2025 live unused."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2073 Mater Amabilis; next every-10 2080",
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
                "last_unit_id": "rq_2073",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Mater Amabilis 0417.430.293 Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2074; next every-10 2080; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_mater_amabilis_jr2025_cw",
                "title": "Companyweb NL — Mater Amabilis Wervik YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL}",
            },
            {
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "title": "Companyweb EN — Mater Amabilis Wervik YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_mater_amabilis_jr2025_cw_fr",
                "title": "Companyweb FR — Mater Amabilis Wervik YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_mater_amabilis_kbo_{TICK}",
                "title": "KBO — Mater Amabilis Wervik 0417.430.293",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-24",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende overheid 1 VE; NACE 87.301",
            },
            {
                "source_id": f"src_mater_amabilis_site_{TICK}",
                "title": "Mater Amabilis Wervik website contact",
                "url": SITE,
                "publisher": "Mater Amabilis vzw",
                "accessed_date": "2026-08-24",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_mater_amabilis_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 7670723",
            },
            {
                "budget_id": "bud_mater_amabilis_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {PNL_YOY} vs YE2024 535103",
            },
            {
                "budget_id": "bud_mater_amabilis_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 9547675",
            },
            {
                "budget_id": "bud_mater_amabilis_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 8117773",
            },
            {
                "budget_id": "bud_mater_amabilis_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Mater Amabilis Wervik YE2025 leftover dual (omzet JUMP 7.97m / pnl DROP 0.21m)",
                "entity_id": ENTITY,
                "beneficiary": "Wervik elderly residents (Mater Amabilis WZC)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO})",
                "decision_date": "2026-06-25",
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
                "stated_goal": "WZC residential elderly care Wervik + CDV/LDC/AW",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -60pct vs omzet +3.9pct",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wervik>Mater_Amabilis>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; HH Grimbergen deferred; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Mater Amabilis Wervik omzet JUMP 7.97m / pnl DROP 0.21m (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wervik>Mater_Amabilis>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_mater_amabilis_jr2025_cw_en",
                "beneficiaries": "WZC/CDV/LDC/AW clients Wervik",
                "stated_goal": "Residential elderly care + community services",
                "measured_outcome": f"omzet JUMP {OMZET_YOY}; pnl DROP {PNL_YOY}; equity JUMP {EQUITY_YOY}; FTE {FTE}",
                "absurdity_score": "5.0",
                "cost_score": "4.7",
                "difficulty": "4.0",
                "priority_index": "5.1",
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP -60pct vs modest omzet growth; map IFIC/Alivia vs dagprijs split",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "vzw MATER AMABILIS woon- en zorgcentrum (Wervik)",
                "name_fr": "ASBL MATER AMABILIS woon- en zorgcentrum (Wervik)",
                "name_en": "Mater Amabilis residential care centre VZW (Wervik)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende overheid 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; HH Grimbergen deferred"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wervik>Mater_Amabilis>NBB_PDF_assets_debt_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -60.48pct with omzet +3.85pct",
                "why_it_matters": "Medium CW shows 7.97m omzet WZC VZW with sharp pnl DROP without balanstotaal/assets/debt; material L5 residual for FOI",
                "priority": "8",
                "recipient_body": "Mater Amabilis vzw",
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
        f"""# FOI draft — Mater Amabilis Wervik (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Mater Amabilis VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET:,}** JUMP {OMZET_YOY}; pnl **EUR{PNL:,}** DROP {PNL_YOY} vs YE2024 EUR535,103; equity **EUR{EQUITY:,}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO:,}** JUMP {BRUTO_YOY}; FTE **{FTE}**; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **1 VE**; zetel Sint Jorisstraat 3 Wervik; NACE 87.301; site {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. HH Grimbergen deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Mater Amabilis vzw — Sint Jorisstraat 3, 8940 Wervik
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Mater Amabilis Wervik + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling winst van EUR535.103 (YE2024) naar EUR{PNL:,} (YE2025; {PNL_YOY}) bij omzetgroei van {OMZET_YOY}.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""".replace(",", "XCOMMA")
        .replace("XCOMMA", ",")  # keep thousands separators from f-string
        ,
        encoding="utf-8",
    )
    # fix accidental double-replace no-op; rewrite cleanly without euro thousands commas issues
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Mater Amabilis Wervik (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Mater Amabilis VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** DROP {PNL_YOY} vs YE2024 EUR535103; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}**; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **1 VE**; zetel Sint Jorisstraat 3 Wervik; NACE 87.301; site {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. HH Grimbergen deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Mater Amabilis vzw — Sint Jorisstraat 3, 8940 Wervik
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Mater Amabilis Wervik + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling winst van EUR535.103 (YE2024) naar EUR{PNL} (YE2025; {PNL_YOY}) bij omzetgroei van {OMZET_YOY}.
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

## Tick {TICK} - {UTC} - rq_2073 Mater Amabilis (omzet JUMP 7.97m / pnl DROP 0.21m / Medium)

- Unit: **rq_2073** leftover dual after **rq_2072 Maria Moorslede**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred leftover **Mater Amabilis Wervik** YE2025 (KBO **{KBO}**; Sint Jorisstraat 3 Wervik; West-Vlaanderen **aanbestedende-overheid VZW** WZC / **1 VE**). Heilig Hart Grimbergen YE2025 also live - deferred. Do not redo Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** DROP {PNL_YOY} vs YE2024 EUR535103; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}**; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.1); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2073=done + rq_2074 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2073/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2074 (AGB/FARO-if-YE2025 / AIESH-REW / HH-Grimbergen deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
