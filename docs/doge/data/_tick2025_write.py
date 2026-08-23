# ephemeral tick2025 — Sint Carolus Mayerhof YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T11:00:00Z"
ENTITY = "vzw_sint_carolus_mayerhof"
GAP = "gap_sint_carolus_mayerhof_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_sint_carolus_mayerhof_jr2025_cw"
SRC_EN = "src_sint_carolus_mayerhof_jr2025_cw_en"
SRC_FR = "src_sint_carolus_mayerhof_jr2025_cw_fr"
SRC_KBO = "src_sint_carolus_mayerhof_kbo_2025"
SRC_SITE = "src_sint_carolus_mayerhof_site_2025"

OMZET = "11459875"
PNL = "144440"
EQUITY = "16112179"
BRUTO = "11780532"
FTE = "135.2"
OMZET24 = "11538135"
PNL24 = "931433"
EQUITY24 = "15967738"
BRUTO24 = "11819035"
FTE24 = "116.2"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2025")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Sint Carolus Mayerhof YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0407040308/sint-carolus-mayerhof",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2025; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE JUMP {FTE}; neerlegging 25.04.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2025/carolus_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Sint Carolus Mayerhof YE2025 statutory",
        "url": "https://www.companyweb.be/en/0407040308/sint-carolus-mayerhof",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2025; EN mirror YE2025 Medium; filed 25-04-2026; Last balance sheet year 2025; FTE 135.2; raw docs/doge/data/raw/tick2025/carolus_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Sint Carolus Mayerhof YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0407040308/sint-carolus-mayerhof",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2025; FR mirror YE2025 Medium; déposés le 25-04-2026; raw docs/doge/data/raw/tick2025/carolus_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Sint Carolus Mayerhof 0407.040.308 Actief VZW Mortsel",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407040308",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2025; Actief VZW; Fredericusstraat 89 2640 Mortsel; 1 VE; sinds 13.08.1922; raw docs/doge/data/raw/tick2025/kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "mayerhof.be Sint Carolus Mayerhof WZC Mortsel",
        "url": "https://www.mayerhof.be/",
        "publisher": "Sint Carolus Mayerhof",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2025; info@mayerhof.be; financieel mj.vaneyndhoven@mayerhof.be; directie jp.waterkeyn@mayerhof.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_sint_carolus_mayerhof_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2025; omzet DROP {OMZET} -0.68pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_sint_carolus_mayerhof_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2025; pnl DROP {PNL} -84.49pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_sint_carolus_mayerhof_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2025; equity JUMP {EQUITY} +0.90pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_sint_carolus_mayerhof_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2025; bruto DROP {BRUTO} -0.33pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_sint_carolus_mayerhof_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2025; YE2025 FTE JUMP {FTE} vs YE2024 {FTE24}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_sint_carolus_mayerhof_jr2025_statutory",
    "title": "Sint Carolus Mayerhof YE2025 leftover WZC dual (omzet DROP 11.46m / pnl DROP 0.14m / FTE JUMP 135.2)",
    "entity_id": ENTITY,
    "beneficiary": "Mortsel elderly residents via Sint Carolus Mayerhof VZW",
    "legal_basis": "VZW/ASBL woonzorgcentrum (KBO 0407.040.308)",
    "decision_date": "2026-04-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0407040308/sint-carolus-mayerhof",
    "stated_goal": "Residential elderly care / WZC Mortsel",
    "cut_option": "Publish NBB PDF assets/debt FOI; recon pnl DROP -84pct vs FTE JUMP",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>Mortsel>WZC_Sint_Carolus_Mayerhof>JR2025_statutory_L5",
    "notes": "tick2025; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zilverbos YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*6.0 + 0.35*5.0 + 0.10*(10-4) = 3.3 + 1.75 + 0.6 = 5.65
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_sint_carolus_mayerhof_omzet_drop_11_46m_pnl_drop_0_14m_fte_jump_jr2025",
    "name": "Sint Carolus Mayerhof omzet DROP 11.46m / pnl DROP 0.14m (-84pct) / FTE JUMP 135.2 (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "Antwerpen>Mortsel>WZC_Sint_Carolus_Mayerhof>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE JUMP {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Mortsel elderly via Sint Carolus Mayerhof VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 11.46m omzet DROP -0.68pct with pnl DROP -84.49pct and FTE JUMP 116.2->135.2; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.65",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP -84pct vs FTE JUMP and subsidy/fee mix",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2025 leftover WZC dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Sint Carolus Mayerhof (WZC Mortsel)",
    "name_fr": "Sint Carolus Mayerhof (maison de repos Mortsel)",
    "name_en": "Sint Carolus Mayerhof (nursing home Mortsel)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.mayerhof.be/",
    "foi_email": "info@mayerhof.be",
    "foi_postal": "Fredericusstraat 89, 2640 Mortsel",
    "notes": "tick2025 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.040.308 Actief VZW; omzet DROP 11.46m pnl DROP 0.14m (-84.49pct) equity JUMP 16.11m bruto DROP 11.78m FTE JUMP 135.2; assets/debt Unknown; neerlegging 25.04.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zilverbos YE2025 deferred; do not redo Evara/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "Antwerpen>Mortsel>WZC_Sint_Carolus_Mayerhof>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl DROP -84.49pct recon vs FTE JUMP 116.2->135.2",
    "why_it_matters": "Medium CW shows 11.46m omzet WZC with near-flat turnover but pnl collapse -84pct and FTE JUMP without balance sheet",
    "priority": "7",
    "recipient_body": "Sint Carolus Mayerhof VZW",
    "recipient_email": "info@mayerhof.be",
    "recipient_postal": "Fredericusstraat 89, 2640 Mortsel",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_sint_carolus_mayerhof_jr2025_statutory",
    "linked_leaderboard_id": "lb_sint_carolus_mayerhof_omzet_drop_11_46m_pnl_drop_0_14m_fte_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2025; human-send only; Medium CW; cc mj.vaneyndhoven@mayerhof.be; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Sint Carolus Mayerhof (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sint Carolus Mayerhof VZW — KBO **0407.040.308**  
**recipient:** info@mayerhof.be · Fredericusstraat 89, 2640 Mortsel  
**cc (optional):** mj.vaneyndhoven@mayerhof.be (financieel beheer) / jp.waterkeyn@mayerhof.be (directie)  
**sources:** [CW NL](https://www.companyweb.be/nl/0407040308/sint-carolus-mayerhof) · [CW EN](https://www.companyweb.be/en/0407040308/sint-carolus-mayerhof) · [CW FR](https://www.companyweb.be/fr/0407040308/sint-carolus-mayerhof) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407040308) · [mayerhof.be](https://www.mayerhof.be/)  
**tick:** 2025  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **25.04.2026**): omzet **EUR11,459,875** DROP −0.68%; pnl **EUR144,440** DROP −84.49%; equity **EUR16,112,179** JUMP +0.90%; bruto **EUR11,780,532** DROP −0.33%; FTE **135.2** JUMP (vs 116.2); assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Zilverbos YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Sint Carolus Mayerhof VZW — Fredericusstraat 89, 2640 Mortsel
info@mayerhof.be
cc: mj.vaneyndhoven@mayerhof.be / jp.waterkeyn@mayerhof.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint Carolus Mayerhof (KBO 0407.040.308)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 25.04.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs bewonersbijdragen 2025.
4. Toelichting pnl DROP (−84,49pct) t.o.v. FTE JUMP (116,2→135,2).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2025":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Evara — Sint Carolus Mayerhof YE2025 Medium"
        x["notes"] = (
            "tick2025 Sint Carolus Mayerhof Medium omzet DROP 11.46m pnl DROP 0.14m (-84.49pct) FTE JUMP 135.2; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zilverbos YE2025 deferred; next rq_2026; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover Sint Carolus Mayerhof YE2025 Medium CW; KBO 0407.040.308; "
            f"omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE JUMP {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2026" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2026",
            "title": "leftover dual hole-fill after Sint Carolus Mayerhof",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2025 after Sint Carolus Mayerhof YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Zilverbos / other unused YE2025 if live with omzet). "
                "Do NOT redo Sint Carolus Mayerhof, Evara/Multiversum, Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
                "PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, "
                "Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, "
                "AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, "
                "CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, "
                "IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, "
                "BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
                "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, "
                "BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/"
                "Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2025 Sint Carolus Mayerhof; next every-10 2030",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue updated")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for x in srows2:
    if x.get("state_id") == "main":
        x["mode"] = "continuous"
        x["current_sprint"] = "hole_fill"
        x["last_tick_utc"] = UTC
        x["last_unit_id"] = "rq_2025"
        x["ticks_completed"] = "2025"
        x["paused"] = "no"
        x["notes"] = (
            "tick2025 leftover Sint Carolus Mayerhof 0407.040.308 Medium CW (omzet DROP 11.46m pnl DROP 0.14m -84.49pct "
            "equity JUMP 16.11m bruto DROP 11.78m FTE JUMP 135.2; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Zilverbos YE2025 deferred; next rq_2026; next every-10 2030; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2025 - {UTC} - rq_2025 Sint Carolus Mayerhof (omzet DROP 11.46m / pnl DROP 0.14m / Medium)

- Unit: **rq_2025** leftover dual after **rq_2024 Evara**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred unused leftover **Sint Carolus Mayerhof** YE2025 (KBO **0407.040.308**; Fredericusstraat 89 Mortsel; Antwerpen **WZC VZW**). Zilverbos YE2025 also live — deferred. Do not redo Evara/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR11,459,875** DROP -0.68%; pnl **EUR144,440** DROP -84.49%; equity **EUR16,112,179** JUMP +0.90%; bruto **EUR11,780,532** DROP -0.33%; FTE **135.2** JUMP (vs 116.2); neerlegging **25.04.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@mayerhof.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_sint_carolus_mayerhof); foi + draft gap_sint_carolus_mayerhof_nbb_pdf_assets_debt_pnl_drop_matrix_l5; rq_2025=done + rq_2026 open; loop_state ticks=2025; raw under docs/doge/data/raw/tick2025/.
- FOI: **ready not sent** (human-gated; info@mayerhof.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2026 (AGB/FARO-if-YE2025 / AIESH-REW / Zilverbos / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2025")
