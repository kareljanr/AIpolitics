# ephemeral tick2000 — EVERY-10 + AZ Delta YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T03:50:00Z"
ENTITY = "vzw_az_delta"
GAP = "gap_az_delta_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_az_delta_jr2025_cw"
SRC_EN = "src_az_delta_jr2025_cw_en"
SRC_FR = "src_az_delta_jr2025_cw_fr"
SRC_KBO = "src_az_delta_kbo_2000"
SRC_SITE = "src_az_delta_site_2000"

OMZET = "739723776"
PNL = "8653379"
EQUITY = "430457306"
BRUTO = "341774840"
FTE = "3481.4"
OMZET24 = "702277943"
PNL24 = "8359915"
EQUITY24 = "431794675"
BRUTO24 = "327733659"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2000")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ Delta YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0505931808/algemeen-ziekenhuis-delta",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2000 EVERY-10; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 29.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2000/delta_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ Delta YE2025 statutory",
        "url": "https://www.companyweb.be/en/0505931808/algemeen-ziekenhuis-delta",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2000 EVERY-10; EN mirror YE2025 Medium; filed 29-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2000/delta_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ Delta YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0505931808/algemeen-ziekenhuis-delta",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2000 EVERY-10; FR mirror YE2025 Medium; deposés le 29-07-2026; raw docs/doge/data/raw/tick2000/delta_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ Delta 0505.931.808 Actief VZW Roeselare",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0505931808",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2000 EVERY-10; Actief VZW since 04.12.2014; Algemeen Ziekenhuis Delta; Deltalaan 1 8800 Roeselare; no KBO email; 6 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azdelta.be Algemeen Ziekenhuis Delta",
        "url": "https://www.azdelta.be/",
        "publisher": "AZ Delta",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2000 EVERY-10; West-Flanders multi-campus hospital; contact via azdelta.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_delta_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2000 EVERY-10; omzet JUMP {OMZET} +5.33pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_az_delta_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2000 EVERY-10; pnl JUMP {PNL} +3.51pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_az_delta_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2000 EVERY-10; equity DROP {EQUITY} -0.31pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_az_delta_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2000 EVERY-10; bruto JUMP {BRUTO} +4.28pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_az_delta_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2000 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_delta_jr2025_statutory_hospital",
    "title": "AZ Delta YE2025 EVERY-10 leftover hospital dual (omzet JUMP 739.72m / pnl JUMP 8.65m / equity DROP 430.46m)",
    "entity_id": ENTITY,
    "beneficiary": "West-Flanders hospital patients / Algemeen Ziekenhuis Delta",
    "legal_basis": "VZW/ASBL hospital (KBO 0505.931.808)",
    "decision_date": "2026-07-29",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0505931808/algemeen-ziekenhuis-delta",
    "stated_goal": "Multi-campus general hospital care (Roeselare/Menen/Torhout)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>AZ_Delta>JR2025_statutory_L5",
    "notes": "tick2000 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AZ Groeninge CW N/A; AZJP already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*7.5 + 0.35*5.5 + 0.10*4.0 = 4.125+1.925+0.4 = 6.45
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_delta_omzet_jump_739_72m_pnl_jump_8_65m_equity_drop_jr2025",
    "name": "AZ Delta omzet JUMP 739.72m / pnl JUMP 8.65m / equity DROP 430.46m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "WestVlaanderen>AZ_Delta>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "West-Flanders patients via AZ Delta VZW",
    "stated_goal": "Multi-campus hospital care",
    "measured_outcome": "Medium CW YE2025; 739.72m omzet JUMP +5.33pct with stable profit JUMP +3.51pct and mild equity DROP -0.31pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.45",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon vs ZAS/CHIREC/Saint-Luc hospital continuum",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2000 EVERY-10 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ Delta / Algemeen Ziekenhuis Delta",
    "name_fr": "AZ Delta / Algemeen Ziekenhuis Delta",
    "name_en": "AZ Delta / Algemeen Ziekenhuis Delta (Roeselare)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azdelta.be/",
    "foi_email": "",
    "foi_postal": "Deltalaan 1, 8800 Roeselare",
    "notes": "tick2000 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0505.931.808 Actief VZW; omzet JUMP 739.72m pnl JUMP 8.65m equity DROP 430.46m bruto JUMP 341.77m FTE 3481.4; assets/debt Unknown; neerlegging 29.07.2026; 6 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; do not redo AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "WestVlaanderen>AZ_Delta>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash)",
    "why_it_matters": "Medium CW shows 739.72m omzet West-Flanders hospital VZW without balance sheet",
    "priority": "7",
    "recipient_body": "Algemeen Ziekenhuis Delta VZW / AZ Delta",
    "recipient_email": "",
    "recipient_postal": "Deltalaan 1, 8800 Roeselare",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_delta_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_delta_omzet_jump_739_72m_pnl_jump_8_65m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2000 EVERY-10; human-send only; Medium CW; route via azdelta.be (no KBO email); next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ Delta (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Algemeen Ziekenhuis Delta VZW / AZ Delta — KBO **0505.931.808**  
**recipient:** route via azdelta.be (no KBO email) · Deltalaan 1, 8800 Roeselare  
**sources:** [CW NL](https://www.companyweb.be/nl/0505931808/algemeen-ziekenhuis-delta) · [CW EN](https://www.companyweb.be/en/0505931808/algemeen-ziekenhuis-delta) · [CW FR](https://www.companyweb.be/fr/0505931808/algemeen-ziekenhuis-delta) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0505931808) · [site](https://www.azdelta.be/)  
**tick:** 2000  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **29.07.2026**): omzet **EUR739,723,776** JUMP +5.33%; pnl **EUR8,653,379** JUMP +3.51%; equity **EUR430,457,306** DROP −0.31%; bruto **EUR341,774,840** JUMP +4.28%; FTE **3481.4**; assets/debt **Unknown**.
- West-Flanders multi-campus VZW hospital. Preferred stall: AGB Bornem / FARO still YE2024. AZJP already mined. AZ Groeninge CW N/A omzet.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Algemeen Ziekenhuis Delta VZW / AZ Delta — Deltalaan 1, 8800 Roeselare
via azdelta.be openbaarheid / contact
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZ Delta + balans (KBO 0505.931.808)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 29.07.2026).
2. Assets / schulden LT-ST / cash.
3. Dual vs ZAS / CHIREC / regionale VL ziekenhuizen indien relevant.
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

