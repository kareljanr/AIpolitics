# -*- coding: utf-8 -*-
"""Tick 2297: finish in_progress SOBO@werk Brugge YE2025 leftover dual."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2297")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T17:00:00Z"
TICK = "2297"
RQ = "rq_2297"
NEXT_RQ = "rq_2298"
ENTITY = "vzw_sobo_werk_brugge"
KBO = "0863.423.427"
GAP = "gap_sobo_nbb_pdf_assets_debt_bruto_gt_omzet_1_85x_pnl_drop_54pct_matrix_l5"
LB = "lb_sobo_bruto_4_53m_omzet_2_45m_1_85x_pnl_drop_54pct_jr2025"
COMM = "comm_sobo_jr2025_statutory_bruto_gt_omzet_1_85x_pnl_drop"

OMZET = 2452992
OMZET24 = 2494768
BRUTO = 4528313
BRUTO24 = 4581826
PNL = 71897
PNL24 = 157239
EQUITY = 1454952
EQUITY24 = 1383054
FTE = 107.6
FTE24 = 107.1
FILED = "01.06.2026"
EMAIL = "info@sobo.be"
RATIO = round(BRUTO / OMZET, 2)  # ~1.85

# cost 5.0 (~4.5m) · abs 6.0 (pnl DROP -54% + bruto~1.85x) · diff 3
# pi = 0.55*5 + 0.35*6 + 0.1*7 = 5.55
ABS, COST, DIFF, PI = 6.0, 5.0, 3.0, 5.55


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path, fieldnames, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


os.makedirs(RAW, exist_ok=True)
os.makedirs(FOI_DRAFTS, exist_ok=True)
with open(os.path.join(RAW, "cw_en_excerpt.txt"), "w", encoding="utf-8") as f:
    f.write(
        f"SOBO@werk YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863423427\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_sobo_jr2025_cw_en",
        "title": f"SOBO@werk YE2025 CW EN (bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54%)",
        "url": "https://www.companyweb.be/en/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; omzet DROP {OMZET} (-1.67%); bruto DROP {BRUTO} (~{RATIO}x / -1.17%); pnl DROP {PNL} (-54.28%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_sobo_jr2025_cw_nl",
        "title": "SOBO@werk YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_sobo_jr2025_cw_fr",
        "title": "SOBO@werk YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_sobo_kbo_0863423427",
        "title": "KBO SOBO@werk 0863.423.427 Actief VZW 5 VE NACE 88.993 Brugge",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863423427",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; VZW sinds 13.02.2004; 5 VE; Pathoekeweg 9 A/7 8000 Brugge; RSZ 88.993; BTW catering/bouw; unlocked YE2025 (was YE2024 stall note)",
    },
    {
        "source_id": "src_sobo_site_contact_2297",
        "title": "SOBO FOI channel info@sobo.be / sobo.be",
        "url": "https://www.sobo.be/contact/contact",
        "publisher": "SOBO@werk VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Pathoekeweg 9 A/7 8000 Brugge; Flemish maatwerk Brugge e.o.",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "SOBO@werk VZW (Brugge / maatwerk)",
    "name_fr": "SOBO@werk ASBL (Bruges / entreprise de travail adapté)",
    "name_en": "SOBO@werk VZW (Bruges sheltered workshop / maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.sobo.be/",
    "foi_email": EMAIL,
    "foi_postal": "Pathoekeweg 9 A/7, 8000 Brugge",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 5 VE VZW RSZ 88.993; "
        f"omzet DROP {OMZET} (-1.67%) bruto DROP {BRUTO} (~{RATIO}x / -1.17%) pnl DROP {PNL} (-54.28%) "
        f"equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; "
        f"unlocked YE2025; after Ryhove@2296; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
    ),
}
if not any(r.get("entity_id") == ENTITY for r in erows):
    erows.append(ent)
else:
    for i, r in enumerate(erows):
        if r.get("entity_id") == ENTITY:
            erows[i] = ent
            break
write_csv(epath, efields, erows)

bpath = os.path.join(DATA, "budgets.csv")
bfields, brows = read_csv(bpath)
for nb in [
    {
        "budget_id": "bud_sobo_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_sobo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} DROP -1.17% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_sobo_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_sobo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} DROP -1.67% vs {OMZET24}",
    },
    {
        "budget_id": "bud_sobo_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_sobo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -54.28% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_sobo_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_sobo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +5.2% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_sobo_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_sobo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}",
    },
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": f"SOBO@werk YE2025 leftover dual (bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54% / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "maatwerkers Brugge e.o. / public loonkost path",
    "legal_basis": f"VZW SOBO@werk (KBO {KBO}; Actief; 5 VE; RSZ 88.993)",
    "decision_date": "2026-06-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk",
    "stated_goal": "Flemish maatwerk Brugge e.o. — catering/bouw/inclusive employment",
    "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -54% vs Vlaamse maatwerk wage-intervention matrix",
    "source_id": "src_sobo_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Brugge>SOBO>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); unlocked YE2025; after Ryhove@2296",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"SOBO@werk bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54% (YE2025)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Brugge>SOBO>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet DROP {OMZET} (-1.67%) / bruto DROP {BRUTO} (~{RATIO}x / -1.17%) / "
        f"pnl DROP {PNL} (-54.28%) / equity JUMP {EQUITY} / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_sobo_jr2025_cw_en",
    "beneficiaries": "maatwerkers Brugge e.o.",
    "stated_goal": "Flemish maatwerk Brugge catering/bouw inclusive employment",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl DROP -54%; omzet/bruto mild DROP; FTE {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -54%",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; unlocked YE2025; after Ryhove@2296; AGB Bornem JR2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Brugge>SOBO>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"Vlaamse maatwerk wage-intervention/GESCO/ESF/gemeente matrix; pnl DROP EUR{PNL} (-54.28%) vs YE2024 EUR{PNL24}"
    ),
    "why_it_matters": (
        f"Medium CW shows Flemish maatwerk VZW Brugge (bruto 4.53m / omzet 2.45m ~{RATIO}x / "
        f"pnl DROP -54% / FTE 107.6) under public path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "SOBO@werk VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Pathoekeweg 9 A/7, 8000 Brugge",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; unlocked YE2025; after Ryhove@2296",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — SOBO@werk (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -54%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** SOBO@werk VZW — KBO **{KBO}** (Actief; Pathoekeweg 9 A/7, 8000 Brugge; **5 VE**; FTE {FTE}; RSZ **88.993**)  
**recipient:** {EMAIL} · Pathoekeweg 9 A/7, 8000 Brugge  
**sources:** [CW EN](https://www.companyweb.be/en/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk) · [CW NL](https://www.companyweb.be/nl/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk) · [CW FR](https://www.companyweb.be/fr/0863423427/sociaal-ondernemen-brugge-en-omgeving-aan-het-werk) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863423427) · [site](https://www.sobo.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **SOCIAAL ONDERNEMEN BRUGGE EN OMGEVING AAN HET WERK** (SOBO@werk); **5 VE**; zetel Pathoekeweg 9 A/7, 8000 Brugge; RSZ NACE **88.993**; begindatum 13.02.2004.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −1.67%; bruto **EUR{BRUTO:,}** DROP −1.17% (~**{RATIO}x** omzet); pnl **EUR{PNL:,}** DROP −54.28%; equity **EUR{EQUITY:,}** JUMP +5.2%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Aralea/Manupal/De Ploeg/Vlotter YE2024. **SOBO unlocked YE2025** (claim notes still said YE2024). After Ryhove@2296. Do NOT redo Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: SOBO@werk VZW
via {EMAIL}
Pathoekeweg 9 A/7, 8000 Brugge
Betreft: Openbaarmaking jaarrekening 2025 SOBO@werk (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — Vlaamse maatwerk loonkost/GESCO/ESF-matrix.
3. Toelichting pnl DROP EUR{PNL} (−54.28% vs YE2024 EUR{PNL24}).
4. Activiteitensplit catering/bouw/maatwerk YE2025.
5. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
"""
with open(os.path.join(FOI_DRAFTS, f"{GAP}.md"), "w", encoding="utf-8") as f:
    f.write(draft)

