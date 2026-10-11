#!/usr/bin/env python3
"""Surgical tick 2383 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_vijvens"
SRC_PDF = "src_vijvens_jr2025_nbb_pdf_2383"
SRC_KBO = "src_vijvens_kbo_2383"
SRC_SBM = "src_vijvens_sbm_2383"
SRC_SITE = "src_vijvens_site_2383"
COMM = "comm_vijvens_jr2025_statutory_omzet_14_42m_pnl_loss_325k"
LB = "lb_vijvens_omzet_14_42m_pnl_loss_325k_jr2025"
GAP = "gap_vijvens_zorgkas_riziv_wzc_matrix_omzet_14_42m_73_3_00m_pnl_loss_3_97m_kapitaalsubsidies_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Vijvens Kruisem deposit 2026-00192587,http://cdn.staatsbladmonitor.be/2026pdf/2026-00192587.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2383; official native PDF 3126398 bytes 44p VOL-VZW 26.0.15 m05-f; header 19.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 14:04:56 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope",
    f"{SRC_KBO},KBO Vijvens vzw 0415.093.385,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415093385,KBO Public Search FOD Economie,{DAY},official_register,tick2383; Actief; 5 VE 2.138.402.414 Home Vijvens Kloosterstraat 18 9750 Kruisem (NOT Kloosterstraat 6) + 2.138.402.513 WZC CKV Home Sint-Petrus Passionistenstraat 19 + 2.251.030.203 CDV De Marolle Passionistenstraat 21 + 2.331.119.242 GAW Residentie Celestin Passionistenstraat 13 + 2.331.119.539 GAW Residentie Kruiskouter Passionistenstraat 23; zetel Passionistenstraat 19 9770 Kruisem since 09.11.2022; RSZ2025 87.301 ROB; voorzitter Rita Vande Moortele; commissaris Steven Vanderhaegen A01944 0708.852.343 tot 30.06.2027",
    f"{SRC_SBM},Staatsbladmonitor fiche Vijvens 0415093385 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0415093385,Staatsbladmonitor,{DAY},official_register,tick2383; deposit-id 2026-00192587 and CDN Last-Modified 2026-07-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Vijvens FOI contact / WZC Kruisem campuses,https://www.vijvens.be/,Vijvens vzw,{DAY},foi_contact,tick2383; FOI info@vijvens.be; zetel Passionistenstraat 19 9770 Kruisem; leftover city_kruisem; Home Vijvens Kloosterstraat 18 9750 NOT Kloosterstraat 6; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Vijvens VZW (WZC Kruisem / Home Sint-Petrus + Home Vijvens + CDV De Marolle + GAW Celestin + GAW Kruiskouter),Vijvens ASBL (MRS Kruisem / Home Sint-Petrus + Home Vijvens),Vijvens VZW (nursing home Kruisem / Home Sint-Petrus + Home Vijvens),parastatal,city_kruisem,nl,https://www.vijvens.be/,info@vijvens.be,"Passionistenstraat 19, 9770 Kruisem",tick2383 YE2025 Strong official native NBB PDF deposit 2026-00192587 + Strong KBO 0415.093.385 Actief 5 VE RSZ2025 87.301; omzet JUMP 14419264 WZC envelope; 73 DROP 3003987; opbr JUMP 17792660; pnl LOSS FLIP -324755; equity DROP 12145996; assets DROP 36901501; debt DROP 24755505; FTE 173.9; kapitaalsubsidies DROP 3971620; destin691 empty; 791 324755; cash JUMP 1112531; uitzend JUMP 645194; leftover city_kruisem after CAR DAT@2382; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_vijvens_omzet_jr2025_statutory,{EID},2025,14419264,14419264,14419264,NBB VOL-VZW code 70 omzet YE2025 JUMP +2.28% (primary L5 envelope; WZC ouderenzorg 100% not commercial-only),{SRC_PDF},strong,tick2383; PDF p7 native; YE2024 14097507; 73 3003987; opbr 17792660",
    f"bud_vijvens_opbr_jr2025_statutory,{EID},2025,17792660,17792660,17792660,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.44%,{SRC_PDF},strong,tick2383; PDF p7 native; YE2024 17368846; 74 317274; 76A 52135",
    f"bud_vijvens_subs73_jr2025_statutory,{EID},2025,3003987,3003987,3003987,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -2.03%,{SRC_PDF},strong,tick2383; PDF p7+p22 native; YE2024 3066293; 733 3003987; 730/731/732 empty",
    f"bud_vijvens_pnl_jr2025_statutory,{EID},2025,-324755,-324755,-324755,NBB VOL-VZW code 9904 winst (verlies) van het boekjaar YE2025 LOSS FLIP,{SRC_PDF},strong,tick2383; PDF p8 native; YE2024 +99736; bedrijfswinst 9901 289655 DROP vs 763954; destin691 empty; 791 324755",
    f"bud_vijvens_equity_jr2025_statutory,{EID},2025,12145996,12145996,12145996,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -4.20%,{SRC_PDF},strong,tick2383; PDF p6 native; YE2024 12678790; kapitaalsubsidies 3971620; fondsen 10 793790; bestemde 13 7380587",
    f"bud_vijvens_assets_jr2025_statutory,{EID},2025,36901501,36901501,36901501,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -5.94%,{SRC_PDF},strong,tick2383; PDF p5 native; YE2024 39233439",
    f"bud_vijvens_debt_jr2025_statutory,{EID},2025,24755505,24755505,24755505,NBB VOL-VZW code 17/49 schulden YE2025 DROP -6.78%,{SRC_PDF},strong,tick2383; PDF p6 native; YE2024 26554650; LT 20425611; ST 4168480; krediet 173 20174878",
    f"bud_vijvens_cash_jr2025_statutory,{EID},2025,1112531,1112531,1112531,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +59.50%,{SRC_PDF},strong,tick2383; PDF p5 native; YE2024 697514; geldbeleggingen 50/53 201463 DROP vs 877239",
    f"bud_vijvens_kapitaalsubsidies_jr2025_statutory,{EID},2025,3971620,3971620,3971620,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -4.98%,{SRC_PDF},strong,tick2383; PDF p6 native; YE2024 4179658",
    f"bud_vijvens_fte_jr2025_statutory,{EID},2025,173.9,173.9,173.9,NBB VOL-VZW gemiddeld personeelseffectief VTE YE2025 173.9 DROP -1.42%,{SRC_PDF},strong,tick2383; PDF p22 native; YE2024 176.4; koppen 9086 210 vs 215; personnel 62 11381980; uitzend 617 645194 JUMP vs 313878; 9097 4.0",
])

cash_json = (
    '"{""2025_omzet"":14419264,""2025_opbr"":17792660,""2025_73"":3003987,'
    '""2025_733"":3003987,""2025_74"":317274,""2025_76A"":52135,'
    '""2025_pnl"":-324755,""2025_bedrijfswinst"":289655,'
    '""2025_equity"":12145996,""2025_assets"":36901501,""2025_debt"":24755505,'
    '""2025_fte"":173.9,""2025_kapitaalsubsidies"":3971620,'
    '""2025_destin691"":0,""2025_791"":324755,""2025_cash"":1112531,'
    '""2025_geldbeleggingen"":201463,""2025_personnel62"":11381980,'
    '""2025_uitzend617"":645194,""2025_diensten61"":3166387,'
    '""2025_gebouwen22"":31040977,""2025_aanbouw27"":10032,'
    '""2025_capex8161"":13762,""2025_fondsen10"":793790,'
    '""2025_bestemde13"":7380587,""2025_fin_kosten65"":622377,'
    '""2024_omzet"":14097507,""2024_opbr"":17368846,'
    '""2024_73"":3066293,""2024_pnl"":99736,""2024_bedrijfswinst"":763954,'
    '""2024_equity"":12678790,""2024_assets"":39233439,""2024_debt"":26554650,'
    '""2024_kapitaalsubsidies"":4179658,""2024_cash"":697514,""2024_fte"":176.4,'
    '""2024_destin691"":99736,""2024_geldbeleggingen"":877239,'
    '""2024_uitzend617"":313878}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Vijvens vzw Kruisem YE2025 (omzet 14.42m / 73 3.00m / pnl LOSS 325k / destin empty / Strong PDF),{EID},Vlaamse zorgkas + Departement Zorg + leftover city_kruisem,VZW Vijvens (KBO 0415.093.385; Actief; 5 VE; RSZ2025 87.301),2026-06-19,2025,2025,14419264,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00192587.pdf,Public WZC dual of mined city_kruisem,Publish zorgkas/RIZIV/WZC matrix inside omzet 14.42m + explain 73 3.00m DROP + pnl LOSS FLIP 325k + destin empty + 791 325k + kapitaalsubsidies 3.97m DROP + uitzend JUMP 645k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Kruisem>Vijvens_WZC>JR2025_statutory_L5,tick2383; Strong official native PDF; leftover city_kruisem after CAR DAT@2382; NOT Kloosterstraat 6; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Vijvens Kruisem omzet 14.42m / 73 3.00m / pnl LOSS FLIP 325k / destin empty (YE2025 Kruisem),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Kruisem>Vijvens_WZC>JR2025,14419264,14419264,PDF omzet JUMP 14419264 WZC envelope; 73 DROP 3003987; opbr JUMP 17792660; bedrijfswinst DROP 289655; pnl LOSS FLIP -324755; equity DROP 12145996; assets DROP 36901501; debt DROP 24755505; FTE 173.9 DROP; kapitaalsubsidies DROP 3971620; destin691 empty; 791 324755; cash JUMP 1112531; geldbeleggingen DROP 201463; gebouwen 31040977; uitzend JUMP 645194,strong,{SRC_PDF},elderly residents Kruisem WZC+CKV+CDV+GAW,Vlaamse zorgkas + Departement Zorg + leftover city_kruisem,14.42m WZC omzet; 3.00m 73 subsidies DROP; pnl LOSS FLIP 325k; destin empty; 3.97m kapitaalsubsidies DROP; uitzend JUMP 645k; leftover city_kruisem,6.0,6.2,5.5,5.90,FOI zorgkas/RIZIV/WZC matrix + 73 3.00m DROP + pnl LOSS FLIP 325k + destin empty + 3.97m kapitaalsubsidies DROP + uitzend JUMP 645k,active,,tick2383; Strong official NBB native PDF + Strong KBO; leftover city_kruisem after CAR DAT@2382; OFF Drongen OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Kruisem>Vijvens_WZC>zorgkas_RIZIV_WZC,{EID},zorgkas/RIZIV/WZC split inside omzet 14419264; why 73 3003987 DROP; why pnl -324755 LOSS FLIP; nature of destin 691 empty and 791 324755 onttrekking from bestemde fondsen 7380587; kapitaalsubsidies 3971620 DROP; cash JUMP 1112531 vs beleggingen DROP 201463; uitzend 617 645194 JUMP; debt 24755505,Strong official PDF leftover public WZC of city_kruisem; 14.42m omzet; public not private clinic,8,Vijvens VZW / Rita Vande Moortele voorzitter,info@vijvens.be,"Passionistenstraat 19, 9770 Kruisem",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2383; ready NOT sent; Strong official native NBB PDF; leftover city_kruisem WZC after CAR DAT@2382; off Drongen off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2383,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2383 line, found {n}")
if "rq_2384," in rq_text:
    raise SystemExit("rq_2384 already exists")

new_2383 = (
    "rq_2383,leftover dual — Vijvens WZC Kruisem YE2025 Strong (omzet JUMP 14.42m / 73 3.00m / pnl LOSS FLIP 325k / destin empty),"
    "hole_fill,8,done,L5,vzw_vijvens,"
    "Tick 2383 leftover after CAR DAT. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT). "
    "Took Vijvens Kruisem 0415.093.385 deposit 2026-00192587 leftover city_kruisem. "
    "Do NOT redo CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:38:22Z,{STAMP},"
    "tick2383 Vijvens 0415.093.385 YE2025 Strong official native PDF 2026-00192587; omzet JUMP 14419264 WZC ouderenzorg envelope; 73 DROP 3003987 (733 3003987); opbr JUMP 17792660; pnl LOSS FLIP -324755; equity DROP 12145996; assets DROP 36901501; debt DROP 24755505; FTE 173.9; kapitaalsubsidies DROP 3971620; destin691 empty; 791 324755; cash JUMP 1112531; uitzend JUMP 645194; FOI ready NOT sent; leftover city_kruisem after CAR DAT@2382; OFF Drongen OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2383,"):
        parts.append(new_2383)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2383 replace count {replaced}")
new_rq = "".join(parts)
new_2384 = (
    "rq_2384,leftover dual after Vijvens — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Vijvens Kruisem YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385). "
    "Do NOT redo Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2383; Vijvens taken leftover city_kruisem after CAR DAT; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2384
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2383 + rq_2384; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2383,2383,no,"
    "tick2383 leftover dual Vijvens WZC Kruisem 0415.093.385 Strong native PDF (omzet JUMP 14419264 WZC envelope; 73 DROP 3003987; opbr JUMP 17792660; pnl LOSS FLIP -324755; equity DROP 12145996; assets DROP 36901501; debt DROP 24755505; FTE 173.9; kapitaalsubsidies DROP 3971620; destin691 empty; 791 324755; cash JUMP 1112531; uitzend JUMP 645194; 5 VE RSZ2025 87.301); leftover city_kruisem after CAR DAT@2382; OFF Drongen OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2384; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2383 - rq_2383 Vijvens WZC Kruisem (omzet JUMP 14.42m / 73 3.00m / pnl LOSS FLIP 325k / destin empty / Strong PDF)

- Unit: **rq_2383** leftover dual after **CAR DAT@2382**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Zeepreventorium still **YE2024**. De Bolster 0861.680.989 still **YE2024**. Zwarte Zusters 0413.272.260 **stopgezet 26.06.2000** (skip). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Vijvens VZW (WZC Kruisem)** YE2025 (KBO **0415.093.385**; zetel Passionistenstraat 19, 9770 Kruisem; **Actief** **5 VE** **2.138.402.414** Home Vijvens Kloosterstraat 18 9750 (NOT Kloosterstraat 6) + **2.138.402.513** WZC/CKV Home Sint-Petrus + **2.251.030.203** CDV De Marolle + **2.331.119.242** GAW Célestin + **2.331.119.539** GAW Kruiskouter; RSZ2025 **87.301**; leftover of mined **city_kruisem@932**; info@vijvens.be). Confirmed leftover public (Departement Zorg WZC Home Sint-Petrus HCO 3738 + CKV + CDV + GAW) not private clinic / not CAR DAT 0463.347.917 / not H.Hart 0407.644.082 / not Sint-Vincentius Zulte / not Floordam / not NMSC. Do not redo CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW native PDF deposit **2026-00192587** (3126398 B / 44p; AV **17.06.2026**; header **19.06.2026**; CDN Last-Modified **07.07.2026**) — omzet 70 **EUR14419264** JUMP +2.28% (WZC ouderenzorg envelope; not commercial-only; 100% categorie Ouderenzorg); 73 **EUR3003987** DROP −2.03% (733 **3003987**); bedrijfsopbrengsten 70/76A **EUR17792660** JUMP +2.44%; 74 **317274**; 76A **52135**; bedrijfswinst 9901 **EUR289655** DROP −62.08%; pnl 9904 **EUR−324755** LOSS FLIP (was +99736); equity **EUR12145996** DROP −4.20%; assets **EUR36901501** DROP −5.94%; debt **EUR24755505** DROP −6.78%; FTE **173.9** DROP −1.42%; kapitaalsubsidies **EUR3971620** DROP −4.98%; destin 691 **empty**; 791 **EUR324755**; cash **EUR1112531** JUMP +59.50%; geldbeleggingen **EUR201463** DROP −77.03%; gebouwen **EUR31040977**; aanbouw **EUR10032**; capex 8161 **EUR13762**; personeel 62 **EUR11381980**; uitzend 617 **EUR645194** JUMP +105.56%. Strong KBO + Strong PDF (native text; not SBM table; not Companyweb euros; smaller than Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.90); entities (+1 vzw_vijvens); foi + draft `{GAP}`; rq_2383=done + rq_2384 open; loop_state ticks=2383; raw tick2383/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2390**). Next: rq_2384 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Vijvens / NOT CAR DAT / NOT H.Hart Oudenaarde / NOT Sint-Vincentius Zulte / NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). De Bolster 0861.680.989 still YE2024 public file. School Perk 0417.085.845 only if leftover school of mined parent is in priority. Zeepreventorium still YE2024.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
