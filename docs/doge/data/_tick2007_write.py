# ephemeral tick2007 — Werken Glorieux / AZ Glorieux YE2025 Medium (leftover dual after AZ Alma)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T05:55:00Z"
ENTITY = "vzw_werken_glorieux"
GAP = "gap_werken_glorieux_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_werken_glorieux_jr2025_cw"
SRC_EN = "src_werken_glorieux_jr2025_cw_en"
SRC_FR = "src_werken_glorieux_jr2025_cw_fr"
SRC_KBO = "src_werken_glorieux_kbo_2007"
SRC_SITE = "src_werken_glorieux_site_2007"

OMZET = "164361670"
PNL = "1546006"
EQUITY = "72761817"
BRUTO = "91539005"
FTE = "1053.9"
OMZET24 = "162755812"
PNL24 = "1908140"
EQUITY24 = "71576247"
BRUTO24 = "89819802"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2007")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Werken Glorieux / AZ Glorieux YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0424380938/werken-glorieux",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2007; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 11.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2007/glorieux_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Werken Glorieux YE2025 statutory",
        "url": "https://www.companyweb.be/en/0424380938/werken-glorieux",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2007; EN mirror YE2025 Medium; filed 11-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2007/glorieux_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Werken Glorieux YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0424380938/werken-glorieux",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2007; FR mirror YE2025 Medium; deposés le 11-07-2026; raw docs/doge/data/raw/tick2007/glorieux_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Werken Glorieux 0424.380.938 Actief VZW Ronse",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424380938",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2007; Actief VZW since 24.09.1982; Werken Glorieux; Stefaan Modest Glorieuxlaan 55 9600 Ronse; no KBO email; 5 VE; Normale toestand",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azglorieux.be AZ Glorieux Ronse",
        "url": "https://azglorieux.be/",
        "publisher": "AZ Glorieux / Werken Glorieux",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2007; Ronse regional hospital; info@azglorieux.be; Glorieuxlaan 55 9600 Ronse",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_werken_glorieux_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2007; omzet JUMP {OMZET} +0.99pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_werken_glorieux_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2007; pnl DROP {PNL} -18.98pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_werken_glorieux_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2007; equity JUMP {EQUITY} +1.66pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_werken_glorieux_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2007; bruto JUMP {BRUTO} +1.91pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_werken_glorieux_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2007; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_werken_glorieux_jr2025_statutory_hospital",
    "title": "Werken Glorieux / AZ Glorieux YE2025 leftover hospital dual (omzet JUMP 164.36m / pnl DROP 1.55m / equity JUMP 72.76m)",
    "entity_id": ENTITY,
    "beneficiary": "Ronse-region hospital patients / AZ Glorieux",
    "legal_basis": "VZW/ASBL hospital Werken Glorieux (KBO 0424.380.938)",
    "decision_date": "2026-07-11",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0424380938/werken-glorieux",
    "stated_goal": "Regional hospital care (Ronse / Vlaamse Ardennen)",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>AZ_Glorieux_Werken_Glorieux>JR2025_statutory_L5",
    "notes": "tick2007; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH YE2024; Imelda CW N/A omzet; AZ Alma already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.4 + 0.35*5.4 + 0.10*4.0 = 5.26
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_werken_glorieux_omzet_jump_164_36m_pnl_drop_1_55m_jr2025",
    "name": "Werken Glorieux / AZ Glorieux omzet JUMP 164.36m / pnl DROP 1.55m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>AZ_Glorieux_Werken_Glorieux>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Ronse patients via Werken Glorieux VZW / AZ Glorieux",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 164.36m omzet JUMP +0.99pct with pnl DROP -18.98pct and mild equity JUMP +1.66pct; NBB PDF residual",
    "absurdity_score": "5.4",
    "cost_score": "5.4",
    "difficulty": "4.0",
    "priority_index": "5.26",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP path vs Alma/Herentals/Vitaz",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2007 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Werken Glorieux / AZ Glorieux",
    "name_fr": "Werken Glorieux / AZ Glorieux",
    "name_en": "Werken Glorieux / AZ Glorieux (Ronse hospital)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://azglorieux.be/",
    "foi_email": "info@azglorieux.be",
    "foi_postal": "Stefaan Modest Glorieuxlaan 55, 9600 Ronse",
    "notes": "tick2007 YE2025 Medium CW NL+EN+FR + Strong KBO 0424.380.938 Actief VZW; omzet JUMP 164.36m pnl DROP 1.55m equity JUMP 72.76m bruto JUMP 91.54m FTE 1053.9; assets/debt Unknown; neerlegging 11.07.2026; 5 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH YE2024; Imelda CW N/A; do not redo AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "OostVlaanderen>AZ_Glorieux_Werken_Glorieux>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP recon vs YE2024",
    "why_it_matters": "Medium CW shows 164.36m omzet Ronse hospital VZW with pnl DROP -19pct without balance sheet",
    "priority": "7",
    "recipient_body": "Werken Glorieux VZW / AZ Glorieux",
    "recipient_email": "info@azglorieux.be",
    "recipient_postal": "Stefaan Modest Glorieuxlaan 55, 9600 Ronse",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_werken_glorieux_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_werken_glorieux_omzet_jump_164_36m_pnl_drop_1_55m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2007; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Werken Glorieux / AZ Glorieux (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Werken Glorieux VZW / AZ Glorieux — KBO **0424.380.938**  
**recipient:** info@azglorieux.be · Stefaan Modest Glorieuxlaan 55, 9600 Ronse  
**sources:** [CW NL](https://www.companyweb.be/nl/0424380938/werken-glorieux) · [CW EN](https://www.companyweb.be/en/0424380938/werken-glorieux) · [CW FR](https://www.companyweb.be/fr/0424380938/werken-glorieux) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424380938) · [site](https://azglorieux.be/)  
**tick:** 2007  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **11.07.2026**): omzet **EUR164,361,670** JUMP +0.99%; pnl **EUR1,546,006** DROP −18.98%; equity **EUR72,761,817** JUMP +1.66%; bruto **EUR91,539,005** JUMP +1.91%; FTE **1053.9**; assets/debt **Unknown**.
- Ronse VZW hospital (legal name Werken Glorieux; brand AZ Glorieux). Preferred stall: AGB Bornem / FARO / AIESH still YE2024. Imelda CW N/A omzet. AZ Alma already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Werken Glorieux VZW / AZ Glorieux — Stefaan Modest Glorieuxlaan 55, 9600 Ronse
info@azglorieux.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Werken Glorieux / AZ Glorieux + balans (KBO 0424.380.938)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 11.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (EUR1.546.006 vs YE2024 EUR1.908.140; −18,98pct).
4. Dual vs Alma / Herentals / Vitaz indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2007":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ Alma — Werken Glorieux / AZ Glorieux YE2025 Medium"
        x["notes"] = (
            "tick2007 Werken Glorieux Medium omzet JUMP 164.36m pnl DROP 1.55m equity JUMP 72.76m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH YE2024; Imelda CW N/A; next rq_2008; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover Werken Glorieux / AZ Glorieux YE2025 Medium CW; KBO 0424.380.938; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2008" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2008",
            "title": "leftover dual hole-fill after Werken Glorieux / AZ Glorieux",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2007 after Werken Glorieux / AZ Glorieux YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Damiaan Oostende / AZ Maria Middelares / other unused YE2025 if live). "
                "Do NOT redo Werken Glorieux / AZ Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Maria Middelares/Imelda CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count. Erasme/UZB CW opaque."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2007 Werken Glorieux; next every-10 2010; Imelda CW N/A omzet",
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
        "last_unit_id": "rq_2007",
        "ticks_completed": "2007",
        "paused": "no",
        "notes": (
            "tick2007 leftover Werken Glorieux / AZ Glorieux 0424.380.938 Medium CW (omzet JUMP 164.36m pnl DROP 1.55m equity JUMP 72.76m bruto JUMP 91.54m FTE 1053.9; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH YE2024; Imelda CW N/A; next rq_2008; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2007 - {UTC} - rq_2007 Werken Glorieux / AZ Glorieux (omzet JUMP 164.36m / pnl DROP 1.55m / Medium)

- Unit: **rq_2007** leftover dual after **rq_2006 AZ Alma**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH still **YE2024**. Imelda CW **N/A omzet**; Erasme/UZB CW opaque. Took preferred leftover **Werken Glorieux / AZ Glorieux** YE2025 (KBO **0424.380.938**; Stefaan Modest Glorieuxlaan 55 Ronse; Oost-Vlaanderen **hospital VZW**). Do not redo AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR164,361,670** JUMP +0.99%; pnl **EUR1,546,006** DROP −18.98%; equity **EUR72,761,817** JUMP +1.66%; bruto **EUR91,539,005** JUMP +1.91%; FTE **1053.9**; neerlegging **11.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE; email info@azglorieux.be (no KBO email).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_werken_glorieux); foi + draft {GAP}; rq_2007=done + rq_2008 open; loop_state ticks=2007; raw under docs/doge/data/raw/tick2007/.
- FOI: **ready not sent** (human-gated; info@azglorieux.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2008 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Damiaan-Maria Middelares / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
