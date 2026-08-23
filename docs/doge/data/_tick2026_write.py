# ephemeral tick2026 — WZC Zilverbos Zelzate YE2025 Medium
import csv
import shutil
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T11:10:00Z"
ENTITY = "vzw_wzc_zilverbos_zelzate"
GAP = "gap_wzc_zilverbos_zelzate_nbb_pdf_assets_debt_pnl_recovery_matrix_l5"
SRC = "src_wzc_zilverbos_zelzate_jr2025_cw"
SRC_EN = "src_wzc_zilverbos_zelzate_jr2025_cw_en"
SRC_FR = "src_wzc_zilverbos_zelzate_jr2025_cw_fr"
SRC_KBO = "src_wzc_zilverbos_zelzate_kbo_2026"
SRC_SITE = "src_wzc_zilverbos_zelzate_site_2026"

OMZET = "7846856"
PNL = "113577"
EQUITY = "6050428"
BRUTO = "7364283"
FTE = "101.4"
OMZET24 = "7660297"
PNL24 = "-732476"
EQUITY24 = "6211024"
BRUTO24 = "6785295"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# ensure site copy
raw = Path("docs/doge/data/raw/tick2026")
raw.mkdir(parents=True, exist_ok=True)
src_site = Path("docs/doge/data/raw/tick2025/zilverbos_site.html")
if src_site.exists() and not (raw / "zilverbos_site.html").exists():
    shutil.copy(src_site, raw / "zilverbos_site.html")

qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2026")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Zilverbos Zelzate YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0644984078/woonzorgcentrum-zilverbos",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2026; YE2025 omzet JUMP {OMZET} pnl RECOVERY {PNL} (vs YE2024 LOSS {PNL24}) equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 11.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2026/zilverbos_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Zilverbos Zelzate YE2025 statutory",
        "url": "https://www.companyweb.be/en/0644984078/woonzorgcentrum-zilverbos",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2026; EN mirror YE2025 Medium; filed 11-07-2026; Last balance sheet year 2025; FTE 101.4; raw docs/doge/data/raw/tick2026/zilverbos_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Zilverbos Zelzate YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0644984078/woonzorgcentrum-zilverbos",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2026; FR mirror YE2025 Medium; déposés le 11-07-2026; raw docs/doge/data/raw/tick2026/zilverbos_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum Zilverbos 0644.984.078 Actief VZW Zelzate",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0644984078",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2026; Actief VZW since 18.12.2015; Bloemenboslaan 30 9060 Zelzate; 1 VE; Zorggroep Agapè path; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzczilverbos.be WZC Zilverbos Zelzate",
        "url": "https://www.wzczilverbos.be/",
        "publisher": "WZC Zilverbos / Zorggroep Agapè",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2026; info@wzczilverbos.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_zilverbos_zelzate_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2026; omzet JUMP {OMZET} +2.44pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_zilverbos_zelzate_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2026; pnl RECOVERY {PNL} from YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_wzc_zilverbos_zelzate_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2026; equity DROP {EQUITY} -2.59pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_zilverbos_zelzate_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2026; bruto JUMP {BRUTO} +8.53pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_zilverbos_zelzate_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2026; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_zilverbos_zelzate_jr2025_statutory_wzc",
    "title": "WZC Zilverbos Zelzate YE2025 leftover dual (omzet JUMP 7.85m / pnl RECOVERY 0.11m / equity DROP 6.05m)",
    "entity_id": ENTITY,
    "beneficiary": "Zelzate elderly care residents / WZC Zilverbos / Zorggroep Agapè",
    "legal_basis": "VZW/ASBL WZC (KBO 0644.984.078)",
    "decision_date": "2026-07-11",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0644984078/woonzorgcentrum-zilverbos",
    "stated_goal": "Residential elderly care (Zelzate)",
    "cut_option": "Publish NBB PDF assets/debt FOI; Agapè group map",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>WZC_Zilverbos_Zelzate>JR2025_statutory_L5",
    "notes": "tick2026; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint Carolus Mayerhof already mined; Sint-Carolus Ternat deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 4.275
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_zilverbos_zelzate_omzet_jump_7_85m_pnl_recovery_0_11m_jr2025",
    "name": "WZC Zilverbos Zelzate omzet JUMP 7.85m / pnl RECOVERY 0.11m (from YE2024 LOSS) / equity DROP 6.05m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "OostVlaanderen>WZC_Zilverbos_Zelzate>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl RECOVERY {PNL} (vs LOSS {PNL24}) equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Zelzate elderly via WZC Zilverbos / Agapè",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.85m omzet JUMP +2.44pct with pnl recovery from YE2024 LOSS; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.275",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map Agapè group + public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2026 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Zilverbos (Zelzate)",
    "name_fr": "Maison de repos Zilverbos (Zelzate)",
    "name_en": "WZC Zilverbos Zelzate (elderly care)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.wzczilverbos.be/",
    "foi_email": "info@wzczilverbos.be",
    "foi_postal": "Bloemenboslaan 30, 9060 Zelzate",
    "notes": "tick2026 YE2025 Medium CW NL+EN+FR + Strong KBO 0644.984.078 Actief VZW; omzet JUMP 7.85m pnl RECOVERY 0.11m (from YE2024 LOSS) equity DROP 6.05m bruto JUMP 7.36m FTE 101.4; assets/debt Unknown; neerlegging 11.07.2026; 1 VE; Zorggroep Agapè; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Carolus Ternat deferred; do not redo Sint Carolus Mayerhof/Evara/Multiversum/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "OostVlaanderen>WZC_Zilverbos_Zelzate>NBB_PDF_assets_debt_pnl_recovery",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); Agapè group map; public subsidy vs resident-fee split; pnl recovery path",
    "why_it_matters": "Medium CW shows 7.85m omzet Zelzate WZC VZW without balance sheet or Agapè/subsidy transparency",
    "priority": "6",
    "recipient_body": "Woonzorgcentrum Zilverbos vzw",
    "recipient_email": "info@wzczilverbos.be",
    "recipient_postal": "Bloemenboslaan 30, 9060 Zelzate",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_zilverbos_zelzate_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_zilverbos_zelzate_omzet_jump_7_85m_pnl_recovery_0_11m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2026; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Zilverbos Zelzate (NBB PDF / assets-debt / pnl recovery)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Zilverbos vzw — KBO **0644.984.078**  
