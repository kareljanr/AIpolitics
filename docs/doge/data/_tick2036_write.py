# ephemeral tick2036 — OLVA Antwerpen YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T13:40:00Z"
ENTITY = "vzw_wzc_olva_antwerpen"
GAP = "gap_wzc_olva_antwerpen_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_wzc_olva_antwerpen_jr2025_cw"
SRC_EN = "src_wzc_olva_antwerpen_jr2025_cw_en"
SRC_FR = "src_wzc_olva_antwerpen_jr2025_cw_fr"
SRC_KBO = "src_wzc_olva_antwerpen_kbo_2036"
SRC_SITE = "src_wzc_olva_antwerpen_site_2036"

OMZET = "10810892"
PNL = "76807"
EQUITY = "13738639"
BRUTO = "11254590"
FTE = "143.4"
OMZET24 = "11017242"
PNL24 = "853286"
EQUITY24 = "14063307"
BRUTO24 = "11536044"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2036")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL OLVA Antwerpen YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2036; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 19.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2036/olva_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN OLVA Antwerpen YE2025 statutory",
        "url": "https://www.companyweb.be/en/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2036; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; FTE 143.4; raw docs/doge/data/raw/tick2036/olva_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR OLVA Antwerpen YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2036; FR mirror YE2025 Medium; déposés le 19-06-2026; raw docs/doge/data/raw/tick2036/olva_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO OLVA 0430.977.136 Actief VZW Antwerpen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430977136",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2036; Actief VZW; Pieter van Hobokenstraat 3 2000 Antwerpen; 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "olvantwerpen.be WZC OLVA Antwerpen",
        "url": "https://www.olvantwerpen.be/",
        "publisher": "WZC OLVA",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2036; info@olvantwerpen.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_olva_antwerpen_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2036; omzet DROP {OMZET} -1.87pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_olva_antwerpen_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2036; pnl DROP {PNL} -91.00pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_olva_antwerpen_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2036; equity DROP {EQUITY} -2.31pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_olva_antwerpen_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2036; bruto DROP {BRUTO} -2.44pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_olva_antwerpen_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2036; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_olva_antwerpen_jr2025_statutory_wzc",
    "title": "OLVA Antwerpen YE2025 leftover dual (omzet DROP 10.81m / pnl DROP 77k / equity DROP 13.74m)",
    "entity_id": ENTITY,
    "beneficiary": "Antwerpen city elderly care residents / WZC OLVA",
    "legal_basis": "VZW/ASBL WZC (KBO 0430.977.136)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen",
    "stated_goal": "Residential elderly care (Antwerpen)",
    "cut_option": "Publish NBB PDF assets/debt FOI; scrutinise pnl DROP -91pct",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>WZC_OLVA>JR2025_statutory_L5",
    "notes": "tick2036; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Roosdaal already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.5 + 0.10*(10-4) = 5.55 (pnl collapse bump)
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_olva_antwerpen_omzet_drop_10_81m_pnl_drop_77k_jr2025",
    "name": "OLVA Antwerpen omzet DROP 10.81m / pnl DROP 77k (-91pct) / equity DROP 13.74m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "Antwerpen>WZC_OLVA>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet DROP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Antwerpen elderly via WZC OLVA VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 10.81m omzet DROP -1.87pct with pnl DROP -91.00pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.55",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; scrutinise pnl DROP path + subsidy vs fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2036 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon- en zorgcentrum Onze-Lieve-Vrouw van Antwerpen (OLVA)",
    "name_fr": "Maison de repos Notre-Dame d'Anvers (OLVA)",
    "name_en": "WZC OLVA Antwerpen (elderly care)",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.olvantwerpen.be/",
    "foi_email": "info@olvantwerpen.be",
    "foi_postal": "Pieter van Hobokenstraat 3, 2000 Antwerpen",
    "notes": "tick2036 YE2025 Medium CW NL+EN+FR + Strong KBO 0430.977.136 Actief VZW; omzet DROP 10.81m pnl DROP 77k equity DROP 13.74m bruto DROP 11.25m FTE 143.4; assets/debt Unknown; neerlegging 19.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo OLV Roosdaal/Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "Antwerpen>WZC_OLVA>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl DROP -91pct recon",
    "why_it_matters": "Medium CW shows 10.81m omzet Antwerpen WZC VZW with pnl DROP -91pct without balance sheet",
    "priority": "7",
    "recipient_body": "Woon- en zorgcentrum Onze-Lieve-Vrouw van Antwerpen (OLVA) vzw",
    "recipient_email": "info@olvantwerpen.be",
    "recipient_postal": "Pieter van Hobokenstraat 3, 2000 Antwerpen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_olva_antwerpen_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_olva_antwerpen_omzet_drop_10_81m_pnl_drop_77k_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2036; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — OLVA Antwerpen (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en zorgcentrum Onze-Lieve-Vrouw van Antwerpen (OLVA) vzw — KBO **0430.977.136**  
