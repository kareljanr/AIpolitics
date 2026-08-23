# ephemeral tick2047 — Integro YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T16:55:00Z"
ENTITY = "vzw_integro"
GAP = "gap_integro_nbb_pdf_assets_debt_subsidy_matrix_l5"
SRC = "src_integro_jr2025_cw"
SRC_EN = "src_integro_jr2025_cw_en"
SRC_FR = "src_integro_jr2025_cw_fr"
SRC_KBO = "src_integro_kbo_2047"
SRC_SITE = "src_integro_site_2047"

OMZET = "63703738"
PNL = "2089779"
EQUITY = "49536655"
BRUTO = "63694364"
FTE = "813.5"
OMZET24 = "62169598"
PNL24 = "1960286"
EQUITY24 = "48361498"
BRUTO24 = "62506372"
FTE24 = "831.6"
# pi = 0.55*5.5 + 0.35*6.0 + 0.10*(10-4) = 3.025 + 2.1 + 0.6 = 5.725
PI = "5.725"

DO_NOT_REDO = (
    "Curando, Integro, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, "
    "Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, "
    "Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, "
    "Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, "
    "Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, "
    "WZC Sint-Vincentius Avelgem, PC Sint-Hieronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, "
    "AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, "
    "Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, "
    "AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaus, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, "
    "CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, "
    "ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, "
    "FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, "
    "IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, "
    "Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, "
    "INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren, "
    "Sint-Jozef Rumst, Gravenkasteel, Armonea, Colisee Belgium, Prinsenhof, Vivalto Home BE, "
    "emeis Belgium / ORPEA, AGB Bornem"
)


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
r = next(x for x in qrows if x.get("task_id") == "rq_2047")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Integro VZW YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0654847196/integro",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick2047; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
            f"bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.07.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2047/integro_nl.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Integro YE2025 statutory",
        "url": "https://www.companyweb.be/en/0654847196/integro",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick2047; EN mirror YE2025 Medium; filed 10-07-2026; Last balance sheet year 2025; "
            f"FTE {FTE}; raw docs/doge/data/raw/tick2047/integro_en.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Integro YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0654847196/integro",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick2047; FR mirror YE2025 Medium; depose le 10-07-2026; "
            "raw docs/doge/data/raw/tick2047/integro_fr.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Integro 0654.847.196 Actief VZW aanbestedende overheid Hasselt",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0654847196",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": (
            "tick2047; Actief VZW; Kempische steenweg 555 3500 Hasselt (since 01.01.2025); "
            "11 VE; aanbestedende overheid sinds 19.05.2016; NACE 87.101; "
            "dagelijks bestuur Roel Eerlingen; KBO email empty; absorbed De Kring 30.09.2024"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Integro contact (info@integrozorg.eu) + Limburg multi-campus WZC footprint",
        "url": "https://www.integrozorg.eu/",
        "publisher": "Integro vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": (
            "tick2047; Kempische steenweg 555 Hasselt; info@integrozorg.eu; "
            "campuses Cecilia/Sint-Jozef/Immaculata/Voorzienigheid/Home Elisabeth/Het Park/Hamont e.a.; "
            "raw docs/doge/data/raw/tick2047/integro_site.html"
        ),
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_integro_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2047; omzet JUMP {OMZET} +2.47pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_integro_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2047; pnl JUMP {PNL} +6.61pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_integro_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2047; equity JUMP {EQUITY} +2.43pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_integro_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2047; bruto JUMP {BRUTO} +1.90pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_integro_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2047; FTE DROP {FTE} vs YE2024 {FTE24}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_integro_jr2025_statutory_wzc",
    "title": "Integro YE2025 leftover dual (omzet JUMP 63.70m / pnl JUMP 2.09m)",
    "entity_id": ENTITY,
    "beneficiary": "VL Limburg elderly-care residents (Integro multi-campus WZC/AW/DVC)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0654.847.196)",
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0654847196/integro",
    "stated_goal": "Limburg multi-campus nursing-home / assisted-living operations",
    "cut_option": "NBB PDF assets/debt + public subsidy vs dagprijs matrix FOI; campus-level split across 11 VE",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Integro>JR2025_statutory_L5",
    "notes": (
        "tick2047; Medium CW NL+EN+FR; assets/debt Unknown; Strong KBO aanbestedende overheid 11 VE; "
        "FARO/AIESH/REW still YE2024; Huize Vincent/Hof ter Waarbeek/Ter Kimme still YE2024 on CW; "
        "not TE-additive of 348bn"
    ),
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_integro_omzet_jump_63_70m_pnl_jump_jr2025",
    "name": "Integro omzet JUMP 63.70m / pnl JUMP 2.09m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Integro>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": (
        f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} "
        f"FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual"
    ),
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Limburg elderly-care residents via Integro campuses",
    "stated_goal": "Multi-campus WZC/AW/DVC social-profit operations",
    "measured_outcome": (
        "Medium CW YE2025; 63.70m omzet mild JUMP +2.47% with pnl JUMP +6.61%; "
        "FTE DROP 813.5 vs 831.6; assets/debt still opaque"
    ),
    "absurdity_score": "5.5",
    "cost_score": "6.0",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "FOI NBB PDF assets/debt + subsidy/dagprijs split; campus matrix 11 VE",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2047 leftover dual Integro; Medium CW; TE-adjacent WZC dual not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Integro (VZW, Limburg multi-campus WZC)",
    "name_fr": "Integro (ASBL, MRS multi-sites Limbourg)",
    "name_en": "Integro (VZW multi-campus nursing homes Limburg)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.integrozorg.eu/",
    "foi_email": "info@integrozorg.eu",
    "foi_postal": "Kempische steenweg 555, 3500 Hasselt",
    "notes": (
        f"tick2047 YE2025 Medium CW NL+EN+FR + Strong KBO 0654.847.196 Actief VZW aanbestedende overheid 11 VE; "
        f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; "
        f"neerlegging 10.07.2026; assets/debt Unknown; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
        "Huize Vincent/Hof ter Waarbeek/Ter Kimme CW still YE2024; do not redo Curando/De Verlosser/"
        "Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/AGB Bornem"
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
    "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Integro>NBB_PDF_assets_debt_subsidy_matrix",
    "entity_id": ENTITY,
    "what_is_missing": (
        "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/balanstotaal); "
        "public subsidy vs dagprijs split (IFIC/Alivia/Vlaio/code73); "
        "campus-level revenue matrix across 11 VE; related-party notes"
    ),
    "why_it_matters": (
        "Medium CW shows 63.70m omzet VL aanbestedende-overheid Limburg WZC VZW with pnl JUMP "
        "and no balanstotaal/assets/debt; material L5 residual for FOI"
    ),
    "priority": "8",
    "recipient_body": "Integro vzw",
    "recipient_email": "info@integrozorg.eu",
    "recipient_postal": "Kempische steenweg 555, 3500 Hasselt",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_integro_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_integro_omzet_jump_63_70m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2047; human-send only; Medium CW YE2025; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Integro (NBB PDF / assets-debt / subsidy matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Integro VZW — KBO **0654.847.196**  
**recipient:** info@integrozorg.eu · Kempische steenweg 555, 3500 Hasselt  
**sources:** [CW NL](https://www.companyweb.be/nl/0654847196/integro) · [CW EN](https://www.companyweb.be/en/0654847196/integro) · [CW FR](https://www.companyweb.be/fr/0654847196/integro) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0654847196) · [site](https://www.integrozorg.eu/)  
**tick:** 2047  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.07.2026**): omzet **EUR63,703,738** JUMP +2.47%; pnl **EUR2,089,779** JUMP +6.61% vs YE2024 EUR1,960,286; equity **EUR49,536,655** JUMP +2.43%; bruto **EUR63,694,364** JUMP +1.90%; FTE **{FTE}** (DROP vs {FTE24}); assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **11 VE**; zetel Kempische steenweg 555 Hasselt; NACE 87.101; dagelijks bestuur Roel Eerlingen.
- Preferred stall: FARO/AIESH/REW still YE2024. Huize Vincent / Hof ter Waarbeek / Ter Kimme CW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Integro vzw — Kempische steenweg 555, 3500 Hasselt
info@integrozorg.eu
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Integro + subsidiematrix (KBO 0654.847.196)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting FTE DROP (van {FTE24} YE2024 naar {FTE} YE2025) bij omzet/pnl JUMP.
5. Niet-confidentieel overzicht omzet/subsidies per campus of VE-groep (11 VE).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("draft", GAP)

# close rq_2047 + spawn rq_2048
r["status"] = "done"
r["entity_id"] = ENTITY
r["title"] = "leftover dual hole-fill after Curando — Integro YE2025 Medium"
r["instructions"] = (
    f"Completed leftover Integro YE2025 Medium CW; KBO 0654.847.196; "
    f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; "
    f"FOI {GAP}"
)
r["blocked_gap_id"] = GAP
r["updated_utc"] = UTC
r["notes"] = (
    f"tick2047 Integro Medium omzet JUMP 63.70m pnl JUMP 2.09m equity JUMP 49.54m bruto JUMP 63.69m; "
    f"FOI ready; FARO/AIESH/REW YE2024; Huize Vincent/Hof ter Waarbeek/Ter Kimme CW YE2024; "
    f"next rq_2048; next every-10 2050"
)

next_instr = (
    "Tick 2047 after Integro YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
    "hospital/WZC/psych (Huize Vincent/Hof ter Waarbeek/Ter Kimme still YE2024 on CW — skip until live; "
    "other unused YE2025 if live with omzet). Do NOT redo " + DO_NOT_REDO + ". "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/"
    "Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if "
    "figures appear. OLV Aalst deferred AZORG double-count."
)
if not any(x.get("task_id") == "rq_2048" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2048",
            "title": "leftover dual hole-fill after Integro",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": next_instr,
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                "spawned after tick2047 Integro; next every-10 2050; "
                "FARO/AIESH/REW YE2024; Huize Vincent/Hof/Ter Kimme YE2024"
            ),
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue rq_2047=done rq_2048=open")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
main = srows2[0]
main["mode"] = "continuous"
main["current_sprint"] = "hole_fill"
main["last_tick_utc"] = UTC
main["last_unit_id"] = "rq_2047"
main["ticks_completed"] = "2047"
main["paused"] = "no"
main["notes"] = (
    f"tick2047 leftover Integro 0654.847.196 Medium CW (omzet JUMP 63.70m pnl JUMP 2.09m "
    f"equity JUMP 49.54m bruto JUMP 63.69m FTE 813.5; assets/debt Unknown); "
    f"FARO/AIESH/REW YE2024; Huize Vincent/Hof ter Waarbeek/Ter Kimme YE2024; "
    f"next rq_2048; next every-10 2050; continuous hole_fill"
)
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state ticks=2047")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2047 - {UTC} - rq_2047 Integro (omzet JUMP 63.70m / pnl JUMP 2.09m / Medium)

- Unit: **rq_2047** leftover dual after **rq_2046 Curando**. Prefer NON-stall live: FARO/AIESH/REW still **YE2024**. Huize Vincent / Hof ter Waarbeek / Ter Kimme still **YE2024** on CW. Took deferred leftover **Integro** YE2025 (KBO **0654.847.196**; Kempische steenweg 555 Hasselt; Limburg **WZC VZW** / aanbestedende overheid / **11 VE**). Do not redo Curando/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR63,703,738** JUMP +2.47%; pnl **EUR2,089,779** JUMP +6.61%; equity **EUR49,536,655** JUMP +2.43%; bruto **EUR63,694,364** JUMP +1.90%; FTE **813.5** DROP vs 831.6; neerlegging **10.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 11 VE; email info@integrozorg.eu.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.725); entities (+1 vzw_integro); foi + draft {GAP}; rq_2047=done + rq_2048 open; loop_state ticks=2047; raw under docs/doge/data/raw/tick2047/.
- FOI: **ready not sent** (human-gated; info@integrozorg.eu).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2048 (FARO-if-YE2025 / AIESH-REW-if-YE2025 / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log appended")