# EVERY-10 progress refresh
progress = Path("docs/doge/data/progress_every_10_ticks.md")
prog_text = progress.read_text(encoding="utf-8")
snapshot = f"""## Snapshot at **tick 2000** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1991-2000 hospital continuum after 1990 CHIREC |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1991-2000 is residual dual L5 (not near-complete of 348bn):** **Humani** omzet JUMP **662.29m** / pnl LOSS · **GHdC** omzet JUMP **550.35m** / pnl LOSS · **Saint-Luc** omzet JUMP **857.94m** / pnl LOSS / equity DROP · **CHBA** omzet JUMP **183.56m** · **Haute Senne** omzet JUMP **126.74m** / pnl DROP · **CNDG** omzet JUMP **149.61m** / pnl DROP · **CHR Verviers** omzet JUMP **251.76m** · **ZAS** omzet JUMP **1370.34m** / pnl LOSS · **AZJP** omzet JUMP **126.33m** / pnl LOSS · **AZ Delta** omzet JUMP **739.72m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; partial **~{n_part}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital shells** (**NEW 1991-2000** Humani · GHdC · Saint-Luc · CHBA · Haute Senne · CNDG · CHR Verviers · **ZAS** · AZJP · **AZ Delta** · prior CHIREC/Citadelle/ISoSL/Tivoli/Epicura/CHwapi/CHU UCL Namur/Vivalia/SPI/IDETA stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2000)

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
| research_queue open | rq_2001 after progress |

### What improved since tick 1990

- **Residual dual (tick1991-2000):** **Humani** · **GHdC** · **Saint-Luc** · **CHBA** · **Haute Senne** · **CNDG** · **CHR Verviers** · **ZAS** · **AZJP** · **AZ Delta** (this tick EVERY-10 dual — West-Flanders hospital VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · Erasme/UZ Brussel CW opaque · AZ Sint-Lucas Gent/Brugge CW N/A omzet · AZ Groeninge CW N/A omzet · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2010**.


"""
if "## Snapshot at **tick 2000**" not in prog_text:
    # insert after header block (after first --- following How to read)
    anchor = "## Snapshot at **tick 1990**"
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text + "\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has tick 2000")

