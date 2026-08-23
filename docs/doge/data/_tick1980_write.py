# ephemeral tick1980 — EVERY-10 + IDELUX Finances YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T22:30:00Z"
ENTITY = "igs_idelux_finances"
GAP = "gap_idelux_fin_nbb_pdf_assets_debt_omzet_drop_bruto_neg_matrix_l5"
SRC = "src_idelux_fin_jr2025_cw"
SRC_EN = "src_idelux_fin_jr2025_cw_en"
SRC_KBO = "src_idelux_fin_kbo_1980"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1980")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL IDELUX Finances YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0258258738/idelux-finances",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1980; YE2025 omzet DROP 644147 pnl JUMP 1026516 equity JUMP 36065604 bruto NEG -675994 FTE 0; neerlegging 19.06.2026; raw docs/doge/data/raw/tick1980/idelux_fin_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN IDELUX Finances YE2025 statutory",
        "url": "https://www.companyweb.be/en/0258258738/idelux-finances",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1980; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1980/idelux_fin_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO IDELUX Finances 0258.258.738 Actief CV Arlon",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0258258738",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1980; Actief CV; Schoppach dreve de l Arc-en-Ciel 98 6700 Arlon; email officiel.ic-ideluxfinances@idelux.be; Aanbestedende overheid; NACE 68.203/64.929/64.910",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_idelux_fin_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "644147",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1980; omzet DROP 644147 -78.85pct vs YE2024 3045931",
    },
    {
        "budget_id": "bud_idelux_fin_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1026516",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1980; pnl JUMP 1026516 +31.69pct vs YE2024 779467",
    },
    {
        "budget_id": "bud_idelux_fin_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "36065604",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1980; equity JUMP 36065604 +1.47pct vs YE2024 35543360",
    },
    {
        "budget_id": "bud_idelux_fin_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "-675994",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge NEG",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1980; bruto NEG -675994 swing -139.41pct vs YE2024 +1715314",
    },
    {
        "budget_id": "bud_idelux_fin_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "0",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1980; YE2025 FTE 0 financing/real-estate shell",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_idelux_fin_jr2025_statutory_ipf",
    "title": "IDELUX Finances YE2025 leftover Luxembourg economic-equipment financing dual (omzet DROP 0.644m / bruto NEG 0.676m)",
    "entity_id": ENTITY,
    "beneficiary": "Luxembourg province communes + IDELUX group dual",
    "legal_basis": "Code democratie locale intercommunale financement CV",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1026516",
    "cash_by_year": '{"2025_omzet":644147,"2025_pnl":1026516,"2025_equity":36065604,"2025_bruto":-675994,"2025_fte":0}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0258258738/idelux-finances",
    "stated_goal": "Intercommunale financing/real-estate vehicle for Luxembourg economic equipment",
    "cut_option": "Publish NBB PDF assets/debt + omzet DROP recon + bruto NEG swing FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Finances>JR2025_statutory_L5",
    "notes": "tick1980 EVERY-10 dual; Medium CW; assets/debt Unknown; dual of IDELUX Environnement/Eau; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_idelux_fin_omzet_drop_0_644m_bruto_neg_0_676m_jr2025",
    "name": "IDELUX Finances omzet DROP 0.644m / bruto NEG 0.676m / equity JUMP 36.07m (Luxembourg economic financing YE2025)",
    "level": "L5",
    "type": "walloon_igs_financing_realestate_dual",
    "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Finances>JR2025_statutory_L5",
    "annual_cost_eur": "1026516",
    "total_cost_eur": "36065604",
    "tco_notes": "statutory omzet DROP 644147 pnl JUMP 1026516 equity JUMP 36065604 bruto NEG -675994 FTE 0; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Luxembourg communes via IDELUX Finances shell",
    "stated_goal": "Municipal financing/real-estate vehicle for economic equipment",
    "measured_outcome": "Medium CW YE2025; FTE 0 shell; omzet collapse -79pct; bruto flipped to NEG; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "3.5",
    "difficulty": "3.0",
    "priority_index": "4.55",
    "cut_proposal": "Publish NBB PDF + omzet DROP / bruto NEG recon + dual vs IDELUX Env/Eau FOI; scrutinise zero-FTE 36m equity shell",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1980 EVERY-10 leftover dual; Medium CW; not TE-additive pure-waste top10",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "IDELUX Finances (Luxembourg economic-equipment financing)",
    "name_fr": "IDELUX Finances (financement equipement economique Luxembourg)",
    "name_en": "IDELUX Finances (Luxembourg economic equipment financing IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.idelux.be/",
    "foi_email": "officiel.ic-ideluxfinances@idelux.be",
    "foi_postal": "Schoppach, dreve de l'Arc-en-Ciel 98, 6700 Arlon",
    "notes": "tick1980 YE2025 Medium CW NL+EN + Strong KBO 0258.258.738 Actief CV; omzet DROP 0.644m pnl JUMP 1.027m equity JUMP 36.07m bruto NEG 0.676m FTE 0; assets/debt Unknown; neerlegging 19.06.2026; dual IDELUX Environnement/Eau; FOI gap_idelux_fin_nbb_pdf_assets_debt_omzet_drop_bruto_neg_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/IPALLE/INTRADEL/TIBI/IPFBW",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Finances>NBB_PDF_assets_debt_omzet_bruto",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet DROP -79pct recon; bruto NEG swing recon; dual vs IDELUX Environnement/Eau / SOFILUX",
    "why_it_matters": "Medium CW shows FTE-0 shell with 36m equity, omzet collapse and bruto flip to NEG without balance sheet",
    "priority": "6",
    "recipient_body": "IDELUX Finances",
    "recipient_email": "officiel.ic-ideluxfinances@idelux.be",
    "recipient_postal": "https://www.idelux.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_idelux_fin_jr2025_statutory_ipf",
    "linked_leaderboard_id": "lb_idelux_fin_omzet_drop_0_644m_bruto_neg_0_676m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1980 EVERY-10; human-send only; Medium CW; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — IDELUX Finances (NBB PDF / assets-debt / omzet DROP / bruto NEG)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** IDELUX Finances CV — KBO **0258.258.738**  
**recipient:** officiel.ic-ideluxfinances@idelux.be  
**sources:** [CW NL](https://www.companyweb.be/nl/0258258738/idelux-finances) · [CW EN](https://www.companyweb.be/en/0258258738/idelux-finances) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0258258738)  
**tick:** 1980  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **19.06.2026**): omzet **EUR644,147** DROP -78.85%; pnl **EUR1,026,516** JUMP +31.69%; equity **EUR36,065,604** JUMP +1.47%; bruto **NEG EUR-675,994** (swing from +1.715m); FTE **0**; assets/debt **Unknown**.
- Luxembourg economic-equipment financing intercommunale (dual IDELUX Environnement/Eau). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: IDELUX Finances — officiel.ic-ideluxfinances@idelux.be
Schoppach, dreve de l'Arc-en-Ciel 98, 6700 Arlon
cc: IDELUX group / SPW transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 IDELUX Finances + balans + omzet/bruto recon (KBO 0258.258.738)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 19.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon omzet DROP (-79pct vs YE2024 3.05m).
4. Recon bruto NEG swing (-0.676m vs +1.715m YE2024).
5. Dual vs IDELUX Environnement / Eau / SOFILUX indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# inventory for progress
n_bud = len(brows)
n_cmt = len(crows)
n_lb = len(lrows)
n_ent = len(erows)
n_src = len(srows)
foi_ready = sum(1 for x in frows if (x.get("status") or "").lower() == "ready")
foi_ans = sum(1 for x in frows if (x.get("status") or "").lower() == "answered")
foi_part = sum(1 for x in frows if (x.get("status") or "").lower() == "partial")
foi_tot = len(frows)

# progress + top10
prog = Path("docs/doge/data/progress_every_10_ticks.md")
old = prog.read_text(encoding="utf-8")
snap = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## How to read the % figures

| Layer | Meaning | “End stop of money”? |
|-------|---------|----------------------|
| **A. L0 total** | Official GG TE known | No — single top line |
| **B. L1 subsector** | TE split federal / SS / state / local | No — still aggregates |
| **C. L2 entity totals** | Named institutions with primary budget totals (De Lijn, FOREM, ORES, …) | **Partial** — who holds the money |
| **D. L5 end-receivers** | Named third party / project / ASBL / firm with € | **Yes** — where possible |
| **E. FOI residual** | Known gap, draft ready for human send | Tracked, not yet answered |

**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).

