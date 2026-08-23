# ephemeral tick2018 — WZC Sint-Barbara Herselt YE2025 Medium (leftover HVZ dual after AZ Rivierenland)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T08:55:00Z"
ENTITY = "vzw_wzc_sint_barbara_herselt"
GAP = "gap_wzc_sint_barbara_herselt_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_wzc_sint_barbara_herselt_jr2025_cw"
SRC_EN = "src_wzc_sint_barbara_herselt_jr2025_cw_en"
SRC_FR = "src_wzc_sint_barbara_herselt_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_barbara_herselt_kbo_2018"
SRC_SITE = "src_wzc_sint_barbara_herselt_site_2018"

OMZET = "15237909"
PNL = "1757913"
EQUITY = "25533129"
BRUTO = "15645709"
FTE = "191.4"
OMZET24 = "14974221"
PNL24 = "1922924"
EQUITY24 = "24174064"
BRUTO24 = "15241341"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2018")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Barbara Herselt YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0422152314/woonzorgcentrum-sint-barbara",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2018; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 19.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2018/barbara_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Barbara Herselt YE2025 statutory",
        "url": "https://www.companyweb.be/en/0422152314/woonzorgcentrum-sint-barbara",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2018; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2018/barbara_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Barbara Herselt YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0422152314/woonzorgcentrum-sint-barbara",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2018; FR mirror YE2025 Medium; deposés le 19-06-2026; raw docs/doge/data/raw/tick2018/barbara_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum Sint-Barbara 0422.152.314 Actief VZW Herselt",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0422152314",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2018; Actief VZW since 10.12.1981; Dieperstraat 17 2230 Herselt; no KBO email; 1 VE",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "sintbarbara.be WZC Sint-Barbara Herselt",
        "url": "https://www.sintbarbara.be/",
        "publisher": "WZC Sint-Barbara",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2018; info@sintbarbara.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_barbara_herselt_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2018; omzet JUMP {OMZET} +1.76pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_barbara_herselt_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2018; pnl DROP {PNL} -8.58pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_sint_barbara_herselt_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2018; equity JUMP {EQUITY} +5.62pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_barbara_herselt_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2018; bruto JUMP {BRUTO} +2.65pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_barbara_herselt_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2018; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_barbara_herselt_jr2025_statutory_wzc",
    "title": "WZC Sint-Barbara Herselt YE2025 leftover HVZ dual (omzet JUMP 15.24m / pnl DROP 1.76m / equity JUMP 25.53m)",
    "entity_id": ENTITY,
    "beneficiary": "Herselt elderly care residents / WZC Sint-Barbara",
    "legal_basis": "VZW/ASBL WZC (KBO 0422.152.314)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0422152314/woonzorgcentrum-sint-barbara",
    "stated_goal": "Residential elderly care (Herselt)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>WZC_Sint_Barbara_Herselt>JR2025_statutory_L5",
    "notes": "tick2018; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; SFZ/Noorderhart/Jessa CW N/A; AZ Rivierenland already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_barbara_herselt_omzet_jump_15_24m_pnl_drop_1_76m_equity_jump_jr2025",
    "name": "WZC Sint-Barbara Herselt omzet JUMP 15.24m / pnl DROP 1.76m / equity JUMP 25.53m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "Antwerpen>WZC_Sint_Barbara_Herselt>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Herselt elderly via WZC Sint-Barbara VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 15.24m omzet JUMP +1.76pct with pnl DROP -8.58pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.175",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2018 leftover HVZ dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Sint-Barbara (Herselt)",
    "name_fr": "Woonzorgcentrum Sint-Barbara (Herselt)",
    "name_en": "WZC Sint-Barbara Herselt (elderly care)",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.sintbarbara.be/",
    "foi_email": "info@sintbarbara.be",
    "foi_postal": "Dieperstraat 17, 2230 Herselt",
    "notes": "tick2018 YE2025 Medium CW NL+EN+FR + Strong KBO 0422.152.314 Actief VZW; omzet JUMP 15.24m pnl DROP 1.76m equity JUMP 25.53m bruto JUMP 15.65m FTE 191.4; assets/debt Unknown; neerlegging 19.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; SFZ/Noorderhart/Jessa CW N/A; do not redo AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>WZC_Sint_Barbara_Herselt>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split",
    "why_it_matters": "Medium CW shows 15.24m omzet Herselt WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "Woonzorgcentrum Sint-Barbara vzw",
    "recipient_email": "info@sintbarbara.be",
    "recipient_postal": "Dieperstraat 17, 2230 Herselt",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_barbara_herselt_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_sint_barbara_herselt_omzet_jump_15_24m_pnl_drop_1_76m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2018; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Barbara Herselt (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Sint-Barbara vzw — KBO **0422.152.314**  
**recipient:** info@sintbarbara.be · Dieperstraat 17, 2230 Herselt  
**sources:** [CW NL](https://www.companyweb.be/nl/0422152314/woonzorgcentrum-sint-barbara) · [CW EN](https://www.companyweb.be/en/0422152314/woonzorgcentrum-sint-barbara) · [CW FR](https://www.companyweb.be/fr/0422152314/woonzorgcentrum-sint-barbara) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0422152314) · [site](https://www.sintbarbara.be/)  
**tick:** 2018  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **19.06.2026**): omzet **EUR15,237,909** JUMP +1.76%; pnl **EUR1,757,913** DROP −8.58%; equity **EUR25,533,129** JUMP +5.62%; bruto **EUR15,645,709** JUMP +2.65%; FTE **191.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024. SFZ/Noorderhart/Jessa CW N/A. AZ Rivierenland already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Sint-Barbara vzw — Dieperstraat 17, 2230 Herselt
info@sintbarbara.be
cc: Agentschap Zorg en Gezondheid / Provincie Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Barbara + balans (KBO 0422.152.314)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 19.06.2026).
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
    if x.get("task_id") == "rq_2018":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ Rivierenland — WZC Sint-Barbara Herselt YE2025 Medium"
        x["notes"] = (
            "tick2018 WZC Sint-Barbara Herselt Medium omzet JUMP 15.24m pnl DROP 1.76m equity JUMP 25.53m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; SFZ/Noorderhart/Jessa CW N/A; next rq_2019; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover WZC Sint-Barbara Herselt YE2025 Medium CW; KBO 0422.152.314; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2019" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2019",
            "title": "leftover dual hole-fill after WZC Sint-Barbara Herselt",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2018 after WZC Sint-Barbara Herselt YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC (St Vincentius Antwerpen / Maria's Rustoord / Sint-Carolus / Zilverbos / SFZ if omzet / other unused YE2025 if live). "
                "Do NOT redo WZC Sint-Barbara Herselt, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2018 WZC Sint-Barbara Herselt; next every-10 2020; SFZ/Jessa/ZOL CW N/A",
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
        "last_unit_id": "rq_2018",
        "ticks_completed": "2018",
        "paused": "no",
        "notes": (
            "tick2018 leftover WZC Sint-Barbara Herselt 0422.152.314 Medium CW (omzet JUMP 15.24m pnl DROP 1.76m equity JUMP 25.53m bruto JUMP 15.65m FTE 191.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; SFZ/Noorderhart/Jessa CW N/A; next rq_2019; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2018 - {UTC} - rq_2018 WZC Sint-Barbara Herselt (omzet JUMP 15.24m / pnl DROP 1.76m / Medium)

- Unit: **rq_2018** leftover dual after **rq_2017 AZ Rivierenland**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. SFZ/Noorderhart/Jessa/ZOL CW **N/A omzet**. Took unused leftover **WZC Sint-Barbara Herselt** YE2025 (KBO **0422.152.314**; Dieperstraat 17 Herselt; Antwerpen **WZC/HVZ VZW**). Do not redo AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC/Molenheide.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR15,237,909** JUMP +1.76%; pnl **EUR1,757,913** DROP −8.58%; equity **EUR25,533,129** JUMP +5.62%; bruto **EUR15,645,709** JUMP +2.65%; FTE **191.4**; neerlegging **19.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@sintbarbara.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_barbara_herselt); foi + draft {GAP}; rq_2018=done + rq_2019 open; loop_state ticks=2018; raw under docs/doge/data/raw/tick2018/.
- FOI: **ready not sent** (human-gated; info@sintbarbara.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2019 (AGB/FARO-if-YE2025 / AIESH-REW / St Vincentius-Maria Rustoord / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
