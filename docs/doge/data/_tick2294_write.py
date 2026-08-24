# -*- coding: utf-8 -*-
"""Tick 2294: Mo-Clean YE2025 leftover dual (final filing before Den Azalee fusion)."""
from __future__ import annotations

import csv
import os

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2294")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = "2026-08-27T16:00:00Z"
TICK = "2294"
RQ = "rq_2294"
NEXT_RQ = "rq_2295"
ENTITY = "vzw_mo_clean_sint_niklaas"
KBO = "0453.129.362"
GAP = "gap_mo_clean_nbb_pdf_assets_debt_empty_omzet_bruto_2_16m_pnl_loss_flip_equity_drop_45pct_fusion_matrix_l5"
LB = "lb_mo_clean_bruto_2_16m_empty_omzet_pnl_loss_flip_equity_drop_45pct_fusion_jr2025"
COMM = "comm_mo_clean_jr2025_statutory_empty_omzet_bruto_pnl_loss_flip_fusion"

BRUTO = 2160004
BRUTO24 = 2256865
PNL = -138224
PNL24 = 27907
EQUITY = 195665
EQUITY24 = 356155
FTE = 60.0
FTE24 = 58.9
FILED = "08.07.2026"
EMAIL = "info@vzwdenazalee.be"
# successor Den Azalee absorbed Mo-Clean 01.01.2026

