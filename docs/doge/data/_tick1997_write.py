# ephemeral tick1997 — CHR Verviers YE2025 Medium (leftover dual after CNDG)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T02:50:00Z"
ENTITY = "igs_chr_verviers"
GAP = "gap_chr_verviers_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5"
SRC = "src_chr_verviers_jr2025_cw"
SRC_EN = "src_chr_verviers_jr2025_cw_en"
SRC_FR = "src_chr_verviers_jr2025_cw_fr"
SRC_KBO = "src_chr_verviers_kbo_1997"
SRC_SITE = "src_chr_verviers_site_1997"

OMZET = "251756992"
PNL = "890809"
EQUITY = "62397208"
BRUTO = "125531398"
FTE = "1272.9"
OMZET24 = "243319464"
PNL24 = "-927625"
EQUITY24 = "62382086"
BRUTO24 = "120153427"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1997")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHR Verviers YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1997; YE2025 omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 18.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1997/verviers_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHR Verviers YE2025 statutory",
        "url": "https://www.companyweb.be/en/0250893369/centre-hospitalier-regional-de-verviers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1997; EN mirror YE2025 Medium; filed 18-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick1997/verviers_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR CHR Verviers YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0250893369/centre-hospitalier-regional-de-verviers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1997; FR mirror YE2025 Medium; deposés le 18-07-2026; raw docs/doge/data/raw/tick1997/verviers_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHR Verviers 0250.893.369 Actief CV Verviers",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0250893369",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1997; Actief CV since 07.01.1993 (rechtsvorm CV sinds 17.12.2021); Centre Hospitalier Regional de Verviers; Rue du Parc 29 4800 Verviers; email officiel.ic-chrverviers@chrverviers.be; 8 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chrverviers.be Centre Hospitalier Regional de Verviers",
        "url": "https://www.chrverviers.be/",
        "publisher": "CHR Verviers",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1997; Verviers regional hospital; info@chrverviers.be; contact via chrverviers.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chr_verviers_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1997; omzet JUMP {OMZET} +3.47pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_chr_verviers_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1997; pnl JUMP turnaround {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_chr_verviers_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1997; equity JUMP {EQUITY} +0.02pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_chr_verviers_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1997; bruto JUMP {BRUTO} +4.48pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_chr_verviers_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1997; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chr_verviers_jr2025_statutory_hospital",
    "title": "CHR Verviers YE2025 leftover hospital dual (omzet JUMP 251.76m / pnl JUMP turnaround 0.89m / equity JUMP 62.40m)",
    "entity_id": ENTITY,
    "beneficiary": "Verviers/Liege hospital patients / Centre Hospitalier Regional de Verviers",
    "legal_basis": "CV / SC hospital (KBO 0250.893.369)",
    "decision_date": "2026-07-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers",
    "stated_goal": "Regional hospital care (Verviers)",
    "cut_option": "Publish NBB PDF assets/debt + pnl turnaround recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Liege>CHR_Verviers>JR2025_statutory_L5",
    "notes": "tick1997; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CNDG already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*6.5 + 0.35*5.5 + 0.10*4.0 = 3.575+1.925+0.4 = 5.9
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chr_verviers_omzet_jump_251_76m_pnl_turnaround_0_89m_equity_jump_jr2025",
    "name": "CHR Verviers omzet JUMP 251.76m / pnl JUMP turnaround 0.89m / equity JUMP 62.40m (YE2025)",
    "level": "L5",
    "type": "walloon_hospital_igs_dual",
    "hierarchy_path": "Liege>CHR_Verviers>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Verviers hospital patients via CHR Verviers CV",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 251.76m omzet with pnl turnaround from YE2024 LOSS; equity flat JUMP +0.02pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.5",
    "difficulty": "4.0",
    "priority_index": "5.9",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl turnaround vs YE2024 LOSS path vs CNDG/Citadelle/CHBA",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1997 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHR Verviers / Centre Hospitalier Regional de Verviers",
    "name_fr": "CHR Verviers / Centre Hospitalier Regional de Verviers",
    "name_en": "CHR Verviers (regional hospital cooperative)",
    "level": "igs",
    "parent_id": "prov_liege",
    "community_language": "fr",
    "website": "https://www.chrverviers.be/",
    "foi_email": "officiel.ic-chrverviers@chrverviers.be",
    "foi_postal": "Rue du Parc 29, 4800 Verviers",
    "notes": "tick1997 YE2025 Medium CW NL+EN+FR + Strong KBO 0250.893.369 Actief CV; omzet JUMP 251.76m pnl JUMP turnaround 0.89m equity JUMP 62.40m bruto JUMP 125.53m FTE 1272.9; assets/debt Unknown; neerlegging 18.07.2026; 8 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
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
    "hierarchy_path": "Liege>CHR_Verviers>NBB_PDF_assets_debt_pnl_turnaround",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl turnaround recon vs YE2024 LOSS",
    "why_it_matters": "Medium CW shows 251.76m omzet Verviers hospital CV with pnl turnaround from LOSS without balance sheet",
    "priority": "7",
    "recipient_body": "Centre Hospitalier Regional de Verviers CV",
    "recipient_email": "officiel.ic-chrverviers@chrverviers.be",
    "recipient_postal": "Rue du Parc 29, 4800 Verviers",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_chr_verviers_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chr_verviers_omzet_jump_251_76m_pnl_turnaround_0_89m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1997; human-send only; Medium CW; also info@chrverviers.be; next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHR Verviers (NBB PDF / assets-debt / pnl turnaround)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Centre Hospitalier Regional de Verviers CV — KBO **0250.893.369**  
**recipient:** officiel.ic-chrverviers@chrverviers.be · Rue du Parc 29, 4800 Verviers  
**sources:** [CW NL](https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers) · [CW EN](https://www.companyweb.be/en/0250893369/centre-hospitalier-regional-de-verviers) · [CW FR](https://www.companyweb.be/fr/0250893369/centre-hospitalier-regional-de-verviers) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0250893369) · [site](https://www.chrverviers.be/)  
**tick:** 1997  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **18.07.2026**): omzet **EUR251,756,992** JUMP +3.47%; pnl **EUR890,809** JUMP turnaround (vs YE2024 LOSS EUR-927,625); equity **EUR62,397,208** JUMP +0.02%; bruto **EUR125,531,398** JUMP +4.48%; FTE **1272.9**; assets/debt **Unknown**.
- Verviers CV hospital. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CNDG already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Centre Hospitalier Regional de Verviers CV — Rue du Parc 29, 4800 Verviers
officiel.ic-chrverviers@chrverviers.be / info@chrverviers.be
cc: SPW Interieur / Province Liege transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHR Verviers + balans (KBO 0250.893.369)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 18.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl turnaround (EUR890.809 vs YE2024 verlies EUR-927.625).
4. Dual vs Citadelle / CNDG / CHBA indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1997":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after CNDG — CHR Verviers YE2025 Medium"
        x["notes"] = (
            "tick1997 CHR Verviers Medium omzet JUMP 251.76m pnl JUMP turnaround 0.89m equity JUMP 62.40m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1998; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover CHR Verviers YE2025 Medium CW; KBO 0250.893.369; "
            f"omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1998" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1998",
            "title": "leftover dual hole-fill after CHR Verviers",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1997 after CHR Verviers YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Erasme / UZ Brussel / other unused YE2025 hospital if live). "
                "Do NOT redo CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1997 CHR Verviers; next every-10 2000",
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
        "last_unit_id": "rq_1997",
        "ticks_completed": "1997",
        "paused": "no",
        "notes": (
            "tick1997 leftover CHR Verviers 0250.893.369 Medium CW (omzet JUMP 251.76m pnl JUMP turnaround 0.89m equity JUMP 62.40m bruto JUMP 125.53m FTE 1272.9; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1998; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1997 - {UTC} - rq_1997 CHR Verviers (omzet JUMP 251.76m / pnl JUMP turnaround 0.89m / Medium)

- Unit: **rq_1997** leftover dual after **rq_1996 CNDG**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **CHR Verviers** YE2025 (KBO **0250.893.369**; Rue du Parc 29 Verviers; Liege **hospital CV**). Do not redo CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR251,756,992** JUMP +3.47%; pnl **EUR890,809** JUMP turnaround (vs YE2024 LOSS 0.93m); equity **EUR62,397,208** JUMP +0.02%; bruto **EUR125,531,398** JUMP +4.48%; FTE **1272.9**; neerlegging **18.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV 8 VE; email officiel.ic-chrverviers@chrverviers.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_chr_verviers); foi + draft {GAP}; rq_1997=done + rq_1998 open; loop_state ticks=1997; raw under docs/doge/data/raw/tick1997/.
- FOI: **ready not sent** (human-gated; officiel.ic-chrverviers@chrverviers.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1998 (AGB/FARO-if-YE2025 / AIESH-REW / Erasme-UZ / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
