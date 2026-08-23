# ephemeral tick2015 — Heilig Hart Tienen YE2025 Medium (leftover dual after HH Leuven)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T08:10:00Z"
ENTITY = "vzw_hh_tienen"
GAP = "gap_hh_tienen_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_hh_tienen_jr2025_cw"
SRC_EN = "src_hh_tienen_jr2025_cw_en"
SRC_FR = "src_hh_tienen_jr2025_cw_fr"
SRC_KBO = "src_hh_tienen_kbo_2015"
SRC_SITE = "src_hh_tienen_site_2015"

OMZET = "138497861"
PNL = "820951"
EQUITY = "72199492"
BRUTO = "64664813"
FTE = "710.4"
OMZET24 = "132643366"
PNL24 = "2185210"
EQUITY24 = "69360227"
BRUTO24 = "61884912"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2015")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Regionaal Ziekenhuis Heilig Hart Tienen YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0408228557/regionaal-ziekenhuis-heilig-hart-tienen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2015; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 27.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2015/hhtienen_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Regionaal Ziekenhuis Heilig Hart Tienen YE2025 statutory",
        "url": "https://www.companyweb.be/en/0408228557/regionaal-ziekenhuis-heilig-hart-tienen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2015; EN mirror YE2025 Medium; filed 27-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2015/hhtienen_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Regionaal Ziekenhuis Heilig Hart Tienen YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0408228557/regionaal-ziekenhuis-heilig-hart-tienen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2015; FR mirror YE2025 Medium; deposés le 27-06-2026; raw docs/doge/data/raw/tick2015/hhtienen_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Regionaal Ziekenhuis Heilig Hart Tienen 0408.228.557 Actief VZW Tienen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408228557",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2015; Actief VZW since 19.03.1971; Kliniekstraat 45 3300 Tienen; no KBO email; 3 VE; 15 functiehouders",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "rztienen.be Regionaal Ziekenhuis Heilig Hart Tienen",
        "url": "https://www.rztienen.be/",
        "publisher": "Heilig Hart Tienen",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2015; communicatiedienst@rztienen.be (published FOI/comms route)",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_hh_tienen_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2015; omzet JUMP {OMZET} +4.41pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_hh_tienen_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2015; pnl DROP {PNL} -62.43pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_hh_tienen_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2015; equity JUMP {EQUITY} +4.09pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_hh_tienen_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2015; bruto JUMP {BRUTO} +4.49pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_hh_tienen_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2015; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_hh_tienen_jr2025_statutory_hospital",
    "title": "Heilig Hart Tienen YE2025 leftover hospital dual (omzet JUMP 138.50m / pnl DROP 0.82m / equity JUMP 72.20m)",
    "entity_id": ENTITY,
    "beneficiary": "Tienen-region hospital patients / Heilig Hart Tienen",
    "legal_basis": "VZW/ASBL hospital (KBO 0408.228.557)",
    "decision_date": "2026-06-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0408228557/regionaal-ziekenhuis-heilig-hart-tienen",
    "stated_goal": "Regional hospital care (Tienen)",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Tienen>JR2025_statutory_L5",
    "notes": "tick2015; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; AZ Zeno CW year-label 2008 opaque deferred; HH Leuven already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_hh_tienen_omzet_jump_138_50m_pnl_drop_0_82m_equity_jump_jr2025",
    "name": "Heilig Hart Tienen omzet JUMP 138.50m / pnl DROP 0.82m (-62.43pct) / equity JUMP 72.20m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Tienen>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Tienen patients via Heilig Hart Tienen VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 138.50m omzet JUMP +4.41pct with pnl DROP -62.43pct; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.40",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP vs HH Leuven/Lier/Sint-Trudo",
    "status": "active",
    "struck_reason": "",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Regionaal Ziekenhuis Heilig Hart Tienen",
    "name_fr": "Hôpital régional Heilig Hart Tienen",
    "name_en": "Regional Hospital Heilig Hart Tienen",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.rztienen.be/",
    "foi_email": "communicatiedienst@rztienen.be",
    "foi_postal": "Kliniekstraat 45, 3300 Tienen",
    "notes": "tick2015 YE2025 Medium CW NL+EN+FR + Strong KBO 0408.228.557 Actief VZW; omzet JUMP 138.50m pnl DROP 0.82m equity JUMP 72.20m bruto JUMP 64.66m FTE 710.4; assets/debt Unknown; neerlegging 27.06.2026; 3 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; AZ Zeno year-label 2008 opaque deferred; do not redo HH Leuven/Sint-Trudo/Sint-Andries Tielt/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS",
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
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Tienen>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash) + pnl DROP recon from 2.19m to 0.82m",
    "why_it_matters": "Medium CW shows 138.50m omzet Tienen hospital VZW with pnl DROP -62.43pct and no balance sheet",
    "priority": "8",
    "recipient_body": "Regionaal Ziekenhuis Heilig Hart Tienen vzw",
    "recipient_email": "communicatiedienst@rztienen.be",
    "recipient_postal": "Kliniekstraat 45, 3300 Tienen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_hh_tienen_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_hh_tienen_omzet_jump_138_50m_pnl_drop_0_82m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2015; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Heilig Hart Tienen (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Regionaal Ziekenhuis Heilig Hart Tienen vzw — KBO **0408.228.557**  
