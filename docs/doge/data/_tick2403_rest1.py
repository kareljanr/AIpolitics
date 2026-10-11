#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2403_stamp.txt").read_text().strip().splitlines()
EID = "vzw_de_kade"
SRC_PDF = "src_dekade_jr2025_nbb_pdf_2403"
COMM = "comm_dekade_jr2025_statutory_opbr_60_22m_73_51_29m_pnl_drop"
LB = "lb_dekade_opbr_60_22m_73_51_29m_pnl_drop_destin_800k_jr2025"
GAP = "gap_dekade_vaph_car_matrix_opbr_60_22m_73_51_29m_pnl_drop_destin_800k_l5"
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
    '"{""2025_omzet"":7767727,""2025_bruto9900"":0,""2025_73"":51285974,'
    '""2025_7076A"":60221495,""2025_pnl"":803199,""2025_bedrijfswinst"":747615,'
    '""2025_equity"":64477006,""2025_assets"":86453940,""2025_debt"":20196222,'
    '""2025_fte"":657.5,""2025_kapitaalsubsidies"":11803327,""2025_destin691"":800000,'
    '""2025_cash"":5301142,""2025_geldbeleggingen"":21930224,'
    '""2025_personnel62"":48609106,""2025_gebouwen22"":40253767,'
    '""2025_aanbouw27"":10885,""2025_capex"":2185673,""2025_fondsen10"":26440058,'
    '""2025_bestemde13"":26226361,""2025_overgedragen14"":7260,'
    '""2025_76A"":2090,""2025_74"":1165704,""2025_733"":51179710,'
    '""2025_731"":62195,""2025_630"":3575060,'
    '""2024_7076A"":58577339,""2024_73"":49782751,""2024_omzet"":7732793,'
    '""2024_pnl"":2365138,""2024_bedrijfswinst"":1678673,""2024_equity"":64301634,'
    '""2024_assets"":85708946,""2024_debt"":19833252,'
    '""2024_kapitaalsubsidies"":12431154,""2024_cash"":18926306,""2024_fte"":649,'
    '""2024_destin691"":2395000,""2024_geldbeleggingen"":6176184}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},De Kade vzw YE2025 (opbr JUMP 60.22m / 73 51.29m / pnl DROP 803k / destin 800k / Strong PDF),{EID},VAPH + Departement Zorg CAR Spermalie + leftover city_brugge,VZW De Kade (KBO 0413.650.659; Actief; 35 VE; RSZ2025 87.201; VAPH+CAR+BuO),2026-07-15,2025,2025,60221495,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00300772.pdf,Public VAPH+CAR+BuO dual of mined city_brugge,Publish VAPH/CAR/BuO/stad matrix behind 70/76A 60.22m + 73 51.29m + pnl DROP 803k + destin DROP 800k + cash DROP vs beleggingen JUMP,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Brugge>DeKade>JR2025_statutory_L5,tick2403; Strong official native PDF; leftover city_brugge after CFR Zelzate@2402; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},De Kade opbr JUMP 60.22m / 73 51.29m / pnl DROP 803k / destin 800k (YE2025 Brugge VAPH+CAR+BuO),L5,vaph_car_vzw_statutory,Vlaanderen>West-Vlaanderen>Brugge>DeKade>JR2025,60221495,60221495,PDF 70/76A JUMP 60221495 VAPH+CAR+BuO envelope; omzet70 7767727 commercial-only; 73 JUMP 51285974; bedrijfswinst DROP 747615; pnl DROP 803199; equity JUMP 64477006; assets JUMP 86453940; debt JUMP 20196222; FTE 657.5; kapitaalsubsidies DROP 11803327; destin691 DROP 800000; cash DROP 5301142; geldbeleggingen JUMP 21930224; gebouwen 40253767; aanbouw 10885; capex 2185673; personeel 62 48609106,strong,{SRC_PDF},VAPH + CAR Spermalie + BuO leftover city_brugge,VAPH + Departement Zorg + leftover city_brugge,60.22m 70/76A JUMP; 73 51.29m; pnl DROP 803k; destin DROP 800k; cash DROP vs beleggingen JUMP 21.93m; leftover city_brugge,6.2,6.0,5.8,6.05,FOI VAPH/CAR/BuO/stad matrix behind 70/76A 60.22m + 73 51.29m + pnl DROP 803k + destin DROP 800k + cash DROP vs beleggingen JUMP,active,,tick2403; Strong official NBB native PDF + Strong KBO; leftover city_brugge after CFR Zelzate@2402; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Brugge>DeKade>VAPH+CAR,{EID},VAPH/CAR Spermalie/BuO/stad split behind 70/76A 60221495 and 73 51285974 and why omzet 70 7767727 commercial-only; why pnl DROP 803199 (was 2365138) and 9901 DROP 747615 after personeel 48609106; why 691 DROP 800000 (was 2395000); why cash DROP 5301142 vs geldbeleggingen JUMP 21930224; why kapitaalsubsidies DROP 11803327 with capex 2185673,Strong official PDF leftover public VAPH+CAR+BuO of city_brugge; 60.22m 70/76A; public VAPH/CAR not private clinic; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,De Kade VZW / Raad van Bestuur,info@de-kade.be,"Potterierei 42, 8000 Brugge",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2403; ready NOT sent; Strong official native NBB PDF; leftover city_brugge VAPH+CAR after CFR Zelzate@2402; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
