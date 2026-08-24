# -*- coding: utf-8 -*-
"""Tick 2300 EVERY-10 + leftover dual: MPI Oosterlo Geel YE2025 VAPH."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2300")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2300"
RQ = "rq_2300"
NEXT_RQ = "rq_2301"
ENTITY = "vzw_mpi_oosterlo_geel"
KBO = "0414.326.293"
GAP = "gap_mpi_oosterlo_nbb_pdf_assets_debt_bruto_gt_omzet_10_7x_pnl_drop_72pct_equity_jump_vaph_matrix_l5"
LB = "lb_mpi_oosterlo_bruto_29_46m_omzet_2_76m_10_7x_pnl_drop_72pct_jr2025"
COMM = "comm_mpi_oosterlo_jr2025_statutory_bruto_gt_omzet_10_7x_pnl_drop_vaph"

OMZET = 2763794
OMZET24 = 2719687
BRUTO = 29463527
BRUTO24 = 27616128
PNL = 172880
PNL24 = 621237
EQUITY = 20252849
EQUITY24 = 16612538
FTE = 371.6
FTE24 = 362.5
FILED = "02.07.2026"
EMAIL = "info@mpi-oosterlo.be"
RATIO = round(BRUTO / OMZET, 2)  # ~10.66 → present as ~10.7x

# cost 5.5 (~29.5m) · abs 7.8 (bruto~10.7x + pnl DROP -72% + equity JUMP) · diff 3
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
        f"MPI Oosterlo YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity JUMP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0414326293/mpi-oosterlo\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414326293\n"
        "https://www.mpi-oosterlo.be/contact\n"
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
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
        "title": f"MPI Oosterlo YE2025 CW EN (bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72%)",
        "url": "https://www.companyweb.be/en/0414326293/mpi-oosterlo",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+1.62%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +6.69%); pnl DROP {PNL} (-72.17%); equity JUMP {EQUITY} (+21.91%); "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_mpi_oosterlo_jr2025_cw_nl",
        "title": "MPI Oosterlo YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0414326293/mpi-oosterlo",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_mpi_oosterlo_jr2025_cw_fr",
        "title": "MPI Oosterlo YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0414326293/mpi-oosterlo",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_mpi_oosterlo_kbo_0414326293",
        "title": "KBO MPI Oosterlo 0414.326.293 Actief VZW 1 VE NACE 87.201 Geel",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414326293",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 06.05.1974; 1 VE; Eindhoutseweg 25 2440 Geel; "
            f"RSZ/BTW 87.201; Aanbestedende overheid; email {EMAIL}; Tel 014 86 11 40"
        ),
    },
    {
        "source_id": "src_mpi_oosterlo_site_contact_2300",
        "title": "MPI Oosterlo FOI channel info@mpi-oosterlo.be / VAPH-recognised",
        "url": "https://www.mpi-oosterlo.be/contact",
        "publisher": "MPI Oosterlo VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; {EMAIL}; Eindhoutseweg 25 2440 Geel; VAPH-recognised residential care "
            f"for minors with mental disability"
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
    "name_nl": "MPI Oosterlo VZW (Geel / VAPH orthopedagogisch)",
    "name_fr": "MPI Oosterlo ASBL (Geel / soins résidentiels VAPH)",
    "name_en": "MPI Oosterlo VZW (Geel / VAPH residential care for minors with mental disability)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.mpi-oosterlo.be/",
    "foi_email": EMAIL,
    "foi_postal": "Eindhoutseweg 25, 2440 Geel",
    "notes": (
        f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE VZW "
        f"NACE 87.201 Aanbestedende overheid; omzet JUMP {OMZET} (+1.62%) bruto JUMP {BRUTO} "
        f"(~{RATIO}x / +6.69%) pnl DROP {PNL} (-72.17%) equity JUMP {EQUITY} (+21.91%) FTE JUMP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after JOMI@2299; "
        f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_mpi_oosterlo_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +6.69% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_mpi_oosterlo_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +1.62% vs {OMZET24}",
    },
    {
        "budget_id": "bud_mpi_oosterlo_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -72.17% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_mpi_oosterlo_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 JUMP",
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +21.91% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_mpi_oosterlo_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_mpi_oosterlo_jr2025_cw_en",
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
        f"MPI Oosterlo YE2025 leftover dual (bruto 29.46m / omzet 2.76m ~{RATIO}x / "
        f"pnl DROP -72% / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "VAPH-recognised residential care users / minors with mental disability Geel",
    "legal_basis": f"VZW MPI Oosterlo (KBO {KBO}; Actief; 1 VE; NACE 87.201; Aanbestedende overheid)",
    "decision_date": "2026-07-02",
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
    "evaluation_url": "https://www.companyweb.be/en/0414326293/mpi-oosterlo",
    "stated_goal": "VAPH residential / orthopedagogical care for minors with mental disability (Geel)",
    "cut_option": (
        f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -72% vs "
        f"VAPH/persoonsvolgende financiering matrix while equity JUMP +22%"
    ),
    "source_id": "src_mpi_oosterlo_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Geel>MPI_Oosterlo>JR2025_statutory_L5",
    "notes": (
        f"tick{TICK} EVERY-10; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after JOMI@2299"
    ),
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"MPI Oosterlo bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72% (YE2025)",
    "level": "L5",
    "type": "vaph_mpi_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Geel>MPI_Oosterlo>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+1.62%) / bruto JUMP {BRUTO} (~{RATIO}x / +6.69%) / "
        f"pnl DROP {PNL} (-72.17%) / equity JUMP {EQUITY} (+21.91%) / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_mpi_oosterlo_jr2025_cw_en",
    "beneficiaries": "VAPH residential care users / minors with mental disability Geel",
    "stated_goal": "VAPH orthopedagogical residential care",
    "measured_outcome": (
        f"bruto÷omzet ~{RATIO}x; pnl DROP -72%; equity JUMP +22%; FTE {FTE}; VAPH subsidy opacity"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -72% "
        f"vs VAPH/persoonsvolgende financing while equity JUMP"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; after JOMI@2299; AGB Bornem JR2024; "
        f"FARO/AIESH/Citeco/Groupe Foes YE2024"
    ),
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Geel>MPI_Oosterlo>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"VAPH/persoonsvolgende/Agentschap Opgroeien financing matrix; pnl DROP EUR{PNL} (-72.17%) vs "
        f"YE2024 EUR{PNL24} while equity JUMP EUR{EQUITY} (+21.91%)"
    ),
    "why_it_matters": (
        f"Medium CW shows large VAPH MPI VZW Geel (bruto 29.46m / omzet 2.76m ~{RATIO}x / "
        f"pnl DROP -72% / equity JUMP +22% / FTE 371.6) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "MPI Oosterlo VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Eindhoutseweg 25, 2440 Geel",
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
    "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; after JOMI@2299",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — MPI Oosterlo (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -72%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** MPI Oosterlo VZW — KBO **{KBO}** (Actief; Eindhoutseweg 25, 2440 Geel; **1 VE**; FTE {FTE}; NACE **87.201**; Aanbestedende overheid; VAPH-recognised)  
**recipient:** {EMAIL} · Eindhoutseweg 25, 2440 Geel (T 014 86 11 40)  
**sources:** [CW EN](https://www.companyweb.be/en/0414326293/mpi-oosterlo) · [CW NL](https://www.companyweb.be/nl/0414326293/mpi-oosterlo) · [CW FR](https://www.companyweb.be/fr/0414326293/mpi-oosterlo) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414326293) · [contact](https://www.mpi-oosterlo.be/contact) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0414326293)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **MPI Oosterlo** sinds **06.05.1974**; **1 VE**; zetel Eindhoutseweg 25, 2440 Geel; RSZ/BTW NACE **87.201**; Aanbestedende overheid; email {EMAIL}.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +1.62%; bruto **EUR{BRUTO:,}** JUMP +6.69% (~**{RATIO}x** omzet); pnl **EUR{PNL:,}** DROP −72.17%; equity **EUR{EQUITY:,}** JUMP +21.91%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Gandae YE2024. After JOMI@2299. Do NOT redo JOMI/De Stobbe/SOBO/Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/De Okkernoot stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: MPI Oosterlo VZW
via {EMAIL}
Eindhoutseweg 25, 2440 Geel
Betreft: Openbaarmaking jaarrekening 2025 MPI Oosterlo (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) —
   VAPH/persoonsvolgende financiering / Agentschap Opgroeien matrix.
3. Toelichting pnl DROP EUR{PNL} (−72.17% vs YE2024 EUR{PNL24}) terwijl
   equity JUMP EUR{EQUITY} (+21.91%) en FTE JUMP {FTE}.
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
            f"EVERY-10 + leftover dual — MPI Oosterlo YE2025 Medium "
            f"(bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72%)"
        )
        r["notes"] = (
            f"tick{TICK} EVERY-10 + MPI Oosterlo {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl DROP {PNL}; equity JUMP {EQUITY}; "
            f"FTE JUMP {FTE}; 1 VE NACE 87.201 VAPH Geel; neerlegging {FILED}; assets/debt Unknown; "
            f"FOI ready NOT sent; progress+waste top10 refreshed; stalls AGB Bornem JR2024 / "
            f"FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; after JOMI@2299; next EVERY-10 2310"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after MPI Oosterlo — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after MPI Oosterlo YE2025 Medium "
                f"(bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72%). "
                "Prefer leftover dual: AGB Bornem/APB → FARO/AIESH if YE2025 → Citeco/Groupe Foes "
                "if YE2025 → unused DSO/water/nuclear/IGS/HVZ or FREE ETA-VAPH-WZC-maatwerk "
                "(Gandae if YE2025; Aralea/Manupal/De Ploeg/Vlotter if YE2025). "
                "Do NOT redo MPI Oosterlo/JOMI/De Stobbe/SOBO/Ryhove/Rozemarijn/Mo-Clean/"
                "Den Azalee/NLZ/De Okkernoot/Labor/Intro/Buseloc/Ateljee/Borgerstein/"
                "Waak/InterWest/BWB/Wroeter/Springplank/Stroom stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} MPI Oosterlo EVERY-10; AGB Bornem JR2024; "
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
            f"tick{TICK} EVERY-10 + leftover dual MPI Oosterlo {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -72.17%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE VAPH Geel); after JOMI@2299; "
            f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2310; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

# EVERY-10 progress + waste top10
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick {TICK}** ({UTC[:10]})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2291-2300 continuum; AGB Bornem / FARO / AIESH / Citeco / Groupe Foes still YE2024 stalls; Gandae still YE2024; **MPI Oosterlo unlocked YE2025@2300** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2291-2300 is residual dual L5 (not near-complete of 348bn):** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Okkernoot · JOMI · EVERY-10 primary **MPI Oosterlo bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72% / FTE 371.6** (Medium CW) |
| **E. FOI-ready gaps** | **~1972** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~2024** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2291-2300** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Okkernoot · JOMI · **MPI Oosterlo** · prior 2281-2290 REW/Op Maat/Buseloc stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53842+ |
| commitments.csv | 6023+ |
| leaderboard.csv | 8143+ |
| entities.csv | 2047+ |
| sources.csv | 6658+ |
| FOI ready | ~1972 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~2024 |
| research_queue open | {NEXT_RQ} after MPI Oosterlo EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2290

- **Residual dual (tick2291-2300):** **Intro Schoonmaak** · **Labor Arbeidskansen** · **NLZ** · **Mo-Clean** (Stopgezet fusie) · **Rozemarijn** · **Ryhove** · **SOBO@werk** (YE2025 unlocked) · **De Okkernoot** · **JOMI** · EVERY-10 primary **MPI Oosterlo** (bruto **29.46m** / omzet **2.76m** ~**{RATIO}x** / pnl DROP **-72%** / equity JUMP **+22%** / FTE **371.6**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH YE2024-only · Citeco / Groupe Foes YE2024 · Gandae YE2024 · Aralea / Manupal / De Ploeg / Vlotter YE2024 · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
with open(os.path.join(DATA, "progress_every_10_ticks.md"), "w", encoding="utf-8") as f:
    f.write(progress)

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({UTC[:10]}) · **8143+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2291-2300:** **MPI Oosterlo bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72% / FTE 371.6** (EVERY-10@{TICK} primary) · JOMI · De Okkernoot · SOBO · Ryhove · Rozemarijn · Mo-Clean · NLZ · Labor · Intro Schoonmaak · prior 2281-2290 REW/Op Maat/Buseloc stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2290:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2291-2300 (off pure top10 / dual):** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Okkernoot · JOMI · **MPI Oosterlo bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72% / FTE 371.6** (EVERY-10@{TICK} primary). Count NEW since 2290: ~10 residual dual fills. **Prior 2281-2290 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **MPI Oosterlo** EVERY-10 primary bruto **EUR29.46m** / omzet **EUR2.76m** ~**{RATIO}x** / pnl DROP **-72%** / equity JUMP **+22%** / FTE **371.6** — Geel VAPH MPI opacity.
- **De Okkernoot** bruto **EUR13.44m** / ~**5.4x** omzet / pnl JUMP / FTE **143.3**.
- **Ryhove** bruto **EUR17.67m** / ~**2.2x** omzet / FTE **406.5**.
- **Rozemarijn** bruto **EUR5.96m** / ~**7.0x** omzet / pnl JUMP **+255%**.
- **SOBO@werk** bruto **EUR4.53m** / ~**1.85x** / pnl DROP **-54%**.
- **JOMI** bruto **EUR1.98m** / empty omzet / pnl DROP **-33%**.
- **Op Maat** prior EVERY-10 bruto **EUR2.35m** / empty omzet / pnl JUMP (retained).
- **REW** prior omzet **EUR14.72m** / bruto~**0.6x** / PROFIT FLIP (retained).
"""
with open(os.path.join(DATA, "doge_waste_top10_current.md"), "w", encoding="utf-8") as f:
    f.write(waste)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} EVERY-10 + MPI Oosterlo Geel (bruto 29.46m / omzet 2.76m ~{RATIO}x / pnl DROP -72% / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **JOMI@2299**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Gandae still **YE2024**. Took unused FREE Flemish VAPH MPI **MPI Oosterlo VZW** YE2025 (KBO **{KBO}**; Eindhoutseweg 25 Geel; **Actief** **1 VE**; NACE **87.201**; Aanbestedende overheid; VAPH-recognised). Do not redo JOMI/De Stobbe/SOBO/Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/De Okkernoot/Labor/Intro/Buseloc/Ateljee/Borgerstein/Waak/InterWest stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +1.62% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +6.69% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -72.17% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +21.91%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 1 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/; **EVERY-10** refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md`.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 @ {TICK}** (last was 2290; next **2310**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk).
"""
    )

print(
    f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x "
    f"pnl={PNL} pi={PI} next={NEXT_RQ} EVERY-10"
)
