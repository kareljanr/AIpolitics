# ephemeral tick2023 — Maria Rustoord Ingelmunster YE2025 Medium (leftover after PPC Pittem)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T10:25:00Z"
ENTITY = "vzw_maria_rustoord_ingelmunster"
GAP = "gap_maria_rustoord_ingelmunster_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_maria_rustoord_ingelmunster_jr2025_cw"
SRC_EN = "src_maria_rustoord_ingelmunster_jr2025_cw_en"
SRC_FR = "src_maria_rustoord_ingelmunster_jr2025_cw_fr"
SRC_KBO = "src_maria_rustoord_ingelmunster_kbo_2023"
SRC_SITE = "src_maria_rustoord_ingelmunster_site_2023"

OMZET = "11639118"
PNL = "28482"
EQUITY = "6729521"
BRUTO = "12878713"
FTE = "160.1"
OMZET24 = "11439681"
PNL24 = "70471"
EQUITY24 = "7013419"
BRUTO24 = "12662457"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2023")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Maria Rustoord Ingelmunster YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0458458325/maria-rustoord-ingelmunster-v-z-w-",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2023; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2023/maria_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Maria Rustoord Ingelmunster YE2025 statutory",
        "url": "https://www.companyweb.be/en/0458458325/maria-rustoord-ingelmunster-v-z-w-",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2023; EN mirror YE2025 Medium; filed 01-07-2026; Last balance sheet year 2025; FTE 160.1; raw docs/doge/data/raw/tick2023/maria_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Maria Rustoord Ingelmunster YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0458458325/maria-rustoord-ingelmunster-v-z-w-",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2023; FR mirror YE2025 Medium; déposés le 01-07-2026; raw docs/doge/data/raw/tick2023/maria_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Maria Rustoord Ingelmunster 0458.458.325 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458458325",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2023; Actief VZW; Weststraat 53 8770 Ingelmunster; 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzcingelmunster.be WZC Maria Rustoord",
        "url": "https://www.wzcingelmunster.be/",
        "publisher": "WZC Maria Rustoord",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2023; info@wzcingelmunster.be; Weststraat 53 Ingelmunster",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_maria_rustoord_ingelmunster_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2023; omzet JUMP {OMZET} +1.74pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_maria_rustoord_ingelmunster_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2023; pnl DROP {PNL} -59.58pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_maria_rustoord_ingelmunster_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2023; equity DROP {EQUITY} -4.05pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_maria_rustoord_ingelmunster_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2023; bruto JUMP {BRUTO} +1.71pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_maria_rustoord_ingelmunster_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2023; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_maria_rustoord_ingelmunster_jr2025_statutory_wzc",
    "title": "Maria Rustoord Ingelmunster YE2025 leftover dual (omzet JUMP 11.64m / pnl DROP 28k / equity DROP 6.73m)",
    "entity_id": ENTITY,
    "beneficiary": "Ingelmunster elderly care residents / WZC Maria Rustoord",
    "legal_basis": "VZW/ASBL WZC (KBO 0458.458.325)",
    "decision_date": "2026-07-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0458458325/maria-rustoord-ingelmunster-v-z-w-",
    "stated_goal": "Residential elderly care (Ingelmunster)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>WZC_Maria_Rustoord_Ingelmunster>JR2025_statutory_L5",
    "notes": "tick2023; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; PPC Pittem already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.0 + 0.10*(10-4) = 5.375
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_maria_rustoord_ingelmunster_omzet_jump_11_64m_pnl_drop_28k_jr2025",
    "name": "Maria Rustoord Ingelmunster omzet JUMP 11.64m / pnl DROP 28k / equity DROP 6.73m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "WestVlaanderen>WZC_Maria_Rustoord_Ingelmunster>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Ingelmunster elderly via Maria Rustoord VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 11.64m omzet JUMP +1.74pct with pnl DROP -59.58pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.375",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2023 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Maria Rustoord Ingelmunster V.Z.W. (WZC)",
    "name_fr": "Maria Rustoord Ingelmunster (maison de repos)",
    "name_en": "WZC Maria Rustoord Ingelmunster (elderly care)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.wzcingelmunster.be/",
    "foi_email": "info@wzcingelmunster.be",
    "foi_postal": "Weststraat 53, 8770 Ingelmunster",
    "notes": "tick2023 YE2025 Medium CW NL+EN+FR + Strong KBO 0458.458.325 Actief VZW; omzet JUMP 11.64m pnl DROP 28k equity DROP 6.73m bruto JUMP 12.88m FTE 160.1; assets/debt Unknown; neerlegging 01.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "WestVlaanderen>WZC_Maria_Rustoord_Ingelmunster>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl DROP recon",
    "why_it_matters": "Medium CW shows 11.64m omzet Ingelmunster WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "Maria Rustoord Ingelmunster V.Z.W.",
    "recipient_email": "info@wzcingelmunster.be",
    "recipient_postal": "Weststraat 53, 8770 Ingelmunster",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_maria_rustoord_ingelmunster_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_maria_rustoord_ingelmunster_omzet_jump_11_64m_pnl_drop_28k_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2023; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Maria Rustoord Ingelmunster (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Maria Rustoord Ingelmunster V.Z.W. — KBO **0458.458.325**  
**recipient:** info@wzcingelmunster.be · Weststraat 53, 8770 Ingelmunster  
**sources:** [CW NL](https://www.companyweb.be/nl/0458458325/maria-rustoord-ingelmunster-v-z-w-) · [CW EN](https://www.companyweb.be/en/0458458325/maria-rustoord-ingelmunster-v-z-w-) · [CW FR](https://www.companyweb.be/fr/0458458325/maria-rustoord-ingelmunster-v-z-w-) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458458325) · [site](https://www.wzcingelmunster.be/)  
**tick:** 2023  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **01.07.2026**): omzet **EUR11,639,118** JUMP +1.74%; pnl **EUR28,482** DROP −59.58%; equity **EUR6,729,521** DROP −4.05%; bruto **EUR12,878,713** JUMP +1.71%; FTE **160.1**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. PPC Pittem already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Maria Rustoord Ingelmunster V.Z.W. — Weststraat 53, 8770 Ingelmunster
info@wzcingelmunster.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Maria Rustoord Ingelmunster + balans (KBO 0458.458.325)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 01.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl DROP (−59,58pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2023":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after PPC Pittem — Maria Rustoord Ingelmunster YE2025 Medium"
        x["notes"] = (
            "tick2023 Maria Rustoord Ingelmunster Medium omzet JUMP 11.64m pnl DROP 28k equity DROP 6.73m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2024; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover Maria Rustoord Ingelmunster YE2025 Medium CW; KBO 0458.458.325; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2024" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2024",
            "title": "leftover dual hole-fill after Maria Rustoord Ingelmunster",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2023 after Maria Rustoord Ingelmunster YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Multiversum-Evara if not double-count / Sint-Carolus / Zilverbos / other unused YE2025 if live with omzet). "
                "Do NOT redo Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2023 Maria Rustoord Ingelmunster; next every-10 2030",
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
        "last_unit_id": "rq_2023",
        "ticks_completed": "2023",
        "paused": "no",
        "notes": (
            "tick2023 leftover Maria Rustoord Ingelmunster 0458.458.325 Medium CW (omzet JUMP 11.64m pnl DROP 28k equity DROP 6.73m bruto JUMP 12.88m FTE 160.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2024; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2023 - {UTC} - rq_2023 Maria Rustoord Ingelmunster (omzet JUMP 11.64m / pnl DROP 28k / Medium)

- Unit: **rq_2023** leftover dual after **rq_2022 PPC Pittem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Maria Rustoord Ingelmunster** YE2025 (KBO **0458.458.325**; Weststraat 53 Ingelmunster; West-Vlaanderen **WZC VZW**). Do not redo PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR11,639,118** JUMP +1.74%; pnl **EUR28,482** DROP −59.58%; equity **EUR6,729,521** DROP −4.05%; bruto **EUR12,878,713** JUMP +1.71%; FTE **160.1**; neerlegging **01.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@wzcingelmunster.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_maria_rustoord_ingelmunster); foi + draft {GAP}; rq_2023=done + rq_2024 open; loop_state ticks=2023; raw under docs/doge/data/raw/tick2023/.
- FOI: **ready not sent** (human-gated; info@wzcingelmunster.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2024 (AGB/FARO-if-YE2025 / AIESH-REW / Multiversum-Sint-Carolus-Zilverbos / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
