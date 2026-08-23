# ephemeral tick2031 — Cassiers WZC Houthulst YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T12:40:00Z"
ENTITY = "vzw_wzc_cassiers"
GAP = "gap_wzc_cassiers_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_wzc_cassiers_jr2025_cw"
SRC_EN = "src_wzc_cassiers_jr2025_cw_en"
SRC_FR = "src_wzc_cassiers_jr2025_cw_fr"
SRC_KBO = "src_wzc_cassiers_kbo_2025"
SRC_SITE = "src_wzc_cassiers_site_2025"

OMZET = "7196773"
PNL = "424127"
EQUITY = "9741670"
BRUTO = "7762773"
FTE = "97.7"
OMZET24 = "7062796"
PNL24 = "586537"
EQUITY24 = "8847256"
BRUTO24 = "7767769"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2031")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

for x in qrows:
    if x.get("task_id") == "rq_2031":
        x["status"] = "in_progress"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
save("docs/doge/data/research_queue.csv", qrows, qfields)

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Cassiers WZC Houthulst YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0434434393/cassiers-woon-en-zorgcentrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2031; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto FLAT {BRUTO} FTE {FTE}; neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2031/cassiers_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Cassiers WZC Houthulst YE2025 statutory",
        "url": "https://www.companyweb.be/en/0434434393/cassiers-woon-en-zorgcentrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2031; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; FTE 97.7; raw docs/doge/data/raw/tick2031/cassiers_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Cassiers WZC Houthulst YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0434434393/cassiers-woon-en-zorgcentrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2031; FR mirror YE2025 Medium; déposés le 03-07-2026; raw docs/doge/data/raw/tick2031/cassiers_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Cassiers woon- en zorgcentrum 0434.434.393 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434434393",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2031; Actief VZW since 09.12.1987; 7e-Geniestraat 3 8650 Houthulst; 3 VE; raw docs/doge/data/raw/tick2031/cassiers_kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "cassierswzc.be Cassiers WZC Houthulst",
        "url": "http://www.cassierswzc.be/",
        "publisher": "Cassiers WZC VZW",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2031; info@wzccassiers.be; +32 51 70 81 90; 7e Geniestraat 3 8650 Houthulst",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_cassiers_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2031; omzet JUMP {OMZET} +1.90pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_cassiers_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2031; pnl DROP {PNL} -27.69pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_cassiers_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2031; equity JUMP {EQUITY} +10.11pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_cassiers_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2031; bruto FLAT {BRUTO} -0.06pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_cassiers_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick2031; YE2025 FTE 97.7 vs YE2024 98.2",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_cassiers_jr2025_statutory",
    "title": "Cassiers WZC YE2025 leftover dual (omzet JUMP 7.20m / pnl DROP 0.42m / equity JUMP 9.74m)",
    "entity_id": ENTITY,
    "beneficiary": "Houthulst elderly via Cassiers woon- en zorgcentrum VZW",
    "legal_basis": "VZW/ASBL woonzorgcentrum (KBO 0434.434.393)",
    "decision_date": "2026-07-03",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0434434393/cassiers-woon-en-zorgcentrum",
    "stated_goal": "Residential elderly care / WZC Houthulst",
    "cut_option": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees; recon pnl DROP -27.69pct vs equity JUMP +10.11pct",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>Houthulst>WZC_Cassiers>JR2025_statutory_L5",
    "notes": "tick2031; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Bernardus Assenede/OLV Roosdaal/Lourdes/OLVA/Triest/Vincentius Ant deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# ~7.2m WZC; pnl DROP -27.69pct + equity JUMP +10.11pct → absurdity 5.5; cost 5.0; difficulty 4.0
