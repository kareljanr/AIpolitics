# ephemeral tick2027 — WZC Sint-Carolus Ternat YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T11:25:00Z"
ENTITY = "vzw_wzc_sint_carolus_ternat"
GAP = "gap_wzc_sint_carolus_ternat_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_wzc_sint_carolus_ternat_jr2025_cw"
SRC_EN = "src_wzc_sint_carolus_ternat_jr2025_cw_en"
SRC_FR = "src_wzc_sint_carolus_ternat_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_carolus_ternat_kbo_2025"
SRC_SITE = "src_wzc_sint_carolus_ternat_site_2025"

OMZET = "10159951"
PNL = "849928"
EQUITY = "9301970"
BRUTO = "9564169"
FTE = "106.3"
OMZET24 = "9664479"
PNL24 = "534849"
EQUITY24 = "8454658"
BRUTO24 = "9148221"
FTE24 = "108.6"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2027")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Woonzorgcentrum Sint-Carolus Ternat YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0409970203/woonzorgcentrum-sint-carolus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2027; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2027/ternat_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Woonzorgcentrum Sint-Carolus Ternat YE2025 statutory",
        "url": "https://www.companyweb.be/en/0409970203/woonzorgcentrum-sint-carolus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2027; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; FTE 106.3; raw docs/doge/data/raw/tick2027/ternat_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Woonzorgcentrum Sint-Carolus Ternat YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0409970203/woonzorgcentrum-sint-carolus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2027; FR mirror YE2025 Medium; déposés le 02-07-2026; raw docs/doge/data/raw/tick2027/ternat_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum Sint-Carolus Ternat 0409.970.203 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409970203",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2027; Actief VZW; Meersstraat 1 1742 Ternat; 1 VE; sinds 10.01.1931; raw docs/doge/data/raw/tick2027/kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "sintcarolus.be WZC Sint-Carolus Ternat (Solidum Groep)",
        "url": "https://www.sintcarolus.be/",
        "publisher": "WZC Sint-Carolus Ternat",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2027; wzc@sintcarolus.be; +32 2 454 18 00; Meersstraat 1 Ternat; Solidum Groep; directeur Sylvia Gribbe",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_carolus_ternat_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2027; omzet JUMP {OMZET} +5.13pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_carolus_ternat_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2027; pnl JUMP {PNL} +58.91pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_sint_carolus_ternat_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2027; equity JUMP {EQUITY} +10.02pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_carolus_ternat_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2027; bruto JUMP {BRUTO} +4.55pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_carolus_ternat_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2027; YE2025 FTE {FTE} vs YE2024 {FTE24}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_carolus_ternat_jr2025_statutory",
    "title": "WZC Sint-Carolus Ternat YE2025 leftover dual (omzet JUMP 10.16m / pnl JUMP 0.85m / equity JUMP 9.30m)",
    "entity_id": ENTITY,
    "beneficiary": "Ternat elderly residents via Woonzorgcentrum Sint-Carolus VZW (Solidum Groep)",
    "legal_basis": "VZW/ASBL woonzorgcentrum (KBO 0409.970.203)",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0409970203/woonzorgcentrum-sint-carolus",
    "stated_goal": "Residential elderly care / WZC Ternat",
    "cut_option": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>Ternat>WZC_Sint_Carolus>JR2025_statutory_L5",
    "notes": "tick2027; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; deferred from tick2026",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.0 + 0.35*5.0 + 0.10*(10-4) = 2.75 + 1.75 + 0.6 = 5.1
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_carolus_ternat_omzet_jump_10_16m_pnl_jump_0_85m_jr2025",
    "name": "WZC Sint-Carolus Ternat omzet JUMP 10.16m / pnl JUMP 0.85m (+59pct) / equity JUMP 9.30m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>Ternat>WZC_Sint_Carolus>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Ternat elderly via WZC Sint-Carolus VZW (Solidum)",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 10.16m omzet JUMP +5.13pct with pnl JUMP +58.91pct and equity JUMP +10.02pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.1",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidy vs resident-fee mix",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2027 leftover WZC dual (deferred tick2026); Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Sint-Carolus (Ternat)",
    "name_fr": "Woonzorgcentrum Sint-Carolus (maison de repos Ternat)",
    "name_en": "Woonzorgcentrum Sint-Carolus (nursing home Ternat)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.sintcarolus.be/",
    "foi_email": "wzc@sintcarolus.be",
    "foi_postal": "Meersstraat 1, 1742 Ternat",
    "notes": "tick2027 YE2025 Medium CW NL+EN+FR + Strong KBO 0409.970.203 Actief VZW; omzet JUMP 10.16m pnl JUMP 0.85m (+58.91pct) equity JUMP 9.30m bruto JUMP 9.56m FTE 106.3; assets/debt Unknown; neerlegging 02.07.2026; 1 VE; Solidum Groep; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo WZC Zilverbos/Sint Carolus Mayerhof/Evara/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "VlaamsBrabant>Ternat>WZC_Sint_Carolus>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl JUMP +58.91pct recon vs omzet +5.13pct",
    "why_it_matters": "Medium CW shows 10.16m omzet WZC with strong pnl/equity JUMP without balance sheet or public/private revenue mix",
    "priority": "7",
    "recipient_body": "Woonzorgcentrum Sint-Carolus VZW Ternat",
    "recipient_email": "wzc@sintcarolus.be",
    "recipient_postal": "Meersstraat 1, 1742 Ternat",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_carolus_ternat_jr2025_statutory",
    "linked_leaderboard_id": "lb_wzc_sint_carolus_ternat_omzet_jump_10_16m_pnl_jump_0_85m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2027; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Carolus Ternat (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Sint-Carolus VZW Ternat — KBO **0409.970.203**  
