#!/usr/bin/env python3
"""Surgical tick 2381 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_hhart"
SRC_PDF = "src_hhart_jr2025_nbb_pdf_2381"
SRC_KBO = "src_hhart_kbo_2381"
SRC_SBM = "src_hhart_sbm_2381"
SRC_SITE = "src_hhart_site_2381"
COMM = "comm_hhart_jr2025_statutory_omzet_9_56m_pnl_loss_1_63m_kapitaalsubsidies"
LB = "lb_hhart_omzet_9_56m_pnl_loss_1_63m_kapitaalsubsidies_jr2025"
GAP = "gap_hhart_zorgkas_riziv_wzc_matrix_omzet_9_56m_73_1_88m_pnl_loss_1_63m_kapitaalsubsidies_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Woonzorgcentrum H.Hart Oudenaarde deposit 2026-00191760,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191760.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2381; official native PDF 1809987 bytes 53p VOL-VZW 26.0.15 m05-f; header 24.06.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 10:18:05 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Belscope",
    f"{SRC_KBO},KBO Woonzorgcentrum H.Hart vzw 0407.644.082,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407644082,KBO Public Search FOD Economie,{DAY},official_register,tick2381; Actief; 2 VE; zetel Marlboroughlaan 3 9700 Oudenaarde since 05.10.1970; RSZ2025 87.301 ROB; BTW 87.101 RVT; voorzitter Fernand Maes; ondervoorzitter Anne Saveyn; commissaris Baker Tilly / Christel De Blander tot 30.06.2027; related 0413.272.260 Vereniging der Zwarte Zusters van Oudenaarde",
    f"{SRC_SBM},Staatsbladmonitor fiche Woonzorgcentrum H.Hart vzw 0407644082 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0407644082,Staatsbladmonitor,{DAY},official_register,tick2381; deposit-id 2026-00191760 and CDN Last-Modified 2026-07-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC H.Hart Oudenaarde FOI contact / WZC Oudenaarde,https://www.wzchhart.be/,Woonzorgcentrum H.Hart vzw,{DAY},foi_contact,tick2381; FOI info@wzchhart.be; PDF email marc.saveyn@wzchhart.be; zetel Marlboroughlaan 3 9700 Oudenaarde; campus Kloosterhof Pamele Grachtschelde 2; leftover city_oudenaarde; NOT Kloosterstraat 6; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Woonzorgcentrum H.Hart VZW (WZC Oudenaarde / ouderenzorg + kortverblijf + herstelverblijf + dagverzorging + Kloosterhof Pamele),Woonzorgcentrum H.Hart ASBL (MRS Audenarde),Woonzorgcentrum H.Hart VZW (WZC Oudenaarde),parastatal,city_oudenaarde,nl,https://www.wzchhart.be/,info@wzchhart.be,"Marlboroughlaan 3, 9700 Oudenaarde",tick2381 YE2025 Strong official native NBB PDF deposit 2026-00191760 + Strong KBO 0407.644.082 Actief 2 VE RSZ2025 87.301; omzet JUMP 9557481 WZC ouderenzorg envelope; 73 DROP 1878216 (733 1876986); opbr JUMP 11503252; pnl LOSS IMPROVED -60237; equity DROP 8682349; assets DROP 13168996; debt DROP 4486648; FTE 131.5; kapitaalsubsidies DROP 1634174; destin691 empty; cash DROP 632715; leftover city_oudenaarde after Sint-Vincentius@2380; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_hhart_omzet_jr2025_statutory,{EID},2025,9557481,9557481,9557481,NBB VOL-VZW code 70 omzet YE2025 JUMP +4.59% (primary L5 envelope; WZC ouderenzorg not commercial-only),{SRC_PDF},strong,tick2381; PDF p7 native; YE2024 9138214; 73 1878216 of which 733 1876986; categorie-uitsplitsing empty",
    f"bud_hhart_opbr_jr2025_statutory,{EID},2025,11503252,11503252,11503252,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +3.38%,{SRC_PDF},strong,tick2381; PDF p7 native; YE2024 11126596; 74 67480; 76A 75",
    f"bud_hhart_subs73_jr2025_statutory,{EID},2025,1878216,1878216,1878216,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -0.46%,{SRC_PDF},strong,tick2381; PDF p7+p21 native; YE2024 1886904; 733 1876986; 731 1230; 730 empty; 732 empty",
    f"bud_hhart_pnl_jr2025_statutory,{EID},2025,-60237,-60237,-60237,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 LOSS IMPROVED,{SRC_PDF},strong,tick2381; PDF p8 native; YE2024 -135418; bedrijfswinst 9901 -45154 IMPROVED vs YE2024 -101370; destin691 empty",
    f"bud_hhart_equity_jr2025_statutory,{EID},2025,8682349,8682349,8682349,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -2.31%,{SRC_PDF},strong,tick2381; PDF p6 native; YE2024 8887307; kapitaalsubsidies 1634174; overgedragen 14 -451953; fondsen 10 7500128",
    f"bud_hhart_assets_jr2025_statutory,{EID},2025,13168996,13168996,13168996,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -5.19%,{SRC_PDF},strong,tick2381; PDF p5 native; YE2024 13890397",
    f"bud_hhart_debt_jr2025_statutory,{EID},2025,4486648,4486648,4486648,NBB VOL-VZW code 17/49 schulden incl accruals YE2025 DROP -10.32%,{SRC_PDF},strong,tick2381; PDF p6 native; YE2024 5003091; LT 2043353; ST 2436093",
    f"bud_hhart_cash_jr2025_statutory,{EID},2025,632715,632715,632715,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -24.38%,{SRC_PDF},strong,tick2381; PDF p5 native; YE2024 836685; geldbeleggingen 50/53 2089862 JUMP vs 2055690",
    f"bud_hhart_kapitaalsubsidies_jr2025_statutory,{EID},2025,1634174,1634174,1634174,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -8.14%,{SRC_PDF},strong,tick2381; PDF p6 native; YE2024 1778895",
    f"bud_hhart_fte_jr2025_statutory,{EID},2025,131.5,131.5,131.5,NBB VOL-VZW gemiddeld personeelseffectief VTE YE2025 131.5 DROP -1.50%,{SRC_PDF},strong,tick2381; PDF p21 native; YE2024 133.5; koppen 9086 175 vs 179; personnel 62 8878519; uitzend 617 empty",
])

cash_json = (
    '"{""2025_omzet"":9557481,""2025_opbr"":11503252,""2025_73"":1878216,'
    '""2025_731"":1230,""2025_733"":1876986,""2025_74"":67480,""2025_76A"":75,'
    '""2025_pnl"":-60237,""2025_bedrijfswinst"":-45154,""2025_equity"":8682349,'
    '""2025_assets"":13168996,""2025_debt"":4486648,""2025_fte"":131.5,'
    '""2025_kapitaalsubsidies"":1634174,""2025_destin691"":0,""2025_cash"":632715,'
    '""2025_geldbeleggingen"":2089862,""2025_personnel62"":8878519,'
    '""2025_uitzend617"":0,""2025_gebouwen22"":6692603,'
    '""2025_aanbouw27"":1515990,""2025_fondsen10"":7500128,'
    '""2024_omzet"":9138214,""2024_opbr"":11126596,'
    '""2024_73"":1886904,""2024_pnl"":-135418,""2024_bedrijfswinst"":-101370,'
    '""2024_equity"":8887307,""2024_assets"":13890397,""2024_debt"":5003091,'
    '""2024_kapitaalsubsidies"":1778895,""2024_cash"":836685,""2024_fte"":133.5,'
    '""2024_destin691"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Woonzorgcentrum H.Hart vzw WZC Oudenaarde YE2025 (omzet 9.56m / 73 1.88m / pnl LOSS 60k / 1.63m kapitaalsubsidies / Strong PDF),{EID},Vlaamse zorgkas + Departement Zorg + leftover city_oudenaarde,VZW Woonzorgcentrum H.Hart (KBO 0407.644.082; Actief; 2 VE; RSZ2025 87.301),2026-06-24,2025,2025,9557481,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191760.pdf,Public WZC dual of mined city_oudenaarde,Publish zorgkas/RIZIV/resident-fee matrix inside omzet 9.56m + explain 73 1.88m DROP + pnl LOSS 60k + kapitaalsubsidies 1.63m DROP + destin 691 empty,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Oudenaarde>HHart_WZC>JR2025_statutory_L5,tick2381; Strong official native PDF; leftover city_oudenaarde after Sint-Vincentius@2380; NOT Kloosterstraat 6; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},H.Hart Oudenaarde WZC omzet 9.56m / 73 1.88m / pnl LOSS 60k / 1.63m kapitaalsubsidies (YE2025 Oudenaarde),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Oudenaarde>HHart_WZC>JR2025,9557481,9557481,PDF omzet JUMP 9557481 WZC ouderenzorg envelope; 73 DROP 1878216 (733 1876986); opbr JUMP 11503252; 74 67480; bedrijfswinst IMPROVED -45154; pnl LOSS IMPROVED -60237; equity DROP 8682349; assets DROP 13168996; debt DROP 4486648; FTE 131.5 DROP; kapitaalsubsidies DROP 1634174; destin691 empty; cash DROP 632715; geldbeleggingen JUMP 2089862; gebouwen 6692603; aanbouw 1515990; personnel 8878519,strong,{SRC_PDF},WZC + kortverblijf + herstelverblijf + dagverzorging + Kloosterhof Pamele residents Oudenaarde,Vlaamse zorgkas + Departement Zorg + leftover city_oudenaarde,9.56m WZC omzet; 1.88m 73 subsidies DROP; pnl LOSS 60k IMPROVED; 1.63m kapitaalsubsidies DROP; destin empty; leftover city_oudenaarde,5.8,5.7,5.5,5.62,FOI zorgkas/RIZIV/resident-fee matrix + 73 1.88m DROP + pnl LOSS 60k + 1.63m kapitaalsubsidies DROP + destin empty,active,,tick2381; Strong official NBB native PDF + Strong KBO; leftover city_oudenaarde after Sint-Vincentius@2380; OFF Drongen OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Oudenaarde>HHart_WZC>zorgkas_RIZIV_WZC,vzw_hhart,zorgkas/RIZIV/resident-fee split inside omzet 9557481; why 73 1878216 DROP (733 1876986); nature of kapitaalsubsidies 1634174 DROP and destin 691 empty; pnl LOSS 60237 IMPROVED; cash DROP 632715 vs beleggingen JUMP 2089862; aanbouw 1515990 3e campus; related 0413.272.260 Zwarte Zusters,Strong official PDF leftover public WZC of city_oudenaarde; 9.56m omzet; public not private clinic,8,Woonzorgcentrum H.Hart VZW / Fernand Maes voorzitter RvB,info@wzchhart.be,"Marlboroughlaan 3, 9700 Oudenaarde",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2381; ready NOT sent; Strong official native NBB PDF; leftover city_oudenaarde WZC after Sint-Vincentius@2380; off Drongen off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2381,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2381 line, found {n}")
if "rq_2382," in rq_text:
    raise SystemExit("rq_2382 already exists")

new_2381 = (
    "rq_2381,leftover dual — Woonzorgcentrum H.Hart Oudenaarde YE2025 Strong (omzet JUMP 9.56m / 73 1.88m / pnl LOSS 60k / 1.63m kapitaalsubsidies),"
    "hole_fill,8,done,L5,vzw_hhart,"
    "Tick 2381 leftover after Sint-Vincentius Zulte. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte). "
    "Took Woonzorgcentrum H.Hart Oudenaarde 0407.644.082 deposit 2026-00191760 leftover city_oudenaarde. "
    "Do NOT redo Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:22:44Z,{STAMP},"
    "tick2381 H.Hart Oudenaarde 0407.644.082 YE2025 Strong official native PDF 2026-00191760; omzet JUMP 9557481 WZC ouderenzorg envelope; 73 DROP 1878216 (733 1876986); opbr JUMP 11503252; pnl LOSS IMPROVED -60237; equity DROP 8682349; assets DROP 13168996; debt DROP 4486648; FTE 131.5; kapitaalsubsidies DROP 1634174; destin691 empty; cash DROP 632715; FOI ready NOT sent; leftover city_oudenaarde after Sint-Vincentius@2380; OFF Drongen OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2381,"):
        parts.append(new_2381)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2381 replace count {replaced}")
new_rq = "".join(parts)
new_2382 = (
    "rq_2382,leftover dual after H.Hart Oudenaarde — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Woonzorgcentrum H.Hart Oudenaarde YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082). "
    "Do NOT redo H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2381; H.Hart Oudenaarde WZC taken leftover city_oudenaarde after Sint-Vincentius Zulte; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2382
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2381 + rq_2382; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2381,2381,no,"
    "tick2381 leftover dual Woonzorgcentrum H.Hart Oudenaarde 0407.644.082 Strong native PDF (omzet JUMP 9557481 WZC ouderenzorg envelope; 73 DROP 1878216 733 1876986; opbr JUMP 11503252; pnl LOSS IMPROVED -60237; equity DROP 8682349; assets DROP 13168996; debt DROP 4486648; FTE 131.5; kapitaalsubsidies DROP 1634174; destin691 empty; cash DROP 632715; 2 VE RSZ2025 87.301); leftover city_oudenaarde after Sint-Vincentius@2380; OFF Drongen OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2382; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2381 - rq_2381 Woonzorgcentrum H.Hart Oudenaarde (omzet JUMP 9.56m / 73 1.88m / pnl LOSS 60k / 1.63m kapitaalsubsidies / Strong PDF)

- Unit: **rq_2381** leftover dual after **Sint-Vincentius Zulte@2380**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Woonzorgcentrum H.Hart VZW (WZC Oudenaarde)** YE2025 (KBO **0407.644.082**; zetel Marlboroughlaan 3, 9700 Oudenaarde; **Actief** **2 VE**; RSZ2025 **87.301** ROB; leftover of mined **city_oudenaarde**; info@wzchhart.be). Confirmed leftover public (Departement Zorg WZC + kortverblijf + herstelverblijf + dagverzorging + campus Kloosterhof Pamele + 3e campus in opbouw) not private clinic / not Sint-Vincentius Zulte 0448.633.413 / not Floordam / not NMSC. Do not redo Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW native PDF deposit **2026-00191760** (1809987 B / 53p; AV **23.06.2026**; header **24.06.2026**; CDN Last-Modified **07.07.2026**) — omzet 70 **EUR9557481** JUMP +4.59% (WZC ouderenzorg envelope; not commercial-only); 73 **EUR1878216** DROP −0.46% (733 **1876986**; 731 **1230**); bedrijfsopbrengsten 70/76A **EUR11503252** JUMP +3.38%; 74 **67480**; 76A **75**; bedrijfswinst 9901 **EUR−45154** IMPROVED; pnl 9904 **EUR−60237** IMPROVED; equity **EUR8682349** DROP −2.31%; assets **EUR13168996** DROP −5.19%; debt **EUR4486648** DROP −10.32%; FTE **131.5** DROP −1.50%; kapitaalsubsidies **EUR1634174** DROP −8.14%; destin 691 **empty**; cash **EUR632715** DROP −24.38%; geldbeleggingen **EUR2089862** JUMP; gebouwen **EUR6692603**; aanbouw **EUR1515990**; personeel 62 **EUR8878519**; uitzend 617 empty. Strong KBO + Strong PDF (native text; not SBM table; smaller than Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.62); entities (+1 vzw_hhart); foi + draft `{GAP}`; rq_2381=done + rq_2382 open; loop_state ticks=2381; raw tick2381/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2390**). Next: rq_2382 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT H.Hart Oudenaarde / NOT Sint-Vincentius Zulte / NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Candidate leftover same-parent 0413.272.260 Vereniging der Zwarte Zusters van Oudenaarde only if public + live 2026pdf. School Perk 0417.085.845 only if leftover school of mined parent is in priority. Zeepreventorium still YE2024.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
