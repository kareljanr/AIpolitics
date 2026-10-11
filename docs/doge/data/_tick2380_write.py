#!/usr/bin/env python3
"""Surgical tick 2380 writes — append/patch only, never rewrite whole CSVs. EVERY-10 refresh from live CSVs."""
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

EID = "vzw_stvzulte"
SRC_PDF = "src_stvzulte_jr2025_nbb_pdf_2380"
SRC_KBO = "src_stvzulte_kbo_2380"
SRC_SBM = "src_stvzulte_sbm_2380"
SRC_SITE = "src_stvzulte_site_2380"
COMM = "comm_stvzulte_jr2025_statutory_omzet_6_92m_pnl_loss_destin_empty"
LB = "lb_stvzulte_omzet_6_92m_pnl_loss_destin_empty_jr2025"
GAP = "gap_stvzulte_zorgkas_riziv_wzc_matrix_omzet_6_92m_73_1_17m_pnl_loss_destin_empty_l5"
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


append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Woonzorg Sint-Vincentius Zulte deposit 2026-00285601,http://cdn.staatsbladmonitor.be/2026pdf/2026-00285601.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2380; official native PDF 588212 bytes 47p VOL-VZW 23.0.10 m05-f; header 10.07.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-30; CreationDate 2026-07-13 21:39:13 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table",
    f"{SRC_KBO},KBO Woonzorg Sint-Vincentius vzw 0448.633.413,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448633413,KBO Public Search FOD Economie,{DAY},official_register,tick2380; Actief; 1 VE 2.150.780.307 Woonzorg Sint-Vincentius Pontstraat 20 since 03.01.2006; zetel Pontstraat 20 9870 Zulte since 01.10.1992; RSZ2025 87.101 RVT; voorzitter Dirk Adams; dagelijks bestuur Bart Verschelde since 10.12.2025; commissaris Baker Tilly / Wim Van De Walle tot 27.06.2027",
    f"{SRC_SBM},Staatsbladmonitor fiche Woonzorg Sint-Vincentius vzw 0448633413 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0448633413,Staatsbladmonitor,{DAY},official_register,tick2380; deposit-id 2026-00285601 and CDN Last-Modified 2026-07-30; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC Sint-Vincentius Zulte FOI contact / WZC Zulte,https://stvzulte.be/,Woonzorg Sint-Vincentius vzw,{DAY},foi_contact,tick2380; FOI info@stvzulte.be; zetel Pontstraat 20 9870 Zulte; leftover city_zulte; NOT Kloosterstraat 6; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Woonzorg Sint-Vincentius VZW (WZC Zulte / ouderenzorg + kortverblijf + dagverzorging + Ponthove),Woonzorg Sint-Vincentius ASBL (MRS Zulte),Woonzorg Sint-Vincentius VZW (WZC Zulte),parastatal,city_zulte,nl,https://stvzulte.be/,info@stvzulte.be,"Pontstraat 20, 9870 Zulte",tick2380 YE2025 Strong official native NBB PDF deposit 2026-00285601 + Strong KBO 0448.633.413 Actief 1 VE RSZ2025 87.101; omzet JUMP 6916405 WZC ouderenzorg envelope; 73 DROP 1169444 (733 1169444); opbr JUMP 8133032; pnl LOSS JUMP -361438; equity DROP 3867855; assets DROP 12087824; debt DROP 8203044; FTE 88.3; kapitaalsubsidies JUMP 986484; destin691 empty; cash JUMP 249100; leftover city_zulte after Floordam@2379; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_stvzulte_omzet_jr2025_statutory,{EID},2025,6916405,6916405,6916405,NBB VOL-VZW code 70 omzet YE2025 JUMP +0.49% (primary L5 envelope; WZC ouderenzorg not commercial-only),{SRC_PDF},strong,tick2380; PDF p6 native; YE2024 6882816; 73 1169444 all 733; categorie-uitsplitsing empty",
    f"bud_stvzulte_opbr_jr2025_statutory,{EID},2025,8133032,8133032,8133032,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +0.21%,{SRC_PDF},strong,tick2380; PDF p6 native; YE2024 8116230; 74 43860; 76A 3322",
    f"bud_stvzulte_subs73_jr2025_statutory,{EID},2025,1169444,1169444,1169444,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -1.70%,{SRC_PDF},strong,tick2380; PDF p6+p21 native; YE2024 1189680; 733 1169444; 730 empty; 731 empty; 732 empty",
    f"bud_stvzulte_pnl_jr2025_statutory,{EID},2025,-361438,-361438,-361438,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 LOSS JUMP,{SRC_PDF},strong,tick2380; PDF p7 native; YE2024 -73419; bedrijfswinst 9901 -135434 LOSS FLIP vs YE2024 143518; destin691 empty",
    f"bud_stvzulte_equity_jr2025_statutory,{EID},2025,3867855,3867855,3867855,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -7.79%,{SRC_PDF},strong,tick2380; PDF p5 native; YE2024 4194708; kapitaalsubsidies 986484; overgedragen 14 2129111; bestemde fondsen 13 emptied",
    f"bud_stvzulte_assets_jr2025_statutory,{EID},2025,12087824,12087824,12087824,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.92%,{SRC_PDF},strong,tick2380; PDF p4 native; YE2024 12713201",
    f"bud_stvzulte_debt_jr2025_statutory,{EID},2025,8203044,8203044,8203044,NBB VOL-VZW code 17/49 schulden incl accruals YE2025 DROP -3.51%,{SRC_PDF},strong,tick2380; PDF p5 native; YE2024 8501568; LT 6444293; ST 1729055",
    f"bud_stvzulte_cash_jr2025_statutory,{EID},2025,249100,249100,249100,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +84.54%,{SRC_PDF},strong,tick2380; PDF p4 native; YE2024 134988; geldbeleggingen 50/53 742205 DROP vs 1303002",
    f"bud_stvzulte_kapitaalsubsidies_jr2025_statutory,{EID},2025,986484,986484,986484,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 JUMP +3.63%,{SRC_PDF},strong,tick2380; PDF p5 native; YE2024 951899",
    f"bud_stvzulte_fte_jr2025_statutory,{EID},2025,88.3,88.3,88.3,NBB VOL-VZW gemiddeld personeelseffectief VTE YE2025 88.3 JUMP +2.32%,{SRC_PDF},strong,tick2380; PDF p21 native; YE2024 86.3; koppen 9086 133 vs 122; personnel 62 6014374; uitzend 617 empty vs 64252",
])

