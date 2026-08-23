# tick 2091 — rq_2091 Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T03:50:00Z"
TICK = 2091
ENTITY = "vzw_sint_elisabeths_dal_zoutleeuw"
GAP = "gap_sed_zoutleeuw_nbb_pdf_assets_debt_pnl_flip_loss_equity_drop_matrix_l5"
LB = "lb_sed_zoutleeuw_omzet_jump_16_36m_pnl_flip_loss_jr2025"
COMM = "comm_sed_zoutleeuw_jr2025_statutory_wzc"

OMZET = 16361513
PNL = -238101
EQUITY = 8763808
BRUTO = 16337809
FTE = 212.1
OMZET24 = 15938721
PNL24 = 225456
EQUITY24 = 9390058
BRUTO24 = 16511285
OMZET_YOY = "+2.65%"
PNL_YOY = "FLIP LOSS"
EQUITY_YOY = "DROP -6.63%"
BRUTO_YOY = "DROP -1.05%"
FTE_YOY = "Unknown"
FILED = "23.06.2026"
KBO = "0413.653.827"
EMAIL = "info.zl@vzwsed.be"
ADDR = "Stationsstraat 36, 3440 Zoutleeuw"
SITE = "https://st-elisabethsdal.be/"
CW_NL = "https://www.companyweb.be/nl/0413653827/sint-elisabeth-s-dal"
CW_EN = "https://www.companyweb.be/en/0413653827/sint-elisabeth-s-dal"
CW_FR = "https://www.companyweb.be/fr/0413653827/sint-elisabeth-s-dal"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413653827"
PI = "5.4"
ABSURD = "5.2"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Sint-Elisabeth's Dal Zoutleeuw, Familiezorg West-Vlaanderen, CZD Zilvervogel Lo-Reninge, "
    "De Lovie Poperinge, VZW Woonzorgcentra Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, "
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
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, "
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
        if r["task_id"] == "rq_2091":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2091 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto DROP {BRUTO} pnl FLIP LOSS {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.101 RVT 3 VE"
            )
            r["notes"] = (
                f"tick{TICK} SED Medium omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2092; next every-10 2100"
            )
    if not any(r["task_id"] == "rq_2092" for r in rows):
        rows.append(
            {
                "task_id": "rq_2092",
                "title": "leftover dual hole-fill after SED Zoutleeuw — prefer AGB/FARO-YE2025/AIESH-REW/unused",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2092 after Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    "STRONG deferred live unused: Lidwina Mol 0407.601.720 YE2025; Sint-Lucia Turnhout 0410.151.137 YE2025. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2091 SED Zoutleeuw; next every-10 2100",
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
                "last_unit_id": "rq_2091",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Sint-Elisabeth's Dal Zoutleeuw {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m "
                    f"equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; NACE 87.101 3 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2092; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_sed_zoutleeuw_jr2025_cw",
                "title": "Companyweb NL — Sint-Elisabeth's Dal Zoutleeuw YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "title": "Companyweb EN — Sint-Elisabeth's Dal Zoutleeuw YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_sed_zoutleeuw_jr2025_cw_fr",
                "title": "Companyweb FR — Sint-Elisabeth's Dal Zoutleeuw YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_sed_zoutleeuw_kbo_{TICK}",
                "title": "KBO — Sint-Elisabeth's Dal 0413.653.827",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW aanbestedende 3 VE; NACE 87.101 RVT; "
                    f"zetel Stationsstraat 36 Zoutleeuw; {EMAIL}"
                ),
            },
            {
                "source_id": f"src_sed_zoutleeuw_site_{TICK}",
                "title": "Sint-Elisabeth's Dal website (3 WZC campuses)",
                "url": SITE,
                "publisher": "Sint-Elisabeth's Dal",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; OLV Lourdes Zoutleeuw / Sint-Jozef Nieuwerkerken / Betze Rust Geetbets; "
                    f"{EMAIL} / info.nk@vzwsed.be / info.gb@vzwsed.be"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_sed_zoutleeuw_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; bruto {BRUTO} near omzet",
            },
            {
                "budget_id": "bud_sed_zoutleeuw_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {BRUTO_YOY} vs YE2024 {BRUTO24}; primary operating-scale proxy",
            },
            {
                "budget_id": "bud_sed_zoutleeuw_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLIP LOSS vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_sed_zoutleeuw_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_sed_zoutleeuw_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE}; prior-year FTE Unknown on CW",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Sint-Elisabeth's Dal Zoutleeuw YE2025 leftover dual (omzet JUMP 16.36m / pnl FLIP LOSS)",
                "entity_id": ENTITY,
                "beneficiary": "WZC residents (OLV Lourdes Zoutleeuw / Sint-Jozef Nieuwerkerken / Betze Rust Geetbets)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg / aanbestedende overheid (KBO {KBO}; NACE 87.101)",
                "decision_date": "2026-06-23",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": "Multi-campus WZC care (Sint-Elisabeth's Dal / Zoutleeuw region)",
                "cut_option": "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS and equity DROP with omzet JUMP",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zoutleeuw>Sint_Elisabeths_Dal>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; dual city_zoutleeuw; "
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
                "name": "Sint-Elisabeth's Dal omzet JUMP 16.36m / pnl FLIP LOSS (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zoutleeuw>Sint_Elisabeths_Dal>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet/bruto proxy (~16.3m); assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_sed_zoutleeuw_jr2025_cw_en",
                "beneficiaries": "WZC residents Zoutleeuw/Nieuwerkerken/Geetbets (3 VE)",
                "stated_goal": "Multi-campus residential elderly care",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; bruto {BRUTO_YOY}; pnl FLIP LOSS vs YE2024 PROFIT {PNL24}; "
                    f"equity {EQUITY_YOY}; FTE {FTE} (YoY Unknown)"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; explain FLIP to LOSS EUR-238101 and equity DROP -6.63pct "
                    "while omzet JUMP +2.65pct across 3 WZC campuses"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                    "NACE 87.101 aanbestedende 3 VE; not OLV Lourdes Kortenberg"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Sint-Elisabeth's Dal vzw (Zoutleeuw)",
                "name_fr": "Sint-Elisabeth's Dal ASBL (Zoutleeuw)",
                "name_en": "Sint-Elisabeth's Dal VZW (Zoutleeuw)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende 3 VE; "
                    f"NACE 87.101 RVT; omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                    f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; "
                    f"neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Stationsstraat 36 Zoutleeuw; campuses OLV Lourdes / Sint-Jozef Nieuwerkerken / Betze Rust"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zoutleeuw>Sint_Elisabeths_Dal>NBB_PDF_assets_debt_pnl_flip_loss",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); split subsidies (code73/74 / Zorgkas / other) "
                    f"vs commercial omzet; explanation of pnl FLIP from PROFIT EUR{PNL24} to LOSS EUR{PNL} "
                    f"and equity DROP {EQUITY_YOY} with omzet JUMP {OMZET_YOY}; prior-year FTE"
                ),
                "why_it_matters": (
                    "Medium CW shows multi-campus WZC VZW with omzet 16.36m flipping to LOSS and equity DROP "
                    "without balanstotaal/assets/debt; material L5 residual for FOI; dual city_zoutleeuw"
                ),
                "priority": "8",
                "recipient_body": "Sint-Elisabeth's Dal vzw",
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
        f"""# FOI draft — Sint-Elisabeth's Dal Zoutleeuw (NBB PDF / assets-debt / pnl-flip-loss / equity-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sint-Elisabeth's Dal VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** (prior-year FTE Unknown on CW); assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **3 VE**; NACE **87.101** (RVT); zetel Stationsstraat 36 Zoutleeuw; email {EMAIL} (also info.nk@vzwsed.be / info.gb@vzwsed.be).
- Campuses: OLV Lourdes Zoutleeuw / Sint-Jozef Nieuwerkerken / Betze Rust Geetbets (not WZC OLV Lourdes Kortenberg).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Sint-Elisabeth's Dal vzw — Stationsstraat 36, 3440 Zoutleeuw
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint-Elisabeth's Dal + balans/resultaatmatrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde zorg / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (Zorgkas/IFIC/andere code73/74) vs omzet/eigen bijdragen 2025 (omzet EUR{OMZET} / bruto EUR{BRUTO}).
4. Toelichting van de winstflip van PROFIT EUR{PNL24} (YE2024) naar LOSS EUR{PNL} (YE2025) bij equity-daling {EQUITY_YOY} en omzet-stijging {OMZET_YOY}; tevens FTE YE2024.
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

### {UTC} — tick {TICK}
- Unit: **rq_2091** leftover dual after **rq_2090 Familiezorg WV / EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused WZC **Sint-Elisabeth's Dal** YE2025 (KBO **{KBO}**; Stationsstraat 36 Zoutleeuw; Vlaams-Brabant **aanbestedende-overheid VZW** NACE **87.101** / **3 VE**; campuses OLV Lourdes / Sint-Jozef Nieuwerkerken / Betze Rust). Deferred live unused Lidwina Mol / Sint-Lucia Turnhout. Do not redo Familiezorg WV/Zilvervogel/De Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/…/AGB Bornem/Armonea/Always Home/Solidum.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** (YoY Unknown); neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 3 VE NACE 87.101; email {EMAIL}; site {SITE}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} omzet proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2091=done + rq_2092 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2091/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2092 (AGB/FARO-if-YE2025 / AIESH-REW / Lidwina / Sint-Lucia / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()