---

## Snapshot at **tick 1980** (2026-08-23)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1971-1980 BEP/HYGEA/ORES-IPF/IDELUX continuum after 1970 IBH |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1971-1980 is residual dual L5 (not near-complete of 348bn):** **BEP NAMUR** omzet DROP **3.85m** · **LOGIPOLE** omzet JUMP **24.82m** · **BEP Environnement** omzet DROP **25.69m** · **FINEST** pnl DROP **2.65m** / equity JUMP **64.64m** · **HYGEA** assets JUMP **58.45m** · **FINIMO** pnl DROP **3.73m** / equity JUMP **106.33m** · **IDEFIN** pnl DROP **13.21m** / equity JUMP **329.54m** · **SOFILUX** pnl DROP **7.98m** / equity JUMP **203.98m** · **IFIGA** pnl JUMP **0.605m** / equity JUMP **10.09m** · **IDELUX Finances** omzet DROP **0.644m** / bruto NEG **0.676m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest shells** (**NEW 1971-1980** BEP NAMUR · LOGIPOLE · BEP Environnement · FINEST · HYGEA · FINIMO · IDEFIN · SOFILUX · IFIGA · **IDELUX Finances** · prior IBH/CENEO/IEG/IGRETEC/HELORA/SPGE/Aquiris/Vivaqua stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs IDELUX Env/Eau/SOFILUX/ORES/IPFBW path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 1980)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_cmt} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | {foi_tot} |
| research_queue open | rq_1981 after progress |

