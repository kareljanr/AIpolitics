# ephemeral tick2021 — WZC Sint-Vincentius Avelgem YE2025 Medium (leftover after PC Sint-Hiëronymus EVERY-10)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T10:05:00Z"
ENTITY = "vzw_wzc_sint_vincentius_avelgem"
GAP = "gap_wzc_sint_vincentius_avelgem_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_wzc_sint_vincentius_avelgem_jr2025_cw"
SRC_EN = "src_wzc_sint_vincentius_avelgem_jr2025_cw_en"
SRC_FR = "src_wzc_sint_vincentius_avelgem_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_vincentius_avelgem_kbo_2021"
SRC_SITE = "src_wzc_sint_vincentius_avelgem_site_2021"

OMZET = "7493161"
PNL = "74613"
EQUITY = "7303884"
BRUTO = "8116678"
FTE = "103.3"
OMZET24 = "7321405"
PNL24 = "88563"
EQUITY24 = "7421209"
BRUTO24 = "7938462"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2021")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2021; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2021/sint_vincentius_avelgem.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2021; EN mirror YE2025 Medium; filed 10-06-2026; Last balance sheet year 2025; FTE 103.3; raw docs/doge/data/raw/tick2021/sint_vincentius_avelgem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2021; FR mirror YE2025 Medium; déposés le 10-06-2026; raw docs/doge/data/raw/tick2021/sint_vincentius_avelgem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woon- en Zorgcentrum Sint-Vincentius 0420.504.403 Actief VZW Avelgem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420504403",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2021; Actief VZW since 29.01.1980; Bevrijdingslaan 18 8580 Avelgem; 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "vincentiusavelgem.be WZC Sint-Vincentius Avelgem",
        "url": "https://www.vincentiusavelgem.be/",
        "publisher": "WZC Sint-Vincentius Avelgem",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2021; info@vincentiusavelgem.be; Bevrijdingslaan 18 8580 Avelgem",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2021; omzet JUMP {OMZET} +2.35pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2021; pnl DROP {PNL} -15.75pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2021; equity DROP {EQUITY} -1.58pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2021; bruto JUMP {BRUTO} +2.24pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2021; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_vincentius_avelgem_jr2025_statutory_wzc",
    "title": "WZC Sint-Vincentius Avelgem YE2025 leftover dual (omzet JUMP 7.49m / pnl DROP 75k / equity DROP 7.30m)",
    "entity_id": ENTITY,
    "beneficiary": "Avelgem elderly care residents / WZC Sint-Vincentius",
    "legal_basis": "VZW/ASBL WZC (KBO 0420.504.403)",
    "decision_date": "2026-06-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius",
    "stated_goal": "Residential elderly care (Avelgem)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>JR2025_statutory_L5",
    "notes": "tick2021; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024; St Vincentius Antwerpen YE2024-only; Maria Ingelmunster YE2025 deferred; PC Sint-Hiëronymus already mined EVERY-10",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 4.275
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_vincentius_avelgem_omzet_jump_7_49m_pnl_drop_75k_jr2025",
    "name": "WZC Sint-Vincentius Avelgem omzet JUMP 7.49m / pnl DROP 75k / equity DROP 7.30m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Avelgem elderly via WZC Sint-Vincentius VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.49m omzet JUMP +2.35pct with pnl DROP -15.75pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.275",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2021 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon- en Zorgcentrum Sint-Vincentius (Avelgem)",
    "name_fr": "Maison de repos Sint-Vincentius (Avelgem)",
    "name_en": "WZC Sint-Vincentius Avelgem (elderly care)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.vincentiusavelgem.be/",
    "foi_email": "info@vincentiusavelgem.be",
    "foi_postal": "Bevrijdingslaan 18, 8580 Avelgem",
    "notes": "tick2021 YE2025 Medium CW NL+EN+FR + Strong KBO 0420.504.403 Actief VZW; omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m bruto JUMP 8.12m FTE 103.3; assets/debt Unknown; neerlegging 10.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024; St Vincentius Antwerpen YE2024-only; Maria Ingelmunster YE2025 deferred; do not redo PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS",
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
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split",
    "why_it_matters": "Medium CW shows 7.49m omzet Avelgem WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "Woon- en Zorgcentrum Sint-Vincentius vzw",
    "recipient_email": "info@vincentiusavelgem.be",
    "recipient_postal": "Bevrijdingslaan 18, 8580 Avelgem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_vincentius_avelgem_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_sint_vincentius_avelgem_omzet_jump_7_49m_pnl_drop_75k_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2021; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Vincentius Avelgem (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en Zorgcentrum Sint-Vincentius vzw — KBO **0420.504.403**  
