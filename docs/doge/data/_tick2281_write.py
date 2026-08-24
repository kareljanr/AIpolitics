# -*- coding: utf-8 -*-
"""Tick 2281: Les Ateliers du 94 YE2025 leftover dual ETA/care La Louvière."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2281")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T12:45:00Z"
TICK = "2281"
RQ = "rq_2281"
NEXT_RQ = "rq_2282"
ENTITY = "vzw_ateliers_du_94_la_louviere"
KBO = "0407.601.522"
GAP = "gap_a94_nbb_pdf_assets_debt_empty_omzet_bruto_2_56m_pnl_loss_flip_eta_care_matrix_l5"
LB = "lb_a94_bruto_2_56m_empty_omzet_pnl_loss_flip_equity_drop_jr2025"
COMM = "comm_a94_jr2025_statutory_eta_care_empty_omzet_bruto_pnl_loss_flip"

BRUTO = 2561027
BRUTO24 = 2369516
PNL = -23078
PNL24 = 14026
EQUITY = 4030267
EQUITY24 = 4115604
FTE = 30.8
FTE24 = 29.5
FTE22 = 61.6
FILED = "14.07.2026"

# cost 3.5 (<10m) · abs 6.8 · diff 3.0 → pi = 0.55*3.5 + 0.35*6.8 + 0.1*(10-3) = 5.005 → 5.00
ABS, COST, DIFF, PI = 6.8, 3.5, 3.0, 5.00


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
        "Les Ateliers du 94 / A94 YE2025 CW EN\n"
        f"omzet unpublished bruto {BRUTO} (+8.08%) pnl {PNL} (-264.53% LOSS FLIP) "
        f"equity {EQUITY} (-2.07%) FTE {FTE}\n"
        f"filed {FILED}\n"
        "url https://www.companyweb.be/en/0407601522/les-ateliers-du-94\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    f.write(
        "{\n"
        f'  "tick": "{TICK}",\n'
        f'  "unit": "{RQ}",\n'
        f'  "entity": "{ENTITY}",\n'
        f'  "kbo": "{KBO}",\n'
        '  "omzet": null,\n'
        f'  "bruto": {BRUTO},\n'
        f'  "pnl": {PNL},\n'
        f'  "equity": {EQUITY},\n'
        f'  "fte": {FTE},\n'
        '  "confidence": "medium",\n'
        f'  "gap": "{GAP}"\n'
        "}\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
new_sources = [
    {
        "source_id": "src_a94_jr2025_cw_en",
        "title": "Les Ateliers du 94 / A94 YE2025 Companyweb EN (bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP)",
        "url": "https://www.companyweb.be/en/0407601522/les-ateliers-du-94",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; YE2025 Medium CW EN; omzet unpublished; bruto {BRUTO} JUMP +8.08%; "
            f"pnl {PNL} LOSS FLIP -264.53%; equity {EQUITY} DROP -2.07%; FTE {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_a94_jr2025_cw_nl",
        "title": "Les Ateliers du 94 / A94 YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0407601522/les-ateliers-du-94",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; YE2025 Medium CW NL; same euros as EN; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_a94_jr2025_cw_fr",
        "title": "Les Ateliers du 94 / A94 YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0407601522/les-ateliers-du-94",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; YE2025 Medium CW FR; CA unpublished; marge brute {BRUTO}; "
            f"résultat {PNL}; capitaux propres {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_a94_kbo_0407601522",
        "title": "KBO Les Ateliers du 94 0407.601.522 Actief VZW 1 VE NACE 87.202 La Louvière",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=407601522",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 13.07.1966; afkorting A94; 1 VE; "
            f"zetel Rue Houtart(H-A) 18 7110 La Louvière (Houdeng-Goegnies); "
            f"info@ateliersdu94.be; www.ateliersdu94.be; RSZ NACE 87.202; EWETA ETA member dual care+ETA"
        ),
    },
    {
        "source_id": "src_a94_site_contact_2281",
        "title": "Les Ateliers du 94 FOI channel info@ / eta@ateliersdu94.be / ateliersdu94.be + leseta",
        "url": "https://www.ateliersdu94.be/",
        "publisher": "Les Ateliers du 94 ASBL",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; info@ateliersdu94.be; eta@ateliersdu94.be; +32 64 22 32 13; "
            f"leseta.be/annuaire-eta/les-ateliers-du-94/; Walloon disability care + ETA AViQ path"
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
    "name_nl": "Les Ateliers du 94 / A94 VZW (La Louvière / Walloon ETA+zorg)",
    "name_fr": "Les Ateliers du 94 / A94 ASBL (La Louvière / ETA + accueil handicap)",
    "name_en": "Les Ateliers du 94 adapted-work + residential-care ASBL (La Louvière Walloon ETA)",
    "level": "parastatal",
    "parent_id": "sec_wallonia",
    "community_language": "fr",
    "website": "https://www.ateliersdu94.be/",
    "foi_email": "info@ateliersdu94.be",
    "foi_postal": "Rue Houtart(H-A) 18, 7110 La Louvière (Houdeng-Goegnies)",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE VZW NACE 87.202; "
        f"omzet unpublished; bruto JUMP {BRUTO} (+8.08%) pnl LOSS FLIP {PNL} (-264.53%) "
        f"equity DROP {EQUITY} (-2.07%) FTE {FTE} (structural shrink vs FTE2022 {FTE22}); "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; EWETA ETA member dual care+ETA; "
        f"after eurakor@2280 / Alternatief@2280; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
        f"APN still YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_a94_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto_marge YE2025 (omzet unpublished)",
        "source_id": "src_a94_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 bruto {BRUTO} JUMP +8.08% vs YE2024 {BRUTO24}; empty omzet",
    },
    {
        "budget_id": "bud_a94_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory winst/verlies YE2025 pnl LOSS FLIP",
        "source_id": "src_a94_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 pnl {PNL} LOSS FLIP -264.53% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_a94_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": "src_a94_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2025 equity {EQUITY} DROP -2.07% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_a94_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE YE2025",
        "source_id": "src_a94_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs YE2024 {FTE24}; structural shrink vs YE2022 {FTE22}",
    },
    {
        "budget_id": "bud_a94_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": "src_a94_jr2025_cw_en",
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
        "Les Ateliers du 94 YE2025 leftover dual "
        "(bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP / equity DROP / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "ETA + residential-care workers La Louvière / AViQ disability path",
    "legal_basis": f"ASBL Les Ateliers du 94 / A94 (KBO {KBO}; Actief; 1 VE; NACE 87.202; EWETA ETA)",
    "decision_date": "2026-07-14",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},'
        f'"2024_fte":{FTE24},"2022_fte":{FTE22}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0407601522/les-ateliers-du-94",
    "stated_goal": "Walloon disability residential care + ETA sheltered workshop — inclusive employment",
    "cut_option": (
        "Publish NBB PDF assets/debt; reconcile empty omzet vs bruto 2.56m; "
        "disclose AViQ care+ETA matrix behind pnl LOSS FLIP and FTE structural shrink"
    ),
    "source_id": "src_a94_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>LaLouviere>AteliersDu94>JR2025_statutory_L5",
    "notes": (
        f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); "
        f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; after eurakor@2280; "
        f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; APN still YE2024"
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
        "Les Ateliers du 94 bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP "
        "/ equity DROP (YE2025 Walloon ETA+care La Louvière)"
    ),
    "level": "L5",
    "type": "eta_care_asbl_statutory",
    "hierarchy_path": "Wallonie>Hainaut>LaLouviere>AteliersDu94>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW empty omzet / bruto JUMP {BRUTO} (+8.08%) / pnl LOSS FLIP {PNL} (-264.53% vs {PNL24}) / "
        f"equity DROP {EQUITY} (-2.07%) / FTE {FTE} (vs {FTE24}; shrink vs {FTE22} YE2022) / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_a94_jr2025_cw_en",
    "beneficiaries": "ETA + residential-care workers La Louvière / AViQ disability path",
    "stated_goal": "Walloon disability residential care + ETA sheltered workshop",
    "measured_outcome": (
        f"empty omzet; bruto JUMP +8.08%; pnl LOSS FLIP -264.53%; equity DROP -2.07%; "
        f"FTE {FTE}; filed {FILED}"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        "Publish NBB PDF assets/debt/cash FOI; disclose AViQ care+ETA matrix behind "
        "empty omzet / bruto 2.56m / pnl LOSS FLIP / FTE structural shrink"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
        f"FARO/AIESH/Citeco/Groupe Foes YE2024; APN still YE2024"
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
        "Wallonie>Hainaut>LaLouviere>AteliersDu94>"
        "NBB_PDF_assets_debt_empty_omzet_bruto_pnl_loss_flip"
    ),
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished "
        f"while bruto EUR{BRUTO}; pnl LOSS FLIP EUR{PNL} vs YE2024 EUR{PNL24}; equity DROP "
        f"EUR{EQUITY}; FTE structural shrink {FTE22}->{FTE}; AViQ care+ETA subsidy matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows Walloon EWETA ETA+care ASBL La Louvière (bruto 2.56m / empty omzet / "
        f"pnl LOSS FLIP / equity DROP / FTE {FTE}) under AViQ path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Les Ateliers du 94 ASBL",
    "recipient_email": "info@ateliersdu94.be",
    "recipient_postal": "Rue Houtart(H-A) 18, 7110 La Louvière (Houdeng-Goegnies)",
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
        f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/"
        f"Groupe Foes YE2024; AGB Bornem JR2024; APN still YE2024; after eurakor@2280"
    ),
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Les Ateliers du 94 (NBB PDF / empty omzet / bruto 2.56m / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Ateliers du 94 / A94 ASBL — KBO **{KBO}** (Actief; Rue Houtart(H-A) 18, 7110 La Louvière; **1 VE**; FTE {FTE} CW; NACE **87.202**; EWETA ETA + residential care AViQ)  
**recipient:** info@ateliersdu94.be · eta@ateliersdu94.be · Rue Houtart(H-A) 18, 7110 La Louvière (+32 64 22 32 13)  
**sources:** [CW EN](https://www.companyweb.be/en/0407601522/les-ateliers-du-94) · [CW NL](https://www.companyweb.be/nl/0407601522/les-ateliers-du-94) · [CW FR](https://www.companyweb.be/fr/0407601522/les-ateliers-du-94) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=407601522) · [site](https://www.ateliersdu94.be/) · [leseta](https://leseta.be/annuaire-eta/les-ateliers-du-94/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Les Ateliers du 94** (afkorting **A94**); **1 VE**; zetel Rue Houtart(H-A) 18, 7110 La Louvière (Houdeng-Goegnies); RSZ NACE **87.202**; info@ateliersdu94.be; www.ateliersdu94.be; begindatum 13.07.1966; EWETA member (care + ETA).
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +8.08% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** LOSS FLIP −264.53% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −2.07%; FTE **{FTE}** (vs {FTE24}; structural shrink vs YE2022 {FTE22}); filed **{FILED}**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; REW YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal/Posthoorn/De Ploeg/Vlotter/Buseloc YE2024; APN still YE2024; Heropbeuring CW opaque. After eurakor@2280 / Alternatief@2280. Do NOT redo eurakor / Alternatief / Reset / Ateliers de l'Avenir / IN-Z / m-accent / AMAB / C.A.R.P. / A.P.A.C. / Adapta / Atelier 85 / La Gaume / De Enter / Fournipac stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Les Ateliers du 94 ASBL
via info@ateliersdu94.be / eta@ateliersdu94.be
Rue Houtart(H-A) 18, 7110 La Louvière (Houdeng-Goegnies)
Betreft: Openbaarmaking jaarrekening 2025 Les Ateliers du 94 (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Wallonië / Code de la démocratie locale et de la décentralisation / openbaarheid
bestuursdocumenten), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO} (+8.08%) gepubliceerd is.
3. Toelichting bij pnl LOSS FLIP EUR{PNL} (vs YE2024 EUR{PNL24}; −264.53%) en equity DROP
   EUR{EQUITY} (−2.07%), plus FTE-pad {FTE22} (2022) → {FTE} (2025).
4. Overzicht van AViQ/Waalse toelagen (zorg + ETA-loonkostentussenkomst) YE2025.
5. Verdeling activiteiten (residential care vs ETA atelier) en schulden LT/KT + liquide middelen.

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
            "leftover dual — Les Ateliers du 94 YE2025 Medium "
            "(bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP / FTE 30.8)"
        )
        r["notes"] = (
            f"tick{TICK} A94 YE2025; FARO/AIESH/REW/APN still YE2024; bruto {BRUTO}; "
            f"pnl {PNL}; equity {EQUITY}; FTE {FTE}; FOI ready NOT sent"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after A94 — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after Les Ateliers du 94 YE2025 Medium "
                "(bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP / FTE 30.8). "
                "Prefer NON-stall live: AGB Bornem if JR2025; FARO/AIESH/REW/Citeco/Groupe Foes if YE2025; "
                "else unused ETA-VAPH-WZC-maatwerk (Die Zukunft / Roseau Vert / Ateliers de Mons / "
                "Village Liégeois / Monceau if YE2025) or unused DSO/water/nuclear/IGS/HVZ. "
                "Do NOT redo A94/eurakor/Alternatief/Reset/Ateliers Avenir/IN-Z/m-accent/AMAB/"
                "C.A.R.P./A.P.A.C./Adapta/Atelier85/La Gaume/De Enter/Fournipac."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} A94; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
                f"AGB Bornem JR2024; APN/Manupal/Posthoorn/De Ploeg/Vlotter/Buseloc YE2024; "
                f"next every-10 2290"
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
            f"tick{TICK} leftover dual Les Ateliers du 94 {KBO} Medium "
            f"(bruto JUMP {BRUTO} +8.08%; empty omzet; pnl LOSS FLIP {PNL} -264.53%; "
            f"equity DROP {EQUITY} -2.07%; FTE {FTE}; 1 VE La Louvière EWETA ETA+care); "
            f"after eurakor@2280; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes/APN YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2290; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

log_block = f"""
### {UTC} - tick {TICK} - {RQ} Les Ateliers du 94 La Louvière (bruto JUMP 2.56m / empty omzet / pnl LOSS FLIP / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **rq_2280 eurakor/Alternatief EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (0201.712.587); REW still **YE2024**; Citeco/Groupe Foes still **YE2024**; APN still **YE2024**; Manupal/Posthoorn/De Ploeg/Vlotter/Buseloc still **YE2024**; Heropbeuring still **CW opaque**. Took unused FREE Walloon EWETA **Les Ateliers du 94 / A94 ASBL** YE2025 (KBO **{KBO}**; Rue Houtart(H-A) 18 La Louvière / Houdeng-Goegnies; **Actief** **1 VE**; NACE **87.202** residential care + ETA dual; info@ateliersdu94.be). Do not redo eurakor/Alternatief/Reset/Ateliers Avenir/IN-Z/m-accent/AMAB/C.A.R.P./A.P.A.C./Adapta/Atelier85/La Gaume/De Enter/Fournipac stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +8.08% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** LOSS FLIP -264.53% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP -2.07%; FTE **{FTE}** (vs {FTE24}; structural shrink vs YE2022 {FTE22}); neerlegging **{FILED}**. Strong KBO Actief 1 VE VZW. Assets/debt Unknown. Medium. FOI via info@ateliersdu94.be / eta@ateliersdu94.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused ETA Die Zukunft-Roseau Vert-Ateliers Mons-Village Liégeois-Monceau / unused DSO-water-IGS-HVZ).
"""
with open(LOG, "a", encoding="utf-8") as f:
    f.write(log_block)

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