### What improved since tick 1970

- **Residual dual (tick1971-1980):** **BEP NAMUR** · **LOGIPOLE** · **BEP Environnement** · **FINEST** · **HYGEA** · **FINIMO** · **IDEFIN** · **SOFILUX** · **IFIGA** · **IDELUX Finances** (this tick EVERY-10 dual — Luxembourg economic-equipment financing CV YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1990**.

"""
# keep prior snapshots from old file starting at tick 1970
idx = old.find("## Snapshot at **tick 1970**")
if idx < 0:
    idx = old.find("## Snapshot at **tick 1960**")
tail = old[idx:] if idx >= 0 else ""
prog.write_text(snap + "\n" + tail, encoding="utf-8")
print("progress refreshed")

top = Path("docs/doge/data/doge_waste_top10_current.md")
top.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **1980** (2026-08-23) · **{n_lb}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1971-1980:** **IDEFIN equity 329.54m** · **SOFILUX equity 203.98m** · **FINIMO equity 106.33m** · **FINEST equity 64.64m** · **HYGEA assets 58.45m** · **IDELUX Finances equity 36.07m** · **BEP Environnement equity 37.57m** · **LOGIPOLE omzet 24.82m** · **IFIGA equity 10.09m** · **BEP NAMUR omzet 3.85m** · prior **IBH / CENEO / IEG / HELORA / IGRETEC / SPGE / Aquiris / Vivaqua** · prior **nuclear / Fluxys / Elia / Enodia / RESA** · prior Publi-T/Publigas/Nethys/Virya · prior **Eneco continuum** · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1970:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 1971-1980 (off pure top10 / dual):** BEP NAMUR · LOGIPOLE · BEP Environnement · FINEST · HYGEA · FINIMO · IDEFIN · SOFILUX · IFIGA · **IDELUX Finances** (EVERY-10 dual). Count NEW since 1970: 10 residual dual ticks. **Prior IBH/CENEO/IEG/IGRETEC/HELORA/SPGE stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_1980":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after IFIGA — IDELUX Finances YE2025 Medium"
        x["notes"] = "tick1980 EVERY-10 + IDELUX Finances Medium omzet DROP 0.644m bruto NEG 0.676m; FOI ready; next rq_1981; next every-10 1990"
        x["instructions"] = (
            "Completed EVERY-10 progress/top10 + leftover IDELUX Finances YE2025 Medium CW; KBO 0258.258.738; "
            "omzet DROP 644147 pnl JUMP 1026516 equity JUMP 36065604 bruto NEG -675994 FTE 0; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1981" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1981",
            "title": "leftover dual hole-fill after IDELUX Finances EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1980 after EVERY-10 + IDELUX Finances YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/ADT (IDETA/SPI parent if YE2025). Do NOT redo IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1980 EVERY-10 IDELUX Finances; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1980",
        "ticks_completed": "1980",
        "paused": "no",
        "notes": "tick1980 EVERY-10 + IDELUX Finances 0258.258.738 Medium CW (omzet DROP 0.644m pnl JUMP 1.027m equity JUMP 36.07m bruto NEG 0.676m FTE 0; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1981; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = f"""

## Tick 1980 - 2026-08-23T22:30:00Z - rq_1980 EVERY-10 + IDELUX Finances (omzet DROP 0.644m / bruto NEG 0.676m / Medium)

- Unit: **rq_1980** EVERY-10 mandatory + leftover dual after **rq_1979 IFIGA**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**; IPALLE/INTRADEL/TIBI already YE2025 mined. Took unused leftover **IDELUX Finances** YE2025 (KBO **0258.258.738**; Schoppach Arc-en-Ciel 98 Arlon; Luxembourg economic-equipment financing CV). Do not redo IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IPFBW/IPALLE/INTRADEL/TIBI/IDELUX Env/Eau.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 1980 snapshot; residual dual 1971-1980) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN YE2025 - omzet **EUR644,147** DROP -78.85%; pnl **EUR1,026,516** JUMP +31.69%; equity **EUR36,065,604** JUMP +1.47%; bruto **NEG EUR-675,994** (swing from +1.715m); FTE **0**; neerlegging **19.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV; email officiel.ic-ideluxfinances@idelux.be.
- Wrote: sources (+3); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_idelux_finances); foi + draft {GAP}; progress+top10; rq_1980=done + rq_1981 open; loop_state ticks=1980.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done. Next every-10 **1990**. Next: rq_1981 (AGB/FARO-if-YE2025 / AIESH-REW / IDETA-SPI / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1980" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1980")
