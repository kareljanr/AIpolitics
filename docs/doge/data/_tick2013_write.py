# ephemeral tick2013 — Sint-Trudo YE2025 Medium (leftover dual after Sint-Andries Tielt)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T07:40:00Z"
ENTITY = "vzw_sint_trudo"
GAP = "gap_sint_trudo_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_sint_trudo_jr2025_cw"
SRC_EN = "src_sint_trudo_jr2025_cw_en"
SRC_FR = "src_sint_trudo_jr2025_cw_fr"
SRC_KBO = "src_sint_trudo_kbo_2013"
SRC_SITE = "src_sint_trudo_site_2013"

OMZET = "181318718"
PNL = "2049232"
EQUITY = "67783254"
BRUTO = "75425136"
FTE = "780"
OMZET24 = "169109219"
PNL24 = "2120841"
EQUITY24 = "66616688"
BRUTO24 = "71173754"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2013")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Sint-Trudo Ziekenhuis YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0443260603/sint-trudo-ziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2013; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2013/trudo_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Sint-Trudo Ziekenhuis YE2025 statutory",
        "url": "https://www.companyweb.be/en/0443260603/sint-trudo-ziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2013; EN mirror YE2025 Medium; filed 01-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2013/trudo_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Sint-Trudo Ziekenhuis YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0443260603/sint-trudo-ziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2013; FR mirror YE2025 Medium; deposés le 01-07-2026; raw docs/doge/data/raw/tick2013/trudo_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Sint-Trudo Ziekenhuis 0443.260.603 Actief VZW Sint-Truiden",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443260603",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2013; Actief VZW since 21.06.1990; Diestersteenweg 100 3800 Sint-Truiden; no KBO email; 2 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "sint-trudo.be Sint-Trudo Ziekenhuis",
        "url": "https://www.sint-trudo.be/nl",
        "publisher": "Sint-Trudo Ziekenhuis",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2013; info@stzh.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_sint_trudo_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2013; omzet JUMP {OMZET} +7.22pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_sint_trudo_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2013; pnl DROP {PNL} -3.38pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_sint_trudo_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2013; equity JUMP {EQUITY} +1.75pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_sint_trudo_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2013; bruto JUMP {BRUTO} +5.97pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_sint_trudo_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2013; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_sint_trudo_jr2025_statutory_hospital",
    "title": "Sint-Trudo YE2025 leftover hospital dual (omzet JUMP 181.32m / pnl DROP 2.05m / equity JUMP 67.78m)",
    "entity_id": ENTITY,
    "beneficiary": "Sint-Truiden-region hospital patients / Sint-Trudo",
    "legal_basis": "VZW/ASBL hospital (KBO 0443.260.603)",
    "decision_date": "2026-07-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0443260603/sint-trudo-ziekenhuis",
    "stated_goal": "Regional hospital care (Sint-Truiden)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Limburg>Sint_Trudo>JR2025_statutory_L5",
    "notes": "tick2013; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; HH Leuven YE2025 deferred; Sint-Andries already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_sint_trudo_omzet_jump_181_32m_pnl_drop_2_05m_equity_jump_jr2025",
    "name": "Sint-Trudo omzet JUMP 181.32m / pnl DROP 2.05m / equity JUMP 67.78m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "Limburg>Sint_Trudo>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Sint-Truiden patients via Sint-Trudo VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 181.32m omzet JUMP +7.22pct with mild pnl DROP -3.38pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon vs Sint-Andries/Lier/OLVT",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2013 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Sint-Trudo Ziekenhuis",
    "name_fr": "Sint-Trudo Ziekenhuis",
    "name_en": "Sint-Trudo Hospital (Sint-Truiden)",
    "level": "asbl",
    "parent_id": "prov_limburg",
    "community_language": "nl",
    "website": "https://www.sint-trudo.be/",
    "foi_email": "info@stzh.be",
    "foi_postal": "Diestersteenweg 100, 3800 Sint-Truiden",
    "notes": "tick2013 YE2025 Medium CW NL+EN+FR + Strong KBO 0443.260.603 Actief VZW; omzet JUMP 181.32m pnl DROP 2.05m equity JUMP 67.78m bruto JUMP 75.43m FTE 780; assets/debt Unknown; neerlegging 01.07.2026; 2 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; HH Leuven YE2025 deferred; do not redo Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Limburg>Sint_Trudo>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash)",
    "why_it_matters": "Medium CW shows 181.32m omzet Limburg hospital VZW without balance sheet",
    "priority": "7",
    "recipient_body": "Sint-Trudo Ziekenhuis vzw",
    "recipient_email": "info@stzh.be",
    "recipient_postal": "Diestersteenweg 100, 3800 Sint-Truiden",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_sint_trudo_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_sint_trudo_omzet_jump_181_32m_pnl_drop_2_05m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2013; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Sint-Trudo (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sint-Trudo Ziekenhuis vzw — KBO **0443.260.603**  
**recipient:** info@stzh.be · Diestersteenweg 100, 3800 Sint-Truiden  
**sources:** [CW NL](https://www.companyweb.be/nl/0443260603/sint-trudo-ziekenhuis) · [CW EN](https://www.companyweb.be/en/0443260603/sint-trudo-ziekenhuis) · [CW FR](https://www.companyweb.be/fr/0443260603/sint-trudo-ziekenhuis) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443260603) · [site](https://www.sint-trudo.be/)  
**tick:** 2013  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **01.07.2026**): omzet **EUR181,318,718** JUMP +7.22%; pnl **EUR2,049,232** DROP −3.38%; equity **EUR67,783,254** JUMP +1.75%; bruto **EUR75,425,136** JUMP +5.97%; FTE **780**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024. HH Leuven YE2025 deferred. Sint-Andries already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Sint-Trudo Ziekenhuis vzw — Diestersteenweg 100, 3800 Sint-Truiden
info@stzh.be
cc: Agentschap Zorg en Gezondheid / Provincie Limburg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint-Trudo + balans (KBO 0443.260.603)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 01.07.2026).
2. Assets / schulden LT-ST / cash.
3. Dual vs Sint-Andries / Heilig Hart Lier indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2013":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Sint-Andries Tielt — Sint-Trudo YE2025 Medium"
        x["notes"] = (
            "tick2013 Sint-Trudo Medium omzet JUMP 181.32m pnl DROP 2.05m equity JUMP 67.78m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; HH Leuven YE2025 deferred; next rq_2014; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover Sint-Trudo YE2025 Medium CW; KBO 0443.260.603; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2014" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2014",
            "title": "leftover dual hole-fill after Sint-Trudo",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2013 after Sint-Trudo YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Heilig Hart Leuven YE2025 live deferred / AZ Zeno / Vesalius / other unused YE2025 if live). "
                "Do NOT redo Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2013 Sint-Trudo; next every-10 2020; HH Leuven YE2025 deferred",
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
        "last_unit_id": "rq_2013",
        "ticks_completed": "2013",
        "paused": "no",
        "notes": (
            "tick2013 leftover Sint-Trudo 0443.260.603 Medium CW (omzet JUMP 181.32m pnl DROP 2.05m equity JUMP 67.78m bruto JUMP 75.43m FTE 780; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; HH Leuven YE2025 deferred; next rq_2014; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2013 - {UTC} - rq_2013 Sint-Trudo (omzet JUMP 181.32m / pnl DROP 2.05m / Medium)

- Unit: **rq_2013** leftover dual after **rq_2012 Sint-Andries Tielt**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Took preferred leftover **Sint-Trudo** YE2025 (KBO **0443.260.603**; Diestersteenweg 100 Sint-Truiden; Limburg **hospital VZW**). **Heilig Hart Leuven** YE2025 also live deferred. Do not redo Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR181,318,718** JUMP +7.22%; pnl **EUR2,049,232** DROP −3.38%; equity **EUR67,783,254** JUMP +1.75%; bruto **EUR75,425,136** JUMP +5.97%; FTE **780**; neerlegging **01.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 2 VE; email info@stzh.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_sint_trudo); foi + draft {GAP}; rq_2013=done + rq_2014 open; loop_state ticks=2013; raw under docs/doge/data/raw/tick2013/.
- FOI: **ready not sent** (human-gated; info@stzh.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2014 (AGB/FARO-if-YE2025 / AIESH-REW / HH Leuven-AZ Zeno / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
