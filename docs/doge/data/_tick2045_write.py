# ephemeral tick2045 — AGB Bornem JR2024 Strong official PDF
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T16:25:00Z"
ENTITY = "agb_bornem"
GAP = "gap_agb_bornem_omzet_empty_debt_20_50m_jr2025_l5"
SRC = "src_agb_bornem_jr2024_statutair_official"
SRC_BBC = "src_agb_bornem_jr2024_bbc_official"
SRC_RVB = "src_agb_bornem_jr2024_rvb_official"
SRC_CW = "src_agb_bornem_jr2024_cw"
SRC_CW_EN = "src_agb_bornem_jr2024_cw_en"
SRC_CW_FR = "src_agb_bornem_jr2024_cw_fr"
SRC_KBO = "src_agb_bornem_kbo_2044"
SRC_PAGE = "src_agb_bornem_jr_page_2044"

ASSETS = "21871182"
EQUITY = "1360756"
DEBT = "20499767"
BRUTO = "2767146"
PNL = "1379250"
CASH = "646906"
EBIT = "1926693"
BUDGETAIR = "2764770"
GUARANTEED = "17794002"
FTE = "0"
# YE2023 comps (statutair)
ASSETS23 = "19630966"
EQUITY23 = "363663"
DEBT23 = "19253737"
BRUTO23 = "3162329"
PNL23 = "2078354"
CASH23 = "855824"
# pi = 0.55*6.0 + 0.35*5.5 + 0.10*(10-3) = 3.3 + 1.925 + 0.7 = 5.925 → 5.9
PI = "5.9"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2045")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "AGB Bornem Jaarrekening 2024 (Statutair) official municipal PDF",
        "url": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
        "publisher": "AGB Bornem / Gemeente Bornem",
        "accessed_date": "2026-08-24",
        "source_class": "primary_official",
        "notes": (
            f"tick2045; VKT-inb YE2024; assets JUMP {ASSETS} equity JUMP {EQUITY} debt JUMP {DEBT} "
            f"bruto DROP {BRUTO} pnl DROP {PNL} cash DROP {CASH} ebit {EBIT}; omzet/60-61/62 empty; "
            f"FTE 0; guaranteed debt {GUARANTEED}; GR/RvB vaststelling 14.10.2025; "
            "raw docs/doge/data/raw/tick2045/agb_statutair.pdf"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_BBC,
        "title": "AGB Bornem Jaarrekening 2024 BBC (incl. bijlagen) official",
        "url": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
        "publisher": "AGB Bornem / Gemeente Bornem",
        "accessed_date": "2026-08-24",
        "source_class": "primary_official",
        "notes": "tick2045; BBC JR2024 policy+finance pack (~5.8MB); complements statutair; raw docs/doge/data/raw/tick2045/agb_bbc.pdf",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_RVB,
        "title": "Vaststelling RVB Jaarrekening 2024 AGB Bornem (14.10.2025)",
        "url": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
        "publisher": "AGB Bornem Raad van Bestuur",
        "accessed_date": "2026-08-24",
        "source_class": "primary_official",
        "notes": f"tick2045; RvB 14.10.2025 vaststelling; budgettair resultaat EUR{BUDGETAIR}; raw docs/doge/data/raw/tick2045/agb_rvb.pdf",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_CW,
        "title": "Companyweb NL Autonoom Gemeentebedrijf Bornem YE2024",
        "url": "https://www.companyweb.be/nl/0877556624/autonoom-gemeentebedrijf-bornem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2045; YE2024 Medium CW corroboration pnl {PNL} equity {EQUITY} bruto {BRUTO} omzet empty FTE 0; raw docs/doge/data/raw/tick2045/agb_bornem_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_CW_EN,
        "title": "Companyweb EN Autonoom Gemeentebedrijf Bornem YE2024",
        "url": "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2045; EN mirror YE2024; Last balance sheet year 2024; FTE 0; raw docs/doge/data/raw/tick2045/agb_bornem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_CW_FR,
        "title": "Companyweb FR Autonoom Gemeentebedrijf Bornem YE2024",
        "url": "https://www.companyweb.be/fr/0877556624/autonoom-gemeentebedrijf-bornem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2045; FR mirror YE2024; raw docs/doge/data/raw/tick2045/agb_bornem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AGB Bornem 0877.556.624 Actief Autonoom gemeentebedrijf",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0877556624",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2045; Actief; Hingenesteenweg 13 2880 Bornem; NBB consult-enterprise link; email empty in KBO",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_PAGE,
        "title": "Bornem jaarrekening gemeente OCMW en AGB portal",
        "url": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
        "publisher": "Gemeente Bornem",
        "accessed_date": "2026-08-24",
        "source_class": "primary_official",
        "notes": "tick2045; latest approved pack JR2024 (GR 14.10.2025 / web 16.10.2025); JR2025 not listed; older via financien@bornem.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_agb_bornem_assets_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": ASSETS,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 20/58 TOTAAL DER ACTIVA",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; assets JUMP {ASSETS} +11.41pct vs YE2023 {ASSETS23}",
    },
    {
        "budget_id": "bud_agb_bornem_equity_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 10/15 EIGEN VERMOGEN",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; equity JUMP {EQUITY} +274.18pct vs YE2023 {EQUITY23}",
    },
    {
        "budget_id": "bud_agb_bornem_debt_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": DEBT,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 17/49 SCHULDEN",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; debt JUMP {DEBT} +6.47pct vs YE2023 {DEBT23}; guaranteed 9061 {GUARANTEED}",
    },
    {
        "budget_id": "bud_agb_bornem_bruto_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 9900 Brutomarge",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; bruto DROP {BRUTO} -12.50pct vs YE2023 {BRUTO23}; omzet 70 empty",
    },
    {
        "budget_id": "bud_agb_bornem_pnl_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 9904 Winst/verlies",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; pnl DROP {PNL} -33.64pct vs YE2023 {PNL23}",
    },
    {
        "budget_id": "bud_agb_bornem_cash_jr2024_statutory",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": CASH,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "official statutair code 54/58 liquide middelen",
        "source_id": SRC,
        "confidence": "strong",
        "notes": f"tick2045; cash DROP {CASH} -24.41pct vs YE2023 {CASH23}",
    },
    {
        "budget_id": "bud_agb_bornem_budgetair_jr2024_rvb",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": BUDGETAIR,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "RvB vaststelling 14.10.2025 budgettair resultaat",
        "source_id": SRC_RVB,
        "confidence": "strong",
        "notes": f"tick2045; budgettair resultaat {BUDGETAIR} te verwerken in MJP-aanpassing",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_agb_bornem_jr2024_statutory_agb",
    "title": "AGB Bornem YE2024 leftover dual (assets JUMP 21.87m / debt 20.50m / bruto DROP 2.77m)",
    "entity_id": ENTITY,
    "beneficiary": "Bornem residents via AGB sport/culture/patrimonium dual",
    "legal_basis": "Autonoom gemeentebedrijf (Decreet Lokaal Bestuur); KBO 0877.556.624",
    "decision_date": "2025-10-14",
    "start_year": "2024",
    "end_year": "2024",
    "total_envelope_eur": ASSETS,
    "cash_by_year": (
        f'{{"2024_assets":{ASSETS},"2024_equity":{EQUITY},"2024_debt":{DEBT},'
        f'"2024_bruto":{BRUTO},"2024_pnl":{PNL},"2024_cash":{CASH},'
        f'"2024_budgetair":{BUDGETAIR},"2024_guaranteed":{GUARANTEED}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "stated_goal": "Municipal AGB sport/culture/patrimonium operations Bornem",
    "cut_option": "Publish JR2025 + omzet/60-61/62 split FOI; scrutinise 20.50m debt vs empty omzet + 0 FTE dual",
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>AGB>JR2024_statutory_L5",
    "notes": (
        "tick2045; Strong official statutair+BBC+RvB; CW Medium corroboration; omzet/staff empty; "
        "JR2025 still unpublished (existing gap_bornem_dual_jr2025); FARO/AIESH/REW still YE2024; "
        "De Verlosser already mined 1742; not TE-additive of 348bn"
    ),
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_agb_bornem_assets_21_87m_debt_20_50m_jr2024",
    "name": "AGB Bornem assets JUMP 21.87m / debt 20.50m / bruto DROP 2.77m (YE2024)",
    "level": "L5",
    "type": "agb_municipal_patrimonium_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>AGB>JR2024_statutory_L5",
    "annual_cost_eur": ASSETS,
    "total_cost_eur": DEBT,
    "tco_notes": (
        f"statutory assets JUMP {ASSETS} debt JUMP {DEBT} equity JUMP {EQUITY} bruto DROP {BRUTO} "
        f"pnl DROP {PNL} cash DROP {CASH}; omzet/60-61/62 empty; FTE 0; budgettair {BUDGETAIR}"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Bornem residents via AGB sport/culture/patrimonium",
    "stated_goal": "Municipal AGB dual operations",
    "measured_outcome": (
        "Strong official YE2024; 21.87m assets with 20.50m debt and empty omzet; "
        "equity JUMP from 0.36m; JR2025 still unpublished"
    ),
    "absurdity_score": "5.5",
    "cost_score": "6.0",
    "difficulty": "3.0",
    "priority_index": PI,
    "cut_proposal": "Publish JR2025 FOI; map empty omzet vs bruto; debt schedule + guaranteed 17.79m; 0-FTE ops model",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2045 leftover dual AGB; Strong official; TE-adjacent municipal dual not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AGB Bornem (Autonoom gemeentebedrijf)",
    "name_fr": "AGB Bornem (régie communale autonome)",
    "name_en": "AGB Bornem (autonomous municipal company)",
    "level": "local_entity",
    "parent_id": "city_bornem",
    "community_language": "nl",
    "website": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "foi_email": "financien@bornem.be",
    "foi_postal": "Hingenesteenweg 13, 2880 Bornem",
    "notes": (
        "tick2045 YE2024 Strong official statutair+BBC+RvB + Medium CW NL+EN+FR + Strong KBO 0877.556.624 Actief; "
        f"assets JUMP {ASSETS} equity JUMP {EQUITY} debt JUMP {DEBT} bruto DROP {BRUTO} pnl DROP {PNL} cash DROP {CASH} "
        f"budgettair {BUDGETAIR} FTE 0; omzet/60-61/62 empty; vaststelling 14.10.2025; FOI {GAP}; "
        "FARO/AIESH/REW still YE2024; De Verlosser already mined 1742; do not redo Zorggroep Zusters van Berlaar/"
        "Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/"
        "Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara"
    ),
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>AGB>omzet_empty_debt_JR2025",
    "entity_id": ENTITY,
    "what_is_missing": (
        "JR2025 statutair+BBC when approved; omzet(70)/60-61/62 split behind empty YE2024 codes; "
        "debt schedule LT-ST reconciling 20.50m + guaranteed 17.79m; toelagen/huur matrix behind bruto 2.77m; "
        "0-FTE staffing/outsourcing model; link to existing gap_bornem_dual_jr2025_ge_ocmw_agb_l5"
    ),
    "why_it_matters": (
        "Strong official YE2024 shows 21.87m assets / 20.50m debt municipal AGB dual with empty omzet and 0 FTE — "
        "need JR2025 + opacity fill before claiming city↔AGB waste path"
    ),
    "priority": "8",
    "recipient_body": "Lokaal bestuur Bornem / AGB Bornem",
    "recipient_email": "financien@bornem.be",
    "recipient_postal": "Hingenesteenweg 13, 2880 Bornem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_agb_bornem_jr2024_statutory_agb",
    "linked_leaderboard_id": "lb_agb_bornem_assets_21_87m_debt_20_50m_jr2024",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2045; human-send only; Strong official YE2024; JR2025 still unpublished; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
# refresh existing JR2025 dual gap notes
for x in frows:
    if x.get("gap_id") == "gap_bornem_dual_jr2025_ge_ocmw_agb_l5":
        x["updated_utc"] = UTC
        x["notes"] = (
            (x.get("notes") or "")
            + f"; tick2045 AGB JR2024 Strong filled (assets {ASSETS}); JR2025 still missing; sister gap {GAP}"
        )
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AGB Bornem (omzet empty / debt 20.50m / JR2025)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AGB Bornem — KBO **0877.556.624**  
**recipient:** financien@bornem.be · Hingenesteenweg 13, 2880 Bornem  
**sources:** [JR portal](https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb) · [CW NL](https://www.companyweb.be/nl/0877556624/autonoom-gemeentebedrijf-bornem) · [CW EN](https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0877556624) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0877556624)  
**related:** `gap_bornem_dual_jr2025_ge_ocmw_agb_l5` (GE+OCMW+AGB JR2025 pack)  
**tick:** 2044  
**confidence:** Strong (official statutair+BBC+RvB; CW corroboration)

## Context
- YE **2024** (vaststelling RvB/GR **14.10.2025**): assets **EUR21,871,182** JUMP; equity **EUR1,360,756** JUMP; debt **EUR20,499,767** JUMP; bruto **EUR2,767,146** DROP; pnl **EUR1,379,250** DROP; cash **EUR646,906** DROP; budgettair resultaat **EUR2,764,770**; guaranteed debt (9061) **EUR17,794,002**; omzet(70)/60-61/62 **empty**; FTE **0**.
- Portal still lists JR2024 as latest approved pack; JR2025 not published.
- Preferred residual after this fill: FARO/AIESH/REW if YE2025; else unused DSO/IGS/HVZ/WZC/psych. De Verlosser already mined (tick1742). Do not redo Zorggroep Zusters van Berlaar / Psychogeriatrisch / De Linde / …

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Lokaal bestuur Bornem / AGB Bornem — Hingenesteenweg 13, 2880 Bornem
financien@bornem.be
cc: gemeentebestuur@bornem.be indien relevant
Betreft: Openbaarmaking AGB Bornem — omzet/kosten-split YE2024 + jaarrekening 2025 (KBO 0877.556.624)
Geachte, op grond van het Bestuursdecreet / Decreet Lokaal Bestuur vraag ik:
1. Jaarrekening 2025 AGB Bornem (statutair + BBC) zodra vastgesteld, of bevestiging dat die nog niet is goedgekeurd.
2. Toelichting bij lege codes YE2024: omzet (70), 60/61, bezoldigingen (62) ondanks brutomarge EUR2.767.146.
3. Schuldenmatrix LT-ST + gewaarborgde schulden (code 9061 EUR17.794.002) per kredietgever.
4. Opsplitsing bedrijfsopbrengsten achter brutomarge (huur sport/cultuur, toelagen, overige).
5. Toelichting 0 FTE / outsourcing- of personeelsmodel AGB vs gemeente.
Periode 01.01.2024–31.12.2025. Ref: {GAP} / gap_bornem_dual_jr2025_ge_ocmw_agb_l5
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo AGB Bornem, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), "
    "Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, "
    "PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, "
    "Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, "
    "AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, "
    "Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, "
    "IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, "
    "BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, "
    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, "
    "Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Gravenkasteel, "
    "Armonea, Colisée Belgium, Prinsenhof, Vivalto Home BE, emeis Belgium / ORPEA, De Verlosser. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2045":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC De Verlosser Dilbeek — AGB Bornem YE2024 Strong"
        x["notes"] = (
            "tick2045 AGB Bornem Strong assets JUMP 21.87m debt 20.50m bruto DROP 2.77m pnl DROP 1.38m; FOI ready; "
            "FARO/AIESH/REW YE2024; De Verlosser already mined; next rq_2046; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover AGB Bornem YE2024 Strong official statutair; KBO 0877.556.624; "
            f"assets JUMP {ASSETS} debt JUMP {DEBT} bruto DROP {BRUTO} pnl DROP {PNL}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2046" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2046",
            "title": "leftover dual hole-fill after AGB Bornem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2045 after AGB Bornem YE2024 Strong. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2045 AGB Bornem; next every-10 2050; FARO/AIESH/REW still YE2024",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2045",
        "ticks_completed": "2045",
        "paused": "no",
        "notes": (
            "tick2045 leftover AGB Bornem 0877.556.624 Strong official (assets JUMP 21.87m debt JUMP 20.50m equity JUMP 1.36m "
            "bruto DROP 2.77m pnl DROP 1.38m cash DROP 0.65m budgettair 2.76m FTE 0; omzet empty); "
            "FARO/AIESH/REW YE2024; De Verlosser mined; next rq_2046; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2045 - {UTC} - rq_2045 AGB Bornem (assets JUMP 21.87m / debt 20.50m / Strong)

- Unit: **rq_2045** leftover dual after **rq_2044 WZC De Verlosser Dilbeek**. Prefer cascade: AGB/APB if JR2025 live → FARO if NBB YE2025 → AIESH/REW if YE2025 → unused. Took long-deferred **AGB Bornem** JR2024 (KBO **0877.556.624**; Hingenesteenweg 13 Bornem) — official municipal statutair+BBC+RvB live; JR2025 still unpublished. FARO/AIESH/REW still YE2024-only. De Verlosser already mined (1742 + concurrent 2044 CW). Do not redo De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Official statutair YE2024 — assets **EUR21,871,182** JUMP +11.41%; equity **EUR1,360,756** JUMP +274%; debt **EUR20,499,767** JUMP +6.47%; bruto **EUR2,767,146** DROP −12.50%; pnl **EUR1,379,250** DROP −33.64%; cash **EUR646,906** DROP −24.41%; ebit **EUR1,926,693**; budgettair **EUR2,764,770** (RvB); guaranteed **EUR17,794,002**; omzet/60-61/62 empty; FTE **0**; vaststelling **14.10.2025**. Strong confidence. CW NL+EN+FR Medium corroboration. Strong KBO Actief.
- Wrote: sources (+8); budgets (+7); commitments (+1); leaderboard (+1 pi {PI}); entities (update {ENTITY}); foi + draft {GAP}; rq_2045=done + rq_2046 open; loop_state ticks=2045; raw under docs/doge/data/raw/tick2045/.
- FOI: **ready not sent** (human-gated; financien@bornem.be). Sister gap_bornem_dual_jr2025 still ready.
- NOT every-10 (**next every-10 is 2050**). Next: rq_2046 (FARO-if-YE2025 / AIESH-REW-if-YE2025 / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2045 AGB Bornem", ASSETS, "pi", PI)
