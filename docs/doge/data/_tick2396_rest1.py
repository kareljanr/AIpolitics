#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2396_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_accent"
SRC_PDF = "src_accent_jr2025_nbb_pdf_2396"
COMM = "comm_accent_jr2025_statutory_bruto_1_24m_omzet73_empty_pnl_loss"
LB = "lb_accent_bruto_1_24m_omzet73_empty_pnl_loss_17k_jr2025"
GAP = "gap_accent_riziv_vl_vaph_matrix_bruto_1_24m_omzet73_empty_pnl_loss_17k_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

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

cash_json = (
    '"{""2025_omzet"":0,""2025_bruto9900"":1242740,""2025_73"":0,'
    '""2025_7076A"":0,""2025_pnl"":-17304,""2025_bedrijfswinst"":-96083,'
    '""2025_equity"":1988694,""2025_assets"":2194549,""2025_debt"":205855,'
    '""2025_fte"":14.1,""2025_kapitaalsubsidies"":411,""2025_destin691"":0,'
    '""2025_cash"":1320711,""2025_geldbeleggingen"":725000,'
    '""2025_personnel62"":1293483,""2025_gebouwen22"":66004,'
    '""2025_aanbouw27"":0,""2025_capex"":2698,""2025_fondsen10"":0,'
    '""2025_bestemde13"":3000,""2025_overgedragen14"":1985283,'
    '""2025_76A"":1404,""2025_66A"":19077,""2025_76B"":0,'
    '""2025_791"":0,""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto9900"":1125749,""2024_pnl"":-28673,""2024_bedrijfswinst"":-104678,'
    '""2024_equity"":2006203,""2024_assets"":2210889,""2024_debt"":204686,'
    '""2024_kapitaalsubsidies"":616,""2024_cash"":1362450,""2024_fte"":14.8,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":725000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Accent vzw YE2025 (bruto JUMP 1.24m / omzet+73 empty / pnl LOSS NARROW 17k / destin empty / Strong PDF),{EID},RIZIV + VAZG + leftover city_kortrijk,VZW CAR Accent (KBO 0413.208.122; Actief; 1 VE; RSZ2025 86.959),2026-06-29,2025,2025,1242740,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00215981.pdf,Public CAR dual of mined city_kortrijk,Publish RIZIV/VAPH/VAZG/stad matrix behind bruto 1.24m + empty 70/73 + pnl loss narrow 17k + destin empty + cash 1.32m vs beleggingen 725k flat,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>CAR Accent>JR2025_statutory_L5,tick2396; Strong official native PDF; leftover city_kortrijk after CAR Horizon@2395; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Accent bruto JUMP 1.24m / omzet+73 empty / pnl LOSS NARROW 17k / destin empty (YE2025 Kortrijk),L5,car_vzw_statutory,Vlaanderen>West-Vlaanderen>Kortrijk>CAR Accent>JR2025,1242740,1242740,PDF bruto JUMP 1242740 CAR envelope; omzet70 empty; 73 empty; 76A 1404; bedrijfswinst LOSS NARROW -96083; pnl LOSS NARROW -17304; equity DROP 1988694; assets DROP 2194549; debt JUMP 205855; FTE 14.1; kapitaalsubsidies DROP 411; destin691 empty; cash DROP 1320711; geldbeleggingen FLAT 725000; gebouwen 66004; aanbouw empty; capex 2698; personeel 62 1293483,strong,{SRC_PDF},children CAR Kortrijk-Heule ambulante revalidatie,RIZIV + VAZG + leftover city_kortrijk,1.24m CAR bruto JUMP 10.4pct; omzet+73 empty; pnl LOSS NARROW 17k; destin empty; cash 1.32m vs beleggingen FLAT 725k; leftover city_kortrijk,5.1,5.0,5.0,5.03,FOI RIZIV/VAPH/VAZG/stad matrix behind bruto 1.24m + empty 70/73 + pnl loss narrow 17k + destin empty + cash vs geldbeleggingen + 66A 19k,active,,tick2396; Strong official NBB native PDF + Strong KBO; leftover city_kortrijk after CAR Horizon@2395; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Ten Anker OFF Leieborg OFF m-accent Eeklo",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Kortrijk>CAR Accent>RIZIV_VAPH_VAZG,{EID},RIZIV/VAPH/VAZG/stad split behind bruto 1242740; why 70 and 73 empty on recognized CAR; why pnl LOSS NARROW -17304 (was -28673) and 9901 -96083; why 691 empty while 9905 -17304 hits overgedragen 1985283; why cash DROP 1320711 vs geldbeleggingen FLAT 725000; why kapitaalsubsidies DROP 411 with capex 2698; why 66A 19077,Strong official PDF leftover public CAR of city_kortrijk; 1.24m bruto; public CAR not private clinic; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411,8,CAR Accent VZW / Raad van Bestuur,info@revaccent.be,"Lagaeplein 12/14, 8501 Kortrijk-Heule",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2396; ready NOT sent; Strong official native NBB PDF; leftover city_kortrijk CAR after CAR Horizon@2395; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Ten Anker off Leieborg off m-accent Eeklo; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
