# -*- coding: utf-8 -*-
"""Tick 2307: leftover dual Katrinahof Antwerpen YE2025 VAPH after Alvinnenberg."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2307")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2307"
RQ = "rq_2307"
NEXT_RQ = "rq_2308"
ENTITY = "vzw_katrinahof_antwerpen"
KBO = "0414.830.792"
GAP = "gap_katrinahof_nbb_pdf_assets_debt_bruto_gt_omzet_10_47x_pnl_drop_93pct_vaph_matrix_l5"
LB = "lb_katrinahof_bruto_11_18m_omzet_1_07m_10_47x_pnl_drop_93pct_jr2025"
COMM = "comm_katrinahof_jr2025_statutory_bruto_gt_omzet_10_47x_pnl_drop_vaph"

OMZET = 1067123
OMZET24 = 1032089
BRUTO = 11176535
BRUTO24 = 10466910
PNL = 11440
PNL24 = 162968
EQUITY = 6810399
EQUITY24 = 6893223
FTE = 141.8
FTE24 = 138.4
FILED = "02.06.2026"
EMAIL = "info@katrinahof.be"
RATIO = round(BRUTO / OMZET, 2)  # ~10.47

# cost 5.5 (~11.2m) · abs 7.6 (bruto~10.5x + pnl DROP -93%) · diff 3
# pi = 0.55*5.5 + 0.35*7.6 + 0.1*7 = 6.385 → 6.4
ABS, COST, DIFF, PI = 7.6, 5.5, 3.0, 6.4


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
        f"Katrinahof YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity DROP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0414830792/vzw-katrinahof\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414830792\n"
        "https://www.katrinahof.be/\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    f.write(
        "{\n"
        f'  "tick": "{TICK}",\n'
        f'  "unit": "{RQ}",\n'
        f'  "entity": "{ENTITY}",\n'
        f'  "kbo": "{KBO}",\n'
        f'  "omzet": {OMZET},\n'
        f'  "bruto": {BRUTO},\n'
        f'  "pnl": {PNL},\n'
        f'  "equity": {EQUITY},\n'
        f'  "fte": {FTE},\n'
        f'  "ratio": {RATIO},\n'
        f'  "confidence": "medium",\n'
        f'  "gap": "{GAP}",\n'
        f'  "pi": {PI}\n'
        "}\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_katrinahof_jr2025_cw_en",
        "title": f"Katrinahof YE2025 CW EN (bruto 11.18m / omzet 1.07m ~{RATIO}x / pnl DROP -93%)",
        "url": "https://www.companyweb.be/en/0414830792/vzw-katrinahof",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+3.39%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +6.78%); pnl DROP {PNL} (-92.98%); equity DROP {EQUITY} (-1.2%); "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_katrinahof_jr2025_cw_nl",
        "title": "Katrinahof YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0414830792/vzw-katrinahof",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_katrinahof_jr2025_cw_fr",
        "title": "Katrinahof YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0414830792/vzw-katrinahof",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_katrinahof_kbo_0414830792",
        "title": "KBO VZW Katrinahof 0414.830.792 Actief VZW 2 VE NACE 87.201 Antwerpen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414830792",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 20.06.1974; 2 VE; Fromentinstraat 1 2050 Antwerpen; "
            f"RSZ 87.201; BTW Nee; VAPH orthopedagogisch centrum"
        ),
    },
    {
        "source_id": "src_katrinahof_site_contact_2307",
        "title": "Katrinahof FOI channel info@katrinahof.be",
        "url": "https://www.katrinahof.be/",
        "publisher": "VZW Katrinahof",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Fromentinstraat 1-3 2050 Antwerpen; T 03 722 07 22",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "VZW Katrinahof (Antwerpen / VAPH orthopedagogisch)",
    "name_fr": "ASBL Katrinahof (Anvers / centre orthopédagogique VAPH)",
    "name_en": "Katrinahof VZW (Antwerp / VAPH orthopedagogical centre)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.katrinahof.be/",
    "foi_email": EMAIL,
    "foi_postal": "Fromentinstraat 1, 2050 Antwerpen",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW "
        f"NACE 87.201; omzet JUMP {OMZET} (+3.39%) bruto JUMP {BRUTO} (~{RATIO}x / +6.78%) "
        f"pnl DROP {PNL} (-92.98%) equity DROP {EQUITY} (-1.2%) FTE JUMP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Alvinnenberg@2306; "
        f"AGB Bornem JR2024; FARO/AIESH YE2024; DISTINCT Katrinahof Scholen 0891.279.946; "
        f"not TE-additive of 348bn"
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
        "budget_id": "bud_katrinahof_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_katrinahof_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +6.78% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_katrinahof_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_katrinahof_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +3.39% vs {OMZET24}",
    },
    {
        "budget_id": "bud_katrinahof_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_katrinahof_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -92.98% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_katrinahof_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 DROP",
        "source_id": "src_katrinahof_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} DROP -1.2% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_katrinahof_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_katrinahof_jr2025_cw_en",
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
    "title": (
        f"Katrinahof YE2025 leftover dual (bruto 11.18m / omzet 1.07m ~{RATIO}x / "
        f"pnl DROP -93% / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "VAPH users / children youth adults with disability Antwerpen",
    "legal_basis": f"VZW Katrinahof (KBO {KBO}; Actief; 2 VE; NACE 87.201; VAPH OC)",
    "decision_date": "2026-06-02",
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
    "evaluation_url": "https://www.companyweb.be/en/0414830792/vzw-katrinahof",
    "stated_goal": "VAPH orthopedagogical care children/youth/adults with disability (Antwerp)",
    "cut_option": (
        f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -93% vs VAPH/PVF matrix"
    ),
    "source_id": "src_katrinahof_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Katrinahof>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Alvinnenberg@2306",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Katrinahof bruto 11.18m / omzet 1.07m ~{RATIO}x / pnl DROP -93% (YE2025)",
    "level": "L5",
    "type": "vaph_mpi_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Katrinahof>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+3.39%) / bruto JUMP {BRUTO} (~{RATIO}x / +6.78%) / "
        f"pnl DROP {PNL} (-92.98%) / equity DROP {EQUITY} (-1.2%) / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_katrinahof_jr2025_cw_en",
    "beneficiaries": "VAPH users Antwerpen Linkeroever",
    "stated_goal": "VAPH orthopedagogical residential/day care",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl DROP -93%; FTE {FTE}; VAPH subsidy opacity",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -93% vs VAPH/PVF"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Alvinnenberg@2306; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Katrinahof>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"VAPH/PVF matrix; pnl DROP EUR{PNL} (-92.98%) vs YE2024 EUR{PNL24}"
    ),
    "why_it_matters": (
        f"Medium CW shows Antwerp VAPH OC (bruto 11.18m / omzet 1.07m ~{RATIO}x / "
        f"pnl DROP -93% / FTE 141.8) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "VZW Katrinahof",
    "recipient_email": EMAIL,
    "recipient_postal": "Fromentinstraat 1, 2050 Antwerpen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Alvinnenberg@2306",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Katrinahof (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -93%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** VZW Katrinahof — KBO **{KBO}** (Actief; Fromentinstraat 1, 2050 Antwerpen; **2 VE**; FTE {FTE}; NACE **87.201**; VAPH OC)  
**recipient:** {EMAIL} · Fromentinstraat 1-3, 2050 Antwerpen (T 03 722 07 22)  
**sources:** [CW EN](https://www.companyweb.be/en/0414830792/vzw-katrinahof) · [CW NL](https://www.companyweb.be/nl/0414830792/vzw-katrinahof) · [CW FR](https://www.companyweb.be/fr/0414830792/vzw-katrinahof) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414830792) · [site](https://www.katrinahof.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0414830792)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **VZW KATRINAHOF** sinds **20.06.1974**; **2 VE**; zetel Fromentinstraat 1, 2050 Antwerpen; RSZ NACE **87.201**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +3.39%; bruto **EUR{BRUTO:,}** JUMP +6.78% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −92.98%; equity **EUR{EQUITY:,}** DROP −1.2%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After Alvinnenberg@2306. DISTINCT Katrinahof Scholen. Do NOT redo Alvinnenberg/TM Kempen/BC Sint-Elisabeth/Voluit/Kompas/Havinet stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: VZW Katrinahof
via {EMAIL}
Fromentinstraat 1-3, 2050 Antwerpen
Betreft: Openbaarmaking jaarrekening 2025 Katrinahof (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl DROP EUR{PNL} (−92.98% vs YE2024 EUR{PNL24}).
4. Overzicht publieke toelagen/PVF/VAPH-stromen YE2025.
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
            f"leftover dual — Katrinahof YE2025 Medium "
            f"(bruto JUMP 11.18m / ~{RATIO}x omzet / pnl DROP -93% / FTE JUMP 141.8)"
        )
        r["notes"] = (
            f"tick{TICK} Katrinahof {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl DROP {PNL}; "
            f"equity DROP {EQUITY}; FTE JUMP {FTE}; 2 VE NACE 87.201 VAPH Antwerpen; "
            f"neerlegging {FILED}; assets/debt Unknown; FOI ready NOT sent; "
            f"after Alvinnenberg@2306; stalls AGB/FARO YE2024; next EVERY-10 2310"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Katrinahof — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Katrinahof YE2025 Medium "
                f"(bruto 11.18m / omzet 1.07m ~{RATIO}x / pnl DROP -93%). "
                "Prefer AGB/FARO if YE2025 else FREE ETA-VAPH-WZC-maatwerk "
                "(Hejmen/Willekom/Zewopa/De Max/Iris Kontich if YE2025 unused; Gandae if YE2025). "
                "Do NOT redo Katrinahof/Alvinnenberg/TM Kempen/TMMA/BC Sint-Elisabeth/Voluit/"
                "Kompas/Havinet/MPI Oosterlo/Levensvreugde stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Katrinahof; AGB Bornem JR2024; FARO/AIESH YE2024; "
                f"next EVERY-10 2310"
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
            f"tick{TICK} leftover dual Katrinahof {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -92.98%; "
            f"equity DROP {EQUITY}; FTE JUMP {FTE}; 2 VE VAPH Antwerpen); after Alvinnenberg@2306; "
            f"AGB Bornem JR2024; FARO/AIESH YE2024; next {NEXT_RQ}; next EVERY-10 2310; "
            f"continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Katrinahof Antwerpen (bruto JUMP 11.18m / ~{RATIO}x omzet / pnl DROP -93% / Medium)

- Unit: **{RQ}** leftover dual after **Alvinnenberg@2306**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO still **YE2024**; AIESH still **YE2024**. Took unused FREE Flemish VAPH **VZW Katrinahof** YE2025 (KBO **{KBO}**; Fromentinstraat 1 Antwerpen; **Actief** **2 VE**; NACE **87.201**). Do not redo Alvinnenberg/TM Kempen/BC Sint-Elisabeth/Voluit/Kompas/Havinet stack. DISTINCT Katrinahof Scholen.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +3.39%; bruto **EUR{BRUTO}** JUMP +6.78% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -92.98%; equity **EUR{EQUITY}** DROP -1.2%; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {NEXT_RQ}.
"""
    )

print(
    f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x "
    f"pnl={PNL} pi={PI} next={NEXT_RQ}"
)
