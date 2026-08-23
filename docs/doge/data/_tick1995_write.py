# ephemeral tick1995 — CHR Haute Senne YE2025 Medium (leftover dual after CHBA)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T02:20:00Z"
ENTITY = "vzw_haute_senne"
GAP = "gap_haute_senne_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_haute_senne_jr2025_cw"
SRC_EN = "src_haute_senne_jr2025_cw_en"
SRC_FR = "src_haute_senne_jr2025_cw_fr"
SRC_KBO = "src_haute_senne_kbo_1995"
SRC_SITE = "src_haute_senne_site_1995"

OMZET = "126740274"
PNL = "893431"
EQUITY = "37330673"
BRUTO = "59033630"
FTE = "710"
OMZET24 = "121832963"
PNL24 = "1776358"
EQUITY24 = "37071453"
BRUTO24 = "55587177"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1995")
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
        "title": "Companyweb NL CHR Haute Senne YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0256981407/centre-hospitalier-regional-de-la-haute-senne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1995; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1995/hs_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHR Haute Senne YE2025 statutory",
        "url": "https://www.companyweb.be/en/0256981407/centre-hospitalier-regional-de-la-haute-senne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1995; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick1995/hs_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR CHR Haute Senne YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0256981407/centre-hospitalier-regional-de-la-haute-senne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1995; FR mirror YE2025 Medium; deposés le 08-07-2026; raw docs/doge/data/raw/tick1995/hs_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHR Haute Senne 0256.981.407 Actief VZW publiek recht Soignies",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0256981407",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1995; Actief VZW van publiek recht since 28.12.1995; CENTRE HOSPITALIER REGIONAL DE LA HAUTE SENNE; Chaussee de Braine 49 7060 Soignies; email officiel.pr-chrhautesenne@chrhautesenne.be; 7 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chrhautesenne.be CHR Haute Senne",
        "url": "https://www.chrhautesenne.be/fr",
        "publisher": "CHR Haute Senne",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1995; Soignies regional hospital; contact via chrhautesenne.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_haute_senne_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1995; omzet JUMP {OMZET} +4.03pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_haute_senne_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1995; pnl DROP {PNL} -49.7pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_haute_senne_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1995; equity JUMP {EQUITY} +0.7pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_haute_senne_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1995; bruto JUMP {BRUTO} +6.2pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_haute_senne_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1995; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_haute_senne_jr2025_statutory_hospital",
    "title": "CHR Haute Senne YE2025 leftover hospital dual (omzet JUMP 126.74m / pnl DROP 0.89m / equity JUMP 37.33m)",
    "entity_id": ENTITY,
    "beneficiary": "Soignies/Hainaut hospital patients / CHR Haute Senne",
    "legal_basis": "VZW van publiek recht / ASBL DPU hospital (KBO 0256.981.407)",
    "decision_date": "2026-07-08",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0256981407/centre-hospitalier-regional-de-la-haute-senne",
    "stated_goal": "Regional hospital care (Soignies / Haute Senne)",
    "cut_option": "Publish NBB PDF assets/debt + pnl DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Hainaut>HauteSenne_Soignies>JR2025_statutory_L5",
    "notes": "tick1995; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHBA already mined; CNDG/CHR Verviers YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.5 + 0.10*4.0 = 3.025+1.925+0.4 = 5.35
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_haute_senne_omzet_jump_126_74m_pnl_drop_0_89m_equity_jump_jr2025",
    "name": "Haute Senne omzet JUMP 126.74m / pnl DROP 0.89m (-50pct) / equity JUMP 37.33m (YE2025)",
    "level": "L5",
    "type": "walloon_hospital_asbl_dual",
    "hierarchy_path": "Hainaut>HauteSenne_Soignies>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Soignies hospital patients via CHR Haute Senne VZW publiek recht",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 126.74m omzet with pnl DROP -49.7pct; equity JUMP +0.7pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl DROP vs YE2024 path vs CHBA/Saint-Luc/GHdC",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1995 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHR Haute Senne (Centre Hospitalier Regional de la Haute Senne)",
    "name_fr": "CHR Haute Senne (Centre Hospitalier Regional de la Haute Senne)",
    "name_en": "CHR Haute Senne (Soignies regional hospital VZW publiek recht)",
    "level": "asbl",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.chrhautesenne.be/fr",
    "foi_email": "officiel.pr-chrhautesenne@chrhautesenne.be",
    "foi_postal": "Chaussee de Braine 49, 7060 Soignies",
    "notes": (
        "tick1995 YE2025 Medium CW NL+EN+FR + Strong KBO 0256.981.407 Actief VZW publiek recht; "
        "omzet JUMP 126.74m pnl DROP 0.89m equity JUMP 37.33m bruto JUMP 59.03m FTE 710; "
        "assets/debt Unknown; neerlegging 08.07.2026; 7 VE; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia"
    ),
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
    "hierarchy_path": "Hainaut>HauteSenne_Soignies>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP recon vs YE2024",
    "why_it_matters": "Medium CW shows 126.74m omzet Soignies hospital VZW with pnl DROP -50pct without balance sheet",
    "priority": "7",
    "recipient_body": "CHR Haute Senne VZW publiek recht",
    "recipient_email": "officiel.pr-chrhautesenne@chrhautesenne.be",
    "recipient_postal": "Chaussee de Braine 49, 7060 Soignies",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_haute_senne_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_haute_senne_omzet_jump_126_74m_pnl_drop_0_89m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1995; human-send only; Medium CW; route via chrhautesenne.be; next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHR Haute Senne (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHR Haute Senne VZW publiek recht — KBO **0256.981.407**  
**recipient:** officiel.pr-chrhautesenne@chrhautesenne.be · Chaussee de Braine 49, 7060 Soignies  
**sources:** [CW NL](https://www.companyweb.be/nl/0256981407/centre-hospitalier-regional-de-la-haute-senne) · [CW EN](https://www.companyweb.be/en/0256981407/centre-hospitalier-regional-de-la-haute-senne) · [CW FR](https://www.companyweb.be/fr/0256981407/centre-hospitalier-regional-de-la-haute-senne) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0256981407) · [site](https://www.chrhautesenne.be/fr)  
**tick:** 1995  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **08.07.2026**): omzet **EUR126,740,274** JUMP +4.03%; pnl **EUR893,431** DROP **-49.7%** (vs YE2024 EUR1,776,358); equity **EUR37,330,673** JUMP +0.7%; bruto **EUR59,033,630** JUMP +6.2%; FTE **710**; assets/debt **Unknown**.
- Soignies VZW van publiek recht regional hospital (Haute Senne). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CHBA already mined. CNDG / CHR Verviers YE2025 also live deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHR Haute Senne VZW — Chaussee de Braine 49, 7060 Soignies
officiel.pr-chrhautesenne@chrhautesenne.be
cc: SPW Interieur / Province Hainaut transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHR Haute Senne + balans (KBO 0256.981.407)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 08.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (EUR893.431 vs YE2024 EUR1.776.358; -49.7pct).
4. Dual vs CHBA / Saint-Luc / GHdC indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1995":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after CHBA Seraing — Haute Senne YE2025 Medium"
        x["notes"] = (
            "tick1995 Haute Senne Medium omzet JUMP 126.74m pnl DROP 0.89m equity JUMP 37.33m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; CNDG/CHR Verviers YE2025 deferred; next rq_1996; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover CHR Haute Senne YE2025 Medium CW; KBO 0256.981.407; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1996" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1996",
            "title": "leftover dual hole-fill after Haute Senne",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1995 after Haute Senne YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (CNDG 0401.690.559 / CHR Verviers 0250.893.369 / Erasme / UZ if YE2025). "
                "Do NOT redo Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1995 Haute Senne; next every-10 2000; CNDG/CHR Verviers YE2025 live deferred",
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
        "last_unit_id": "rq_1995",
        "ticks_completed": "1995",
        "paused": "no",
        "notes": (
            "tick1995 leftover Haute Senne 0256.981.407 Medium CW (omzet JUMP 126.74m pnl DROP 0.89m equity JUMP 37.33m bruto JUMP 59.03m FTE 710; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; CNDG/CHR Verviers YE2025 deferred; next rq_1996; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1995 - {UTC} - rq_1995 Haute Senne (omzet JUMP 126.74m / pnl DROP 0.89m / Medium)

- Unit: **rq_1995** leftover dual after **rq_1994 CHBA Seraing**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **CHR Haute Senne** YE2025 (KBO **0256.981.407**; Chaussee de Braine 49 Soignies; Hainaut **regional hospital VZW publiek recht**). **CNDG** YE2025 (omzet 149.61m) and **CHR Verviers** YE2025 (omzet 251.76m) also live deferred. Do not redo CHBA/Saint-Luc/GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR126,740,274** JUMP +4.03%; pnl **EUR893,431** DROP **-49.7%**; equity **EUR37,330,673** JUMP +0.7%; bruto **EUR59,033,630** JUMP +6.2%; FTE **710**; neerlegging **08.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW publiek recht 7 VE; email officiel.pr-chrhautesenne@chrhautesenne.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_haute_senne); foi + draft {GAP}; rq_1995=done + rq_1996 open; loop_state ticks=1995; raw under docs/doge/data/raw/tick1995/.
- FOI: **ready not sent** (human-gated; officiel.pr-chrhautesenne@chrhautesenne.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1996 (AGB/FARO-if-YE2025 / AIESH-REW / CNDG / CHR Verviers / Erasme-UZ / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