**recipient:** info@wzczilverbos.be · Bloemenboslaan 30, 9060 Zelzate  
**sources:** [CW NL](https://www.companyweb.be/nl/0644984078/woonzorgcentrum-zilverbos) · [CW EN](https://www.companyweb.be/en/0644984078/woonzorgcentrum-zilverbos) · [CW FR](https://www.companyweb.be/fr/0644984078/woonzorgcentrum-zilverbos) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0644984078) · [site](https://www.wzczilverbos.be/)  
**tick:** 2026  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **11.07.2026**): omzet **EUR7,846,856** JUMP +2.44%; pnl **EUR113,577** RECOVERY from YE2024 LOSS EUR−732,476; equity **EUR6,050,428** DROP −2.59%; bruto **EUR7,364,283** JUMP +8.53%; FTE **101.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Sint Carolus Mayerhof already mined. Sint-Carolus Ternat deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Zilverbos vzw — Bloemenboslaan 30, 9060 Zelzate
info@wzczilverbos.be
cc: Zorggroep Agapè / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Zilverbos + balans (KBO 0644.984.078)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 11.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Relatie Zorggroep Agapè + toelichting pnl-herstel vs YE2024 verlies.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2026":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Sint Carolus Mayerhof — WZC Zilverbos Zelzate YE2025 Medium"
        x["notes"] = (
            "tick2026 WZC Zilverbos Zelzate Medium omzet JUMP 7.85m pnl RECOVERY 0.11m equity DROP 6.05m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Carolus Ternat deferred; next rq_2027; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover WZC Zilverbos Zelzate YE2025 Medium CW; KBO 0644.984.078; "
            f"omzet JUMP {OMZET} pnl RECOVERY {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2027" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2027",
            "title": "leftover dual hole-fill after WZC Zilverbos Zelzate",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2026 after WZC Zilverbos Zelzate YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Sint-Carolus Ternat KBO 0409.970.203 YE2025 live deferred / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2026 WZC Zilverbos Zelzate; next every-10 2030; Sint-Carolus Ternat YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2026",
        "ticks_completed": "2026",
        "paused": "no",
        "notes": (
            "tick2026 leftover WZC Zilverbos Zelzate 0644.984.078 Medium CW (omzet JUMP 7.85m pnl RECOVERY 0.11m equity DROP 6.05m bruto JUMP 7.36m FTE 101.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Carolus Ternat deferred; next rq_2027; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2026 - {UTC} - rq_2026 WZC Zilverbos Zelzate (omzet JUMP 7.85m / pnl RECOVERY 0.11m / Medium)

- Unit: **rq_2026** leftover dual after **rq_2025 Sint Carolus Mayerhof**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **WZC Zilverbos Zelzate** YE2025 (KBO **0644.984.078**; Bloemenboslaan 30 Zelzate; Oost-Vlaanderen **WZC VZW** / Zorggroep Agapè). Sint-Carolus Ternat YE2025 also live — deferred. Do not redo Sint Carolus Mayerhof/Evara/Multiversum/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,846,856** JUMP +2.44%; pnl **EUR113,577** RECOVERY from YE2024 LOSS EUR−732,476; equity **EUR6,050,428** DROP −2.59%; bruto **EUR7,364,283** JUMP +8.53%; FTE **101.4**; neerlegging **11.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@wzczilverbos.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_zilverbos_zelzate); foi + draft {GAP}; rq_2026=done + rq_2027 open; loop_state ticks=2026; raw under docs/doge/data/raw/tick2026/.
- FOI: **ready not sent** (human-gated; info@wzczilverbos.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2027 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Carolus Ternat / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
