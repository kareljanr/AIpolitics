# tick 2096 — rq_2096 emeis Belgium YE2025 Medium CW
# (rq_2095 concurrent Begralim; this tick takes unused emeis on 2096)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW = DATA / "raw" / "tick2095"
RAW2096 = DATA / "raw" / "tick2096"

csv.field_size_limit(10**7)
UTC = "2026-08-25T05:05:00Z"
TICK = 2096
ENTITY = "nv_emeis_belgium"
GAP = "gap_emeis_belgium_nbb_pdf_assets_debt_pnl_loss_narrow_equity_neg_matrix_l5"
LB = "lb_emeis_belgium_omzet_jump_19_63m_pnl_loss_narrow_jr2025"
COMM = "comm_emeis_belgium_jr2025_statutory_wzc"

OMZET = 19633819
PNL = -89076155
EQUITY = -360390406
BRUTO = 8255042
FTE = 70.8
OMZET24 = 15826396
PNL24 = -147828527
EQUITY24 = -471314251
BRUTO24 = 1847037
OMZET_YOY = "+24.06%"
PNL_YOY = "LOSS NARROW +39.74%"
EQUITY_YOY = "NEG NARROW +23.54%"
BRUTO_YOY = "JUMP +346.93%"
FTE_YOY = "Unknown"
FILED = "08.07.2026"
KBO = "0887.690.451"
EMAIL = ""  # no public email; FOI via contact form + 0800 88 888
PHONE = "0800 88 888"
ADDR = "Alsembergsesteenweg 1037, 1180 Ukkel"
SITE = "https://www.emeis.be/"
CW_NL = "https://www.companyweb.be/nl/0887690451/emeis-belgium"
CW_EN = "https://www.companyweb.be/en/0887690451/emeis-belgium"
CW_FR = "https://www.companyweb.be/fr/0887690451/emeis-belgium"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0887690451"
PI = "5.6"
ABSURD = "6.2"
COST = "5.5"
DIFF = "4.5"

