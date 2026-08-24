# -*- coding: utf-8 -*-
"""Tick 2291: finish in_progress Intro Schoonmaak YE2025 leftover dual."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2291")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T15:15:00Z"
TICK = "2291"
RQ = "rq_2291"
NEXT_RQ = "rq_2292"
ENTITY = "vzw_groep_intro_schoonmaak"
KBO = "0636.767.584"
GAP = "gap_intro_schoonmaak_nbb_pdf_assets_debt_empty_omzet_bruto_0_89m_pnl_loss_flip_equity_drop_matrix_l5"
LB = "lb_intro_schoonmaak_bruto_0_89m_empty_omzet_pnl_loss_flip_equity_drop_24pct_jr2025"
COMM = "comm_intro_schoonmaak_jr2025_statutory_empty_omzet_bruto_pnl_loss_flip"

BRUTO = 888071
BRUTO24 = 944259
PNL = -121456
PNL24 = 11731
EQUITY = 382077
EQUITY24 = 503533
FTE = 22.1
FTE24 = 21.3
FILED = "22.04.2026"
EMAIL = "info@groepintro.be"

# cost 1.5 (<1m) · abs 7.0 · diff 3 → pi = 0.55*1.5 + 0.35*7 + 0.1*7 = 3.975 → 4.00
ABS, COST, DIFF, PI = 7.0, 1.5, 3.0, 4.00


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
        f"Intro Schoonmaak YE2025 empty omzet bruto {BRUTO} pnl LOSS FLIP {PNL} "
        f"equity DROP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0636767584/groep-intro-schoonmaak\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "title": "Groep Intro Schoonmaak YE2025 CW EN (bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24%)",
        "url": "https://www.companyweb.be/en/0636767584/groep-intro-schoonmaak",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; empty omzet; bruto {BRUTO} DROP -5.95%; pnl {PNL} LOSS FLIP; equity {EQUITY} DROP -24.12%; FTE {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_intro_schoonmaak_jr2025_cw_nl",
        "title": "Groep Intro Schoonmaak YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0636767584/groep-intro-schoonmaak",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; same euros; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_intro_schoonmaak_jr2025_cw_fr",
        "title": "Groep Intro Schoonmaak YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0636767584/groep-intro-schoonmaak",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; CA unpublished; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_intro_schoonmaak_kbo_0636767584",
        "title": "KBO Groep Intro Schoonmaak 0636.767.584 Actief VZW 2 VE NACE 81.210 Anderlecht",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=636767584",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; VZW sinds 30.03.2021 (begindatum 04.09.2015); 2 VE; Charles Parentéstraat 6 1070 Anderlecht; RSZ 81.210 cleaning; DISTINCT Groep INTRO Maatwerk 0472.098.703",
    },
    {
        "source_id": "src_intro_schoonmaak_site_contact_2291",
        "title": "Groep INTRO FOI channel info@groepintro.be / groepintro.be",
        "url": "https://www.groepintro.be/",
        "publisher": "Groep INTRO",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Charles Parentéstraat 6 1070 Anderlecht; cleaning dual of Groep INTRO maatwerk",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Groep Intro Schoonmaak VZW (Anderlecht / schoonmaak dual INTRO)",
    "name_fr": "Groep Intro Schoonmaak ASBL (Anderlecht / nettoyage dual INTRO)",
    "name_en": "Groep Intro Schoonmaak VZW (Anderlecht cleaning dual of INTRO maatwerk)",
    "level": "parastatal",
    "parent_id": "brussels_gov",
    "community_language": "nl",
    "website": "https://www.groepintro.be/",
    "foi_email": EMAIL,
    "foi_postal": "Charles Parentéstraat 6, 1070 Anderlecht",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW RSZ 81.210; "
        f"empty omzet; bruto DROP {BRUTO} (-5.95%) pnl LOSS FLIP {PNL} equity DROP {EQUITY} (-24.12%) "
        f"FTE {FTE}; neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; DISTINCT Groep INTRO Maatwerk@2182 "
        f"0472.098.703; after Buseloc/Op Maat@2290; AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_intro_schoonmaak_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto YE2025 (omzet unpublished)",
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} DROP -5.95% vs {BRUTO24}; empty omzet",
    },
    {
        "budget_id": "bud_intro_schoonmaak_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 LOSS FLIP",
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} LOSS FLIP vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_intro_schoonmaak_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} DROP -24.12% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_intro_schoonmaak_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}",
    },
    {
        "budget_id": "bud_intro_schoonmaak_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW pnl YE2024 comparative",
        "source_id": "src_intro_schoonmaak_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS FLIP)",
    },
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": "Intro Schoonmaak YE2025 leftover dual (bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24% / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "schoonmaak-maatwerkers Anderlecht / Groep INTRO dual path",
    "legal_basis": f"VZW Groep Intro Schoonmaak (KBO {KBO}; Actief; 2 VE; RSZ 81.210)",
    "decision_date": "2026-04-22",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0636767584/groep-intro-schoonmaak",
    "stated_goal": "Brussels Groep INTRO cleaning dual — inclusive employment",
    "cut_option": "Publish NBB PDF assets/debt; disclose empty omzet vs bruto 0.89m; recon pnl LOSS FLIP + equity DROP -24%",
    "source_id": "src_intro_schoonmaak_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Bruxelles>Anderlecht>IntroSchoonmaak>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; DISTINCT INTRO Maatwerk@2182; after Buseloc/Op Maat@2290",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Intro Schoonmaak bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24% (YE2025)",
    "level": "L5",
    "type": "maatwerk_schoonmaak_vzw_statutory",
    "hierarchy_path": "Bruxelles>Anderlecht>IntroSchoonmaak>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW empty omzet / bruto DROP {BRUTO} (-5.95%) / pnl LOSS FLIP {PNL} vs {PNL24} / "
        f"equity DROP {EQUITY} (-24.12%) / FTE {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_intro_schoonmaak_jr2025_cw_en",
    "beneficiaries": "schoonmaak-maatwerkers Anderlecht / INTRO dual",
    "stated_goal": "Brussels cleaning dual of Groep INTRO",
    "measured_outcome": f"empty omzet; bruto DROP; pnl LOSS FLIP; equity DROP -24%; FTE {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt FOI; disclose empty omzet; recon LOSS FLIP + equity DROP -24%",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; DISTINCT INTRO Maatwerk@2182; AGB Bornem JR2024; FARO/AIESH YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Bruxelles>Anderlecht>IntroSchoonmaak>NBB_PDF_assets_debt_empty_omzet_pnl_loss_flip",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
        f"pnl LOSS FLIP EUR{PNL} vs YE2024 EUR{PNL24}; equity DROP EUR{EQUITY} (-24.12%); "
        f"related-party vs Groep INTRO Maatwerk 0472.098.703"
    ),
    "why_it_matters": (
        f"Medium CW shows Brussels INTRO cleaning dual VZW (bruto 0.89m / empty omzet / "
        f"pnl LOSS FLIP / equity DROP -24%) under public path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Groep Intro Schoonmaak VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Charles Parentéstraat 6, 1070 Anderlecht",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; DISTINCT INTRO Maatwerk@2182; after Buseloc/Op Maat@2290",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Groep Intro Schoonmaak (NBB PDF / empty omzet / bruto 0.89m / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Groep Intro Schoonmaak VZW — KBO **{KBO}** (Actief; Charles Parentéstraat 6, 1070 Anderlecht; **2 VE**; FTE {FTE}; RSZ **81.210**; DISTINCT INTRO Maatwerk 0472.098.703)  
**recipient:** {EMAIL} · Charles Parentéstraat 6, 1070 Anderlecht  
**sources:** [CW EN](https://www.companyweb.be/en/0636767584/groep-intro-schoonmaak) · [CW NL](https://www.companyweb.be/nl/0636767584/groep-intro-schoonmaak) · [CW FR](https://www.companyweb.be/fr/0636767584/groep-intro-schoonmaak) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=636767584) · [site](https://www.groepintro.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **GROEP INTRO SCHOONMAAK**; **2 VE**; zetel Charles Parentéstraat 6, 1070 Anderlecht; RSZ NACE **81.210**; DISTINCT Groep INTRO Maatwerk KBO **0472.098.703** (already mined@2182).
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP −5.95%; pnl **EUR{PNL:,}** LOSS FLIP vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −24.12%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Manupal/Vlotter/De Ploeg YE2024. After Buseloc/Op Maat@2290 EVERY-10. Do NOT redo Buseloc/Op Maat/REW/Labeur/Village Liegeois/De Sprong/INTRO Maatwerk stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Groep Intro Schoonmaak VZW
via {EMAIL}
Charles Parentéstraat 6, 1070 Anderlecht
Betreft: Openbaarmaking jaarrekening 2025 Groep Intro Schoonmaak (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Brussel / ordonnantie openbaarheid), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO} gepubliceerd is.
3. Toelichting pnl LOSS FLIP EUR{PNL} (vs YE2024 EUR{PNL24}) en equity DROP EUR{EQUITY} (−24.12%).
4. Related-party / recharges vs Groep INTRO Maatwerk (KBO 0472.098.703) YE2025.
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
            f"leftover dual — Intro Schoonmaak YE2025 Medium "
            f"(bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24%)"
        )
        r["notes"] = (
            f"tick{TICK} Intro Schoonmaak YE2025; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; "
            f"FTE {FTE}; FOI ready NOT sent; DISTINCT INTRO Maatwerk@2182"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Intro Schoonmaak — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after Intro Schoonmaak YE2025 Medium "
                "(bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24%). "
                "Prefer NON-stall: AGB Bornem if JR2025; FARO/AIESH/Citeco/Groupe Foes if YE2025; "
                "else Manupal/Vlotter/De Ploeg if YE2025 or unused ETA/DSO/IGS/HVZ. "
                "Do NOT redo Intro Schoonmaak/INTRO Maatwerk/Buseloc/Op Maat/REW/Labeur/"
                "Village Liegeois/De Sprong/Borgerstein/Posthoorn."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Intro Schoonmaak; Manupal/Vlotter/De Ploeg YE2024; "
                f"AGB Bornem JR2024; FARO/AIESH YE2024; next every-10 2300"
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
            f"tick{TICK} leftover dual Intro Schoonmaak {KBO} Medium "
            f"(bruto DROP {BRUTO}; empty omzet; pnl LOSS FLIP {PNL}; equity DROP {EQUITY} -24.12%; "
            f"FTE {FTE}; 2 VE Anderlecht cleaning dual INTRO); DISTINCT INTRO Maatwerk@2182; "
            f"after Buseloc/Op Maat@2290; AGB Bornem JR2024; FARO/AIESH YE2024; "
            f"next {NEXT_RQ}; next every-10 2300; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Intro Schoonmaak Anderlecht (bruto 0.89m / empty omzet / pnl LOSS FLIP / equity DROP -24% / Medium)

- Unit: **{RQ}** finish **in_progress** leftover dual after **rq_2290 Buseloc/Op Maat EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Manupal/Vlotter/De Ploeg still **YE2024**. Took claimed FREE Brussels **Groep Intro Schoonmaak VZW** YE2025 (KBO **{KBO}**; Charles Parentéstraat 6 Anderlecht; **Actief** **2 VE**; RSZ **81.210** cleaning; DISTINCT INTRO Maatwerk@2182 **0472.098.703**). Do not redo Buseloc/Op Maat/REW/Labeur/Village Liegeois/De Sprong/INTRO Maatwerk stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP -5.95% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** LOSS FLIP vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP -24.12%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Manupal-Vlotter-De Ploeg-if-YE2025 / unused ETA-DSO-IGS).
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
