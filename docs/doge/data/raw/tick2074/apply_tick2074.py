# tick 2074 — rq_2074 Heilig Hart Grimbergen YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-24T23:35:00Z"
TICK = 2074
ENTITY = "vzw_wzc_heilig_hart_grimbergen"
GAP = "gap_hh_grimbergen_nbb_pdf_assets_debt_pnl_near_zero_matrix_l5"
LB = "lb_hh_grimbergen_omzet_jump_10_61m_pnl_drop_near_zero_jr2025"
COMM = "comm_hh_grimbergen_jr2025_statutory_wzc"

OMZET = 10609510
PNL = 4035
EQUITY = 5749528
BRUTO = 10285059
FTE = 128.6
OMZET_YOY = "+3.69%"
PNL_YOY = "-98.38%"
EQUITY_YOY = "-1.38%"
BRUTO_YOY = "-2.5%"
FILED = "26.05.2026"
KBO = "0409.724.238"
EMAIL = "info@hhg.be"
ADDR = "Veldkantstraat 30, 1850 Grimbergen"
SITE = "https://www.hhg.be"
CW_NL = "https://www.companyweb.be/nl/0409724238/woon-en-zorgcentrum-heilig-hart-te-grimbergen"
CW_EN = "https://www.companyweb.be/en/0409724238/woon-en-zorgcentrum-heilig-hart-te-grimbergen"
CW_FR = "https://www.companyweb.be/fr/0409724238/woon-en-zorgcentrum-heilig-hart-te-grimbergen"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409724238"


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
        if r["task_id"] == "rq_2074":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Heilig Hart Grimbergen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Heilig Hart Grimbergen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} "
                f"bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} HH Grimbergen Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl DROP near-zero {PNL} equity DROP {EQUITY/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m; "
                "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2075; next every-10 2080"
            )
    if not any(r["task_id"] == "rq_2075" for r in rows):
        rows.append(
            {
                "task_id": "rq_2075",
                "title": "leftover dual hole-fill after HH Grimbergen — prefer AGB/FARO-YE2025/AIESH-REW/ZorgWelzijn-Kuurne-SintJozef-Brugge",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2074 after Heilig Hart Grimbergen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Zorg en Welzijn Kuurne 0412.703.029 YE2025 "
                    "(note: prior note flagged private — verify public subsidy / aanbestedende overheid before L5) / "
                    "Sint-Jozef Brugge Sint-Michiels 0461.563.315 YE2025 live unused / unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    "Do NOT redo Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
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
                    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2074 HH Grimbergen; next every-10 2080",
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
                "last_unit_id": "rq_2074",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover HH Grimbergen 0409.724.238 Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl DROP near-zero {PNL} equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2075; next every-10 2080; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_hh_grimbergen_jr2025_cw",
                "title": "Companyweb NL — Heilig Hart Grimbergen YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL}",
            },
            {
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "title": "Companyweb EN — Heilig Hart Grimbergen YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_hh_grimbergen_jr2025_cw_fr",
                "title": "Companyweb FR — Heilig Hart Grimbergen YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-24",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_hh_grimbergen_kbo_{TICK}",
                "title": "KBO — Heilig Hart Grimbergen 0409.724.238",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-24",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW aanbestedende overheid 1 VE; NACE 87.101",
            },
            {
                "source_id": f"src_hh_grimbergen_site_{TICK}",
                "title": "Heilig Hart Grimbergen website contact",
                "url": SITE,
                "publisher": "WZC Heilig Hart Grimbergen vzw",
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
                "budget_id": "bud_hh_grimbergen_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 10232240",
            },
            {
                "budget_id": "bud_hh_grimbergen_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {PNL_YOY} vs YE2024 248847",
            },
            {
                "budget_id": "bud_hh_grimbergen_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {EQUITY_YOY} vs YE2024 5829820",
            },
            {
                "budget_id": "bud_hh_grimbergen_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {BRUTO_YOY} vs YE2024 10549092",
            },
            {
                "budget_id": "bud_hh_grimbergen_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
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
                "title": "Heilig Hart Grimbergen YE2025 leftover dual (omzet JUMP 10.61m / pnl DROP near-zero 4k)",
                "entity_id": ENTITY,
                "beneficiary": "Grimbergen elderly residents (WZC Heilig Hart)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO})",
                "decision_date": "2026-05-26",
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
                "stated_goal": "WZC residential elderly care Grimbergen (160 places incl KV)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -98pct to near-zero vs omzet +3.7pct",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Grimbergen>Heilig_Hart>JR2025_statutory_L5",
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
                "name": "Heilig Hart Grimbergen omzet JUMP 10.61m / pnl DROP near-zero 4k (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Grimbergen>Heilig_Hart>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_hh_grimbergen_jr2025_cw_en",
                "beneficiaries": "WZC/KV clients Grimbergen (~160 places)",
                "stated_goal": "Residential elderly care Grimbergen",
                "measured_outcome": f"omzet JUMP {OMZET_YOY}; pnl DROP {PNL_YOY} to EUR{PNL}; equity DROP {EQUITY_YOY}; FTE {FTE}",
                "absurdity_score": "5.8",
                "cost_score": "5.1",
                "difficulty": "4.0",
                "priority_index": "5.5",
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP -98pct to near-zero vs modest omzet growth; map IFIC/Alivia vs dagprijs split",
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
                "name_nl": "Woon- en Zorgcentrum Heilig Hart te Grimbergen vzw",
                "name_fr": "Maison de repos et de soins Heilig Hart à Grimbergen ASBL",
                "name_en": "Heilig Hart residential care centre VZW (Grimbergen)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende overheid 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl DROP near-zero {PNL} equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Grimbergen>Heilig_Hart>NBB_PDF_assets_debt_pnl_near_zero",
                "entity_id": ENTITY,
                "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -98.38pct from EUR248847 to near-zero EUR4035 with omzet +3.69pct",
                "why_it_matters": "Medium CW shows 10.61m omzet WZC VZW with near-wipe of profit without balanstotaal/assets/debt; material L5 residual for FOI",
                "priority": "8",
                "recipient_body": "WZC Heilig Hart te Grimbergen vzw",
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
        f"""# FOI draft — Heilig Hart Grimbergen (NBB PDF / assets-debt / pnl-near-zero)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC Heilig Hart te Grimbergen VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** DROP {PNL_YOY} vs YE2024 EUR248847; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}**; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **1 VE**; zetel Veldkantstraat 30 Grimbergen; NACE 87.101; site {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentrum Heilig Hart te Grimbergen vzw — Veldkantstraat 30, 1850 Grimbergen
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Heilig Hart Grimbergen + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling winst van EUR248.847 (YE2024) naar EUR{PNL} (YE2025; {PNL_YOY}) bij omzetgroei van {OMZET_YOY}.
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

## Tick {TICK} - {UTC} - rq_2074 Heilig Hart Grimbergen (omzet JUMP 10.61m / pnl DROP near-zero 4k / Medium)

- Unit: **rq_2074** leftover dual after **rq_2073 Mater Amabilis**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **Heilig Hart Grimbergen** YE2025 (KBO **{KBO}**; Veldkantstraat 30 Grimbergen; Vlaams-Brabant **aanbestedende-overheid VZW** WZC / **1 VE**). Zorg en Welzijn Kuurne / Sint-Jozef Brugge Sint-Michiels YE2025 also live - deferred. Do not redo Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **EUR{PNL}** DROP {PNL_YOY} vs YE2024 EUR248847; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}**; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.5); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2074=done + rq_2075 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2074/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2075 (AGB/FARO-if-YE2025 / AIESH-REW / ZorgWelzijn-Kuurne-SintJozef-Brugge deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
