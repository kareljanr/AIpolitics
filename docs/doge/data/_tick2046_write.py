# ephemeral tick2046 — Curando YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T16:40:00Z"
ENTITY = "vzw_curando"
GAP = "gap_curando_nbb_pdf_assets_debt_subsidy_matrix_l5"
SRC = "src_curando_jr2025_cw"
SRC_EN = "src_curando_jr2025_cw_en"
SRC_FR = "src_curando_jr2025_cw_fr"
SRC_KBO = "src_curando_kbo_2046"
SRC_SITE = "src_curando_site_2046"

OMZET = "87690207"
PNL = "2863387"
EQUITY = "63483907"
BRUTO = "91460512"
FTE = "1107"
OMZET24 = "82845080"
PNL24 = "3089557"
EQUITY24 = "61690655"
BRUTO24 = "86668126"
# pi = 0.55*6.7 + 0.35*5.5 + 0.10*(10-4) = 3.685 + 1.925 + 0.6 = 6.21 → 6.2
PI = "6.2"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2046")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CURANDO (O.L.V. van 7 Weeen Ruiselede) YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0445499422/curando",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2046; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 15.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2045/curando_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CURANDO YE2025 statutory",
        "url": "https://www.companyweb.be/en/0445499422/curando",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2046; EN mirror YE2025 Medium; filed 15-07-2026; Last balance sheet year 2025; FTE 1.107 (=1107); raw docs/doge/data/raw/tick2045/curando_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR CURANDO YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0445499422/curando",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2046; FR mirror YE2025 Medium; depose le 15-07-2026; raw docs/doge/data/raw/tick2045/curando_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CURANDO 0445.499.422 Actief VZW aanbestedende overheid Wingene",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445499422",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2046; Actief VZW; Zuster Filiepstraat 3 8755 Wingene (since 30.06.2026); 27 VE; aanbestedende overheid sinds 15.05.1991; NACE 87.101/87.301; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Curando contact (info@curando.be) + WZC/thuiszorg footprint",
        "url": "https://www.curando.be/nl/contact",
        "publisher": "Curando vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2046; Pensionaatstraat 8A 8755 Ruiselede (Wingene); info@curando.be; multi-campus WZC/AW/thuiszorg West-Vlaanderen; raw docs/doge/data/raw/tick2045/curando_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_curando_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2046; omzet JUMP {OMZET} +5.85pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_curando_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2046; pnl DROP {PNL} -7.32pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_curando_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2046; equity JUMP {EQUITY} +2.91pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_curando_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2046; bruto JUMP {BRUTO} +5.53pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_curando_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2046; YE2025 FTE {FTE} (CW displays 1.107 with thousands separator)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_curando_jr2025_statutory_wzc",
    "title": "Curando YE2025 leftover dual (omzet JUMP 87.69m / pnl DROP 2.86m)",
    "entity_id": ENTITY,
    "beneficiary": "VL West-Vlaanderen elderly-care residents (WZC/AW/thuiszorg Curando campuses)",
    "legal_basis": "VZW WZC/thuiszorg operator / aanbestedende overheid (KBO 0445.499.422)",
    "decision_date": "2026-07-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0445499422/curando",
    "stated_goal": "Multi-campus VL woonzorg / thuiszorg / assistentiewoningen (Curando / OLV 7 Weeen Ruiselede)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; scrutinise IFIC/Alivia/Vlaio subsidy stack vs 87.7m omzet",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>Curando>JR2025_statutory_L5",
    "notes": "tick2046; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Integro/Huize Vincent/Hof ter Waarbeek/Ter Kimme YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_curando_omzet_jump_87_69m_pnl_drop_jr2025",
    "name": "Curando omzet JUMP 87.69m / pnl DROP 2.86m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>Curando>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "VL elderly-care residents via Curando multi-campus WZC/AW/thuiszorg",
    "stated_goal": "Multi-campus VL woonzorg / thuiszorg",
    "measured_outcome": "Medium CW YE2025; 87.69m omzet JUMP +5.85pct with pnl DROP -7.32pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.7",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs/IFIC/Alivia stack; explain pnl DROP vs omzet JUMP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2046 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Curando / O.L.V. van 7 Weeen Ruiselede (VZW, multi-campus WZC)",
    "name_fr": "Curando / Notre-Dame des Sept Douleurs Ruiselede (ASBL, MRS multi-sites)",
    "name_en": "Curando (VZW multi-campus nursing homes / home care)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.curando.be/",
    "foi_email": "info@curando.be",
    "foi_postal": "Zuster Filiepstraat 3, 8755 Wingene (ops: Pensionaatstraat 8A, 8755 Ruiselede)",
    "notes": (
        "tick2046 YE2025 Medium CW NL+EN+FR + Strong KBO 0445.499.422 Actief VZW aanbestedende overheid 27 VE; omzet JUMP 87.69m pnl DROP 2.86m equity JUMP 63.48m bruto JUMP 91.46m FTE 1107; "
        "assets/debt Unknown; neerlegging 15.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Integro/Huize Vincent/Hof ter Waarbeek/Ter Kimme YE2025 deferred; do not redo De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hieronymus/Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>Curando>NBB_PDF_assets_debt_subsidy_matrix",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split (IFIC/Alivia/Vlaio/code73); campus-level revenue matrix across 27 VE; related-party notes",
    "why_it_matters": "Medium CW shows 87.69m omzet VL aanbestedende-overheid WZC/thuiszorg VZW with pnl DROP and no balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Curando vzw (O.L.V. van 7 Weeen Ruiselede)",
    "recipient_email": "info@curando.be",
    "recipient_postal": "Zuster Filiepstraat 3, 8755 Wingene / Pensionaatstraat 8A, 8755 Ruiselede",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_curando_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_curando_omzet_jump_87_69m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2046; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Curando (NBB PDF / assets-debt / subsidy matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Curando VZW (O.L.V. van 7 Weeen Ruiselede) — KBO **0445.499.422**  
**recipient:** info@curando.be · Zuster Filiepstraat 3, 8755 Wingene / Pensionaatstraat 8A, 8755 Ruiselede  
**sources:** [CW NL](https://www.companyweb.be/nl/0445499422/curando) · [CW EN](https://www.companyweb.be/en/0445499422/curando) · [CW FR](https://www.companyweb.be/fr/0445499422/curando) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445499422) · [site](https://www.curando.be/nl/contact)  
**tick:** 2046  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **15.07.2026**): omzet **EUR87,690,207** JUMP +5.85%; pnl **EUR2,863,387** DROP −7.32% vs YE2024 EUR3,089,557; equity **EUR63,483,907** JUMP +2.91%; bruto **EUR91,460,512** JUMP +5.53%; FTE **1107**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **27 VE**; zetel Zuster Filiepstraat 3 Wingene; NACE 87.101/87.301.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Integro / Huize Vincent / Hof ter Waarbeek / Ter Kimme YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Curando vzw — Zuster Filiepstraat 3, 8755 Wingene
info@curando.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Curando + subsidiematrix (KBO 0445.499.422)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 15.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen/thuiszorg 2025.
4. Toelichting pnl DROP (van EUR3.089.557 YE2024 naar EUR2.863.387 YE2025) bij omzet JUMP.
5. Niet-confidentieel overzicht omzet/subsidies per campus of VE-groep (27 VE).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Curando, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, "
    "Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
    "PC Sint-Hieronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
    "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, "
    "AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaus, AZORG, "
    "Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, "
    "CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, "
    "SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, "
    "IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
    "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, "
    "IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Gravenkasteel, Armonea, "
    "Colisee Belgium, Prinsenhof, Vivalto Home BE, emeis Belgium / ORPEA. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2046":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AGB Bornem — Curando YE2025 Medium"
        x["notes"] = (
            "tick2046 Curando Medium omzet JUMP 87.69m pnl DROP 2.86m equity JUMP 63.48m bruto JUMP 91.46m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Integro/Huize Vincent/Hof Waarbeek/Ter Kimme deferred; next rq_2047; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover Curando YE2025 Medium CW; KBO 0445.499.422; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2047" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2047",
            "title": "leftover dual hole-fill after Curando",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2046 after Curando YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Integro YE2025 live deferred / Huize Vincent YE2025 / Hof ter Waarbeek YE2025 / Ter Kimme YE2025 / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2046 Curando; next every-10 2050; Integro/Huize Vincent/Hof Waarbeek/Ter Kimme YE2025 deferred",
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
        "last_unit_id": "rq_2046",
        "ticks_completed": "2046",
        "paused": "no",
        "notes": (
            "tick2046 leftover Curando 0445.499.422 Medium CW (omzet JUMP 87.69m pnl DROP 2.86m equity JUMP 63.48m bruto JUMP 91.46m FTE 1107; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Integro/Huize Vincent/Hof Waarbeek/Ter Kimme deferred; next rq_2047; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2046 - {UTC} - rq_2045 Curando (omzet JUMP 87.69m / pnl DROP 2.86m / Medium)

- Unit: **rq_2045** leftover dual after **rq_2045 AGB Bornem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took unused leftover **Curando** YE2025 (KBO **0445.499.422**; Zuster Filiepstraat 3 Wingene / Pensionaatstraat 8A Ruiselede; West-Vlaanderen **aanbestedende-overheid VZW** multi-campus WZC/thuiszorg / **27 VE**). Integro / Huize Vincent / Hof ter Waarbeek / Ter Kimme YE2025 also live — deferred. Do not redo AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR87,690,207** JUMP +5.85%; pnl **EUR2,863,387** DROP −7.32%; equity **EUR63,483,907** JUMP +2.91%; bruto **EUR91,460,512** JUMP +5.53%; FTE **1107**; neerlegging **15.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 27 VE; email info@curando.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2045=done + rq_2047 open; loop_state ticks=2045; raw under docs/doge/data/raw/tick2045/.
- FOI: **ready not sent** (human-gated; info@curando.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2047 (AGB/FARO-if-YE2025 / AIESH-REW / Integro-Huize Vincent-Hof Waarbeek-Ter Kimme deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2046 Curando", OMZET, "pi", PI)
