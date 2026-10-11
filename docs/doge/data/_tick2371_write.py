#!/usr/bin/env python3
"""Surgical tick 2371 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_car_impuls"
SRC_PDF = "src_impuls_jr2025_nbb_pdf_2371"
SRC_KBO = "src_impuls_kbo_2371"
SRC_SBM = "src_impuls_sbm_2371"
SRC_SITE = "src_impuls_site_2371"
COMM = "comm_impuls_jr2025_statutory_omzet_2_53m_pnl_drop_163k_kapitaalsubsidies"
LB = "lb_impuls_omzet_2_53m_pnl_drop_163k_kapitaalsubsidies_jr2025"
GAP = "gap_impuls_riziv_vl_matrix_2_53m_omzet_pnl_drop_163k_kapitaalsubsidies_car_l5"
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
    f"{SRC_PDF},NBB WVV VKT-VZW jaarrekening 2025 CAR Impuls vzw deposit 2026-00206349,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206349.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2371; official PDF 50923 bytes 13p VKT-VZW 26.0.15 m04-f; header 24.06.2026; AV 08.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-10; CreationDate 2026-06-27 01:26:42 UTC OpenPDF 1.3.26; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO CAR Impuls vzw 0416.318.951,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416318951,KBO Public Search FOD Economie,{DAY},official_register,tick2371; Actief; 1 VE 2.153.800.668 Kloosterstraat 6 9031 Gent since 31.05.2006; zetel Kloosterstraat 6 9031 Gent/Drongen; RSZ2025 86.959; voorzitter Schutyser Henk; dagelijks bestuur Van Hamme Nick",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Impuls vzw 0416318951 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0416318951,Staatsbladmonitor,{DAY},official_register,tick2371; deposit-id 2026-00206349 and CDN Last-Modified 2026-07-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Impuls vzw FOI contact / RIZIV CAR Gent,https://www.centrumimpuls.be/,CAR Impuls vzw,{DAY},foi_contact,tick2371; FOI info@centrumimpuls.be; operational Karel Lodewijk Dierickxstraat 30 9000 Gent; zetel Kloosterstraat 6 9031 Drongen; RIZIV 96541526 HCO 29577; leftover same-zetel Bolt/Mozaiek/DIGOR/Ter Kouter cluster",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},CAR Impuls VZW (Gent / ambulante revalidatie),CAR Impuls ASBL (Gand / revalidation ambulatoire),CAR Impuls VZW (Ghent / outpatient rehabilitation),parastatal,sec_flanders,nl,https://www.centrumimpuls.be/,info@centrumimpuls.be,"Karel Lodewijk Dierickxstraat 30, 9000 Gent",tick2371 YE2025 Strong official NBB PDF deposit 2026-00206349 + Strong KBO 0416.318.951 Actief 1 VE 2.153.800.668 RSZ2025 86.959 RIZIV 96541526 HCO 29577; omzet JUMP 2534712; bruto DROP 2863608 ~1.13x; pnl DROP 32748; equity JUMP 1748906; assets JUMP 2204250; debt DROP 321286; FTE JUMP 33; code73 549746; kapitaalsubsidies JUMP 162804; destin691 empty; cash DROP 1359369; leftover Bolt@2370 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = omzet 70 (present and not commercial-only vs 73)
append_lines(DATA / "budgets.csv", [
    f"bud_impuls_omzet_jr2025_statutory,{EID},2025,2534712,2534712,2534712,NBB VKT-VZW code 70 omzet YE2025 JUMP +2.38% (primary L5 envelope),{SRC_PDF},strong,tick2371; PDF p5; YE2024 2475761; omzet present and not commercial-only vs 73 549746",
    f"bud_impuls_bruto_jr2025_statutory,{EID},2025,2863608,2863608,2863608,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -0.49% (~1.13x omzet),{SRC_PDF},strong,tick2371; PDF p5; YE2024 2877854",
    f"bud_impuls_code73_jr2025_statutory,{EID},2025,549746,549746,549746,NBB VKT-VZW code 73 lidgeld/schenkingen/subsidies YE2025 JUMP +4.11%,{SRC_PDF},strong,tick2371; PDF p5; YE2024 528035",
    f"bud_impuls_pnl_jr2025_statutory,{EID},2025,32748,32748,32748,NBB VKT-VZW code 9905 te bestemmen winst YE2025 DROP -72.92%,{SRC_PDF},strong,tick2371; PDF p5; YE2024 120950; bedrijfswinst 9901 24842 DROP -75.96%",
    f"bud_impuls_equity_jr2025_statutory,{EID},2025,1748906,1748906,1748906,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.52%,{SRC_PDF},strong,tick2371; PDF p4; YE2024 1657353; kapitaalsubsidies 162804; bestemde fondsen 195094",
    f"bud_impuls_assets_jr2025_statutory,{EID},2025,2204250,2204250,2204250,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +0.98%,{SRC_PDF},strong,tick2371; PDF p3; YE2024 2182864",
    f"bud_impuls_debt_jr2025_statutory,{EID},2025,321286,321286,321286,NBB VKT-VZW code 17/49 schulden YE2025 DROP -17.92%,{SRC_PDF},strong,tick2371; PDF p4; YE2024 391453",
    f"bud_impuls_cash_jr2025_statutory,{EID},2025,1359369,1359369,1359369,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -2.46%,{SRC_PDF},strong,tick2371; PDF p3; YE2024 1393688",
    f"bud_impuls_kapitaalsubsidies_jr2025_statutory,{EID},2025,162804,162804,162804,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 JUMP +56.54%,{SRC_PDF},strong,tick2371; PDF p4; YE2024 103999; installaties 23 JUMP 146824; capex 8169 238660",
    f"bud_impuls_fte_jr2025_statutory,{EID},2025,33,33,33,NBB VKT-VZW code 9087 FTE YE2025 JUMP +3.45%,{SRC_PDF},strong,tick2371; PDF p9; YE2024 31.9",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":2534712,""2025_code73"":549746,""2025_bruto"":2863608,""2025_pnl"":32748,'
    '""2025_equity"":1748906,""2025_assets"":2204250,""2025_debt"":321286,""2025_fte"":33,'
    '""2025_kapitaalsubsidies"":162804,""2025_destin691"":0,""2025_destin13"":195094,'
    '""2025_cash"":1359369,""2025_personnel62"":2677565,""2025_capex8169"":238660,'
    '""2025_installaties23"":146824,""2025_voorzieningen16"":134058,""2024_omzet"":2475761,'
    '""2024_code73"":528035,""2024_bruto"":2877854,""2024_pnl"":120950,""2024_equity"":1657353,'
    '""2024_assets"":2182864,""2024_debt"":391453,""2024_fte"":31.9,""2024_kapitaalsubsidies"":103999,'
    '""2024_destin13"":195094,""2024_cash"":1393688}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Impuls vzw YE2025 (omzet 2.53m / pnl DROP / 163k kapitaalsubsidies JUMP / Strong PDF),{EID},RIZIV CAR Gent / dual same zetel,VZW CAR Impuls (KBO 0416.318.951; Actief; 1 VE; RSZ2025 86.959; RIZIV 96541526),2026-06-24,2025,2025,2534712,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206349.pdf,RIZIV-conventioned ambulante revalidatie children 2-19 + dual Drongen Ter Kouter cluster,Publish RIZIV/VL matrix inside omzet 2.53m + 73 0.55m; explain 163k kapitaalsubsidies JUMP +57pct and pnl DROP -73pct vs destin 691 empty,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Gent>CAR_Impuls>JR2025_statutory_L5,tick2371; Strong official PDF; leftover Bolt@2370 same Drongen zetel; not TE-additive",
])

# leaderboard (+1) pi = 0.4*5.9 + 0.4*4.8 + 0.2*5.0 = 5.28
append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Impuls omzet 2.53m / pnl DROP -73% / 163k kapitaalsubsidies JUMP +57% (YE2025 CAR Gent),L5,car_revalidatie_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Gent>CAR_Impuls>JR2025,2534712,2534712,PDF omzet JUMP 2534712; bruto DROP 2863608 (~1.13x); pnl DROP 32748; equity JUMP 1748906; assets JUMP 2204250; debt DROP 321286; FTE JUMP 33; destin691 empty; kapitaalsubsidies JUMP 162804; cash DROP 1359369; code73 549746; installaties JUMP 146824; capex 238660,strong,{SRC_PDF},outpatient rehab children/adolescents 2-19 Gent (RIZIV 96541526 + dual Ter Kouter cluster),RIZIV-conventioned ambulante revalidatie Gent,pnl DROP -72.92% (120950 to 32748) while omzet JUMP; kapitaalsubsidies JUMP +56.54%; destin 691 empty; installaties JUMP +691%; RIZIV/VL split unpublished; leftover same-zetel of Bolt/Mozaiek/DIGOR/Ter Kouter cluster,5.9,4.8,5,5.28,FOI RIZIV/VL matrix + 163k kapitaalsubsidies JUMP + pnl DROP + installaties JUMP + dual Drongen cluster,active,,tick2371; Strong official NBB PDF + Strong KBO; leftover Bolt@2370 same zetel; next leftover Buggenhout",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Gent>CAR_Impuls>RIZIV_VL_kapitaalsubsidies,vzw_car_impuls,RIZIV vs VL split inside omzet 2534712 + code 73 549746; nature of kapitaalsubsidies 162804 JUMP +56.54pct; toelichting destin 691 empty and pnl DROP 32748; installaties JUMP 146824 after capex 238660; dual Drongen zetel,Strong official PDF leftover RIZIV CAR of Bolt@2370 same zetel; 163k capital subsidies JUMP; pnl DROP -73pct; public CAR not private clinic,8,CAR Impuls VZW / Henk Schutyser voorzitter RvB,info@centrumimpuls.be,"Karel Lodewijk Dierickxstraat 30, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2371; ready NOT sent; Strong official NBB PDF; after Bolt@2370; leftover same-zetel CAR; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2371 + append rq_2372 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2371,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2371 line, found {n}")
if "rq_2372," in rq_text:
    raise SystemExit("rq_2372 already exists")

new_2371 = (
    "rq_2371,leftover dual — CAR Impuls YE2025 Strong (omzet JUMP 2.53m / pnl DROP / 163k kapitaalsubsidies JUMP),"
    "hole_fill,8,done,L5,vzw_car_impuls,"
    "Tick 2371 leftover after CAR Bolt. Prefer AGB/FARO if YE2025 else leftover same-zetel CAR Impuls 0416.318.951 deposit 2026-00206349 if live 2026pdf. "
    "Do NOT redo CAR Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:15:51Z,{STAMP},"
    "tick2371 CAR Impuls 0416.318.951 YE2025 Strong official PDF 2026-00206349; omzet JUMP 2534712; bruto DROP 2863608; pnl DROP 32748; equity JUMP 1748906; assets JUMP 2204250; debt DROP 321286; FTE JUMP 33; destin691 empty; kapitaalsubsidies JUMP 162804; cash DROP 1359369; FOI ready NOT sent; leftover Bolt@2370 same zetel CAR\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2371,"):
        parts.append(new_2371)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2371 replace count {replaced}")
new_rq = "".join(parts)
new_2372 = (
    "rq_2372,leftover dual after CAR Impuls — Buggenhout same-zetel,"
    "hole_fill,8,open,L5,,"
    "After CAR Impuls YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel Revalidatiecentrum Buggenhout 0412.404.903 deposit 2026-00205237 if live 2026pdf. "
    "Do NOT redo CAR Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2371; leftover Buggenhout same zetel HEAD 200 48084B this tick; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2372
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2371 + rq_2372; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2371,2371,no,"
    "tick2371 leftover dual CAR Impuls 0416.318.951 Strong PDF (omzet JUMP 2534712; bruto DROP 2863608 ~1.13x; pnl DROP 32748; equity JUMP 1748906; assets JUMP 2204250; debt DROP 321286; FTE JUMP 33; destin691 empty; kapitaalsubsidies JUMP 162804; cash DROP 1359369; 1 VE RSZ2025 86.959 RIZIV 96541526); after Bolt@2370 same zetel; leftover Buggenhout; AGB/FARO/Gandae YE2024; next rq_2372; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append (NOT every-10)
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2371 - rq_2371 CAR Impuls Gent (omzet JUMP 2.53m / pnl DROP -73% / 163k kapitaalsubsidies JUMP / Strong PDF)

- Unit: **rq_2371** leftover dual after **CAR Bolt@2370**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover same-zetel Flemish **CAR Impuls VZW** YE2025 (KBO **0416.318.951**; zetel Kloosterstraat 6, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs + Sig + DiGOR + Mozaiek + Bolt; VE **2.153.800.668** same address since 31.05.2006; operational Karel Lodewijk Dierickxstraat 30, 9000 Gent; **Actief** **1 VE**; RSZ2025 **86.959**; RIZIV **96541526** / HCO **29577** overeenkomst 953/965; leftover same-zetel CAR of mined **Bolt@2370** / **Mozaiek@2369** / **DiGOR@2368** / **Sig@2367** / **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355**; info@centrumimpuls.be). Confirmed leftover public (RIZIV-conventioned CAR + Departement Zorg) not private clinic. Do not redo Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VKT-VZW PDF deposit **2026-00206349** (50923 B / 13p; AV **08.05.2026**; header **24.06.2026**; CDN Last-Modified **10.07.2026**) — omzet 70 **EUR2534712** JUMP +2.38%; bruto **EUR2863608** DROP −0.49% (~**1.13x**); code 73 **EUR549746** JUMP +4.11%; pnl **EUR32748** DROP −72.92%; equity **EUR1748906** JUMP +5.52%; assets **EUR2204250** JUMP +0.98%; debt **EUR321286** DROP −17.92%; FTE **33** JUMP +3.45%; kapitaalsubsidies **EUR162804** JUMP +56.54%; destin 691 **empty**; cash **EUR1359369** DROP −2.46%; installaties **EUR146824** JUMP +691%; capex **EUR238660**. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.28); entities (+1 vzw_car_impuls); foi + draft `{GAP}`; rq_2371=done + rq_2372 open; loop_state ticks=2371; raw tick2371/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2372 leftover same-zetel Revalidatiecentrum Buggenhout 0412.404.903 deposit 2026-00205237 if live 2026pdf (HEAD 200 / 48084 B this tick).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
