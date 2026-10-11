#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2399_stamp.txt").read_text().strip().splitlines()
EID = "vzw_heuvelheem"
SRC_PDF = "src_heuvelheem_jr2025_nbb_pdf_2399"
COMM = "comm_heuvelheem_jr2025_statutory_opbr_15_17m_73_12_22m_pnl_flip"
LB = "lb_heuvelheem_opbr_15_17m_73_12_22m_pnl_flip_405k_jr2025"
GAP = "gap_heuvelheem_vaph_matrix_opbr_15_17m_73_12_22m_pnl_flip_destin_empty_l5"
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
    '"{""2025_omzet"":181042,""2025_73"":12221891,'
    '""2025_7076A"":15172213,""2025_pnl"":404772,""2025_bedrijfswinst"":453416,'
    '""2025_equity"":7254780,""2025_assets"":10879683,""2025_debt"":3267730,'
    '""2025_fte"":152.3,""2025_kapitaalsubsidies"":942213,""2025_destin691"":0,'
    '""2025_cash"":772792,""2025_geldbeleggingen"":206185,'
    '""2025_personnel62"":11821579,""2025_gebouwen22"":6132505,'
    '""2025_aanbouw27"":867145,""2025_capex"":1894318,""2025_fondsen10"":369858,'
    '""2025_bestemde13"":5257556,""2025_overgedragen14"":685153,'
    '""2025_76A"":265452,""2025_66A"":0,""2025_76B"":0,'
    '""2025_74"":2503828,""2025_731"":64024,""2025_733"":12157867,'
    '""2025_791"":0,""2024_omzet"":150825,""2024_73"":11490437,'
    '""2024_7076A"":14158123,""2024_pnl"":-72089,""2024_bedrijfswinst"":-54671,'
    '""2024_equity"":6932417,""2024_assets"":9609483,""2024_debt"":2467775,'
    '""2024_kapitaalsubsidies"":1024622,""2024_cash"":1375924,""2024_fte"":156.4,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":206147}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Heuvelheem vzw YE2025 (opbr JUMP 15.17m / 73 12.22m / pnl PROFIT FLIP 405k / destin empty / Strong PDF),{EID},VAPH + leftover city_kruisem + leftover city_oudenaarde,VZW Heuvelheem (KBO 0413.210.201; Actief; 8 VE; RSZ2025 87.202),2026-06-30,2025,2025,15172213,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243798.pdf,Public VAPH dual of mined city_kruisem + leftover city_oudenaarde,Publish VAPH/VIPA/stad matrix behind opbr 15.17m + 73 12.22m + pnl flip 405k + cash drop 773k + De Zalm loan,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Kruisem>Heuvelheem>JR2025_statutory_L5,tick2399; Strong official native PDF; leftover city_kruisem after Halle Asse@2398; NOT Vijvens 0415.093.385; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Heuvelheem opbr JUMP 15.17m / 73 12.22m / pnl PROFIT FLIP 405k / cash DROP 773k (YE2025 Kruisem),L5,vaph_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Kruisem>Heuvelheem>JR2025,15172213,15172213,PDF opbr JUMP 15172213 VAPH envelope; omzet70 181042 commercial-only; 73 JUMP 12221891; 76A 265452 VAPH 2024 surplus; bedrijfswinst PROFIT FLIP 453416; pnl PROFIT FLIP 404772; equity JUMP 7254780; assets JUMP 10879683; debt JUMP 3267730; FTE 152.3; kapitaalsubsidies DROP 942213; destin691 empty; cash DROP 772792; geldbeleggingen 206185; gebouwen 6132505; aanbouw 867145; capex 1894318; personeel 62 11821579,strong,{SRC_PDF},adults with disability Heuvelheem VAPH,VAPH + leftover city_kruisem + leftover city_oudenaarde,15.17m VAPH opbr JUMP 7.16pct; 73 12.22m; pnl PROFIT FLIP 405k; cash DROP 773k; debt JUMP 3.27m after De Zalm; leftover city_kruisem + leftover city_oudenaarde,5.9,5.9,5.7,5.91,FOI VAPH/VIPA/stad matrix behind opbr 15.17m + 73 12.22m + pnl flip 405k + cash drop 773k + De Zalm loan,active,,tick2399; Strong official NBB native PDF + Strong KBO; leftover city_kruisem after Halle Asse@2398; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Ten Anker OFF Leieborg OFF m-accent Eeklo",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Kruisem>Heuvelheem>VAPH_VIPA,{EID},VAPH/VIPA/stad split behind opbr 15172213 and 73 12221891; why omzet 70 only 181042 commercial-only; why pnl PROFIT FLIP 404772 (was -72089) and 9901 PROFIT FLIP 453416; why 76A 265452 VAPH 2024 surplus vs raming; why 691 empty while 14 JUMP 685153; why cash DROP 772792 vs schulden JUMP 3267730 after De Zalm purchase + new loan; why kapitaalsubsidies DROP 942213 with capex 1894318,Strong official PDF leftover public VAPH of city_kruisem + leftover city_oudenaarde; 15.17m opbr; public VAPH not private clinic; not Vijvens 0415.093.385; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411,8,Heuvelheem VZW / Raad van Bestuur,info@heuvelheem.be,"Nokerepontweg 1, 9772 Kruisem",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2399; ready NOT sent; Strong official native NBB PDF; leftover city_kruisem VAPH after Halle Asse@2398; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Ten Anker off Leieborg off m-accent Eeklo; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
