# ephemeral tick2003 — Emmaüs YE2025 Medium (leftover dual after AZORG; OLV Aalst deferred double-count)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T04:55:00Z"
ENTITY = "vzw_emmaus"
GAP = "gap_emmaus_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_emmaus_jr2025_cw"
SRC_EN = "src_emmaus_jr2025_cw_en"
SRC_FR = "src_emmaus_jr2025_cw_fr"
SRC_KBO = "src_emmaus_kbo_2003"
SRC_SITE = "src_emmaus_site_2003"

OMZET = "624168726"
PNL = "15447573"
EQUITY = "572374043"
BRUTO = "557830841"
FTE = "6326.6"
OMZET24 = "596901644"
PNL24 = "11025160"
EQUITY24 = "557842351"
BRUTO24 = "531908547"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2003")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Emmaüs YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0411515075",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2003; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 25.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2003/emmaus_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Emmaüs YE2025 statutory",
        "url": "https://www.companyweb.be/en/0411515075",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2003; EN mirror YE2025 Medium; filed 25-06-2026; Last balance sheet year 2025; Hospital activities; raw docs/doge/data/raw/tick2003/emmaus_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Emmaüs YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0411515075",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2003; FR mirror YE2025 Medium; déposés le 25-06-2026; raw docs/doge/data/raw/tick2003/emmaus_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Emmaüs 0411.515.075 Actief VZW Mechelen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411515075",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2003; Actief VZW since 17.09.1971; Emmaüs; Edgard Tinellaan 1C 2800 Mechelen; coordinatie@emmaus.be; www.emmaus.be; 100 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "emmaus.be / azsintmaarten.be Emmaüs care+hospital group",
        "url": "https://www.emmaus.be/",
        "publisher": "Emmaüs VZW",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2003; Emmaüs zorggroep incl. AZ Sint-Maarten Mechelen; azsintmaarten@emmaus.be; dual hospital+care",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_emmaus_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2003; omzet JUMP {OMZET} +4.57pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_emmaus_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2003; pnl JUMP {PNL} +40.11pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_emmaus_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2003; equity JUMP {EQUITY} +2.60pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_emmaus_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2003; bruto JUMP {BRUTO} +4.87pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_emmaus_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2003; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_emmaus_jr2025_statutory_hospital",
    "title": "Emmaüs YE2025 leftover hospital-zorg dual (omzet JUMP 624.17m / pnl JUMP 15.45m / equity JUMP 572.37m)",
    "entity_id": ENTITY,
    "beneficiary": "Mechelen-region patients / AZ Sint-Maarten + Emmaüs care network",
    "legal_basis": "VZW/ASBL care+hospital entity (KBO 0411.515.075); Emmaüs zorggroep / AZ Sint-Maarten",
    "decision_date": "2026-06-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0411515075",
    "stated_goal": "Emmaüs hospital+care network operations (AZ Sint-Maarten dual)",
    "cut_option": "Publish NBB PDF assets/debt + pnl JUMP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>Mechelen>Emmaus>JR2025_statutory_L5",
    "notes": "tick2003; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Aalst YE2025 live but AZORG fusion double-count deferred; AZORG already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*6.5 + 0.10*4.0 = 5.70
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_emmaus_omzet_jump_624_17m_pnl_jump_15_45m_equity_jump_jr2025",
    "name": "Emmaüs omzet JUMP 624.17m / pnl JUMP 15.45m / equity JUMP 572.37m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_zorg_vzw_dual",
    "hierarchy_path": "Antwerpen>Mechelen>Emmaus>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Mechelen-region patients via Emmaüs / AZ Sint-Maarten VZW",
    "stated_goal": "Hospital+care network",
    "measured_outcome": "Medium CW YE2025; 624.17m omzet with pnl JUMP +40pct and equity JUMP +2.6pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.5",
    "difficulty": "4.0",
    "priority_index": "5.70",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl JUMP path vs AZORG/Z.org/AZ Delta; dual AZ Sint-Maarten vs Emmaüs perimeter",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2003 leftover dual; Medium CW; TE-adjacent hospital-zorg flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Emmaüs (AZ Sint-Maarten zorggroep)",
    "name_fr": "Emmaüs (groupe hospitalier AZ Sint-Maarten)",
    "name_en": "Emmaüs (AZ Sint-Maarten hospital+care VZW)",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.emmaus.be/",
    "foi_email": "coordinatie@emmaus.be",
    "foi_postal": "Edgard Tinellaan 1C, 2800 Mechelen",
    "notes": "tick2003 YE2025 Medium CW NL+EN+FR + Strong KBO 0411.515.075 Actief VZW; omzet JUMP 624.17m pnl JUMP 15.45m equity JUMP 572.37m bruto JUMP 557.83m FTE 6326.6; assets/debt Unknown; neerlegging 25.06.2026; 100 VE; Aanbestedende overheid; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Aalst deferred AZORG double-count; do not redo AZORG/Z.org/AZ Delta/AZJP/ZAS/Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>Mechelen>Emmaus>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl JUMP recon vs YE2024; dual AZ Sint-Maarten vs Emmaüs care perimeter",
    "why_it_matters": "Medium CW shows 624.17m omzet Mechelen hospital+care VZW with pnl JUMP +40pct without balance sheet",
    "priority": "7",
    "recipient_body": "Emmaüs VZW",
    "recipient_email": "coordinatie@emmaus.be",
    "recipient_postal": "Edgard Tinellaan 1C, 2800 Mechelen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_emmaus_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_emmaus_omzet_jump_624_17m_pnl_jump_15_45m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2003; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Emmaüs / AZ Sint-Maarten (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Emmaüs VZW — KBO **0411.515.075**  