# EVERY-10 waste top10 refresh
top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2000** (2026-08-24) · **{n_lb}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1991-2000:** **ZAS omzet 1370.34m** · **AZ Delta omzet 739.72m** · **Saint-Luc omzet 857.94m** · **Humani omzet 662.29m** · **GHdC omzet 550.35m** · **CHR Verviers omzet 251.76m** · **CHBA omzet 183.56m** · **CNDG omzet 149.61m** · **Haute Senne omzet 126.74m** · **AZJP omzet 126.33m** · prior **CHIREC equity 457.59m** · prior Citadelle/ISoSL/Tivoli/Epicura/CHwapi/CHU UCL Namur/Vivalia/SPI/IDETA · prior **IDELUX Finances / IFIGA / SOFILUX / HELORA** · prior **nuclear / Fluxys / Elia / Enodia / RESA** · prior Publi-T/Publigas/Nethys/Virya · prior **Eneco continuum** · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1990:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 1991-2000 (off pure top10 / dual):** Humani · GHdC · Saint-Luc · CHBA · Haute Senne · CNDG · CHR Verviers · **ZAS** · AZJP · **AZ Delta** (EVERY-10 dual). Count NEW since 1990: 10 residual dual ticks. **Prior CHIREC/Citadelle/IDELUX Finances stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_2000":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after AZJP — AZ Delta YE2025 Medium"
        x["notes"] = (
            "tick2000 EVERY-10 + AZ Delta Medium omzet JUMP 739.72m pnl JUMP 8.65m equity DROP 430.46m; FOI ready; "
            "progress+top10 refreshed; next rq_2001; next every-10 2010"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover AZ Delta YE2025 Medium CW; KBO 0505.931.808; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2001" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2001",
            "title": "leftover dual hole-fill after AZ Delta EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2000 EVERY-10 after AZ Delta YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Sint-Jan Brugge / AZ Turnhout / other unused YE2025 if live). "
                "Do NOT redo AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2000 EVERY-10 AZ Delta; next every-10 2010",
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
        "last_unit_id": "rq_2000",
        "ticks_completed": "2000",
        "paused": "no",
        "notes": (
            "tick2000 EVERY-10 + leftover AZ Delta 0505.931.808 Medium CW (omzet JUMP 739.72m pnl JUMP 8.65m equity DROP 430.46m bruto JUMP 341.77m FTE 3481.4; "
            "assets/debt Unknown); progress+top10 refreshed; AGB Bornem JR2024; FARO YE2024; next rq_2001; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2000 - {UTC} - rq_2000 EVERY-10 + AZ Delta (omzet JUMP 739.72m / pnl JUMP 8.65m / Medium)

- Unit: **rq_2000** EVERY-10 mandatory + leftover dual after **rq_1999 AZJP**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. AZ Groeninge CW N/A omzet. Took unused leftover **AZ Delta** YE2025 (KBO **0505.931.808**; Deltalaan 1 Roeselare; West-Flanders **hospital VZW**). Do not redo AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2000 snapshot; residual dual 1991-2000) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR739,723,776** JUMP +5.33%; pnl **EUR8,653,379** JUMP +3.51%; equity **EUR430,457,306** DROP −0.31%; bruto **EUR341,774,840** JUMP +4.28%; FTE **3481.4**; neerlegging **29.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 6 VE; no KBO email (route via azdelta.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_delta); foi + draft {GAP}; progress+top10; rq_2000=done + rq_2001 open; loop_state ticks=2000; raw under docs/doge/data/raw/tick2000/.
- FOI: **ready not sent** (human-gated; route via azdelta.be).
- EVERY-10 done. Next every-10 **2010**. Next: rq_2001 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