# cost 4.0 (~2.16m) · abs 7.5 · diff 3 → pi = 0.55*4 + 0.35*7.5 + 0.1*7 = 5.525 → 5.55
ABS, COST, DIFF, PI = 7.5, 4.0, 3.0, 5.55


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
        f"Mo-Clean YE2025 Closed/Stopgezet empty omzet bruto {BRUTO} pnl LOSS FLIP {PNL} "
        f"equity DROP {EQUITY} FTE {FTE} filed {FILED}; absorbed by Den Azalee 0456.719.748 since 01.01.2026\n"
        "https://www.companyweb.be/en/0453129362/maatwerkbedrijf-mo-clean\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453129362\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_mo_clean_jr2025_cw_en",
        "title": "Mo-Clean YE2025 CW EN (bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / Closed)",
        "url": "https://www.companyweb.be/en/0453129362/maatwerkbedrijf-mo-clean",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW EN; Status Closed; empty omzet; bruto {BRUTO} DROP -4.29%; pnl {PNL} LOSS FLIP; equity {EQUITY} DROP -45.06%; FTE {FTE}; filed {FILED}",
    },
    {
        "source_id": "src_mo_clean_jr2025_cw_nl",
        "title": "Mo-Clean YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0453129362/maatwerkbedrijf-mo-clean",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Status Stopgezet; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_mo_clean_jr2025_cw_fr",
        "title": "Mo-Clean YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0453129362/maatwerkbedrijf-mo-clean",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW FR; Statut Cessation; CA unpublished; marge brute {BRUTO}; résultat {PNL}; capitaux {EQUITY}; personnel {FTE}",
    },
    {
        "source_id": "src_mo_clean_kbo_0453129362",
        "title": "KBO Mo-Clean 0453.129.362 Stopgezet Fusie door overneming → Den Azalee 0456.719.748",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453129362",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-27",
        "source_class": "kbo",
        "notes": f"tick{TICK}; Strong KBO Stopgezet sinds 01.01.2026; Fusie door overneming; absorbed by Den Azalee 0456.719.748; 1 VE; Klein-Hulststraat 6 9100 Sint-Niklaas; VZW sinds 06.06.1994; BTW NACE 96.999",
    },
    {
        "source_id": "src_mo_clean_foi_den_azalee_successor_2294",
        "title": "Den Azalee successor FOI channel info@vzwdenazalee.be (Mo-Clean absorbed 01.01.2026)",
        "url": "https://www.denazalee.be/",
        "publisher": "Den Azalee VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Nobels-Peelmanstraat 17 9100 Sint-Niklaas; Mo-Clean site mo-clean.be 503 at access; FOI via absorbing entity",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Mo-Clean VZW (Sint-Niklaas / maatwerk; Stopgezet fusie → Den Azalee)",
    "name_fr": "Mo-Clean ASBL (Saint-Nicolas / travail adapté; Cessation fusion → Den Azalee)",
    "name_en": "Mo-Clean VZW (Sint-Niklaas maatwerk; Closed merger into Den Azalee)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://mo-clean.be/",
    "foi_email": EMAIL,
    "foi_postal": "Klein-Hulststraat 6, 9100 Sint-Niklaas (successor: Nobels-Peelmanstraat 17, Den Azalee)",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Stopgezet 01.01.2026 Fusie door overneming → Den Azalee 0456.719.748; "
        f"1 VE; empty omzet; bruto DROP {BRUTO} (-4.29%) pnl LOSS FLIP {PNL} equity DROP {EQUITY} (-45.06%) "
        f"FTE {FTE}; neerlegging {FILED}; assets/debt Unknown; FOI {GAP} via successor {EMAIL}; "
        f"DISTINCT Den Azalee@2281/2224; after NLZ@2293; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_mo_clean_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto YE2025 (omzet unpublished; final year pre-fusion)",
        "source_id": "src_mo_clean_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} DROP -4.29% vs {BRUTO24}; empty omzet; Stopgezet",
    },
    {
        "budget_id": "bud_mo_clean_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 LOSS FLIP",
        "source_id": "src_mo_clean_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} LOSS FLIP vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_mo_clean_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_mo_clean_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} DROP -45.06% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_mo_clean_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_mo_clean_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}",
    },
    {
        "budget_id": "bud_mo_clean_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": str(PNL24),
        "amount_min_eur": str(PNL24),
        "amount_max_eur": str(PNL24),
        "basis": "CW pnl YE2024 comparative",
        "source_id": "src_mo_clean_jr2025_cw_en",
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
    "title": "Mo-Clean YE2025 leftover dual (bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / fusion Stopgezet / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "maatwerkers Sint-Niklaas cleaning/fietsmobiliteit / Den Azalee fusion perimeter",
    "legal_basis": f"VZW Mo-Clean (KBO {KBO}; Stopgezet 01.01.2026 Fusie → Den Azalee 0456.719.748; 1 VE)",
    "decision_date": "2026-07-08",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "closed",
    "evaluation_url": "https://www.companyweb.be/en/0453129362/maatwerkbedrijf-mo-clean",
    "stated_goal": "Flemish maatwerk cleaning/fietsmobiliteit Sint-Niklaas — absorbed into Den Azalee 01.01.2026",
    "cut_option": "Publish NBB PDF assets/debt; disclose empty omzet vs bruto 2.16m; recon LOSS FLIP + equity DROP -45% vs Den Azalee fusion perimeter",
    "source_id": "src_mo_clean_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Sint_Niklaas>MoClean>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; final YE2025 pre-fusion; DISTINCT Den Azalee@2281; after NLZ@2293",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Mo-Clean bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / fusion Closed (YE2025)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory_fusion_final",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Sint_Niklaas>MoClean>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW empty omzet / bruto DROP {BRUTO} (-4.29%) / pnl LOSS FLIP {PNL} vs {PNL24} / "
        f"equity DROP {EQUITY} (-45.06%) / FTE {FTE} / Stopgezet fusion → Den Azalee / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_mo_clean_jr2025_cw_en",
    "beneficiaries": "maatwerkers Sint-Niklaas / Den Azalee fusion perimeter",
    "stated_goal": "Flemish maatwerk cleaning/mobility — final year before Den Azalee absorb",
    "measured_outcome": f"empty omzet; bruto DROP; pnl LOSS FLIP; equity DROP -45%; FTE {FTE}; Closed 01.01.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt FOI via Den Azalee; disclose empty omzet; recon LOSS FLIP + equity DROP -45% vs fusion matrix",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; DISTINCT Den Azalee@2281; AGB Bornem JR2024; FARO/AIESH YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Sint_Niklaas>MoClean>NBB_PDF_assets_debt_empty_omzet_pnl_loss_flip_fusion",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
        f"pnl LOSS FLIP EUR{PNL} vs YE2024 EUR{PNL24}; equity DROP EUR{EQUITY} (-45.06%); "
        f"Den Azalee fusion perimeter 01.01.2026 (KBO 0456.719.748) asset/liability transfer"
    ),
    "why_it_matters": (
        f"Medium CW shows final YE2025 of Stopgezet Flemish maatwerk Mo-Clean (bruto 2.16m / empty omzet / "
        f"pnl LOSS FLIP / equity DROP -45%) absorbed into Den Azalee; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Den Azalee VZW (successor / absorbing entity of Mo-Clean)",
    "recipient_email": EMAIL,
    "recipient_postal": "Nobels-Peelmanstraat 17, 9100 Sint-Niklaas (Mo-Clean was Klein-Hulststraat 6)",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO Stopgezet; FOI via Den Azalee successor; after NLZ@2293",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Mo-Clean (NBB PDF / empty omzet / bruto 2.16m / pnl LOSS FLIP / equity DROP -45% / fusion)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Maatwerkbedrijf Mo-Clean VZW — KBO **{KBO}** (Stopgezet sinds 01.01.2026; Fusie door overneming → Den Azalee **0456.719.748**; Klein-Hulststraat 6, 9100 Sint-Niklaas; **1 VE**; FTE {FTE})  
**recipient:** {EMAIL} · Nobels-Peelmanstraat 17, 9100 Sint-Niklaas (absorbing entity Den Azalee)  
**sources:** [CW EN](https://www.companyweb.be/en/0453129362/maatwerkbedrijf-mo-clean) · [CW NL](https://www.companyweb.be/nl/0453129362/maatwerkbedrijf-mo-clean) · [CW FR](https://www.companyweb.be/fr/0453129362/maatwerkbedrijf-mo-clean) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453129362) · [Den Azalee](https://www.denazalee.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO Stopgezet + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: **Stopgezet** sinds 01.01.2026; rechtstoestand **Fusie door overneming**; opgeslorpt door Den Azalee **0456.719.748**; 1 VE; zetel Klein-Hulststraat 6, 9100 Sint-Niklaas; VZW sinds 06.06.1994.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP −4.29%; pnl **EUR{PNL:,}** LOSS FLIP vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −45.06%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Aralea/Manupal/De Ploeg/Vlotter YE2024. After NLZ@2293. Do NOT redo NLZ/Labor/Intro Schoonmaak/Den Azalee/Buseloc/Op Maat/REW stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Den Azalee VZW (rechtsopvolger Mo-Clean VZW)
via {EMAIL}
Nobels-Peelmanstraat 17, 9100 Sint-Niklaas
Betreft: Openbaarmaking jaarrekening 2025 Mo-Clean (KBO {KBO}) + fusieperimeter

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 Mo-Clean (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO} gepubliceerd is.
3. Toelichting pnl LOSS FLIP EUR{PNL} (vs YE2024 EUR{PNL24}) en equity DROP EUR{EQUITY} (−45.06%).
4. Fusieperimeter 01.01.2026: overgenomen activa/schulden/FTE van Mo-Clean in Den Azalee (KBO 0456.719.748).
5. Schulden LT/KT en liquide middelen YE2025 Mo-Clean.

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
            f"leftover dual — Mo-Clean YE2025 Medium "
            f"(bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / fusion Stopgezet)"
        )
        r["notes"] = (
            f"tick{TICK} Mo-Clean YE2025 final filing; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; "
            f"FTE {FTE}; Stopgezet fusie → Den Azalee; FOI ready NOT sent; DISTINCT Den Azalee@2281"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Mo-Clean — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after Mo-Clean YE2025 Medium "
                "(bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / fusion). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH if YE2025, else unused DSO/water/nuclear/IGS/HVZ, else unused "
                "ETA-VAPH-WZC-maatwerk (Aralea/Manupal/De Ploeg/Vlotter YE2024). "
                "Do NOT redo Mo-Clean/Den Azalee/NLZ/Labor/Intro Schoonmaak/Buseloc/Op Maat/REW stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Mo-Clean; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
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
            f"tick{TICK} leftover dual Mo-Clean {KBO} Medium "
            f"(bruto DROP {BRUTO}; empty omzet; pnl LOSS FLIP {PNL}; equity DROP {EQUITY} -45.06%; "
            f"FTE {FTE}; Stopgezet fusie → Den Azalee 0456.719.748); after NLZ@2293; "
            f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; "
            f"next {NEXT_RQ}; next every-10 2300; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Mo-Clean Sint-Niklaas (bruto 2.16m / empty omzet / pnl LOSS FLIP / equity DROP -45% / fusion Stopgezet / Medium)

- Unit: **{RQ}** leftover dual after **rq_2293 NLZ Mechelen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Aralea/Manupal/De Ploeg/Vlotter still **YE2024**. Took FREE Flemish maatwerk **Mo-Clean VZW** YE2025 final filing (KBO **{KBO}**; Klein-Hulststraat 6 Sint-Niklaas; **Stopgezet** 01.01.2026 Fusie door overneming → Den Azalee **0456.719.748**; **1 VE**). Do not redo NLZ/Labor/Intro Schoonmaak/Den Azalee/Buseloc/Op Maat/REW stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP -4.29% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** LOSS FLIP vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP -45.06%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Stopgezet 1 VE VZW. Assets/debt Unknown. Medium. FOI via successor {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk).
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