# priority = 0.55*5.5 + 0.35*5.0 + 0.10*6 = 3.025 + 1.75 + 0.6 = 5.375 ~ 5.4
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_cassiers_omzet_jump_7_20m_pnl_drop_0_42m_jr2025",
    "name": "Cassiers WZC omzet JUMP 7.20m / pnl DROP 0.42m (-27.69pct) / equity JUMP 9.74m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "WestVlaanderen>Houthulst>WZC_Cassiers>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto FLAT {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Houthulst elderly via Cassiers WZC VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.20m omzet JUMP +1.90pct with pnl DROP -27.69pct and equity JUMP +10.11pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.4",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidy vs resident-fee mix; recon pnl DROP vs equity JUMP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2031 leftover WZC dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Cassiers woon- en zorgcentrum (Houthulst)",
    "name_fr": "Cassiers centre de soins et de logement (Houthulst)",
    "name_en": "Cassiers nursing home (Houthulst)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "http://www.cassierswzc.be/",
    "foi_email": "info@wzccassiers.be",
    "foi_postal": "7e-Geniestraat 3, 8650 Houthulst",
    "notes": "tick2031 YE2025 Medium CW NL+EN+FR + Strong KBO 0434.434.393 Actief VZW; omzet JUMP 7.20m pnl DROP 0.42m (-27.69pct) equity JUMP 9.74m (+10.11pct) bruto FLAT 7.76m FTE 97.7; assets/debt Unknown; neerlegging 03.07.2026; 3 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo WZC Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara",
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
    "hierarchy_path": "WestVlaanderen>Houthulst>WZC_Cassiers>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl DROP -27.69pct recon vs equity JUMP +10.11pct",
    "why_it_matters": "Medium CW shows 7.20m omzet WZC with pnl DROP and equity JUMP without balance sheet or public/private revenue mix",
    "priority": "7",
    "recipient_body": "Cassiers woon- en zorgcentrum VZW",
    "recipient_email": "info@wzccassiers.be",
    "recipient_postal": "7e-Geniestraat 3, 8650 Houthulst",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_cassiers_jr2025_statutory",
    "linked_leaderboard_id": "lb_wzc_cassiers_omzet_jump_7_20m_pnl_drop_0_42m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2031; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Cassiers WZC Houthulst (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Cassiers woon- en zorgcentrum VZW — KBO **0434.434.393**  
**recipient:** info@wzccassiers.be · 7e-Geniestraat 3, 8650 Houthulst  
**sources:** [CW NL](https://www.companyweb.be/nl/0434434393/cassiers-woon-en-zorgcentrum) · [CW EN](https://www.companyweb.be/en/0434434393/cassiers-woon-en-zorgcentrum) · [CW FR](https://www.companyweb.be/fr/0434434393/cassiers-woon-en-zorgcentrum) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434434393) · [cassierswzc.be](http://www.cassierswzc.be/)  
**tick:** 2031  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **03.07.2026**): omzet **EUR7,196,773** JUMP +1.90%; pnl **EUR424,127** DROP -27.69%; equity **EUR9,741,670** JUMP +10.11%; bruto **EUR7,762,773** FLAT -0.06%; FTE **97.7**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Bernardus Assenede / OLV Roosdaal / Lourdes / OLVA / Triest / Vincentius Ant YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Cassiers woon- en zorgcentrum VZW — 7e-Geniestraat 3, 8650 Houthulst
info@wzccassiers.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 Cassiers WZC (KBO 0434.434.393)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 03.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs bewonersbijdragen 2025.
4. Toelichting pnl DROP (-27,69pct) t.o.v. equity JUMP (+10,11pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

skip_list = (
    "Do NOT redo Cassiers WZC, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, "
    "Sint Carolus Mayerhof, Evara/Multiversum, Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
    "PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, Veilige Have, Zusterhof, Bethanie Zoersel (Emmaüs double-count), "
    "AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, "
    "Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, "
    "Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS. "
    "Jessa/ZOL/Vesalius CW N/A omzet — take only if figures appear."
)

qrows, qfields = load("docs/doge/data/research_queue.csv")
for x in qrows:
    if x.get("task_id") == "rq_2031":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Sint-Jozef Rillaar — Cassiers WZC YE2025 Medium"
        x["notes"] = (
            "tick2031 Cassiers Medium omzet JUMP 7.20m pnl DROP 0.42m (-27.69pct) equity JUMP 9.74m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2032; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover Cassiers WZC YE2025 Medium CW; KBO 0434.434.393; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto FLAT {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2032" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2032",
            "title": "leftover dual hole-fill after Cassiers WZC",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2031 after Cassiers WZC YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Sint-Bernardus Assenede YE2025 live deferred / OLV Roosdaal YE2025 / Lourdes Kortenberg YE2025 / OLVA Antwerpen YE2025 / "
                "Kanunnik Triest YE2025 / WZC St Vincentius Antwerpen-Ekeren YE2025 / other unused YE2025 if live with omzet). "
                + skip_list
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2031 Cassiers; next every-10 2040",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue updated")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for x in srows2:
    if x.get("state_id") == "main":
        x["mode"] = "continuous"
        x["current_sprint"] = "hole_fill"
        x["last_tick_utc"] = UTC
        x["last_unit_id"] = "rq_2031"
        x["ticks_completed"] = "2031"
        x["paused"] = "no"
        x["notes"] = (
            "tick2031 leftover Cassiers WZC 0434.434.393 Medium CW (omzet JUMP 7.20m pnl DROP 0.42m -27.69pct "
            "equity JUMP 9.74m bruto FLAT 7.76m FTE 97.7; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2032; next every-10 2040; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2031 - {UTC} - rq_2031 Cassiers WZC (omzet JUMP 7.20m / pnl DROP 0.42m / Medium)

- Unit: **rq_2031** leftover dual after **rq_2030 EVERY-10 + WZC Sint-Jozef Rillaar**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred unused leftover **Cassiers WZC Houthulst** YE2025 (KBO **0434.434.393**; 7e-Geniestraat 3 Houthulst; West-Vlaanderen **WZC VZW**). Sint-Bernardus Assenede / OLV Roosdaal / Lourdes / OLVA / Triest / Vincentius Antwerpen YE2025 also live — deferred. Do not redo Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,196,773** JUMP +1.90%; pnl **EUR424,127** DROP -27.69%; equity **EUR9,741,670** JUMP +10.11%; bruto **EUR7,762,773** FLAT -0.06%; FTE **97.7**; neerlegging **03.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email info@wzccassiers.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_cassiers); foi + draft gap_wzc_cassiers_nbb_pdf_assets_debt_pnl_drop_matrix_l5; rq_2031=done + rq_2032 open; loop_state ticks=2031; raw under docs/doge/data/raw/tick2031/.
- FOI: **ready not sent** (human-gated; info@wzccassiers.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2032 (AGB/FARO-if-YE2025 / AIESH-REW / Bernardus Assenede-OLV Roosdaal-Lourdes-OLVA-Triest-Vincentius Ant / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2031")
