# -*- coding: utf-8 -*-
"""Tick 2286: De Sprong Meerhout YE2025 leftover dual maatwerk."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2286")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T14:00:00Z"
TICK = "2286"
RQ = "rq_2286"
NEXT_RQ = "rq_2287"
ENTITY = "vzw_de_sprong_meerhout"
KBO = "0466.328.686"
GAP = "gap_desprong_nbb_pdf_assets_debt_empty_omzet_bruto_4_53m_pnl_drop_fte_jump_matrix_l5"
LB = "lb_desprong_bruto_4_53m_empty_omzet_pnl_drop_fte_jump_jr2025"
COMM = "comm_desprong_jr2025_statutory_maatwerk_empty_omzet_bruto_pnl_drop"

BRUTO = 4526068
BRUTO24 = 4234619
PNL = 56628
PNL24 = 58754
EQUITY = 2621748
EQUITY24 = 2574854
FTE = 110.9
FTE24 = 106.4
FILED = "20.06.2026"
EMAIL = "info@desprongvzw.be"

# cost 3.5 · abs 6.0 · diff 3 → pi = 0.55*3.5 + 0.35*6.0 + 0.1*7 = 4.725 → 4.75
ABS, COST, DIFF, PI = 6.0, 3.5, 3.0, 4.75


def read_csv(path: str):
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
        f"De Sprong YE2025 empty omzet bruto {BRUTO} (+6.88%) pnl {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0466328686/de-sprong\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_desprong_jr2025_cw_en",
        "title": "De Sprong Meerhout YE2025 CW EN (bruto JUMP 4.53m / empty omzet / FTE JUMP)",
        "url": "https://www.companyweb.be/en/0466328686/de-sprong",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; empty omzet; bruto {BRUTO} JUMP +6.88%; pnl {PNL} DROP -3.62%; equity {EQUITY}; FTE JUMP {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_desprong_jr2025_cw_nl",
        "title": "De Sprong Meerhout YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0466328686/de-sprong",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; same euros; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_desprong_jr2025_cw_fr",
        "title": "De Sprong Meerhout YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0466328686/de-sprong",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; CA unpublished; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_desprong_kbo_0466328686",
        "title": "KBO De Sprong 0466.328.686 Actief VZW 9 VE NACE 88.993 aanbestedende overheid",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=466328686",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Actief; VZW sinds 27.01.1999; 9 VE; zetel Vaartstraat 1 2450 Meerhout; RSZ/BTW NACE 88.993; aanbestedende overheid; absorbed Fietsenatelier Mol 0465.589.508 (2015)",
    },
    {
        "source_id": "src_desprong_site_contact_2286",
        "title": "De Sprong FOI channel info@desprongvzw.be / desprongvzw.be",
        "url": "https://www.desprongvzw.be/",
        "publisher": "De Sprong VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; +32 14 86 98 45; Kempen maatwerk groen/recyclage/fiets (shops closing Jul 2026)",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "De Sprong VZW (Meerhout / Kempen maatwerk)",
    "name_fr": "De Sprong ASBL (Meerhout / entreprise de travail adapté Campine)",
    "name_en": "De Sprong sheltered workshop VZW (Meerhout Kempen maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.desprongvzw.be/",
    "foi_email": EMAIL,
    "foi_postal": "Vaartstraat 1, 2450 Meerhout",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 9 VE VZW NACE 88.993 "
        f"aanbestedende overheid; empty omzet; bruto JUMP {BRUTO} (+6.88%) pnl DROP {PNL} (-3.62%) "
        f"equity JUMP {EQUITY} (+1.82%) FTE JUMP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; bike shops closing Jul2026 press; after Mobiel@2285; Manupal still YE2024; "
        f"AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_desprong_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto YE2025 (omzet unpublished)",
        "source_id": "src_desprong_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +6.88% vs {BRUTO24}; empty omzet",
    },
    {
        "budget_id": "bud_desprong_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025",
        "source_id": "src_desprong_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -3.62% vs {PNL24}",
    },
    {
        "budget_id": "bud_desprong_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_desprong_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +1.82% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_desprong_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_desprong_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} JUMP vs {FTE24}",
    },
    {
        "budget_id": "bud_desprong_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW pnl YE2024 comparative",
        "source_id": "src_desprong_jr2025_cw_en",
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
    "title": f"De Sprong YE2025 leftover dual (bruto JUMP 4.53m / empty omzet / FTE JUMP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "maatwerkers Kempen Meerhout-Geel-Mol / VDAB-ESF path",
    "legal_basis": f"VZW De Sprong (KBO {KBO}; Actief; 9 VE; RSZ NACE 88.993; aanbestedende overheid)",
    "decision_date": "2026-06-20",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0466328686/de-sprong",
    "stated_goal": "Flemish Kempen maatwerk groen/recyclage/fiets — inclusive employment",
    "cut_option": "Publish NBB PDF assets/debt; disclose empty omzet vs bruto 4.53m loonkost matrix; recon bike-shop exit vs FTE JUMP",
    "source_id": "src_desprong_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>DeSprong>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; empty omzet; after Mobiel@2285; Manupal YE2024",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "De Sprong bruto JUMP 4.53m / empty omzet / FTE JUMP 110.9 (YE2025 Kempen maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>DeSprong>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW empty omzet / bruto JUMP {BRUTO} (+6.88%) / pnl DROP {PNL} (-3.62%) / "
        f"equity JUMP {EQUITY} / FTE JUMP {FTE} (vs {FTE24}) / 9 VE / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_desprong_jr2025_cw_en",
    "beneficiaries": "maatwerkers Kempen / VDAB-ESF path",
    "stated_goal": "Flemish maatwerk groen/recyclage/fiets",
    "measured_outcome": f"empty omzet; bruto JUMP +6.88%; pnl DROP -3.62%; FTE JUMP {FTE}; bike shops closing Jul2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 4.53m; recon FTE JUMP vs bike exit",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; Manupal still YE2024; AGB Bornem JR2024; FARO/AIESH YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>DeSprong>NBB_PDF_assets_debt_empty_omzet_bruto",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
        f"pnl DROP EUR{PNL}; FTE JUMP {FTE}; VDAB/ESF loonkost matrix; bike-shop exit path Jul2026"
    ),
    "why_it_matters": (
        f"Medium CW shows Kempen maatwerk VZW (bruto 4.53m / empty omzet / 9 VE / FTE JUMP) "
        f"under public loonkost + aanbestedende overheid; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "De Sprong VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Vaartstraat 1, 2450 Meerhout",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Mobiel@2285; Manupal YE2024",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — De Sprong Meerhout (NBB PDF / empty omzet / bruto 4.53m / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Sprong VZW — KBO **{KBO}** (Actief; Vaartstraat 1, 2450 Meerhout; **9 VE**; FTE {FTE}; NACE **88.993**; aanbestedende overheid)  
**recipient:** {EMAIL} · Vaartstraat 1, 2450 Meerhout (+32 14 86 98 45)  
**sources:** [CW EN](https://www.companyweb.be/en/0466328686/de-sprong) · [CW NL](https://www.companyweb.be/nl/0466328686/de-sprong) · [CW FR](https://www.companyweb.be/fr/0466328686/de-sprong) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=466328686) · [site](https://www.desprongvzw.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **DE SPRONG**; **9 VE**; zetel Vaartstraat 1, 2450 Meerhout; RSZ NACE **88.993**; aanbestedende overheid sinds 27.01.1999; absorbed Fietsenatelier Mol 2015.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +6.88% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP −3.62%; equity **EUR{EQUITY:,}** JUMP +1.82%; FTE **{FTE}** JUMP (vs {FTE24}); filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Manupal/Vlotter/Buseloc/De Ploeg still YE2024. After Mobiel@2285. Do NOT redo Mobiel/Posthoorn/Ateljee/Die Zukunft/TWI/A94 stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Sprong VZW
via {EMAIL}
Vaartstraat 1, 2450 Meerhout
Betreft: Openbaarmaking jaarrekening 2025 De Sprong (KBO {KBO})

Geachte,

Op grond van het Bestuursdecreet vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO} gepubliceerd is.
3. VDAB/ESF/gemeente loonkostsubsidiematrix YE2025 (FTE {FTE}).
4. Toelichting FTE JUMP {FTE24}→{FTE} naast sluiting fietswinkels Meerhout/Mol (jul 2026).
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
            f"leftover dual — De Sprong Meerhout YE2025 Medium "
            f"(bruto JUMP 4.53m / empty omzet / FTE JUMP {FTE})"
        )
        r["notes"] = (
            f"tick{TICK} De Sprong YE2025; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; "
            f"FTE {FTE}; FOI ready NOT sent; Manupal still YE2024"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after De Sprong — prefer AGB/FARO-YE2025/AIESH-REW/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after De Sprong YE2025 Medium (bruto JUMP 4.53m / empty omzet / FTE JUMP). "
                "Prefer NON-stall: AGB Bornem if JR2025; FARO/AIESH/REW/Citeco/Groupe Foes if YE2025; "
                "else Manupal/Vlotter/Buseloc/De Ploeg if YE2025 or unused ETA Village Liégeois/"
                "Ateliers de Mons. Do NOT redo De Sprong/Mobiel/Posthoorn/Ateljee/Die Zukunft/"
                "TWI/A94/eurakor/Alternatief."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} De Sprong; Manupal/Vlotter/Buseloc/De Ploeg YE2024; "
                f"AGB Bornem JR2024; FARO/AIESH YE2024; next every-10 2290"
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
            f"tick{TICK} leftover dual De Sprong {KBO} Medium "
            f"(bruto JUMP {BRUTO} +6.88%; empty omzet; pnl DROP {PNL}; equity JUMP {EQUITY}; "
            f"FTE JUMP {FTE}; 9 VE Meerhout Kempen maatwerk); after Mobiel@2285; "
            f"Manupal still YE2024; AGB Bornem JR2024; FARO/AIESH YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2290; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} De Sprong Meerhout (bruto JUMP 4.53m / empty omzet / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **rq_2285 Mobiel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Manupal/Vlotter/Buseloc/De Ploeg still **YE2024**. Took FREE Flemish Kempen maatwerk **De Sprong VZW** YE2025 (KBO **{KBO}**; Vaartstraat 1 Meerhout; **Actief** **9 VE**; NACE **88.993** aanbestedende overheid; groen/recyclage/fiets; info@desprongvzw.be). Do not redo Mobiel/Posthoorn/Ateljee/Die Zukunft/TWI/A94 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +6.88% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP -3.62% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +1.82%; FTE **{FTE}** JUMP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 9 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Manupal-Vlotter-Buseloc-if-YE2025 / unused ETA).
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
