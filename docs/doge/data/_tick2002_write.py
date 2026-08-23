# ephemeral tick2002 — AZORG YE2025 Medium (leftover dual after Z.org KU Leuven)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T04:20:00Z"
ENTITY = "vzw_azorg"
GAP = "gap_azorg_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
SRC = "src_azorg_jr2025_cw"
SRC_EN = "src_azorg_jr2025_cw_en"
SRC_FR = "src_azorg_jr2025_cw_fr"
SRC_KBO = "src_azorg_kbo_2002"
SRC_SITE = "src_azorg_site_2002"

OMZET = "824928494"
PNL = "-5085994"
EQUITY = "273342580"
BRUTO = "360386008"
FTE = "3786.7"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2002")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZORG YE2025 statutory",
        "url": "https://www.companyweb.be/nl/1005154085",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2002; YE2025 fusion-first omzet {OMZET} pnl LOSS {PNL} equity {EQUITY} bruto {BRUTO} FTE {FTE}; neerlegging 07.07.2026; no YE2024 CW compare; assets/debt Unknown; raw docs/doge/data/raw/tick2002/azorg_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZORG YE2025 statutory",
        "url": "https://www.companyweb.be/en/1005154085",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2002; EN mirror YE2025 Medium; filed 07-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2002/azorg_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZORG YE2025 statutory",
        "url": "https://www.companyweb.be/fr/1005154085",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2002; FR mirror YE2025 Medium; deposés le 07-07-2026; raw docs/doge/data/raw/tick2002/azorg_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZORG 1005.154.085 Actief VZW Aalst",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=1005154085",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2002; Actief VZW since 24.01.2024; AZORG; Moorselbaan 164 9300 Aalst; no KBO email; 6 VE; Aanbestedende overheid sinds 01.01.2025; ASZ+OLV fusion hospital",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azorg.be AZORG",
        "url": "https://www.azorg.be/",
        "publisher": "AZORG",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2002; Aalst fusion hospital (ex ASZ+OLV); info@azorg.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_azorg_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover (fusion-first year)",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2002; YE2025 fusion-first omzet {OMZET}; no YE2024 CW peer year",
    },
    {
        "budget_id": "bud_azorg_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2002; pnl LOSS {PNL} fusion-first YE2025",
    },
    {
        "budget_id": "bud_azorg_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2002; equity {EQUITY} fusion-first YE2025",
    },
    {
        "budget_id": "bud_azorg_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2002; bruto {BRUTO} fusion-first YE2025",
    },
    {
        "budget_id": "bud_azorg_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2002; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_azorg_jr2025_statutory_hospital",
    "title": "AZORG YE2025 leftover hospital dual (omzet 824.93m / pnl LOSS 5.09m / equity 273.34m fusion-first)",
    "entity_id": ENTITY,
    "beneficiary": "Aalst-region hospital patients / AZORG (ex ASZ+OLV fusion)",
    "legal_basis": "VZW/ASBL hospital (KBO 1005.154.085); ASZ+OLV fusion from 2025",
    "decision_date": "2026-07-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/1005154085",
    "stated_goal": "Fused multi-campus hospital care (Aalst region)",
    "cut_option": "Publish NBB PDF assets/debt + fusion perimeter / pnl LOSS recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>AZORG>JR2025_statutory_L5",
    "notes": "tick2002; Medium CW; fusion-first YE2025 no YE2024 CW peer; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; OLV Aalst YE2025 also live deferred (possible double-count); Z.org KU Leuven already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*7.5 + 0.35*6.5 + 0.10*4.0 = 4.125+2.275+0.4 = 6.8
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_azorg_omzet_824_93m_pnl_loss_5_09m_equity_273_34m_jr2025",
    "name": "AZORG omzet 824.93m / pnl LOSS 5.09m / equity 273.34m (YE2025 fusion-first)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>AZORG>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory fusion-first omzet {OMZET} pnl LOSS {PNL} equity {EQUITY} bruto {BRUTO} FTE {FTE}; assets/debt Unknown; no YE2024 CW peer",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Aalst-region patients via AZORG VZW (ASZ+OLV fusion)",
    "stated_goal": "Fused multi-campus hospital care",
    "measured_outcome": "Medium CW YE2025 fusion-first; 824.93m omzet with pnl LOSS 5.09m; NBB PDF residual; dual vs OLV Aalst path possible",
    "absurdity_score": "6.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.8",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon fusion perimeter vs OLV/ASZ legacy; pnl LOSS path vs ZAS/AZ Delta",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2002 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZORG",
    "name_fr": "AZORG",
    "name_en": "AZORG (Aalst fusion hospital, ex ASZ+OLV)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azorg.be/",
    "foi_email": "info@azorg.be",
    "foi_postal": "Moorselbaan 164, 9300 Aalst",
    "notes": "tick2002 YE2025 Medium CW NL+EN+FR + Strong KBO 1005.154.085 Actief VZW; fusion-first omzet 824.93m pnl LOSS 5.09m equity 273.34m bruto 360.39m FTE 3786.7; assets/debt Unknown; neerlegging 07.07.2026; 6 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; OLV Aalst YE2025 deferred; do not redo Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "OostVlaanderen>AZORG>NBB_PDF_assets_debt_pnl_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); fusion perimeter ASZ+OLV; pnl LOSS recon",
    "why_it_matters": "Medium CW shows 824.93m omzet Aalst fusion hospital VZW with pnl LOSS without balance sheet",
    "priority": "8",
    "recipient_body": "AZORG VZW",
    "recipient_email": "info@azorg.be",
    "recipient_postal": "Moorselbaan 164, 9300 Aalst",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_azorg_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_azorg_omzet_824_93m_pnl_loss_5_09m_equity_273_34m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2002; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZORG (NBB PDF / assets-debt / pnl LOSS / fusion)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AZORG VZW — KBO **1005.154.085**  
