import csv
from collections import Counter
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T15:00:00Z"
Path("docs/doge/data/raw/tick2290").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def count(path):
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


# Guard
path_rq = "docs/doge/data/research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2290" and row["status"] == "done":
        raise SystemExit(f"rq_2290 already done: {row.get('title','')[:90]}")

# --- Op Maat unit fills ---
for sid, title, url, pub, klass, notes in [
    (
        "src_op_maat_jr2025_cw_nl",
        "Companyweb NL Op Maat YE2025 statutory",
        "https://www.companyweb.be/nl/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2290; YE2025 empty omzet bruto JUMP 2347442 pnl JUMP 88925 equity JUMP 914553 FTE JUMP 50.5; neerlegging 13.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2290/",
    ),
    (
        "src_op_maat_jr2025_cw_en",
        "Companyweb EN Op Maat YE2025 statutory",
        "https://www.companyweb.be/en/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2290; EN mirror YE2025 Medium; filed 13-06-2026; Last balance sheet year 2025; Turnover unpublished Gross margin 2347442 Profit/Loss 88925 Equity 914553 FTE 50.5",
    ),
    (
        "src_op_maat_jr2025_cw_fr",
        "Companyweb FR Op Maat YE2025 statutory",
        "https://www.companyweb.be/fr/0841138864/op-maat",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        "tick2290; FR mirror; CA unpublished; Marge brute 2347442; Benefice 88925",
    ),
    (
        "src_op_maat_kbo_2290",
        "KBO Op Maat 0841.138.864 Actief Kuurne 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0841138864",
        "KBO FOD Economie",
        "official_register",
        "tick2290; Actief VZW OP MAAT; zetel Twaalfde-Liniestraat 4 bus 1 8520 Kuurne; 1 VE; RSZ NACE 88.999; geen BTW; dienst persoonlijke assistentie W-Vl",
    ),
    (
        "src_op_maat_site_contact_2290",
        "Op Maat FOI channel info@vzwopmaat.be",
        "https://vzwopmaat.be/",
        "Op Maat VZW",
        "foi_contact",
        "tick2290; info@vzwopmaat.be; +32 56 72 73 06; Twaalfde-Liniestraat 4/1 Kuurne; PAB/persoonlijke assistentie West-Vlaanderen",
    ),
]:
    append_csv(
        "docs/doge/data/sources.csv",
        dict(
            source_id=sid,
            title=title,
            url=url,
            publisher=pub,
            accessed_date="2026-08-27",
            source_class=klass,
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/entities.csv",
    dict(
        entity_id="vzw_op_maat_kuurne",
        name_nl="Op Maat VZW (Kuurne / persoonlijke assistentie W-Vl)",
        name_fr="Op Maat ASBL (Kuurne / assistance personnelle Flandre occidentale)",
        name_en="Op Maat VZW (Kuurne / personal assistance West Flanders disability support)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://vzwopmaat.be/",
        foi_email="info@vzwopmaat.be",
        foi_postal="Twaalfde-Liniestraat 4/1, 8520 Kuurne",
        notes=(
            "tick2290 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0841.138.864 Actief 1 VE NACE 88.999; empty omzet; "
            "bruto JUMP 2347442 (+10.86%) pnl JUMP 88925 (+29.3%) equity JUMP 914553 (+10.77%) FTE JUMP 50.5; "
            "neerlegging 13.06.2026; assets/debt Unknown; FOI "
            "gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5; "
            "after REW@2289; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
        ),
    ),
)

for bid, amt, basis, notes in [
    (
        "bud_op_maat_bruto_jr2025_statutory",
        2347442,
        "CW statutory bruto_marge YE2025 (empty omzet)",
        "tick2290; Medium CW; bruto JUMP +10.86% vs YE2024 2117574; omzet unpublished",
    ),
    (
        "bud_op_maat_pnl_jr2025_statutory",
        88925,
        "CW statutory winst/verlies YE2025 JUMP",
        "tick2290; Medium CW; pnl JUMP +29.3% vs YE2024 68775",
    ),
    (
        "bud_op_maat_equity_jr2025_statutory",
        914553,
        "CW statutory eigen_vermogen YE2025 JUMP",
        "tick2290; Medium CW; equity JUMP +10.77% vs YE2024 825628",
    ),
    (
        "bud_op_maat_fte_jr2025_statutory",
        50.5,
        "CW social-balance FTE 50.5",
        "tick2290; Medium CW; FTE 50.5 vs YE2024 46.7; assets/debt Unknown",
    ),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        dict(
            budget_id=bid,
            entity_id="vzw_op_maat_kuurne",
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_op_maat_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    "docs/doge/data/commitments.csv",
    dict(
        commitment_id="comm_op_maat_jr2025_statutory_pab_bruto_2_35m_empty_omzet",
        title=(
            "Op Maat YE2025 leftover dual (bruto 2.35m / empty omzet / pnl JUMP / equity JUMP / FTE 50.5 / Medium)"
        ),
        entity_id="vzw_op_maat_kuurne",
        beneficiary="personen met handicap W-Vl / persoonlijke assistentie (PAB) clients",
        legal_basis="VZW Op Maat (KBO 0841.138.864; Actief; 1 VE; NACE 88.999; Kuurne; PAB/dienstverlening)",
        decision_date="2026-06-13",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="2347442",
        cash_by_year=(
            '{"2025_omzet":null,"2025_bruto":2347442,"2025_pnl":88925,"2025_equity":914553,"2025_fte":50.5,'
            '"2024_omzet":null,"2024_bruto":2117574,"2024_pnl":68775,"2024_equity":825628,"2024_fte":46.7}'
        ),
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0841138864/op-maat",
        stated_goal="Persoonlijke assistentie West-Vlaanderen (disability home support)",
        cut_option="Publish NBB PDF assets/debt; reconcile empty omzet + bruto JUMP vs PAB/VAPH subsidy matrix",
        source_id="src_op_maat_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>JR2025_statutory_L5",
        notes=(
            "tick2290 EVERY-10; Medium CW; bruto primary envelope 2347442 (empty omzet); pnl JUMP 88925; "
            "equity JUMP 914553; FTE JUMP 50.5; 1 VE; after REW@2289; AGB Bornem JR2024; FARO YE2024; not TE-additive of 348bn"
        ),
    ),
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    dict(
        item_id="lb_op_maat_bruto_2_35m_empty_omzet_pnl_jump_fte_jump_jr2025",
        name=(
            "Op Maat bruto 2.35m / empty omzet / pnl JUMP / FTE JUMP 50.5 "
            "(YE2025 PAB persoonlijke assistentie Kuurne)"
        ),
        level="L5",
        type="pab_vzw_statutory",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>JR2025",
        annual_cost_eur="2347442",
        total_cost_eur="2347442",
        tco_notes=(
            "CW empty omzet / bruto 2347442 (+10.86%) / pnl JUMP 88925 (+29.3%) / equity JUMP 914553 (+10.77%) / "
            "FTE JUMP 50.5 (vs 46.7) / 1 VE PAB W-Vl"
        ),
        confidence="medium",
        source_id="src_op_maat_jr2025_cw_en",
        beneficiaries="personen met handicap West-Vlaanderen / PAB clients",
        stated_goal="Persoonlijke assistentie W-Vl (home disability support)",
        measured_outcome=(
            "empty omzet; bruto JUMP +10.86%; pnl JUMP +29.3%; equity JUMP +10.77%; FTE JUMP 50.5; filed 13.06.2026"
        ),
        absurdity_score="5.5",
        cost_score="3.6",
        difficulty="3.0",
        priority_index="4.55",
        cut_proposal="Publish NBB PDF assets/debt FOI; disclose empty-omzet + bruto JUMP vs PAB/VAPH subsidy matrix",
        status="open",
        struck_reason="",
        notes=(
            "tick2290 EVERY-10; Medium CW; FOI gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after REW@2289"
        ),
    ),
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    dict(
        gap_id="gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kuurne>Op_Maat>NBB_PDF_assets_debt_empty_omzet_bruto_jump",
        entity_id="vzw_op_maat_kuurne",
        what_is_missing=(
            "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet; bruto EUR2347442; "
            "pnl JUMP EUR88925; equity JUMP EUR914553; PAB/VAPH subsidy matrix; FTE 50.5; client/activity split"
        ),
        why_it_matters=(
            "Medium CW shows W-Vl PAB VZW (bruto 2.35m / empty omzet / pnl JUMP / FTE JUMP 50.5) "
            "under persoonlijke-assistentie path; assets/debt unpublished"
        ),
        priority="8",
        recipient_body="Op Maat VZW",
        recipient_email="info@vzwopmaat.be",
        recipient_postal="Twaalfde-Liniestraat 4/1, 8520 Kuurne",
        draft_letter_path="docs/doge/foi/drafts/gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5.md",
        status="ready",
        date_ready="2026-08-27",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id="comm_op_maat_jr2025_statutory_pab_bruto_2_35m_empty_omzet",
        linked_leaderboard_id="lb_op_maat_bruto_2_35m_empty_omzet_pnl_jump_fte_jump_jr2025",
        created_utc=utc,
        updated_utc=utc,
        notes="tick2290 EVERY-10; ready NOT sent; Medium CW + Strong KBO; next every-10 2300",
    ),
)

# inventory after Op Maat append
b = count("docs/doge/data/budgets.csv")
c = count("docs/doge/data/commitments.csv")
l = count("docs/doge/data/leaderboard.csv")
e = count("docs/doge/data/entities.csv")
s = count("docs/doge/data/sources.csv")
with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
    foi_rows = list(csv.DictReader(f))
foi_c = Counter(r.get("status") for r in foi_rows)
ready = foi_c.get("ready", 0)
answered = foi_c.get("answered", 0)
partial = foi_c.get("partial", 0)
foi_total = len(foi_rows)

# --- EVERY-10 progress ---
Path("docs/doge/data/progress_every_10_ticks.md").write_text(
    f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2290** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2281-2290 continuum; AGB Bornem / FARO still YE2024 stalls; AIESH YE2024; **REW unlocked YE2025@2289**; Citeco/Groupe Foes/Aralea/Manupal/De Ploeg/Vlotter/Buseloc YE2024 |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2281-2290 is residual dual L5 (not near-complete of 348bn):** De Dageraad · Ateliers du 94 · Die Zukunft · Ateljee · Posthoorn · Mobiel · Borgerstein/WEBO · De Sprong · Village Liegeois · **REW omzet 14.72m** · EVERY-10 primary **Op Maat** bruto **2.35m** / empty omzet / pnl JUMP / FTE **50.5** (Medium CW) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}**; partial **~{partial}**; total FOI rows **~{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2281-2290** De Dageraad · A94 · Die Zukunft · Ateljee · Posthoorn · Mobiel · Borgerstein/WEBO · De Sprong · Village Liegeois · **REW** · **Op Maat** · prior 2271-2280 Alternatief/AMAB/IN-Z stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2290)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {b}+ |
| commitments.csv | {c}+ |
| leaderboard.csv | {l}+ |
| entities.csv | {e}+ |
| sources.csv | {s}+ |
| FOI ready | ~{ready} |
| FOI answered | {answered} |
| FOI partial | {partial} |
| FOI total rows | ~{foi_total} |
| research_queue open | rq_2291 after Op Maat EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2280

- **Residual dual (tick2281-2290):** **De Dageraad** / **Ateliers du 94** · **Die Zukunft** · **Ateljee** · **Posthoorn** (YE2025 unlocked) · **Mobiel** · **Borgerstein/WEBO** · **De Sprong** · **Village Liegeois** · **REW** (YE2025 unlocked municipal DSO Wavre; omzet **14.72m**) · EVERY-10 primary **Op Maat** (bruto **2.35m** / empty omzet / pnl JUMP / FTE **50.5**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH YE2024-only · Citeco / Groupe Foes / Aralea / Manupal / De Ploeg / Vlotter / Buseloc YE2024 · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
""",
    encoding="utf-8",
)

Path("docs/doge/data/doge_waste_top10_current.md").write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2290** (2026-08-27) · **{l}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2281-2290:** **Op Maat bruto 2.35m / empty omzet / pnl JUMP / FTE 50.5** (EVERY-10@2290 primary) · **REW omzet 14.72m / bruto~0.6x / PROFIT FLIP** · Village Liegeois · De Sprong · Borgerstein/WEBO · Posthoorn · Mobiel · Ateljee · Die Zukunft · A94 · De Dageraad · prior 2271-2280 Alternatief/AMAB/IN-Z stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2280:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2281-2290 (off pure top10 / dual):** De Dageraad · A94 · Die Zukunft · Ateljee · Posthoorn · Mobiel · Borgerstein/WEBO · De Sprong · Village Liegeois · **REW** · **Op Maat bruto 2.35m / empty omzet / pnl JUMP / FTE 50.5** (EVERY-10@2290 primary). Count NEW since 2280: ~11 residual dual fills. **Prior 2271-2280 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Op Maat** EVERY-10 primary bruto **EUR2.35m** / empty omzet / pnl JUMP **+29%** / FTE **50.5** — Kuurne PAB / persoonlijke assistentie opacity.
- **REW** omzet **EUR14.72m** / bruto~**0.6x** / pnl PROFIT FLIP / FTE **35** — Wavre municipal DSO unlocked YE2025.
- **Village Liegeois** bruto **EUR2.25m** / empty omzet / pnl DROP / FTE **58**.
- **De Sprong** bruto **EUR4.53m** / empty omzet / FTE **111**.
- **Borgerstein/WEBO** omzet **EUR14.70m** / bruto~**2.62x** / FTE **548**.
- **Posthoorn** omzet **EUR1.94m** / bruto~**1.51x** / LOSS FLIP / FTE **82**.
- **Atelier Alternatief** prior EVERY-10 bruto **EUR4.11m** / empty omzet / equity DROP **-30.5%** (retained).
- **AMAB** / **IN-Z** prior large maatwerk LOSS paths retained.
""",
    encoding="utf-8",
)

# research queue close + spawn
for row in rows:
    if row["task_id"] == "rq_2290":
        row.update(
            {
                "title": (
                    "EVERY-10 + leftover dual — Op Maat YE2025 Medium "
                    "(bruto JUMP 2.35m / empty omzet / pnl JUMP / FTE 50.5)"
                ),
                "status": "done",
                "entity_id": "vzw_op_maat_kuurne",
                "blocked_gap_id": "gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5",
                "updated_utc": utc,
                "instructions": (
                    "EVERY-10 + leftover dual Op Maat YE2025 FREE W-Vl PAB after REW@2289; "
                    "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
                ),
                "notes": (
                    "tick2290 EVERY-10 + Op Maat VZW Kuurne 0841.138.864 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                    "omzet unpublished; bruto JUMP 2347442 (+10.86%); pnl JUMP 88925 (+29.3%); equity JUMP 914553 (+10.77%); "
                    "FTE JUMP 50.5; 1 VE; NACE 88.999; neerlegging 13.06.2026; assets/debt Unknown; FOI ready NOT sent; "
                    "progress+waste top10 refreshed; stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; "
                    "after REW@2289; next EVERY-10 2300"
                ),
            }
        )

if not any(row["task_id"] == "rq_2291" for row in rows):
    rows.append(
        {
            "task_id": "rq_2291",
            "title": (
                "leftover dual after Op Maat — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after rq_2290 Op Maat YE2025 Medium primary (bruto JUMP 2.35m / empty omzet / pnl JUMP / FTE 50.5). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ, else unused ETA-VAPH-WZC-maatwerk "
                "(Aralea/Manupal/De Ploeg/Vlotter/Buseloc YE2024; Roseau Vert/Ateliers Mons/Monceau if YE2025). "
                "Do NOT redo Op Maat/REW/Village Liegeois/De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn stack."
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": (
                "spawned after tick2290 EVERY-10 Op Maat; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "REW YE2025 taken@2289; next every-10 2300"
            ),
        }
    )

with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fields})

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": utc,
            "last_unit_id": "rq_2290",
            "ticks_completed": "2290",
            "paused": "no",
            "notes": (
                "tick2290 EVERY-10 + leftover dual Op Maat 0841.138.864 Medium (bruto JUMP 2347442 +10.86%; empty omzet; "
                "pnl JUMP 88925; equity JUMP 914553; FTE JUMP 50.5; 1 VE Kuurne PAB W-Vl); after REW@2289; "
                "AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2291; next EVERY-10 2300; continuous hole_fill"
            ),
        }
    )

# update FOI draft tick label if present
draft = Path(
    "docs/doge/foi/drafts/gap_op_maat_nbb_pdf_assets_debt_empty_omzet_bruto_jump_pnl_jump_pab_matrix_l5.md"
)
if draft.exists():
    txt = draft.read_text(encoding="utf-8")
    txt = txt.replace("**tick:** 2289", "**tick:** 2290")
    txt = txt.replace("After Village Liegeois@2288", "After REW@2289 (EVERY-10@2290 primary)")
    draft.write_text(txt, encoding="utf-8")

print("tick2290 EVERY-10 + Op Maat OK")
print("inventory", b, c, l, e, s, "foi_ready", ready)
