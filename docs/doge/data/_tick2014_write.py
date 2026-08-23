# ephemeral tick2014 — Heilig Hart Leuven YE2025 Medium (leftover dual after Sint-Trudo)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T07:55:00Z"
ENTITY = "vzw_heilig_hart_leuven"
GAP = "gap_heilig_hart_leuven_nbb_pdf_assets_debt_pnl_collapse_matrix_l5"
SRC = "src_heilig_hart_leuven_jr2025_cw"
SRC_EN = "src_heilig_hart_leuven_jr2025_cw_en"
SRC_FR = "src_heilig_hart_leuven_jr2025_cw_fr"
SRC_KBO = "src_heilig_hart_leuven_kbo_2014"
SRC_SITE = "src_heilig_hart_leuven_site_2014"

OMZET = "118726370"
PNL = "8990"
EQUITY = "46843891"
BRUTO = "59136126"
FTE = "626.7"
OMZET24 = "112710535"
PNL24 = "3854490"
EQUITY24 = "47372337"
BRUTO24 = "56786211"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2014")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Heilig Hart Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0412939886",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2014; YE2025 omzet JUMP {OMZET} pnl COLLAPSE {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2014/hhleuven_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Heilig Hart Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/en/0412939886",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2014; EN mirror YE2025 Medium; filed 10-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2014/hhleuven_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Heilig Hart Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0412939886",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2014; FR mirror YE2025 Medium; deposés le 10-07-2026; raw docs/doge/data/raw/tick2014/hhleuven_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Regionaal Ziekenhuis Heilig Hart Leuven 0412.939.886 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412939886",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2014; Actief VZW since 22.01.1973; Naamsestraat 105 3000 Leuven; no KBO email; 1 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "hhleuven.be Heilig Hart Leuven",
        "url": "https://www.hhleuven.be/",
        "publisher": "Heilig Hart Leuven",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2014; info@hhleuven.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_heilig_hart_leuven_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2014; omzet JUMP {OMZET} +5.34pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_heilig_hart_leuven_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2014; pnl COLLAPSE {PNL} -99.77pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_heilig_hart_leuven_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2014; equity DROP {EQUITY} -1.12pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_heilig_hart_leuven_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2014; bruto JUMP {BRUTO} +4.14pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_heilig_hart_leuven_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2014; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_heilig_hart_leuven_jr2025_statutory_hospital",
    "title": "Heilig Hart Leuven YE2025 leftover hospital dual (omzet JUMP 118.73m / pnl COLLAPSE 9k / equity DROP 46.84m)",
    "entity_id": ENTITY,
    "beneficiary": "Leuven-region hospital patients / Heilig Hart Leuven",
    "legal_basis": "VZW/ASBL hospital (KBO 0412.939.886)",
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0412939886",
    "stated_goal": "Regional hospital care (Leuven)",
    "cut_option": "Publish NBB PDF assets/debt + pnl collapse recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Leuven>JR2025_statutory_L5",
    "notes": "tick2014; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AZ Zeno CW year-label opaque deferred; Sint-Trudo already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_heilig_hart_leuven_omzet_jump_118_73m_pnl_collapse_9k_equity_drop_jr2025",
    "name": "Heilig Hart Leuven omzet JUMP 118.73m / pnl COLLAPSE 9k / equity DROP 46.84m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Leuven>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl COLLAPSE {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Leuven patients via Heilig Hart Leuven VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 118.73m omzet JUMP +5.34pct with pnl COLLAPSE -99.77pct to EUR8990; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.525",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl collapse path vs YE2024 EUR3.85m",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2014 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Regionaal Ziekenhuis Heilig Hart Leuven",
    "name_fr": "Regionaal Ziekenhuis Heilig Hart Leuven",
    "name_en": "Heilig Hart Hospital Leuven",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.hhleuven.be/",
    "foi_email": "info@hhleuven.be",
    "foi_postal": "Naamsestraat 105, 3000 Leuven",
    "notes": "tick2014 YE2025 Medium CW NL+EN+FR + Strong KBO 0412.939.886 Actief VZW; omzet JUMP 118.73m pnl COLLAPSE 9k equity DROP 46.84m bruto JUMP 59.14m FTE 626.7; assets/debt Unknown; neerlegging 10.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; do not redo Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "VlaamsBrabant>Heilig_Hart_Leuven>NBB_PDF_assets_debt_pnl_collapse",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl collapse recon vs YE2024",
    "why_it_matters": "Medium CW shows 118.73m omzet Leuven hospital VZW with pnl collapse to EUR8990 (-99.77pct) without balance sheet",
    "priority": "7",
    "recipient_body": "Regionaal Ziekenhuis Heilig Hart Leuven vzw",
    "recipient_email": "info@hhleuven.be",
    "recipient_postal": "Naamsestraat 105, 3000 Leuven",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_heilig_hart_leuven_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_heilig_hart_leuven_omzet_jump_118_73m_pnl_collapse_9k_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2014; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Heilig Hart Leuven (NBB PDF / assets-debt / pnl COLLAPSE)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Regionaal Ziekenhuis Heilig Hart Leuven vzw — KBO **0412.939.886**  
**recipient:** info@hhleuven.be · Naamsestraat 105, 3000 Leuven  
**sources:** [CW NL](https://www.companyweb.be/nl/0412939886) · [CW EN](https://www.companyweb.be/en/0412939886) · [CW FR](https://www.companyweb.be/fr/0412939886) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412939886) · [site](https://www.hhleuven.be/)  
**tick:** 2014  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.07.2026**): omzet **EUR118,726,370** JUMP +5.34%; pnl **EUR8,990** COLLAPSE −99.77% (vs YE2024 EUR3,854,490); equity **EUR46,843,891** DROP −1.12%; bruto **EUR59,136,126** JUMP +4.14%; FTE **626.7**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024. Sint-Trudo already mined. AZ Zeno CW year-label opaque deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Regionaal Ziekenhuis Heilig Hart Leuven vzw — Naamsestraat 105, 3000 Leuven
info@hhleuven.be
cc: Agentschap Zorg en Gezondheid / Provincie Vlaams-Brabant indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Heilig Hart Leuven + balans (KBO 0412.939.886)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl COLLAPSE (EUR8.990 vs YE2024 EUR3.854.490; −99,77pct).
4. Dual vs Sint-Trudo / Z.org KU Leuven indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2014":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Sint-Trudo — Heilig Hart Leuven YE2025 Medium"
        x["notes"] = (
            "tick2014 Heilig Hart Leuven Medium omzet JUMP 118.73m pnl COLLAPSE 9k equity DROP 46.84m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; AZ Zeno deferred; next rq_2015; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover Heilig Hart Leuven YE2025 Medium CW; KBO 0412.939.886; "
            f"omzet JUMP {OMZET} pnl COLLAPSE {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2015" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2015",
            "title": "leftover dual hole-fill after Heilig Hart Leuven",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2014 after Heilig Hart Leuven YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Zeno if YE2025 figures clarified / Vesalius / other unused YE2025 if live). "
                "Do NOT redo Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2014 Heilig Hart Leuven; next every-10 2020; AZ Zeno CW year-label opaque",
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
        "last_unit_id": "rq_2014",
        "ticks_completed": "2014",
        "paused": "no",
        "notes": (
            "tick2014 leftover Heilig Hart Leuven 0412.939.886 Medium CW (omzet JUMP 118.73m pnl COLLAPSE 9k equity DROP 46.84m bruto JUMP 59.14m FTE 626.7; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; AZ Zeno deferred; next rq_2015; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2014 - {UTC} - rq_2014 Heilig Hart Leuven (omzet JUMP 118.73m / pnl COLLAPSE 9k / Medium)

- Unit: **rq_2014** leftover dual after **rq_2013 Sint-Trudo**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Took deferred leftover **Heilig Hart Leuven** YE2025 (KBO **0412.939.886**; Naamsestraat 105 Leuven; Vlaams-Brabant **hospital VZW**). AZ Zeno CW year-label opaque deferred. Do not redo Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR118,726,370** JUMP +5.34%; pnl **EUR8,990** COLLAPSE −99.77%; equity **EUR46,843,891** DROP −1.12%; bruto **EUR59,136,126** JUMP +4.14%; FTE **626.7**; neerlegging **10.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@hhleuven.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_heilig_hart_leuven); foi + draft {GAP}; rq_2014=done + rq_2015 open; loop_state ticks=2014; raw under docs/doge/data/raw/tick2014/.
- FOI: **ready not sent** (human-gated; info@hhleuven.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2015 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Zeno-Vesalius / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
