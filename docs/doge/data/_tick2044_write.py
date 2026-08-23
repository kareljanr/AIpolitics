# ephemeral tick2044 — WZC De Verlosser Dilbeek YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T15:40:00Z"
ENTITY = "vzw_wzc_de_verlosser_dilbeek"
GAP = "gap_wzc_de_verlosser_dilbeek_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_wzc_de_verlosser_dilbeek_jr2025_cw"
SRC_EN = "src_wzc_de_verlosser_dilbeek_jr2025_cw_en"
SRC_FR = "src_wzc_de_verlosser_dilbeek_jr2025_cw_fr"
SRC_KBO = "src_wzc_de_verlosser_dilbeek_kbo_2044"
SRC_SITE = "src_wzc_de_verlosser_dilbeek_site_2044"

OMZET = "3015833"
PNL = "94194"
EQUITY = "1690969"
BRUTO = "2248348"
FTE = "31"
OMZET24 = "2809593"
PNL24 = "65092"
EQUITY24 = "1599176"
BRUTO24 = "2327248"
# pi = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 1.925 + 1.75 + 0.6 = 4.275 → 4.3
PI = "4.3"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2044")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC De Verlosser Dilbeek YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0446340946/woonzorgcentrum-de-verlosser",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2044; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 19.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2044/verlosser_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC De Verlosser Dilbeek YE2025 statutory",
        "url": "https://www.companyweb.be/en/0446340946/woonzorgcentrum-de-verlosser",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2044; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; FTE 31; raw docs/doge/data/raw/tick2044/verlosser_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC De Verlosser Dilbeek YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0446340946/woonzorgcentrum-de-verlosser",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2044; FR mirror YE2025 Medium; déposés le 19-06-2026; raw docs/doge/data/raw/tick2044/verlosser_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum De Verlosser 0446.340.946 Actief VZW Dilbeek",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0446340946",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2044; Actief VZW; Brusselstraat 647 1700 Dilbeek; 1 VE; KBO email empty; NACE RVT 87.101",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzcdeverlosser.be WZC De Verlosser Dilbeek",
        "url": "https://www.wzcdeverlosser.be/",
        "publisher": "WZC De Verlosser",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2044; info@wzcdeverlosser.be; Brusselstraat 647 1700 Sint-Ulriks-Kapelle (Dilbeek); raw docs/doge/data/raw/tick2044/verlosser_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_de_verlosser_dilbeek_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2044; omzet JUMP {OMZET} +7.34pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_de_verlosser_dilbeek_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2044; pnl JUMP {PNL} +44.71pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_de_verlosser_dilbeek_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2044; equity JUMP {EQUITY} +5.74pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_de_verlosser_dilbeek_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2044; bruto DROP {BRUTO} -3.39pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_de_verlosser_dilbeek_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": "tick2044; YE2025 FTE 31 (YE2024 29.6)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_de_verlosser_dilbeek_jr2025_statutory",
    "title": "WZC De Verlosser Dilbeek YE2025 leftover dual (omzet JUMP 3.02m / pnl JUMP 94k)",
    "entity_id": ENTITY,
    "beneficiary": "Dilbeek / Sint-Ulriks-Kapelle WZC residents (~56 beds)",
    "legal_basis": "VZW WZC operator (KBO 0446.340.946)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0446340946/woonzorgcentrum-de-verlosser",
    "stated_goal": "Kleinschalig VL woonzorgcentrum Dilbeek (kasteeldomein Sint-Ulriks-Kapelle)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl JUMP +44.7pct with bruto DROP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Dilbeek>WZCDeVerlosser>JR2025_statutory_L5",
    "notes": "tick2044; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_de_verlosser_dilbeek_omzet_jump_3_02m_pnl_jump_jr2025",
    "name": "WZC De Verlosser Dilbeek omzet JUMP 3.02m / pnl JUMP 94k (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Dilbeek>WZCDeVerlosser>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Dilbeek Sint-Ulriks-Kapelle elderly-care residents (~56 beds)",
    "stated_goal": "Kleinschalig VL woonzorgcentrum",
    "measured_outcome": "Medium CW YE2025; 3.02m omzet JUMP +7.34pct with pnl JUMP +44.71pct and bruto DROP -3.39pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs; explain pnl JUMP vs bruto DROP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2044 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum De Verlosser (Dilbeek)",
    "name_fr": "Maison de repos De Verlosser (Dilbeek)",
    "name_en": "WZC De Verlosser Dilbeek (elderly care)",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.wzcdeverlosser.be/",
    "foi_email": "info@wzcdeverlosser.be",
    "foi_postal": "Brusselstraat 647, 1700 Dilbeek",
    "notes": (
        "tick2044 YE2025 Medium CW NL+EN+FR + Strong KBO 0446.340.946 Actief VZW; omzet JUMP 3.02m pnl JUMP 94k equity JUMP 1.69m bruto DROP 2.25m FTE 31; "
        "assets/debt Unknown; neerlegging 19.06.2026; 1 VE; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Zorggroep Zusters van Berlaar/Psychogeriatrisch Centrum/WZC De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/Sint-Barbara"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Dilbeek>WZCDeVerlosser>NBB_PDF_assets_debt_pnl_jump_matrix",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; toelichting pnl JUMP +44.71pct with bruto DROP -3.39pct",
    "why_it_matters": "Medium CW shows 3.02m omzet VL WZC VZW with sharp pnl JUMP and bruto DROP without balance sheet or euro subsidy matrix",
    "priority": "8",
    "recipient_body": "Woonzorgcentrum De Verlosser VZW",
    "recipient_email": "info@wzcdeverlosser.be",
    "recipient_postal": "Brusselstraat 647, 1700 Dilbeek",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_de_verlosser_dilbeek_jr2025_statutory",
    "linked_leaderboard_id": "lb_wzc_de_verlosser_dilbeek_omzet_jump_3_02m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2044; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC De Verlosser Dilbeek (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum De Verlosser vzw — KBO **0446.340.946**  
**recipient:** info@wzcdeverlosser.be · Brusselstraat 647, 1700 Dilbeek  
**sources:** [CW NL](https://www.companyweb.be/nl/0446340946/woonzorgcentrum-de-verlosser) · [CW EN](https://www.companyweb.be/en/0446340946/woonzorgcentrum-de-verlosser) · [CW FR](https://www.companyweb.be/fr/0446340946/woonzorgcentrum-de-verlosser) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0446340946) · [site](https://www.wzcdeverlosser.be/)  
**tick:** 2044  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **19.06.2026**): omzet **EUR3,015,833** JUMP +7.34%; pnl **EUR94,194** JUMP +44.71%; equity **EUR1,690,969** JUMP +5.74%; bruto **EUR2,248,348** DROP −3.39%; FTE **31**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024; AIESH/REW YE2024. Zorggroep Zusters van Berlaar already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum De Verlosser vzw — Brusselstraat 647, 1700 Dilbeek
info@wzcdeverlosser.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC De Verlosser + balans (KBO 0446.340.946)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 19.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl JUMP (+44,71pct) bij bruto DROP (−3,39pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, "
    "Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
    "PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
    "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, "
    "Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, "
    "AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, "
    "Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
    "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
    "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, "
    "INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, "
    "Gravenkasteel, Armonea, Colisée Belgium, Prinsenhof, Vivalto Home BE, emeis Belgium / ORPEA. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2044":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Zorggroep Zusters van Berlaar — WZC De Verlosser Dilbeek YE2025 Medium"
        x["notes"] = (
            "tick2044 WZC De Verlosser Dilbeek Medium omzet JUMP 3.02m pnl JUMP 94k (+44.7pct) equity JUMP 1.69m bruto DROP 2.25m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2045; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover WZC De Verlosser Dilbeek YE2025 Medium CW; KBO 0446.340.946; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2045" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2045",
            "title": "leftover dual hole-fill after WZC De Verlosser Dilbeek",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2044 after WZC De Verlosser Dilbeek YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2044 WZC De Verlosser Dilbeek; next every-10 2050",
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
        "last_unit_id": "rq_2044",
        "ticks_completed": "2044",
        "paused": "no",
        "notes": (
            "tick2044 leftover WZC De Verlosser Dilbeek 0446.340.946 Medium CW (omzet JUMP 3.02m pnl JUMP 94k +44.7pct equity JUMP 1.69m bruto DROP 2.25m FTE 31; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2045; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2044 - {UTC} - rq_2044 WZC De Verlosser Dilbeek (omzet JUMP 3.02m / pnl JUMP 94k / Medium)

- Unit: **rq_2044** leftover dual after **rq_2043 Zorggroep Zusters van Berlaar**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024); AIESH/REW still YE2024. Took deferred leftover **WZC De Verlosser Dilbeek** YE2025 (KBO **0446.340.946**; Brusselstraat 647 Dilbeek / Sint-Ulriks-Kapelle; VZW WZC / 1 VE / ~56 beds). Do not redo Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR3,015,833** JUMP +7.34%; pnl **EUR94,194** JUMP +44.71%; equity **EUR1,690,969** JUMP +5.74%; bruto **EUR2,248,348** DROP −3.39%; FTE **31**; neerlegging **19.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; site email info@wzcdeverlosser.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2044=done + rq_2045 open; loop_state ticks=2044; raw under docs/doge/data/raw/tick2044/.
- FOI: **ready not sent** (human-gated; info@wzcdeverlosser.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2045 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2044 WZC De Verlosser Dilbeek", OMZET, "pi", PI)