**recipient:** coordinatie@emmaus.be · Edgard Tinellaan 1C, 2800 Mechelen (cc azsintmaarten@emmaus.be)  
**sources:** [CW NL](https://www.companyweb.be/nl/0411515075) · [CW EN](https://www.companyweb.be/en/0411515075) · [CW FR](https://www.companyweb.be/fr/0411515075) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411515075) · [emmaus.be](https://www.emmaus.be/) · [azsintmaarten.be](https://www.azsintmaarten.be/)  
**tick:** 2003  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **25.06.2026**): omzet **EUR624,168,726** JUMP +4.57%; pnl **EUR15,447,573** JUMP +40.11%; equity **EUR572,374,043** JUMP +2.60%; bruto **EUR557,830,841** JUMP +4.87%; FTE **6326.6**; assets/debt **Unknown**.
- Mechelen VZW hospital+care group (Hospital activities / AZ Sint-Maarten dual; 100 VE; Aanbestedende overheid). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. OLV Aalst YE2025 live but deferred (AZORG fusion double-count; site→azorg.be). AZORG already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Emmaüs VZW — Edgard Tinellaan 1C, 2800 Mechelen
coordinatie@emmaus.be
cc: azsintmaarten@emmaus.be / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Emmaüs + balans (KBO 0411.515.075)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 25.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl JUMP (EUR15.447.573 vs YE2024 EUR11.025.160; +40,11pct) en equity JUMP (+2,60pct).
4. Dual AZ Sint-Maarten vs overige Emmaüs zorgperimeter indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2003":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZORG — Emmaüs YE2025 Medium"
        x["notes"] = (
            "tick2003 Emmaüs Medium omzet JUMP 624.17m pnl JUMP 15.45m equity JUMP 572.37m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Aalst deferred AZORG double-count; next rq_2004; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover Emmaüs YE2025 Medium CW; KBO 0411.515.075; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2004" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2004",
            "title": "leftover dual hole-fill after Emmaüs",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2003 after Emmaüs YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital "
                "(AZ Monica / other unused YE2025 if live figures; Erasme/UZ Brussel/AZ Sint-Jan/AZ Turnhout/AZ Klina only if public euros appear). "
                "Do NOT redo Emmaüs, AZORG, OLV Aalst (AZORG fusion double-count), Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, "
                "CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Note: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZB/AZ Sint-Jan/AZ Turnhout/AZ Klina CW opaque or N/A omzet as of 2003. Next every-10 is 2010."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2003 Emmaüs; next every-10 2010; AGB/FARO/AIESH/REW still YE2024; OLV Aalst deferred AZORG double-count",
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
        "last_unit_id": "rq_2003",
        "ticks_completed": "2003",
        "paused": "no",
        "notes": (
            "tick2003 leftover Emmaüs 0411.515.075 Medium CW (omzet JUMP 624.17m pnl JUMP 15.45m equity JUMP 572.37m bruto JUMP 557.83m FTE 6326.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Aalst deferred AZORG double-count; next rq_2004; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2003 - {UTC} - rq_2003 Emmaüs (omzet JUMP 624.17m / pnl JUMP 15.45m / Medium)

- Unit: **rq_2003** leftover dual after **rq_2002 AZORG**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. OLV Aalst YE2025 live (omzet 464.13m) but **deferred** (site→azorg.be / AZORG fusion **double-count**). Took unused leftover **Emmaüs** YE2025 (KBO **0411.515.075**; Edgard Tinellaan 1C Mechelen; Antwerpen **hospital+care VZW** / AZ Sint-Maarten dual). Do not redo AZORG/Z.org/AZ Delta/AZJP/ZAS/Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR624,168,726** JUMP +4.57%; pnl **EUR15,447,573** JUMP +40.11%; equity **EUR572,374,043** JUMP +2.60%; bruto **EUR557,830,841** JUMP +4.87%; FTE **6326.6**; neerlegging **25.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 100 VE; Aanbestedende overheid; email coordinatie@emmaus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_emmaus); foi + draft {GAP}; rq_2003=done + rq_2004 open; loop_state ticks=2003; raw under docs/doge/data/raw/tick2003/.
- FOI: **ready not sent** (human-gated; coordinatie@emmaus.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2004 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Monica / unused DSO-IGS-HVZ-hospital).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
