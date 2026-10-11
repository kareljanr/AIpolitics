#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2401_stamp.txt").read_text().strip().splitlines()
EID = "vzw_verbint"
SRC_PDF = "src_verbint_jr2025_nbb_pdf_2401"
COMM = "comm_verbint_jr2025_statutory_omzet_12_89m_73_10_06m_pnl_jump"
LB = "lb_verbint_omzet_12_89m_73_10_06m_pnl_jump_6_0m_jr2025"
GAP = "gap_verbint_car_clb_wzc_vaph_matrix_omzet_12_89m_73_10_06m_pnl_jump_6_0m_l5"
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
    '"{""2025_omzet"":12890158,""2025_bruto9900"":0,""2025_73"":10059857,'
    '""2025_7076A"":31375466,""2025_pnl"":5963538,""2025_bedrijfswinst"":5978070,'
    '""2025_equity"":30969115,""2025_assets"":48228242,""2025_debt"":16245572,'
    '""2025_fte"":207.7,""2025_kapitaalsubsidies"":2615933,""2025_destin691"":284439,'
    '""2025_cash"":6890725,""2025_geldbeleggingen"":12298772,'
    '""2025_personnel62"":16642024,""2025_gebouwen22"":24214101,'
    '""2025_aanbouw27"":65325,""2025_capex8161"":21608874,""2025_fondsen10"":6222868,'
    '""2025_bestemde13"":6031592,""2025_overgedragen14"":16098723,'
    '""2025_76A"":6524604,""2025_66A"":1388882,""2025_76B"":0,'
    '""2025_791"":75556,""2024_omzet"":7192948,""2024_73"":8927185,'
    '""2024_7076A"":17551685,""2024_pnl"":668995,""2024_bedrijfswinst"":615325,'
    '""2024_equity"":14766643,""2024_assets"":23865928,""2024_debt"":8097298,'
    '""2024_kapitaalsubsidies"":2786184,""2024_cash"":3105490,""2024_fte"":159.7,'
    '""2024_destin691"":214164,""2024_geldbeleggingen"":2450000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},VERBINT vzw YE2025 (omzet JUMP 12.89m / 73 10.06m / pnl JUMP 6.0m / destin 284k / KMSI fusion / Strong PDF),{EID},RIZIV + VAZG + VAPH + Onderwijs CLB + leftover city_turnhout,VZW VERBINT (KBO 0408.032.379; Actief; 20 VE; RSZ2025 85.691; Aanbestedende overheid),2026-07-14,2025,2025,12890158,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00297392.pdf,Public CAR/CLB/WZC/VAPH dual of mined city_turnhout,Publish CAR/CLB/WZC/VAPH/stad matrix behind omzet 12.89m + 73 10.06m + 76A meerwaarden 6.52m + pnl jump 6.0m + destin 284k + cash JUMP 6.89m,{SRC_PDF},strong,Vlaanderen>Antwerpen>Turnhout>VERBINT>JR2025_statutory_L5,tick2401; Strong official native PDF; leftover city_turnhout + city_mechelen + city_westerlo after ARC@2400; KMSI fusion 31.03.2025 not like-for-like; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},VERBINT omzet JUMP 12.89m / 73 10.06m / pnl JUMP 6.0m / destin 284k (YE2025 Turnhout KMSI fusion),L5,car_clb_wzc_vzw_statutory,Vlaanderen>Antwerpen>Turnhout>VERBINT>JR2025,12890158,31375466,PDF omzet JUMP 12890158 CAR/WZC envelope; 73 JUMP 10059857; 70/76A JUMP 31375466; 76A 6524604 meerwaarden; bedrijfswinst JUMP 5978070; pnl JUMP 5963538; equity JUMP 30969115; assets JUMP 48228242; debt JUMP 16245572; FTE 207.7; kapitaalsubsidies DROP 2615933; destin691 JUMP 284439; cash JUMP 6890725; geldbeleggingen JUMP 12298772; gebouwen 24214101; aanbouw 65325; 8161 fusion 21608874; personeel 62 16642024,strong,{SRC_PDF},children CAR Carrewiel + WZC De Winde + VAPH Muylenberg + Vrij CLB Kempen,RIZIV + VAZG + VAPH + Onderwijs CLB + leftover city_turnhout,12.89m omzet JUMP after KMSI fusion; 73 10.06m; 76A meerwaarden 6.52m; pnl JUMP 6.0m; destin 284k; cash JUMP 6.89m; leftover city_turnhout,5.4,6.2,5.3,5.70,FOI CAR/CLB/WZC/VAPH/stad matrix behind omzet 12.89m + 73 10.06m + 76A meerwaarden 6.52m + pnl jump 6.0m + destin 284k + cash JUMP 6.89m,active,,tick2401; Strong official NBB native PDF + Strong KBO; leftover city_turnhout after ARC@2400; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Antwerpen>Turnhout>VERBINT>CAR_CLB_WZC_VAPH,{EID},CAR/CLB/WZC/VAPH/stad split behind omzet 12890158 and 73 10059857; why 6.9 731+733 does not sum to 73 (gap 2.47m); why pnl JUMP 5963538 (was 668995) and 9901 JUMP 5978070 after 76A meerwaarden 6524604 and KMSI fusion; why 691 JUMP 284439 while fonds 13 JUMP 6031592; why cash JUMP 6890725 and geldbeleggingen JUMP 12298772 vs schulden JUMP 16245572; why kapitaalsubsidies DROP 2615933 with 8161 21608874 fusion-inclusive,Strong official PDF leftover public CAR/CLB/WZC/VAPH of city_turnhout; 12.89m omzet; public aanbestedende overheid not private clinic; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411; not CAR Noorderkempen 0408.078.010 scan,8,VERBINT VZW / Raad van Bestuur,info@verbint.be,"Korte Begijnenstraat 22, 2300 Turnhout",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2401; ready NOT sent; Strong official native NBB PDF; leftover city_turnhout CAR/CLB/WZC after ARC@2400; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan; Zelzate now live 2026-00243990 not taken; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
