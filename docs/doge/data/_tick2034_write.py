# ephemeral tick2034 — WZC Sint-Bernardus Assenede YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T13:10:00Z"
ENTITY = "vzw_wzc_sint_bernardus_assenede"
GAP = "gap_wzc_sint_bernardus_assenede_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
SRC = "src_wzc_sint_bernardus_assenede_jr2025_cw"
SRC_EN = "src_wzc_sint_bernardus_assenede_jr2025_cw_en"
SRC_FR = "src_wzc_sint_bernardus_assenede_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_bernardus_assenede_kbo_2034"
SRC_SITE = "src_wzc_sint_bernardus_assenede_site_2034"

OMZET = "6364855"
PNL = "-231428"
EQUITY = "4618453"
BRUTO = "7009955"
FTE = "85.6"
OMZET24 = "6027796"
PNL24 = "-581751"
EQUITY24 = "5134111"
BRUTO24 = "6479412"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2034")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Bernardus Assenede YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0445106274/wzc-sint-bernardus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2034; YE2025 omzet JUMP {OMZET} pnl LOSS IMPROVED {PNL} (vs YE2024 LOSS {PNL24}) equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 24.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2034/bernardus_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Bernardus Assenede YE2025 statutory",
        "url": "https://www.companyweb.be/en/0445106274/wzc-sint-bernardus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2034; EN mirror YE2025 Medium; filed 24-07-2026; Last balance sheet year 2025; FTE 85.6; raw docs/doge/data/raw/tick2034/bernardus_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Bernardus Assenede YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0445106274/wzc-sint-bernardus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2034; FR mirror YE2025 Medium; déposés le 24-07-2026; raw docs/doge/data/raw/tick2034/bernardus_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Sint-Bernardus 0445.106.274 Actief VZW Assenede",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445106274",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2034; Actief VZW; Assenedestraat 18 9968 Assenede (Bassevelde); 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzcsintbernardus.be WZC Sint-Bernardus Bassevelde",
        "url": "https://www.wzcsintbernardus.be/",
        "publisher": "WZC Sint-Bernardus",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2034; info@wzcsintbernardus.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_bernardus_assenede_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2034; omzet JUMP {OMZET} +5.59pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_bernardus_assenede_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2034; pnl LOSS IMPROVED {PNL} vs YE2024 LOSS {PNL24} (+60.22pct less loss)",
    },
    {
        "budget_id": "bud_wzc_sint_bernardus_assenede_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2034; equity DROP {EQUITY} -10.04pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_bernardus_assenede_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2034; bruto JUMP {BRUTO} +8.19pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_bernardus_assenede_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2034; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_bernardus_assenede_jr2025_statutory_wzc",
    "title": "WZC Sint-Bernardus Assenede YE2025 leftover dual (omzet JUMP 6.36m / pnl LOSS IMPROVED -0.23m / equity DROP 4.62m)",
    "entity_id": ENTITY,
    "beneficiary": "Assenede/Bassevelde elderly care residents / WZC Sint-Bernardus",
    "legal_basis": "VZW/ASBL WZC (KBO 0445.106.274)",
    "decision_date": "2026-07-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0445106274/wzc-sint-bernardus",
    "stated_goal": "Residential elderly care (Assenede/Bassevelde)",
    "cut_option": "Publish NBB PDF assets/debt FOI; scrutinise continued LOSS + equity DROP",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>WZC_Sint_Bernardus_Assenede>JR2025_statutory_L5",
    "notes": "tick2034; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Cassiers already mined; Curando fusion press context not euro-invented",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.5 + 0.10*(10-4) = 1.925 + 1.925 + 0.6 = 4.45 (LOSS bump absurdity)
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_bernardus_assenede_omzet_jump_6_36m_pnl_loss_improved_jr2025",
    "name": "WZC Sint-Bernardus Assenede omzet JUMP 6.36m / pnl LOSS IMPROVED -0.23m / equity DROP 4.62m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "OostVlaanderen>WZC_Sint_Bernardus_Assenede>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS IMPROVED {PNL} (vs LOSS {PNL24}) equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Assenede/Bassevelde elderly via WZC Sint-Bernardus VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 6.36m omzet JUMP +5.59pct with continued LOSS improved vs YE2024 and equity DROP -10.04pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.45",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; scrutinise LOSS path + equity DROP + Curando fusion euros",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2034 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Sint-Bernardus (Assenede/Bassevelde)",
    "name_fr": "Maison de repos Sint-Bernardus (Assenede)",
    "name_en": "WZC Sint-Bernardus Assenede (elderly care)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.wzcsintbernardus.be/",
    "foi_email": "info@wzcsintbernardus.be",
    "foi_postal": "Assenedestraat 18, 9968 Assenede",
    "notes": "tick2034 YE2025 Medium CW NL+EN+FR + Strong KBO 0445.106.274 Actief VZW; omzet JUMP 6.36m pnl LOSS IMPROVED -0.23m equity DROP 4.62m bruto JUMP 7.01m FTE 85.6; assets/debt Unknown; neerlegging 24.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "OostVlaanderen>WZC_Sint_Bernardus_Assenede>NBB_PDF_assets_debt_pnl_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; LOSS + equity DROP recon; Curando fusion euros if material",
    "why_it_matters": "Medium CW shows 6.36m omzet Assenede WZC VZW with continued LOSS and equity DROP without balance sheet",
    "priority": "6",
    "recipient_body": "WZC Sint-Bernardus vzw",
    "recipient_email": "info@wzcsintbernardus.be",
    "recipient_postal": "Assenedestraat 18, 9968 Assenede",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_bernardus_assenede_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_sint_bernardus_assenede_omzet_jump_6_36m_pnl_loss_improved_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2034; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Bernardus Assenede (NBB PDF / assets-debt / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC Sint-Bernardus vzw — KBO **0445.106.274**  
**recipient:** info@wzcsintbernardus.be · Assenedestraat 18, 9968 Assenede  
**sources:** [CW NL](https://www.companyweb.be/nl/0445106274/wzc-sint-bernardus) · [CW EN](https://www.companyweb.be/en/0445106274/wzc-sint-bernardus) · [CW FR](https://www.companyweb.be/fr/0445106274/wzc-sint-bernardus) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445106274) · [site](https://www.wzcsintbernardus.be/)  
**tick:** 2034  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.07.2026**): omzet **EUR6,364,855** JUMP +5.59%; pnl **LOSS EUR−231,428** IMPROVED vs YE2024 LOSS EUR−581,751; equity **EUR4,618,453** DROP −10.04%; bruto **EUR7,009,955** JUMP +8.19%; FTE **85.6**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Cassiers already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC Sint-Bernardus vzw — Assenedestraat 18, 9968 Assenede
info@wzcsintbernardus.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Bernardus Assenede + balans (KBO 0445.106.274)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting continued LOSS + equity DROP (−10,04pct); Curando-fusie-euros indien materieel.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2034":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Cassiers — WZC Sint-Bernardus Assenede YE2025 Medium"
        x["notes"] = (
            "tick2034 WZC Sint-Bernardus Assenede Medium omzet JUMP 6.36m pnl LOSS IMPROVED -0.23m equity DROP 4.62m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2035; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover WZC Sint-Bernardus Assenede YE2025 Medium CW; KBO 0445.106.274; "
            f"omzet JUMP {OMZET} pnl LOSS IMPROVED {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2035" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2035",
            "title": "leftover dual hole-fill after WZC Sint-Bernardus Assenede",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2034 after WZC Sint-Bernardus Assenede YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (OLV Roosdaal YE2025 live deferred / OLVA Antwerpen YE2025 / Kanunnik Triest YE2025 / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2034 WZC Sint-Bernardus Assenede; next every-10 2040; Roosdaal/OLVA/Triest YE2025 deferred",
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
        "last_unit_id": "rq_2034",
        "ticks_completed": "2034",
        "paused": "no",
        "notes": (
            "tick2034 leftover WZC Sint-Bernardus Assenede 0445.106.274 Medium CW (omzet JUMP 6.36m pnl LOSS IMPROVED -0.23m equity DROP 4.62m bruto JUMP 7.01m FTE 85.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2035; next every-10 2040; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2034 - {UTC} - rq_2034 WZC Sint-Bernardus Assenede (omzet JUMP 6.36m / pnl LOSS IMPROVED -0.23m / Medium)

- Unit: **rq_2034** leftover dual after **rq_2033 Cassiers**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC Sint-Bernardus Assenede** YE2025 (KBO **0445.106.274**; Assenedestraat 18 Bassevelde; Oost-Vlaanderen **WZC VZW**). Do not redo Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR6,364,855** JUMP +5.59%; pnl **LOSS EUR−231,428** IMPROVED vs YE2024 LOSS EUR−581,751; equity **EUR4,618,453** DROP −10.04%; bruto **EUR7,009,955** JUMP +8.19%; FTE **85.6**; neerlegging **24.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@wzcsintbernardus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_bernardus_assenede); foi + draft {GAP}; rq_2034=done + rq_2035 open; loop_state ticks=2034; raw under docs/doge/data/raw/tick2034/.
- FOI: **ready not sent** (human-gated; info@wzcsintbernardus.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2035 (AGB/FARO-if-YE2025 / AIESH-REW / Roosdaal-OLVA-Triest / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
