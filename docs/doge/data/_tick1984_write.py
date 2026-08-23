# ephemeral tick1984 — CHwapi YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T23:45:00Z"
ENTITY = "vzw_chwapi"
GAP = "gap_chwapi_nbb_pdf_assets_debt_equity_drop_matrix_l5"
SRC = "src_chwapi_jr2025_cw"
SRC_EN = "src_chwapi_jr2025_cw_en"
SRC_KBO = "src_chwapi_kbo_1984"
SRC_SITE = "src_chwapi_site_1984"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1984")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHwapi YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0876107364/centre-hospitalier-de-wallonie-picarde",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1984; YE2025 omzet JUMP 337723001 pnl DROP 31036811 equity DROP 128517683 (-46pct) bruto DROP 186838358 FTE 2204; neerlegging 09.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1984/chwapi_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHwapi YE2025 statutory",
        "url": "https://www.companyweb.be/en/0876107364/centre-hospitalier-de-wallonie-picarde",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1984; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1984/chwapi_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHwapi 0876.107.364 Actief VZW Tournai",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0876107364",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1984; Actief VZW; Avenue Delmee 9 7500 Tournai; 4 VE; Aanbestedende overheid; NACE 86.101; no KBO email/web",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chwapi.be Wallonie picarde hospital",
        "url": "https://www.chwapi.be/",
        "publisher": "CHwapi",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": "tick1984; Wallonie picarde hospital VZW dual of Vivalia/HELORA",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chwapi_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "337723001",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1984; omzet JUMP 337723001 +7.75pct vs YE2024 313441650",
    },
    {
        "budget_id": "bud_chwapi_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "31036811",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1984; pnl DROP 31036811 -48.74pct vs YE2024 60544504",
    },
    {
        "budget_id": "bud_chwapi_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "128517683",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1984; equity DROP 128517683 -46.05pct vs YE2024 238200239 (~-109.7m)",
    },
    {
        "budget_id": "bud_chwapi_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "186838358",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1984; bruto DROP 186838358 -3.51pct vs YE2024 193638234",
    },
    {
        "budget_id": "bud_chwapi_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "2204",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1984; YE2025 FTE 2204 vs YE2024 2164",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chwapi_jr2025_statutory_hospital",
    "title": "CHwapi YE2025 leftover Wallonie picarde hospital dual (omzet JUMP 337.72m / equity DROP 128.52m -46pct)",
    "entity_id": ENTITY,
    "beneficiary": "Wallonie picarde patients / communes dual",
    "legal_basis": "WVV VZW / hospital care Wallonie",
    "decision_date": "2026-07-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "337723001",
    "cash_by_year": '{"2025_omzet":337723001,"2025_pnl":31036811,"2025_equity":128517683,"2025_bruto":186838358,"2025_fte":2204}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0876107364/centre-hospitalier-de-wallonie-picarde",
    "stated_goal": "General hospital care for Wallonie picarde",
    "cut_option": "Publish NBB PDF assets/debt + equity DROP ~110m recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Tournai>CHwapi>JR2025_statutory_L5",
    "notes": "tick1984; Medium CW; assets/debt Unknown; equity DROP -46pct standout; dual Vivalia/HELORA; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chwapi_omzet_jump_337_72m_equity_drop_128_52m_jr2025",
    "name": "CHwapi omzet JUMP 337.72m / equity DROP 128.52m (-46pct) / pnl DROP 31.04m (Wallonie picarde hospital YE2025)",
    "level": "L5",
    "type": "walloon_hospital_vzw_dual",
    "hierarchy_path": "Wallonie>Hainaut>Tournai>CHwapi>JR2025_statutory_L5",
    "annual_cost_eur": "337723001",
    "total_cost_eur": "128517683",
    "tco_notes": "statutory omzet JUMP 337723001 pnl DROP 31036811 equity DROP 128517683 (-46pct vs 238.2m) bruto DROP 186838358 FTE 2204; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Wallonie picarde patients via hospital VZW",
    "stated_goal": "General hospital care network",
    "measured_outcome": "Medium CW YE2025; 338m omzet with equity halved (~-110m); NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.425",
    "cut_proposal": "Publish NBB PDF assets/debt + equity DROP ~110m recon FOI; dual vs Vivalia/HELORA hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1984 leftover dual; Medium CW; equity DROP standout; TE-adjacent hospital flow not pure-waste top10; next every-10 1990",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHwapi (centre Hospitalier de Wallonie Picarde)",
    "name_fr": "CHwapi (centre Hospitalier de Wallonie Picarde)",
    "name_en": "CHwapi (Wallonie picarde hospital VZW)",
    "level": "other",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.chwapi.be/",
    "foi_email": "",
    "foi_postal": "Avenue Delmee 9, 7500 Tournai",
    "notes": "tick1984 YE2025 Medium CW NL+EN + Strong KBO 0876.107.364 Actief VZW; omzet JUMP 337.72m pnl DROP 31.04m equity DROP 128.52m (-46pct) bruto DROP 186.84m FTE 2204; assets/debt Unknown; neerlegging 09.07.2026; 4 VE; FOI gap_chwapi_nbb_pdf_assets_debt_equity_drop_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo IDETA/SPI/Vivalia/HELORA/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Hainaut>Tournai>CHwapi>NBB_PDF_assets_debt_equity_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); equity DROP ~110m (-46pct) recon; dual vs Vivalia/HELORA",
    "why_it_matters": "Medium CW shows 338m omzet hospital with equity halved without balance sheet; material restructuring opacity",
    "priority": "7",
    "recipient_body": "CHwapi",
    "recipient_email": "",
    "recipient_postal": "https://www.chwapi.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_chwapi_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chwapi_omzet_jump_337_72m_equity_drop_128_52m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1984; human-send only; Medium CW; KBO no email — route via chwapi.be; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHwapi (NBB PDF / assets-debt / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHwapi VZW — KBO **0876.107.364**  
**recipient:** CHwapi (KBO has no email; route via https://www.chwapi.be/ contact)  
**sources:** [CW NL](https://www.companyweb.be/nl/0876107364/centre-hospitalier-de-wallonie-picarde) · [CW EN](https://www.companyweb.be/en/0876107364/centre-hospitalier-de-wallonie-picarde) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0876107364) · [site](https://www.chwapi.be/)  
**tick:** 1984  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **09.07.2026**): omzet **EUR337,723,001** JUMP +7.75%; pnl **EUR31,036,811** DROP -48.74%; equity **EUR128,517,683** DROP **-46.05%** (~-109.7m vs YE2024 238.2m); bruto **EUR186,838,358** DROP -3.51%; FTE **2204**; assets/debt **Unknown**.
- Wallonie picarde hospital VZW. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHwapi — Avenue Delmee 9, 7500 Tournai
cc: SPW sante / Province Hainaut transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHwapi + balans + equity DROP recon (KBO 0876.107.364)
Geachte, op grond van decret wallon / CDLD / openbaarheid vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 09.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon equity DROP (~-110m / -46pct vs YE2024 238.2m).
4. Recon pnl DROP (-49pct vs YE2024 60.5m) vs omzet JUMP.
5. Dual vs Vivalia / HELORA indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1984":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after IDETA — CHwapi YE2025 Medium"
        x["notes"] = "tick1984 CHwapi Medium omzet JUMP 337.72m equity DROP 128.52m -46pct; FOI ready; next rq_1985; next every-10 1990"
        x["instructions"] = (
            "Completed leftover CHwapi Wallonie picarde hospital YE2025 Medium CW; KBO 0876.107.364; "
            "omzet JUMP 337723001 pnl DROP 31036811 equity DROP 128517683 bruto DROP 186838358 FTE 2204; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1985" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1985",
            "title": "leftover dual hole-fill after CHwapi",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1984 after CHwapi YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital. Do NOT redo CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1984 CHwapi; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1984",
        "ticks_completed": "1984",
        "paused": "no",
        "notes": "tick1984 leftover CHwapi 0876.107.364 Medium CW (omzet JUMP 337.72m pnl DROP 31.04m equity DROP 128.52m -46pct bruto DROP 186.84m FTE 2204; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1985; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1984 - 2026-08-23T23:45:00Z - rq_1984 CHwapi (omzet JUMP 337.72m / equity DROP 128.52m -46pct / Medium)

- Unit: **rq_1984** leftover dual after **rq_1983 IDETA**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **CHwapi** YE2025 (KBO **0876.107.364**; Avenue Delmee 9 Tournai; Wallonie picarde **hospital VZW**). Do not redo IDETA/SPI/Vivalia/HELORA/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/IPFBW.
- Found: Companyweb NL+EN YE2025 - omzet **EUR337,723,001** JUMP +7.75%; pnl **EUR31,036,811** DROP -48.74%; equity **EUR128,517,683** DROP **-46.05%** (~-109.7m vs 238.2m); bruto **EUR186,838,358** DROP -3.51%; FTE **2204**; neerlegging **09.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 4 VE; no KBO email.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_chwapi); foi + draft gap_chwapi_nbb_pdf_assets_debt_equity_drop_matrix_l5; rq_1984=done + rq_1985 open; loop_state ticks=1984.
- FOI: **ready not sent** (human-gated; route via chwapi.be).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1985 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1984" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1984")