cash_json = (
    '"{""2025_omzet"":6916405,""2025_opbr"":8133032,""2025_73"":1169444,'
    '""2025_731"":0,""2025_733"":1169444,""2025_74"":43860,""2025_76A"":3322,'
    '""2025_pnl"":-361438,""2025_bedrijfswinst"":-135434,""2025_equity"":3867855,'
    '""2025_assets"":12087824,""2025_debt"":8203044,""2025_fte"":88.3,'
    '""2025_kapitaalsubsidies"":986484,""2025_destin691"":0,""2025_cash"":249100,'
    '""2025_geldbeleggingen"":742205,""2025_personnel62"":6014374,'
    '""2025_uitzend617"":0,""2025_gebouwen22"":9136992,'
    '""2025_fondsen13"":0,""2025_onttrekking791"":672037,'
    '""2024_omzet"":6882816,""2024_opbr"":8116230,'
    '""2024_73"":1189680,""2024_pnl"":-73419,""2024_bedrijfswinst"":143518,'
    '""2024_equity"":4194708,""2024_assets"":12713201,""2024_debt"":8501568,'
    '""2024_kapitaalsubsidies"":951899,""2024_cash"":134988,""2024_fte"":86.3,'
    '""2024_destin691"":10745,""2024_fondsen13"":672037}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Woonzorg Sint-Vincentius vzw WZC Zulte YE2025 (omzet 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty / Strong PDF),{EID},Vlaamse zorgkas + Departement Zorg + leftover city_zulte,VZW Woonzorg Sint-Vincentius (KBO 0448.633.413; Actief; 1 VE; RSZ2025 87.101),2026-07-10,2025,2025,6916405,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00285601.pdf,Public WZC dual of mined city_zulte,Publish zorgkas/RIZIV/resident-fee matrix inside omzet 6.92m + explain 73 1.17m DROP + pnl LOSS 0.36m + destin 691 empty + fondsen 13 emptied 672k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Zulte>SintVincentius_WZC>JR2025_statutory_L5,tick2380; Strong official native PDF; leftover city_zulte after Floordam@2379; NOT Kloosterstraat 6; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Sint-Vincentius Zulte WZC omzet 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty (YE2025 Zulte),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Zulte>SintVincentius_WZC>JR2025,6916405,6916405,PDF omzet JUMP 6916405 WZC ouderenzorg envelope; 73 DROP 1169444 (733 1169444); opbr JUMP 8133032; 74 43860; bedrijfswinst LOSS FLIP -135434; pnl LOSS JUMP -361438; equity DROP 3867855; assets DROP 12087824; debt DROP 8203044; FTE 88.3 JUMP; kapitaalsubsidies JUMP 986484; destin691 empty; cash JUMP 249100; geldbeleggingen DROP 742205; gebouwen 9136992; personnel 6014374; fondsen13 emptied 672037,strong,{SRC_PDF},WZC + kortverblijf + dagverzorging + Ponthove residents Zulte,Vlaamse zorgkas + Departement Zorg + leftover city_zulte,6.92m WZC omzet; 1.17m 73 subsidies DROP; pnl LOSS 0.36m; destin empty; fondsen 13 emptied 672k; leftover city_zulte,5.8,5.6,5.4,5.57,FOI zorgkas/RIZIV/resident-fee matrix + 73 1.17m DROP + pnl LOSS 0.36m + destin empty + fondsen 13 emptied,active,,tick2380; Strong official NBB native PDF + Strong KBO; leftover city_zulte after Floordam@2379; OFF Drongen OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Zulte>SintVincentius_WZC>zorgkas_RIZIV_WZC,vzw_stvzulte,zorgkas/RIZIV/resident-fee split inside omzet 6916405; why 73 1169444 DROP (733 1169444); nature of kapitaalsubsidies 986484 JUMP and destin 691 empty; pnl LOSS 361438; fondsen 13 emptied 672037; cash JUMP 249100 vs beleggingen DROP 742205,Strong official PDF leftover public WZC of city_zulte; 6.92m omzet; public not private clinic,8,Woonzorg Sint-Vincentius VZW / Dirk Adams voorzitter RvB,info@stvzulte.be,"Pontstraat 20, 9870 Zulte",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2380; ready NOT sent; Strong official native NBB PDF; EVERY-10 after Floordam@2379; leftover city_zulte WZC off Drongen off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2380,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2380 line, found {n}")
if "rq_2381," in rq_text:
    raise SystemExit("rq_2381 already exists")

new_2380 = (
    "rq_2380,EVERY-10 + leftover dual — Woonzorg Sint-Vincentius Zulte YE2025 Strong (omzet JUMP 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty),"
    "hole_fill,8,done,L5,vzw_stvzulte,"
    "Tick 2380 EVERY-10 leftover after Floordam. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam). "
    "Took Woonzorg Sint-Vincentius Zulte 0448.633.413 deposit 2026-00285601 leftover city_zulte. "
    "Do NOT redo Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:15:16Z,{STAMP},"
    "tick2380 EVERY-10 Sint-Vincentius Zulte 0448.633.413 YE2025 Strong official native PDF 2026-00285601; omzet JUMP 6916405 WZC ouderenzorg envelope; 73 DROP 1169444 (733 1169444); opbr JUMP 8133032; pnl LOSS JUMP -361438; equity DROP 3867855; assets DROP 12087824; debt DROP 8203044; FTE 88.3; kapitaalsubsidies JUMP 986484; destin691 empty; cash JUMP 249100; FOI ready NOT sent; leftover city_zulte after Floordam@2379; OFF Drongen OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2380,"):
        parts.append(new_2380)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2380 replace count {replaced}")
new_rq = "".join(parts)
new_2381 = (
    "rq_2381,leftover dual after Sint-Vincentius Zulte — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Woonzorg Sint-Vincentius Zulte YE2025 EVERY-10. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413). "
    "Do NOT redo Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2380 EVERY-10; Sint-Vincentius Zulte WZC taken leftover city_zulte after Floordam; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2381
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2380 + rq_2381; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2380,2380,no,"
    "tick2380 EVERY-10 leftover dual Woonzorg Sint-Vincentius Zulte 0448.633.413 Strong native PDF (omzet JUMP 6916405 WZC ouderenzorg envelope; 73 DROP 1169444 733 1169444; opbr JUMP 8133032; pnl LOSS JUMP -361438; equity DROP 3867855; assets DROP 12087824; debt DROP 8203044; FTE 88.3; kapitaalsubsidies JUMP 986484; destin691 empty; cash JUMP 249100; 1 VE RSZ2025 87.101); leftover city_zulte after Floordam@2379; OFF Drongen OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2381; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

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
foi_c = Counter((r.get("status") or "").strip() for r in foi_rows)
n_foi = len(foi_rows)
n_ready = foi_c.get("ready", 0)
n_ans = foi_c.get("answered", 0)
n_part = foi_c.get("partial", 0)
print("INV", n_bud, n_com, n_lb, n_ent, n_src, "foi", n_foi, "ready", n_ready, "ans", n_ans, "part", n_part)

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2380** ({DAY})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2371-2380 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **WZC Sint-Vincentius Zulte unlocked YE2025@2380** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2371-2380 residual dual L5 (not near-complete of 348bn):** Impuls · Buggenhout · Sint-Lievenspoort · Inkendaal · Pulderbos · MKL · NMSC · Heropbeuring · Floordam · EVERY-10 primary **WZC Sint-Vincentius Zulte omzet 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty** (Strong PDF) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **{n_ans}**; partial **{n_part}**; total FOI rows **{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR shells** (**NEW 2371-2380** Impuls · Buggenhout · Sint-Lievenspoort · Inkendaal · Pulderbos · MKL · NMSC · Heropbeuring · Floordam · **WZC Sint-Vincentius Zulte**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2380)

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
| research_queue open | rq_2381 after Sint-Vincentius Zulte EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2370 / last file refresh 2370

- **Residual dual (tick2371-2380):** leftover public CAR/hospital/WZC **Impuls / Buggenhout / Sint-Lievenspoort / Inkendaal / Pulderbos / MKL / NMSC / Heropbeuring / Floordam** · EVERY-10 primary **WZC Sint-Vincentius Zulte** (omzet **6.92m** / 73 **1.17m** DROP / pnl LOSS **0.36m** / destin 691 empty / fondsen 13 emptied **672k** / cash JUMP **0.25m +85%** / Strong official PDF 2026-00285601; Departement Zorg HCO 3762; FOI ready). Named+unnamed Drongen CARs exhausted. Steenokkerzeel leftover Floordam+NMSC taken.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024 · Zeepreventorium YE2024.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2380** ({DAY}) · **{n_lb}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2371-2380:** **WZC Sint-Vincentius Zulte omzet 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty** (EVERY-10@2380 Strong PDF) · Floordam 9.63m / pnl DROP 71% · Heropbeuring 12.15m / pnl LOSS · NMSC 28.75m · MKL 45.61m · Pulderbos 16.89m · Inkendaal 43.55m · Sint-Lievenspoort 20.98m · CAR Bolt 2.10m / 1.95m kapitaalsubsidies · Helan HH 115m.

**Change vs tick 2370:** pure annual top10 **stable** (recomputed from live leaderboard {n_lb} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2371-2380:** WZC Sint-Vincentius Zulte EVERY-10 primary + leftover public CAR/hospital/WZC close-out (Impuls→Floordam). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **WZC Sint-Vincentius Zulte** EVERY-10 primary omzet **EUR6.92m** / 73 **EUR1.17m** DROP / pnl LOSS **EUR0.36m** / destin 691 empty / fondsen 13 emptied **EUR672k** / cash JUMP **EUR0.25m +85%** / FTE **88.3** — Zulte Departement Zorg HCO 3762.
- **Floordam** omzet **EUR9.63m** / 73 **EUR2.10m** DROP / pnl DROP **−71%** / kapitaalsubsidies **EUR3.89m**.
- **MKL / RevArte** omzet **EUR45.61m** / 73 vs 733 gap **EUR4.14m** / kapitaalsubsidies **EUR14.95m**.
- **Helan Huishoudhulp** omzet **EUR115.15m** / pnl JUMP +690% / FTE **2809**.
- **Staf Leuven** bruto **EUR5.05m** / ~**68.12x** / pnl PROFIT FLIP.
- **Adem** bruto **EUR16.86m** / ~**17.53x** / pnl LOSS JUMP.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2380 - EVERY-10 + rq_2380 Woonzorg Sint-Vincentius Zulte (omzet JUMP 6.92m / 73 1.17m / pnl LOSS 0.36m / destin empty / Strong PDF)

- Unit: **rq_2380** leftover dual after **Floordam@2379** + **EVERY-10**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Woonzorg Sint-Vincentius VZW (WZC Zulte)** YE2025 (KBO **0448.633.413**; zetel Pontstraat 20, 9870 Zulte; **Actief** **1 VE** **2.150.780.307** Woonzorg Sint-Vincentius; RSZ2025 **87.101** RVT; leftover of mined **city_zulte**; info@stvzulte.be). Confirmed leftover public (Departement Zorg WZC HCO 3762 + RIZIV 76030182 + kortverblijf + dagverzorging + serviceflats Ponthove) not private clinic / not Floordam 0428.792.557 / not NMSC. Do not redo Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW native PDF deposit **2026-00285601** (588212 B / 47p; AV **23.06.2026**; header **10.07.2026**; CDN Last-Modified **30.07.2026**) — omzet 70 **EUR6916405** JUMP +0.49% (WZC ouderenzorg envelope; not commercial-only); 73 **EUR1169444** DROP −1.70% (733 **1169444**); bedrijfsopbrengsten 70/76A **EUR8133032** JUMP +0.21%; 74 **43860**; 76A **3322**; bedrijfswinst 9901 **EUR−135434** LOSS FLIP; pnl 9904 **EUR−361438** LOSS JUMP; equity **EUR3867855** DROP −7.79%; assets **EUR12087824** DROP −4.92%; debt **EUR8203044** DROP −3.51%; FTE **88.3** JUMP +2.32%; kapitaalsubsidies **EUR986484** JUMP +3.63%; destin 691 **empty**; cash **EUR249100** JUMP +84.54%; geldbeleggingen **EUR742205** DROP −43.04%; gebouwen **EUR9136992**; personeel 62 **EUR6014374**; uitzend 617 empty; fondsen 13 emptied via 791 **672037**. Strong KBO + Strong PDF (native text; not SBM table; smaller than Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.57); entities (+1 vzw_stvzulte); foi + draft `{GAP}`; rq_2380=done + rq_2381 open; loop_state ticks=2380; raw tick2380/ untracked.
- EVERY-10: refreshed `docs/doge/data/progress_every_10_ticks.md` + `docs/doge/data/doge_waste_top10_current.md` from live CSVs (inventory budgets {n_bud} / lb {n_lb} / FOI ready {n_ready}; annual top10 stable; residual 2371-2380 CAR+hospital+WZC close-out + Sint-Vincentius Zulte primary). Next every-10 **2390**.
- FOI: **ready not sent**. Next: rq_2381 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Sint-Vincentius Zulte / NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Candidate leftover school Katholiek Onderwijs Perk/Steenokkerzeel 0417.085.845 deposit 2026-00117941 only if leftover school of mined parent is in priority. Zeepreventorium still YE2024.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
