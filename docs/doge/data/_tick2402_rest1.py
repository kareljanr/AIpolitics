#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2402_stamp.txt").read_text().strip().splitlines()
EID = "vzw_cfr_zelzate"
SRC_PDF = "src_cfrzelzate_jr2025_nbb_pdf_2402"
COMM = "comm_cfrzelzate_jr2025_statutory_bruto_1_42m_omzet73_empty_pnl_loss_flip"
LB = "lb_cfrzelzate_bruto_1_42m_omzet73_empty_pnl_loss_flip_128k_jr2025"
GAP = "gap_cfrzelzate_riziv_vl_vaph_matrix_bruto_1_42m_omzet73_empty_pnl_loss_flip_128k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":1419621,""2025_73"":0,'
    '""2025_7076A"":0,""2025_pnl"":-127569,""2025_bedrijfswinst"":-129899,'
    '""2025_equity"":1259125,""2025_assets"":2709376,""2025_debt"":1450251,'
    '""2025_fte"":16.7,""2025_kapitaalsubsidies"":1005973,""2025_destin691"":0,'
    '""2025_cash"":441005,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":1470293,""2025_gebouwen22"":1874287,'
    '""2025_aanbouw27"":0,""2025_capex8169"":1630690,""2025_fondsen10"":18886,'
    '""2025_bestemde13"":0,""2025_overgedragen14"":234266,'
    '""2025_76A"":0,""2025_66A"":0,""2025_76B"":0,'
    '""2025_6408"":43668,""2025_630"":35559,""2025_hypotheek91621"":248000,'
    '""2024_bruto9900"":1462566,""2024_pnl"":9867,'
    '""2024_bedrijfswinst"":10167,""2024_equity"":662527,'
    '""2024_assets"":1127549,""2024_debt"":465022,'
    '""2024_kapitaalsubsidies"":281806,""2024_cash"":335361,""2024_fte"":16.6,'
    '""2024_destin691"":0,""2024_gebouwen22"":446235}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CFR Zelzate vzw YE2025 (bruto DROP 1.42m / omzet+73 empty / pnl LOSS FLIP 128k / capex 1.63m / Strong PDF),{EID},RIZIV + VAZG + leftover city_zelzate,VZW Centrum voor Functionele Revalidatie (KBO 0419.645.952; Actief; 1 VE; RSZ2025 86.959; Aanbestedende overheid),2026-06-30,2025,2025,1419621,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243990.pdf,Public CAR dual of mined city_zelzate,Publish RIZIV/VAZG/VAPH/stad + bouw matrix behind bruto 1.42m + empty 70/73 + pnl loss flip 128k + kapitaalsubsidies JUMP 1.01m + capex 1.63m + debt JUMP 1.45m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Zelzate>CFR>JR2025_statutory_L5,tick2402; Strong official native PDF; leftover city_zelzate after VERBINT@2401; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT WZC Zilverbos 0644.984.078; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CFR Zelzate bruto DROP 1.42m / omzet+73 empty / pnl LOSS FLIP 128k / capex 1.63m (YE2025 Zelzate nieuw gebouw),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Zelzate>CFR>JR2025,1419621,1419621,PDF bruto DROP 1419621 VKT envelope; omzet70 empty; 73 empty; bedrijfswinst LOSS FLIP -129899; pnl LOSS FLIP -127569; equity JUMP 1259125; assets JUMP 2709376; debt JUMP 1450251; FTE 16.7; kapitaalsubsidies JUMP 1005973; destin691 empty; cash JUMP 441005; geldbeleggingen empty; gebouwen 1874287 JUMP; aanbouw empty; capex 8169 1630690; hypotheek 248000; personeel 62 1470293,strong,{SRC_PDF},children CAR Zelzate ~135 kinderen 0-19,RIZIV + VAZG + leftover city_zelzate,1.42m bruto DROP; omzet+73 empty; pnl LOSS FLIP 128k; kapitaalsubsidies JUMP 1.01m; capex 1.63m nieuw gebouw; debt JUMP 1.45m; leftover city_zelzate,5.3,5.1,5.0,5.16,FOI RIZIV/VAZG/VAPH/stad + bouw matrix behind bruto 1.42m + empty 70/73 + pnl loss flip 128k + kapitaalsubsidies JUMP 1.01m + capex 1.63m + debt JUMP 1.45m,active,,tick2402; Strong official NBB native PDF + Strong KBO; leftover city_zelzate after VERBINT@2401; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Zelzate>CFR>CAR,{EID},RIZIV/VAZG/VAPH/stad split behind bruto 1419621 and why 70+73 empty; why pnl LOSS FLIP -127569 (was +9867) and 9901 LOSS FLIP -129899 after andere kosten 43668 and afschrijvingen 35559; why 691 empty while 14 DROP 234266; why cash JUMP 441005 vs schulden JUMP 1450251; why kapitaalsubsidies JUMP 1005973 with capex 1630690 gebouwen JUMP 1874287 hypotheek 248000 nieuw Stationsstraat,Strong official PDF leftover public CAR of city_zelzate; 1.42m bruto; public aanbestedende overheid not private clinic; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not WZC Zilverbos 0644.984.078; not m-accent Eeklo 0465.841.411; not CAR Noorderkempen 0408.078.010 scan,8,Centrum voor Functionele Revalidatie VZW / Raad van Bestuur,info@revalidatiecentrum.be,"Stationsstraat 40, 9060 Zelzate",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2402; ready NOT sent; Strong official native NBB PDF; leftover city_zelzate CAR after VERBINT@2401; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