**recipient:** communicatiedienst@rztienen.be · Kliniekstraat 45, 3300 Tienen  
**sources:** [CW NL](https://www.companyweb.be/nl/0408228557/regionaal-ziekenhuis-heilig-hart-tienen) · [CW EN](https://www.companyweb.be/en/0408228557/regionaal-ziekenhuis-heilig-hart-tienen) · [CW FR](https://www.companyweb.be/fr/0408228557/regionaal-ziekenhuis-heilig-hart-tienen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408228557) · [site](https://www.rztienen.be/)  
**tick:** 2015  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **27.06.2026**): omzet **EUR138,497,861** JUMP +4.41%; pnl **EUR820,951** DROP −62.43%; equity **EUR72,199,492** JUMP +4.09%; bruto **EUR64,664,813** JUMP +4.49%; FTE **710.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; AZ Zeno CW year-label still **2008** opaque. HH Leuven already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Regionaal Ziekenhuis Heilig Hart Tienen vzw — Kliniekstraat 45, 3300 Tienen
communicatiedienst@rztienen.be
cc: Agentschap Zorg en Gezondheid / Provincie Vlaams-Brabant indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Heilig Hart Tienen + balans + PnL-daling (KBO 0408.228.557)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 27.06.2026).
2. Assets / schulden LT-ST / cash.
3. Toelichting PnL-daling van EUR2.185.210 (YE2024) naar EUR820.951 (YE2025).
4. Dual vs Heilig Hart Leuven / Heilig Hart Lier indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2015":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Heilig Hart Leuven — Heilig Hart Tienen YE2025 Medium"
        x["notes"] = (
            "tick2015 HH Tienen Medium omzet JUMP 138.50m pnl DROP 0.82m equity JUMP 72.20m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; AZ Zeno year-label 2008 deferred; next rq_2016; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover Heilig Hart Tienen YE2025 Medium CW; KBO 0408.228.557; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2016" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2016",
            "title": "leftover dual hole-fill after Heilig Hart Tienen",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2015 after Heilig Hart Tienen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Zeno if YE2025 year-label clarified / Vesalius / Klina / Rivierenland / SFZ / other unused YE2025 if live). "
                "Do NOT redo Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count. AZ Zeno CW still labels year 2008 despite 02.07.2026 filing — do not invent YE2025."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2015 HH Tienen; next every-10 2020; AZ Zeno year-label 2008 opaque",
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
        "last_unit_id": "rq_2015",
        "ticks_completed": "2015",
        "paused": "no",
        "notes": (
            "tick2015 leftover HH Tienen 0408.228.557 Medium CW (omzet JUMP 138.50m pnl DROP 0.82m equity JUMP 72.20m bruto JUMP 64.66m FTE 710.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; AZ Zeno year-label 2008 deferred; next rq_2016; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2015 - {UTC} - rq_2015 Heilig Hart Tienen (omzet JUMP 138.50m / pnl DROP 0.82m / Medium)

- Unit: **rq_2015** leftover dual after **rq_2014 Heilig Hart Leuven**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (filed 17.07.2025); REW still **YE2024** (filed 11.12.2025). AZ Zeno CW still labels year **2008** despite filing 02.07.2026 — deferred (no invented YE2025). Took unused leftover **Heilig Hart Tienen** YE2025 (KBO **0408.228.557**; Kliniekstraat 45 Tienen; Vlaams-Brabant **hospital VZW**). Do not redo HH Leuven/Sint-Trudo/Sint-Andries Tielt/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR138,497,861** JUMP +4.41%; pnl **EUR820,951** DROP −62.43%; equity **EUR72,199,492** JUMP +4.09%; bruto **EUR64,664,813** JUMP +4.49%; FTE **710.4**; neerlegging **27.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email communicatiedienst@rztienen.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_hh_tienen); foi + draft {GAP}; rq_2015=done + rq_2016 open; loop_state ticks=2015; raw under docs/doge/data/raw/tick2015/.
- FOI: **ready not sent** (human-gated; communicatiedienst@rztienen.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2016 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Zeno-if-clarified / Vesalius-Klina / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
