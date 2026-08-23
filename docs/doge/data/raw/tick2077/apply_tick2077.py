# tick 2077 — rq_2077 De Zwaluw (Pajottegem) YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T00:20:00Z"
TICK = 2077
ENTITY = "nv_wzc_de_zwaluw_pajottegem"
GAP = "gap_de_zwaluw_nbb_pdf_assets_debt_pnl_flip_fte_drop_matrix_l5"
LB = "lb_de_zwaluw_omzet_drop_5_44m_pnl_flip_profit_fte_drop_jr2025"
COMM = "comm_de_zwaluw_jr2025_statutory_wzc"

OMZET = 5443008
PNL = 1429803
EQUITY = 9070655
BRUTO = 3910864
FTE = 69.0
OMZET24 = 5465878
PNL24 = -1064708
EQUITY24 = 7640852
BRUTO24 = 3937196
FTE24 = 80.5
OMZET_YOY = "-0.42%"
PNL_YOY = "FLIP to profit from LOSS"
EQUITY_YOY = "+18.71%"
BRUTO_YOY = "-0.67%"
FTE_YOY = "-14.29%"
FILED = "21.07.2026"
KBO = "0431.632.776"
EMAIL = "info.zwaluw@cura-care.be"
ADDR = "Vollezeelsesteenweg 44, 1570 Pajottegem"
SITE = "https://rvtdezwaluw.be/"
CW_NL = "https://www.companyweb.be/nl/0431632776/de-zwaluw"
CW_EN = "https://www.companyweb.be/en/0431632776/de-zwaluw"
CW_FR = "https://www.companyweb.be/fr/0431632776/de-zwaluw"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431632776"
PI = "5.1"

