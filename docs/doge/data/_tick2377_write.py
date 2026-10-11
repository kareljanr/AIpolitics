#!/usr/bin/env python3
"""Surgical tick 2377 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_nmsc"
SRC_PDF = "src_nmsc_jr2025_nbb_pdf_2377"
SRC_KBO = "src_nmsc_kbo_2377"
SRC_SBM = "src_nmsc_sbm_2377"
SRC_SITE = "src_nmsc_site_2377"
COMM = "comm_nmsc_jr2025_statutory_omzet_28_75m_pnl_jump"
LB = "lb_nmsc_omzet_28_75m_pnl_jump_jr2025"
GAP = "gap_nmsc_bfm_riziv_inhaal_matrix_omzet_28_75m_622k_destin_471k_kapitaalsubsidies_l5"
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
    f"{SRC_PDF},NBB hospital-schema S-vzw jaarrekening 2025 NMSC vzw deposit 2026-00194601,http://cdn.staatsbladmonitor.be/2026pdf/2026-00194601.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2377; official scanned PDF 17161407 bytes 43p S-vzw 26.0.15 m140-f-p hospital KB 19 juni 2007; header 22.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-09; CreationDate 2026-06-22 11:23:01 UTC Canon iR-ADV C5850 + OpenPDF 1.3.26; euros OCR from official PDF pages not SBM table",
    f"{SRC_KBO},KBO Nationaal Multiple Sclerose Centrum vzw 0410.338.110,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410338110,KBO Public Search FOD Economie,{DAY},official_register,tick2377; Actief; 1 VE 2.150.746.059; zetel Vanheylenstraat 16 1820 Steenokkerzeel since 01.10.1990; Aanbestedende overheid since 18.03.1970; RSZ2025 86.103; voorzitter Dirk De Ridder; gedelegeerd bestuurder EVDH Consulting / Eric Vanderheyden since 23.06.2017",
    f"{SRC_SBM},Staatsbladmonitor fiche NMSC vzw 0410338110 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410338110,Staatsbladmonitor,{DAY},official_register,tick2377; deposit-id 2026-00194601 and CDN Last-Modified 2026-07-09; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},NMSC vzw FOI contact / categoraal MS-revalidatieziekenhuis Melsbroek,https://www.mscenter.be/,Nationaal Multiple Sclerose Centrum vzw,{DAY},foi_contact,tick2377; FOI info@mscenter.be; zetel Vanheylenstraat 16 1820 Steenokkerzeel (Melsbroek); leftover city_steenokkerzeel@1298; NOT Kloosterstraat 6; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Nationaal Multiple Sclerose Centrum VZW (NMSC / Melsbroek / specialized MS rehab hospital),NMSC ASBL (Melsbroek / hopital de reeducation SEP),NMSC VZW (Melsbroek / specialized MS rehab hospital),parastatal,city_steenokkerzeel,nl,https://www.mscenter.be/,info@mscenter.be,"Vanheylenstraat 16, 1820 Steenokkerzeel (Melsbroek)",tick2377 YE2025 Strong official scanned NBB PDF deposit 2026-00194601 + Strong KBO 0410.338.110 Actief 1 VE Aanbestedende RSZ2025 86.103; omzet JUMP 28752817 hospital envelope 700 14134580 + RIZIV 703 9270482; opbr JUMP 31849978; pnl JUMP 980209; equity JUMP 15285799; assets JUMP 23154847; debt JUMP 7814733; FTE 208.77; kapitaalsubsidies DROP 470657; destin691 JUMP 622247; cash JUMP 9807729; leftover city_steenokkerzeel@1298; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_nmsc_omzet_jr2025_statutory,{EID},2025,28752817,28752817,28752817,NBB hospital S-vzw code 70 omzet YE2025 JUMP +2.18% (primary L5 envelope; BFM+RIZIV hospital not commercial-only),{SRC_PDF},strong,tick2377; PDF p6 OCR; YE2024 28138764; 700 verpleegdagprijs 14134580; 703 RIZIV 9270482; 702 1046640; 705 3126506; 708/709 1112669; 701 residue 61940",
    f"bud_nmsc_opbr_jr2025_statutory,{EID},2025,31849978,31849978,31849978,NBB hospital S-vzw code 70/74 bedrijfsopbrengsten YE2025 JUMP +2.95%,{SRC_PDF},strong,tick2377; PDF p6 OCR; YE2024 30938031; 74 3086100; 741 empty; 72 11061",
    f"bud_nmsc_riziv703_jr2025_statutory,{EID},2025,9270482,9270482,9270482,NBB hospital S-vzw code 703 forfaits conventies RIZIV YE2025 (rehab/TMST/chronic conventions inside omzet 70),{SRC_PDF},strong,tick2377; PDF p6 OCR; 700 verpleegdagprijs 14134580; 702 kamersupplementen 1046640",
    f"bud_nmsc_pnl_jr2025_statutory,{EID},2025,980209,980209,980209,NBB hospital S-vzw code 70/66 winst van het boekjaar YE2025 JUMP +26.66%,{SRC_PDF},strong,tick2377; PDF p7-8 OCR; YE2024 773910; bedrijfswinst 70/64 798236 vs YE2024 loss -64766; destin691/2 622247",
    f"bud_nmsc_equity_jr2025_statutory,{EID},2025,15285799,15285799,15285799,NBB hospital S-vzw code 10/15 eigen vermogen YE2025 JUMP +9.42%,{SRC_PDF},strong,tick2377; PDF p5 OCR; YE2024 13969655; kapitaalsubsidies 470657; reserves 13 7471283",
    f"bud_nmsc_assets_jr2025_statutory,{EID},2025,23154847,23154847,23154847,NBB hospital S-vzw code 20/58 totaal activa YE2025 JUMP +6.12%,{SRC_PDF},strong,tick2377; PDF p4 OCR; YE2024 21820474",
    f"bud_nmsc_debt_jr2025_statutory,{EID},2025,7814733,7814733,7814733,NBB hospital S-vzw code 17/49 schulden incl accruals YE2025 JUMP +0.44%,{SRC_PDF},strong,tick2377; PDF p5 OCR; YE2024 7780756; LT 574427; ST 7240306; inhaal 443 1891694",
    f"bud_nmsc_cash_jr2025_statutory,{EID},2025,9807729,9807729,9807729,NBB hospital S-vzw code 54/58 liquide middelen YE2025 JUMP +2.15%,{SRC_PDF},strong,tick2377; PDF p4 OCR; YE2024 9600934; geldbeleggingen 51/53 2775522",
    f"bud_nmsc_kapitaalsubsidies_jr2025_statutory,{EID},2025,470657,470657,470657,NBB hospital S-vzw code 15 investeringssubsidies YE2025 DROP -19.63%,{SRC_PDF},strong,tick2377; PDF p5 OCR; YE2024 585616",
    f"bud_nmsc_fte_jr2025_statutory,{EID},2025,208.77,208.77,208.77,NBB hospital S-vzw gemiddeld personeelseffectief VTE YE2025 208.77,{SRC_PDF},strong,tick2377; PDF p11 OCR; personnel 62 17974709; bezoldigingen 13276047; RSZ 4109997; andere 603956",
])

cash_json = (
    '"{""2025_omzet"":28752817,""2025_opbr"":31849978,""2025_700"":14134580,""2025_703"":9270482,'
    '""2025_702"":1046640,""2025_705"":3126506,""2025_708"":1112669,""2025_701"":61940,'
    '""2025_74"":3086100,""2025_741"":0,""2025_if74"":435010,""2025_pnl"":980209,'
    '""2025_bedrijfswinst"":798236,""2025_equity"":15285799,""2025_assets"":23154847,""2025_debt"":7814733,'
    '""2025_fte"":208.77,""2025_kapitaalsubsidies"":470657,""2025_destin691"":622247,'
    '""2025_cash"":9807729,""2025_geldbeleggingen"":2775522,""2025_personnel62"":17974709,'
    '""2025_gebouwen22"":2856606,""2025_aanbouw27"":2750465,""2025_capex27"":1989270,'
    '""2025_inhaal443"":1891694,""2024_omzet"":28138764,""2024_opbr"":30938031,'
    '""2024_pnl"":773910,""2024_bedrijfswinst"":-64766,""2024_equity"":13969655,'
    '""2024_assets"":21820474,""2024_debt"":7780756,""2024_kapitaalsubsidies"":585616,'
    '""2024_destin691"":458487,""2024_cash"":9600934}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},NMSC vzw YE2025 (omzet 28.75m / pnl JUMP 0.98m / 622k destin / 471k kapitaalsubsidies / Strong PDF),{EID},FOD Volksgezondheid BFM + RIZIV MS rehab + leftover city_steenokkerzeel,VZW Nationaal Multiple Sclerose Centrum (KBO 0410.338.110; Actief; 1 VE; Aanbestedende; RSZ2025 86.103),2026-06-22,2025,2025,28752817,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00194601.pdf,Public specialized MS rehab hospital dual of mined city_steenokkerzeel,Publish BFM/RIZIV/inhaal matrix inside omzet 28.75m + 622k destin vs 471k kapitaalsubsidies DROP,{SRC_PDF},strong,Vlaanderen>Vlaams_Brabant>Steenokkerzeel>NMSC>JR2025_statutory_L5,tick2377; Strong official scanned PDF OCR; leftover city_steenokkerzeel@1298; NOT Kloosterstraat 6; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},NMSC omzet 28.75m / pnl JUMP 0.98m / 622k destin / 471k kapitaalsubsidies (YE2025 MS rehab Melsbroek),L5,ms_rehab_hospital_vzw_statutory,Vlaanderen>Vlaams_Brabant>Steenokkerzeel>NMSC>JR2025,28752817,28752817,PDF omzet JUMP 28752817 hospital envelope; 700 14134580; 703 RIZIV 9270482; 702 1046640; 705 3126506; 708/709 1112669; 701 61940; opbr JUMP 31849978; 74 3086100 741 empty IF 435010; bedrijfswinst JUMP 798236 from loss; pnl JUMP 980209; equity JUMP 15285799; assets JUMP 23154847; debt JUMP 7814733; FTE 208.77; kapitaalsubsidies DROP 470657; destin691 JUMP 622247; cash JUMP 9807729; geldbeleggingen 2775522; gebouwen 2856606; aanbouw JUMP 2750465 capex 1989270; personnel 17974709; inhaal443 1891694 uncertain,strong,{SRC_PDF},MS / neurological rehab patients Melsbroek,FOD Volksgezondheid BFM + RIZIV + leftover city_steenokkerzeel,28.75m hospital omzet; 1.89m inhaal 443 uncertain; 622k destin; 471k kapitaalsubsidies DROP; 741 empty vs 74 3.09m; leftover city_steenokkerzeel,6.2,6.6,5.4,6.20,FOI BFM/RIZIV/inhaal matrix + 622k destin + 471k kapitaalsubsidies DROP + VIPA nieuwbouw,active,,tick2377; Strong official NBB scanned PDF OCR + Strong KBO; leftover city_steenokkerzeel@1298; OFF Drongen OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams_Brabant>Steenokkerzeel>NMSC>BFM_RIZIV_inhaal,vzw_nmsc,BFM/RIZIV/inhaal split inside omzet 28752817 + 700 14134580 / 703 9270482 / 701 61940; why 741 empty vs 74 3086100 IF 435010; nature of kapitaalsubsidies 470657 DROP and destin 691/2 622247; inhaal 443 1891694 uncertain,Strong official PDF leftover public MS rehab hospital of city_steenokkerzeel@1298; 28.75m omzet; public not private clinic,8,Nationaal Multiple Sclerose Centrum VZW / Prof. dr. Dirk De Ridder voorzitter RvB,info@mscenter.be,"Vanheylenstraat 16, 1820 Steenokkerzeel (Melsbroek)",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2377; ready NOT sent; Strong official scanned NBB PDF OCR; after MKL@2376; leftover city_steenokkerzeel hospital off Drongen off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2377,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2377 line, found {n}")
if "rq_2378," in rq_text:
    raise SystemExit("rq_2378 already exists")

new_2377 = (
    "rq_2377,leftover dual — NMSC YE2025 Strong (omzet JUMP 28.75m / pnl JUMP 0.98m / 622k destin),"
    "hole_fill,8,done,L5,vzw_nmsc,"
    "Tick 2377 leftover after MKL. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL). "
    "Took NMSC 0410.338.110 deposit 2026-00194601 leftover city_steenokkerzeel@1298. "
    "Do NOT redo MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:50:07Z,{STAMP},"
    "tick2377 NMSC 0410.338.110 YE2025 Strong official scanned PDF 2026-00194601; omzet JUMP 28752817 hospital envelope 700 14134580 + RIZIV 703 9270482; opbr JUMP 31849978; pnl JUMP 980209; equity JUMP 15285799; assets JUMP 23154847; debt JUMP 7814733; FTE 208.77; kapitaalsubsidies DROP 470657; destin691 JUMP 622247; cash JUMP 9807729; FOI ready NOT sent; leftover city_steenokkerzeel@1298; OFF Drongen OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2377,"):
        parts.append(new_2377)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2377 replace count {replaced}")
new_rq = "".join(parts)
new_2378 = (
    "rq_2378,leftover dual after NMSC — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After NMSC YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110). "
    "Do NOT redo NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2377; NMSC taken leftover city_steenokkerzeel; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2378
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2377 + rq_2378; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2377,2377,no,"
    "tick2377 leftover dual NMSC 0410.338.110 Strong scanned PDF (omzet JUMP 28752817 hospital envelope 700 14134580 + RIZIV 703 9270482; opbr JUMP 31849978; pnl JUMP 980209; equity JUMP 15285799; assets JUMP 23154847; debt JUMP 7814733; FTE 208.77; kapitaalsubsidies DROP 470657; destin691 JUMP 622247; cash JUMP 9807729; 1 VE Aanbestedende RSZ2025 86.103); leftover city_steenokkerzeel@1298; OFF Drongen OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2378; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2377 - rq_2377 NMSC Melsbroek (omzet JUMP 28.75m / pnl JUMP 0.98m / 622k destin / Strong PDF)

- Unit: **rq_2377** leftover dual after **MKL@2376**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Nationaal Multiple Sclerose Centrum VZW (NMSC)** YE2025 (KBO **0410.338.110**; zetel Vanheylenstraat 16, 1820 Steenokkerzeel / Melsbroek; **Actief** **1 VE** **2.150.746.059**; **Aanbestedende overheid**; RSZ2025 **86.103**; leftover of mined **city_steenokkerzeel@1298** / leftover after **agb_steenokkerzeel@1167**; info@mscenter.be). Confirmed leftover public (RIZIV/FOD specialized MS rehab hospital + VAND/TMST conventies) not private clinic. Do not redo MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB hospital-schema S-vzw scanned PDF deposit **2026-00194601** (17161407 B / 43p; AV **17.06.2026**; header **22.06.2026**; CDN Last-Modified **09.07.2026**) — omzet 70 **EUR28752817** JUMP +2.18% (hospital envelope; not commercial-only); 700 verpleegdagprijs **14134580** + 703 RIZIV **9270482** + 702 **1046640** + 705 **3126506** + 708/709 **1112669** + 701 residue **61940**; bedrijfsopbrengsten 70/74 **EUR31849978** JUMP +2.95%; 74 **3086100** (741 empty; instandhoudingsforfait **435010**); bedrijfswinst **EUR798236** JUMP from loss -64766; pnl 70/66 **EUR980209** JUMP +26.66%; equity **EUR15285799** JUMP +9.42%; assets **EUR23154847** JUMP +6.12%; debt **EUR7814733** JUMP +0.44%; FTE **208.77**; kapitaalsubsidies **EUR470657** DROP -19.63%; destin 691/2 **EUR622247** JUMP +35.72%; cash **EUR9807729** JUMP +2.15%; geldbeleggingen **EUR2775522**; gebouwen **EUR2856606**; aanbouw **EUR2750465** JUMP +261% (capex **1989270**); personeel 62 **EUR17974709**; inhaal 443 **1891694** uncertain. Strong KBO + Strong PDF (OCR of official scan; not SBM table; smaller than Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 vzw_nmsc); foi + draft `{GAP}`; rq_2377=done + rq_2378 open; loop_state ticks=2377; raw tick2377/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2378 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Zeepreventorium still YE2024.

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