rqpath = os.path.join(DATA, "research_queue.csv")
rqfields, rqrows = read_csv(rqpath)
for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = (
            f"leftover dual — SOBO@werk YE2025 Medium "
            f"(bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54%)"
        )
        r["notes"] = (
            f"tick{TICK} SOBO YE2025 unlocked; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; pnl {PNL}; "
            f"equity {EQUITY}; FTE {FTE}; FOI ready NOT sent; after Ryhove@2296"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after SOBO — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after SOBO@werk YE2025 Medium "
                f"(bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH if YE2025, else unused DSO/water/nuclear/IGS/HVZ, else unused "
                "ETA-VAPH-WZC-maatwerk (Aralea/Manupal/De Ploeg/Vlotter YE2024; Veerkracht4/Atelier Groot Eiland if YE2025). "
                "Do NOT redo SOBO/Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/"
                "Buseloc/Op Maat/REW stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} SOBO; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                f"Aralea/Manupal/De Ploeg/Vlotter YE2024; next every-10 2300"
            ),
        }
    )
write_csv(rqpath, rqfields, rqrows)

lspath = os.path.join(DATA, "loop_state.csv")
lsfields, lsrows = read_csv(lspath)
for r in lsrows:
    if r.get("state_id") == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = UTC
        r["last_unit_id"] = RQ
        r["ticks_completed"] = TICK
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover dual SOBO@werk {KBO} Medium "
            f"(omzet DROP {OMZET} -1.67%; bruto DROP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -54.28%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 5 VE Brugge maatwerk unlocked YE2025); after Ryhove@2296; "
            f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            f"next {NEXT_RQ}; next every-10 2300; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} SOBO@werk Brugge (bruto 4.53m / omzet 2.45m ~{RATIO}x / pnl DROP -54% / Medium)

- Unit: **{RQ}** finish **in_progress** leftover dual after **rq_2296 Ryhove**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Aralea/Manupal/De Ploeg/Vlotter still **YE2024**. **Preferred stall unlocked:** SOBO now **YE2025** (claim notes still said YE2024). Took FREE Flemish maatwerk **SOBO@werk VZW** YE2025 (KBO **{KBO}**; Pathoekeweg 9 A/7 Brugge; **Actief** **5 VE**; RSZ **88.993**). Do not redo Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/Buseloc/Op Maat/REW stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -1.67% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP -1.17% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -54.28% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +5.2%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 5 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk).
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x pnl={PNL} pi={PI} next={NEXT_RQ}")
