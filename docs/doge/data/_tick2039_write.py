# ephemeral tick2039 — C.W.Z.C. Zonhoven YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T14:25:00Z"
ENTITY = "vzw_cwzc_zonhoven"
GAP = "gap_cwzc_zonhoven_nbb_pdf_assets_debt_pnl_flip_matrix_l5"
SRC = "src_cwzc_zonhoven_jr2025_cw"
SRC_EN = "src_cwzc_zonhoven_jr2025_cw_en"
SRC_FR = "src_cwzc_zonhoven_jr2025_cw_fr"
SRC_KBO = "src_cwzc_zonhoven_kbo_2039"
SRC_SITE = "src_cwzc_zonhoven_site_2039"
SRC_REPER = "src_cwzc_zonhoven_zorg_repertorium_email_2039"

OMZET = "8556731"
PNL = "508040"
EQUITY = "16170229"
BRUTO = "16590512"
FTE = "182"
OMZET24 = "7929328"
PNL24 = "-797334"
EQUITY24 = "15840170"
BRUTO24 = "14667250"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2039")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL C.W.Z.C. YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0413203073/christelijke-woon-en-zorgcentra",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2039; YE2025 omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 24.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2039/cwzc_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN C.W.Z.C. YE2025 statutory",
        "url": "https://www.companyweb.be/en/0413203073/christelijke-woon-en-zorgcentra",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2039; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; FTE 182; raw docs/doge/data/raw/tick2039/cwzc_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR C.W.Z.C. YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0413203073/christelijke-woon-en-zorgcentra",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2039; FR mirror YE2025 Medium; déposés le 24-06-2026; raw docs/doge/data/raw/tick2039/cwzc_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO C.W.Z.C. 0413.203.073 Actief VZW Zonhoven",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413203073",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2039; Actief VZW; Engstegenseweg 3 3520 Zonhoven; 3 VE; no KBO email; afkorting C.W.Z.C.; aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "cwzc.be C.W.Z.C. campussen",
        "url": "http://www.cwzc.be/",
        "publisher": "C.W.Z.C. vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2039; HTTP site (HTTPS hostname mismatch); campuses H.Catharina/Dorpvelt/Sint-Jozef; raw docs/doge/data/raw/tick2039/cwzc_site.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_REPER,
        "title": "Departement Zorg repertorium Limburg WZC/CVK — CWZC emails",
        "url": "https://www.zorg-en-gezondheid.be/sites/default/files/external/Repertorium_burst_def_-_ADRESSEN_WZC-_PROVINCIE_Limburg.pdf",
        "publisher": "Departement Zorg Vlaanderen",
        "accessed_date": "2026-08-24",
        "source_class": "official_gov",
        "notes": "tick2039; PE935 Heilige Catharina + PE2837 Het Dorpvelt list info@cwzc.be; CVK Apostelhuis apostelhuis@cwzc.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_cwzc_zonhoven_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2039; omzet JUMP {OMZET} +7.91pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_cwzc_zonhoven_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2039; pnl FLIP profit {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_cwzc_zonhoven_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2039; equity JUMP {EQUITY} +2.08pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_cwzc_zonhoven_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2039; bruto JUMP {BRUTO} +13.11pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_cwzc_zonhoven_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2039; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_cwzc_zonhoven_jr2025_statutory_wzc",
    "title": "C.W.Z.C. Zonhoven YE2025 leftover dual (omzet JUMP 8.56m / pnl FLIP 0.51m)",
    "entity_id": ENTITY,
    "beneficiary": "Limburg elderly care residents (Zonhoven + Munsterbilzen campuses)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0413.203.073)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0413203073/christelijke-woon-en-zorgcentra",
    "stated_goal": "Christian residential elderly care (Limburg multi-campus)",
    "cut_option": "Publish NBB PDF assets/debt + pnl FLIP FOI; map public subsidies vs resident fees",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Limburg>Zonhoven>CWZC>JR2025_statutory_L5",
    "notes": "tick2039; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Samen Ouder/De Linde YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*4.0 + 0.35*5.5 + 0.10*(10-4) = 2.2 + 1.925 + 0.6 = 4.725
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_cwzc_zonhoven_omzet_jump_8_56m_pnl_flip_0_51m_jr2025",
    "name": "C.W.Z.C. Zonhoven omzet JUMP 8.56m / pnl FLIP 0.51m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "Limburg>Zonhoven>CWZC>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Limburg elderly via C.W.Z.C. VZW (Zonhoven+Munsterbilzen)",
    "stated_goal": "Christian residential elderly care",
    "measured_outcome": "Medium CW YE2025; 8.56m omzet JUMP +7.91pct with pnl FLIP from -0.80m LOSS to +0.51m; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "4.0",
    "difficulty": "4.0",
    "priority_index": "4.725",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl FLIP vs public care euros; map subsidy vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2039 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "C.W.Z.C. / Christelijke Woon- en Zorgcentra (Zonhoven)",
    "name_fr": "C.W.Z.C. / Centres de soins chrétiens (Zonhoven)",
    "name_en": "C.W.Z.C. Christian residential care centres (Zonhoven)",
    "level": "vzw",
    "parent_id": "prov_limburg",
    "community_language": "nl",
    "website": "http://www.cwzc.be/",
    "foi_email": "info@cwzc.be",
    "foi_postal": "Engstegenseweg 3, 3520 Zonhoven",
    "notes": "tick2039 YE2025 Medium CW NL+EN+FR + Strong KBO 0413.203.073 Actief VZW; omzet JUMP 8.56m pnl FLIP 0.51m equity JUMP 16.17m bruto JUMP 16.59m FTE 182; assets/debt Unknown; neerlegging 24.06.2026; 3 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Samen Ouder/De Linde YE2025 deferred; do not redo Orelia/Kanunnik Triest/OLVA/OLV Roosdaal/Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have",
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
    "hierarchy_path": "Limburg>Zonhoven>CWZC>NBB_PDF_assets_debt_pnl_flip",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl FLIP recon (-0.80m LOSS YE2024 to +0.51m YE2025)",
    "why_it_matters": "Medium CW shows 8.56m omzet Limburg multi-campus WZC VZW (aanbestedende overheid) with pnl FLIP without balance sheet or subsidy transparency",
    "priority": "8",
    "recipient_body": "C.W.Z.C. vzw / Christelijke Woon- en Zorgcentra",
    "recipient_email": "info@cwzc.be",
    "recipient_postal": "Engstegenseweg 3, 3520 Zonhoven",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_cwzc_zonhoven_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_cwzc_zonhoven_omzet_jump_8_56m_pnl_flip_0_51m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2039; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — C.W.Z.C. Zonhoven (NBB PDF / assets-debt / pnl FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** C.W.Z.C. vzw — KBO **0413.203.073**  
**recipient:** info@cwzc.be · Engstegenseweg 3, 3520 Zonhoven  
**sources:** [CW NL](https://www.companyweb.be/nl/0413203073/christelijke-woon-en-zorgcentra) · [CW EN](https://www.companyweb.be/en/0413203073/christelijke-woon-en-zorgcentra) · [CW FR](https://www.companyweb.be/fr/0413203073/christelijke-woon-en-zorgcentra) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413203073) · [site](http://www.cwzc.be/) · Departement Zorg repertorium Limburg  
**tick:** 2039  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.06.2026**): omzet **EUR8,556,731** JUMP +7.91%; pnl **EUR508,040** FLIP vs YE2024 LOSS; equity **EUR16,170,229** JUMP +2.08%; bruto **EUR16,590,512** JUMP +13.11%; FTE **182**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Orelia already mined. Samen Ouder / De Linde YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: C.W.Z.C. vzw — Engstegenseweg 3, 3520 Zonhoven
info@cwzc.be
cc: Agentschap Zorg en Gezondheid / Provincie Limburg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 C.W.Z.C. + balans (KBO 0413.203.073)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl FLIP (van LOSS EUR-797.334 YE2024 naar winst EUR508.040 YE2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2039":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Orelia Zorg — C.W.Z.C. Zonhoven YE2025 Medium"
        x["notes"] = (
            "tick2039 C.W.Z.C. Zonhoven Medium omzet JUMP 8.56m pnl FLIP 0.51m equity JUMP 16.17m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Samen Ouder/De Linde deferred; next rq_2040; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover C.W.Z.C. Zonhoven YE2025 Medium CW; KBO 0413.203.073; "
            f"omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2040" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2040",
            "title": "EVERY-10 + leftover dual hole-fill after C.W.Z.C. Zonhoven",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2039 after C.W.Z.C. Zonhoven YE2025 Medium. FIRST: mandatory every-10 refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "THEN Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Woonzorg Samen Ouder YE2025 live deferred / WZC De Linde Lievegem YE2025 / other unused YE2025 if live with omzet). "
                "Do NOT redo C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2039 C.W.Z.C. Zonhoven; EVERY-10 mandatory at 2040; Samen Ouder/De Linde YE2025 deferred",
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
        "last_unit_id": "rq_2039",
        "ticks_completed": "2039",
        "paused": "no",
        "notes": (
            "tick2039 leftover C.W.Z.C. Zonhoven 0413.203.073 Medium CW (omzet JUMP 8.56m pnl FLIP 0.51m equity JUMP 16.17m bruto JUMP 16.59m FTE 182; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Samen Ouder/De Linde deferred; next rq_2040 EVERY-10; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2039 - {UTC} - rq_2039 C.W.Z.C. Zonhoven (omzet JUMP 8.56m / pnl FLIP 0.51m / Medium)

- Unit: **rq_2039** leftover dual after **rq_2038 Orelia Zorg**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **C.W.Z.C. Zonhoven** YE2025 (KBO **0413.203.073**; Engstegenseweg 3 Zonhoven; Limburg **WZC VZW** / aanbestedende overheid; 3 VE). Samen Ouder / De Linde YE2025 also live — deferred. Do not redo Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR8,556,731** JUMP +7.91%; pnl **EUR508,040** FLIP vs YE2024 LOSS EUR-797,334; equity **EUR16,170,229** JUMP +2.08%; bruto **EUR16,590,512** JUMP +13.11%; FTE **182**; neerlegging **24.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email info@cwzc.be (Departement Zorg repertorium).
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi 4.725); entities (+1 vzw_cwzc_zonhoven); foi + draft {GAP}; rq_2039=done + rq_2040 open (EVERY-10); loop_state ticks=2039; raw under docs/doge/data/raw/tick2039/.
- FOI: **ready not sent** (human-gated; info@cwzc.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2040 (EVERY-10 mandatory + AGB/FARO-if-YE2025 / AIESH-REW / Samen Ouder-De Linde deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
