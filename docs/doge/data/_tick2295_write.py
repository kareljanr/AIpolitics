# -*- coding: utf-8 -*-
"""Tick 2295: finish in_progress Rozemarijn Keerbergen YE2025 leftover dual."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2295")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T16:15:00Z"
TICK = "2295"
RQ = "rq_2295"
NEXT_RQ = "rq_2296"
ENTITY = "vzw_rozemarijn_keerbergen"
KBO = "0436.599.077"
GAP = "gap_rozemarijn_nbb_pdf_assets_debt_bruto_gt_omzet_7_00x_pnl_jump_255pct_vaph_matrix_l5"
LB = "lb_rozemarijn_bruto_5_96m_omzet_0_85m_7_00x_pnl_jump_255pct_jr2025"
COMM = "comm_rozemarijn_jr2025_statutory_bruto_gt_omzet_7_00x_pnl_jump"

OMZET = 851570
OMZET24 = 773100
BRUTO = 5962647
BRUTO24 = 5450195
PNL = 209245
PNL24 = 58877
EQUITY = 5763526
EQUITY24 = 5589811
FTE = 62.2
FTE24 = 63.4
FILED = "29.06.2026"
EMAIL = "info@vzwrozemarijn.be"
RATIO = round(BRUTO / OMZET, 2)  # ~7.00

# cost 6.0 (~6m bruto) · abs 8.0 (bruto÷omzet ~7x + pnl JUMP 255%) · diff 3
# pi = 0.55*6 + 0.35*8 + 0.1*7 = 6.80
ABS, COST, DIFF, PI = 8.0, 6.0, 3.0, 6.80


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
        f"Rozemarijn YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0436599077/rozemarijn\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436599077\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "title": f"Rozemarijn YE2025 CW EN (bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255%)",
        "url": "https://www.companyweb.be/en/0436599077/rozemarijn",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+10.15%); bruto JUMP {BRUTO} (~{RATIO}x / +9.4%); pnl JUMP {PNL} (+255.39%); equity JUMP {EQUITY}; FTE DROP {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_rozemarijn_jr2025_cw_nl",
        "title": "Rozemarijn YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0436599077/rozemarijn",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_rozemarijn_jr2025_cw_fr",
        "title": "Rozemarijn YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0436599077/rozemarijn",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_rozemarijn_kbo_0436599077",
        "title": "KBO Rozemarijn 0436.599.077 Actief VZW 2 VE NACE 88.993 Aanbestedende overheid Keerbergen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436599077",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; VZW sinds 18.10.1988; 2 VE; Wageman 5 3140 Keerbergen; RSZ 88.993; Aanbestedende overheid; Werkgever RSZ",
    },
    {
        "source_id": "src_rozemarijn_site_contact_2295",
        "title": "Rozemarijn FOI channel info@vzwrozemarijn.be / vzwrozemarijn.be",
        "url": "https://www.vzwrozemarijn.be/",
        "publisher": "VZW Rozemarijn",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Wageman 5 3140 Keerbergen; VAPH disability care + CW NACE 88.993 adapted-work label",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Rozemarijn VZW (Keerbergen / VAPH handicapenzorg + CW NACE 88.993)",
    "name_fr": "Rozemarijn ASBL (Keerbergen / soins handicap VAPH + NACE 88.993)",
    "name_en": "Rozemarijn VZW (Keerbergen VAPH disability care / CW adapted-work NACE)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.vzwrozemarijn.be/",
    "foi_email": EMAIL,
    "foi_postal": "Wageman 5, 3140 Keerbergen",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW RSZ 88.993 Aanbestedende; "
        f"omzet JUMP {OMZET} (+10.15%) bruto JUMP {BRUTO} (~{RATIO}x / +9.4%) pnl JUMP {PNL} (+255.39%) "
        f"equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; "
        f"after Mo-Clean@2294; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_rozemarijn_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +9.4% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_rozemarijn_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +10.15% vs {OMZET24}",
    },
    {
        "budget_id": "bud_rozemarijn_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 JUMP",
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} JUMP +255.39% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_rozemarijn_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +3.11% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_rozemarijn_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_rozemarijn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} DROP vs {FTE24}",
    },
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": f"Rozemarijn YE2025 leftover dual (bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255% / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH cliënten / handicapenzorg Keerbergen-Haacht path",
    "legal_basis": f"VZW Rozemarijn (KBO {KBO}; Actief; 2 VE; RSZ 88.993; Aanbestedende overheid)",
    "decision_date": "2026-06-29",
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
    "evaluation_url": "https://www.companyweb.be/en/0436599077/rozemarijn",
    "stated_goal": "Flemish VAPH disability care / CW adapted-work label Keerbergen — persoonsvolgend budget path",
    "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x vs VAPH/PVB subsidy matrix; disclose pnl JUMP +255%",
    "source_id": "src_rozemarijn_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Keerbergen>Rozemarijn>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x omzet); after Mo-Clean@2294",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Rozemarijn bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255% (YE2025)",
    "level": "L5",
    "type": "vaph_maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Keerbergen>Rozemarijn>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+10.15%) / bruto JUMP {BRUTO} (~{RATIO}x / +9.4%) / "
        f"pnl JUMP {PNL} (+255.39%) / equity JUMP {EQUITY} / FTE DROP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_rozemarijn_jr2025_cw_en",
    "beneficiaries": "VAPH cliënten handicapenzorg Keerbergen",
    "stated_goal": "Flemish VAPH disability care / adapted-work NACE path",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl JUMP +255%; omzet JUMP +10%; FTE DROP {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x vs VAPH/PVB matrix",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Mo-Clean@2294; AGB Bornem JR2024; FARO/AIESH YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Keerbergen>Rozemarijn>NBB_PDF_assets_debt_bruto_gt_omzet_vaph",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"VAPH/PVB/gemeente/ESF subsidy matrix; pnl JUMP EUR{PNL} (+255.39%) vs YE2024 EUR{PNL24}; "
        f"activity split care vs CW NACE 88.993 label"
    ),
    "why_it_matters": (
        f"Medium CW shows Flemish VAPH/adapted-work VZW Keerbergen (bruto 5.96m / omzet 0.85m ~{RATIO}x / "
        f"pnl JUMP +255% / FTE 62.2) under public path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Rozemarijn VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Wageman 5, 3140 Keerbergen",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Mo-Clean@2294",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Rozemarijn (NBB PDF / bruto≫omzet ~{RATIO}x / pnl JUMP +255%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Rozemarijn VZW — KBO **{KBO}** (Actief; Wageman 5, 3140 Keerbergen; **2 VE**; FTE {FTE}; RSZ **88.993**; Aanbestedende overheid)  
**recipient:** {EMAIL} · Wageman 5, 3140 Keerbergen  
**sources:** [CW EN](https://www.companyweb.be/en/0436599077/rozemarijn) · [CW NL](https://www.companyweb.be/nl/0436599077/rozemarijn) · [CW FR](https://www.companyweb.be/fr/0436599077/rozemarijn) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436599077) · [site](https://www.vzwrozemarijn.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Rozemarijn**; **2 VE**; zetel Wageman 5, 3140 Keerbergen; RSZ NACE **88.993**; Aanbestedende overheid; begindatum 18.10.1988.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +10.15%; bruto **EUR{BRUTO:,}** JUMP +9.4% (~**{RATIO}x** omzet); pnl **EUR{PNL:,}** JUMP +255.39%; equity **EUR{EQUITY:,}**; FTE **{FTE}** DROP; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Aralea/Manupal/De Ploeg/Vlotter YE2024. After Mo-Clean@2294. Do NOT redo Mo-Clean/Den Azalee/NLZ/Labor/Intro Schoonmaak stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Rozemarijn VZW
via {EMAIL}
Wageman 5, 3140 Keerbergen
Betreft: Openbaarmaking jaarrekening 2025 Rozemarijn (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVB/gemeente/ESF-matrix.
3. Toelichting pnl JUMP EUR{PNL} (+255.39% vs YE2024 EUR{PNL24}).
4. Activiteitensplit zorg vs CW NACE 88.993-label YE2025.
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
            f"leftover dual — Rozemarijn YE2025 Medium "
            f"(bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255%)"
        )
        r["notes"] = (
            f"tick{TICK} Rozemarijn YE2025; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; pnl {PNL}; "
            f"equity {EQUITY}; FTE {FTE}; FOI ready NOT sent; after Mo-Clean@2294"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Rozemarijn — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Rozemarijn YE2025 Medium "
                f"(bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH if YE2025, else unused DSO/water/nuclear/IGS/HVZ, else unused "
                "ETA-VAPH-WZC-maatwerk (Aralea/Manupal/De Ploeg/Vlotter YE2024). "
                "Do NOT redo Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/Intro Schoonmaak/"
                "Buseloc/Op Maat/REW stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Rozemarijn; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
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
            f"tick{TICK} leftover dual Rozemarijn {KBO} Medium "
            f"(omzet JUMP {OMZET} +10.15%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +255.39%; "
            f"equity JUMP {EQUITY}; FTE DROP {FTE}; 2 VE Keerbergen VAPH/NACE 88.993); after Mo-Clean@2294; "
            f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            f"next {NEXT_RQ}; next every-10 2300; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Rozemarijn Keerbergen (bruto 5.96m / omzet 0.85m ~{RATIO}x / pnl JUMP +255% / Medium)

- Unit: **{RQ}** finish **in_progress** leftover dual after **rq_2294 Mo-Clean**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Aralea/Manupal/De Ploeg/Vlotter still **YE2024**. Took claimed FREE Flemish VAPH/adapted-work **Rozemarijn VZW** YE2025 (KBO **{KBO}**; Wageman 5 Keerbergen; **Actief** **2 VE**; RSZ **88.993**; Aanbestedende overheid). Do not redo Mo-Clean/Den Azalee/NLZ/Labor/Intro Schoonmaak/Buseloc/Op Maat/REW stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +10.15% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +9.4% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +255.39% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +3.11%; FTE **{FTE}** DROP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk).
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x pnl={PNL} pi={PI} next={NEXT_RQ}")
