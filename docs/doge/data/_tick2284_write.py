# -*- coding: utf-8 -*-
"""Tick 2284: De Posthoorn Beringen YE2025 leftover dual maatwerk (preferred stall unlocked)."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2284")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T13:30:00Z"
TICK = "2284"
RQ = "rq_2284"
NEXT_RQ = "rq_2285"
ENTITY = "vzw_de_posthoorn_beringen"
KBO = "0429.827.388"
GAP = "gap_posthoorn_nbb_pdf_assets_debt_bruto_gt_omzet_1_51x_pnl_loss_flip_fte_drop_matrix_l5"
LB = "lb_posthoorn_omzet_1_94m_bruto_1_51x_pnl_loss_flip_fte_drop_jr2025"
COMM = "comm_posthoorn_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_loss_flip"

OMZET = 1935730
OMZET24 = 1944233
BRUTO = 2916026
BRUTO24 = 2962946
PNL = -36106
PNL24 = 59451
EQUITY = 4214334
EQUITY24 = 4294492
FTE = 82.3
FTE24 = 85.9
RATIO = round(BRUTO / OMZET, 2)  # ~1.51
FILED = "05.06.2026"
EMAIL = "info@posthoorn.be"

# cost 3.5 · abs 6.5 · diff 3 → pi = 0.55*3.5 + 0.35*6.5 + 0.1*7 = 4.90
ABS, COST, DIFF, PI = 6.5, 3.5, 3.0, 4.90


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

with open(os.path.join(RAW, "cw_en_excerpt.txt"), "w", encoding="utf-8") as f:
    f.write(
        "De Posthoorn Beringen YE2025 CW EN\n"
        f"omzet {OMZET} (-0.44%) bruto {BRUTO} (~{RATIO}x) pnl {PNL} LOSS FLIP "
        f"equity {EQUITY} FTE {FTE}\nfiled {FILED}\n"
        "url https://www.companyweb.be/en/0429827388/de-posthoorn-beringen\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    f.write(
        "{\n"
        f'  "tick": "{TICK}", "unit": "{RQ}", "entity": "{ENTITY}", "kbo": "{KBO}",\n'
        f'  "omzet": {OMZET}, "bruto": {BRUTO}, "pnl": {PNL}, "equity": {EQUITY},\n'
        f'  "fte": {FTE}, "ratio": {RATIO}, "confidence": "medium", "gap": "{GAP}"\n'
        "}\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
new_sources = [
    {
        "source_id": "src_posthoorn_jr2025_cw_en",
        "title": f"De Posthoorn Beringen YE2025 CW EN (omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP)",
        "url": "https://www.companyweb.be/en/0429827388/de-posthoorn-beringen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; YE2025 Medium CW EN; omzet {OMZET} DROP -0.44%; bruto {BRUTO} (~{RATIO}x); "
            f"pnl {PNL} LOSS FLIP -160.73%; equity {EQUITY} DROP -1.87%; FTE DROP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_posthoorn_jr2025_cw_nl",
        "title": "De Posthoorn Beringen YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0429827388/de-posthoorn-beringen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; YE2025 Medium CW NL; same euros; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_posthoorn_jr2025_cw_fr",
        "title": "De Posthoorn Beringen YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0429827388/de-posthoorn-beringen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; YE2025 Medium CW FR; CA {OMZET}; marge brute {BRUTO}; "
            f"résultat {PNL}; capitaux propres {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_posthoorn_kbo_0429827388",
        "title": "KBO De Posthoorn Beringen 0429.827.388 Actief VZW 2 VE NACE 88.993",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=429827388",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 19.06.1986; naam sinds 09.06.2021; 2 VE; "
            f"zetel Koolmijnlaan 141 3582 Beringen; RSZ/BTW NACE 88.993 + bakery/green/clothing/horeca; "
            f"DG Pieter Decelle sinds 21.06.2021"
        ),
    },
    {
        "source_id": "src_posthoorn_site_contact_2284",
        "title": "De Posthoorn FOI channel info@posthoorn.be / posthoorn.be",
        "url": "https://www.posthoorn.be/",
        "publisher": "De Posthoorn Beringen VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; {EMAIL}; Koolmijnlaan 141 3582 Beringen; Flemish maatwerk bakery/"
            f"green/atelier/taverne; preferred stall unlocked YE2025 this tick"
        ),
    },
]
existing_s = {r["source_id"] for r in srows}
for ns in new_sources:
    if ns["source_id"] not in existing_s:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "De Posthoorn Beringen VZW (Limburg maatwerk)",
    "name_fr": "De Posthoorn Beringen ASBL (entreprise de travail adapté Limbourg)",
    "name_en": "De Posthoorn Beringen sheltered workshop VZW (Limburg maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.posthoorn.be/",
    "foi_email": EMAIL,
    "foi_postal": "Koolmijnlaan 141, 3582 Beringen",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW NACE 88.993; "
        f"omzet DROP {OMZET} (-0.44%) bruto DROP {BRUTO} (~{RATIO}x) pnl LOSS FLIP {PNL} "
        f"equity DROP {EQUITY} (-1.87%) FTE DROP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; preferred stall unlocked (was YE2024 as of 2280); after Ateljee@2283; "
        f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
new_budgets = [
    {
        "budget_id": "bud_posthoorn_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 omzet {OMZET} DROP -0.44% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_posthoorn_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 (~{RATIO}x omzet)",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 bruto {BRUTO} DROP -1.58%; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_posthoorn_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 LOSS FLIP",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 pnl {PNL} LOSS FLIP -160.73% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_posthoorn_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 equity {EQUITY} DROP -1.87% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_posthoorn_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} DROP vs YE2024 {FTE24}",
    },
    {
        "budget_id": "bud_posthoorn_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW pnl YE2024 comparative",
        "source_id": "src_posthoorn_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS FLIP)",
    },
]
existing_b = {r["budget_id"] for r in brows}
for nb in new_budgets:
    if nb["budget_id"] not in existing_b:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": (
        f"De Posthoorn Beringen YE2025 leftover dual "
        f"(omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP / FTE DROP / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "maatwerkers Limburg Beringen / VDAB-ESF loonkost path",
    "legal_basis": f"VZW De Posthoorn Beringen (KBO {KBO}; Actief; 2 VE; RSZ NACE 88.993)",
    "decision_date": "2026-06-05",
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
    "evaluation_url": "https://www.companyweb.be/en/0429827388/de-posthoorn-beringen",
    "stated_goal": "Flemish maatwerk bakery/green/atelier/taverne — inclusive employment",
    "cut_option": (
        f"Publish NBB PDF assets/debt; disclose loonkost matrix behind bruto~{RATIO}x; "
        f"reconcile pnl LOSS FLIP with FTE DROP"
    ),
    "source_id": "src_posthoorn_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Limburg>Beringen>Posthoorn>JR2025_statutory_L5",
    "notes": (
        f"tick{TICK}; Medium CW; omzet primary {OMZET}; bruto {BRUTO} (~{RATIO}x); "
        f"pnl LOSS FLIP {PNL}; preferred stall unlocked YE2025; after Ateljee@2283"
    ),
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": (
        f"De Posthoorn omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP / "
        f"FTE DROP (YE2025 Limburg maatwerk Beringen)"
    ),
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Beringen>Posthoorn>JR2025",
    "annual_cost_eur": str(OMZET),
    "total_cost_eur": str(OMZET),
    "tco_notes": (
        f"CW omzet {OMZET} DROP -0.44% / bruto {BRUTO} (~{RATIO}x) / "
        f"pnl LOSS FLIP {PNL} (-160.73% vs {PNL24}) / equity DROP {EQUITY} / "
        f"FTE DROP {FTE} (vs {FTE24}) / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_posthoorn_jr2025_cw_en",
    "beneficiaries": "maatwerkers Limburg Beringen / VDAB-ESF path",
    "stated_goal": "Flemish maatwerk bakery/green/atelier/taverne",
    "measured_outcome": (
        f"omzet flat DROP -0.44%; bruto~{RATIO}x; pnl LOSS FLIP; equity DROP -1.87%; "
        f"FTE DROP {FTE}; filed {FILED}"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; disclose loonkost matrix behind bruto~{RATIO}x "
        f"and pnl LOSS FLIP with FTE DROP"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; preferred stall unlocked YE2025; "
        f"AGB Bornem JR2024; FARO/AIESH YE2024"
    ),
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": (
        "Vlaanderen>Limburg>Beringen>Posthoorn>"
        "NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip"
    ),
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO} vs "
        f"omzet EUR{OMZET} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs YE2024 EUR{PNL24}; "
        f"FTE DROP {FTE24}->{FTE}; VDAB/ESF/gemeente loonkostsubsidie matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows Limburg maatwerk VZW Beringen (omzet 1.94m / bruto~{RATIO}x / "
        f"pnl LOSS FLIP / FTE DROP) under public loonkost path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "De Posthoorn Beringen VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Koolmijnlaan 141, 3582 Beringen",
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
        f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall unlocked YE2025; "
        f"after Ateljee@2283; AGB Bornem JR2024; FARO/AIESH YE2024"
    ),
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — De Posthoorn Beringen (NBB PDF / bruto~{RATIO}x / pnl LOSS FLIP / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Posthoorn Beringen VZW — KBO **{KBO}** (Actief; Koolmijnlaan 141, 3582 Beringen; **2 VE**; FTE {FTE} CW; NACE **88.993**; Flemish maatwerk)  
**recipient:** {EMAIL} · Koolmijnlaan 141, 3582 Beringen  
**sources:** [CW EN](https://www.companyweb.be/en/0429827388/de-posthoorn-beringen) · [CW NL](https://www.companyweb.be/nl/0429827388/de-posthoorn-beringen) · [CW FR](https://www.companyweb.be/fr/0429827388/de-posthoorn-beringen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=429827388) · [site](https://www.posthoorn.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **De Posthoorn Beringen**; **2 VE**; zetel Koolmijnlaan 141, 3582 Beringen; RSZ NACE **88.993**; DG Pieter Decelle sinds 21.06.2021; bakery/green/atelier/horeca BTW codes.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −0.44% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** (~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP −160.73% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −1.87%; FTE **{FTE}** DROP (vs {FTE24}); filed **{FILED}**.
- Preferred stall check: AGB Bornem JR2024; FARO/AIESH/REW YE2024; this tick **Posthoorn unlocked YE2025** (was YE2024 as of 2280). After Ateljee@2283. Do NOT redo Ateljee/Die Zukunft/TWI/A94/De Dageraad/eurakor/Alternatief/IN-Z/m-accent/AMAB stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Posthoorn Beringen VZW
via {EMAIL}
Koolmijnlaan 141, 3582 Beringen
Betreft: Openbaarmaking jaarrekening 2025 De Posthoorn Beringen (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij bruto EUR{BRUTO} vs omzet EUR{OMZET} (~{RATIO}x) en de
   VDAB/ESF/gemeente loonkostsubsidiematrix YE2025.
3. Toelichting bij pnl LOSS FLIP EUR{PNL} (vs YE2024 EUR{PNL24}) naast FTE DROP
   {FTE24} → {FTE}.
4. Verdeling omzet/activiteiten (bakkerij / groendienst / atelier / taverne).
5. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

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
        r["title"] = (
            f"leftover dual — De Posthoorn Beringen YE2025 Medium "
            f"(omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP / FTE DROP {FTE})"
        )
        r["notes"] = (
            f"tick{TICK} Posthoorn YE2025 unlocked; omzet {OMZET}; bruto {BRUTO}; "
            f"pnl {PNL}; equity {EQUITY}; FTE {FTE}; FOI ready NOT sent"
        )
        break
# also mark rq_2283 done if somehow still open and fix loop cursor continuity
for r in rqrows:
    if r.get("task_id") == "rq_2283" and r.get("status") != "done":
        r["status"] = "done"
        r["updated_utc"] = UTC
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Posthoorn — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Posthoorn YE2025 Medium "
                f"(omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP). "
                "Prefer NON-stall: AGB Bornem if JR2025; FARO/AIESH/REW/Citeco/Groupe Foes if YE2025; "
                "else unused ETA Roseau Vert/Ateliers Mons/Village Liégeois or maatwerk "
                "WEBO/De Sprong/Manupal/Vlotter/Buseloc if YE2025. "
                "Do NOT redo Posthoorn/Ateljee/Die Zukunft/TWI/A94/De Dageraad/eurakor/"
                "Alternatief/IN-Z/m-accent/AMAB."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Posthoorn unlocked YE2025; "
                f"FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                f"Manupal/Vlotter/Buseloc/De Ploeg YE2024; next every-10 2290"
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
            f"tick{TICK} leftover dual De Posthoorn {KBO} Medium "
            f"(omzet DROP {OMZET} -0.44%; bruto DROP {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; "
            f"equity DROP {EQUITY} -1.87%; FTE DROP {FTE}; 2 VE Beringen maatwerk); "
            f"preferred stall unlocked YE2025; after Ateljee@2283; AGB Bornem JR2024; "
            f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next EVERY-10 2290; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

log_block = f"""
### {UTC} - tick {TICK} - {RQ} De Posthoorn Beringen (omzet 1.94m / bruto~{RATIO}x / pnl LOSS FLIP / FTE DROP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **rq_2283 Ateljee** (loop_state lag fixed: 2283 already on remote). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**. **Preferred stall unlocked:** De Posthoorn now **YE2025** (was YE2024 as of 2280). Took FREE Flemish maatwerk **De Posthoorn Beringen VZW** YE2025 (KBO **{KBO}**; Koolmijnlaan 141 Beringen; **Actief** **2 VE**; NACE **88.993** bakery/green/atelier/taverne; DG Pieter Decelle). Do not redo Ateljee/Die Zukunft/TWI/A94/De Dageraad/eurakor/Alternatief/IN-Z/m-accent/AMAB stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -0.44% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP -1.58% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP -160.73% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP -1.87%; FTE **{FTE}** DROP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused ETA Roseau Vert-Ateliers Mons / Manupal-Vlotter-Buseloc-if-YE2025).
"""
with open(LOG, "a", encoding="utf-8") as f:
    f.write(log_block)

print(f"OK tick{TICK} {ENTITY} omzet={OMZET} bruto={BRUTO} pi={PI} next={NEXT_RQ}")
