#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2413_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bengelhof"
SRC_PDF = "src_bengelhof_jr2025_nbb_pdf_2413"
COMM = "comm_bengelhof_jr2025_statutory_bruto_933k_omzet73_empty_pnl_drop_11k"
LB = "lb_bengelhof_bruto_933k_omzet73_empty_pnl_drop_11k_destin_0_jr2025"
GAP = "gap_bengelhof_opgroeien_matrix_bruto_933k_omzet73_empty_pnl_drop_11k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":933326,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":933326,'
    '""2025_pnl"":10667,""2025_bedrijfswinst"":9876,'
    '""2025_equity"":433400,""2025_assets"":667298,""2025_debt"":212898,'
    '""2025_fte"":17.4,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":224013,""2025_geldbeleggingen"":363981,'
    '""2025_personnel62"":916206,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":4553,'
    '""2025_fondsen10"":446,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":432954,""2025_66A"":0,'
    '""2025_voorzieningen16"":21000,""2025_6061"":0,'
    '""2024_omzet"":0,""2024_bruto9900"":802755,""2024_73"":0,'
    '""2024_opbr"":802755,""2024_pnl"":27690,""2024_bedrijfswinst"":26790,'
    '""2024_equity"":422734,""2024_assets"":780792,'
    '""2024_debt"":337058,""2024_cash"":346873,""2024_fte"":15.2,'
    '""2024_destin691"":0,""2024_voorzieningen16"":21000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Bengelhof vzw YE2025 (bruto JUMP 933k / omzet+73 empty / pnl DROP 11k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_gent,VZW Bengelhof (KBO 0455.442.813; Actief; 1 VE 2.159.891.971; RSZ2025 88.911; Kinderopvang VG since 01.04.2014; 72 plaatsen inkomenstarief),2026-05-28,2025,2025,933326,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191897.pdf,Public CIK dual of mined city_gent,Publish Opgroeien/stad/ouder matrix behind bruto 933k + why 70+73 empty + why pnl DROP 11k + destin 0 + cash DROP 35pct + FTE JUMP 17.4,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>Bengelhof>JR2025_statutory_L5,tick2413; Strong official native PDF; leftover city_gent after Elfenbankje@2409; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Bengelhof bruto JUMP 933k / omzet+73 empty / pnl DROP 11k / destin 0 (YE2025 Gent CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>Bengelhof>JR2025,933326,933326,PDF bruto9900 JUMP 933326 CIK envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst DROP 9876; pnl DROP 10667; equity JUMP 433400; assets DROP 667298; debt DROP 212898; FTE JUMP 17.4; kapitaalsubsidies empty; destin691 empty; cash DROP 224013; geldbeleggingen JUMP 363981; gebouwen empty; 1 VE 72 plaatsen inkomenstarief,strong,{SRC_PDF},Opgroeien + CIK leftover city_gent,Opgroeien Kind en Gezin + leftover city_gent,933k bruto JUMP; omzet+73 empty; pnl DROP 11k; destin 0; leftover city_gent,5.22,5.12,5.08,5.14,FOI Opgroeien/stad/ouder matrix behind bruto 933k + why 70+73 empty + why pnl DROP 11k + destin 0 + cash DROP 35pct + FTE JUMP 17.4,active,,tick2413; Strong official NBB native PDF + Strong KBO; leftover city_gent after Elfenbankje@2409; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Gent>Bengelhof>CIK,{EID},Opgroeien/stad/ouder split behind bruto 933326 and why 70+73 empty on VKT; why pnl DROP 10667 (was 27690) and 9901 DROP 9876; why destin 691 empty and 9905 10667 fully to overgedragen 14 432954; why cash DROP 224013 and debt DROP 212898 via leveranciers 52979 (was 193004); FTE 17.4 JUMP; 1 VE; 72 plaatsen inkomenstarief,Strong official PDF leftover public CIK of city_gent; 933k bruto; public groepsopvang inkomenstarief not private clinic; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Bengelhof / Raad van Bestuur,bengelhof@dominovzw.be,"Sint-Margrietstraat 36, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2413; ready NOT sent; Strong official native NBB PDF; leftover city_gent CIK after Elfenbankje@2409; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
