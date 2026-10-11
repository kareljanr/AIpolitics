#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2409_stamp.txt").read_text().strip().splitlines()
EID = "vzw_elfenbankje"
SRC_PDF = "src_elfenbankje_jr2025_nbb_pdf_2409"
COMM = "comm_elfenbankje_jr2025_statutory_bruto_2_19m_omzet73_empty_pnl_drop_destin_0"
LB = "lb_elfenbankje_bruto_2_19m_omzet73_empty_pnl_drop_197k_destin_0_jr2025"
GAP = "gap_elfenbankje_opgroeien_matrix_bruto_2_19m_omzet73_empty_pnl_drop_197k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":2185717,""2025_73"":0,'
    '""2025_pnl"":197033,""2025_bedrijfswinst"":203285,'
    '""2025_equity"":2825006,""2025_assets"":3552531,""2025_debt"":727525,'
    '""2025_fte"":32.1,""2025_kapitaalsubsidies"":965541,""2025_destin691"":0,'
    '""2025_cash"":1286323,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":1842406,""2025_gebouwen22"":1896642,'
    '""2025_aanbouw27"":0,""2025_capex"":20654,""2025_bestemde13"":1140000,'
    '""2025_overgedragen14"":708004,""2025_76A"":2557,""2025_630"":137265,'
    '""2025_fondsen10"":11461,""2025_9061"":423000,""2025_LT17"":387000,'
    '""2025_6408"":2761,'
    '""2024_omzet"":0,""2024_bruto9900"":2127706,""2024_pnl"":204636,'
    '""2024_bedrijfswinst"":207419,""2024_equity"":2692476,""2024_assets"":3477682,'
    '""2024_debt"":785206,""2024_kapitaalsubsidies"":1030044,""2024_cash"":1137339,'
    '""2024_fte"":32.7,""2024_destin691"":1000000,""2024_gebouwen22"":2009160,'
    '""2024_76A"":11440}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang Elfenbankje vzw YE2025 (bruto JUMP 2.19m / omzet+73 empty / pnl DROP 197k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_gent,VZW Kinderopvang Elfenbankje (KBO 0417.638.151; Actief; 1 VE; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 12.12.2025; slorpte ELFENBANKJE D.V.O. 0862.573.884 since 30.03.2026 post-YE2025),2026-04-03,2025,2025,2185717,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00072866.pdf,Public CIK dual of mined city_gent,Publish Opgroeien T1/T2/stad/ouder matrix behind bruto 2.19m + why 70 and 73 empty + pnl DROP 197k + destin 0 after 1.00m + DVO absorption 30.03.2026 + cash JUMP 1.29m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>Elfenbankje>JR2025_statutory_L5,tick2409; Strong official native PDF; leftover city_gent after t Eekhoorntje@2408; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Elfenbankje bruto JUMP 2.19m / omzet+73 empty / pnl DROP 197k / destin 0 (YE2025 Gent CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>Elfenbankje>JR2025,2185717,2185717,PDF bruto9900 JUMP 2185717 CIK envelope; omzet70 empty; 73 empty; 76A 2557; bedrijfswinst DROP 203285; pnl DROP 197033; equity JUMP 2825006; assets JUMP 3552531; debt DROP 727525; FTE DROP 32.1; kapitaalsubsidies DROP 965541; destin691 0 was 1000000; cash JUMP 1286323; geldbeleggingen empty; gebouwen DROP 1896642; aanbouw empty; capex 20654; personeel 62 1842406; slorpte DVO 0862.573.884 30.03.2026 post-YE2025; 1 VE,strong,{SRC_PDF},Opgroeien + CIK leftover city_gent,Opgroeien Kind en Gezin + leftover city_gent,2.19m bruto JUMP; omzet+73 empty; pnl DROP 197k; destin 0 after 1.00m; leftover city_gent,5.28,5.36,5.14,5.26,FOI Opgroeien T1/T2/stad/ouder matrix behind bruto 2.19m + why 70 and 73 empty + pnl DROP 197k + destin 0 after 1.00m + DVO absorption 30.03.2026 + cash JUMP 1.29m,active,,tick2409; Strong official NBB native PDF + Strong KBO; leftover city_gent after t Eekhoorntje@2408; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Gent>Elfenbankje>CIK,{EID},Opgroeien T1/T2/stad/ouder split behind bruto 2185717 and why 70 and 73 empty; why pnl DROP 197033 (was 204636) and 9901 DROP 203285; why destin 691 is 0 after 1000000 in 2024; why slorpte ELFENBANKJE D.V.O. 0862.573.884 30.03.2026 same day as AV; why cash JUMP 1286323 vs geldbeleggingen empty; 1 VE + FTE 32.1,Strong official PDF leftover public CIK of city_gent; 2.19m bruto; public vergunde kinderopvang not private clinic; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Elfenbankje / Raad van Bestuur,kdv@elfenbankje.be,"Sint-Pietersaalststraat 80, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2409; ready NOT sent; Strong official native NBB PDF; leftover city_gent CIK after t Eekhoorntje@2408; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
