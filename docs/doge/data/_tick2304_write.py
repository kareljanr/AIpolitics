# -*- coding: utf-8 -*-
"""Tick 2304: leftover dual BC Sint-Elisabeth Peer YE2025 VAPH after Voluit."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2304")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2304"
RQ = "rq_2304"
NEXT_RQ = "rq_2305"
ENTITY = "vzw_bc_sint_elisabeth_peer"
KBO = "0418.714.851"
GAP = "gap_bc_elisabeth_nbb_pdf_assets_debt_bruto_gt_omzet_11_8x_pnl_drop_70pct_equity_jump_vaph_matrix_l5"
LB = "lb_bc_elisabeth_bruto_26_44m_omzet_2_24m_11_8x_pnl_drop_70pct_jr2025"
COMM = "comm_bc_elisabeth_jr2025_statutory_bruto_gt_omzet_11_8x_pnl_drop_vaph"

OMZET = 2239635
OMZET24 = 2123518
BRUTO = 26440267
BRUTO24 = 25635405
PNL = 1561422
PNL24 = 5238400
EQUITY = 22964375
EQUITY24 = 21629892
FTE = 303.6
FTE24 = 297.8
FILED = "22.06.2026"
EMAIL = "info@bc-elisabeth.be"
RATIO = round(BRUTO / OMZET, 2)  # ~11.81

# cost 5.5 (~26.4m) · abs 7.8 (bruto~11.8x + pnl DROP -70% + equity JUMP) · diff 3
# pi = 0.55*5.5 + 0.35*7.8 + 0.1*7 = 6.455 → 6.45
ABS, COST, DIFF, PI = 7.8, 5.5, 3.0, 6.45


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
        f"BC Sint-Elisabeth Peer YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity JUMP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0418714851/begeleidingscentrum-sint-elisabeth\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418714851\n"
        "https://www.bc-elisabeth.be/contact/contacteer-ons/\n"
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
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
        "title": f"BC Sint-Elisabeth YE2025 CW EN (bruto 26.44m / omzet 2.24m ~{RATIO}x / pnl DROP -70%)",
        "url": "https://www.companyweb.be/en/0418714851/begeleidingscentrum-sint-elisabeth",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+5.47%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +3.14%); pnl DROP {PNL} (-70.19%); equity JUMP {EQUITY} (+6.17%); "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_bc_elisabeth_jr2025_cw_nl",
        "title": "BC Sint-Elisabeth YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0418714851/begeleidingscentrum-sint-elisabeth",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_bc_elisabeth_jr2025_cw_fr",
        "title": "BC Sint-Elisabeth YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0418714851/begeleidingscentrum-sint-elisabeth",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_bc_elisabeth_kbo_0418714851",
        "title": "KBO BC Sint-Elisabeth 0418.714.851 Actief VZW 2 VE NACE 87.201 Peer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418714851",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 18.05.1978; 2 VE; Sint Elisabethlaan 20 3990 Peer; "
            f"RSZ/BTW 87.201; Aanbestedende overheid; VAPH-recognised"
        ),
    },
    {
        "source_id": "src_bc_elisabeth_site_contact_2304",
        "title": "BC Sint-Elisabeth FOI channel info@bc-elisabeth.be / VAPH",
        "url": "https://www.bc-elisabeth.be/contact/contacteer-ons/",
        "publisher": "Begeleidingscentrum Sint-Elisabeth VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; {EMAIL}; Sint-Elisabethlaan 20 3990 Peer; T 011 39 95 00; "
            f"VAPH vergunde zorgaanbieder"
        ),
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Begeleidingscentrum Sint-Elisabeth VZW (Peer / VAPH)",
    "name_fr": "Centre d'accompagnement Sainte-Élisabeth ASBL (Peer / VAPH)",
    "name_en": "Guidance Centre Sint-Elisabeth VZW (Peer / VAPH residential care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.bc-elisabeth.be/",
    "foi_email": EMAIL,
    "foi_postal": "Sint-Elisabethlaan 20, 3990 Peer",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW "
        f"NACE 87.201 Aanbestedende overheid; omzet JUMP {OMZET} (+5.47%) bruto JUMP {BRUTO} "
        f"(~{RATIO}x / +3.14%) pnl DROP {PNL} (-70.19%) equity JUMP {EQUITY} (+6.17%) FTE JUMP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Voluit@2303; "
        f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; "
        f"DISTINCT Sint-Elisabeths Dal Zoutleeuw; not TE-additive of 348bn"
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
        "budget_id": "bud_bc_elisabeth_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +3.14% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_bc_elisabeth_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +5.47% vs {OMZET24}",
    },
    {
        "budget_id": "bud_bc_elisabeth_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -70.19% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_bc_elisabeth_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 JUMP",
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +6.17% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_bc_elisabeth_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_bc_elisabeth_jr2025_cw_en",
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
        f"BC Sint-Elisabeth YE2025 leftover dual (bruto 26.44m / omzet 2.24m ~{RATIO}x / "
        f"pnl DROP -70% / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "VAPH users / minors+adults with disability Peer-Limburg",
    "legal_basis": (
        f"VZW Begeleidingscentrum Sint-Elisabeth (KBO {KBO}; Actief; 2 VE; NACE 87.201; "
        f"Aanbestedende overheid; VAPH)"
    ),
    "decision_date": "2026-06-22",
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
    "evaluation_url": "https://www.companyweb.be/en/0418714851/begeleidingscentrum-sint-elisabeth",
    "stated_goal": "VAPH residential / day / ambulatory care for people with disability (Peer)",
    "cut_option": (
        f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -70% vs "
        f"VAPH/PVF matrix while equity JUMP +6%"
    ),
    "source_id": "src_bc_elisabeth_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Limburg>Peer>BC_SintElisabeth>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Voluit@2303",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"BC Sint-Elisabeth bruto 26.44m / omzet 2.24m ~{RATIO}x / pnl DROP -70% (YE2025)",
    "level": "L5",
    "type": "vaph_mpi_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Peer>BC_SintElisabeth>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+5.47%) / bruto JUMP {BRUTO} (~{RATIO}x / +3.14%) / "
        f"pnl DROP {PNL} (-70.19%) / equity JUMP {EQUITY} (+6.17%) / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_bc_elisabeth_jr2025_cw_en",
    "beneficiaries": "VAPH users Peer-Limburg",
    "stated_goal": "VAPH residential/day/ambulatory disability care",
    "measured_outcome": (
        f"bruto÷omzet ~{RATIO}x; pnl DROP -70%; equity JUMP +6%; FTE {FTE}; VAPH subsidy opacity"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -70% "
        f"vs VAPH/PVF while equity JUMP"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; after Voluit@2303; AGB Bornem JR2024; "
        f"FARO/AIESH YE2024"
    ),
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Peer>BC_SintElisabeth>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"VAPH/PVF financing matrix; pnl DROP EUR{PNL} (-70.19%) vs YE2024 EUR{PNL24} while "
        f"equity JUMP EUR{EQUITY} (+6.17%)"
    ),
    "why_it_matters": (
        f"Medium CW shows large VAPH VZW Peer (bruto 26.44m / omzet 2.24m ~{RATIO}x / "
        f"pnl DROP -70% / equity JUMP +6% / FTE 303.6) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Begeleidingscentrum Sint-Elisabeth VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Sint-Elisabethlaan 20, 3990 Peer",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Voluit@2303",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — BC Sint-Elisabeth Peer (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -70%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Begeleidingscentrum Sint-Elisabeth VZW — KBO **{KBO}** (Actief; Sint-Elisabethlaan 20, 3990 Peer; **2 VE**; FTE {FTE}; NACE **87.201**; Aanbestedende overheid; VAPH)  
**recipient:** {EMAIL} · Sint-Elisabethlaan 20, 3990 Peer (T 011 39 95 00)  
**sources:** [CW EN](https://www.companyweb.be/en/0418714851/begeleidingscentrum-sint-elisabeth) · [CW NL](https://www.companyweb.be/nl/0418714851/begeleidingscentrum-sint-elisabeth) · [CW FR](https://www.companyweb.be/fr/0418714851/begeleidingscentrum-sint-elisabeth) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418714851) · [contact](https://www.bc-elisabeth.be/contact/contacteer-ons/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0418714851)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **BEGELEIDINGSCENTRUM SINT - ELISABETH** sinds **18.05.1978**; **2 VE**; zetel Sint Elisabethlaan 20, 3990 Peer; RSZ NACE **87.201**; Aanbestedende overheid.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +5.47%; bruto **EUR{BRUTO:,}** JUMP +3.14% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −70.19%; equity **EUR{EQUITY:,}** JUMP +6.17%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Gandae YE2024. After Voluit@2303. Do NOT redo Voluit/MLP/Havinet/De Kiem/MPI Oosterlo/JOMI/De Okkernoot stack. DISTINCT Sint-Elisabeths Dal Zoutleeuw.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Begeleidingscentrum Sint-Elisabeth VZW
via {EMAIL}
Sint-Elisabethlaan 20, 3990 Peer
Betreft: Openbaarmaking jaarrekening 2025 BC Sint-Elisabeth (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) —
   VAPH/persoonsvolgende financiering matrix.
3. Toelichting pnl DROP EUR{PNL} (−70.19% vs YE2024 EUR{PNL24}) terwijl
   equity JUMP EUR{EQUITY} (+6.17%) en FTE JUMP {FTE}.
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
            f"leftover dual — BC Sint-Elisabeth Peer YE2025 Medium "
            f"(bruto JUMP 26.44m / ~{RATIO}x omzet / pnl DROP -70% / FTE JUMP 303.6)"
        )
        r["notes"] = (
            f"tick{TICK} BC Sint-Elisabeth {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl DROP {PNL}; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 2 VE NACE 87.201 VAPH Peer; "
            f"neerlegging {FILED}; assets/debt Unknown; FOI ready NOT sent; "
            f"after Voluit@2303; stalls AGB/FARO/AIESH YE2024; next EVERY-10 2310"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after BC Sint-Elisabeth — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after BC Sint-Elisabeth YE2025 Medium "
                f"(bruto 26.44m / omzet 2.24m ~{RATIO}x / pnl DROP -70%). "
                "Prefer leftover dual: AGB Bornem/APB → FARO/AIESH if YE2025 → Citeco/Groupe Foes "
                "if YE2025 → unused DSO/water/nuclear/IGS/HVZ or FREE ETA-VAPH-WZC-maatwerk "
                "(Gandae if YE2025; Thomas More Kempen / Katrinahof / Levensvreugde / Hejmen / "
                "Willekom / Zewopa if YE2025 unused). "
                "Do NOT redo BC Sint-Elisabeth/Voluit/MLP/Havinet/De Kiem/MPI Oosterlo/JOMI/"
                "De Stobbe/De Okkernoot/SOBO/Ryhove/TMMA/Entiris/Mirto/Blankedale/"
                "Werkmmaat/Lidwina/Zonnelied stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} BC Sint-Elisabeth; AGB Bornem JR2024; "
                f"FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; next EVERY-10 2310"
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
            f"tick{TICK} leftover dual BC Sint-Elisabeth {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -70.19%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 2 VE VAPH Peer); after Voluit@2303; "
            f"AGB Bornem JR2024; FARO/AIESH YE2024; next {NEXT_RQ}; next EVERY-10 2310; "
            f"continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} BC Sint-Elisabeth Peer (bruto JUMP 26.44m / ~{RATIO}x omzet / pnl DROP -70% / Medium)

- Unit: **{RQ}** leftover dual after **Voluit@2303**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Gandae still **YE2024**. Took unused FREE Flemish VAPH **Begeleidingscentrum Sint-Elisabeth VZW** YE2025 (KBO **{KBO}**; Sint-Elisabethlaan 20 Peer; **Actief** **2 VE**; NACE **87.201**; Aanbestedende overheid; VAPH). Do not redo Voluit/MLP/Havinet/De Kiem/MPI Oosterlo/JOMI/De Okkernoot/SOBO/Ryhove/TMMA stack. DISTINCT Sint-Elisabeths Dal Zoutleeuw.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +5.47% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +3.14% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -70.19% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +6.17%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk / TM Kempen-if-unused).
"""
    )

print(
    f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x "
    f"pnl={PNL} pi={PI} next={NEXT_RQ}"
)
