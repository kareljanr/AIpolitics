# ephemeral tick2005 — AZ St.-Elisabeth Herentals YE2025 Medium (leftover dual after Vitaz)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T05:25:00Z"
ENTITY = "vzw_az_st_eli_herentals"
GAP = "gap_az_st_eli_herentals_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_az_st_eli_herentals_jr2025_cw"
SRC_EN = "src_az_st_eli_herentals_jr2025_cw_en"
SRC_FR = "src_az_st_eli_herentals_jr2025_cw_fr"
SRC_KBO = "src_az_st_eli_herentals_kbo_2005"
SRC_SITE = "src_az_st_eli_herentals_site_2005"

OMZET = "171666951"
PNL = "2774462"
EQUITY = "54818543"
BRUTO = "69923624"
FTE = "719.2"
OMZET24 = "164011503"
PNL24 = "3414964"
EQUITY24 = "52921180"
BRUTO24 = "67251299"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2005")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ St.-Elisabeth Herentals YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0821734213/az-st-elisabeth-herentals-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2005; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2005/herentals_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ St.-Elisabeth Herentals YE2025 statutory",
        "url": "https://www.companyweb.be/en/0821734213/az-st-elisabeth-herentals-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2005; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2005/herentals_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ St.-Elisabeth Herentals YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0821734213/az-st-elisabeth-herentals-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2005; FR mirror YE2025 Medium; deposés le 03-07-2026; raw docs/doge/data/raw/tick2005/herentals_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ St.-Elisabeth Herentals 0821.734.213 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0821734213",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2005; Actief VZW since 30.11.2009; AZ St.-Elisabeth Herentals; Nederrij 133 2200 Herentals; no KBO email; 1 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azherentals.be AZ St.-Elisabeth Herentals",
        "url": "https://www.azherentals.be/",
        "publisher": "AZ St.-Elisabeth Herentals",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2005; Herentals hospital; contact via azherentals.be / 014 24 61 11",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_st_eli_herentals_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2005; omzet JUMP {OMZET} +4.67pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_az_st_eli_herentals_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2005; pnl DROP {PNL} -18.76pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_az_st_eli_herentals_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2005; equity JUMP {EQUITY} +3.59pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_az_st_eli_herentals_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2005; bruto JUMP {BRUTO} +3.97pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_az_st_eli_herentals_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2005; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_st_eli_herentals_jr2025_statutory_hospital",
    "title": "AZ St.-Elisabeth Herentals YE2025 leftover hospital dual (omzet JUMP 171.67m / pnl DROP 2.77m / equity JUMP 54.82m)",
    "entity_id": ENTITY,
    "beneficiary": "Herentals-region hospital patients / AZ St.-Elisabeth Herentals",
    "legal_basis": "VZW/ASBL hospital (KBO 0821.734.213)",
    "decision_date": "2026-07-03",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0821734213/az-st-elisabeth-herentals-vzw",
    "stated_goal": "Regional hospital care (Herentals)",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>AZ_StEli_Herentals>JR2025_statutory_L5",
    "notes": "tick2005; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AZ Imelda/Monica CW N/A omzet; Vitaz already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.5 + 0.10*4.0 = 5.35
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_st_eli_herentals_omzet_jump_171_67m_pnl_drop_2_77m_equity_jump_jr2025",
    "name": "AZ St.-Elisabeth Herentals omzet JUMP 171.67m / pnl DROP 2.77m / equity JUMP 54.82m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "Antwerpen>AZ_StEli_Herentals>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Herentals patients via AZ St.-Elisabeth VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 171.67m omzet JUMP +4.67pct with pnl DROP -18.8pct and equity JUMP +3.6pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP path vs Vitaz/Emmaüs/AZORG",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2005 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ St.-Elisabeth Herentals",
    "name_fr": "AZ St.-Elisabeth Herentals",
    "name_en": "AZ St.-Elisabeth Herentals",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.azherentals.be/",
    "foi_email": "",
    "foi_postal": "Nederrij 133, 2200 Herentals",
    "notes": "tick2005 YE2025 Medium CW NL+EN+FR + Strong KBO 0821.734.213 Actief VZW; omzet JUMP 171.67m pnl DROP 2.77m equity JUMP 54.82m bruto JUMP 69.92m FTE 719.2; assets/debt Unknown; neerlegging 03.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; AZ Imelda/Monica CW N/A; do not redo Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>AZ_StEli_Herentals>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP recon vs YE2024",
    "why_it_matters": "Medium CW shows 171.67m omzet Herentals hospital VZW with pnl DROP -19pct without balance sheet",
    "priority": "7",
    "recipient_body": "AZ St.-Elisabeth Herentals VZW",
    "recipient_email": "",
    "recipient_postal": "Nederrij 133, 2200 Herentals",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_st_eli_herentals_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_st_eli_herentals_omzet_jump_171_67m_pnl_drop_2_77m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2005; human-send only; Medium CW; route via azherentals.be; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ St.-Elisabeth Herentals (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AZ St.-Elisabeth Herentals VZW — KBO **0821.734.213**  
**recipient:** route via azherentals.be · Nederrij 133, 2200 Herentals · 014 24 61 11  
**sources:** [CW NL](https://www.companyweb.be/nl/0821734213/az-st-elisabeth-herentals-vzw) · [CW EN](https://www.companyweb.be/en/0821734213/az-st-elisabeth-herentals-vzw) · [CW FR](https://www.companyweb.be/fr/0821734213/az-st-elisabeth-herentals-vzw) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0821734213) · [site](https://www.azherentals.be/)  
**tick:** 2005  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **03.07.2026**): omzet **EUR171,666,951** JUMP +4.67%; pnl **EUR2,774,462** DROP −18.76%; equity **EUR54,818,543** JUMP +3.59%; bruto **EUR69,923,624** JUMP +3.97%; FTE **719.2**; assets/debt **Unknown**.
- Herentals VZW hospital. Preferred stall: AGB Bornem / FARO still YE2024. AZ Imelda/Monica CW N/A omzet. Vitaz already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: AZ St.-Elisabeth Herentals VZW — Nederrij 133, 2200 Herentals
via azherentals.be openbaarheid / contact
cc: Agentschap Zorg en Gezondheid / Provincie Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZ St.-Elisabeth Herentals + balans (KBO 0821.734.213)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 03.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (EUR2.774.462 vs YE2024 EUR3.414.964; −18,76pct).
4. Dual vs Vitaz / Emmaüs indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2005":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Vitaz — AZ St.-Elisabeth Herentals YE2025 Medium"
        x["notes"] = (
            "tick2005 AZ St.-Elisabeth Herentals Medium omzet JUMP 171.67m pnl DROP 2.77m equity JUMP 54.82m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; AZ Imelda/Monica CW N/A; next rq_2006; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover AZ St.-Elisabeth Herentals YE2025 Medium CW; KBO 0821.734.213; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2006" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2006",
            "title": "leftover dual hole-fill after AZ St.-Elisabeth Herentals",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2005 after AZ St.-Elisabeth Herentals YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Maria Middelares / AZ Alma / AZ Imelda if figures appear / other unused YE2025 if live). "
                "Do NOT redo AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "AZ Imelda/Monica CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2005 AZ St.-Elisabeth Herentals; next every-10 2010",
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
        "last_unit_id": "rq_2005",
        "ticks_completed": "2005",
        "paused": "no",
        "notes": (
            "tick2005 leftover AZ St.-Elisabeth Herentals 0821.734.213 Medium CW (omzet JUMP 171.67m pnl DROP 2.77m equity JUMP 54.82m bruto JUMP 69.92m FTE 719.2; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; AZ Imelda/Monica CW N/A; next rq_2006; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2005 - {UTC} - rq_2005 AZ St.-Elisabeth Herentals (omzet JUMP 171.67m / pnl DROP 2.77m / Medium)

- Unit: **rq_2005** leftover dual after **rq_2004 Vitaz**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. AZ Imelda/Monica CW **N/A omzet**. Took unused leftover **AZ St.-Elisabeth Herentals** YE2025 (KBO **0821.734.213**; Nederrij 133 Herentals; Antwerpen **hospital VZW**). Do not redo Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR171,666,951** JUMP +4.67%; pnl **EUR2,774,462** DROP −18.76%; equity **EUR54,818,543** JUMP +3.59%; bruto **EUR69,923,624** JUMP +3.97%; FTE **719.2**; neerlegging **03.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; no KBO email (route via azherentals.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_st_eli_herentals); foi + draft {GAP}; rq_2005=done + rq_2006 open; loop_state ticks=2005; raw under docs/doge/data/raw/tick2005/.
- FOI: **ready not sent** (human-gated; route via azherentals.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2006 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Maria Middelares-Alma / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
