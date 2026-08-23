# ephemeral tick1999 — AZJP YE2025 Medium (leftover dual after ZAS)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T03:20:00Z"
ENTITY = "vzw_azjp"
GAP = "gap_azjp_nbb_pdf_assets_debt_pnl_loss_equity_drop_matrix_l5"
SRC = "src_azjp_jr2025_cw"
SRC_EN = "src_azjp_jr2025_cw_en"
SRC_FR = "src_azjp_jr2025_cw_fr"
SRC_KBO = "src_azjp_kbo_1999"
SRC_SITE = "src_azjp_site_1999"

OMZET = "126326443"
PNL = "-814870"
EQUITY = "43356483"
BRUTO = "55640098"
FTE = "625.7"
OMZET24 = "124592525"
PNL24 = "1224794"
EQUITY24 = "44173608"
BRUTO24 = "54189104"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1999")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZJP YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0267386438/algemeen-ziekenhuis-jan-portaels",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1999; YE2025 omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 15.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1999/azjp_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZJP YE2025 statutory",
        "url": "https://www.companyweb.be/en/0267386438/algemeen-ziekenhuis-jan-portaels",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1999; EN mirror YE2025 Medium; filed 15-07-2026; raw docs/doge/data/raw/tick1999/azjp_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZJP YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0267386438/algemeen-ziekenhuis-jan-portaels",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1999; FR mirror YE2025 Medium; deposés le 15-07-2026; raw docs/doge/data/raw/tick1999/azjp_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZJP 0267.386.438 Actief VZW Vilvoorde",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0267386438",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1999; Actief VZW since 18.12.2001; Algemeen Ziekenhuis Jan Portaels; Gendarmeriestraat 65 1800 Vilvoorde; no KBO email; 4 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azjanportaels.be AZ Jan Portaels",
        "url": "https://www.azjanportaels.be/",
        "publisher": "AZJP",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1999; Vilvoorde hospital; info@azjanportaels.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_azjp_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1999; omzet JUMP {OMZET} +1.39pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_azjp_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1999; pnl LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_azjp_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1999; equity DROP {EQUITY} -1.85pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_azjp_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1999; bruto JUMP {BRUTO} +2.68pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_azjp_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1999; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_azjp_jr2025_statutory_hospital",
    "title": "AZJP YE2025 leftover hospital dual (omzet JUMP 126.33m / pnl LOSS 0.81m / equity DROP 43.36m)",
    "entity_id": ENTITY,
    "beneficiary": "Vilvoorde hospital patients / Algemeen Ziekenhuis Jan Portaels",
    "legal_basis": "VZW/ASBL hospital (KBO 0267.386.438)",
    "decision_date": "2026-07-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0267386438/algemeen-ziekenhuis-jan-portaels",
    "stated_goal": "General hospital care (Vilvoorde / Jan Portaels)",
    "cut_option": "Publish NBB PDF assets/debt + pnl LOSS / equity DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>AZJP_Vilvoorde>JR2025_statutory_L5",
    "notes": "tick1999; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; ZAS already mined; AZ Groeninge CW N/A omzet",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*6.0 + 0.10*4.0 = 3.025+2.1+0.4 = 5.525
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_azjp_omzet_jump_126_33m_pnl_loss_0_81m_equity_drop_jr2025",
    "name": "AZJP omzet JUMP 126.33m / pnl LOSS 0.81m / equity DROP 43.36m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>AZJP_Vilvoorde>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Vilvoorde hospital patients via AZJP VZW",
    "stated_goal": "General hospital care",
    "measured_outcome": "Medium CW YE2025; 126.33m omzet with pnl LOSS turnaround from YE2024 profit and equity DROP -1.85pct; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.525",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl LOSS + equity DROP path vs ZAS/Haute Senne/CNDG",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1999 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZJP / Algemeen Ziekenhuis Jan Portaels",
    "name_fr": "AZJP / Algemeen Ziekenhuis Jan Portaels",
    "name_en": "AZJP / Algemeen Ziekenhuis Jan Portaels (Vilvoorde)",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.azjanportaels.be/",
    "foi_email": "info@azjanportaels.be",
    "foi_postal": "Gendarmeriestraat 65, 1800 Vilvoorde",
    "notes": "tick1999 YE2025 Medium CW NL+EN+FR + Strong KBO 0267.386.438 Actief VZW; omzet JUMP 126.33m pnl LOSS 0.81m equity DROP 43.36m bruto JUMP 55.64m FTE 625.7; assets/debt Unknown; neerlegging 15.07.2026; 4 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; do not redo ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "VlaamsBrabant>AZJP_Vilvoorde>NBB_PDF_assets_debt_pnl_loss_equity_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS recon vs YE2024 profit; equity DROP recon",
    "why_it_matters": "Medium CW shows 126.33m omzet Vilvoorde hospital VZW with pnl LOSS turnaround and equity DROP without balance sheet",
    "priority": "7",
    "recipient_body": "Algemeen Ziekenhuis Jan Portaels VZW / AZJP",
    "recipient_email": "info@azjanportaels.be",
    "recipient_postal": "Gendarmeriestraat 65, 1800 Vilvoorde",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_azjp_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_azjp_omzet_jump_126_33m_pnl_loss_0_81m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1999; human-send only; Medium CW; next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZJP (NBB PDF / assets-debt / pnl LOSS / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Algemeen Ziekenhuis Jan Portaels VZW / AZJP — KBO **0267.386.438**  
**recipient:** info@azjanportaels.be · Gendarmeriestraat 65, 1800 Vilvoorde  
**sources:** [CW NL](https://www.companyweb.be/nl/0267386438/algemeen-ziekenhuis-jan-portaels) · [CW EN](https://www.companyweb.be/en/0267386438/algemeen-ziekenhuis-jan-portaels) · [CW FR](https://www.companyweb.be/fr/0267386438/algemeen-ziekenhuis-jan-portaels) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0267386438) · [site](https://www.azjanportaels.be/)  
**tick:** 1999  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **15.07.2026**): omzet **EUR126,326,443** JUMP +1.39%; pnl **LOSS EUR-814,870** (vs YE2024 profit EUR1,224,794); equity **EUR43,356,483** DROP −1.85%; bruto **EUR55,640,098** JUMP +2.68%; FTE **625.7**; assets/debt **Unknown**.
- Vilvoorde VZW hospital. Preferred stall: AGB Bornem / FARO still YE2024. ZAS already mined. AZ Groeninge CW N/A omzet.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Algemeen Ziekenhuis Jan Portaels VZW / AZJP — Gendarmeriestraat 65, 1800 Vilvoorde
info@azjanportaels.be
cc: Agentschap Zorg en Gezondheid / Provincie Vlaams-Brabant indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZJP + balans (KBO 0267.386.438)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 15.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS (EUR-814.870 vs YE2024 winst EUR1.224.794) en equity DROP (−1,85pct).
4. Dual vs ZAS / regionale VL ziekenhuizen indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1999":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after ZAS — AZJP YE2025 Medium"
        x["notes"] = (
            "tick1999 AZJP Medium omzet JUMP 126.33m pnl LOSS 0.81m equity DROP 43.36m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; AZ Groeninge CW N/A; next rq_2000 EVERY-10; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover AZJP YE2025 Medium CW; KBO 0267.386.438; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2000" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2000",
            "title": "EVERY-10 + leftover dual hole-fill after AZJP",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1999 after AZJP YE2025 Medium. MUST do every-10 refresh of progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Groeninge if YE2025 figures live / other unused). "
                "Do NOT redo AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1999 AZJP; EVERY-10 mandatory at 2000; AZ Groeninge CW N/A omzet as of 1999",
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
        "last_unit_id": "rq_1999",
        "ticks_completed": "1999",
        "paused": "no",
        "notes": (
            "tick1999 leftover AZJP 0267.386.438 Medium CW (omzet JUMP 126.33m pnl LOSS 0.81m equity DROP 43.36m bruto JUMP 55.64m FTE 625.7; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; next rq_2000 EVERY-10; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1999 - {UTC} - rq_1999 AZJP (omzet JUMP 126.33m / pnl LOSS 0.81m / Medium)

- Unit: **rq_1999** leftover dual after **rq_1998 ZAS**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Took deferred leftover **AZJP** YE2025 (KBO **0267.386.438**; Gendarmeriestraat 65 Vilvoorde; Vlaams-Brabant **hospital VZW**). AZ Groeninge CW N/A omzet. Do not redo ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR126,326,443** JUMP +1.39%; pnl **LOSS EUR-814,870** (vs YE2024 profit 1.22m); equity **EUR43,356,483** DROP −1.85%; bruto **EUR55,640,098** JUMP +2.68%; FTE **625.7**; neerlegging **15.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 4 VE; email info@azjanportaels.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_azjp); foi + draft {GAP}; rq_1999=done + rq_2000 open (EVERY-10); loop_state ticks=1999; raw under docs/doge/data/raw/tick1999/.
- FOI: **ready not sent** (human-gated; info@azjanportaels.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_2000 (EVERY-10 progress + AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
