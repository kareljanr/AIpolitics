# ephemeral tick2030 — EVERY-10 + WZC St Vincentius Antwerpen/Ekeren YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T12:10:00Z"
ENTITY = "vzw_wzc_st_vincentius_antwerpen"
GAP = "gap_wzc_st_vincentius_antwerpen_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_wzc_st_vincentius_antwerpen_jr2025_cw"
SRC_EN = "src_wzc_st_vincentius_antwerpen_jr2025_cw_en"
SRC_FR = "src_wzc_st_vincentius_antwerpen_jr2025_cw_fr"
SRC_KBO = "src_wzc_st_vincentius_antwerpen_kbo_2030"
SRC_SITE = "src_wzc_st_vincentius_antwerpen_site_2030"

OMZET = "7550039"
PNL = "427313"
EQUITY = "12448629"
BRUTO = "7362184"
FTE = "89.8"
OMZET24 = "7435346"
PNL24 = "351690"
EQUITY24 = "12302513"
BRUTO24 = "7227230"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def count_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2030")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC St Vincentius Antwerpen/Ekeren YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0418016550/woonzorgcentrum-st-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2030 EVERY-10; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 17.07.2026; assets/debt Unknown; distinct from Avelgem; raw docs/doge/data/raw/tick2030/vincentius_ant_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC St Vincentius Antwerpen/Ekeren YE2025 statutory",
        "url": "https://www.companyweb.be/en/0418016550/woonzorgcentrum-st-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2030 EVERY-10; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025; FTE 89.8; raw docs/doge/data/raw/tick2030/vincentius_ant_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC St Vincentius Antwerpen/Ekeren YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0418016550/woonzorgcentrum-st-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2030 EVERY-10; FR mirror YE2025 Medium; déposés le 17-07-2026; raw docs/doge/data/raw/tick2030/vincentius_ant_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum St Vincentius 0418.016.550 Actief VZW Ekeren",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418016550",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2030; Actief VZW since 02.03.1978; Dorpstraat 32 2180 Antwerpen; 2 VE; KBO email inge.vriesacker@vincentiusekeren.be",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "vincentiusekeren.be WZC Sint-Vincentius Ekeren",
        "url": "https://www.vincentiusekeren.be/",
        "publisher": "WZC Sint-Vincentius Ekeren",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2030; info@vincentiusekeren.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_st_vincentius_antwerpen_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030 EVERY-10; omzet JUMP {OMZET} +1.54pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_st_vincentius_antwerpen_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030 EVERY-10; pnl JUMP {PNL} +21.50pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_st_vincentius_antwerpen_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030 EVERY-10; equity JUMP {EQUITY} +1.19pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_st_vincentius_antwerpen_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030 EVERY-10; bruto JUMP {BRUTO} +1.87pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_st_vincentius_antwerpen_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_st_vincentius_antwerpen_jr2025_statutory_wzc",
    "title": "WZC St Vincentius Antwerpen/Ekeren YE2025 EVERY-10 leftover dual (omzet JUMP 7.55m / pnl JUMP 0.43m / equity JUMP 12.45m)",
    "entity_id": ENTITY,
    "beneficiary": "Ekeren/Antwerpen elderly care residents / WZC St Vincentius",
    "legal_basis": "VZW/ASBL WZC (KBO 0418.016.550)",
    "decision_date": "2026-07-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0418016550/woonzorgcentrum-st-vincentius",
    "stated_goal": "Residential elderly care (Ekeren)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>WZC_St_Vincentius_Ekeren>JR2025_statutory_L5",
    "notes": "tick2030 EVERY-10; Medium CW; assets/debt Unknown; DISTINCT from Avelgem Sint-Vincentius; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Lourdes/OLVA/Triest deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 4.275
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_st_vincentius_antwerpen_omzet_jump_7_55m_pnl_jump_0_43m_jr2025",
    "name": "WZC St Vincentius Antwerpen/Ekeren omzet JUMP 7.55m / pnl JUMP 0.43m / equity JUMP 12.45m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "Antwerpen>WZC_St_Vincentius_Ekeren>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Ekeren elderly via WZC St Vincentius VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.55m omzet JUMP +1.54pct with pnl JUMP +21.50pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.275",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2030 EVERY-10 leftover dual; Medium CW; distinct from Avelgem; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum St. Vincentius (Antwerpen/Ekeren)",
    "name_fr": "Maison de repos St. Vincentius (Anvers/Ekeren)",
    "name_en": "WZC St Vincentius Antwerpen/Ekeren (elderly care)",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.vincentiusekeren.be/",
    "foi_email": "info@vincentiusekeren.be",
    "foi_postal": "Dorpstraat 32, 2180 Antwerpen (Ekeren)",
    "notes": "tick2030 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0418.016.550 Actief VZW; omzet JUMP 7.55m pnl JUMP 0.43m equity JUMP 12.45m bruto JUMP 7.36m FTE 89.8; assets/debt Unknown; neerlegging 17.07.2026; 2 VE; DISTINCT from Avelgem; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "Antwerpen>WZC_St_Vincentius_Ekeren>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split",
    "why_it_matters": "Medium CW shows 7.55m omzet Ekeren WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "Woonzorgcentrum St. Vincentius vzw",
    "recipient_email": "info@vincentiusekeren.be",
    "recipient_postal": "Dorpstraat 32, 2180 Antwerpen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_st_vincentius_antwerpen_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_st_vincentius_antwerpen_omzet_jump_7_55m_pnl_jump_0_43m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2030 EVERY-10; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC St Vincentius Antwerpen/Ekeren (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum St. Vincentius vzw — KBO **0418.016.550**  
