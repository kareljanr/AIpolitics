# ephemeral tick2004 — Vitaz YE2025 Medium (leftover dual after Emmaüs)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T05:10:00Z"
ENTITY = "vzw_vitaz"
GAP = "gap_vitaz_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_vitaz_jr2025_cw"
SRC_EN = "src_vitaz_jr2025_cw_en"
SRC_FR = "src_vitaz_jr2025_cw_fr"
SRC_KBO = "src_vitaz_kbo_2004"
SRC_SITE = "src_vitaz_site_2004"

OMZET = "474708586"
PNL = "12864965"
EQUITY = "181913017"
BRUTO = "201584911"
FTE = "2227.4"
OMZET24 = "455024743"
PNL24 = "11224932"
EQUITY24 = "170205055"
BRUTO24 = "193489556"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2004")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Vitaz YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0881291322/vitaz",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2004; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 24.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2004/vitaz_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Vitaz YE2025 statutory",
        "url": "https://www.companyweb.be/en/0881291322/vitaz",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2004; EN mirror YE2025 Medium; filed 24-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2004/vitaz_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Vitaz YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0881291322/vitaz",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2004; FR mirror YE2025 Medium; deposés le 24-07-2026; raw docs/doge/data/raw/tick2004/vitaz_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Vitaz 0881.291.322 Actief VZW Sint-Niklaas",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0881291322",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2004; Actief VZW since 12.05.2006; Vitaz; Moerlandstraat 1 9100 Sint-Niklaas; no KBO email; 9 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "vitaz.be Vitaz",
        "url": "https://www.vitaz.be/",
        "publisher": "Vitaz",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2004; Waasland hospital network; info@vitaz.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_vitaz_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2004; omzet JUMP {OMZET} +4.33pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_vitaz_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2004; pnl JUMP {PNL} +14.61pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_vitaz_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2004; equity JUMP {EQUITY} +6.88pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_vitaz_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2004; bruto JUMP {BRUTO} +4.18pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_vitaz_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2004; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_vitaz_jr2025_statutory_hospital",
    "title": "Vitaz YE2025 leftover hospital dual (omzet JUMP 474.71m / pnl JUMP 12.86m / equity JUMP 181.91m)",
    "entity_id": ENTITY,
    "beneficiary": "Waasland hospital patients / Vitaz",
    "legal_basis": "VZW/ASBL hospital (KBO 0881.291.322)",
    "decision_date": "2026-07-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0881291322/vitaz",
    "stated_goal": "Waasland multi-campus hospital care",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>Vitaz>JR2025_statutory_L5",
    "notes": "tick2004; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AZ Monica CW N/A omzet; Emmaüs already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*7.5 + 0.35*5.5 + 0.10*4.0 = 6.45
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_vitaz_omzet_jump_474_71m_pnl_jump_12_86m_equity_jump_jr2025",
    "name": "Vitaz omzet JUMP 474.71m / pnl JUMP 12.86m / equity JUMP 181.91m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>Vitaz>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Waasland patients via Vitaz VZW",
    "stated_goal": "Multi-campus hospital care",
    "measured_outcome": "Medium CW YE2025; 474.71m omzet JUMP +4.33pct with pnl JUMP +14.6pct and equity JUMP +6.9pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.45",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon vs Emmaüs/AZORG/AZ Delta continuum",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2004 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Vitaz",
    "name_fr": "Vitaz",
    "name_en": "Vitaz (Waasland hospital network)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.vitaz.be/",
    "foi_email": "info@vitaz.be",
    "foi_postal": "Moerlandstraat 1, 9100 Sint-Niklaas",
    "notes": "tick2004 YE2025 Medium CW NL+EN+FR + Strong KBO 0881.291.322 Actief VZW; omzet JUMP 474.71m pnl JUMP 12.86m equity JUMP 181.91m bruto JUMP 201.58m FTE 2227.4; assets/debt Unknown; neerlegging 24.07.2026; 9 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; AZ Monica CW N/A; do not redo Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "OostVlaanderen>Vitaz>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash)",
    "why_it_matters": "Medium CW shows 474.71m omzet Waasland hospital VZW without balance sheet",
    "priority": "7",
    "recipient_body": "Vitaz VZW",
    "recipient_email": "info@vitaz.be",
    "recipient_postal": "Moerlandstraat 1, 9100 Sint-Niklaas",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_vitaz_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_vitaz_omzet_jump_474_71m_pnl_jump_12_86m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2004; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Vitaz (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Vitaz VZW — KBO **0881.291.322**  
**recipient:** info@vitaz.be · Moerlandstraat 1, 9100 Sint-Niklaas  
**sources:** [CW NL](https://www.companyweb.be/nl/0881291322/vitaz) · [CW EN](https://www.companyweb.be/en/0881291322/vitaz) · [CW FR](https://www.companyweb.be/fr/0881291322/vitaz) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0881291322) · [site](https://www.vitaz.be/)  
**tick:** 2004  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.07.2026**): omzet **EUR474,708,586** JUMP +4.33%; pnl **EUR12,864,965** JUMP +14.61%; equity **EUR181,913,017** JUMP +6.88%; bruto **EUR201,584,911** JUMP +4.18%; FTE **2227.4**; assets/debt **Unknown**.
- Waasland VZW hospital. Preferred stall: AGB Bornem / FARO still YE2024. AZ Monica filed but CW N/A omzet. Emmaüs already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Vitaz VZW — Moerlandstraat 1, 9100 Sint-Niklaas
info@vitaz.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Vitaz + balans (KBO 0881.291.322)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.07.2026).
2. Assets / schulden LT-ST / cash.
3. Dual vs Emmaüs / AZORG / AZ Delta indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2004":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Emmaüs — Vitaz YE2025 Medium"
        x["notes"] = (
            "tick2004 Vitaz Medium omzet JUMP 474.71m pnl JUMP 12.86m equity JUMP 181.91m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; AZ Monica CW N/A; next rq_2005; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover Vitaz YE2025 Medium CW; KBO 0881.291.322; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2005" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2005",
            "title": "leftover dual hole-fill after Vitaz",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2004 after Vitaz YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Imelda / AZ Monica if figures appear / other unused YE2025 if live). "
                "Do NOT redo Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "AZ Monica 0459.768.815 filed 04.08.2026 but CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2004 Vitaz; next every-10 2010; AZ Monica CW N/A omzet",
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
        "last_unit_id": "rq_2004",
        "ticks_completed": "2004",
        "paused": "no",
        "notes": (
            "tick2004 leftover Vitaz 0881.291.322 Medium CW (omzet JUMP 474.71m pnl JUMP 12.86m equity JUMP 181.91m bruto JUMP 201.58m FTE 2227.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; AZ Monica CW N/A; next rq_2005; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2004 - {UTC} - rq_2004 Vitaz (omzet JUMP 474.71m / pnl JUMP 12.86m / Medium)

- Unit: **rq_2004** leftover dual after **rq_2003 Emmaüs**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. AZ Monica filed **04.08.2026** but CW **N/A omzet**. Took unused leftover **Vitaz** YE2025 (KBO **0881.291.322**; Moerlandstraat 1 Sint-Niklaas; Oost-Vlaanderen **hospital VZW**). Do not redo Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR474,708,586** JUMP +4.33%; pnl **EUR12,864,965** JUMP +14.61%; equity **EUR181,913,017** JUMP +6.88%; bruto **EUR201,584,911** JUMP +4.18%; FTE **2227.4**; neerlegging **24.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 9 VE; email info@vitaz.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_vitaz); foi + draft {GAP}; rq_2004=done + rq_2005 open; loop_state ticks=2004; raw under docs/doge/data/raw/tick2004/.
- FOI: **ready not sent** (human-gated; info@vitaz.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2005 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Imelda / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
