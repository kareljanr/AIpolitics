# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T17:40:00Z"
TICK = 2143
RQ = "rq_2143"
NEXT_RQ = "rq_2144"
ENTITY = "bv_seniors_care_ion_anderlecht"
GAP = "gap_care_ion_nbb_pdf_assets_debt_equity_collapse_pnl_loss_matrix_l5"
COMM = "comm_care_ion_jr2025_statutory_mrs_equity_collapse"
LB = "lb_care_ion_omzet_86_0m_equity_drop_79pct_pnl_loss_jr2025"
SRC_EN = "src_care_ion_jr2025_cw_en"
KBO = "0422.923.859"
KBO_DIGITS = "0422923859"
OMZET = "85993318"
OMZET_PRIOR = "84465840"
OMZET_YOY = "+1.81%"
BRUTO = "54607136"
BRUTO_PRIOR = "53541480"
BRUTO_YOY = "+1.99%"
PNL = "-5073803"
PNL_PRIOR = "-6794354"
PNL_YOY = "LOSS_NARROW_+25.32%"
EQUITY = "1290120"
EQUITY_PRIOR = "6363923"
EQUITY_YOY = "-79.73%"
FTE = "873.8"
FTE_PRIOR = "924.9"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI_DIR = ROOT / "foi" / "drafts"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = (
                "leftover dual — Seniors Care-Ion Anderlecht YE2025 Medium "
                "(omzet JUMP 86.0m / equity DROP -79.7% / pnl LOSS narrow)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Care-Ion Medium omzet JUMP 86.0m bruto JUMP 54.6m "
                f"pnl LOSS NARROW -5.07m equity DROP 1.29m (-79.73%) FTE DROP 873.8; "
                f"KBO Actief BV 19 VE NACE ROB/MRS Anderlecht; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover Seniors Care-Ion YE2025 Medium CW after Groep Sint-Franciscus; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS {PNL} equity DROP {EQUITY} FTE {FTE}; FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Seniors Care-Ion — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Seniors Care-Ion YE2025 Medium "
                    "(omzet JUMP 86.0m / equity DROP -79.7% / pnl LOSS narrow). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Seniors Care-Ion / Care-Ion Group, Groep Sint-Franciscus Brakel / Groep van Voorzieningen Sint-Franciscus, "
                    "Denderrust Dienstengroep, Zorgcampus Denderrust Aalst, Maison De Repos En Famille Vaux, Residence Prestige Chaudfontaine, "
                    "Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, MRS Comte d'Egmont, C.I.G.B. Menen, "
                    "Maagd Der Armen / Ten Rozen, L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus Roosdaal, Zorghome De Fakkel, "
                    "Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, "
                    "Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, "
                    "Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde Olen, Sint-Camillus, IDELUX*, INTRADEL, "
                    "Korian*, Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding, Prinsenhof, Akapella, Familiehof, "
                    "La Moisson (absorbed), Zusterhof Geel, Den Akker, Mater Dei, Vander Stokken, Huize Sion, "
                    "Zorggroep Zusters van Berlaar, WZC Veilige Have, WZC Christine, WZC Zilverbos."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Seniors Care-Ion; "
                    "FARO/AIESH/REW still YE2024; next every-10 2150"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_care_ion_jr2025_cw",
        "title": "Companyweb NL Seniors Care-Ion YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/seniors-care-ion",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS NARROW {PNL} (vs YE2024 {PNL_PRIOR}) equity DROP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 11.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2143/careion_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Seniors Care-Ion YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/seniors-care-ion",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 11-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes; raw docs/doge/data/raw/tick2143/careion_cw_en.html"
        ),
    },
    {
        "source_id": "src_care_ion_jr2025_cw_fr",
        "title": "Companyweb FR Seniors Care-Ion YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/seniors-care-ion",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2143/careion_cw_fr.html",
    },
    {
        "source_id": f"src_care_ion_kbo_{TICK}",
        "title": f"KBO Seniors Care-Ion {KBO} Actief Anderlecht BV 19 VE",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; BV SENIORS CARE-ION; Ninoofse Steenweg 534 1070 Anderlecht; "
            "19 VE; NACE 87.301 ROB / 87.101 MRS; sinds 22.06.1982; absorbed Senior's Flatel 0441.944.668 + Residence Brunehault 0480.156.730"
        ),
    },
    {
        "source_id": f"src_care_ion_site_{TICK}",
        "title": "Care-Ion Group site FOI info@care-ion.be",
        "url": "https://www.careion.be/",
        "publisher": "Care-Ion Group / Seniors Care-Ion BV",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Ninoofsesteenweg 534 1070 Anderlecht; FOI info@care-ion.be; "
            "multi-site WZC/MRS network VL+BRU+WAL"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Seniors Care-Ion (Anderlecht multi-site WZC/MRS BV)",
        "name_fr": "Seniors Care-Ion (Anderlecht multi-site MRS/MRPA SRL)",
        "name_en": "Seniors Care-Ion (Anderlecht multi-site nursing homes)",
        "level": "other",
        "parent_id": "brussels_gov",
        "community_language": "bi",
        "website": "https://www.careion.be/",
        "foi_email": "info@care-ion.be",
        "foi_postal": "Ninoofse Steenweg 534, 1070 Anderlecht",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV; "
            f"omzet JUMP 86.0m ({OMZET_YOY}) bruto JUMP 54.6m ({BRUTO_YOY}) pnl LOSS NARROW -5.07m "
            f"(vs -6.79m) equity DROP 1.29m ({EQUITY_YOY}) FTE DROP {FTE} (vs {FTE_PRIOR}); "
            f"assets/debt Unknown; filed 11.07.2026; 19 VE; FOI {GAP}; preferred AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; DISTINCT Care-Support Houthalen 0827.850.260 / emeis / Armonea holdings"
        ),
    },
)