**recipient:** info@vincentiusekeren.be · Dorpstraat 32, 2180 Antwerpen  
**sources:** [CW NL](https://www.companyweb.be/nl/0418016550/woonzorgcentrum-st-vincentius) · [CW EN](https://www.companyweb.be/en/0418016550/woonzorgcentrum-st-vincentius) · [CW FR](https://www.companyweb.be/fr/0418016550/woonzorgcentrum-st-vincentius) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418016550) · [site](https://www.vincentiusekeren.be/)  
**tick:** 2030 EVERY-10  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **17.07.2026**): omzet **EUR7,550,039** JUMP +1.54%; pnl **EUR427,313** JUMP +21.50%; equity **EUR12,448,629** JUMP +1.19%; bruto **EUR7,362,184** JUMP +1.87%; FTE **89.8**; assets/debt **Unknown**.
- Distinct from WZC Sint-Vincentius Avelgem. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Lourdes/OLVA/Kanunnik Triest deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum St. Vincentius vzw — Dorpstraat 32, 2180 Antwerpen
info@vincentiusekeren.be
cc: Agentschap Zorg en Gezondheid / Stad Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC St Vincentius Ekeren + balans (KBO 0418.016.550)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 17.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

# EVERY-10 inventory after writes
n_bud = count_rows("docs/doge/data/budgets.csv")
n_comm = count_rows("docs/doge/data/commitments.csv")
n_lb = count_rows("docs/doge/data/leaderboard.csv")
n_ent = count_rows("docs/doge/data/entities.csv")
n_src = count_rows("docs/doge/data/sources.csv")
with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
    frows2 = list(csv.DictReader(f))
n_foi = len(frows2)
n_ready = sum(1 for x in frows2 if (x.get("status") or "").lower() == "ready")
n_ans = sum(1 for x in frows2 if (x.get("status") or "").lower() == "answered")
n_part = sum(1 for x in frows2 if (x.get("status") or "").lower() == "partial")

