#!/usr/bin/env python3
"""Surgical tick 2382 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_car_dat"
SRC_PDF = "src_car_dat_jr2025_nbb_pdf_2382"
SRC_KBO = "src_car_dat_kbo_2382"
SRC_SBM = "src_car_dat_sbm_2382"
SRC_SITE = "src_car_dat_site_2382"
COMM = "comm_car_dat_jr2025_statutory_omzet_2_01m_pnl_drop_destin_50k"
LB = "lb_car_dat_omzet_2_01m_pnl_drop_destin_50k_jr2025"
GAP = "gap_car_dat_riziv_vl_matrix_omzet_2_01m_73_348k_pnl_drop_destin_50k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR DAT Tienen/Aarschot deposit 2026-00106951,http://cdn.staatsbladmonitor.be/2026pdf/2026-00106951.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2382; official native PDF 51204 bytes 14p VKT-VZW 26.0.10 m04-f; header 09.05.2026; AV 24.04.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-04; CreationDate 2026-05-09 19:59:50 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Belscope",
    f"{SRC_KBO},KBO Centrum voor Ambulante Revalidatie D.A.T. vzw 0463.347.917,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463347917,KBO Public Search FOD Economie,{DAY},official_register,tick2382; Actief; 2 VE 2.143.479.076 Langdorpsesteenweg 129 3200 Aarschot since 20.12.1997 + 2.144.697.615 Houtemstraat 115B 3300 Tienen since 19.01.2005; zetel Houtemstraat 115B 3300 Tienen since 19.06.1998; RSZ2025 86.959; gedelegeerd bestuurder Luc Holemans; ondervoorzitter Mia Honinckx",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR DAT 0463347917 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0463347917,Staatsbladmonitor,{DAY},official_register,tick2382; deposit-id 2026-00106951 and CDN Last-Modified 2026-06-04; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR DAT FOI contact / RIZIV CAR Tienen Aarschot,https://www.cardat.be/,Centrum voor Ambulante Revalidatie D.A.T. vzw,{DAY},foi_contact,tick2382; FOI info@cardat.be; zetel Houtemstraat 115B 3300 Tienen; campus Aarschot Langdorpsesteenweg 129; leftover city_tienen + city_aarschot + city_diest; NOT Kloosterstraat 6; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},CAR DAT VZW (Tienen + Aarschot / ambulante revalidatie D.A.T. Diest-Aarschot-Tienen),CAR DAT ASBL (Tirlemont + Aarschot / revalidation ambulatoire),CAR DAT VZW (Tienen + Aarschot / outpatient rehabilitation),parastatal,city_tienen,nl,https://www.cardat.be/,info@cardat.be,"Houtemstraat 115B, 3300 Tienen",tick2382 YE2025 Strong official native NBB PDF deposit 2026-00106951 + Strong KBO 0463.347.917 Actief 2 VE RSZ2025 86.959; omzet JUMP 2012057 CAR envelope; bruto JUMP 2074211; 73 JUMP 348197; pnl DROP 54847; equity JUMP 1315664; assets JUMP 1725875; debt JUMP 410211; FTE 24.5; kapitaalsubsidies DROP 169865; destin691 DROP 50000; cash JUMP 867261; leftover city_tienen after H.Hart@2381; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_car_dat_omzet_jr2025_statutory,{EID},2025,2012057,2012057,2012057,NBB VKT-VZW code 70 omzet YE2025 JUMP +3.03% (primary L5 envelope; CAR RIZIV/Departement Zorg not commercial-only),{SRC_PDF},strong,tick2382; PDF p5 native; YE2024 1952978; 73 348197; bruto 2074211 ~1.03x",
    f"bud_car_dat_bruto_jr2025_statutory,{EID},2025,2074211,2074211,2074211,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.82%,{SRC_PDF},strong,tick2382; PDF p5 native; YE2024 2017402; 76A empty",
    f"bud_car_dat_subs73_jr2025_statutory,{EID},2025,348197,348197,348197,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +8.86%,{SRC_PDF},strong,tick2382; PDF p5 native; YE2024 319849",
    f"bud_car_dat_pnl_jr2025_statutory,{EID},2025,54847,54847,54847,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -27.71%,{SRC_PDF},strong,tick2382; PDF p5 native; YE2024 75867; bedrijfswinst 9901 40625 DROP vs YE2024 52881; destin691 50000 DROP",
    f"bud_car_dat_equity_jr2025_statutory,{EID},2025,1315664,1315664,1315664,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.68%,{SRC_PDF},strong,tick2382; PDF p4 native; YE2024 1281349; kapitaalsubsidies 169865; overgedragen 14 178146; fondsen 10 51653; bestemde 13 916000",
    f"bud_car_dat_assets_jr2025_statutory,{EID},2025,1725875,1725875,1725875,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +8.13%,{SRC_PDF},strong,tick2382; PDF p3 native; YE2024 1596071",
    f"bud_car_dat_debt_jr2025_statutory,{EID},2025,410211,410211,410211,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +30.34%,{SRC_PDF},strong,tick2382; PDF p4 native; YE2024 314722; LT empty; ST 410211; handel 105903; sociaal 254522",
    f"bud_car_dat_cash_jr2025_statutory,{EID},2025,867261,867261,867261,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +33.74%,{SRC_PDF},strong,tick2382; PDF p3 native; YE2024 648453; geldbeleggingen 50/53 400000 DROP vs 600000",
    f"bud_car_dat_kapitaalsubsidies_jr2025_statutory,{EID},2025,169865,169865,169865,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -10.78%,{SRC_PDF},strong,tick2382; PDF p4 native; YE2024 190397",
    f"bud_car_dat_fte_jr2025_statutory,{EID},2025,24.5,24.5,24.5,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 24.5 JUMP +0.82%,{SRC_PDF},strong,tick2382; PDF p11 native; YE2024 24.3; koppen 105 32 vs; personnel 62 1989575; uitzend empty",
])

cash_json = (
    '"{""2025_omzet"":2012057,""2025_bruto"":2074211,""2025_73"":348197,'
    '""2025_pnl"":54847,""2025_bedrijfswinst"":40625,""2025_equity"":1315664,'
    '""2025_assets"":1725875,""2025_debt"":410211,""2025_fte"":24.5,'
    '""2025_kapitaalsubsidies"":169865,""2025_destin691"":50000,""2025_cash"":867261,'
    '""2025_geldbeleggingen"":400000,""2025_personnel62"":1989575,'
    '""2025_gebouwen22"":243164,""2025_aanbouw27"":87001,'
    '""2025_capex8169"":95862,""2025_fondsen10"":51653,'
    '""2025_bestemde13"":916000,""2025_overgedragen14"":178146,'
    '""2024_omzet"":1952978,""2024_bruto"":2017402,'
    '""2024_73"":319849,""2024_pnl"":75867,""2024_bedrijfswinst"":52881,'
    '""2024_equity"":1281349,""2024_assets"":1596071,""2024_debt"":314722,'
    '""2024_kapitaalsubsidies"":190397,""2024_cash"":648453,""2024_fte"":24.3,'
    '""2024_destin691"":75000,""2024_geldbeleggingen"":600000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR DAT vzw Tienen/Aarschot YE2025 (omzet 2.01m / 73 348k / pnl DROP 55k / destin 50k / Strong PDF),{EID},RIZIV + Departement Zorg + leftover city_tienen,VZW CAR DAT (KBO 0463.347.917; Actief; 2 VE; RSZ2025 86.959),2026-05-09,2025,2025,2012057,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00106951.pdf,Public CAR dual of mined city_tienen,Publish RIZIV/VL matrix inside omzet 2.01m + explain 73 348k JUMP + pnl DROP 55k + destin 50k DROP + kapitaalsubsidies 170k DROP + cash JUMP 867k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Tienen>CAR_DAT>JR2025_statutory_L5,tick2382; Strong official native PDF; leftover city_tienen after H.Hart@2381; NOT Kloosterstraat 6; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR DAT Tienen/Aarschot omzet 2.01m / 73 348k / pnl DROP 55k / destin 50k (YE2025 Tienen),L5,car_vzw_statutory,Vlaanderen>Vlaams-Brabant>Tienen>CAR_DAT>JR2025,2012057,2012057,PDF omzet JUMP 2012057 CAR envelope; bruto JUMP 2074211 ~1.03x; 73 JUMP 348197; bedrijfswinst DROP 40625; pnl DROP 54847; equity JUMP 1315664; assets JUMP 1725875; debt JUMP 410211; FTE 24.5 JUMP; kapitaalsubsidies DROP 169865; destin691 DROP 50000; cash JUMP 867261; geldbeleggingen DROP 400000; gebouwen 243164; aanbouw 87001; capex 95862; personnel 1989575,strong,{SRC_PDF},children with developmental disorders Tienen + Aarschot,RIZIV + Departement Zorg + leftover city_tienen,2.01m CAR omzet; 348k 73 subsidies JUMP; pnl DROP 55k; destin 50k DROP; 170k kapitaalsubsidies DROP; cash JUMP 867k; leftover city_tienen,5.4,5.0,5.2,5.18,FOI RIZIV/VL matrix + 73 348k JUMP + pnl DROP 55k + destin 50k DROP + 170k kapitaalsubsidies DROP + cash JUMP,active,,tick2382; Strong official NBB native PDF + Strong KBO; leftover city_tienen after H.Hart@2381; OFF Drongen OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams-Brabant>Tienen>CAR_DAT>RIZIV_VL_CAR,{EID},RIZIV/Departement Zorg split inside omzet 2012057; why 73 348197 JUMP; why pnl 54847 DROP; nature of destin 691 50000 DROP and bestemde fondsen 916000 (sociaal passief 300000 + nieuwbouw Tienen 616000); kapitaalsubsidies 169865 DROP; cash JUMP 867261 vs beleggingen DROP 400000; aanbouw 87001; debt JUMP 410211,Strong official PDF leftover public CAR of city_tienen; 2.01m omzet; public not private clinic,8,Centrum voor Ambulante Revalidatie D.A.T. VZW / Luc Holemans gedelegeerd bestuurder,info@cardat.be,"Houtemstraat 115B, 3300 Tienen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2382; ready NOT sent; Strong official native NBB PDF; leftover city_tienen CAR after H.Hart@2381; off Drongen off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2382,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2382 line, found {n}")
if "rq_2383," in rq_text:
    raise SystemExit("rq_2383 already exists")

new_2382 = (
    "rq_2382,leftover dual — CAR DAT Tienen/Aarschot YE2025 Strong (omzet JUMP 2.01m / 73 348k / pnl DROP 55k / destin 50k),"
    "hole_fill,8,done,L5,vzw_car_dat,"
    "Tick 2382 leftover after H.Hart Oudenaarde. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde). "
    "Took CAR DAT Tienen/Aarschot 0463.347.917 deposit 2026-00106951 leftover city_tienen. "
    "Do NOT redo H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:32:59Z,{STAMP},"
    "tick2382 CAR DAT 0463.347.917 YE2025 Strong official native PDF 2026-00106951; omzet JUMP 2012057 CAR envelope; bruto JUMP 2074211; 73 JUMP 348197; pnl DROP 54847; equity JUMP 1315664; assets JUMP 1725875; debt JUMP 410211; FTE 24.5; kapitaalsubsidies DROP 169865; destin691 DROP 50000; cash JUMP 867261; FOI ready NOT sent; leftover city_tienen after H.Hart@2381; OFF Drongen OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2382,"):
        parts.append(new_2382)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2382 replace count {replaced}")
new_rq = "".join(parts)
new_2383 = (
    "rq_2383,leftover dual after CAR DAT — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR DAT Tienen/Aarschot YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917). "
    "Do NOT redo CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2382; CAR DAT taken leftover city_tienen after H.Hart Oudenaarde; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2383
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2382 + rq_2383; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2382,2382,no,"
    "tick2382 leftover dual CAR DAT Tienen/Aarschot 0463.347.917 Strong native PDF (omzet JUMP 2012057 CAR envelope; bruto JUMP 2074211; 73 JUMP 348197; pnl DROP 54847; equity JUMP 1315664; assets JUMP 1725875; debt JUMP 410211; FTE 24.5; kapitaalsubsidies DROP 169865; destin691 DROP 50000; cash JUMP 867261; 2 VE RSZ2025 86.959); leftover city_tienen after H.Hart@2381; OFF Drongen OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2383; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2382 - rq_2382 CAR DAT Tienen/Aarschot (omzet JUMP 2.01m / 73 348k / pnl DROP 55k / destin 50k / Strong PDF)

- Unit: **rq_2382** leftover dual after **H.Hart Oudenaarde@2381**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Zeepreventorium still **YE2024**. Zwarte Zusters 0413.272.260 **stopgezet 26.06.2000** (private convent / empty; skip). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **CAR DAT VZW (Centrum voor Ambulante Revalidatie D.A.T.)** YE2025 (KBO **0463.347.917**; zetel Houtemstraat 115B, 3300 Tienen; **Actief** **2 VE** **2.143.479.076** Aarschot + **2.144.697.615** Tienen; RSZ2025 **86.959**; leftover of mined **city_tienen** + leftover of mined **city_aarschot** + leftover of mined **city_diest**; info@cardat.be). Confirmed leftover public (Departement Zorg CAR + RIZIV ambulante revalidatie children) not private clinic / not H.Hart 0407.644.082 / not Sint-Vincentius Zulte / not Floordam / not NMSC. Do not redo H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VKT-VZW native PDF deposit **2026-00106951** (51204 B / 14p; AV **24.04.2026**; header **09.05.2026**; CDN Last-Modified **04.06.2026**) — omzet 70 **EUR2012057** JUMP +3.03% (CAR envelope; not commercial-only); bruto 9900 **EUR2074211** JUMP +2.82% (~**1.03x**); 73 **EUR348197** JUMP +8.86%; bedrijfswinst 9901 **EUR40625** DROP −23.18%; pnl 9904 **EUR54847** DROP −27.71%; equity **EUR1315664** JUMP +2.68%; assets **EUR1725875** JUMP +8.13%; debt **EUR410211** JUMP +30.34%; FTE **24.5** JUMP +0.82%; kapitaalsubsidies **EUR169865** DROP −10.78%; destin 691 **EUR50000** DROP −33.33%; cash **EUR867261** JUMP +33.74%; geldbeleggingen **EUR400000** DROP; gebouwen **EUR243164**; aanbouw **EUR87001**; capex **EUR95862**; personeel 62 **EUR1989575**. Strong KBO + Strong PDF (native text; not SBM table; smaller than H.Hart 1.8MB / Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.18); entities (+1 vzw_car_dat); foi + draft `{GAP}`; rq_2382=done + rq_2383 open; loop_state ticks=2382; raw tick2382/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2390**). Next: rq_2383 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT CAR DAT / NOT H.Hart Oudenaarde / NOT Sint-Vincentius Zulte / NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Candidate leftover WZC Vijvens Kruisem 0415.093.385 (Companyweb YE2025 filed 24.06.2026; need live 2026pdf deposit-id). De Bolster 0861.680.989 still YE2024 public file. School Perk 0417.085.845 only if leftover school of mined parent is in priority. Zeepreventorium still YE2024.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