**recipient:** info@olvantwerpen.be · Pieter van Hobokenstraat 3, 2000 Antwerpen  
**sources:** [CW NL](https://www.companyweb.be/nl/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen) · [CW EN](https://www.companyweb.be/en/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen) · [CW FR](https://www.companyweb.be/fr/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430977136) · [site](https://www.olvantwerpen.be/)  
**tick:** 2036  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **19.06.2026**): omzet **EUR10,810,892** DROP −1.87%; pnl **EUR76,807** DROP −91.00%; equity **EUR13,738,639** DROP −2.31%; bruto **EUR11,254,590** DROP −2.44%; FTE **143.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. OLV Roosdaal already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en zorgcentrum Onze-Lieve-Vrouw van Antwerpen (OLVA) vzw — Pieter van Hobokenstraat 3, 2000 Antwerpen
info@olvantwerpen.be
cc: Agentschap Zorg en Gezondheid / Stad Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 OLVA Antwerpen + balans (KBO 0430.977.136)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 19.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl DROP (−91,00pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2036":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC OLV Roosdaal — OLVA Antwerpen YE2025 Medium"
        x["notes"] = (
            "tick2036 OLVA Antwerpen Medium omzet DROP 10.81m pnl DROP 77k (-91pct) equity DROP 13.74m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2037; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover OLVA Antwerpen YE2025 Medium CW; KBO 0430.977.136; "
            f"omzet DROP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2037" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2037",
            "title": "leftover dual hole-fill after OLVA Antwerpen",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2036 after OLVA Antwerpen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Kanunnik Triest YE2025 live deferred / other unused YE2025 if live with omzet). "
                "Do NOT redo OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2036 OLVA Antwerpen; next every-10 2040; Kanunnik Triest YE2025 deferred",
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
        "last_unit_id": "rq_2036",
        "ticks_completed": "2036",
        "paused": "no",
        "notes": (
            "tick2036 leftover OLVA Antwerpen 0430.977.136 Medium CW (omzet DROP 10.81m pnl DROP 77k -91pct equity DROP 13.74m bruto DROP 11.25m FTE 143.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2037; next every-10 2040; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2036 - {UTC} - rq_2036 OLVA Antwerpen (omzet DROP 10.81m / pnl DROP 77k / Medium)

- Unit: **rq_2036** leftover dual after **rq_2035 WZC OLV Roosdaal**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **OLVA Antwerpen** YE2025 (KBO **0430.977.136**; Pieter van Hobokenstraat 3 Antwerpen; **WZC VZW**). Do not redo OLV Roosdaal/Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR10,810,892** DROP −1.87%; pnl **EUR76,807** DROP −91.00%; equity **EUR13,738,639** DROP −2.31%; bruto **EUR11,254,590** DROP −2.44%; FTE **143.4**; neerlegging **19.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@olvantwerpen.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_olva_antwerpen); foi + draft {GAP}; rq_2036=done + rq_2037 open; loop_state ticks=2036; raw under docs/doge/data/raw/tick2036/.
- FOI: **ready not sent** (human-gated; info@olvantwerpen.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2037 (AGB/FARO-if-YE2025 / AIESH-REW / Kanunnik Triest / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
