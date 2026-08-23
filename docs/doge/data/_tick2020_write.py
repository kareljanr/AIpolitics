# ephemeral tick2020 — EVERY-10 + WZC Sint-Vincentius Avelgem YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T09:50:00Z"
ENTITY = "vzw_wzc_sint_vincentius_avelgem"
GAP = "gap_wzc_sint_vincentius_avelgem_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_wzc_sint_vincentius_avelgem_jr2025_cw"
SRC_EN = "src_wzc_sint_vincentius_avelgem_jr2025_cw_en"
SRC_FR = "src_wzc_sint_vincentius_avelgem_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_vincentius_avelgem_kbo_2020"
SRC_SITE = "src_wzc_sint_vincentius_avelgem_site_2020"

OMZET = "7493161"
PNL = "74613"
EQUITY = "7303884"
BRUTO = "8116678"
FTE = "103.3"
OMZET24 = "7321405"
PNL24 = "88563"
EQUITY24 = "7421209"
BRUTO24 = "7938462"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2020")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2020 EVERY-10; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2020/sint_vincentius_avelgem.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2020 EVERY-10; EN mirror YE2025 Medium; filed 10-06-2026; Last balance sheet year 2025; FTE 103.3; raw docs/doge/data/raw/tick2020/sint_vincentius_avelgem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Vincentius Avelgem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0420504403/woon-en-zorgcentrum-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2020 EVERY-10; FR mirror YE2025 Medium; déposés le 10-06-2026; raw docs/doge/data/raw/tick2020/sint_vincentius_avelgem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woon- en Zorgcentrum Sint-Vincentius 0420.504.403 Actief VZW Avelgem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420504403",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2020; Actief VZW since 29.01.1980; Bevrijdingslaan 18 8580 Avelgem; 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "vincentiusavelgem.be WZC Sint-Vincentius Avelgem",
        "url": "https://www.vincentiusavelgem.be/",
        "publisher": "WZC Sint-Vincentius Avelgem",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2020; info@vincentiusavelgem.be; Bevrijdingslaan 18 8580 Avelgem",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2020 EVERY-10; omzet JUMP {OMZET} +2.35pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2020 EVERY-10; pnl DROP {PNL} -15.75pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2020 EVERY-10; equity DROP {EQUITY} -1.58pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2020 EVERY-10; bruto JUMP {BRUTO} +2.24pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_vincentius_avelgem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2020 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_vincentius_avelgem_jr2025_statutory_wzc",
    "title": "WZC Sint-Vincentius Avelgem YE2025 EVERY-10 leftover dual (omzet JUMP 7.49m / pnl DROP 75k / equity DROP 7.30m)",
    "entity_id": ENTITY,
    "beneficiary": "Avelgem elderly care residents / WZC Sint-Vincentius",
    "legal_basis": "VZW/ASBL WZC (KBO 0420.504.403)",
    "decision_date": "2026-06-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius",
    "stated_goal": "Residential elderly care (Avelgem)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>JR2025_statutory_L5",
    "notes": "tick2020 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024; St Vincentius Antwerpen YE2024-only; Maria Ingelmunster YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 1.925 + 1.75 + 0.6 = 4.275
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_vincentius_avelgem_omzet_jump_7_49m_pnl_drop_75k_jr2025",
    "name": "WZC Sint-Vincentius Avelgem omzet JUMP 7.49m / pnl DROP 75k / equity DROP 7.30m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Avelgem elderly via WZC Sint-Vincentius VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.49m omzet JUMP +2.35pct with pnl DROP -15.75pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.275",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2020 EVERY-10 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon- en Zorgcentrum Sint-Vincentius (Avelgem)",
    "name_fr": "Maison de repos Sint-Vincentius (Avelgem)",
    "name_en": "WZC Sint-Vincentius Avelgem (elderly care)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.vincentiusavelgem.be/",
    "foi_email": "info@vincentiusavelgem.be",
    "foi_postal": "Bevrijdingslaan 18, 8580 Avelgem",
    "notes": "tick2020 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0420.504.403 Actief VZW; omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m bruto JUMP 8.12m FTE 103.3; assets/debt Unknown; neerlegging 10.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024; St Vincentius Antwerpen YE2024-only; Maria Ingelmunster YE2025 deferred; do not redo WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS",
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
    "hierarchy_path": "WestVlaanderen>WZC_Sint_Vincentius_Avelgem>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split",
    "why_it_matters": "Medium CW shows 7.49m omzet Avelgem WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "Woon- en Zorgcentrum Sint-Vincentius vzw",
    "recipient_email": "info@vincentiusavelgem.be",
    "recipient_postal": "Bevrijdingslaan 18, 8580 Avelgem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_vincentius_avelgem_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_sint_vincentius_avelgem_omzet_jump_7_49m_pnl_drop_75k_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2020 EVERY-10; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Vincentius Avelgem (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en Zorgcentrum Sint-Vincentius vzw — KBO **0420.504.403**  