DO_NOT_REDO = (
    "Do NOT redo De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, "
    "Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, "
    "Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
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
        if r["task_id"] == "rq_2077":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2077 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — De Zwaluw Pajottegem YE2025 Medium"
            r["instructions"] = (
                "Completed leftover De Zwaluw Pajottegem YE2025 Medium CW; "
                f"KBO {KBO}; omzet DROP {OMZET} pnl FLIP PROFIT {PNL} equity JUMP {EQUITY} "
                f"bruto DROP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} De Zwaluw Medium omzet DROP {OMZET/1e6:.2f}m "
                f"pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2078; next every-10 2080"
            )
    if not any(r["task_id"] == "rq_2078" for r in rows):
        rows.append(
            {
                "task_id": "rq_2078",
                "title": "leftover dual hole-fill after De Zwaluw — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2077 after De Zwaluw Pajottegem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2077 De Zwaluw Pajottegem; next every-10 2080",
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
                "last_unit_id": "rq_2077",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover De Zwaluw Pajottegem {KBO} Medium CW "
                    f"(omzet DROP {OMZET/1e6:.2f}m pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2078; next every-10 2080; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_de_zwaluw_jr2025_cw",
                "title": "Companyweb NL — De Zwaluw Pajottegem YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "title": "Companyweb EN — De Zwaluw Pajottegem YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_de_zwaluw_jr2025_cw_fr",
                "title": "Companyweb FR — De Zwaluw Pajottegem YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_de_zwaluw_kbo_{TICK}",
                "title": "KBO — De Zwaluw 0431.632.776",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief NV 1 VE; NACE 87.101; {EMAIL}; CuraCare group",
            },
            {
                "source_id": f"src_de_zwaluw_site_{TICK}",
                "title": "RVT De Zwaluw website (Pajottegem / Vollezele)",
                "url": SITE,
                "publisher": "RVT De Zwaluw / CuraCare",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; ~88 beds; {EMAIL}; part of CuraCare",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_de_zwaluw_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_de_zwaluw_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLIP PROFIT vs YE2024 LOSS {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_de_zwaluw_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_de_zwaluw_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_de_zwaluw_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
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
                "title": "De Zwaluw Pajottegem YE2025 leftover dual (omzet DROP 5.44m / pnl FLIP PROFIT)",
                "entity_id": ENTITY,
                "beneficiary": "Pajottegem/Vollezele elderly residents (WZC/RVT De Zwaluw ~88 beds)",
                "legal_basis": f"NV WZC / publiek erkende zorg (Departement Zorg) (KBO {KBO})",
                "decision_date": "2026-07-21",
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
                "stated_goal": "WZC residential elderly care Vollezele/Pajottegem (~88 beds)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl FLIP + FTE DROP 80.5→69",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pajottegem>De_Zwaluw>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; CuraCare group NV; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "De Zwaluw Pajottegem omzet DROP 5.44m / pnl FLIP PROFIT + FTE DROP (YE2025)",
                "level": "L5",
                "type": "wzc_nv_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pajottegem>De_Zwaluw>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; pnl flip after multi-year losses with FTE DROP",
                "confidence": "medium",
                "source_id": "src_de_zwaluw_jr2025_cw_en",
                "beneficiaries": "WZC/RVT clients Vollezele/Pajottegem (~88 beds)",
                "stated_goal": "Residential elderly care Pajottenland",
                "measured_outcome": (
                    f"omzet DROP {OMZET_YOY}; pnl FLIP PROFIT vs YE2024 LOSS {PNL24}; equity JUMP {EQUITY_YOY}; "
                    f"bruto DROP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": "5.1",
                "cost_score": "4.8",
                "difficulty": "4.0",
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain flip from EUR-1.06m loss to EUR1.43m profit with FTE DROP 80.5→69 (-14.3pct); map IFIC/Alivia vs dagprijs",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; CuraCare NV",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "De Zwaluw nv (WZC Pajottegem)",
                "name_fr": "De Zwaluw SA (MRS Pajottegem)",
                "name_en": "De Zwaluw NV (WZC Pajottegem / Vollezele)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV 1 VE; "
                    f"omzet DROP {OMZET/1e6:.2f}m pnl FLIP PROFIT {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "CuraCare group; ~88 beds Vollezele/Pajottegem"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Pajottegem>De_Zwaluw>NBB_PDF_assets_debt_pnl_flip_fte_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    "explanation of pnl FLIP from LOSS EUR-1064708 (YE2024) to PROFIT EUR1429803 (YE2025) with FTE DROP 80.5→69 (-14.29pct) and near-flat omzet"
                ),
                "why_it_matters": (
                    "Medium CW shows 5.44m omzet erkende WZC NV with dramatic multi-year loss→profit flip and large FTE cut without balanstotaal/assets/debt; "
                    "material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "De Zwaluw nv (RVT De Zwaluw / CuraCare)",
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
        f"""# FOI draft — De Zwaluw Pajottegem (NBB PDF / assets-debt / pnl-flip / FTE-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Zwaluw NV — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** FLIP vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief NV; **1 VE**; zetel Vollezeelsesteenweg 44 Pajottegem; NACE 87.101; email {EMAIL}; tel +32 54 56 80 77; CuraCare group.
- Site: RVT De Zwaluw (~88 beds) Vollezele/Pajottegem.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Zwaluw nv — Vollezeelsesteenweg 44, 1570 Pajottegem
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 De Zwaluw + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek erkende WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de omslag van een verlies van EUR{PNL24} (YE2024) naar een winst van EUR{PNL} (YE2025) bij vrijwel vlakke omzet ({OMZET_YOY}) en FTE-daling van {FTE24} naar {FTE} ({FTE_YOY}).
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

## Tick {TICK} - {UTC} - rq_2077 De Zwaluw Pajottegem (omzet DROP 5.44m / pnl FLIP PROFIT 1.43m / Medium)

- Unit: **rq_2077** leftover dual after **rq_2076 Zorg en Welzijn Kuurne**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **De Zwaluw** YE2025 (KBO **{KBO}**; Vollezeelsesteenweg 44 Pajottegem; Vlaams-Brabant **NV** WZC/RVT / **1 VE**; ~88 beds; CuraCare). Do not redo Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/Groep Zorg H. Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** FLIP vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2077=done + rq_2078 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2077/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2078 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "bruto", BRUTO, "fte", FTE)


if __name__ == "__main__":
    main()
