# -*- coding: utf-8 -*-
"""Tick 2302: finish in_progress Thomas More Mechelen-Antwerpen YE2025 leftover dual."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2302")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2302"
RQ = "rq_2302"
NEXT_RQ = "rq_2303"
ENTITY = "vzw_thomas_more_mechelen_antwerpen"
KBO = "0455.411.733"
GAP = "gap_tmma_nbb_pdf_assets_debt_omzet_92_12m_pnl_jump_equity_82_59m_fte_opacity_he_matrix_l5"
LB = "lb_tmma_omzet_jump_92_12m_pnl_jump_16pct_equity_82_59m_jr2025"
COMM = "comm_tmma_jr2025_statutory_hogeschool_omzet_pnl_jump_equity"

OMZET = 92122094
OMZET24 = 87258066
BRUTO = 85855378
BRUTO24 = 81128349
PNL = 6481920
PNL24 = 5577807
EQUITY = 82591264
EQUITY24 = 76965294
FTE = 259.0
FTE24 = 247.0
FILED = "01.04.2026"
EMAIL = "info@thomasmore.be"
RATIO = round(BRUTO / OMZET, 2)  # ~0.93

# cost 5.5 (~92m) · abs 6.2 (public HE omzet 92m + equity 82.6m + FTE opacity) · diff 3
# pi = 0.55*5.5 + 0.35*6.2 + 0.1*7 = 5.895 → 5.9
ABS, COST, DIFF, PI = 6.2, 5.5, 3.0, 5.9


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
        f"TMMA YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} "
        f"equity JUMP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0455411733/thomas-more-mechelen-antwerpen\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455411733\n"
        "https://thomasmore.be/\n"
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
        "source_id": "src_tmma_jr2025_cw_en",
        "title": "TMMA YE2025 CW EN (omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m)",
        "url": "https://www.companyweb.be/en/0455411733/thomas-more-mechelen-antwerpen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+5.57%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +5.83%); pnl JUMP {PNL} (+16.21%); equity JUMP {EQUITY} (+7.31%); "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_tmma_jr2025_cw_nl",
        "title": "TMMA YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0455411733/thomas-more-mechelen-antwerpen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_tmma_jr2025_cw_fr",
        "title": "TMMA YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0455411733/thomas-more-mechelen-antwerpen",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_tmma_kbo_0455411733",
        "title": "KBO Thomas More Mechelen-Antwerpen 0455.411.733 Actief VZW 11 VE NACE 85.402",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455411733",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 07.11.1994; 11 VE; Zandpoortvest 60 2800 Mechelen; "
            f"RSZ 85.402 vrij gesubsidieerd hoger onderwijs; Aanbestedende overheid; "
            f"absorbed Thomas More Antwerpen 0420.575.568 + LASCENTRUM"
        ),
    },
    {
        "source_id": "src_tmma_site_contact_2302",
        "title": "Thomas More FOI channel info@thomasmore.be / onthaal.mechelen@thomasmore.be",
        "url": "https://thomasmore.be/",
        "publisher": "Thomas More Mechelen-Antwerpen VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; {EMAIL}; onthaal.mechelen@thomasmore.be; Zandpoortvest 60 2800 Mechelen; "
            f"T 015 36 91 00; VL freely subsidised hogeschool"
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
    "name_nl": "Thomas More Mechelen-Antwerpen VZW (hogeschool)",
    "name_fr": "Thomas More Malines-Anvers ASBL (haute école)",
    "name_en": "Thomas More Mechelen-Antwerp VZW (university college)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://thomasmore.be/",
    "foi_email": EMAIL,
    "foi_postal": "Zandpoortvest 60, 2800 Mechelen",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 11 VE VZW "
        f"NACE 85.402 Aanbestedende overheid; omzet JUMP {OMZET} (+5.57%) bruto JUMP {BRUTO} "
        f"(~{RATIO}x) pnl JUMP {PNL} (+16.21%) equity JUMP {EQUITY} (+7.31%) FTE JUMP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Havinet@2301; "
        f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024; "
        f"DISTINCT Thomas More Kempen 0409.667.028; not TE-additive of 348bn"
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
        "budget_id": "bud_tmma_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025 primary envelope (VL-subsidised HE)",
        "source_id": "src_tmma_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +5.57% vs {OMZET24}",
    },
    {
        "budget_id": "bud_tmma_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 (~{RATIO}x omzet)",
        "source_id": "src_tmma_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +5.83% vs {BRUTO24}; ~{RATIO}x omzet",
    },
    {
        "budget_id": "bud_tmma_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 JUMP",
        "source_id": "src_tmma_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} JUMP +16.21% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_tmma_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 JUMP",
        "source_id": "src_tmma_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +7.31% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_tmma_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025 (may undercount vs campus headcount)",
        "source_id": "src_tmma_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}; reconcile vs full academic/admin headcount FOI",
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
        f"TMMA YE2025 leftover dual (omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "students / staff Mechelen-Antwerpen campuses (VL freely subsidised HE)",
    "legal_basis": (
        f"VZW Thomas More Mechelen-Antwerpen (KBO {KBO}; Actief; 11 VE; NACE 85.402; "
        f"Aanbestedende overheid)"
    ),
    "decision_date": "2026-04-01",
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
    "evaluation_url": "https://www.companyweb.be/en/0455411733/thomas-more-mechelen-antwerpen",
    "stated_goal": "VL freely subsidised higher education (hogeschool Mechelen-Antwerpen)",
    "cut_option": (
        "Publish NBB PDF assets/debt; disclose VL werkingsuitkering vs tuition/other revenue split; "
        "reconcile CW FTE 259 vs campus headcount; equity 82.59m deployment path"
    ),
    "source_id": "src_tmma_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>ThomasMore_MA>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; omzet primary {OMZET}; after Havinet@2301; DISTINCT TM Kempen",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "TMMA omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m (YE2025)",
    "level": "L5",
    "type": "hogeschool_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>ThomasMore_MA>JR2025",
    "annual_cost_eur": str(OMZET),
    "total_cost_eur": str(OMZET),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+5.57%) / bruto JUMP {BRUTO} (~{RATIO}x) / "
        f"pnl JUMP {PNL} (+16.21%) / equity JUMP {EQUITY} (+7.31%) / FTE JUMP {FTE} / filed {FILED}; "
        f"VL-subsidy share opaque; assets/debt Unknown"
    ),
    "confidence": "medium",
    "source_id": "src_tmma_jr2025_cw_en",
    "beneficiaries": "students/staff Mechelen-Antwerpen campuses",
    "stated_goal": "VL freely subsidised hogeschool education",
    "measured_outcome": (
        f"omzet JUMP +5.57%; pnl JUMP +16%; equity JUMP +7.3% to 82.59m; CW FTE {FTE} opacity vs campuses"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        "Publish NBB PDF assets/debt FOI; disclose VL werkingsuitkering vs tuition split; "
        "reconcile FTE/headcount; equity deployment path"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; after Havinet@2301; AGB Bornem JR2024; "
        f"FARO/AIESH YE2024; DISTINCT TM Kempen"
    ),
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>ThomasMore_MA>NBB_PDF_assets_debt_omzet_pnl_equity",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); VL werkingsuitkering vs tuition/other revenue "
        f"inside omzet EUR{OMZET}; reconcile CW FTE {FTE} vs campus academic/admin headcount; "
        f"equity EUR{EQUITY} deployment / reserved funds path"
    ),
    "why_it_matters": (
        f"Medium CW shows VL freely subsidised hogeschool (omzet 92.12m / pnl JUMP +16% / "
        f"equity 82.59m / FTE 259) under public HE path; assets/debt + subsidy split unpublished"
    ),
    "priority": "8",
    "recipient_body": "Thomas More Mechelen-Antwerpen VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Zandpoortvest 60, 2800 Mechelen",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Havinet@2301; claimed TMMA",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Thomas More Mechelen-Antwerpen (NBB PDF / omzet 92.12m / equity 82.59m)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Thomas More Mechelen-Antwerpen VZW — KBO **{KBO}** (Actief; Zandpoortvest 60, 2800 Mechelen; **11 VE**; FTE {FTE}; NACE **85.402**; Aanbestedende overheid)  
**recipient:** {EMAIL} · cc onthaal.mechelen@thomasmore.be · Zandpoortvest 60, 2800 Mechelen (T 015 36 91 00)  
**sources:** [CW EN](https://www.companyweb.be/en/0455411733/thomas-more-mechelen-antwerpen) · [CW NL](https://www.companyweb.be/nl/0455411733/thomas-more-mechelen-antwerpen) · [CW FR](https://www.companyweb.be/fr/0455411733/thomas-more-mechelen-antwerpen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455411733) · [site](https://thomasmore.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0455411733)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Thomas More Mechelen-Antwerpen** sinds **07.11.1994**; **11 VE**; zetel Zandpoortvest 60, 2800 Mechelen; RSZ NACE **85.402**; Aanbestedende overheid; absorbed Thomas More Antwerpen + LASCENTRUM.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +5.57%; bruto **EUR{BRUTO:,}** JUMP +5.83% (~**{RATIO}x**); pnl **EUR{PNL:,}** JUMP +16.21%; equity **EUR{EQUITY:,}** JUMP +7.31%; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024; Citeco/Groupe Foes YE2024; Gandae YE2024. After Havinet@2301. DISTINCT Thomas More Kempen (0409.667.028). Do NOT redo Havinet/De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Thomas More Mechelen-Antwerpen VZW
via {EMAIL}
Zandpoortvest 60, 2800 Mechelen
Betreft: Openbaarmaking jaarrekening 2025 TMMA (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Uitsplitsing omzet EUR{OMZET}: Vlaamse werkingsuitkering vs inschrijvingsgelden vs overig.
3. Toelichting pnl JUMP EUR{PNL} (+16.21%) en equity JUMP EUR{EQUITY} (+7.31%).
4. Verzoening CW-personeelscijfer FTE {FTE} met campus academisch/administratief headcount.
5. Bestemmingsfondsen / reserves binnen equity YE2025.

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
            "leftover dual — TMMA YE2025 Medium "
            "(omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m / FTE 259)"
        )
        r["notes"] = (
            f"tick{TICK} TMMA {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl JUMP {PNL}; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 11 VE NACE 85.402 Mechelen; "
            f"neerlegging {FILED}; assets/debt Unknown; FOI ready NOT sent; "
            f"after Havinet@2301; stalls AGB/FARO/AIESH YE2024; next EVERY-10 2310"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after TMMA — prefer AGB/FARO-YE2025/"
                "AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after TMMA YE2025 Medium "
                f"(omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m). "
                "Prefer leftover dual: AGB Bornem/APB → FARO/AIESH if YE2025 → Citeco/Groupe Foes "
                "if YE2025 → unused DSO/water/nuclear/IGS/HVZ or FREE ETA-VAPH-WZC-maatwerk "
                "(Gandae if YE2025; Thomas More Kempen if unused YE2025; Aralea/Manupal if YE2025). "
                "Do NOT redo TMMA/Havinet/De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/"
                "MPI Oosterlo/Entiris/Mirto/Blankedale/Werkmmaat stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} TMMA; AGB Bornem JR2024; "
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
            f"tick{TICK} leftover dual TMMA {KBO} Medium "
            f"(omzet JUMP {OMZET} +5.57%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +16.21%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 11 VE hogeschool Mechelen-Antwerpen); "
            f"after Havinet@2301; AGB Bornem JR2024; FARO/AIESH YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2310; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Thomas More Mechelen-Antwerpen (omzet JUMP 92.12m / pnl JUMP +16% / equity 82.59m / Medium)

- Unit: **{RQ}** finish **in_progress** leftover dual after **Havinet@2301** (claim notes: Thomas More MA). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Gandae still **YE2024**. Took claimed FREE VL hogeschool **Thomas More Mechelen-Antwerpen VZW** YE2025 (KBO **{KBO}**; Zandpoortvest 60 Mechelen; **Actief** **11 VE**; NACE **85.402**; Aanbestedende overheid). Do not redo Havinet/De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/MPI Oosterlo stack. DISTINCT Thomas More Kempen.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +5.57% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +5.83% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +16.21% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +7.31%; FTE **{FTE}** (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 11 VE VZW. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk / TM Kempen-if-unused).
"""
    )

print(
    f"OK tick{TICK} {ENTITY} omzet={OMZET} bruto={BRUTO} ratio={RATIO}x "
    f"pnl={PNL} pi={PI} next={NEXT_RQ}"
)