**recipient:** info@vincentiusavelgem.be · Bevrijdingslaan 18, 8580 Avelgem  
**sources:** [CW NL](https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius) · [CW EN](https://www.companyweb.be/en/0420504403/woon-en-zorgcentrum-sint-vincentius) · [CW FR](https://www.companyweb.be/fr/0420504403/woon-en-zorgcentrum-sint-vincentius) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420504403) · [site](https://www.vincentiusavelgem.be/)  
**tick:** 2020 EVERY-10  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.06.2026**): omzet **EUR7,493,161** JUMP +2.35%; pnl **EUR74,613** DROP −15.75%; equity **EUR7,303,884** DROP −1.58%; bruto **EUR8,116,678** JUMP +2.24%; FTE **103.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO NBB YE2025 unpublished; AIESH/REW YE2024. St Vincentius Antwerpen YE2024-only. Maria Rustoord Ingelmunster YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentrum Sint-Vincentius vzw — Bevrijdingslaan 18, 8580 Avelgem
info@vincentiusavelgem.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Vincentius Avelgem + balans (KBO 0420.504.403)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.06.2026).
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
snapshot = f"""## Snapshot at **tick 2020** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2011-2020 hospital/WZC continuum after 2010 Vlaamse Zorgkas |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2011-2020 is residual dual L5 (not near-complete of 348bn):** **Heilig Hart Lier** omzet JUMP **204.49m** / pnl LOSS · **Sint-Andries Tielt** omzet JUMP **132.31m** / pnl DROP · **Sint-Trudo** omzet JUMP **181.32m** / pnl DROP · **Heilig Hart Leuven** omzet JUMP **118.73m** / pnl COLLAPSE · **Heilig Hart Tienen** omzet JUMP **138.50m** / pnl DROP · **AZ Zeno** omzet JUMP **64.65m** / pnl JUMP · **AZ Rivierenland** omzet JUMP **208.26m** / pnl LOSS · **PC Gent-Sleidinge** omzet JUMP **41.00m** / pnl JUMP · **WZC Sint-Barbara Herselt** omzet JUMP **15.24m** / pnl DROP · **WZC Sint-Vincentius Avelgem** omzet JUMP **7.49m** / pnl DROP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; partial **~{n_part}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/zorgkas/psych shells** (**NEW 2011-2020** Heilig Hart Lier · Sint-Andries Tielt · Sint-Trudo · Heilig Hart Leuven · Heilig Hart Tienen · AZ Zeno · AZ Rivierenland · PC Gent-Sleidinge · WZC Sint-Barbara Herselt · **WZC Sint-Vincentius Avelgem** · prior Vlaamse Zorgkas/OLVT/AZ Oostende/Glorieux/Alma/Herentals/Vitaz/Emmaüs/AZORG/Z.org/ZAS/AZ Delta stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2020)

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
| research_queue open | rq_2021 after progress |

### What improved since tick 2010

- **Residual dual (tick2011-2020):** **Heilig Hart Lier** · **Sint-Andries Tielt** · **Sint-Trudo** · **Heilig Hart Leuven** · **Heilig Hart Tienen** · **AZ Zeno** · **AZ Rivierenland** · **PC Gent-Sleidinge** · **WZC Sint-Barbara Herselt** · **WZC Sint-Vincentius Avelgem** (this tick EVERY-10 dual — West-Flanders WZC VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · St Vincentius Antwerpen YE2024-only · Erasme/UZ Brussel CW opaque · AZ Sint-Lucas / Groeninge / Zottegem / Turnhout / Waregem / Yperman / Maria Middelares / Imelda / Monica / Jessa / ZOL / SFZ / Noorderhart CW N/A omzet · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack. **Deferred live:** Maria Rustoord Ingelmunster YE2025.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2030**.


"""
if "## Snapshot at **tick 2020**" not in prog_text:
    anchor = "## Snapshot at **tick 2010**"
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text + "\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has tick 2020")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2020** (2026-08-24) · **{n_lb}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 2011-2020:** **Heilig Hart Lier omzet 204.49m** · **AZ Rivierenland omzet 208.26m** · **Sint-Trudo omzet 181.32m** · **Heilig Hart Tienen omzet 138.50m** · **Sint-Andries Tielt omzet 132.31m** · **Heilig Hart Leuven omzet 118.73m** · **AZ Zeno omzet 64.65m** · **PC Gent-Sleidinge omzet 41.00m** · **WZC Sint-Barbara Herselt omzet 15.24m** · **WZC Sint-Vincentius Avelgem omzet 7.49m** · prior **Vlaamse Zorgkas/OLVT/AZ Oostende/Glorieux/Alma/Herentals/Vitaz/Emmaüs/AZORG/Z.org/ZAS/AZ Delta** stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2010:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 2011-2020 (off pure top10 / dual):** Heilig Hart Lier · Sint-Andries Tielt · Sint-Trudo · Heilig Hart Leuven · Heilig Hart Tienen · AZ Zeno · AZ Rivierenland · PC Gent-Sleidinge · WZC Sint-Barbara Herselt · **WZC Sint-Vincentius Avelgem** (EVERY-10 dual). Count NEW since 2010: 10 residual dual ticks. **Prior Vlaamse Zorgkas/hospital stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_2020":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after WZC Sint-Barbara Herselt — WZC Sint-Vincentius Avelgem YE2025 Medium"
        x["notes"] = (
            "tick2020 EVERY-10 + WZC Sint-Vincentius Avelgem Medium omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m; FOI ready; "
            "progress+top10 refreshed; AGB Bornem JR2024; FARO YE2024; Maria Ingelmunster YE2025 deferred; next rq_2021; next every-10 2030"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover WZC Sint-Vincentius Avelgem YE2025 Medium CW; KBO 0420.504.403; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2021" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2021",
            "title": "leftover dual hole-fill after WZC Sint-Vincentius Avelgem EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2020 EVERY-10 after WZC Sint-Vincentius Avelgem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Maria Rustoord Ingelmunster YE2025 live deferred / Sint-Carolus / Zilverbos / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC Sint-Vincentius Avelgem, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count. St Vincentius Antwerpen still YE2024-only."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2020 EVERY-10 WZC Sint-Vincentius Avelgem; next every-10 2030; Maria Ingelmunster YE2025 deferred",
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
        "last_unit_id": "rq_2020",
        "ticks_completed": "2020",
        "paused": "no",
        "notes": (
            "tick2020 EVERY-10 + leftover WZC Sint-Vincentius Avelgem 0420.504.403 Medium CW (omzet JUMP 7.49m pnl DROP 75k equity DROP 7.30m bruto JUMP 8.12m FTE 103.3; "
            "assets/debt Unknown); progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; next rq_2021; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2020 - {UTC} - rq_2020 EVERY-10 + WZC Sint-Vincentius Avelgem (omzet JUMP 7.49m / pnl DROP 75k / Medium)

- Unit: **rq_2020** EVERY-10 mandatory + leftover dual after **rq_2019 WZC Sint-Barbara Herselt**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO NBB YE2025 still **unpublished** (YE2024 filing); AIESH/REW still **YE2024**. St Vincentius Antwerpen still **YE2024-only**. Took unused leftover **WZC Sint-Vincentius Avelgem** YE2025 (KBO **0420.504.403**; Bevrijdingslaan 18 Avelgem; West-Vlaanderen **WZC VZW**). Maria Rustoord Ingelmunster YE2025 also live — deferred. Do not redo WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2020 snapshot; residual dual 2011-2020) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,493,161** JUMP +2.35%; pnl **EUR74,613** DROP −15.75%; equity **EUR7,303,884** DROP −1.58%; bruto **EUR8,116,678** JUMP +2.24%; FTE **103.3**; neerlegging **10.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@vincentiusavelgem.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_vincentius_avelgem); foi + draft {GAP}; progress+top10; rq_2020=done + rq_2021 open; loop_state ticks=2020; raw under docs/doge/data/raw/tick2020/.
- FOI: **ready not sent** (human-gated; info@vincentiusavelgem.be).
- EVERY-10 done. Next every-10 **2030**. Next: rq_2021 (AGB/FARO-if-YE2025 / AIESH-REW / Maria Ingelmunster / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
