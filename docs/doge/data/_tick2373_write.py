#!/usr/bin/env python3
"""Surgical tick 2373 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_sint_lievenspoort"
SRC_PDF = "src_sint_lievenspoort_jr2025_nbb_pdf_2373"
SRC_KBO = "src_sint_lievenspoort_kbo_2373"
SRC_SBM = "src_sint_lievenspoort_sbm_2373"
SRC_SITE = "src_sint_lievenspoort_site_2373"
COMM = "comm_sint_lievenspoort_jr2025_statutory_opbr_20_98m_73_18_53m"
LB = "lb_sint_lievenspoort_opbr_20_98m_73_18_53m_cash_jump_jr2025"
GAP = "gap_slp_riziv_vaph_onderwijs_matrix_73_18_53m_opbr_20_98m_13_77m_kapitaalsubsidies_cash_6_31m_l5"
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
    f"{SRC_PDF},NBB WVV VOL-VZW jaarrekening 2025 Sint-Lievenspoort vzw deposit 2026-00214840,http://cdn.staatsbladmonitor.be/2026pdf/2026-00214840.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2373; official PDF 969601 bytes 47p VOL-VZW 23.0.10 m05-f; header 25.06.2026; AV 16.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-12; CreationDate 2026-06-29 22:09:01 UTC OpenPDF 1.3.26; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO Sint-Lievenspoort vzw 0410.570.712,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410570712,KBO Public Search FOD Economie,{DAY},official_register,tick2373; Actief; 5 VE; zetel Sint-Lievenspoortstraat 129 9000 Gent since 19.08.1999; Aanbestedende overheid since 11.01.1968; Kinderopvang VG since 06.10.2016; RSZ2025 88.103; voorzitter Craeghs Cyriel since 01.01.2026; dagelijks bestuur Vandenbussche Vincent since 01.01.2026",
    f"{SRC_SBM},Staatsbladmonitor fiche Sint-Lievenspoort vzw 0410570712 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410570712,Staatsbladmonitor,{DAY},official_register,tick2373; deposit-id 2026-00214840 and CDN Last-Modified 2026-07-12; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Sint-Lievenspoort vzw FOI contact / CAR + MFC + BuO + KDV,https://www.sintlievenspoort.be/,Sint-Lievenspoort vzw,{DAY},foi_contact,tick2373; FOI boekhouding@sintlievenspoort.be / car@sintlievenspoort.be; zetel Sint-Lievenspoortstraat 129 9000 Gent; leftover city_gent@101 + leftover Impuls@2371 / Mozaiek@2369 Gent CARs; NOT Kloosterstraat 6",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},Sint-Lievenspoort VZW (Gent / CAR + MFC + BuO + KDV),Sint-Lievenspoort ASBL (Gand / CAR + MFC + enseignement + accueil),Sint-Lievenspoort VZW (Ghent / outpatient rehab + MFC + special school + daycare),parastatal,sec_flanders,nl,https://www.sintlievenspoort.be/,boekhouding@sintlievenspoort.be,"Sint-Lievenspoortstraat 129, 9000 Gent",tick2373 YE2025 Strong official NBB PDF deposit 2026-00214840 + Strong KBO 0410.570.712 Actief 5 VE Aanbestedende RSZ2025 88.103; omzet JUMP 2360907 commercial-only vs 73 JUMP 18533057; opbr 70/76A JUMP 20982828 VOL envelope; pnl JUMP 664264; equity DROP 28703626; assets DROP 44033613; debt DROP 15314717; FTE DROP 222; kapitaalsubsidies DROP 13770768; destin691 empty; cash JUMP 6314727; leftover city_gent@101 + Impuls@2371 / Mozaiek@2369; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = bedrijfsopbrengsten 70/76A (omzet commercial-only vs large 73)
append_lines(DATA / "budgets.csv", [
    f"bud_slp_opbr_jr2025_statutory,{EID},2025,20982828,20982828,20982828,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.26% (primary L5 envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2373; PDF p7; YE2024 20519985; omzet 2360907 vs 73 18533057",
    f"bud_slp_omzet_jr2025_statutory,{EID},2025,2360907,2360907,2360907,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.62% (commercial-only hoorapparaten + ouderbijdragen vs large 73),{SRC_PDF},strong,tick2373; PDF p7; YE2024 2235361",
    f"bud_slp_code73_jr2025_statutory,{EID},2025,18533057,18533057,18533057,NBB VOL-VZW code 73 lidgeld/schenkingen/subsidies YE2025 JUMP +2.06%,{SRC_PDF},strong,tick2373; PDF p7; YE2024 18158416; 733 subsidies 17759656; 730 lidgelden 754787; 731 schenkingen 18614",
    f"bud_slp_pnl_jr2025_statutory,{EID},2025,664264,664264,664264,NBB VOL-VZW code 9905 te bestemmen winst YE2025 JUMP +61.46%,{SRC_PDF},strong,tick2373; PDF p8; YE2024 411418; bedrijfswinst 9901 1067266 JUMP +21.23%",
    f"bud_slp_equity_jr2025_statutory,{EID},2025,28703626,28703626,28703626,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -0.03%,{SRC_PDF},strong,tick2373; PDF p6; YE2024 28711874; kapitaalsubsidies 13770768; bestemde fondsen 4346356 FLAT",
    f"bud_slp_assets_jr2025_statutory,{EID},2025,44033613,44033613,44033613,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.47%,{SRC_PDF},strong,tick2373; PDF p5; YE2024 44689390",
    f"bud_slp_debt_jr2025_statutory,{EID},2025,15314717,15314717,15314717,NBB VOL-VZW code 17/49 schulden YE2025 DROP -4.06%,{SRC_PDF},strong,tick2373; PDF p6; YE2024 15962246; leasing 172 9795724",
    f"bud_slp_cash_jr2025_statutory,{EID},2025,6314727,6314727,6314727,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +54.18%,{SRC_PDF},strong,tick2373; PDF p5; YE2024 4095597; VIPA receivable collected",
    f"bud_slp_kapitaalsubsidies_jr2025_statutory,{EID},2025,13770768,13770768,13770768,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -4.66%,{SRC_PDF},strong,tick2373; PDF p6; YE2024 14443280",
    f"bud_slp_fte_jr2025_statutory,{EID},2025,222,222,222,NBB VOL-VZW code 9087 FTE YE2025 DROP -0.89%,{SRC_PDF},strong,tick2373; PDF p23; YE2024 224; destin691 empty (YE2024 220000); capex 8161+8162+8163 281761",
])

# commitments (+1)
cash_json = (
    '"{""2025_opbr"":20982828,""2025_omzet"":2360907,""2025_code73"":18533057,""2025_733"":17759656,'
    '""2025_pnl"":664264,""2025_equity"":28703626,""2025_assets"":44033613,""2025_debt"":15314717,'
    '""2025_fte"":222,""2025_kapitaalsubsidies"":13770768,""2025_destin691"":0,""2025_destin13"":4346356,'
    '""2025_cash"":6314727,""2025_personnel62"":15439657,""2025_capex816x"":281761,'
    '""2025_gebouwen22"":18705769,""2025_leasing25"":8321951,""2025_lease_debt172"":9795724,'
    '""2024_opbr"":20519985,""2024_omzet"":2235361,""2024_code73"":18158416,""2024_pnl"":411418,'
    '""2024_equity"":28711874,""2024_assets"":44689390,""2024_debt"":15962246,""2024_fte"":224,'
    '""2024_kapitaalsubsidies"":14443280,""2024_destin691"":220000,""2024_destin13"":4346356,'
    '""2024_cash"":4095597}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Sint-Lievenspoort vzw YE2025 (opbr 20.98m / 73 18.53m / 13.77m kapitaalsubsidies / cash JUMP 6.31m / Strong PDF),{EID},Departement Zorg CAR + VAPH MFC + Onderwijs BuO + Opgroeien KDV / leftover city_gent,VZW Sint-Lievenspoort (KBO 0410.570.712; Actief; 5 VE; Aanbestedende; RSZ2025 88.103),2026-06-25,2025,2025,20982828,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00214840.pdf,Public CAR + VAPH MFC + BuO + KDV dual of mined city_gent,Publish RIZIV/VAPH/onderwijs/Opgroeien matrix inside 73 18.53m + 13.77m kapitaalsubsidies vs cash JUMP 6.31m,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Gent>Sint_Lievenspoort>JR2025_statutory_L5,tick2373; Strong official PDF; leftover city_gent@101 + Impuls@2371 / Mozaiek@2369; NOT Kloosterstraat 6; not TE-additive",
])

# leaderboard (+1) pi = 0.4*6.4 + 0.4*6.8 + 0.2*5.0 = 6.28
append_lines(DATA / "leaderboard.csv", [
    f"{LB},Sint-Lievenspoort opbr 20.98m / 73 18.53m / cash JUMP 6.31m (YE2025 CAR+MFC+BuO+KDV Gent),L5,car_mfc_buo_kdv_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Gent>Sint_Lievenspoort>JR2025,20982828,20982828,PDF opbr JUMP 20982828; omzet 2360907 commercial-only vs 73 JUMP 18533057 (733 17759656); pnl JUMP 664264; equity DROP 28703626; assets DROP 44033613; debt DROP 15314717; FTE DROP 222; kapitaalsubsidies DROP 13770768; destin691 empty; cash JUMP 6314727; gebouwen 18705769; capex 281761; DBFM lease 9795724,strong,{SRC_PDF},children + adults with communicative disability Gent (CAR + MFC + BuO + KDV),Departement Zorg CAR + VAPH MFC + onderwijs + Opgroeien,18.53m subsidies vs 2.36m commercial omzet; 13.77m kapitaalsubsidies; cash JUMP +54% to 6.31m after VIPA collection; destin empty after 220k YE2024; leftover city_gent + Impuls/Mozaiek Gent CARs,6.4,6.8,5,6.28,FOI RIZIV/VAPH/onderwijs/Opgroeien matrix + 13.77m kapitaalsubsidies + cash JUMP 6.31m + dual CAR/MFC/BuO/KDV,active,,tick2373; Strong official NBB PDF + Strong KBO; leftover city_gent@101; OFF Drongen",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Gent>Sint_Lievenspoort>RIZIV_VAPH_onderwijs,vzw_sint_lievenspoort,RIZIV/VAPH/onderwijs/Opgroeien split inside 73 18533057 + 733 17759656; nature of kapitaalsubsidies 13770768 DROP and cash JUMP 6314727; destin 691 empty after 220k YE2024; dual CAR+MFC+BuO+KDV,Strong official PDF leftover public CAR/MFC of city_gent@101 + Impuls@2371 / Mozaiek@2369; 18.53m subsidies; 13.77m capital subsidies; cash JUMP 6.31m; public not private clinic,8,Sint-Lievenspoort VZW / Cyriel Craeghs voorzitter RvB,boekhouding@sintlievenspoort.be,"Sint-Lievenspoortstraat 129, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2373; ready NOT sent; Strong official NBB PDF; after Buggenhout@2372; leftover city_gent CAR off Drongen; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2373 + append rq_2374 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2373,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2373 line, found {n}")
if "rq_2374," in rq_text:
    raise SystemExit("rq_2374 already exists")

new_2373 = (
    "rq_2373,leftover dual — Sint-Lievenspoort YE2025 Strong (opbr JUMP 20.98m / 73 18.53m / cash JUMP 6.31m),"
    "hole_fill,8,done,L5,vzw_sint_lievenspoort,"
    "Tick 2373 leftover after CAR Buggenhout. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6). "
    "Took Sint-Lievenspoort 0410.570.712 deposit 2026-00214840. "
    "Do NOT redo CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:24:11Z,{STAMP},"
    "tick2373 Sint-Lievenspoort 0410.570.712 YE2025 Strong official PDF 2026-00214840; opbr JUMP 20982828; omzet 2360907 commercial-only vs 73 JUMP 18533057; pnl JUMP 664264; equity DROP 28703626; assets DROP 44033613; debt DROP 15314717; FTE DROP 222; kapitaalsubsidies DROP 13770768; cash JUMP 6314727; FOI ready NOT sent; leftover city_gent@101 + Impuls@2371 / Mozaiek@2369; OFF Drongen\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2373,"):
        parts.append(new_2373)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2373 replace count {replaced}")
new_rq = "".join(parts)
new_2374 = (
    "rq_2374,leftover dual after Sint-Lievenspoort — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Sint-Lievenspoort YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort). "
    "Candidate: Inkendaal 0410.392.647 deposit 2026-00277815 leftover city_sint_pieters_leeuw@1066 if live 2026pdf. "
    "Do NOT redo Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2373; Sint-Lievenspoort taken leftover city_gent; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2374
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2373 + rq_2374; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2373,2373,no,"
    "tick2373 leftover dual Sint-Lievenspoort 0410.570.712 Strong PDF (opbr JUMP 20982828; omzet 2360907 commercial-only vs 73 JUMP 18533057; pnl JUMP 664264; equity DROP 28703626; assets DROP 44033613; debt DROP 15314717; FTE DROP 222; kapitaalsubsidies DROP 13770768; destin691 empty; cash JUMP 6314727; 5 VE Aanbestedende RSZ2025 88.103); leftover city_gent@101 + Impuls@2371 / Mozaiek@2369; OFF Drongen; AGB/FARO/Gandae YE2024; next rq_2374; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append (NOT every-10)
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2373 - rq_2373 Sint-Lievenspoort Gent (opbr JUMP 20.98m / 73 18.53m / cash JUMP 6.31m / Strong PDF)

- Unit: **rq_2373** leftover dual after **CAR Buggenhout@2372**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Sint-Lievenspoort VZW** YE2025 (KBO **0410.570.712**; zetel Sint-Lievenspoortstraat 129, 9000 Gent; **Actief** **5 VE**; **Aanbestedende overheid**; RSZ2025 **88.103**; leftover of mined **city_gent@101** + leftover of mined **Impuls@2371** / **Mozaiek@2369** Gent operational CARs; boekhouding@sintlievenspoort.be / car@sintlievenspoort.be). Confirmed leftover public (Departement Zorg CAR + VAPH MDT/MFC + BuO + Opgroeien KDV) not private clinic. Do not redo Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW PDF deposit **2026-00214840** (969601 B / 47p; AV **16.06.2026**; header **25.06.2026**; CDN Last-Modified **12.07.2026**) — omzet 70 **EUR2360907** JUMP +5.62% (commercial-only vs large 73); code 73 **EUR18533057** JUMP +2.06% (733 **17759656**); bedrijfsopbrengsten 70/76A **EUR20982828** JUMP +2.26% (VOL envelope); pnl **EUR664264** JUMP +61.46%; equity **EUR28703626** DROP −0.03%; assets **EUR44033613** DROP −1.47%; debt **EUR15314717** DROP −4.06%; FTE **222** DROP −0.89%; kapitaalsubsidies **EUR13770768** DROP −4.66%; destin 691 **empty** (YE2024 220000); cash **EUR6314727** JUMP +54.18%; gebouwen **EUR18705769**; capex **EUR281761**. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 6.28); entities (+1 vzw_sint_lievenspoort); foi + draft `{GAP}`; rq_2373=done + rq_2374 open; loop_state ticks=2373; raw tick2373/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2374 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (candidate Inkendaal 0410.392.647 deposit 2026-00277815 leftover city_sint_pieters_leeuw@1066).

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