DO_NOT_REDO = (
    "Do NOT redo emeis Belgium, Begralim / Grauwzusters Limburg, Sint-Lucia Turnhout, Lidwina Mol, "
    "Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, De Lovie Poperinge, "
    "Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
    "Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, "
    "Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, "
    "VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, "
    "Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, "
    "Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, SLG Operaties Vlaanderen, "
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
    found = False
    for r in rows:
        if r["task_id"] == "rq_2096":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2096 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — emeis Belgium YE2025 Medium"
            r["instructions"] = (
                "Completed leftover emeis Belgium YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS NARROW {PNL} equity NEG NARROW {EQUITY} "
                f"FTE {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.301 ROB 2 VE; "
                "DISTINCT from Always Home/Armonea/SLG Operaties"
            )
            r["notes"] = (
                f"tick{TICK} emeis Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl LOSS NARROW {PNL/1e6:.2f}m equity NEG NARROW {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2097; next every-10 2100"
            )
            found = True
    if not found:
        raise SystemExit("rq_2096 missing")
    if not any(r["task_id"] == "rq_2097" for r in rows):
        rows.append(
            {
                "task_id": "rq_2097",
                "title": "leftover dual hole-fill after emeis — prefer AGB/FARO-YE2025/AIESH-REW/unused",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2097 after emeis Belgium YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych. SLG Operaties Vlaanderen 0845.064.196 YE2025 live but Armonea/Always Home path "
                    "— take only if explicitly distinct unused. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2096 emeis; next every-10 2100; prefer FARO/AIESH/REW if YE2025",
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
                "last_unit_id": "rq_2096",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover emeis Belgium {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl LOSS NARROW {PNL/1e6:.2f}m "
                    f"equity NEG NARROW {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; NACE 87.301 2 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2097; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def copy_raw():
    RAW2096.mkdir(parents=True, exist_ok=True)
    for name in [
        "emeis_nl.html",
        "emeis_en.html",
        "emeis_fr.html",
        "emeis_kbo.html",
        "emeis_site.html",
        "emeis_contact.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "bornem_jr.html",
        "cand_0845064196_nl.html",
        "cand_0887690451_nl.html",
        "apply_tick2096.py",
    ]:
        src = RAW / name
        if src.exists():
            (RAW2096 / name).write_bytes(src.read_bytes())


def main():
    copy_raw()

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_emeis_belgium_jr2025_cw",
                "title": "Companyweb NL — emeis Belgium YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL}",
            },
            {
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "title": "Companyweb EN — emeis Belgium YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_emeis_belgium_jr2025_cw_fr",
                "title": "Companyweb FR — emeis Belgium YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_emeis_belgium_kbo_{TICK}",
                "title": "KBO — emeis Belgium 0887.690.451",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 2 VE; NACE 87.301 ROB + 64.210 holding; "
                    f"zetel Alsembergsesteenweg 1037 Ukkel; ex-Orpea path; contact form {SITE} / {PHONE}"
                ),
            },
            {
                "source_id": f"src_emeis_belgium_site_{TICK}",
                "title": "emeis Belgium website / contact",
                "url": SITE,
                "publisher": "emeis",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; no public email scraped; freephone {PHONE}; contact form",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_emeis_belgium_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}; primary scale proxy",
            },
            {
                "budget_id": "bud_emeis_belgium_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {BRUTO_YOY} vs YE2024 {BRUTO24}; bruto<<omzet commercial margin",
            },
            {
                "budget_id": "bud_emeis_belgium_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 LOSS {PNL24}",
            },
            {
                "budget_id": "bud_emeis_belgium_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {EQUITY_YOY} vs YE2024 {EQUITY24}; still deeply negative",
            },
            {
                "budget_id": "bud_emeis_belgium_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
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
                "title": "emeis Belgium YE2025 leftover dual (omzet JUMP 19.63m / pnl LOSS NARROW -89.1m)",
                "entity_id": ENTITY,
                "beneficiary": "WZC/ROB residents via emeis Belgium (ex-Orpea path)",
                "legal_basis": f"NV private care / publiek gesubsidieerde ROB (KBO {KBO}; NACE 87.301)",
                "decision_date": "2026-07-08",
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
                "stated_goal": "Private residential elderly care (emeis / ex-Orpea Belgium)",
                "cut_option": "Publish NBB PDF assets/debt FOI; explain persistent LOSS and negative equity vs public Zorgkas day-price path",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Belgie>Brussels>Ukkel>emeis_Belgium>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; DISTINCT Always Home/Armonea/SLG; "
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
                "name": "emeis Belgium omzet JUMP 19.63m / pnl LOSS NARROW -89.1m (YE2025)",
                "level": "L5",
                "type": "wzc_nv_statutory_private_care",
                "hierarchy_path": "Belgie>Brussels>Ukkel>emeis_Belgium>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy 19.63m; equity still -360m; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_emeis_belgium_jr2025_cw_en",
                "beneficiaries": "WZC/ROB residents (2 VE); public Zorgkas day-price path",
                "stated_goal": "Private residential elderly care (ex-Orpea)",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; bruto {BRUTO_YOY}; pnl {PNL_YOY} vs YE2024 LOSS {PNL24}; "
                    f"equity {EQUITY_YOY}; FTE {FTE} (YoY Unknown)"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; map public Zorgkas/IFIC subsidies vs private LOSS "
                    f"EUR{PNL} and equity EUR{EQUITY}; DISTINCT from Armonea/Always Home/SLG Operaties"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                    "NACE 87.301 NV 2 VE; ex-Orpea rebrand"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "emeis Belgium NV (Ukkel)",
                "name_fr": "emeis Belgium SA (Uccle)",
                "name_en": "emeis Belgium NV (Uccle)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV 2 VE; "
                    f"NACE 87.301 ROB (+64.210); omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl LOSS NARROW {PNL/1e6:.2f}m equity NEG NARROW {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; "
                    f"neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    f"Alsembergsesteenweg 1037 Ukkel; contact form {SITE} / {PHONE}; DISTINCT Armonea/Always Home/SLG"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Belgie>Brussels>Ukkel>emeis_Belgium>NBB_PDF_assets_debt_pnl_loss_narrow",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); split public Zorgkas/IFIC/other subsidies "
                    f"vs commercial omzet; explanation of persistent LOSS EUR{PNL} ({PNL_YOY} vs YE2024 {PNL24}) "
                    f"and equity EUR{EQUITY} ({EQUITY_YOY}); prior-year FTE; list of Belgian ROB campuses"
                ),
                "why_it_matters": (
                    "Medium CW shows ex-Orpea private care NV with omzet 19.63m still deeply loss-making and "
                    "equity -360m without balanstotaal; material L5 public-subsidy dual residual"
                ),
                "priority": "8",
                "recipient_body": "emeis Belgium NV",
                "recipient_email": EMAIL,
                "recipient_postal": f"{ADDR} (contact form {SITE}; freephone {PHONE})",
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
                "notes": f"tick{TICK}; human-send only; Medium CW; no public email — use form/{PHONE}; next every-10 2100",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — emeis Belgium (NBB PDF / assets-debt / pnl-loss-narrow / equity-neg)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** emeis Belgium NV — KBO **{KBO}**  
**recipient:** contact form {SITE} · freephone {PHONE} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; no public email scraped)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **LOSS EUR{PNL}** {PNL_YOY} vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** (prior-year FTE Unknown on CW); assets/debt **Unknown**.
- KBO: Actief NV; **2 VE**; NACE **87.301** (ROB) + **64.210** (holding); zetel Alsembergsesteenweg 1037 Ukkel; ex-Orpea rebrand.
- DISTINCT from Always Home / Armonea / SLG Operaties Vlaanderen.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: emeis Belgium NV — Alsembergsesteenweg 1037, 1180 Ukkel
via contactformulier {SITE} / {PHONE}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 emeis Belgium + balans/resultaatmatrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde ouderenzorg via Zorgkas-dagprijspad) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke middelen (Zorgkas/IFIC/andere code73/74) vs omzet/eigen bijdragen 2025 (omzet EUR{OMZET} / bruto EUR{BRUTO}).
4. Toelichting van het aanhoudende verlies LOSS EUR{PNL} (YE2025; {PNL_YOY} t.o.v. YE2024 LOSS EUR{PNL24}) en eigen vermogen EUR{EQUITY} ({EQUITY_YOY}); tevens FTE YE2024 en lijst Belgische ROB-campussen.
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
- Unit: **rq_2096** leftover dual after **rq_2095 Begralim** (concurrent closed Begralim on 2095). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **emeis Belgium** YE2025 (KBO **{KBO}**; Alsembergsesteenweg 1037 Ukkel; **NV** ROB NACE **87.301** / **2 VE**; ex-Orpea). SLG Operaties Vlaanderen YE2025 also live but Armonea/Always Home path — deferred. Do not redo Begralim/Sint-Lucia/Lidwina/SED/Zilvervogel/Familiezorg/…/Armonea/Always Home/SLG.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **LOSS EUR{PNL}** {PNL_YOY} vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** (YoY Unknown); neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 2 VE NACE 87.301; contact form {SITE} / {PHONE}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} omzet proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2096=done + rq_2097 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2096/ (+ tick2095 probes).
- FOI: **ready not sent** (human-gated; no public email — form/{PHONE}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2097 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, ENTITY, OMZET, PNL, FTE)


if __name__ == "__main__":
    main()