progress = Path("docs/doge/data/progress_every_10_ticks.md")
prog_text = progress.read_text(encoding="utf-8")
snapshot = f"""## Snapshot at **tick 2030** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2021-2030 WZC/psych/zorggroep continuum after 2020 PC Sint-Hiëronymus |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2021-2030 is residual dual L5 (not near-complete of 348bn):** **WZC Sint-Vincentius Avelgem** omzet JUMP **7.49m** · **PPC Pittem** omzet JUMP **42.45m** / pnl JUMP · **Maria Rustoord Ingelmunster** omzet JUMP **11.64m** / pnl DROP · **Evara/Multiversum** omzet JUMP **443.17m** / pnl DROP · **Sint Carolus Mayerhof** omzet DROP **11.46m** / pnl DROP · **WZC Zilverbos** omzet JUMP **7.85m** / pnl RECOVERY · **WZC Sint-Carolus Ternat** omzet JUMP **10.16m** / pnl JUMP · **WZC De Foyer Gent** omzet JUMP **19.03m** / thin equity · **Karus** omzet JUMP **70.08m** / pnl JUMP · **WZC St Vincentius Antwerpen/Ekeren** omzet JUMP **7.55m** / pnl JUMP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; partial **~{n_part}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych/zorgkas shells** (**NEW 2021-2030** Avelgem · PPC Pittem · Maria Ingelmunster · **Evara/Multiversum** · Mayerhof · Zilverbos · Ternat · De Foyer · Karus · **St Vincentius Antwerpen** · prior PC Sint-Hiëronymus/HH Lier/Sint-Andries/Sint-Trudo/HH Leuven/HH Tienen/AZ Zeno/AZ Rivierenland/PC Gent-Sleidinge/WZC Sint-Barbara/Zorgkas/OLVT/AZ Oostende stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2030)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_comm} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {n_ready} |
| FOI answered | {n_ans} |
| FOI partial | {n_part} |
| FOI total rows | {n_foi} |
| research_queue open | rq_2031 after progress |

### What improved since tick 2020

- **Residual dual (tick2021-2030):** **WZC Sint-Vincentius Avelgem** · **PPC Pittem** · **Maria Rustoord Ingelmunster** · **Evara/Multiversum** · **Sint Carolus Mayerhof** · **WZC Zilverbos Zelzate** · **WZC Sint-Carolus Ternat** · **WZC De Foyer Gent** · **Karus** · **WZC St Vincentius Antwerpen/Ekeren** (this tick EVERY-10 dual — Antwerpen WZC VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · Jessa/ZOL CW N/A omzet · Erasme/UZ Brussel CW opaque · AZ Sint-Lucas / Groeninge / Zottegem / Turnhout / Waregem / Yperman / Maria Middelares / Imelda / Monica CW N/A omzet · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack. **Deferred live:** OLV Lourdes Kortenberg · OLVA Antwerpen · Kanunnik Triest.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2040**.


"""
if "## Snapshot at **tick 2030**" not in prog_text:
    anchor = "## Snapshot at **tick 2020**"
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text + "\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has tick 2030")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2030** (2026-08-24) · **{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 2021-2030:** **Evara/Multiversum omzet 443.17m** · **Karus omzet 70.08m** · **PPC Pittem omzet 42.45m** · **WZC De Foyer omzet 19.03m** · **Maria Ingelmunster omzet 11.64m** · **Sint Carolus Mayerhof omzet 11.46m** · **WZC Sint-Carolus Ternat omzet 10.16m** · **WZC Zilverbos omzet 7.85m** · **WZC St Vincentius Antwerpen omzet 7.55m** · **WZC Sint-Vincentius Avelgem omzet 7.49m** · prior PC Sint-Hiëronymus/HH Lier/AZ Rivierenland/Sint-Trudo/HH Tienen/Sint-Andries/HH Leuven/AZ Zeno/PC Gent-Sleidinge/WZC Sint-Barbara/Zorgkas stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2020:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 2021-2030 (off pure top10 / dual):** Avelgem · PPC Pittem · Maria Ingelmunster · **Evara/Multiversum** · Mayerhof · Zilverbos · Ternat · De Foyer · Karus · **St Vincentius Antwerpen/Ekeren** (EVERY-10 dual). Count NEW since 2020: 10 residual dual ticks. **Prior PC Sint-Hiëronymus/hospital stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_2030":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after Karus — WZC St Vincentius Antwerpen/Ekeren YE2025 Medium"
        x["notes"] = (
            "tick2030 EVERY-10 + WZC St Vincentius Antwerpen Medium omzet JUMP 7.55m pnl JUMP 0.43m equity JUMP 12.45m; FOI ready; "
            "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2031; next every-10 2040"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover WZC St Vincentius Antwerpen/Ekeren YE2025 Medium CW; KBO 0418.016.550; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2031" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2031",
            "title": "leftover dual hole-fill after WZC St Vincentius Antwerpen EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2030 EVERY-10 after WZC St Vincentius Antwerpen/Ekeren YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (OLV Lourdes Kortenberg YE2025 live deferred / OLVA Antwerpen YE2025 / Kanunnik Triest YE2025 / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC St Vincentius Antwerpen/Ekeren, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2030 EVERY-10 St Vincentius Antwerpen; next every-10 2040; Lourdes/OLVA/Triest YE2025 deferred",
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
        "last_unit_id": "rq_2030",
        "ticks_completed": "2030",
        "paused": "no",
        "notes": (
            "tick2030 EVERY-10 + leftover WZC St Vincentius Antwerpen/Ekeren 0418.016.550 Medium CW (omzet JUMP 7.55m pnl JUMP 0.43m equity JUMP 12.45m bruto JUMP 7.36m FTE 89.8; "
            "assets/debt Unknown); progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2031; next every-10 2040; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2030 - {UTC} - rq_2030 EVERY-10 + WZC St Vincentius Antwerpen/Ekeren (omzet JUMP 7.55m / pnl JUMP 0.43m / Medium)

- Unit: **rq_2030** EVERY-10 mandatory + leftover dual after **rq_2029 Karus**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **WZC St Vincentius Antwerpen/Ekeren** YE2025 (KBO **0418.016.550**; Dorpstraat 32 Ekeren; Antwerpen **WZC VZW**). Distinct from Avelgem. Lourdes/OLVA/Kanunnik Triest YE2025 also live — deferred. Do not redo Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2030 snapshot; residual dual 2021-2030) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,550,039** JUMP +1.54%; pnl **EUR427,313** JUMP +21.50%; equity **EUR12,448,629** JUMP +1.19%; bruto **EUR7,362,184** JUMP +1.87%; FTE **89.8**; neerlegging **17.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 2 VE; email info@vincentiusekeren.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_st_vincentius_antwerpen); foi + draft {GAP}; progress+top10; rq_2030=done + rq_2031 open; loop_state ticks=2030; raw under docs/doge/data/raw/tick2030/.
- FOI: **ready not sent** (human-gated; info@vincentiusekeren.be).
- EVERY-10 done. Next every-10 **2040**. Next: rq_2031 (AGB/FARO-if-YE2025 / AIESH-REW / Lourdes-OLVA-Triest / unused DSO-IGS-HVZ).

### Every-10 brief (A/B/C/D/E)
- **A** L0 TE: **100%** (EUR347.956bn Strong)
- **B** L1 subsectors: **100%** unconsol map
- **C** L2 entities: **~99%** order-of-magnitude
- **D** L5 end-receivers: **~74-88%** generous; +10 residual dual 2021-2030 (WZC/psych/zorggroep) — **not** near-complete of 348bn
- **E** FOI-ready: **~{n_ready}** drafts; answered ~{n_ans}; partial ~{n_part}
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
