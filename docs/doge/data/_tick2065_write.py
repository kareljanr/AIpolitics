# ephemeral tick2065 — Seniorencentrum OLV Bornem YE2025 Medium (after concurrent 2064 Huize SJ Ieper)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T21:20:00Z"
ENTITY = "vzw_seniorencentrum_olv_bornem"
GAP = "gap_olv_bornem_nbb_pdf_assets_debt_pnl_flip_profit_matrix_l5"
SRC = "src_olv_bornem_jr2025_cw"
SRC_EN = "src_olv_bornem_jr2025_cw_en"
SRC_FR = "src_olv_bornem_jr2025_cw_fr"
SRC_KBO = "src_olv_bornem_kbo_2065"
SRC_SITE = "src_olv_bornem_site_2065"

OMZET = "9031100"
PNL = "97560"
EQUITY = "8979861"
BRUTO = "8498187"
FTE = "94.4"
OMZET24 = "8661884"
PNL24 = "-92293"
EQUITY24 = "8948073"
BRUTO24 = "7865391"
# pi = 0.55*4.6 + 0.35*4.8 + 0.10*(10-4) = 2.53 + 1.68 + 0.6 = 4.81 → 4.8
PI = "4.8"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2065")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Seniorencentrum OLV Bornem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0436595020/seniorencentrum-onze-lieve-vrouw-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2065; YE2025 omzet JUMP {OMZET} pnl FLIP PROFIT {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 21.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2065/olv_bornem_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Seniorencentrum OLV Bornem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0436595020/seniorencentrum-onze-lieve-vrouw-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2065; EN mirror YE2025 Medium; filed 21-08-2026; Last balance sheet year 2025; FTE 94.4; raw docs/doge/data/raw/tick2065/olv_bornem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Seniorencentrum OLV Bornem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0436595020/seniorencentrum-onze-lieve-vrouw-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2065; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2065/olv_bornem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Seniorencentrum Onze Lieve Vrouw VZW 0436.595.020 Actief Bornem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436595020",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2065; Actief VZW; Stationsstraat(BOR) 29 2880 Bornem (since 01.10.1990); 1 VE; NACE 87.301 ROB; tel 03/899.05.01; web www.seniorencentrum-olv.be; KBO email empty; not marked aanbestedende overheid; RSZ since 01.01.1989",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Seniorencentrum OLV site www.seniorencentrum-olv.be (info@seniorencentrum-olv.be)",
        "url": "https://www.seniorencentrum-olv.be/",
        "publisher": "Seniorencentrum Onze Lieve Vrouw vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2065; Stationsstraat 29 2880 Bornem; Tel 03 899 05 01; email info@seniorencentrum-olv.be; raw docs/doge/data/raw/tick2065/site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_olv_bornem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2065; omzet JUMP {OMZET} +4.26pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_olv_bornem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2065; pnl FLIP PROFIT {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_olv_bornem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2065; equity JUMP {EQUITY} +0.36pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_olv_bornem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2065; bruto JUMP {BRUTO} +8.05pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_olv_bornem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2065; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_olv_bornem_jr2025_statutory_wzc",
    "title": "Seniorencentrum OLV Bornem YE2025 leftover dual (omzet JUMP 9.03m / pnl FLIP PROFIT 98k)",
    "entity_id": ENTITY,
    "beneficiary": "Bornem elderly residents (Seniorencentrum Onze Lieve Vrouw)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0436.595.020)",
    "decision_date": "2026-08-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0436595020/seniorencentrum-onze-lieve-vrouw-vzw",
    "stated_goal": "WZC residential elderly care Bornem Stationsstraat + assistentiewoningen/dagverzorging",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl FLIP from LOSS YE2024 to PROFIT YE2025",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>SeniorencentrumOLV>JR2025_statutory_L5",
    "notes": "tick2065; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Bejaardenzorg Zusters Deinze / Leiehome / Compostela / Always Home / Vulpia YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_olv_bornem_omzet_jump_9_03m_pnl_flip_profit_jr2025",
    "name": "Seniorencentrum OLV Bornem omzet JUMP 9.03m / pnl FLIP PROFIT 98k (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>SeniorencentrumOLV>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP PROFIT {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Bornem elderly residents via Seniorencentrum OLV",
    "stated_goal": "WZC residential elderly care Bornem",
    "measured_outcome": "Medium CW YE2025; 9.03m omzet JUMP +4.26pct with pnl FLIP PROFIT from YE2024 LOSS 92k and equity JUMP +0.36pct; NBB PDF residual",
    "absurdity_score": "4.6",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl FLIP PROFIT; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2065 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Seniorencentrum Onze Lieve Vrouw VZW (Bornem)",
    "name_fr": "Seniorencentrum Onze Lieve Vrouw (ASBL MRS, Bornem)",
    "name_en": "Seniorencentrum Onze Lieve Vrouw (VZW nursing home Bornem)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.seniorencentrum-olv.be/",
    "foi_email": "info@seniorencentrum-olv.be",
    "foi_postal": "Stationsstraat 29, 2880 Bornem",
    "notes": (
        "tick2065 YE2025 Medium CW NL+EN+FR + Strong KBO 0436.595.020 Actief VZW 1 VE; omzet JUMP 9.03m pnl FLIP PROFIT 98k equity JUMP 8.98m bruto JUMP 8.50m FTE 94.4; "
        "assets/debt Unknown; neerlegging 21.08.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Bejaardenzorg Zusters Deinze/Leiehome/Compostela/Always Home/Vulpia YE2025 deferred; do not redo Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>Antwerpen>Bornem>SeniorencentrumOLV>NBB_PDF_assets_debt_pnl_flip_profit",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl FLIP from LOSS YE2024 EUR-92,293 to PROFIT YE2025 EUR97,560",
    "why_it_matters": "Medium CW shows 9.03m omzet WZC VZW with pnl FLIP PROFIT + equity JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Seniorencentrum Onze Lieve Vrouw vzw",
    "recipient_email": "info@seniorencentrum-olv.be",
    "recipient_postal": "Stationsstraat 29, 2880 Bornem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_olv_bornem_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_olv_bornem_omzet_jump_9_03m_pnl_flip_profit_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2065; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Seniorencentrum OLV Bornem (NBB PDF / assets-debt / pnl-flip-profit)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Seniorencentrum Onze Lieve Vrouw VZW — KBO **0436.595.020**  
**recipient:** info@seniorencentrum-olv.be · Stationsstraat 29, 2880 Bornem  
**sources:** [CW NL](https://www.companyweb.be/nl/0436595020/seniorencentrum-onze-lieve-vrouw-vzw) · [CW EN](https://www.companyweb.be/en/0436595020/seniorencentrum-onze-lieve-vrouw-vzw) · [CW FR](https://www.companyweb.be/fr/0436595020/seniorencentrum-onze-lieve-vrouw-vzw) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436595020) · [site](https://www.seniorencentrum-olv.be/)  
**tick:** 2065  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **21.08.2026**): omzet **EUR9,031,100** JUMP +4.26%; pnl **PROFIT EUR97,560** FLIP vs YE2024 LOSS EUR-92,293; equity **EUR8,979,861** JUMP +0.36%; bruto **EUR8,498,187** JUMP +8.05%; FTE **94.4**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Stationsstraat 29 Bornem; NACE 87.301 ROB; tel 03/899.05.01; web www.seniorencentrum-olv.be; KBO email empty (site info@seniorencentrum-olv.be); niet gemarkeerd als aanbestedende overheid.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred: Bejaardenzorg Zusters Deinze / Leiehome / Compostela / Always Home / Vulpia YE2025.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Seniorencentrum Onze Lieve Vrouw vzw — Stationsstraat 29, 2880 Bornem
info@seniorencentrum-olv.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Seniorencentrum OLV Bornem + subsidiematrix (KBO 0436.595.020)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 21.08.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting omslag van verlies (EUR-92.293 YE2024) naar winst (EUR97.560 YE2025) bij omzet JUMP +4,26%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, "
    "Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, "
    "Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
    "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2065":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Huize Sint-Jozef Ieper — Seniorencentrum OLV Bornem YE2025 Medium"
        x["notes"] = (
            "tick2065 OLV Bornem Medium omzet JUMP 9.03m pnl FLIP PROFIT 98k equity JUMP 8.98m bruto JUMP 8.50m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Bejaardenzorg Zusters Deinze/Leiehome/Compostela/Always Home/Vulpia YE2025 deferred; next rq_2066; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Seniorencentrum OLV Bornem YE2025 Medium CW; KBO 0436.595.020; "
            f"omzet JUMP {OMZET} pnl FLIP PROFIT {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2066" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2066",
            "title": "leftover dual hole-fill after Seniorencentrum OLV Bornem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2065 after Seniorencentrum OLV Bornem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else Bejaardenzorg Zusters Sint-Vincentius Deinze YE2025 (KBO 0454.090.355) if still unused, "
                "else Leiehome / Compostela / Always Home / Vulpia if still live with omzet, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2065 Seniorencentrum OLV Bornem; next every-10 2070",
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
        "last_unit_id": "rq_2065",
        "ticks_completed": "2065",
        "paused": "no",
        "notes": (
            "tick2065 leftover Seniorencentrum OLV Bornem 0436.595.020 Medium CW (omzet JUMP 9.03m pnl FLIP PROFIT 98k equity JUMP 8.98m bruto JUMP 8.50m FTE 94.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Bejaardenzorg Zusters Deinze/Leiehome/Compostela/Always Home/Vulpia YE2025 deferred; next rq_2066; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2065 — 2026-08-24T21:20:00Z — rq_2065 Seniorencentrum OLV Bornem (omzet JUMP 9.03m / pnl FLIP PROFIT 98k / Medium)

- Unit: **rq_2065** leftover dual after **rq_2064 Huize Sint-Jozef Ieper** (concurrent race claimed 2064). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (rechecked); AIESH/REW still **YE2024**. Took unused leftover **Seniorencentrum Onze Lieve Vrouw Bornem** YE2025 (KBO **0436.595.020**; Stationsstraat 29 Bornem; Antwerpen **VZW** WZC / **1 VE**). Bejaardenzorg Zusters Sint-Vincentius Deinze / Leiehome / Compostela / Always Home / Vulpia YE2025 also live — deferred. Do not redo Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR9,031,100** JUMP +4.26%; pnl **PROFIT EUR97,560** FLIP vs YE2024 LOSS EUR-92,293; equity **EUR8,979,861** JUMP +0.36%; bruto **EUR8,498,187** JUMP +8.05%; FTE **94.4**; neerlegging **21.08.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE NACE 87.301; email info@seniorencentrum-olv.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.8); entities (+1 vzw_seniorencentrum_olv_bornem); foi + draft {GAP}; rq_2065=done + rq_2066 open; loop_state ticks=2065; raw under docs/doge/data/raw/tick2065/.
- FOI: **ready not sent** (human-gated; info@seniorencentrum-olv.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2066 (AGB/FARO-if-YE2025 / AIESH-REW / Bejaardenzorg Zusters Deinze deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2065")
