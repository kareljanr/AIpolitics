# ephemeral tick2012 — Sint-Andries Tielt YE2025 Medium (leftover dual after Heilig Hart Lier)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T07:25:00Z"
ENTITY = "vzw_sint_andries_tielt"
GAP = "gap_sint_andries_tielt_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_sint_andries_tielt_jr2025_cw"
SRC_EN = "src_sint_andries_tielt_jr2025_cw_en"
SRC_FR = "src_sint_andries_tielt_jr2025_cw_fr"
SRC_KBO = "src_sint_andries_tielt_kbo_2012"
SRC_SITE = "src_sint_andries_tielt_site_2012"

OMZET = "132307140"
PNL = "1192256"
EQUITY = "63965399"
BRUTO = "60750238"
FTE = "583.4"
OMZET24 = "124872198"
PNL24 = "2428881"
EQUITY24 = "63584368"
BRUTO24 = "55763323"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2012")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Sint-Andriesziekenhuis Tielt YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0408661691/sint-andriesziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2012; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 22.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2012/andries_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Sint-Andriesziekenhuis Tielt YE2025 statutory",
        "url": "https://www.companyweb.be/en/0408661691/sint-andriesziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2012; EN mirror YE2025 Medium; filed 22-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2012/andries_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Sint-Andriesziekenhuis Tielt YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0408661691/sint-andriesziekenhuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2012; FR mirror YE2025 Medium; deposés le 22-07-2026; raw docs/doge/data/raw/tick2012/andries_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Sint-Andriesziekenhuis 0408.661.691 Actief VZW Tielt",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408661691",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2012; Actief VZW since 26.07.1966; Bruggestraat 84 8700 Tielt; no KBO email; 1 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "sintandriestielt.be Sint-Andriesziekenhuis",
        "url": "https://www.sintandriestielt.be/",
        "publisher": "Sint-Andriesziekenhuis Tielt",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2012; info@sintandriestielt.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_sint_andries_tielt_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2012; omzet JUMP {OMZET} +5.95pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_sint_andries_tielt_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2012; pnl DROP {PNL} -50.91pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_sint_andries_tielt_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2012; equity JUMP {EQUITY} +0.60pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_sint_andries_tielt_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2012; bruto JUMP {BRUTO} +8.94pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_sint_andries_tielt_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2012; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_sint_andries_tielt_jr2025_statutory_hospital",
    "title": "Sint-Andries Tielt YE2025 leftover hospital dual (omzet JUMP 132.31m / pnl DROP 1.19m / equity JUMP 63.97m)",
    "entity_id": ENTITY,
    "beneficiary": "Tielt-region hospital patients / Sint-Andries",
    "legal_basis": "VZW/ASBL hospital (KBO 0408.661.691)",
    "decision_date": "2026-07-22",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0408661691/sint-andriesziekenhuis",
    "stated_goal": "Regional hospital care (Tielt)",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>Sint_Andries_Tielt>JR2025_statutory_L5",
    "notes": "tick2012; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heilig Hart Lier already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_sint_andries_tielt_omzet_jump_132_31m_pnl_drop_1_19m_equity_jump_jr2025",
    "name": "Sint-Andries Tielt omzet JUMP 132.31m / pnl DROP 1.19m / equity JUMP 63.97m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "WestVlaanderen>Sint_Andries_Tielt>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Tielt patients via Sint-Andries VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 132.31m omzet JUMP +5.95pct with pnl DROP -50.91pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP vs Lier/OLVT/Glorieux",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2012 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Sint-Andriesziekenhuis Tielt",
    "name_fr": "Sint-Andriesziekenhuis Tielt",
    "name_en": "Sint-Andries Hospital Tielt",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.sintandriestielt.be/",
    "foi_email": "info@sintandriestielt.be",
    "foi_postal": "Bruggestraat 84, 8700 Tielt",
    "notes": "tick2012 YE2025 Medium CW NL+EN+FR + Strong KBO 0408.661.691 Actief VZW; omzet JUMP 132.31m pnl DROP 1.19m equity JUMP 63.97m bruto JUMP 60.75m FTE 583.4; assets/debt Unknown; neerlegging 22.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "WestVlaanderen>Sint_Andries_Tielt>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP recon vs YE2024",
    "why_it_matters": "Medium CW shows 132.31m omzet Tielt hospital VZW with pnl DROP -51pct without balance sheet",
    "priority": "7",
    "recipient_body": "Sint-Andriesziekenhuis vzw Tielt",
    "recipient_email": "info@sintandriestielt.be",
    "recipient_postal": "Bruggestraat 84, 8700 Tielt",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_sint_andries_tielt_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_sint_andries_tielt_omzet_jump_132_31m_pnl_drop_1_19m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2012; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Sint-Andries Tielt (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sint-Andriesziekenhuis vzw — KBO **0408.661.691**  
**recipient:** info@sintandriestielt.be · Bruggestraat 84, 8700 Tielt  
**sources:** [CW NL](https://www.companyweb.be/nl/0408661691/sint-andriesziekenhuis) · [CW EN](https://www.companyweb.be/en/0408661691/sint-andriesziekenhuis) · [CW FR](https://www.companyweb.be/fr/0408661691/sint-andriesziekenhuis) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408661691) · [site](https://www.sintandriestielt.be/)  
**tick:** 2012  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **22.07.2026**): omzet **EUR132,307,140** JUMP +5.95%; pnl **EUR1,192,256** DROP −50.91%; equity **EUR63,965,399** JUMP +0.60%; bruto **EUR60,750,238** JUMP +8.94%; FTE **583.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Heilig Hart Lier already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Sint-Andriesziekenhuis vzw — Bruggestraat 84, 8700 Tielt
info@sintandriestielt.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint-Andries Tielt + balans (KBO 0408.661.691)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 22.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (EUR1.192.256 vs YE2024 EUR2.428.881; −50,91pct).
4. Dual vs Heilig Hart Lier / OLVT indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2012":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Heilig Hart Lier — Sint-Andries Tielt YE2025 Medium"
        x["notes"] = (
            "tick2012 Sint-Andries Tielt Medium omzet JUMP 132.31m pnl DROP 1.19m equity JUMP 63.97m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2013; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover Sint-Andries Tielt YE2025 Medium CW; KBO 0408.661.691; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2013" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2013",
            "title": "leftover dual hole-fill after Sint-Andries Tielt",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2012 after Sint-Andries Tielt YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Sint-Trudo / Heilig Hart Leuven / Vesalius / AZ Sint-Jan Brugge if omzet appears / other unused YE2025 if live). "
                "Do NOT redo Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2012 Sint-Andries Tielt; next every-10 2020; AGB/FARO/AIESH/REW still YE2024",
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
        "last_unit_id": "rq_2012",
        "ticks_completed": "2012",
        "paused": "no",
        "notes": (
            "tick2012 leftover Sint-Andries Tielt 0408.661.691 Medium CW (omzet JUMP 132.31m pnl DROP 1.19m equity JUMP 63.97m bruto JUMP 60.75m FTE 583.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2013; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2012 - {UTC} - rq_2012 Sint-Andries Tielt (omzet JUMP 132.31m / pnl DROP 1.19m / Medium)

- Unit: **rq_2012** leftover dual after **rq_2011 Heilig Hart Lier**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Sint-Andriesziekenhuis Tielt** YE2025 (KBO **0408.661.691**; Bruggestraat 84 Tielt; West-Vlaanderen **hospital VZW**). Do not redo Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR132,307,140** JUMP +5.95%; pnl **EUR1,192,256** DROP −50.91%; equity **EUR63,965,399** JUMP +0.60%; bruto **EUR60,750,238** JUMP +8.94%; FTE **583.4**; neerlegging **22.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@sintandriestielt.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_sint_andries_tielt); foi + draft {GAP}; rq_2012=done + rq_2013 open; loop_state ticks=2012; raw under docs/doge/data/raw/tick2012/.
- FOI: **ready not sent** (human-gated; info@sintandriestielt.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2013 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Trudo-HH Leuven-Vesalius / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
