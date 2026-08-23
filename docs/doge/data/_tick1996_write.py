# ephemeral tick1996 — CNDG YE2025 Medium (leftover dual after Haute Senne)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T02:35:00Z"
ENTITY = "vzw_cndg"
GAP = "gap_cndg_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_cndg_jr2025_cw"
SRC_EN = "src_cndg_jr2025_cw_en"
SRC_FR = "src_cndg_jr2025_cw_fr"
SRC_KBO = "src_cndg_kbo_1996"
SRC_SITE = "src_cndg_site_1996"

OMZET = "149607630"
PNL = "2075700"
EQUITY = "49691163"
BRUTO = "71781535"
FTE = "890.4"
OMZET24 = "138524066"
PNL24 = "5200110"
EQUITY24 = "47999008"
BRUTO24 = "69520849"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1996")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CNDG YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0401690559/clinique-notre-dame-de-grace",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1996; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 16.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1996/cndg_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CNDG YE2025 statutory",
        "url": "https://www.companyweb.be/en/0401690559/clinique-notre-dame-de-grace",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1996; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick1996/cndg_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR CNDG YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0401690559/clinique-notre-dame-de-grace",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1996; FR mirror YE2025 Medium; deposés le 16-06-2026; raw docs/doge/data/raw/tick1996/cndg_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CNDG 0401.690.559 Actief VZW Charleroi Gosselies",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0401690559",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1996; Actief VZW/ASBL since 21.08.1921; Clinique Notre-Dame de Grace / CNDG; Chaussee de Nivelles 212 6041 Charleroi; no KBO email; 1 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "cndg.be Clinique Notre-Dame de Grace",
        "url": "https://www.cndg.be/",
        "publisher": "CNDG",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1996; Gosselies/Charleroi hospital; RHCM network with GHdC; contact via cndg.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_cndg_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1996; omzet JUMP {OMZET} +8.00pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_cndg_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1996; pnl DROP {PNL} -60.08pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_cndg_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1996; equity JUMP {EQUITY} +3.53pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_cndg_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1996; bruto JUMP {BRUTO} +3.25pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_cndg_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1996; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_cndg_jr2025_statutory_hospital",
    "title": "CNDG YE2025 leftover hospital dual (omzet JUMP 149.61m / pnl DROP 2.08m / equity JUMP 49.69m)",
    "entity_id": ENTITY,
    "beneficiary": "Charleroi/Gosselies hospital patients / Clinique Notre-Dame de Grace",
    "legal_basis": "VZW/ASBL hospital (KBO 0401.690.559); RHCM with GHdC",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0401690559/clinique-notre-dame-de-grace",
    "stated_goal": "Hospital care Gosselies / Charleroi Metropole network",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Hainaut>CNDG_Gosselies>JR2025_statutory_L5",
    "notes": "tick1996; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Haute Senne already mined; CHR Verviers YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.5 + 0.10*4.0 = 5.35
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_cndg_omzet_jump_149_61m_pnl_drop_2_08m_equity_jump_jr2025",
    "name": "CNDG omzet JUMP 149.61m / pnl DROP 2.08m / equity JUMP 49.69m (YE2025)",
    "level": "L5",
    "type": "walloon_hospital_vzw_dual",
    "hierarchy_path": "Hainaut>CNDG_Gosselies>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Gosselies hospital patients via CNDG VZW (RHCM with GHdC)",
    "stated_goal": "Hospital care",
    "measured_outcome": "Medium CW YE2025; 149.61m omzet with pnl DROP -60pct vs YE2024; equity JUMP +3.5pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP -60pct path vs Haute Senne/GHdC/Humani",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1996 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CNDG / Clinique Notre-Dame de Grace",
    "name_fr": "CNDG / Clinique Notre-Dame de Grâce",
    "name_en": "CNDG / Clinique Notre-Dame de Grace (Gosselies hospital)",
    "level": "asbl",
    "parent_id": "prov_hainaut",
    "community_language": "fr",
    "website": "https://www.cndg.be/",
    "foi_email": "",
    "foi_postal": "Chaussee de Nivelles 212, 6041 Charleroi",
    "notes": "tick1996 YE2025 Medium CW NL+EN+FR + Strong KBO 0401.690.559 Actief VZW; omzet JUMP 149.61m pnl DROP 2.08m equity JUMP 49.69m bruto JUMP 71.78m FTE 890.4; assets/debt Unknown; neerlegging 16.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
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
    "hierarchy_path": "Hainaut>CNDG_Gosselies>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP recon vs YE2024",
    "why_it_matters": "Medium CW shows 149.61m omzet Gosselies hospital VZW with pnl DROP -60pct without balance sheet",
    "priority": "7",
    "recipient_body": "Clinique Notre-Dame de Grace ASBL / CNDG",
    "recipient_email": "",
    "recipient_postal": "Chaussee de Nivelles 212, 6041 Charleroi",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_cndg_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_cndg_omzet_jump_149_61m_pnl_drop_2_08m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1996; human-send only; Medium CW; route via cndg.be (no KBO email); next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CNDG (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Clinique Notre-Dame de Grâce ASBL / CNDG — KBO **0401.690.559**  
**recipient:** route via cndg.be (no KBO email) · Chaussée de Nivelles 212, 6041 Charleroi  
**sources:** [CW NL](https://www.companyweb.be/nl/0401690559/clinique-notre-dame-de-grace) · [CW EN](https://www.companyweb.be/en/0401690559/clinique-notre-dame-de-grace) · [CW FR](https://www.companyweb.be/fr/0401690559/clinique-notre-dame-de-grace) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0401690559) · [site](https://www.cndg.be/)  
**tick:** 1996  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **16.06.2026**): omzet **EUR149,607,630** JUMP +8.00%; pnl **EUR2,075,700** DROP −60.08% (vs YE2024 EUR5,200,110); equity **EUR49,691,163** JUMP +3.53%; bruto **EUR71,781,535** JUMP +3.25%; FTE **890.4**; assets/debt **Unknown**.
- Gosselies/Charleroi VZW hospital (RHCM with GHdC). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. Haute Senne already mined. CHR Verviers YE2025 also live deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Clinique Notre-Dame de Grâce ASBL / CNDG — Chaussée de Nivelles 212, 6041 Charleroi
via cndg.be openbaarheid / contact
cc: SPW Interieur / Province Hainaut transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 CNDG + balans (KBO 0401.690.559)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 16.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (EUR2.075.700 vs YE2024 EUR5.200.110; −60,08pct).
4. Dual vs GHdC / Haute Senne / Humani indien relevant (RHCM).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1996":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Haute Senne — CNDG YE2025 Medium"
        x["notes"] = (
            "tick1996 CNDG Medium omzet JUMP 149.61m pnl DROP 2.08m equity JUMP 49.69m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHR Verviers YE2025 deferred; next rq_1997; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover CNDG YE2025 Medium CW; KBO 0401.690.559; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1997" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1997",
            "title": "leftover dual hole-fill after CNDG",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1996 after CNDG YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (CHR Verviers 0250.893.369 if YE2025). "
                "Do NOT redo CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1996 CNDG; next every-10 2000; CHR Verviers YE2025 live deferred",
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
        "last_unit_id": "rq_1996",
        "ticks_completed": "1996",
        "paused": "no",
        "notes": (
            "tick1996 leftover CNDG 0401.690.559 Medium CW (omzet JUMP 149.61m pnl DROP 2.08m equity JUMP 49.69m bruto JUMP 71.78m FTE 890.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHR Verviers YE2025 deferred; next rq_1997; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1996 - {UTC} - rq_1996 CNDG (omzet JUMP 149.61m / pnl DROP 2.08m / Medium)

- Unit: **rq_1996** leftover dual after **rq_1995 Haute Senne**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **CNDG** YE2025 (KBO **0401.690.559**; Chaussée de Nivelles 212 Charleroi/Gosselies; Hainaut **hospital VZW**; RHCM with GHdC). **CHR Verviers** YE2025 also live deferred. Do not redo Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR149,607,630** JUMP +8.00%; pnl **EUR2,075,700** DROP −60.08%; equity **EUR49,691,163** JUMP +3.53%; bruto **EUR71,781,535** JUMP +3.25%; FTE **890.4**; neerlegging **16.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; no KBO email (route via cndg.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_cndg); foi + draft {GAP}; rq_1996=done + rq_1997 open; loop_state ticks=1996; raw under docs/doge/data/raw/tick1996/.
- FOI: **ready not sent** (human-gated; route via cndg.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1997 (AGB/FARO-if-YE2025 / AIESH-REW / CHR Verviers / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
