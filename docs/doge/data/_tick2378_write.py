#!/usr/bin/env python3
"""Surgical tick 2378 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_heropbeuring"
SRC_PDF = "src_heropbeuring_jr2025_nbb_pdf_2378"
SRC_KBO = "src_heropbeuring_kbo_2378"
SRC_SBM = "src_heropbeuring_sbm_2378"
SRC_SITE = "src_heropbeuring_site_2378"
COMM = "comm_heropbeuring_jr2025_statutory_omzet_12_15m_pnl_loss"
LB = "lb_heropbeuring_omzet_12_15m_pnl_loss_jr2025"
GAP = "gap_heropbeuring_bfm_riziv_wzc_vaph_matrix_omzet_12_15m_74_4_86m_pnl_loss_l5"
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
    f"{SRC_PDF},NBB hospital-schema S-vzw jaarrekening 2025 Heropbeuring vzw De Mick deposit 2026-00197310,http://cdn.staatsbladmonitor.be/2026pdf/2026-00197310.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2378; official scanned PDF 9025650 bytes 23p S-vzw 26.0.15 m140-f-p hospital KB 19 juni 2007; header 24.06.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-09; CreationDate 2026-06-24 12:43:29 UTC Canon iR-ADV C5840 + OpenPDF 1.3.26; euros OCR from official PDF pages not SBM table",
    f"{SRC_KBO},KBO Heropbeuring vzw 0406.678.141,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406678141,KBO Public Search FOD Economie,{DAY},official_register,tick2378; Actief; 2 VE 2.152.235.703 Heropbeuring Papestraat 30 since 15.03.2006 + 2.384.771.625 De Vrije Vlinder Papestraat 28 since 10.02.2026; zetel Papestraat 30 2930 Brasschaat since 01.10.1990; Aanbestedende overheid since 30.10.1922; RSZ2025 87.301 ROB; BTW 86.101+87.301; voorzitter Dirk Schoeters; commissaris EY / Christoph Oris tot 22.06.2028",
    f"{SRC_SBM},Staatsbladmonitor fiche Heropbeuring vzw 0406678141 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0406678141,Staatsbladmonitor,{DAY},official_register,tick2378; deposit-id 2026-00197310 and CDN Last-Modified 2026-07-09; euros NOT taken from SBM HTML table (empty cells)",
    f"{SRC_SITE},Heropbeuring vzw De Mick FOI contact / hospital+WZC+VAPH Brasschaat,https://www.demick.be/,Heropbeuring vzw De Mick,{DAY},foi_contact,tick2378; FOI info@demick.be; zetel Papestraat 30 2930 Brasschaat; leftover city_brasschaat@1179; NOT Kloosterstraat 6; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Heropbeuring VZW (De Mick / Brasschaat / hospital + WZC + VAPH De Vrije Vlinder),Heropbeuring ASBL (De Mick / hopital + MRS + VAPH),Heropbeuring VZW (De Mick / hospital + WZC + VAPH),parastatal,city_brasschaat,nl,https://www.demick.be/,info@demick.be,"Papestraat 30, 2930 Brasschaat",tick2378 YE2025 Strong official scanned NBB PDF deposit 2026-00197310 + Strong KBO 0406.678.141 Actief 2 VE Aanbestedende RSZ2025 87.301; omzet JUMP 12147825 hospital/WZC envelope 700 7274801 + RIZIV 703 4508047; opbr JUMP 17019492; 74 4863745 vs 740 5943; pnl LOSS 390166 IMPROVED; equity DROP 12677603; assets DROP 20824962; debt JUMP 8147359; FTE 174.50; kapitaalsubsidies DROP 1476757; destin691 empty; cash DROP 1016165; leftover city_brasschaat@1179; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_heropbeuring_omzet_jr2025_statutory,{EID},2025,12147825,12147825,12147825,NBB hospital S-vzw code 70 omzet YE2025 JUMP +4.43% (primary L5 envelope; BFM+RIZIV hospital/WZC not commercial-only),{SRC_PDF},strong,tick2378; PDF p3 OCR; YE2024 11632027; 700 verpleegdagprijs 7274801; 703 RIZIV 4508047; 704 29632; 705 151174; 708/709 184171; 701 empty; 702 empty",
    f"bud_heropbeuring_opbr_jr2025_statutory,{EID},2025,17019492,17019492,17019492,NBB hospital S-vzw code 70/74 bedrijfsopbrengsten YE2025 JUMP +3.76%,{SRC_PDF},strong,tick2378; PDF p3 OCR; YE2024 16403572; 74 4863745; 740 5943; T742.9 4857802; 73 7922",
    f"bud_heropbeuring_riziv703_jr2025_statutory,{EID},2025,4508047,4508047,4508047,NBB hospital S-vzw code 703 forfaits conventies RIZIV YE2025 (inside omzet 70),{SRC_PDF},strong,tick2378; PDF p3 OCR; YE2024 4118874; 700 verpleegdagprijs 7274801",
    f"bud_heropbeuring_pnl_jr2025_statutory,{EID},2025,-390166,-390166,-390166,NBB hospital S-vzw code 70/66 verlies van het boekjaar YE2025 IMPROVED -2.74%,{SRC_PDF},strong,tick2378; PDF p4 OCR; YE2024 -401155; bedrijfsverlies 70/64 626869 vs YE2024 765702; destin691 empty",
    f"bud_heropbeuring_equity_jr2025_statutory,{EID},2025,12677603,12677603,12677603,NBB hospital S-vzw code 10/15 eigen vermogen YE2025 DROP -4.67%,{SRC_PDF},strong,tick2378; PDF p2 OCR; YE2024 13298591; kapitaalsubsidies 1476757; overgedragen 14 -4676696",
    f"bud_heropbeuring_assets_jr2025_statutory,{EID},2025,20824962,20824962,20824962,NBB hospital S-vzw code 20/58 totaal activa YE2025 DROP -0.82%,{SRC_PDF},strong,tick2378; PDF p2 OCR; YE2024 20996340",
    f"bud_heropbeuring_debt_jr2025_statutory,{EID},2025,8147359,8147359,8147359,NBB hospital S-vzw code 17/49 schulden incl accruals YE2025 JUMP +5.84%,{SRC_PDF},strong,tick2378; PDF p2 OCR; YE2024 7697748; LT 4016137; ST 3964363; inhaal 403 empty",
    f"bud_heropbeuring_cash_jr2025_statutory,{EID},2025,1016165,1016165,1016165,NBB hospital S-vzw code 54/58 liquide middelen YE2025 DROP -15.42%,{SRC_PDF},strong,tick2378; PDF p2 OCR; YE2024 1201458; geldbeleggingen 51/53 1246085",
    f"bud_heropbeuring_kapitaalsubsidies_jr2025_statutory,{EID},2025,1476757,1476757,1476757,NBB hospital S-vzw code 15 investeringssubsidies YE2025 DROP -13.52%,{SRC_PDF},strong,tick2378; PDF p2 OCR; YE2024 1707579",
    f"bud_heropbeuring_fte_jr2025_statutory,{EID},2025,174.50,174.50,174.50,NBB hospital S-vzw gemiddeld personeelseffectief VTE YE2025 174.50 DROP,{SRC_PDF},strong,tick2378; PDF p5 OCR; YE2024 176.1; personnel 62 12388454; bezoldigingen 9087205; RSZ 2914404; andere 386844",
])

cash_json = (
    '"{""2025_omzet"":12147825,""2025_opbr"":17019492,""2025_700"":7274801,""2025_703"":4508047,'
    '""2025_704"":29632,""2025_705"":151174,""2025_708"":184171,""2025_701"":0,'
    '""2025_73"":7922,""2025_74"":4863745,""2025_740"":5943,""2025_742"":4857802,'
    '""2025_pnl"":-390166,""2025_bedrijfsverlies"":626869,""2025_equity"":12677603,'
    '""2025_assets"":20824962,""2025_debt"":8147359,""2025_fte"":174.50,'
    '""2025_kapitaalsubsidies"":1476757,""2025_destin691"":0,""2025_cash"":1016165,'
    '""2025_geldbeleggingen"":1246085,""2025_personnel62"":12388454,'
    '""2025_gebouwen22"":15882445,""2025_aanbouw27"":42350,'
    '""2024_omzet"":11632027,""2024_opbr"":16403572,""2024_pnl"":-401155,'
    '""2024_bedrijfsverlies"":765702,""2024_equity"":13298591,""2024_assets"":20996340,'
    '""2024_debt"":7697748,""2024_kapitaalsubsidies"":1707579,""2024_cash"":1201458,'
    '""2024_fte"":176.1}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Heropbeuring vzw De Mick YE2025 (omzet 12.15m / 74 4.86m vs 740 5.9k / pnl LOSS 0.39m / Strong PDF),{EID},FOD Volksgezondheid BFM + RIZIV + VAPH De Vrije Vlinder + leftover city_brasschaat,VZW Heropbeuring De Mick (KBO 0406.678.141; Actief; 2 VE; Aanbestedende; RSZ2025 87.301),2026-06-24,2025,2025,12147825,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00197310.pdf,Public hospital+WZC+VAPH dual of mined city_brasschaat,Publish BFM/RIZIV/WZC/VAPH matrix inside omzet 12.15m + explain 74 4.86m vs 740 5.9k + 1.48m kapitaalsubsidies DROP,{SRC_PDF},strong,Vlaanderen>Antwerpen>Brasschaat>Heropbeuring_DeMick>JR2025_statutory_L5,tick2378; Strong official scanned PDF OCR; leftover city_brasschaat@1179; NOT Kloosterstraat 6; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Heropbeuring De Mick omzet 12.15m / 74 4.86m vs 740 5.9k / pnl LOSS 0.39m / 1.48m kapitaalsubsidies (YE2025 hospital+WZC Brasschaat),L5,hospital_wzc_vaph_vzw_statutory,Vlaanderen>Antwerpen>Brasschaat>Heropbeuring_DeMick>JR2025,12147825,12147825,PDF omzet JUMP 12147825 hospital/WZC envelope; 700 7274801; 703 RIZIV 4508047; 704 29632; 705 151174; 708/709 184171; 701 empty; opbr JUMP 17019492; 74 4863745 740 5943 T742.9 4857802; 73 7922; bedrijfsverlies 626869 IMPROVED; pnl LOSS 390166 IMPROVED; equity DROP 12677603; assets DROP 20824962; debt JUMP 8147359; FTE 174.50 DROP; kapitaalsubsidies DROP 1476757; destin691 empty; cash DROP 1016165; geldbeleggingen 1246085; gebouwen 15882445; personnel 12388454,strong,{SRC_PDF},WZC + rehab + VAPH NAH residents Brasschaat,FOD Volksgezondheid BFM + RIZIV + VAPH + leftover city_brasschaat,12.15m hospital/WZC omzet; 4.86m unexplained 74 vs 5.9k 740; pnl LOSS 0.39m; 1.48m kapitaalsubsidies DROP; cash DROP 15%; leftover city_brasschaat,6.1,6.0,5.4,5.92,FOI BFM/RIZIV/WZC/VAPH matrix + 74 4.86m vs 740 5.9k + 1.48m kapitaalsubsidies DROP + cash DROP,active,,tick2378; Strong official NBB scanned PDF OCR + Strong KBO; leftover city_brasschaat@1179; OFF Drongen OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Antwerpen>Brasschaat>Heropbeuring_DeMick>BFM_RIZIV_WZC_VAPH,vzw_heropbeuring,BFM/RIZIV/WZC/VAPH split inside omzet 12147825 + 700 7274801 / 703 4508047; why 74 4863745 vs 740 5943 (T742.9 4857802); nature of kapitaalsubsidies 1476757 DROP and destin 691 empty; pnl LOSS 390166; cash DROP 1016165,Strong official PDF leftover public hospital+WZC+VAPH of city_brasschaat@1179; 12.15m omzet; public not private clinic,8,Heropbeuring VZW / Dirk Schoeters voorzitter RvB,info@demick.be,"Papestraat 30, 2930 Brasschaat",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2378; ready NOT sent; Strong official scanned NBB PDF OCR; after NMSC@2377; leftover city_brasschaat hospital/WZC off Drongen off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2378,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2378 line, found {n}")
if "rq_2379," in rq_text:
    raise SystemExit("rq_2379 already exists")

new_2378 = (
    "rq_2378,leftover dual — Heropbeuring De Mick YE2025 Strong (omzet JUMP 12.15m / 74 4.86m vs 740 5.9k / pnl LOSS 0.39m),"
    "hole_fill,8,done,L5,vzw_heropbeuring,"
    "Tick 2378 leftover after NMSC. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC). "
    "Took Heropbeuring De Mick 0406.678.141 deposit 2026-00197310 leftover city_brasschaat@1179. "
    "Do NOT redo NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:01:26Z,{STAMP},"
    "tick2378 Heropbeuring 0406.678.141 YE2025 Strong official scanned PDF 2026-00197310; omzet JUMP 12147825 hospital/WZC envelope 700 7274801 + RIZIV 703 4508047; opbr JUMP 17019492; 74 4863745 vs 740 5943; pnl LOSS 390166 IMPROVED; equity DROP 12677603; assets DROP 20824962; debt JUMP 8147359; FTE 174.50; kapitaalsubsidies DROP 1476757; destin691 empty; cash DROP 1016165; FOI ready NOT sent; leftover city_brasschaat@1179; OFF Drongen OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2378,"):
        parts.append(new_2378)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2378 replace count {replaced}")
new_rq = "".join(parts)
new_2379 = (
    "rq_2379,leftover dual after Heropbeuring De Mick — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Heropbeuring De Mick YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141). "
    "Do NOT redo Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2378; Heropbeuring De Mick taken leftover city_brasschaat; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2379
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2378 + rq_2379; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2378,2378,no,"
    "tick2378 leftover dual Heropbeuring De Mick 0406.678.141 Strong scanned PDF (omzet JUMP 12147825 hospital/WZC envelope 700 7274801 + RIZIV 703 4508047; opbr JUMP 17019492; 74 4863745 vs 740 5943; pnl LOSS 390166 IMPROVED; equity DROP 12677603; assets DROP 20824962; debt JUMP 8147359; FTE 174.50; kapitaalsubsidies DROP 1476757; destin691 empty; cash DROP 1016165; 2 VE Aanbestedende RSZ2025 87.301); leftover city_brasschaat@1179; OFF Drongen OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2379; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2378 - rq_2378 Heropbeuring De Mick Brasschaat (omzet JUMP 12.15m / 74 4.86m vs 740 5.9k / pnl LOSS 0.39m / Strong PDF)

- Unit: **rq_2378** leftover dual after **NMSC@2377**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; FARO 2026-00010398 is YE2024; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Vanheylenstraat 16 same-zetel hunt not taken (optional). Took FREE leftover Flemish **Heropbeuring VZW (De Mick)** YE2025 (KBO **0406.678.141**; zetel Papestraat 30, 2930 Brasschaat; **Actief** **2 VE** **2.152.235.703** Heropbeuring + **2.384.771.625** De Vrije Vlinder; **Aanbestedende overheid**; RSZ2025 **87.301**; leftover of mined **city_brasschaat@1179** / leftover after **agb_brasschaat@1179** / **zorg_zbb@1339**; info@demick.be). Confirmed leftover public (RIZIV/FOD hospital envelope + ROB/WZC + VAPH De Vrije Vlinder) not private clinic / not Immobiliën De Mick NV 0428.245.694. Do not redo NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB hospital-schema S-vzw scanned PDF deposit **2026-00197310** (9025650 B / 23p; AV **23.06.2026**; header **24.06.2026**; CDN Last-Modified **09.07.2026**) — omzet 70 **EUR12147825** JUMP +4.43% (hospital/WZC envelope; not commercial-only); 700 verpleegdagprijs **7274801** + 703 RIZIV **4508047** + 704 **29632** + 705 **151174** + 708/709 **184171**; 701/702 empty; bedrijfsopbrengsten 70/74 **EUR17019492** JUMP +3.76%; 74 **4863745** (740 only **5943**; T742.9 **4857802**); 73 **7922**; bedrijfsverlies **EUR626869** IMPROVED from 765702; pnl 70/66 LOSS **EUR390166** IMPROVED −2.74%; equity **EUR12677603** DROP −4.67%; assets **EUR20824962** DROP −0.82%; debt **EUR8147359** JUMP +5.84%; FTE **174.50** DROP vs 176.1; kapitaalsubsidies **EUR1476757** DROP −13.52%; destin 691/2 **empty**; cash **EUR1016165** DROP −15.42%; geldbeleggingen **EUR1246085**; gebouwen **EUR15882445**; aanbouw **EUR42350**; personeel 62 **EUR12388454**. Strong KBO + Strong PDF (OCR of official scan; not SBM table; smaller than NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.92); entities (+1 vzw_heropbeuring); foi + draft `{GAP}`; rq_2378=done + rq_2379 open; loop_state ticks=2378; raw tick2378/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2379 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Zeepreventorium still YE2024.

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