**recipient:** info@azorg.be · Moorselbaan 164, 9300 Aalst  
**sources:** [CW NL](https://www.companyweb.be/nl/1005154085) · [CW EN](https://www.companyweb.be/en/1005154085) · [CW FR](https://www.companyweb.be/fr/1005154085) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=1005154085) · [site](https://www.azorg.be/)  
**tick:** 2002  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; fusion-first year)

## Context
- YE **2025** (neerlegging **07.07.2026**): omzet **EUR824,928,494**; pnl **LOSS EUR-5,085,994**; equity **EUR273,342,580**; bruto **EUR360,386,008**; FTE **3786.7**; assets/debt **Unknown**. No YE2024 CW peer (fusion-first).
- Aalst VZW hospital (ASZ+OLV fusion). Preferred stall: AGB Bornem / FARO still YE2024. OLV Aalst YE2025 also live (deferred — possible double-count). Z.org KU Leuven already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: AZORG VZW — Moorselbaan 164, 9300 Aalst
info@azorg.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZORG + balans (KBO 1005.154.085)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 07.07.2026).
2. Assets / schulden LT-ST / cash.
3. Fusion perimeter ASZ+OLV / consolidatie-toelichting.
4. Recon pnl LOSS (EUR-5.085.994).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2002":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Z.org KU Leuven — AZORG YE2025 Medium"
        x["notes"] = (
            "tick2002 AZORG Medium fusion-first omzet 824.93m pnl LOSS 5.09m equity 273.34m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; OLV Aalst YE2025 deferred; next rq_2003; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover AZORG YE2025 Medium CW; KBO 1005.154.085; "
            f"omzet {OMZET} pnl LOSS {PNL} equity {EQUITY} bruto {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2003" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2003",
            "title": "leftover dual hole-fill after AZORG",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2002 after AZORG YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (OLV Aalst 0410.424.222 if not double-count / AZ Sint-Jan / other unused YE2025 if live). "
                "Do NOT redo AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "OLV Aalst YE2025 live but may double-count AZORG fusion — prefer other unused or FOI-clarify perimeter."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2002 AZORG; next every-10 2010; OLV Aalst YE2025 deferred double-count risk",
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
        "last_unit_id": "rq_2002",
        "ticks_completed": "2002",
        "paused": "no",
        "notes": (
            "tick2002 leftover AZORG 1005.154.085 Medium CW (fusion-first omzet 824.93m pnl LOSS 5.09m equity 273.34m bruto 360.39m FTE 3786.7; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; OLV Aalst YE2025 deferred; next rq_2003; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2002 - {UTC} - rq_2002 AZORG (omzet 824.93m / pnl LOSS 5.09m / Medium)

- Unit: **rq_2002** leftover dual after **rq_2001 Z.org KU Leuven**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. AZ Klina filed but CW N/A omzet. Took unused leftover **AZORG** YE2025 (KBO **1005.154.085**; Moorselbaan 164 Aalst; Oost-Vlaanderen **fusion hospital VZW** ex ASZ+OLV). **OLV Aalst** YE2025 also live deferred (double-count risk). Do not redo Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 fusion-first - omzet **EUR824,928,494**; pnl **LOSS EUR-5,085,994**; equity **EUR273,342,580**; bruto **EUR360,386,008**; FTE **3786.7**; neerlegging **07.07.2026**. No YE2024 CW peer. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 6 VE; email info@azorg.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_azorg); foi + draft {GAP}; rq_2002=done + rq_2003 open; loop_state ticks=2002; raw under docs/doge/data/raw/tick2002/.
- FOI: **ready not sent** (human-gated; info@azorg.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2003 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital; OLV Aalst deferred).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
