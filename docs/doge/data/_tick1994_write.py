# ephemeral tick1994 — CHBA Seraing YE2025 Medium (leftover dual after Saint-Luc)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T02:05:00Z"
ENTITY = "igs_chba"
GAP = "gap_chba_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5"
SRC = "src_chba_jr2025_cw"
SRC_EN = "src_chba_jr2025_cw_en"
SRC_FR = "src_chba_jr2025_cw_fr"
SRC_KBO = "src_chba_kbo_1994"
SRC_SITE = "src_chba_site_1994"

OMZET = "183560247"
PNL = "1441066"
EQUITY = "24114550"
BRUTO = "129755799"
FTE = "1563.1"
OMZET24 = "175826110"
PNL24 = "-469472"
EQUITY24 = "23457037"
BRUTO24 = "123318670"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1994")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))
r["status"] = "in_progress"
r["updated_utc"] = UTC
r["entity_id"] = ENTITY
save("docs/doge/data/research_queue.csv", qrows, qfields)

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHBA YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0203980409/centre-hospitalier-bois-de-l-abbaye",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1994; YE2025 omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 14.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1994/chba_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHBA YE2025 statutory",
        "url": "https://www.companyweb.be/en/0203980409/centre-hospitalier-bois-de-l-abbaye",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1994; EN mirror YE2025 Medium; filed 14-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick1994/chba_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR CHBA YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0203980409/centre-hospitalier-bois-de-l-abbaye",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1994; FR mirror YE2025 Medium; deposés le 14-07-2026; raw docs/doge/data/raw/tick1994/chba_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHBA 0203.980.409 Actief CV publiek recht Seraing",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0203980409",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1994; Actief CV van publiek recht since 01.01.1968; Centre Hospitalier Bois de l Abbaye; Rue Laplace 40 4100 Seraing; email officiel.ic-chba@chba.be; 7 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chba.be Centre Hospitalier Bois de l Abbaye",
        "url": "https://www.chba.be/",
        "publisher": "CHBA",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1994; Seraing hospital sites; info@chba.be; contact via chba.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chba_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1994; omzet JUMP {OMZET} +4.40pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_chba_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1994; pnl JUMP turnaround {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_chba_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1994; equity JUMP {EQUITY} +2.80pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_chba_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1994; bruto JUMP {BRUTO} +5.22pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_chba_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1994; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chba_jr2025_statutory_hospital",
    "title": "CHBA YE2025 leftover hospital dual (omzet JUMP 183.56m / pnl JUMP turnaround 1.44m / equity JUMP 24.11m)",
    "entity_id": ENTITY,
    "beneficiary": "Seraing/Liege hospital patients / Centre Hospitalier Bois de l Abbaye",
    "legal_basis": "CV van publiek recht / SC DPU hospital (KBO 0203.980.409)",
    "decision_date": "2026-07-14",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0203980409/centre-hospitalier-bois-de-l-abbaye",
    "stated_goal": "Regional hospital care (Seraing / Bois de l Abbaye)",
    "cut_option": "Publish NBB PDF assets/debt + pnl turnaround recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Liege>CHBA_Seraing>JR2025_statutory_L5",
    "notes": "tick1994; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Saint-Luc already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*6.0 + 0.35*5.5 + 0.10*4.0 = 3.3+1.925+0.4 = 5.625
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chba_omzet_jump_183_56m_pnl_turnaround_1_44m_equity_jump_jr2025",
    "name": "CHBA omzet JUMP 183.56m / pnl JUMP turnaround 1.44m / equity JUMP 24.11m (YE2025)",
    "level": "L5",
    "type": "walloon_hospital_igs_dual",
    "hierarchy_path": "Liege>CHBA_Seraing>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Seraing hospital patients via CHBA CV publiek recht",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 183.56m omzet with pnl turnaround from YE2024 LOSS; equity JUMP +2.8pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.0",
    "difficulty": "4.0",
    "priority_index": "5.625",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl turnaround vs YE2024 LOSS path vs Saint-Luc/GHdC/Humani",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1994 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Centre Hospitalier Bois de l'Abbaye (CHBA)",
    "name_fr": "Centre Hospitalier Bois de l'Abbaye (CHBA)",
    "name_en": "Centre Hospitalier Bois de l'Abbaye (CHBA Seraing hospital)",
    "level": "igs",
    "parent_id": "prov_liege",
    "community_language": "fr",
    "website": "https://www.chba.be/",
    "foi_email": "officiel.ic-chba@chba.be",
    "foi_postal": "Rue Laplace 40, 4100 Seraing",
    "notes": "tick1994 YE2025 Medium CW NL+EN+FR + Strong KBO 0203.980.409 Actief CV publiek recht; omzet JUMP 183.56m pnl JUMP turnaround 1.44m equity JUMP 24.11m bruto JUMP 129.76m FTE 1563.1; assets/debt Unknown; neerlegging 14.07.2026; 7 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
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
    "hierarchy_path": "Liege>CHBA_Seraing>NBB_PDF_assets_debt_pnl_turnaround",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl turnaround recon vs YE2024 LOSS",
    "why_it_matters": "Medium CW shows 183.56m omzet Seraing hospital CV with pnl turnaround from LOSS without balance sheet",
    "priority": "7",
    "recipient_body": "Centre Hospitalier Bois de l'Abbaye CV",
    "recipient_email": "officiel.ic-chba@chba.be",
    "recipient_postal": "Rue Laplace 40, 4100 Seraing",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_chba_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chba_omzet_jump_183_56m_pnl_turnaround_1_44m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1994; human-send only; Medium CW; also info@chba.be; next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHBA Seraing (NBB PDF / assets-debt / pnl turnaround)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Centre Hospitalier Bois de l'Abbaye CV — KBO **0203.980.409**  
**recipient:** officiel.ic-chba@chba.be · Rue Laplace 40, 4100 Seraing  
**sources:** [CW NL](https://www.companyweb.be/nl/0203980409/centre-hospitalier-bois-de-l-abbaye) · [CW EN](https://www.companyweb.be/en/0203980409/centre-hospitalier-bois-de-l-abbaye) · [CW FR](https://www.companyweb.be/fr/0203980409/centre-hospitalier-bois-de-l-abbaye) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0203980409) · [site](https://www.chba.be/)  
**tick:** 1994  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **14.07.2026**): omzet **EUR183,560,247** JUMP +4.40%; pnl **EUR1,441,066** JUMP turnaround (vs YE2024 LOSS EUR-469,472); equity **EUR24,114,550** JUMP +2.80%; bruto **EUR129,755,799** JUMP +5.22%; FTE **1563.1**; assets/debt **Unknown**.
- Seraing CV van publiek recht hospital (Bois de l'Abbaye). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. Saint-Luc already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Centre Hospitalier Bois de l'Abbaye CV — Rue Laplace 40, 4100 Seraing
officiel.ic-chba@chba.be / info@chba.be
cc: SPW Interieur / Province Liege transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHBA + balans (KBO 0203.980.409)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 14.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl turnaround (EUR1.441.066 vs YE2024 verlies EUR-469.472).
4. Dual vs Saint-Luc / GHdC / Humani indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1994":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Saint-Luc — CHBA Seraing YE2025 Medium"
        x["notes"] = (
            "tick1994 CHBA Medium omzet JUMP 183.56m pnl JUMP turnaround 1.44m equity JUMP 24.11m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1995; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover CHBA Seraing YE2025 Medium CW; KBO 0203.980.409; "
            f"omzet JUMP {OMZET} pnl JUMP turnaround {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1995" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1995",
            "title": "leftover dual hole-fill after CHBA Seraing",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1994 after CHBA Seraing YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Haute Senne / CNDG / CHR Verviers if YE2025). "
                "Do NOT redo CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1994 CHBA; next every-10 2000; Haute Senne/CNDG/CHR Verviers candidates if YE2025",
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
        "last_unit_id": "rq_1994",
        "ticks_completed": "1994",
        "paused": "no",
        "notes": (
            "tick1994 leftover CHBA 0203.980.409 Medium CW (omzet JUMP 183.56m pnl JUMP turnaround 1.44m equity JUMP 24.11m bruto JUMP 129.76m FTE 1563.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1995; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1994 - {UTC} - rq_1994 CHBA Seraing (omzet JUMP 183.56m / pnl JUMP turnaround 1.44m / Medium)

- Unit: **rq_1994** leftover dual after **rq_1993 Saint-Luc**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **CHBA Seraing** YE2025 (KBO **0203.980.409**; Rue Laplace 40 Seraing; Liege **hospital CV publiek recht**). Haute Senne / CNDG / CHR Verviers deferred. Do not redo Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR183,560,247** JUMP +4.40%; pnl **EUR1,441,066** JUMP turnaround (vs YE2024 LOSS 0.47m); equity **EUR24,114,550** JUMP +2.80%; bruto **EUR129,755,799** JUMP +5.22%; FTE **1563.1**; neerlegging **14.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV publiek recht 7 VE; email officiel.ic-chba@chba.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_chba); foi + draft {GAP}; rq_1994=done + rq_1995 open; loop_state ticks=1994; raw under docs/doge/data/raw/tick1994/.
- FOI: **ready not sent** (human-gated; officiel.ic-chba@chba.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1995 (AGB/FARO-if-YE2025 / AIESH-REW / Haute Senne / CNDG / CHR Verviers / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