for bid, amt, basis in [
    ("bud_care_ion_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_care_ion_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_care_ion_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss LOSS NARROW"),
    ("bud_care_ion_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity DROP -79.73%"),
    ("bud_care_ion_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
]:
    append_csv(
        DATA / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2143; Medium CW; assets/debt Unknown pending NBB PDF; private BV multi-site MRS",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Seniors Care-Ion YE2025 leftover dual (omzet JUMP 86.0m / equity DROP -79.7%)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "MRS/WZC residents Care-Ion network (BRU/VL/WAL multi-site)",
        "legal_basis": (
            f"BV/SRL multi-site MRS/ROB (KBO {KBO}; Actief; 19 VE; NACE 87.301/87.101)"
        ),
        "decision_date": "2026-07-11",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"2024_fte":{FTE_PRIOR},"ve":19}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/seniors-care-ion",
        "stated_goal": "Residential care / MRS-ROB for elderly (multi-site BE)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose INAMI/Iriscare/VL subsidy vs resident-fee split; "
            "explain equity DROP -79.73% path while LOSS narrows; publish 19 VE site matrix"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Belgium>Brussels>Anderlecht>SeniorsCareIon>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Care-Support Houthalen / emeis / Armonea holdings"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Seniors Care-Ion omzet JUMP 86.0m / equity DROP -79.7% / pnl LOSS -5.07m (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_bv",
        "hierarchy_path": "Belgium>Brussels>Anderlecht>SeniorsCareIon>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} LOSS NARROW vs YE2024 {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY}; "
            f"FTE {FTE} DROP vs {FTE_PRIOR}; assets/debt Unknown pending NBB PDF; 19 VE multi-site"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS/WZC residents Care-Ion multi-site network",
        "stated_goal": "Residential care / MRS-ROB for elderly",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl LOSS NARROW +25.32%; "
            f"equity DROP {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "7.2",
        "cost_score": "7.8",
        "difficulty": "3.5",
        "priority_index": "7.6",
        "cut_proposal": (
            "FOI NBB PDF + INAMI/Iriscare/VL split + equity-collapse path + 19 VE site matrix"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Care-Support Houthalen / emeis / Armonea holdings"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Belgium>Brussels>Anderlecht>SeniorsCareIon>NBB_PDF_assets_debt_equity_collapse_pnl_loss"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); equity DROP -79.73% path "
            "(1.29m vs 6.36m) while pnl LOSS NARROW -5.07m vs omzet JUMP 86.0m; "
            "INAMI/Iriscare/VL care vs resident fee split vs bruto 54.6m; 19 VE site matrix; FTE DROP path"
        ),
        "why_it_matters": (
            "Medium CW shows private multi-site MRS operator with ~86m omzet and equity collapse "
            "to 1.29m while still LOSS — public-care opacity across 19 VE if INAMI/Iriscare/VL flows"
        ),
        "priority": "8",
        "recipient_body": "Seniors Care-Ion BV / Care-Ion Group",
        "recipient_email": "info@care-ion.be",
        "recipient_postal": "Ninoofse Steenweg 534, 1070 Anderlecht",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2150",
    },
)

