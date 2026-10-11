#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2397_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_waas"
SRC_PDF = "src_waas_jr2025_nbb_pdf_2397"
COMM = "comm_waas_jr2025_statutory_bruto_1_64m_omzet73_empty_pnl_drop"
LB = "lb_waas_bruto_1_64m_omzet73_empty_pnl_drop_3k_jr2025"
GAP = "gap_waas_riziv_vl_vaph_matrix_bruto_1_64m_omzet73_empty_pnl_drop_3k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":1636836,""2025_73"":0,'
    '""2025_7076A"":0,""2025_pnl"":3351,""2025_bedrijfswinst"":-49573,'
    '""2025_equity"":1550659,""2025_assets"":1801270,""2025_debt"":250611,'
    '""2025_fte"":21.1,""2025_kapitaalsubsidies"":269052,""2025_destin691"":0,'
    '""2025_cash"":376211,""2025_geldbeleggingen"":425831,'
    '""2025_personnel62"":1586724,""2025_gebouwen22"":720801,'
    '""2025_aanbouw27"":0,""2025_capex"":60067,""2025_fondsen10"":0,'
    '""2025_bestemde13"":600000,""2025_overgedragen14"":681607,'
    '""2025_76A"":0,""2025_66A"":0,""2025_76B"":0,'
    '""2025_791"":0,""2025_vorderingen41"":140000,""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto9900"":1632676,""2024_pnl"":73282,""2024_bedrijfswinst"":26680,'
    '""2024_equity"":1585744,""2024_assets"":1829025,""2024_debt"":243281,'
    '""2024_kapitaalsubsidies"":307488,""2024_cash"":443678,""2024_fte"":19.9,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":528272}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Waas Revalidatiecentrum vzw YE2025 (bruto 1.64m / omzet+73 empty / pnl DROP 3k / destin empty / Strong PDF),{EID},RIZIV + VAZG + leftover city_lokeren,VZW Waas Revalidatiecentrum Lokeren (KBO 0415.472.279; Actief; 1 VE; RSZ2025 86.959),2026-06-30,2025,2025,1636836,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243160.pdf,Public CAR dual of mined city_lokeren,Publish RIZIV/VAPH/VAZG/stad matrix behind bruto 1.64m + empty 70/73 + pnl drop 3k + destin empty + cash 376k vs beleggingen 426k + 140k overige vorderingen,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Lokeren>Waas Revalidatiecentrum>JR2025_statutory_L5,tick2397; Strong official native PDF; leftover city_lokeren after CAR Accent@2396; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Waas Revalidatiecentrum bruto 1.64m / omzet+73 empty / pnl DROP 3k / destin empty (YE2025 Lokeren),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Lokeren>Waas Revalidatiecentrum>JR2025,1636836,1636836,PDF bruto JUMP 1636836 CAR envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst LOSS FLIP -49573; pnl DROP 3351; equity DROP 1550659; assets DROP 1801270; debt JUMP 250611; FTE 21.1; kapitaalsubsidies DROP 269052; destin691 empty; cash DROP 376211; geldbeleggingen DROP 425831; gebouwen 720801; aanbouw empty; capex 60067; personeel 62 1586724; overige vorderingen 41 140000,strong,{SRC_PDF},children CAR Lokeren ambulante revalidatie,RIZIV + VAZG + leftover city_lokeren,1.64m CAR bruto JUMP 0.25pct; omzet+73 empty; pnl DROP 3k; destin empty; cash 376k vs beleggingen DROP 426k; 140k new overige vorderingen; leftover city_lokeren,5.2,5.1,5.0,5.10,FOI RIZIV/VAPH/VAZG/stad matrix behind bruto 1.64m + empty 70/73 + pnl drop 3k + destin empty + cash vs geldbeleggingen + 140k overige vorderingen,active,,tick2397; Strong official NBB native PDF + Strong KBO; leftover city_lokeren after CAR Accent@2396; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Ten Anker OFF Leieborg OFF m-accent Eeklo",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Lokeren>Waas Revalidatiecentrum>RIZIV_VAPH_VAZG,{EID},RIZIV/VAPH/VAZG/stad split behind bruto 1636836; why 70 and 73 empty on recognized CAR; why pnl DROP 3351 (was 73282) and 9901 LOSS FLIP -49573; why 691 empty while 9905 3351 hits overgedragen 681607; why cash DROP 376211 vs geldbeleggingen DROP 425831 vs overige vorderingen JUMP 140000; why kapitaalsubsidies DROP 269052 with capex 60067,Strong official PDF leftover public CAR of city_lokeren; 1.64m bruto; public CAR not private clinic; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411,8,Waas Revalidatiecentrum Lokeren VZW / Raad van Bestuur,kaat.degeest@waasrevalidatiecentrum.be,"Luikstraat 109, 9160 Lokeren",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2397; ready NOT sent; Strong official native NBB PDF; leftover city_lokeren CAR after CAR Accent@2396; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Ten Anker off Leieborg off m-accent Eeklo; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
