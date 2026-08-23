# ephemeral tick2049 — WZC Huize Vincent YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T17:25:00Z"
ENTITY = "vzw_wzc_huize_vincent"
GAP = "gap_wzc_huize_vincent_nbb_pdf_assets_debt_pnl_deeper_loss_matrix_l5"
SRC = "src_huize_vincent_jr2025_cw"
SRC_EN = "src_huize_vincent_jr2025_cw_en"
SRC_FR = "src_huize_vincent_jr2025_cw_fr"
SRC_KBO = "src_huize_vincent_kbo_2049"
SRC_SITE = "src_huize_vincent_zorgnet_2049"

OMZET = "6375376"
PNL = "-258313"
EQUITY = "6620452"
BRUTO = "5989296"
FTE = "85.2"
OMZET24 = "6285726"
PNL24 = "-97812"
EQUITY24 = "7000078"
BRUTO24 = "5889840"
# pi = 0.55*5.8 + 0.35*4.8 + 0.10*(10-4) = 3.19 + 1.68 + 0.6 = 5.47
PI = "5.47"

DO_NOT_REDO = (
    "Do NOT redo WZC Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, "
    "Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, "
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
    "emeis Belgium / ORPEA. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/"
    "Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. "
    "OLV Aalst deferred AZORG double-count. Bethanie Zoersel Emmaüs double-count."
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
r = next(x for x in qrows if x.get("task_id") == "rq_2049")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Huize Vincent VZW YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0463758978/woon-en-zorgcentrum-huize-vincent",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick2049; YE2025 omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} "
            f"bruto JUMP {BRUTO} FTE {FTE}; neerlegging 17.07.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2049/huize_vincent_nl.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Huize Vincent YE2025 statutory",
        "url": "https://www.companyweb.be/en/0463758978/woon-en-zorgcentrum-huize-vincent",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick2049; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025; "
            f"FTE {FTE}; raw docs/doge/data/raw/tick2049/huize_vincent_en.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Huize Vincent YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0463758978/woon-en-zorgcentrum-huize-vincent",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick2049; FR mirror YE2025 Medium; depose le 17-07-2026; "
            "raw docs/doge/data/raw/tick2049/huize_vincent_fr.html"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Huize Vincent 0463.758.978 Actief VZW aanbestedende overheid Temse",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463758978",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": (
            "tick2049; Actief VZW; Antwerpse Steenweg 103 9140 Temse (since 27.04.1998); "
            "1 VE; aanbestedende overheid sinds 27.04.1998; NACE 87.301 ROB; "
            "KBO email/phone/web empty"
        ),
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Zorgnet-Icuro member page Huize Vincent (info@huizevincent.be) + site",
        "url": "https://www.zorgneticuro.be/leden/woon-en-zorgcentrum-huize-vincent-tielrode",
        "publisher": "Zorgnet-Icuro / Huize Vincent",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": (
            "tick2049; Antwerpsesteenweg 103 Temse-Tielrode; info@huizevincent.be; "
            "tel 03 710 51 30; site huizevincent.be (SSL hostname mismatch on fetch; "
            "raw docs/doge/data/raw/tick2049/site_hv.html + zorgneticuro.html)"
        ),
    },
]:
    if ns["source_id"] not in {x.get("source_id") for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_huize_vincent_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2049; omzet JUMP {OMZET} +1.43pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_huize_vincent_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Winst/Verlies / Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2049; pnl DEEPER LOSS {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_huize_vincent_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2049; equity DROP {EQUITY} -5.42pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_huize_vincent_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2049; bruto JUMP {BRUTO} +1.69pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_huize_vincent_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2049; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_huize_vincent_jr2025_statutory_wzc",
    "title": "WZC Huize Vincent YE2025 leftover dual (omzet JUMP 6.38m / pnl DEEPER LOSS 0.26m)",
    "entity_id": ENTITY,
    "beneficiary": "Temse-Tielrode elderly-care residents (WZC Huize Vincent)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0463.758.978)",
    "decision_date": "2026-07-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0463758978/woon-en-zorgcentrum-huize-vincent",
    "stated_goal": "Christian-inspired nursing home care Temse-Tielrode",
    "cut_option": "Publish NBB PDF assets/debt + LOSS path + subsidy vs dagprijs split FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Temse>HuizeVincent>JR2025_statutory_L5",
    "notes": (
        "tick2049; Medium CW; assets/debt Unknown; preferred FARO/AIESH/REW YE2024; "
        "Hof ter Waarbeek YE2025 deferred; not TE-additive of 348bn"
    ),
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_huize_vincent_omzet_jump_6_38m_pnl_deeper_loss_jr2025",
    "name": "WZC Huize Vincent omzet JUMP 6.38m / pnl DEEPER LOSS 0.26m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Temse>HuizeVincent>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": (
        f"statutory omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} "
        f"bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual"
    ),
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Temse-Tielrode elderly-care residents via WZC Huize Vincent",
    "stated_goal": "Christian-inspired nursing home care Temse-Tielrode",
    "measured_outcome": (
        "Medium CW YE2025; 6.38m omzet JUMP +1.43pct with pnl DEEPER LOSS vs YE2024 "
        "and equity DROP -5.42pct; NBB PDF residual"
    ),
    "absurdity_score": "5.8",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": (
        "Publish NBB PDF assets/debt FOI; explain deepening LOSS + equity DROP path; "
        "map subsidy vs dagprijs"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": "tick2049 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Huize Vincent (VZW, Temse-Tielrode)",
    "name_fr": "MRS Huize Vincent (ASBL, Temse-Tielrode)",
    "name_en": "WZC Huize Vincent (VZW nursing home, Temse-Tielrode)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://huizevincent.be/",
    "foi_email": "info@huizevincent.be",
    "foi_postal": "Antwerpse Steenweg 103, 9140 Temse",
    "notes": (
        "tick2049 YE2025 Medium CW NL+EN+FR + Strong KBO 0463.758.978 Actief VZW aanbestedende overheid 1 VE; "
        f"omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; "
        "assets/debt Unknown; neerlegging 17.07.2026; FOI "
        + GAP
        + "; preferred FARO/AIESH/REW YE2024; Hof ter Waarbeek YE2025 deferred; "
        "do not redo Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/"
        "Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal"
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
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Temse>HuizeVincent>NBB_PDF_assets_debt_pnl_deeper_loss",
    "entity_id": ENTITY,
    "what_is_missing": (
        "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DEEPER LOSS recon vs YE2024; "
        "equity DROP recon; public subsidy vs dagprijs split"
    ),
    "why_it_matters": (
        "Medium CW shows 6.38m omzet VL aanbestedende-overheid Temse WZC VZW with deepening LOSS "
        "and equity DROP without balanstotaal/assets/debt; material L5 residual for FOI"
    ),
    "priority": "8",
    "recipient_body": "Woon- en zorgcentrum Huize Vincent vzw",
    "recipient_email": "info@huizevincent.be",
    "recipient_postal": "Antwerpse Steenweg 103, 9140 Temse",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_huize_vincent_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_huize_vincent_omzet_jump_6_38m_pnl_deeper_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2049; human-send only; Medium CW; email via Zorgnet-Icuro member page; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Huize Vincent (NBB PDF / assets-debt / deeper LOSS matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en zorgcentrum Huize Vincent VZW — KBO **0463.758.978**  
**recipient:** info@huizevincent.be · Antwerpse Steenweg 103, 9140 Temse  
**sources:** [CW NL](https://www.companyweb.be/nl/0463758978/woon-en-zorgcentrum-huize-vincent) · [CW EN](https://www.companyweb.be/en/0463758978/woon-en-zorgcentrum-huize-vincent) · [CW FR](https://www.companyweb.be/fr/0463758978/woon-en-zorgcentrum-huize-vincent) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463758978) · [Zorgnet-Icuro](https://www.zorgneticuro.be/leden/woon-en-zorgcentrum-huize-vincent-tielrode) · [site](https://huizevincent.be/)  
**tick:** 2049  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **17.07.2026**): omzet **EUR6,375,376** JUMP +1.43%; pnl **LOSS EUR-258,313** DEEPER vs YE2024 LOSS EUR-97,812; equity **EUR6,620,452** DROP -5.42%; bruto **EUR5,989,296** JUMP +1.69%; FTE **85.2**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **1 VE**; zetel Antwerpse Steenweg 103 Temse; NACE 87.301 ROB.
- Preferred stall: FARO/AIESH/REW still YE2024. Hof ter Waarbeek YE2025 deferred.
- Email via Zorgnet-Icuro member page (KBO email empty).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en zorgcentrum Huize Vincent vzw — Antwerpse Steenweg 103, 9140 Temse
info@huizevincent.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Huize Vincent + verlies/eigen-vermogen toelichting (KBO 0463.758.978)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 17.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Toelichting dieper verlies (van EUR-97.812 YE2024 naar EUR-258.313 YE2025) en equity DROP (~5.4%).
4. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2049":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Ter Kimme — WZC Huize Vincent YE2025 Medium"
        x["notes"] = (
            "tick2049 Huize Vincent Medium omzet JUMP 6.38m pnl DEEPER LOSS 0.26m equity DROP 6.62m bruto JUMP 5.99m; "
            "FOI ready; FARO/AIESH/REW YE2024; Hof Waarbeek deferred; next rq_2050 EVERY-10; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover WZC Huize Vincent YE2025 Medium CW; KBO 0463.758.978; "
            f"omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2050" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2050",
            "title": "EVERY-10 + leftover dual hole-fill after Huize Vincent",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2049 after WZC Huize Vincent YE2025 Medium. EVERY-10 mandatory: refresh "
                "progress_every_10_ticks.md + doge_waste_top10_current.md. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                "hospital/WZC/psych (Hof ter Waarbeek YE2025 live deferred / other unused YE2025 if live with omzet). "
                + DO_NOT_REDO
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                "spawned after tick2049 Huize Vincent; EVERY-10 mandatory at 2050; FARO/AIESH/REW YE2024; "
                "Hof Waarbeek YE2025 deferred"
            ),
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
        "last_unit_id": "rq_2049",
        "ticks_completed": "2049",
        "paused": "no",
        "notes": (
            "tick2049 leftover WZC Huize Vincent 0463.758.978 Medium CW (omzet JUMP 6.38m pnl DEEPER LOSS 0.26m "
            "equity DROP 6.62m bruto JUMP 5.99m FTE 85.2; assets/debt Unknown); FARO/AIESH/REW YE2024; "
            "Hof Waarbeek deferred; next rq_2050 EVERY-10; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2049 - {UTC} - rq_2049 WZC Huize Vincent (omzet JUMP 6.38m / pnl DEEPER LOSS 0.26m / Medium)

- Unit: **rq_2049** leftover dual after **rq_2048 Ter Kimme**. Prefer NON-stall live: FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC Huize Vincent** YE2025 (KBO **0463.758.978**; Antwerpse Steenweg 103 Temse-Tielrode; Oost-Vlaanderen **aanbestedende-overheid VZW** WZC / **1 VE**). Hof ter Waarbeek YE2025 also live — deferred. Do not redo Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR6,375,376** JUMP +1.43%; pnl **LOSS EUR-258,313** DEEPER vs YE2024 LOSS EUR-97,812; equity **EUR6,620,452** DROP -5.42%; bruto **EUR5,989,296** JUMP +1.69%; FTE **85.2**; neerlegging **17.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email info@huizevincent.be (Zorgnet-Icuro).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2049=done + rq_2050 open (EVERY-10); loop_state ticks=2049; raw under docs/doge/data/raw/tick2049/.
- FOI: **ready not sent** (human-gated; info@huizevincent.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2050 (EVERY-10 mandatory + FARO-if-YE2025 / AIESH-REW / Hof Waarbeek deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2049 Huize Vincent", OMZET, "pi", PI)