**recipient:** wzc@sintcarolus.be · Meersstraat 1, 1742 Ternat  
**sources:** [CW NL](https://www.companyweb.be/nl/0409970203/woonzorgcentrum-sint-carolus) · [CW EN](https://www.companyweb.be/en/0409970203/woonzorgcentrum-sint-carolus) · [CW FR](https://www.companyweb.be/fr/0409970203/woonzorgcentrum-sint-carolus) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409970203) · [sintcarolus.be](https://www.sintcarolus.be/)  
**tick:** 2027  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.07.2026**): omzet **EUR10,159,951** JUMP +5.13%; pnl **EUR849,928** JUMP +58.91%; equity **EUR9,301,970** JUMP +10.02%; bruto **EUR9,564,169** JUMP +4.55%; FTE **106.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred from tick2026 after WZC Zilverbos.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Sint-Carolus VZW — Meersstraat 1, 1742 Ternat
wzc@sintcarolus.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Carolus Ternat (KBO 0409.970.203)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs bewonersbijdragen 2025.
4. Toelichting pnl JUMP (+58,91pct) t.o.v. omzet JUMP (+5,13pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2027":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Zilverbos — WZC Sint-Carolus Ternat YE2025 Medium"
        x["notes"] = (
            "tick2027 WZC Sint-Carolus Ternat Medium omzet JUMP 10.16m pnl JUMP 0.85m (+58.91pct) equity JUMP 9.30m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2028; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover WZC Sint-Carolus Ternat YE2025 Medium CW; KBO 0409.970.203; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2028" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2028",
            "title": "leftover dual hole-fill after WZC Sint-Carolus Ternat",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2027 after WZC Sint-Carolus Ternat YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (other unused YE2025 if live with omzet). "
                "Do NOT redo WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara/Multiversum, Maria Rustoord Ingelmunster, PPC Pittem, "
                "WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
                "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, "
                "Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, "
                "Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, "
                "IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, "
                "IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
                "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, "
                "SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/"
                "Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2027 WZC Sint-Carolus Ternat; next every-10 2030",
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
        x["last_unit_id"] = "rq_2027"
        x["ticks_completed"] = "2027"
        x["paused"] = "no"
        x["notes"] = (
            "tick2027 leftover WZC Sint-Carolus Ternat 0409.970.203 Medium CW (omzet JUMP 10.16m pnl JUMP 0.85m +58.91pct "
            "equity JUMP 9.30m bruto JUMP 9.56m FTE 106.3; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2028; next every-10 2030; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2027 - {UTC} - rq_2027 WZC Sint-Carolus Ternat (omzet JUMP 10.16m / pnl JUMP 0.85m / Medium)

- Unit: **rq_2027** leftover dual after **rq_2026 WZC Zilverbos**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC Sint-Carolus Ternat** YE2025 (KBO **0409.970.203**; Meersstraat 1 Ternat; Vlaams-Brabant **WZC VZW** / Solidum Groep). Distinct from Mortsel Sint Carolus Mayerhof. Do not redo Zilverbos/Sint Carolus Mayerhof/Evara/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR10,159,951** JUMP +5.13%; pnl **EUR849,928** JUMP +58.91%; equity **EUR9,301,970** JUMP +10.02%; bruto **EUR9,564,169** JUMP +4.55%; FTE **106.3**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email wzc@sintcarolus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_carolus_ternat); foi + draft gap_wzc_sint_carolus_ternat_nbb_pdf_assets_debt_pnl_jump_matrix_l5; rq_2027=done + rq_2028 open; loop_state ticks=2027; raw under docs/doge/data/raw/tick2027/.
- FOI: **ready not sent** (human-gated; wzc@sintcarolus.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2028 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital-psych-WZC).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2027")
