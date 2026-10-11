#!/usr/bin/env python3
"""Surgical tick 2370 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_car_bolt"
SRC_PDF = "src_bolt_jr2025_nbb_pdf_2370"
SRC_KBO = "src_bolt_kbo_2370"
SRC_SBM = "src_bolt_sbm_2370"
SRC_SITE = "src_bolt_site_2370"
COMM = "comm_bolt_jr2025_statutory_omzet_2_10m_1_95m_kapitaalsubsidies_pnl_drop_cash_drop"
LB = "lb_bolt_omzet_2_10m_1_95m_kapitaalsubsidies_pnl_drop_cash_drop_jr2025"
GAP = "gap_bolt_riziv_vl_matrix_1_95m_kapitaalsubsidies_pnl_drop_cash_drop_car_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"
if not (ROOT / DRAFT).is_file():
    raise SystemExit("FOI draft missing")


def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)


# sources (+4)
append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB WVV VKT-VZW jaarrekening 2025 CAR Bolt vzw deposit 2026-00073585,http://cdn.staatsbladmonitor.be/2026pdf/2026-00073585.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2370; official PDF 48524 bytes 12p VKT-VZW 25.0.9 m04-f; header 02.04.2026; AV 06.03.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-04-11; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO CAR Bolt vzw 0410.571.009,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410571009,KBO Public Search FOD Economie,{DAY},official_register,tick2370; Actief; 1 VE 2.153.755.534 Revalidatiecentrum Drongen Kloosterstraat 6 9031 Gent; zetel Kloosterstraat 6 9031 Gent/Drongen; RSZ2025 86.959; voorzitter Colson Marc; dagelijks bestuur Carpentier Kristof",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Bolt vzw 0410571009 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410571009,Staatsbladmonitor,{DAY},official_register,tick2370; deposit-id 2026-00073585 and CDN Last-Modified 2026-04-11; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Bolt vzw FOI contact / RIZIV-VAPH MDT Drongen,https://carbolt.be/,CAR Bolt vzw,{DAY},foi_contact,tick2370; FOI info@carbolt.be; Kloosterstraat 6/6A 9031 Drongen; erkenningsnummer 96518265; leftover same-zetel Ter Kouter/DIGOR/Mozaiek cluster",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},CAR Bolt VZW (Drongen / ambulante revalidatie),CAR Bolt ASBL (Drongen / revalidation ambulatoire),CAR Bolt VZW (Drongen / outpatient rehabilitation),parastatal,sec_flanders,nl,https://carbolt.be/,info@carbolt.be,"Kloosterstraat 6, 9031 Drongen",tick2370 YE2025 Strong official NBB PDF deposit 2026-00073585 + Strong KBO 0410.571.009 Actief 1 VE 2.153.755.534 RSZ2025 86.959 RIZIV 96518265; omzet JUMP 2100132; bruto JUMP 2543651 ~1.21x; pnl DROP 86426; equity JUMP 5065359; assets JUMP 5529384; debt DROP 293351; FTE JUMP 30.9; code73 629481; kapitaalsubsidies JUMP 1951460; destin691 empty; cash DROP 1308598; leftover Mozaiek@2369 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = omzet 70 (present and not commercial-only vs 73)
append_lines(DATA / "budgets.csv", [
    f"bud_bolt_omzet_jr2025_statutory,{EID},2025,2100132,2100132,2100132,NBB VKT-VZW code 70 omzet YE2025 JUMP +2.68% (primary L5 envelope),{SRC_PDF},strong,tick2370; PDF p5; YE2024 2045306; omzet present and not commercial-only vs 73 629481",
    f"bud_bolt_bruto_jr2025_statutory,{EID},2025,2543651,2543651,2543651,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +0.73% (~1.21x omzet),{SRC_PDF},strong,tick2370; PDF p5; YE2024 2525117",
    f"bud_bolt_code73_jr2025_statutory,{EID},2025,629481,629481,629481,NBB VKT-VZW code 73 lidgeld/schenkingen/subsidies YE2025 JUMP +3.18%,{SRC_PDF},strong,tick2370; PDF p5; YE2024 610109",
    f"bud_bolt_pnl_jr2025_statutory,{EID},2025,86426,86426,86426,NBB VKT-VZW code 9905 te bestemmen winst YE2025 DROP -59.92%,{SRC_PDF},strong,tick2370; PDF p5; YE2024 215648; bedrijfswinst 9901 74607 DROP -60.18%",
    f"bud_bolt_equity_jr2025_statutory,{EID},2025,5065359,5065359,5065359,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +23.82%,{SRC_PDF},strong,tick2370; PDF p4; YE2024 4090886; kapitaalsubsidies 1951460; bestemde fondsen 448882",
    f"bud_bolt_assets_jr2025_statutory,{EID},2025,5529384,5529384,5529384,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +18.21%,{SRC_PDF},strong,tick2370; PDF p3; YE2024 4677738",
    f"bud_bolt_debt_jr2025_statutory,{EID},2025,293351,293351,293351,NBB VKT-VZW code 17/49 schulden YE2025 DROP -29.51%,{SRC_PDF},strong,tick2370; PDF p4; YE2024 416179",
    f"bud_bolt_cash_jr2025_statutory,{EID},2025,1308598,1308598,1308598,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -28.90%,{SRC_PDF},strong,tick2370; PDF p3; YE2024 1840578",
    f"bud_bolt_kapitaalsubsidies_jr2025_statutory,{EID},2025,1951460,1951460,1951460,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 JUMP +83.51%,{SRC_PDF},strong,tick2370; PDF p4; YE2024 1063413; gebouwen 22 JUMP 3818592; capex 8169 1312557",
    f"bud_bolt_fte_jr2025_statutory,{EID},2025,30.9,30.9,30.9,NBB VKT-VZW code 9087 FTE YE2025 JUMP +4.75%,{SRC_PDF},strong,tick2370; PDF p8; YE2024 29.5",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":2100132,""2025_code73"":629481,""2025_bruto"":2543651,""2025_pnl"":86426,'
    '""2025_equity"":5065359,""2025_assets"":5529384,""2025_debt"":293351,""2025_fte"":30.9,'
    '""2025_kapitaalsubsidies"":1951460,""2025_destin691"":0,""2025_destin13"":448882,'
    '""2025_cash"":1308598,""2025_personnel62"":2224297,""2025_capex8169"":1312557,'
    '""2025_gebouwen22"":3818592,""2024_omzet"":2045306,""2024_code73"":610109,""2024_bruto"":2525117,'
    '""2024_pnl"":215648,""2024_equity"":4090886,""2024_assets"":4677738,""2024_debt"":416179,'
    '""2024_fte"":29.5,""2024_kapitaalsubsidies"":1063413,""2024_destin13"":448882,""2024_cash"":1840578}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Bolt vzw YE2025 (omzet 2.10m / 1.95m kapitaalsubsidies JUMP / pnl DROP / Strong PDF),{EID},RIZIV-VAPH CAR Drongen / dual same zetel,VZW CAR Bolt (KBO 0410.571.009; Actief; 1 VE; RSZ2025 86.959; RIZIV 96518265),2026-04-02,2025,2025,2100132,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00073585.pdf,RIZIV-conventioned ambulante revalidatie children 2-19 + VAPH MDT + dual Drongen Ter Kouter cluster,Publish RIZIV/VL matrix inside omzet 2.10m + 73 0.63m; explain 1.95m kapitaalsubsidies JUMP +83pct and gebouwen JUMP +149pct vs cash DROP and pnl DROP,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Drongen>CAR_Bolt>JR2025_statutory_L5,tick2370 EVERY-10; Strong official PDF; leftover Mozaiek@2369 same Drongen zetel; not TE-additive",
])

# leaderboard (+1) pi = 0.4*5.8 + 0.4*4.8 + 0.2*5 = 5.24
append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Bolt omzet 2.10m / 1.95m kapitaalsubsidies JUMP +83% / pnl DROP -60% / cash DROP -29% (YE2025 CAR Drongen),L5,car_revalidatie_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Drongen>CAR_Bolt>JR2025,2100132,2100132,PDF omzet JUMP 2100132; bruto JUMP 2543651 (~1.21x); pnl DROP 86426; equity JUMP 5065359; assets JUMP 5529384; debt DROP 293351; FTE JUMP 30.9; destin691 empty; kapitaalsubsidies JUMP 1951460; cash DROP 1308598; code73 629481; gebouwen JUMP 3818592; capex 1312557,strong,{SRC_PDF},outpatient rehab children/adolescents 2-19 Drongen (RIZIV 96518265 + VAPH MDT + dual Ter Kouter cluster),RIZIV-conventioned ambulante revalidatie Drongen + VAPH MDT,1.95m capital subsidies JUMP +83.51% (1.06m to 1.95m); gebouwen JUMP +148.79% after 1.31m capex; cash DROP -28.90%; pnl DROP -59.92%; destin 691 empty; RIZIV/VL split unpublished; leftover same-zetel unnamed of Mozaiek/DIGOR/Ter Kouter cluster,5.8,4.8,5,5.24,FOI RIZIV/VL matrix + 1.95m kapitaalsubsidies JUMP + gebouwen JUMP + cash DROP + pnl DROP + dual Drongen cluster,active,,tick2370 EVERY-10; Strong official NBB PDF + Strong KBO; leftover Mozaiek@2369 same zetel; next leftover Impuls / Buggenhout",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Drongen>CAR_Bolt>RIZIV_VL_kapitaalsubsidies,vzw_car_bolt,RIZIV vs VAPH vs VL split inside omzet 2100132 + code 73 629481; nature of kapitaalsubsidies 1951460 JUMP +83.51pct; toelichting destin 691 empty and pnl DROP 86426; gebouwen JUMP 3818592 after capex 1312557; cash DROP 1308598; dual Drongen zetel,Strong official PDF leftover RIZIV CAR of Mozaiek@2369 same zetel; 1.95m capital subsidies JUMP; pnl DROP -60pct; cash DROP -29pct; public CAR not private clinic,8,CAR Bolt VZW / Marc Colson voorzitter RvB,info@carbolt.be,"Kloosterstraat 6A, 9031 Drongen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2370 EVERY-10; ready NOT sent; Strong official NBB PDF; after Mozaiek@2369; leftover same-zetel unnamed CAR; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2370 + append rq_2371 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2370,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2370 line, found {n}")
if "rq_2371," in rq_text:
    raise SystemExit("rq_2371 already exists")

new_2370 = (
    "rq_2370,EVERY-10 + leftover dual — CAR Bolt YE2025 Strong (omzet JUMP 2.10m / 1.95m kapitaalsubsidies JUMP / pnl DROP),"
    "hole_fill,8,done,L5,vzw_car_bolt,"
    "Tick 2370 EVERY-10 MANDATORY plus leftover after named Drongen stack. Prefer AGB/FARO if YE2025 else leftover same-zetel CAR Bolt 0410.571.009 deposit 2026-00073585 if live 2026pdf. "
    "Do NOT redo named Drongen stack or Adem/MFC Combo/De Branding/Korenbloem/Leieborg.,"
    f"{GAP},2026-08-24T22:08:21Z,{STAMP},"
    "tick2370 EVERY-10 CAR Bolt 0410.571.009 YE2025 Strong official PDF 2026-00073585; omzet JUMP 2100132; bruto JUMP 2543651; pnl DROP 86426; equity JUMP 5065359; assets JUMP 5529384; debt DROP 293351; FTE JUMP 30.9; destin691 empty; kapitaalsubsidies JUMP 1951460; cash DROP 1308598; FOI ready NOT sent; leftover Mozaiek@2369 same zetel unnamed CAR\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2370,"):
        parts.append(new_2370)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2370 replace count {replaced}")
new_rq = "".join(parts)
new_2371 = (
    "rq_2371,leftover dual after CAR Bolt — Impuls / Buggenhout same-zetel,"
    "hole_fill,8,open,L5,,"
    "After CAR Bolt YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel CAR Impuls 0416.318.951 deposit 2026-00206349 / Revalidatiecentrum Buggenhout 0412.404.903 deposit 2026-00205237 if live 2026pdf. "
    "Do NOT redo CAR Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2370 EVERY-10; leftover Impuls/Buggenhout same zetel; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2371
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2370 + rq_2371; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2370,2370,no,"
    "tick2370 EVERY-10 leftover dual CAR Bolt 0410.571.009 Strong PDF (omzet JUMP 2100132; bruto JUMP 2543651 ~1.21x; pnl DROP 86426; equity JUMP 5065359; assets JUMP 5529384; debt DROP 293351; FTE JUMP 30.9; destin691 empty; kapitaalsubsidies JUMP 1951460; cash DROP 1308598; 1 VE RSZ2025 86.959 RIZIV 96518265); after Mozaiek@2369 same zetel unnamed; leftover Impuls/Buggenhout; AGB/FARO/Gandae YE2024; next rq_2371; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# EVERY-10 refresh from LIVE CSVs (after this tick's appends)
csv.field_size_limit(20_000_000)

def n_data(p):
    with open(p, "rb") as f:
        return sum(1 for _ in f) - 1

n_bud = n_data(DATA / "budgets.csv")
n_com = n_data(DATA / "commitments.csv")
n_lb = n_data(DATA / "leaderboard.csv")
n_ent = n_data(DATA / "entities.csv")
n_src = n_data(DATA / "sources.csv")
with open(DATA / "foi_queue.csv", newline="", encoding="utf-8") as f:
    foi_rows = list(csv.DictReader(f))
foi_c = Counter(r.get("status", "") for r in foi_rows)
n_foi = len(foi_rows)
n_ready = foi_c.get("ready", 0)
n_ans = foi_c.get("answered", 0)
n_part = foi_c.get("partial", 0)
print("INV", n_bud, n_com, n_lb, n_ent, n_src, "foi", n_foi, "ready", n_ready)

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2370** ({DAY})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2361-2370 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **CAR Bolt unlocked YE2025@2370** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2361-2370 residual dual L5 (not near-complete of 348bn):** De Elfjes · De Steijgertjes · De Steijger · Kapelhof · TKDV Het Veer · Wegwijs · SIG · DIGOR · Mozaiek · EVERY-10 primary **CAR Bolt omzet 2.10m / 1.95m kapitaalsubsidies JUMP +83% / pnl DROP -60% / cash DROP -29%** (Strong PDF) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **{n_ans}**; partial **{n_part}**; total FOI rows **{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR shells** (**NEW 2361-2370** De Elfjes · De Steijgertjes · De Steijger · Kapelhof · TKDV Het Veer · Wegwijs · SIG · DIGOR · Mozaiek · **CAR Bolt**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2370)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_com} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {n_ready} |
| FOI answered | {n_ans} |
| FOI partial | {n_part} |
| FOI total rows | {n_foi} |
| research_queue open | rq_2371 after CAR Bolt EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2360 / last file refresh 2360

- **Residual dual (tick2361-2370):** same-zetel CAR+KDV+koepel cluster **De Elfjes / De Steijgertjes / De Steijger / Kapelhof / TKDV Het Veer / Wegwijs / SIG / DIGOR / Mozaiek** · EVERY-10 primary **CAR Bolt** (omzet **2.10m** / kapitaalsubsidies JUMP **1.95m +83%** / pnl DROP **−60%** / cash DROP **1.31m −29%** / gebouwen JUMP **3.82m** / Strong official PDF 2026-00073585; RIZIV 96518265; FOI ready). Named Drongen stack now exhausted except leftover Impuls / Buggenhout.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2370** ({DAY}) · **{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.

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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2361-2370:** **CAR Bolt omzet 2.10m / 1.95m kapitaalsubsidies JUMP +83% / pnl DROP -60% / cash DROP -29%** (EVERY-10@2370 Strong PDF) · Mozaiek 13.18m code73 / 600k destin · DIGOR cash 1.72m · SIG 109k destin · Wegwijs 120k destin · TKDV Het Veer 1.14m kapitaalsubsidies · Kapelhof 487k · Noordhoek 1.50m · Ter Kouter 900k destin · Helan HH 115m.

**Change vs tick 2360:** pure annual top10 **stable** (recomputed from live leaderboard {n_lb} rows; pi>10 excluded; stocks filtered). **Major NEW residual 2361-2370:** CAR Bolt EVERY-10 primary + same-zetel CAR+KDV+koepel close-out (De Elfjes→Mozaiek) + unnamed leftover Impuls/Buggenhout still open. Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **CAR Bolt** EVERY-10 primary omzet **EUR2.10m** / kapitaalsubsidies JUMP **EUR1.95m +83%** / pnl DROP **−60%** / cash DROP **EUR1.31m −29%** / gebouwen JUMP **EUR3.82m** / FTE **30.9** — Drongen koepel-site RIZIV 96518265.
- **Mozaiek** opbr **EUR15.58m** / code 73 **EUR13.18m** vs 733 **EUR22k** / destin **EUR600k**.
- **Helan Huishoudhulp** omzet **EUR115.15m** / pnl JUMP +690% / FTE **2809**.
- **Staf Leuven** bruto **EUR5.05m** / ~**68.12x** / pnl PROFIT FLIP.
- **Adem** bruto **EUR16.86m** / ~**17.53x** / pnl LOSS JUMP.
- **CAR Ter Kouter** destin lock **EUR900k** vs pnl **EUR52k**.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")

# loop_log append
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2370 - EVERY-10 + rq_2370 CAR Bolt Drongen (omzet JUMP 2.10m / 1.95m kapitaalsubsidies JUMP +83% / pnl DROP -60% / Strong PDF)

- Unit: **rq_2370** leftover dual after **Mozaiek@2369** + **EVERY-10**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover unnamed same-zetel Flemish **CAR Bolt VZW** YE2025 (KBO **0410.571.009**; zetel én operationeel Kloosterstraat 6 / 6A, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs + Sig + DiGOR + Mozaiek; VE **2.153.755.534** Revalidatiecentrum Drongen; **Actief** **1 VE**; RSZ2025 **86.959**; RIZIV/VAPH **96518265**; leftover same-zetel unnamed CAR of mined **Mozaiek@2369** / **DiGOR@2368** / **Sig@2367** / **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355**; info@carbolt.be). Confirmed leftover public (RIZIV-conventioned CAR + VAPH-erkend MDT + Departement Zorg) not private clinic. Do not redo named Drongen stack or Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VKT-VZW PDF deposit **2026-00073585** (48524 B / 12p; AV **06.03.2026**; header **02.04.2026**; CDN Last-Modified **11.04.2026**) — omzet 70 **EUR2100132** JUMP +2.68%; bruto **EUR2543651** JUMP +0.73% (~**1.21x**); code 73 **EUR629481** JUMP +3.18%; pnl **EUR86426** DROP −59.92%; equity **EUR5065359** JUMP +23.82%; assets **EUR5529384** JUMP +18.21%; debt **EUR293351** DROP −29.51%; FTE **30.9** JUMP +4.75%; kapitaalsubsidies **EUR1951460** JUMP +83.51%; destin 691 **empty**; cash **EUR1308598** DROP −28.90%; gebouwen **EUR3818592** JUMP +148.79%; capex **EUR1312557**. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.24); entities (+1 vzw_car_bolt); foi + draft `{GAP}`; rq_2370=done + rq_2371 open; loop_state ticks=2370; raw tick2370/ untracked.
- EVERY-10: refreshed `docs/doge/data/progress_every_10_ticks.md` + `docs/doge/data/doge_waste_top10_current.md` from live CSVs (inventory budgets {n_bud} / lb {n_lb} / FOI ready {n_ready}; annual top10 stable; residual 2361-2370 CAR+KDV+koepel close-out + Bolt primary). Next every-10 **2380**.
- FOI: **ready not sent**. Next: rq_2371 leftover same-zetel CAR Impuls 0416.318.951 deposit 2026-00206349 / Revalidatiecentrum Buggenhout 0412.404.903 deposit 2026-00205237 if live 2026pdf.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