**recipient:** info@vincentiusavelgem.be · Bevrijdingslaan 18, 8580 Avelgem  
**sources:** [CW NL](https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius) · [CW EN](https://www.companyweb.be/en/0420504403/woon-en-zorgcentrum-sint-vincentius) · [CW FR](https://www.companyweb.be/fr/0420504403/woon-en-zorgcentrum-sint-vincentius) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420504403) · [site](https://www.vincentiusavelgem.be/)  
**tick:** 2021  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.06.2026**): omzet **EUR7,493,161** JUMP +2.35%; pnl **EUR74,613** DROP −15.75%; equity **EUR7,303,884** DROP −1.58%; bruto **EUR8,116,678** JUMP +2.24%; FTE **103.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024. St Vincentius Antwerpen YE2024-only. Maria Rustoord Ingelmunster YE2025 deferred. PC Sint-Hiëronymus already mined EVERY-10.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentrum Sint-Vincentius vzw — Bevrijdingslaan 18, 8580 Avelgem
info@vincentiusavelgem.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Vincentius Avelgem + balans (KBO 0420.504.403)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2021":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after PC Sint-Hiëronymus — WZC Sint-Vincentius Avelgem YE2025 Medium"
        x["notes"] = (
            "tick2021 WZC Sint-Vincentius Avelgem Medium omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; next rq_2022; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover WZC Sint-Vincentius Avelgem YE2025 Medium CW; KBO 0420.504.403; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2022" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2022",
            "title": "leftover dual hole-fill after WZC Sint-Vincentius Avelgem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2021 after WZC Sint-Vincentius Avelgem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Maria Rustoord Ingelmunster YE2025 live deferred / PPC Pittem / Multiversum-Evara if not double-count / Sint-Carolus / Zilverbos / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count. St Vincentius Antwerpen still YE2024-only."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2021 WZC Sint-Vincentius Avelgem; next every-10 2030; Maria Ingelmunster YE2025 deferred",
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
        "last_unit_id": "rq_2021",
        "ticks_completed": "2021",
        "paused": "no",
        "notes": (
            "tick2021 leftover WZC Sint-Vincentius Avelgem 0420.504.403 Medium CW (omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m bruto JUMP 8.12m FTE 103.3; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; next rq_2022; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2021 - {UTC} - rq_2021 WZC Sint-Vincentius Avelgem (omzet JUMP 7.49m / pnl DROP 75k / Medium)

- Unit: **rq_2021** leftover dual after **rq_2020 EVERY-10 + PC Sint-Hiëronymus**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO NBB YE2025 still **unpublished**; AIESH/REW still **YE2024**. St Vincentius Antwerpen still **YE2024-only**. Took unused leftover **WZC Sint-Vincentius Avelgem** YE2025 (KBO **0420.504.403**; Bevrijdingslaan 18 Avelgem; West-Vlaanderen **WZC VZW**). Maria Rustoord Ingelmunster YE2025 also live — deferred. Do not redo PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,493,161** JUMP +2.35%; pnl **EUR74,613** DROP −15.75%; equity **EUR7,303,884** DROP −1.58%; bruto **EUR8,116,678** JUMP +2.24%; FTE **103.3**; neerlegging **10.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@vincentiusavelgem.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_vincentius_avelgem); foi + draft {GAP}; rq_2021=done + rq_2022 open; loop_state ticks=2021; raw under docs/doge/data/raw/tick2021/.
- FOI: **ready not sent** (human-gated; info@vincentiusavelgem.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2022 (AGB/FARO-if-YE2025 / AIESH-REW / Maria Ingelmunster-PPC Pittem / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
