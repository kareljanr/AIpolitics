# ephemeral tick1998 — ZAS YE2025 Medium (leftover dual after CHR Verviers)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T03:05:00Z"
ENTITY = "vzw_zas"
GAP = "gap_zas_nbb_pdf_assets_debt_pnl_loss_omzet_jump_matrix_l5"
SRC = "src_zas_jr2025_cw"
SRC_EN = "src_zas_jr2025_cw_en"
SRC_FR = "src_zas_jr2025_cw_fr"
SRC_KBO = "src_zas_kbo_1998"
SRC_SITE = "src_zas_site_1998"

OMZET = "1370339118"
PNL = "-814746"
EQUITY = "573600782"
BRUTO = "643722300"
FTE = "6711.9"
OMZET24 = "1072252364"
PNL24 = "6716880"
EQUITY24 = "558853334"
BRUTO24 = "519989802"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1998")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL ZAS YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0862382656/ziekenhuis-aan-de-stroom",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick1998; YE2025 omzet JUMP {OMZET} pnl LOSS {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1998/zas_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN ZAS YE2025 statutory",
        "url": "https://www.companyweb.be/en/0862382656/ziekenhuis-aan-de-stroom",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1998; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick1998/zas_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR ZAS YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0862382656/ziekenhuis-aan-de-stroom",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1998; FR mirror YE2025 Medium; deposés le 02-07-2026; raw docs/doge/data/raw/tick1998/zas_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO ZAS 0862.382.656 Actief VZW Antwerpen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862382656",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1998; Actief VZW since 24.12.2003; Ziekenhuis aan de Stroom; Kempenstraat 100 2030 Antwerpen; no KBO email; 28 VE; Aanbestedende overheid; ZNA+GZA fusion network",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "zas.be Ziekenhuis aan de Stroom",
        "url": "https://www.zas.be/",
        "publisher": "ZAS",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1998; Antwerp hospital network (ex ZNA+GZA); contact via zas.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_zas_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1998; omzet JUMP {OMZET} +27.80pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_zas_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1998; pnl LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_zas_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1998; equity JUMP {EQUITY} +2.64pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_zas_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1998; bruto JUMP {BRUTO} +23.80pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_zas_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1998; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_zas_jr2025_statutory_hospital",
    "title": "ZAS YE2025 leftover hospital dual (omzet JUMP 1370.34m / pnl LOSS 0.81m / equity JUMP 573.60m)",
    "entity_id": ENTITY,
    "beneficiary": "Antwerp hospital patients / Ziekenhuis aan de Stroom (ex ZNA+GZA)",
    "legal_basis": "VZW/ASBL hospital network (KBO 0862.382.656)",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0862382656/ziekenhuis-aan-de-stroom",
    "stated_goal": "Antwerp metropolitan hospital care (ZAS network)",
    "cut_option": "Publish NBB PDF assets/debt + pnl LOSS / omzet JUMP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>ZAS>JR2025_statutory_L5",
    "notes": "tick1998; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; Erasme/UZB CW opaque; AZ Sint-Lucas CW N/A omzet; AZJP YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*9.0 + 0.35*7.0 + 0.10*4.0 = 4.95+2.45+0.4 = 7.8
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_zas_omzet_jump_1370_34m_pnl_loss_0_81m_equity_jump_jr2025",
    "name": "ZAS omzet JUMP 1370.34m / pnl LOSS 0.81m / equity JUMP 573.60m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "Antwerpen>ZAS>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Antwerp patients via ZAS VZW (ZNA+GZA fusion network)",
    "stated_goal": "Metropolitan hospital care",
    "measured_outcome": "Medium CW YE2025; 1.37bn omzet JUMP +27.8pct with pnl LOSS turnaround from YE2024 profit; NBB PDF residual",
    "absurdity_score": "7.0",
    "cost_score": "9.0",
    "difficulty": "4.0",
    "priority_index": "7.8",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon omzet JUMP + pnl LOSS path vs Saint-Luc/GHdC/Humani; fusion perimeter transparency",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1998 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "ZAS / Ziekenhuis aan de Stroom",
    "name_fr": "ZAS / Ziekenhuis aan de Stroom",
    "name_en": "ZAS / Ziekenhuis aan de Stroom (Antwerp hospital network)",
    "level": "asbl",
    "parent_id": "city_antwerpen",
    "community_language": "nl",
    "website": "https://www.zas.be/",
    "foi_email": "",
    "foi_postal": "Kempenstraat 100, 2030 Antwerpen",
    "notes": "tick1998 YE2025 Medium CW NL+EN+FR + Strong KBO 0862.382.656 Actief VZW; omzet JUMP 1370.34m pnl LOSS 0.81m equity JUMP 573.60m bruto JUMP 643.72m FTE 6711.9; assets/debt Unknown; neerlegging 02.07.2026; 28 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; Erasme/UZB CW opaque; AZ Sint-Lucas CW N/A; AZJP deferred; do not redo CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>ZAS>NBB_PDF_assets_debt_pnl_loss_omzet_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS recon vs YE2024 profit; omzet JUMP +27.8pct fusion perimeter",
    "why_it_matters": "Medium CW shows 1.37bn omzet Antwerp hospital VZW with pnl LOSS turnaround and huge JUMP without balance sheet",
    "priority": "9",
    "recipient_body": "Ziekenhuis aan de Stroom VZW / ZAS",
    "recipient_email": "",
    "recipient_postal": "Kempenstraat 100, 2030 Antwerpen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_zas_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_zas_omzet_jump_1370_34m_pnl_loss_0_81m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1998; human-send only; Medium CW; route via zas.be (no KBO email); next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — ZAS (NBB PDF / assets-debt / pnl LOSS / omzet JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ziekenhuis aan de Stroom VZW / ZAS — KBO **0862.382.656**  
**recipient:** route via zas.be (no KBO email) · Kempenstraat 100, 2030 Antwerpen  
**sources:** [CW NL](https://www.companyweb.be/nl/0862382656/ziekenhuis-aan-de-stroom) · [CW EN](https://www.companyweb.be/en/0862382656/ziekenhuis-aan-de-stroom) · [CW FR](https://www.companyweb.be/fr/0862382656/ziekenhuis-aan-de-stroom) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862382656) · [site](https://www.zas.be/)  
**tick:** 1998  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.07.2026**): omzet **EUR1,370,339,118** JUMP +27.80%; pnl **LOSS EUR-814,746** (vs YE2024 profit EUR6,716,880); equity **EUR573,600,782** JUMP +2.64%; bruto **EUR643,722,300** JUMP +23.80%; FTE **6711.9**; assets/debt **Unknown**.
- Antwerp VZW hospital network (ZNA+GZA fusion). Preferred stall: AGB Bornem / FARO still YE2024; Erasme/UZB CW opaque; AZ Sint-Lucas CW N/A omzet. AZJP YE2025 also live deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ziekenhuis aan de Stroom VZW / ZAS — Kempenstraat 100, 2030 Antwerpen
via zas.be openbaarheid / contact
cc: Stad Antwerpen / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 ZAS + balans (KBO 0862.382.656)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon omzet JUMP (+27,80pct vs YE2024) en pnl LOSS (EUR-814.746 vs YE2024 winst EUR6.716.880).
4. Fusion perimeter ZNA/GZA / consolidatie-toelichting indien publiek.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1998":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after CHR Verviers — ZAS YE2025 Medium"
        x["notes"] = (
            "tick1998 ZAS Medium omzet JUMP 1370.34m pnl LOSS 0.81m equity JUMP 573.60m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; Erasme/UZB opaque; AZSL N/A; AZJP YE2025 deferred; next rq_1999; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover ZAS YE2025 Medium CW; KBO 0862.382.656; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1999" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1999",
            "title": "leftover dual hole-fill after ZAS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1998 after ZAS YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZJP 0267.386.438 / AZ Groeninge / other unused YE2025 if live). "
                "Do NOT redo ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1998 ZAS; next every-10 2000; AZJP YE2025 live deferred; Erasme/UZB CW opaque",
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
        "last_unit_id": "rq_1998",
        "ticks_completed": "1998",
        "paused": "no",
        "notes": (
            "tick1998 leftover ZAS 0862.382.656 Medium CW (omzet JUMP 1370.34m pnl LOSS 0.81m equity JUMP 573.60m bruto JUMP 643.72m FTE 6711.9; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; AZJP YE2025 deferred; next rq_1999; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 1998 - {UTC} - rq_1998 ZAS (omzet JUMP 1370.34m / pnl LOSS 0.81m / Medium)

- Unit: **rq_1998** leftover dual after **rq_1997 CHR Verviers**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Erasme/UZ Brussel CW **opaque** (no filed statements); AZ Sint-Lucas Gent/Brugge CW **N/A omzet**. Took unused leftover **ZAS** YE2025 (KBO **0862.382.656**; Kempenstraat 100 Antwerpen; Antwerp **hospital VZW** ZNA+GZA fusion). **AZJP** YE2025 also live deferred. Do not redo CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR1,370,339,118** JUMP +27.80%; pnl **LOSS EUR-814,746** (vs YE2024 profit 6.72m); equity **EUR573,600,782** JUMP +2.64%; bruto **EUR643,722,300** JUMP +23.80%; FTE **6711.9**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 28 VE; no KBO email (route via zas.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_zas); foi + draft {GAP}; rq_1998=done + rq_1999 open; loop_state ticks=1998; raw under docs/doge/data/raw/tick1998/.
- FOI: **ready not sent** (human-gated; route via zas.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1999 (AGB/FARO-if-YE2025 / AIESH-REW / AZJP / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
