#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2411_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnestraal"
SRC_PDF = "src_zonnestraal_jr2025_nbb_pdf_2411"
COMM = "comm_zonnestraal_jr2025_statutory_opbr_3_56m_73_2_20m_omzet_1_35m_pnl_drop_112k"
LB = "lb_zonnestraal_opbr_3_56m_73_2_20m_omzet_1_35m_pnl_drop_112k_destin_0_jr2025"
GAP = "gap_zonnestraal_opgroeien_matrix_opbr_3_56m_73_2_20m_omzet_1_35m_pnl_drop_112k_destin_0_l5"
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
    '"{""2025_omzet"":1353656,""2025_bruto9900"":1563939,""2025_73"":2202564,'
    '""2025_76A"":286,""2025_opbr"":3556506,'
    '""2025_pnl"":112283,""2025_bedrijfswinst"":97457,'
    '""2025_equity"":1228898,""2025_assets"":1789323,""2025_debt"":560425,'
    '""2025_fte"":21.4,""2025_kapitaalsubsidies"":83575,""2025_destin691"":0,'
    '""2025_cash"":513151,""2025_geldbeleggingen"":833500,'
    '""2025_personnel62"":1356137,""2025_gebouwen22"":112546,'
    '""2025_aanbouw27"":0,""2025_capex"":2715,'
    '""2025_fondsen10"":387432,""2025_bestemde13"":200000,'
    '""2025_overgedragen14"":557891,""2025_66A"":62995,'
    '""2025_voorzieningen16"":0,""2025_6061"":2000414,'
    '""2024_omzet"":1379534,""2024_bruto9900"":1399358,""2024_73"":2169811,'
    '""2024_opbr"":3550184,""2024_pnl"":206670,""2024_bedrijfswinst"":190101,'
    '""2024_equity"":929811,""2024_assets"":1681646,'
    '""2024_debt"":537551,""2024_cash"":675489,""2024_fte"":18.1,'
    '""2024_destin691"":200000,""2024_voorzieningen16"":214284}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},KINDEROPVANG ZONNESTRAAL vzw YE2025 (opbr FLAT 3.56m / 73 2.20m / omzet 1.35m / pnl DROP 112k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_sint_niklaas,VZW KINDEROPVANG ZONNESTRAAL (KBO 0413.351.642; Actief; 1 VE; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; dual of Junior 0866.116.859 same zetel same board),2026-06-30,2025,2025,3556506,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244239.pdf,Public CIK dual of mined city_sint_niklaas,Publish Opgroeien T1/T2/stad/ouder/Junior matrix behind opbr 3.56m + why 70 commercial-only vs 73 2.20m + why pnl DROP 112k + destin 0 + voorzieningen 214k released + dual vs Junior 20 VE,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>Zonnestraal>JR2025_statutory_L5,tick2411; Strong official native PDF; leftover city_sint_niklaas after Junior@2410; NOT Junior 0866.116.859; NOT Grimbergen VAPH Zonnestraal; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Zonnestraal parent opbr FLAT 3.56m / 73 2.20m / omzet 1.35m / pnl DROP 112k / destin 0 (YE2025 Sint-Niklaas CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>Zonnestraal>JR2025,3556506,3556506,PDF bedrijfsopbrengsten 70+73+76A FLAT 3556506 VZW envelope; omzet70 DROP 1353656 commercial-only vs large 73 JUMP 2202564; 76A 286; bruto9900 JUMP 1563939; bedrijfswinst DROP 97457; pnl DROP 112283; equity JUMP 1228898; assets JUMP 1789323; debt JUMP 560425; FTE JUMP 21.4; kapitaalsubsidies DROP 83575; destin691 empty; cash DROP 513151; geldbeleggingen JUMP 833500; gebouwen 112546; voorzieningen 16 released 214284; 1 VE parent vs Junior 0866.116.859 20 VE same zetel same board,strong,{SRC_PDF},Opgroeien + CIK leftover city_sint_niklaas,Opgroeien Kind en Gezin + leftover city_sint_niklaas,3.56m opbr FLAT; 73 2.20m; omzet 1.35m commercial-only; pnl DROP 112k; destin 0; leftover city_sint_niklaas,5.42,5.32,5.20,5.34,FOI Opgroeien T1/T2/stad/ouder/Junior matrix behind opbr 3.56m + why 70 commercial-only vs 73 2.20m + why pnl DROP 112k + destin 0 + voorzieningen 214k released + dual vs Junior 20 VE,active,,tick2411; Strong official NBB native PDF + Strong KBO; leftover city_sint_niklaas after Junior@2410; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>Zonnestraal>CIK,{EID},Opgroeien T1/T2/stad/ouder/Junior split behind bedrijfsopbrengsten 3556506 and why 70 1353656 commercial-only vs 73 2202564; why pnl DROP 112283 (was 206670) and 9901 DROP 97457; why destin 691 empty (was 200000) and voorzieningen 16 released 214284; why 1 VE vs Junior 0866.116.859 20 VE same zetel same board; FTE 21.4,Strong official PDF leftover public CIK of city_sint_niklaas; 3.56m opbr; public vergunde kinderopvang not private clinic; not Junior 0866.116.859; not Grimbergen VAPH Zonnestraal; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW KINDEROPVANG ZONNESTRAAL / Raad van Bestuur,info@kinderopvangzonnestraal.be,"Gladiolenstraat 10, 9100 Sint-Niklaas",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2411; ready NOT sent; Strong official native NBB PDF; leftover city_sint_niklaas CIK after Junior@2410; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
