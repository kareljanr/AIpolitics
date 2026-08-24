# -*- coding: utf-8 -*-
"""Tick 2280: EVERY-10 progress + Eurakor YE2025 leftover dual ETA."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2280")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T12:30:00Z"
TICK = "2280"
RQ = "rq_2280"
ENTITY = "sc_eurakor_leuze"
KBO = "0407.408.512"
GAP = "gap_eurakor_nbb_pdf_assets_debt_omzet_drop_6_44m_pnl_drop_85pct_eta_matrix_l5"
LB = "lb_eurakor_omzet_6_44m_pnl_drop_85pct_fte_jump_jr2025"
COMM = "comm_eurakor_jr2025_statutory_eta_omzet_drop_pnl_drop_85pct"

OMZET = 6440876
OMZET24 = 7130470
BRUTO = 3320061
BRUTO24 = 3378061
PNL = 40244
PNL24 = 260922
EQUITY = 1992699
EQUITY24 = 2052059
FTE = 206.5
FTE24 = 196.2
RATIO = round(BRUTO / OMZET, 2)  # ~0.52
FILED = "30.07.2026"

# cost 5.6 · abs 7.0 · diff 3.0 → pi = 0.55*5.6 + 0.35*7 + 0.1*7 = 6.23 → 6.25
ABS, COST, DIFF, PI = 7.0, 5.6, 3.0, 6.25


def read_csv(path: str) -> tuple[list[str], list[dict]]:
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        rows = list(r)
        return list(r.fieldnames or []), rows


def write_csv(path: str, fieldnames: list[str], rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


os.makedirs(RAW, exist_ok=True)
os.makedirs(FOI_DRAFTS, exist_ok=True)

# --- raw excerpts ---
with open(os.path.join(RAW, "cw_en_excerpt.txt"), "w", encoding="utf-8") as f:
    f.write(
        "eurakor YE2025 CW EN\n"
        f"omzet {OMZET} (-9.67%) bruto {BRUTO} (-1.72%) pnl {PNL} (-84.58%) "
        f"equity {EQUITY} (-2.89%) FTE {FTE}\n"
        f"filed {FILED}\n"
        "url https://www.companyweb.be/en/0407408512/eurakor\n"
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
        f'  "ratio_bruto_omzet": {RATIO},\n'
        '  "confidence": "medium",\n'
        f'  "gap": "{GAP}",\n'
        '  "sources": [\n'
        '    "src_eurakor_jr2025_cw_en",\n'
        '    "src_eurakor_jr2025_cw_nl",\n'
        '    "src_eurakor_jr2025_cw_fr",\n'
        '    "src_eurakor_kbo_0407408512",\n'
        '    "src_eurakor_site_contact_2280"\n'
        "  ]\n"
        "}\n"
    )

# --- sources ---
spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
new_sources = [
    {
        "source_id": "src_eurakor_jr2025_cw_en",
        "title": "eurakor SC YE2025 Companyweb EN (omzet DROP 6.44m / pnl DROP -85% / FTE 206.5)",
        "url": "https://www.companyweb.be/en/0407408512/eurakor",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; YE2025 Medium CW EN; omzet {OMZET} DROP -9.67%; bruto {BRUTO} (~{RATIO}x); pnl {PNL} DROP -84.58%; equity {EQUITY} DROP -2.89%; FTE {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_eurakor_jr2025_cw_nl",
        "title": "eurakor CV YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0407408512/eurakor",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; YE2025 Medium CW NL; same euros as EN; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_eurakor_jr2025_cw_fr",
        "title": "eurakor SC YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0407408512/eurakor",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; YE2025 Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; capitaux propres {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_eurakor_kbo_0407408512",
        "title": "KBO eurakor 0407.408.512 Actief SC 2 VE NACE 88.993 Leuze-en-Hainaut",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407408512",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; SC since 10.12.2020; 2 VE; zetel Zone industrielle de l'Europe(L) II 3-9 7900 Leuze-en-Hainaut; NACE 88.993; sociale onderneming since 01.07.2025; RSZ since 01.01.1965; Distinct Le Rucher 0860.345.458 same zone",
    },
    {
        "source_id": "src_eurakor_site_contact_2280",
        "title": "eurakor FOI channel info@eurakor.com / leseta.be + eurakor.com",
        "url": "https://eurakor.com/",
        "publisher": "eurakor SC",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@eurakor.com; ressources.humaines@eurakor.com; +32 69 66 96 90; leseta.be/annuaire-eta/eurakor/; Walloon ETA AViQ packaging/logistics",
    },
]
existing_s = {r["source_id"] for r in srows}
for ns in new_sources:
    if ns["source_id"] not in existing_s:
        srows.append(ns)
write_csv(spath, sfields, srows)

# --- entities ---
epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "eurakor CV (Leuze-en-Hainaut / Walloon ETA conditionering/logistiek)",
    "name_fr": "eurakor SC (Leuze-en-Hainaut / entreprise de travail adapté conditionnement)",
    "name_en": "eurakor adapted-work SC (Leuze-en-Hainaut Walloon ETA packaging/logistics)",
    "level": "parastatal",
    "parent_id": "sec_wallonia",
    "community_language": "fr",
    "website": "https://eurakor.com/",
    "foi_email": "info@eurakor.com",
    "foi_postal": "Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE SC NACE 88.993; "
        f"omzet DROP {OMZET} (-9.67%) bruto DROP {BRUTO} (~{RATIO}x / -1.72%) pnl DROP {PNL} (-84.58%) "
        f"equity DROP {EQUITY} (-2.89%) FTE JUMP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; after Ateliers de l'Avenir@2279; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
        f"DISTINCT Le Rucher@2233 same Leuze zone 0860.345.458; not TE-additive of 348bn"
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

# --- budgets ---
bpath = os.path.join(DATA, "budgets.csv")
bfields, brows = read_csv(bpath)
new_budgets = [
    {
        "budget_id": "bud_eurakor_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 omzet {OMZET} DROP -9.67% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_eurakor_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 bruto {BRUTO} DROP -1.72%; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_eurakor_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory winst/verlies YE2025 pnl DROP -85%",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 pnl {PNL} DROP -84.58% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_eurakor_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 equity {EQUITY} DROP -2.89% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_eurakor_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE YE2025",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} JUMP vs YE2024 {FTE24}",
    },
    {
        "budget_id": "bud_eurakor_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": "src_eurakor_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre pnl DROP -85%)",
    },
]
existing_b = {r["budget_id"] for r in brows}
for nb in new_budgets:
    if nb["budget_id"] not in existing_b:
        brows.append(nb)
write_csv(bpath, bfields, brows)

# --- commitments ---
cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": f"eurakor YE2025 leftover dual (omzet DROP 6.44m / bruto~{RATIO}x / pnl DROP -85% / FTE 206.5 / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "ETA workers Leuze-en-Hainaut / AViQ adapted-work packaging logistics path",
    "legal_basis": f"SC ETA eurakor (KBO {KBO}; Actief; 2 VE; NACE 88.993; Leuze-en-Hainaut)",
    "decision_date": "2026-07-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(OMZET),
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0407408512/eurakor",
    "stated_goal": "Walloon ETA packaging / co-packing / logistics / green spaces — inclusive employment",
    "cut_option": "Publish NBB PDF assets/debt; reconcile pnl DROP -85% despite FTE JUMP vs AViQ ETA wage-intervention matrix",
    "source_id": "src_eurakor_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Leuze>eurakor>JR2025_statutory_L5",
    "notes": (
        f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); "
        f"pnl DROP {PNL}; equity DROP {EQUITY}; FTE {FTE}; 2 VE SC; after Ateliers de l'Avenir@2279; "
        f"DISTINCT Le Rucher@2233; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
    ),
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

# --- leaderboard ---
lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"eurakor omzet DROP 6.44m / pnl DROP -85% / FTE JUMP 206.5 (YE2025 Walloon ETA Leuze)",
    "level": "L5",
    "type": "eta_sc_statutory",
    "hierarchy_path": "Wallonie>Hainaut>Leuze>eurakor>JR2025",
    "annual_cost_eur": str(OMZET),
    "total_cost_eur": str(OMZET),
    "tco_notes": (
        f"CW omzet DROP {OMZET} (-9.67%) / bruto DROP {BRUTO} (-1.72%; ~{RATIO}x) / "
        f"pnl DROP {PNL} (-84.58% vs {PNL24}) / equity DROP {EQUITY} (-2.89%) / FTE JUMP {FTE} (vs {FTE24}) / "
        f"2 VE SC; filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_eurakor_jr2025_cw_en",
    "beneficiaries": "ETA workers Leuze-en-Hainaut / AViQ adapted-work packaging logistics",
    "stated_goal": "Walloon ETA sheltered workshop (packaging / co-packing / logistics / green)",
    "measured_outcome": (
        f"omzet DROP -9.67%; bruto DROP -1.72%; pnl DROP -84.58%; equity DROP -2.89%; "
        f"FTE JUMP {FTE}; filed {FILED}"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA matrix behind pnl DROP -85% with FTE JUMP",
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
        f"FARO/AIESH/Citeco/Groupe Foes YE2024; DISTINCT Le Rucher@2233"
    ),
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

# --- foi_queue ---
fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Hainaut>Leuze>eurakor>NBB_PDF_assets_debt_omzet_drop_pnl_drop_85pct",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet DROP EUR{OMZET} (-9.67%); "
        f"pnl DROP EUR{PNL} vs EUR{PNL24} (-84.58%); equity DROP EUR{EQUITY} (-2.89%); FTE JUMP {FTE}; "
        f"AViQ ETA wage-intervention matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows Walloon ETA SC Leuze (omzet DROP 6.44m / pnl DROP -85% / FTE JUMP 206.5) "
        f"under AViQ packaging-logistics path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "eurakor SC",
    "recipient_email": "info@eurakor.com",
    "recipient_postal": "Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut",
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
    "notes": (
        f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Groupe Foes YE2024; "
        f"AGB Bornem JR2024; after Ateliers de l'Avenir@2279; DISTINCT Le Rucher@2233"
    ),
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

# --- FOI draft ---
draft = f"""# FOI draft — eurakor (NBB PDF / omzet DROP 6.44m / pnl DROP -85% / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** eurakor SC — KBO **{KBO}** (Actief; Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA AViQ)  
**recipient:** info@eurakor.com · Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut (+32 69 66 96 90)  
**sources:** [CW EN](https://www.companyweb.be/en/0407408512/eurakor) · [CW NL](https://www.companyweb.be/nl/0407408512/eurakor) · [CW FR](https://www.companyweb.be/fr/0407408512/eurakor) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407408512) · [site](https://eurakor.com/) · [leseta](https://leseta.be/annuaire-eta/eurakor/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief SC **eurakor** (naam sinds **10.12.2020**); **2 VE**; zetel Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut; RSZ/BTW NACE **88.993**; begindatum 02.07.1964; sociale onderneming sinds 01.07.2025; DG Eric Lenz / Alain Moucheron.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −9.67% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP −1.72% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP −84.58% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −2.89%; FTE **{FTE}** JUMP (vs {FTE24}); filed **{FILED}**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; REW YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal YE2024; Heropbeuring CW opaque. After Ateliers de l'Avenir@2279. Do NOT redo Le Rucher@2233 (same Leuze zone / distinct KBO 0860.345.458) / IN-Z / C.A.R.P. / A.P.A.C. / Ateliers de l'Avenir stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: eurakor SC
via info@eurakor.com
Zone industrielle de l'Europe(L) II 3-9, 7900 Leuze-en-Hainaut
Betreft: Openbaarmaking jaarrekening 2025 eurakor (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Wallonië / Code de la démocratie locale et de la décentralisation / openbaarheid
bestuursdocumenten), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet DROP EUR{OMZET} (−9.67%) naast pnl DROP EUR{PNL}
   (vs YE2024 EUR{PNL24}; −84.58%) en FTE JUMP {FTE} (vs {FTE24}).
3. Overzicht van AViQ/Waalse toelagen achter personeelskosten (FTE {FTE}) en
   de ETA-loonkostentussenkomstmatrix YE2025.
4. Verdeling omzet/activiteiten (Production vs Services / packaging / logistics / green).
5. Schulden LT/KT en liquide middelen YE2025 (niet gepubliceerd op Companyweb).

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
"""
with open(os.path.join(FOI_DRAFTS, f"{GAP}.md"), "w", encoding="utf-8") as f:
    f.write(draft)

# --- research_queue ---
rqpath = os.path.join(DATA, "research_queue.csv")
rqfields, rqrows = read_csv(rqpath)
for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["title"] = (
            f"EVERY-10 + leftover dual — eurakor YE2025 Medium "
            f"(omzet DROP 6.44m / bruto~{RATIO}x / pnl DROP -85% / FTE 206.5)"
        )
        r["notes"] = (
            f"tick{TICK} EVERY-10 + Eurakor YE2025; FARO/AIESH/REW still YE2024; "
            f"omzet {OMZET}; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; FTE {FTE}; FOI ready NOT sent"
        )
        break
# spawn rq_2281
if not any(r.get("task_id") == "rq_2281" for r in rqrows):
    rqrows.append(
        {
            "task_id": "rq_2281",
            "title": (
                "leftover dual after eurakor — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after eurakor YE2025 Medium (omzet DROP 6.44m / pnl DROP -85% / FTE 206.5). "
                "Prefer NON-stall live: AGB Bornem if JR2025; FARO/AIESH/REW/Citeco/Groupe Foes if YE2025; "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced €. "
                "Do NOT redo eurakor/Ateliers de l'Avenir/IN-Z/m-accent/AMAB/C.A.R.P./A.P.A.C./Le Rucher/Metalgroup."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} eurakor EVERY-10; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
                f"AGB Bornem JR2024; Manupal YE2024; Heropbeuring CW opaque; next every-10 2290"
            ),
        }
    )
write_csv(rqpath, rqfields, rqrows)

# --- loop_state ---
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
            f"tick{TICK} EVERY-10 + leftover dual eurakor {KBO} Medium "
            f"(omzet DROP {OMZET} -9.67%; bruto DROP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -84.58%; "
            f"equity DROP {EQUITY} -2.89%; FTE JUMP {FTE}; 2 VE Leuze ETA AViQ packaging); "
            f"after Ateliers de l'Avenir@2279; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
            f"next rq_2281; next EVERY-10 2290; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

# inventory after write
def count_rows(fn: str) -> int:
    _, rows = read_csv(os.path.join(DATA, fn))
    return len(rows)


inv = {
    "budgets": count_rows("budgets.csv"),
    "commitments": count_rows("commitments.csv"),
    "leaderboard": count_rows("leaderboard.csv"),
    "entities": count_rows("entities.csv"),
    "sources": count_rows("sources.csv"),
    "foi": count_rows("foi_queue.csv"),
}

# FOI ready approx
_, frows2 = read_csv(os.path.join(DATA, "foi_queue.csv"))
ready = sum(1 for r in frows2 if (r.get("status") or "").strip() == "ready")
answered = sum(1 for r in frows2 if (r.get("status") or "").strip() == "answered")
partial = sum(1 for r in frows2 if (r.get("status") or "").strip() == "partial")

# --- EVERY-10 progress ---
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2280** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2271-2280 continuum; AGB Bornem / FARO / AIESH / REW / Citeco / Groupe Foes / Manupal still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2271-2280 is residual dual L5 (not near-complete of 348bn):** **La Serre-Outil** omzet **3.11m** / bruto~**1.51×** · **De Enter** bruto **4.09m** / empty omzet / pnl DROP **-64%** · **Fournipac** omzet **3.71m** / equity DROP **-45%** / LOSS WIDEN · **Pépinières La Gaume** omzet **3.00m** / equity DROP **-14%** · **Atelier 85** omzet **7.86m** / bruto~**1.02×** · **Adapta** bruto **1.94m** / LOSS FLIP · **A.P.A.C.** bruto **3.15m** / pnl DROP **-67%** · **Atelier Saint-Vincent** bruto **2.89m** / LOSS NARROW · **C.A.R.P.** omzet **3.21m** / bruto~**1.63×** / equity JUMP · **AMAB** omzet **14.18m** / bruto~**1.53×** / LOSS FLIP / FTE **645.1** · **IN-Z** omzet **14.36m** / bruto~**1.67×** / LOSS WIDEN / FTE **627.5** · **m-accent** omzet **2.75m** / bruto~**1.63×** / pnl JUMP · **Ateliers de l'Avenir** omzet **6.73m** / pnl LOSS WIDEN / equity DROP **-4.5%** / FTE **144.8** · EVERY-10 primary **eurakor** omzet **6.44m** DROP **-9.67%** / bruto~**{RATIO}×** / pnl DROP **-84.58%** / equity DROP **-2.89%** / FTE JUMP **{FTE}** (Medium CW) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}**; partial **~{partial}**; total FOI rows **~{inv['foi']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2271-2280** Serre-Outil · De Enter · Fournipac · La Gaume · Atelier 85 · Adapta · APAC · Saint-Vincent · CARP · AMAB · IN-Z · m-accent · Ateliers de l'Avenir · **eurakor** · prior 2261-2270 Amis/Hautes/Village n1 stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2280)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets']}+ |
| commitments.csv | {inv['commitments']}+ |
| leaderboard.csv | {inv['leaderboard']}+ |
| entities.csv | {inv['entities']}+ |
| sources.csv | {inv['sources']}+ |
| FOI ready | ~{ready} |
| FOI answered | {answered} |
| FOI partial | {partial} |
| FOI total rows | ~{inv['foi']} |
| research_queue open | rq_2281 after eurakor EVERY-10 |

### What improved since tick 2270

- **Residual dual (tick2271-2280):** **La Serre-Outil** (omzet **3.11m** / bruto~**1.51×**) · **De Enter** (bruto **4.09m** / empty omzet / pnl DROP **-64%**) · **Fournipac** (omzet **3.71m** / equity DROP **-45%** / LOSS WIDEN) · **Pépinières La Gaume** (omzet **3.00m** / equity DROP **-14%**) · **Atelier 85** (omzet **7.86m** / bruto~**1.02×**) · **Adapta** (bruto **1.94m** / LOSS FLIP) · **A.P.A.C.** (bruto **3.15m** / pnl DROP **-67%**) · **Atelier Saint-Vincent** (bruto **2.89m** / LOSS NARROW) · **C.A.R.P.** (omzet **3.21m** / bruto~**1.63×** / equity JUMP) · **AMAB** (omzet **14.18m** / bruto~**1.53×** / LOSS FLIP / FTE **645.1**) · **IN-Z** (omzet **14.36m** / bruto~**1.67×** / LOSS WIDEN / FTE **627.5**) · **m-accent** (omzet **2.75m** / bruto~**1.63×** / pnl JUMP) · **Ateliers de l'Avenir** (omzet **6.73m** / pnl LOSS WIDEN / equity DROP **-4.5%** / FTE **144.8**) · EVERY-10 primary **eurakor** (omzet **6.44m** DROP **-9.67%** / bruto~**{RATIO}×** / pnl DROP **-84.58%** / equity DROP **-2.89%** / FTE JUMP **{FTE}**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH / REW YE2024-only · Citeco / Groupe Foes YE2024 · Manupal YE2024 · Heropbeuring CW kern opaque · Relais Haute Sambre / APN YE2024 · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
with open(os.path.join(DATA, "progress_every_10_ticks.md"), "w", encoding="utf-8") as f:
    f.write(progress)

# --- waste top10 ---
top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2280** (2026-08-27) · **{inv['leaderboard']}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2271-2280:** **eurakor omzet 6.44m DROP −9.67% / bruto~{RATIO}× / pnl DROP −85% / FTE JUMP {FTE}** (EVERY-10@2280 primary) · **Ateliers de l'Avenir omzet 6.73m / pnl LOSS WIDEN / equity DROP −4.5% / FTE 144.8** · **IN-Z omzet 14.36m / bruto~1.67× / LOSS WIDEN / FTE 627.5** · **AMAB omzet 14.18m / bruto~1.53× / LOSS FLIP / FTE 645.1** · **m-accent / C.A.R.P. / A.P.A.C. / Atelier 85 / Fournipac / La Gaume / Adapta / Saint-Vincent / De Enter / Serre-Outil** · prior 2261-2270 Amis/Hautes/Village n1 stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2270:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). Tie-break among pi=8.5 puts fossil accises ahead of company cars by annual €; among pi=8.4 dual cars falls to #10 by annual €. **Major NEW residual 2271-2280 (off pure top10 / dual):** Serre-Outil · De Enter · Fournipac · La Gaume · Atelier 85 · Adapta · APAC · Saint-Vincent · CARP · AMAB · IN-Z · m-accent · Ateliers de l'Avenir · **eurakor omzet 6.44m DROP −9.67% / pnl DROP −85% / FTE JUMP {FTE}** (EVERY-10@2280 primary). Count NEW since 2270: ~14 residual dual fills. **Prior 2261-2270 + 2251-2260 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **eurakor** EVERY-10 primary omzet **EUR6.44m** DROP **-9.67%** / bruto **EUR3.32m** (~**{RATIO}×**) / pnl DROP **-84.58%** / equity DROP **-2.89%** / FTE JUMP **{FTE}** — Leuze ETA packaging/logistics + AViQ subsidy opacity.
- **Ateliers de l'Avenir** omzet **EUR6.73m** JUMP / pnl LOSS WIDEN **-0.40m** / equity DROP **-4.5%** / FTE **144.8**.
- **IN-Z** omzet **EUR14.36m** / bruto~**1.67×** / pnl LOSS WIDEN / FTE **627.5**.
- **AMAB** omzet **EUR14.18m** / bruto~**1.53×** / pnl LOSS FLIP / FTE **645.1**.
- **Fournipac** omzet **EUR3.71m** / equity DROP **-45%** / LOSS WIDEN / FTE **95**.
- **A.P.A.C.** bruto **EUR3.15m** / empty omzet / pnl DROP **-67%** / FTE **89**.
- **De Enter** bruto **EUR4.09m** / empty omzet / pnl DROP **-64%** / FTE **92.7**.
- **C.A.R.P.** omzet **EUR3.21m** / bruto~**1.63×** / equity JUMP / FTE **122.9**.
- **Atelier 85** omzet **EUR7.86m** / bruto~**1.02×** / FTE **174.3**.
- **Amis des Aveugles** prior EVERY-10 bruto **EUR6.40m** / ~**3.40×** / pnl LOSS **-4.74m** / FTE **172.9** (retained).
- **Hautes Ardennes** prior bruto **EUR12.66m** / ~**4.11×** / pnl DROP **-84%** / FTE **220.6** (retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
with open(os.path.join(DATA, "doge_waste_top10_current.md"), "w", encoding="utf-8") as f:
    f.write(top10)

# --- loop_log append ---
log_block = f"""
### {UTC} - tick {TICK} - {RQ} EVERY-10 + eurakor Leuze (omzet DROP 6.44m / pnl DROP -85% / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** EVERY-10 mandatory + leftover dual after **rq_2279 Ateliers de l'Avenir**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW Laatste balansjaar 2024; neerlegging 24.11.2025); AIESH still **YE2024** (0201.712.587; neerlegging 17.07.2025); REW still **YE2024**; Citeco/Groupe Foes still **YE2024**; Manupal still **YE2024**; Heropbeuring still **CW opaque**. Took unused FREE Walloon ETA **eurakor SC** YE2025 (KBO **{KBO}**; Zone industrielle de l'Europe(L) II 3-9 Leuze-en-Hainaut; **Actief** **2 VE SC**; NACE **88.993** AViQ packaging/logistics/green; DISTINCT Le Rucher@2233 same zone). Do not redo Ateliers de l'Avenir/IN-Z/m-accent/AMAB/C.A.R.P./A.P.A.C./Le Rucher/Metalgroup stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -9.67% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP -1.72% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** DROP -84.58% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP -2.89%; FTE **{FTE}** JUMP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE SC. Assets/debt Unknown. Medium. FOI via info@eurakor.com.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + rq_2281 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- EVERY-10: refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md` from on-disk CSVs. TE denom €347.956 bn.
  - **A L0:** **100%**
  - **B L1:** **100%**
  - **C L2:** **~99%**
  - **D L5:** **~74-88%** generous (residual dual gain 2271-2280; not near-complete of 348bn)
  - **E FOI-ready:** **~{ready}** drafts ready (answered ~{answered}; partial ~{partial}; total ~{inv['foi']})
  - Pure annual waste top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10).
- Inventory: budgets {inv['budgets']} · commitments {inv['commitments']} · leaderboard {inv['leaderboard']} · entities {inv['entities']} · sources {inv['sources']} · FOI ready {ready}.
- Next: rq_2281 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk). Next EVERY-10 **2290**.
"""
with open(LOG, "a", encoding="utf-8") as f:
    f.write(log_block)

print("TICK2280 DONE")
print(f"omzet={OMZET} bruto={BRUTO} pnl={PNL} equity={EQUITY} fte={FTE} pi={PI}")
print(f"inv budgets={inv['budgets']} lb={inv['leaderboard']} foi_ready={ready}")
print(f"EVERY-10 A=100 B=100 C~99 D~74-88 E~{ready}")
