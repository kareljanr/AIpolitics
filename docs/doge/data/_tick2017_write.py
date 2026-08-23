# ephemeral tick2017 — AZ Rivierenland YE2025 Medium (leftover dual after AZ Zeno)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T08:40:00Z"
ENTITY = "vzw_az_rivierenland"
GAP = "gap_az_rivierenland_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
SRC = "src_az_rivierenland_jr2025_cw"
SRC_EN = "src_az_rivierenland_jr2025_cw_en"
SRC_FR = "src_az_rivierenland_jr2025_cw_fr"
SRC_KBO = "src_az_rivierenland_kbo_2017"
SRC_SITE = "src_az_rivierenland_site_2017"

OMZET = "208256218"
PNL = "-251639"
EQUITY = "86822351"
BRUTO = "97540019"
FTE = "1089.6"
OMZET24 = "202105308"
PNL24 = "237348"
EQUITY24 = "89088809"
BRUTO24 = "93958723"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2017")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ Rivierenland YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0416851659",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2017; YE2025 omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 04.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2017/riv_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ Rivierenland YE2025 statutory",
        "url": "https://www.companyweb.be/en/0416851659",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2017; EN mirror YE2025 Medium; filed 04-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2017/riv_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ Rivierenland YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0416851659",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2017; FR mirror YE2025 Medium; deposés le 04-07-2026; raw docs/doge/data/raw/tick2017/riv_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ Rivierenland 0416.851.659 Actief VZW Rumst",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416851659",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2017; Actief VZW since 22.11.1976; AZ RIVIERENLAND; Rumst; no KBO email; 7 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azrivierenland.be AZ Rivierenland",
        "url": "https://www.azrivierenland.be/",
        "publisher": "AZ Rivierenland",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2017; Bornem/Rumst/Willebroek; info@azr.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_rivierenland_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2017; omzet JUMP {OMZET} +3.04pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_az_rivierenland_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2017; pnl LOSS {PNL} turnaround vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_az_rivierenland_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2017; equity DROP {EQUITY} -2.54pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_az_rivierenland_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2017; bruto JUMP {BRUTO} +3.81pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_az_rivierenland_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2017; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_rivierenland_jr2025_statutory_hospital",
    "title": "AZ Rivierenland YE2025 leftover hospital dual (omzet JUMP 208.26m / pnl LOSS 0.25m / equity DROP 86.82m)",
    "entity_id": ENTITY,
    "beneficiary": "Bornem/Rumst/Willebroek patients / AZ Rivierenland",
    "legal_basis": "VZW/ASBL hospital (KBO 0416.851.659)",
    "decision_date": "2026-07-04",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0416851659",
    "stated_goal": "Regional hospital care (Klein-Brabant / Rupel)",
    "cut_option": "Publish NBB PDF assets/debt + pnl LOSS recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>AZ_Rivierenland>JR2025_statutory_L5",
    "notes": "tick2017; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; Jessa/ZOL/SFZ CW N/A; AZ Zeno already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_rivierenland_omzet_jump_208_26m_pnl_loss_0_25m_equity_drop_jr2025",
    "name": "AZ Rivierenland omzet JUMP 208.26m / pnl LOSS 0.25m / equity DROP 86.82m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "Antwerpen>AZ_Rivierenland>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Bornem/Rumst patients via AZ Rivierenland VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 208.26m omzet JUMP +3.04pct with pnl turnaround LOSS -0.25m and equity DROP -2.54pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl LOSS vs YE2024 profit",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2017 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ Rivierenland",
    "name_fr": "AZ Rivierenland",
    "name_en": "AZ Rivierenland (Bornem/Rumst/Willebroek)",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.azrivierenland.be/",
    "foi_email": "info@azr.be",
    "foi_postal": "'s Herenbaan 172, 2840 Rumst",
    "notes": "tick2017 YE2025 Medium CW NL+EN+FR + Strong KBO 0416.851.659 Actief VZW; omzet JUMP 208.26m pnl LOSS 0.25m equity DROP 86.82m bruto JUMP 97.54m FTE 1089.6; assets/debt Unknown; neerlegging 04.07.2026; 7 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; Jessa/ZOL/SFZ CW N/A; do not redo AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>AZ_Rivierenland>NBB_PDF_assets_debt_pnl_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS recon vs YE2024 profit",
    "why_it_matters": "Medium CW shows 208.26m omzet Antwerp fusion hospital VZW with pnl turnaround LOSS without balance sheet",
    "priority": "7",
    "recipient_body": "AZ Rivierenland vzw",
    "recipient_email": "info@azr.be",
    "recipient_postal": "'s Herenbaan 172, 2840 Rumst",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_rivierenland_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_rivierenland_omzet_jump_208_26m_pnl_loss_0_25m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2017; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ Rivierenland (NBB PDF / assets-debt / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AZ Rivierenland vzw — KBO **0416.851.659**  
**recipient:** info@azr.be · 's Herenbaan 172, 2840 Rumst  
**sources:** [CW NL](https://www.companyweb.be/nl/0416851659) · [CW EN](https://www.companyweb.be/en/0416851659) · [CW FR](https://www.companyweb.be/fr/0416851659) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416851659) · [site](https://www.azrivierenland.be/)  
**tick:** 2017  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **04.07.2026**): omzet **EUR208,256,218** JUMP +3.04%; pnl **LOSS EUR-251,639** (vs YE2024 profit EUR237,348); equity **EUR86,822,351** DROP −2.54%; bruto **EUR97,540,019** JUMP +3.81%; FTE **1089.6**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024. Jessa/ZOL/SFZ CW N/A. AZ Zeno already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: AZ Rivierenland vzw — 's Herenbaan 172, 2840 Rumst
info@azr.be
cc: Agentschap Zorg en Gezondheid / Provincie Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZ Rivierenland + balans (KBO 0416.851.659)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 04.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS (EUR-251.639 vs YE2024 winst EUR237.348).
4. Dual vs campus Bornem/Rumst/Willebroek indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2017":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ Zeno — AZ Rivierenland YE2025 Medium"
        x["notes"] = (
            "tick2017 AZ Rivierenland Medium omzet JUMP 208.26m pnl LOSS 0.25m equity DROP 86.82m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; Jessa/ZOL/SFZ CW N/A; next rq_2018; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover AZ Rivierenland YE2025 Medium CW; KBO 0416.851.659; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2018" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2018",
            "title": "leftover dual hole-fill after AZ Rivierenland",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2017 after AZ Rivierenland YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (SFZ if omzet appears / Noorderhart / Jessa if omzet appears / other unused YE2025 if live). "
                "Do NOT redo AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Jessa/ZOL/Vesalius/SFZ/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2017 AZ Rivierenland; next every-10 2020; Jessa/ZOL/SFZ CW N/A",
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
        "last_unit_id": "rq_2017",
        "ticks_completed": "2017",
        "paused": "no",
        "notes": (
            "tick2017 leftover AZ Rivierenland 0416.851.659 Medium CW (omzet JUMP 208.26m pnl LOSS 0.25m equity DROP 86.82m bruto JUMP 97.54m FTE 1089.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; Jessa/ZOL/SFZ CW N/A; next rq_2018; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2017 - {UTC} - rq_2017 AZ Rivierenland (omzet JUMP 208.26m / pnl LOSS 0.25m / Medium)

- Unit: **rq_2017** leftover dual after **rq_2016 AZ Zeno**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Jessa/ZOL/SFZ CW **N/A omzet**. Took preferred leftover **AZ Rivierenland** YE2025 (KBO **0416.851.659**; Rumst/Bornem/Willebroek; Antwerpen **hospital VZW**). Do not redo AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR208,256,218** JUMP +3.04%; pnl **LOSS EUR-251,639** (vs YE2024 profit 0.24m); equity **EUR86,822,351** DROP −2.54%; bruto **EUR97,540,019** JUMP +3.81%; FTE **1089.6**; neerlegging **04.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 7 VE; email info@azr.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_rivierenland); foi + draft {GAP}; rq_2017=done + rq_2018 open; loop_state ticks=2017; raw under docs/doge/data/raw/tick2017/.
- FOI: **ready not sent** (human-gated; info@azr.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2018 (AGB/FARO-if-YE2025 / AIESH-REW / SFZ-Noorderhart / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
