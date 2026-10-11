#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2400_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_antwerpen"
SRC_PDF = "src_arc_jr2025_nbb_pdf_2400"
COMM = "comm_arc_jr2025_statutory_bruto_2_49m_omzet73_empty_pnl_jump"
LB = "lb_arc_bruto_2_49m_omzet73_empty_pnl_jump_174k_jr2025"
GAP = "gap_arc_riziv_vl_vaph_matrix_bruto_2_49m_omzet73_empty_pnl_jump_destin_170k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":2489143,""2025_73"":0,'
    '""2025_7076A"":0,""2025_pnl"":174281,""2025_bedrijfswinst"":156794,'
    '""2025_equity"":1771285,""2025_assets"":2168233,""2025_debt"":396948,'
    '""2025_fte"":30,""2025_kapitaalsubsidies"":81587,""2025_destin691"":170000,'
    '""2025_cash"":779521,""2025_geldbeleggingen"":880000,'
    '""2025_personnel62"":2264763,""2025_gebouwen22"":280301,'
    '""2025_aanbouw27"":0,""2025_capex"":95710,""2025_fondsen10"":26182,'
    '""2025_bestemde13"":1050000,""2025_overgedragen14"":613515,'
    '""2025_76A"":0,""2025_66A"":0,""2025_76B"":0,'
    '""2025_791"":0,""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto9900"":2492732,""2024_pnl"":155804,""2024_bedrijfswinst"":152349,'
    '""2024_equity"":1616919,""2024_assets"":2044774,""2024_debt"":427855,'
    '""2024_kapitaalsubsidies"":101502,""2024_cash"":467035,""2024_fte"":29.3,'
    '""2024_destin691"":880000,""2024_geldbeleggingen"":880000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Antwerps Revalidatiecentrum vzw YE2025 (bruto FLAT 2.49m / omzet+73 empty / pnl JUMP 174k / destin DROP 170k / Strong PDF),{EID},RIZIV + VAZG + leftover city_antwerpen,VZW Antwerps Revalidatiecentrum (KBO 0408.434.930; Actief; 1 VE; RSZ2025 86.959),2026-07-09,2025,2025,2489143,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00272201.pdf,Public CAR dual of mined city_antwerpen,Publish RIZIV/VAPH/VAZG/stad matrix behind bruto 2.49m + empty 70/73 + pnl jump 174k + destin nieuwbouwfonds DROP 170k + cash JUMP 780k,{SRC_PDF},strong,Vlaanderen>Antwerpen>Antwerpen-stad>CAR ARC>JR2025_statutory_L5,tick2400 EVERY-10; Strong official native PDF; leftover city_antwerpen after Heuvelheem@2399; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo 0465.841.411; NOT Vriendenkring 0436.787.139; NOT CAR Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},ARC Antwerpen bruto FLAT 2.49m / omzet+73 empty / pnl JUMP 174k / destin DROP 170k (YE2025 Antwerpen),L5,car_vzw_statutory,Vlaanderen>Antwerpen>Antwerpen-stad>CAR ARC>JR2025,2489143,2489143,PDF bruto DROP 2489143 CAR envelope; omzet70 empty; 73 empty; 76A 0; bedrijfswinst JUMP 156794; pnl JUMP 174281; equity JUMP 1771285; assets JUMP 2168233; debt DROP 396948; FTE 30; kapitaalsubsidies DROP 81587; destin691 DROP 170000 nieuwbouwfonds; cash JUMP 779521; geldbeleggingen 880000 FLAT; gebouwen 280301; aanbouw empty; capex 95710; personeel 62 2264763,strong,{SRC_PDF},children CAR ARC ambulante revalidatie,RIZIV + VAZG + leftover city_antwerpen,2.49m CAR bruto FLAT; omzet+73 empty; pnl JUMP 174k; destin nieuwbouwfonds DROP 170k; cash JUMP 780k; leftover city_antwerpen,5.3,5.2,5.1,5.21,FOI RIZIV/VAPH/VAZG/stad matrix behind bruto 2.49m + empty 70/73 + pnl jump 174k + destin nieuwbouwfonds DROP 170k + cash JUMP 780k,active,,tick2400 EVERY-10; Strong official NBB native PDF + Strong KBO; leftover city_antwerpen after Heuvelheem@2399; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Antwerpen>Antwerpen-stad>CAR ARC>RIZIV_VAPH_VAZG,{EID},RIZIV/VAPH/VAZG/stad split behind bruto 2489143; why 70 and 73 empty on recognized CAR; why pnl JUMP 174281 (was 155804) and 9901 JUMP 156794; why 691 DROP 170000 nieuwbouwfonds while fonds 13 JUMP 1050000; why cash JUMP 779521 vs schulden DROP 396948; why kapitaalsubsidies DROP 81587 with capex 95710,Strong official PDF leftover public CAR of city_antwerpen; 2.49m bruto; public CAR not private clinic; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411; not Vriendenkring 0436.787.139; not CAR Antenne 3000 0433.184.479,8,Antwerps Revalidatiecentrum VZW / Raad van Bestuur,info@arc-reva.be,"Lange Elzenstraat 52-54, 2018 Antwerpen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2400 EVERY-10; ready NOT sent; Strong official native NBB PDF; leftover city_antwerpen CAR after Heuvelheem@2399; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