with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
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
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover Seniors Care-Ion {KBO} Medium CW (omzet JUMP 86.0m bruto JUMP 54.6m "
                f"pnl LOSS NARROW -5.07m equity DROP 1.29m (-79.73%) FTE DROP 873.8; Actief BV 19 VE Anderlecht; "
                f"assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                "next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

FOI_DIR.mkdir(parents=True, exist_ok=True)
(FOI_DIR / f"{GAP}.md").write_text(
    f"""# FOI draft — Seniors Care-Ion (NBB PDF / assets-debt / equity collapse / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Seniors Care-Ion BV — KBO **{KBO}** (Actief; Ninoofse Steenweg 534, 1070 Anderlecht; 19 VE; NACE ROB/MRS)  
**recipient:** info@care-ion.be · Ninoofse Steenweg 534, 1070 Anderlecht · cc Iriscare / Departement Zorg / AVIQ  
**sources:** [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/seniors-care-ion) · [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/seniors-care-ion) · [CW FR](https://www.companyweb.be/fr/{KBO_DIGITS}/seniors-care-ion) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}) · [site](https://www.careion.be/)  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR YE2025; assets/debt Unknown; KBO Strong; private BV)

## Context
- YE **2025** (filed **11.07.2026**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** LOSS NARROW vs YE2024 EUR{PNL_PRIOR} (+25.32%); equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** DROP vs {FTE_PRIOR}; assets/debt **Unknown**.
- KBO: Actief; BV sinds 30.12.2019 (entiteit sinds 22.06.1982); Ninoofse Steenweg 534 Anderlecht; **19 VE**; NACE 87.301 ROB / 87.101 MRS; absorbed Senior's Flatel + Residence Brunehault.
- DISTINCT from Care-Support Houthalen **0827.850.260**, emeis Belgium **0887.690.451**, Armonea holding, Groep Sint-Franciscus. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Seniors Care-Ion BV / Care-Ion Group
via info@care-ion.be
cc: Iriscare / Departement Zorg / AVIQ (openbaarheid waar van toepassing)
Betreft: Openbaarmaking jaarrekening NBB 2025 Seniors Care-Ion (KBO {KBO})

Geachte,

Op grond van toepasselijke openbaarheidsregels (en, waar van toepassing, regels
rond publieke zorgfinanciering) vraag ik openbaarmaking van:

1. PDF NBB jaarrekening 2025 (neerlegging 11.07.2026) + neerleggingsreferentie.
2. Activa / schulden LT-KT / liquide middelen / balanstotaal.
3. Toelichting equity DROP EUR{EQUITY} (−79.73% vs YE2024 EUR{EQUITY_PRIOR})
   terwijl omzet JUMP tot EUR{OMZET} (+1.81%) en pnl LOSS NARROW EUR{PNL}
   (vs YE2024 EUR{PNL_PRIOR}).
4. Split INAMI/Iriscare/Vlaamse zorgsubsidies vs resident fees; FTE-pad ({FTE} vs {FTE_PRIOR}).
5. Site-matrix omzet/kosten over 19 VE (Care-Ion netwerk BRU/VL/WAL).

Periode boekjaar 2025. Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Seniors Care-Ion Anderlecht (omzet JUMP 86.0m / equity DROP -79.7% / pnl LOSS -5.07m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2142 Groep Sint-Franciscus Brakel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Seniors Care-Ion BV** YE2025 (KBO **{KBO}**; Ninoofse Steenweg 534 Anderlecht; **BV/SRL** NACE **87.301/87.101** / **19 VE**; Care-Ion multi-site MRS/WZC). Do not redo Groep Sint-Franciscus/Denderrust/En Famille/Prestige/Corolles/Esplanade/Peupliers/Comte d'Egmont/CIGB/Ten Rozen/Care-Support/emeis holding/Armonea holding.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** LOSS NARROW +25.32% vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **11.07.2026**. KBO Strong Actief BV 19 VE. Assets/debt Unknown. Medium. FOI via info@care-ion.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 7.6); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2143/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, "next", NEXT_RQ)
