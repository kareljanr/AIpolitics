# -*- coding: utf-8 -*-
"""Tick 2289: Labeur Gent YE2025 leftover dual maatwerk."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2289")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T14:45:00Z"
TICK = "2289"
RQ = "rq_2289"
NEXT_RQ = "rq_2290"
ENTITY = "vzw_labeur_gent"
KBO = "0469.502.269"
GAP = "gap_labeur_nbb_pdf_assets_debt_empty_omzet_bruto_2_17m_pnl_jump_fte_drop_matrix_l5"
LB = "lb_labeur_bruto_2_17m_empty_omzet_pnl_jump_201pct_fte_drop_jr2025"
COMM = "comm_labeur_jr2025_statutory_maatwerk_empty_omzet_bruto_pnl_jump"

BRUTO = 2169142
BRUTO24 = 2210913
PNL = 63726
PNL24 = 21170
EQUITY = 268300
EQUITY24 = 213255
FTE = 49.6
FTE24 = 54.7
FILED = "16.07.2026"
EMAIL = "info@labeur.be"

# cost 3.5 · abs 6.2 · diff 3 → pi = 0.55*3.5 + 0.35*6.2 + 0.1*7 = 4.795 → 4.80
ABS, COST, DIFF, PI = 6.2, 3.5, 3.0, 4.80


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
        f"Labeur YE2025 empty omzet bruto {BRUTO} pnl JUMP {PNL} (+201%) "
        f"equity JUMP {EQUITY} FTE DROP {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0469502269/vereniging-zonder-winstoogmerk-labeur\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_labeur_jr2025_cw_en",
        "title": "Labeur Gent YE2025 CW EN (bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP)",
        "url": "https://www.companyweb.be/en/0469502269/vereniging-zonder-winstoogmerk-labeur",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; empty omzet; bruto {BRUTO} DROP -1.89%; pnl {PNL} JUMP +201.02%; equity {EQUITY} JUMP +25.81%; FTE DROP {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_labeur_jr2025_cw_nl",
        "title": "Labeur Gent YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0469502269/vereniging-zonder-winstoogmerk-labeur",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; same euros; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_labeur_jr2025_cw_fr",
        "title": "Labeur Gent YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0469502269/vereniging-zonder-winstoogmerk-labeur",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; CA unpublished; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_labeur_kbo_0469502269",
        "title": "KBO Labeur 0469.502.269 Actief VZW 2 VE RSZ NACE 88.993 Gent",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=469502269",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; VZW sinds 25.11.1999; 2 VE; zetel Balenmagazijnstraat 1 9000 Gent; RSZ 88.993; BTW schrijnwerk/schilderen; DG Jonas Tournicourt",
    },
    {
        "source_id": "src_labeur_site_contact_2289",
        "title": "Labeur FOI channel info@labeur.be / labeur.be",
        "url": "https://www.labeur.be/",
        "publisher": "Labeur VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; +32 9 223 88 03; Gent circular renovation/atelier maatwerk",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Labeur VZW (Gent / maatwerk renovatie-atelier)",
    "name_fr": "Labeur ASBL (Gand / entreprise de travail adapté rénovation)",
    "name_en": "Labeur sheltered workshop VZW (Ghent circular renovation maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.labeur.be/",
    "foi_email": EMAIL,
    "foi_postal": "Balenmagazijnstraat 1, 9000 Gent",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW RSZ NACE 88.993; "
        f"empty omzet; bruto DROP {BRUTO} (-1.89%) pnl JUMP {PNL} (+201.02%) equity JUMP {EQUITY} (+25.81%) "
        f"FTE DROP {FTE}; neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Village Liegeois@2288; "
        f"Manupal/Vlotter/Buseloc/De Ploeg YE2024; AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_labeur_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto YE2025 (omzet unpublished)",
        "source_id": "src_labeur_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} DROP -1.89% vs {BRUTO24}; empty omzet",
    },
    {
        "budget_id": "bud_labeur_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 JUMP +201%",
        "source_id": "src_labeur_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} JUMP +201.02% vs {PNL24}",
    },
    {
        "budget_id": "bud_labeur_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_labeur_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +25.81% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_labeur_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_labeur_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} DROP vs {FTE24}",
    },
    {
        "budget_id": "bud_labeur_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW pnl YE2024 comparative",
        "source_id": "src_labeur_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative",
    },
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": "Labeur Gent YE2025 leftover dual (bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "maatwerkers Gent renovatie-atelier / VDAB-ESF path",
    "legal_basis": f"VZW Labeur (KBO {KBO}; Actief; 2 VE; RSZ NACE 88.993)",
    "decision_date": "2026-07-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0469502269/vereniging-zonder-winstoogmerk-labeur",
    "stated_goal": "Flemish Gent maatwerk circular renovation/atelier — inclusive employment",
    "cut_option": "Publish NBB PDF assets/debt; disclose empty omzet vs bruto 2.17m; recon pnl JUMP +201% with FTE DROP",
    "source_id": "src_labeur_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Labeur>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; after Village Liegeois@2288; Manupal YE2024",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Labeur bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP (YE2025 Gent maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Labeur>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW empty omzet / bruto DROP {BRUTO} (-1.89%) / pnl JUMP {PNL} (+201.02% vs {PNL24}) / "
        f"equity JUMP {EQUITY} (+25.81%) / FTE DROP {FTE} (vs {FTE24}) / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_labeur_jr2025_cw_en",
    "beneficiaries": "maatwerkers Gent / VDAB-ESF path",
    "stated_goal": "Flemish maatwerk circular renovation/atelier",
    "measured_outcome": f"empty omzet; bruto DROP -1.89%; pnl JUMP +201%; equity JUMP +26%; FTE DROP {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto; recon pnl JUMP with FTE DROP",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; Manupal YE2024; AGB Bornem JR2024; FARO/AIESH YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Labeur>NBB_PDF_assets_debt_empty_omzet_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
        f"pnl JUMP EUR{PNL} (+201% vs {PNL24}); FTE DROP {FTE24}->{FTE}; VDAB/ESF loonkost matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows Gent maatwerk VZW (bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP) "
        f"under public loonkost path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Labeur VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Balenmagazijnstraat 1, 9000 Gent",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Village Liegeois@2288; Manupal YE2024",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Labeur Gent (NBB PDF / empty omzet / bruto 2.17m / pnl JUMP +201%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Labeur VZW — KBO **{KBO}** (Actief; Balenmagazijnstraat 1, 9000 Gent; **2 VE**; FTE {FTE}; RSZ NACE **88.993**)  
**recipient:** {EMAIL} · Balenmagazijnstraat 1, 9000 Gent (+32 9 223 88 03)  
**sources:** [CW EN](https://www.companyweb.be/en/0469502269/vereniging-zonder-winstoogmerk-labeur) · [CW NL](https://www.companyweb.be/nl/0469502269/vereniging-zonder-winstoogmerk-labeur) · [CW FR](https://www.companyweb.be/fr/0469502269/vereniging-zonder-winstoogmerk-labeur) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=469502269) · [site](https://www.labeur.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **vereniging zonder winstoogmerk Labeur**; **2 VE**; zetel Balenmagazijnstraat 1, 9000 Gent; RSZ NACE **88.993**; DG Jonas Tournicourt.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP −1.89%; pnl **EUR{PNL:,}** JUMP +201.02% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +25.81%; FTE **{FTE}** DROP (vs {FTE24}); filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Manupal/Vlotter/Buseloc/De Ploeg YE2024. After Village Liegeois@2288. Do NOT redo Village Liegeois/De Sprong/Borgerstein/Mobiel/Posthoorn/Ateljee stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Labeur VZW
via {EMAIL}
Balenmagazijnstraat 1, 9000 Gent
Betreft: Openbaarmaking jaarrekening 2025 Labeur (KBO {KBO})

Geachte,

Op grond van het Bestuursdecreet vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO} gepubliceerd is.
3. Toelichting pnl JUMP EUR{PNL} (+201% vs YE2024 EUR{PNL24}) naast FTE DROP {FTE24}→{FTE}.
4. VDAB/ESF/stad Gent loonkostsubsidiematrix YE2025.
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
        r["title"] = (
            f"leftover dual — Labeur Gent YE2025 Medium "
            f"(bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP {FTE})"
        )
        r["notes"] = (
            f"tick{TICK} Labeur YE2025; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; "
            f"FTE {FTE}; FOI ready NOT sent; next EVERY-10 2290"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "EVERY-10 + leftover dual after Labeur — prefer AGB/FARO-YE2025/"
                "AIESH-REW/Citeco-Groupe Foes-or-unused DSO-IGS-HVZ-ETA-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "EVERY-10 mandatory progress refresh + leftover dual after Labeur YE2025 Medium "
                "(bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP). "
                "Prefer NON-stall: AGB Bornem if JR2025; FARO/AIESH/REW/Citeco/Groupe Foes if YE2025; "
                "else Manupal/Vlotter/Buseloc/De Ploeg if YE2025 or unused ETA/DSO/IGS/HVZ. "
                "Do NOT redo Labeur/Village Liegeois/De Sprong/Borgerstein/Mobiel/Posthoorn/"
                "Ateljee/Die Zukunft/eurakor/Alternatief."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Labeur; EVERY-10 THIS NEXT TICK; "
                f"Manupal/Vlotter/Buseloc/De Ploeg YE2024; AGB Bornem JR2024; FARO/AIESH YE2024"
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
            f"tick{TICK} leftover dual Labeur {KBO} Medium "
            f"(bruto DROP {BRUTO} -1.89%; empty omzet; pnl JUMP {PNL} +201.02%; "
            f"equity JUMP {EQUITY} +25.81%; FTE DROP {FTE}; 2 VE Gent maatwerk); "
            f"after Village Liegeois@2288; Manupal YE2024; AGB Bornem JR2024; FARO/AIESH YE2024; "
            f"next {NEXT_RQ} EVERY-10; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Labeur Gent (bruto 2.17m / empty omzet / pnl JUMP +201% / FTE DROP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **rq_2288 Village Liegeois**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Manupal/Vlotter/Buseloc/De Ploeg still **YE2024**. Took FREE Flemish Gent maatwerk **Labeur VZW** YE2025 (KBO **{KBO}**; Balenmagazijnstraat 1 Gent; **Actief** **2 VE**; RSZ NACE **88.993** circular renovatie/atelier; info@labeur.be). Do not redo Village Liegeois/De Sprong/Borgerstein/Mobiel/Posthoorn/Ateljee/Die Zukunft stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP -1.89% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** JUMP +201.02% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +25.81%; FTE **{FTE}** DROP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open (EVERY-10); loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290** THIS NEXT). Next: {NEXT_RQ} EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / Manupal-if-YE2025 / unused ETA-DSO-IGS.
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
