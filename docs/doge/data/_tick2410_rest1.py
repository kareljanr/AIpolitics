#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2410_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnestraal_junior"
SRC_PDF = "src_zonnestraal_junior_jr2025_nbb_pdf_2410"
COMM = "comm_zonnestraal_junior_jr2025_statutory_73_200k_omzet_empty_bruto_neg88_pnl_loss_294"
LB = "lb_zonnestraal_junior_73_200k_omzet_empty_bruto_neg88_pnl_loss_294_destin_0_jr2025"
GAP = "gap_zonnestraal_junior_opgroeien_matrix_73_200k_omzet_empty_bruto_neg88_pnl_loss_294_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":-88,""2025_73"":200083,'
    '""2025_pnl"":-294,""2025_bedrijfswinst"":-88,'
    '""2025_equity"":4522,""2025_assets"":13118,""2025_debt"":8596,'
    '""2025_fte"":null,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":4522,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":0,""2025_gebouwen22"":0,'
    '""2025_fondsen10"":4177,""2025_overgedragen14"":345,'
    '""2025_6061"":200170,""2025_65"":206,'
    '""2024_omzet"":0,""2024_bruto9900"":-243,""2024_73"":207298,'
    '""2024_pnl"":-449,""2024_bedrijfswinst"":-243,'
    '""2024_equity"":4816,""2024_assets"":24962,'
    '""2024_debt"":20147,""2024_cash"":4816}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang Zonnestraal Junior vzw YE2025 (73 DROP 200k / omzet empty / bruto -88 / pnl LOSS 294 / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_sint_niklaas,VZW Kinderopvang Zonnestraal Junior (KBO 0866.116.859; Actief; 20 VE; RSZ2025 88.911; dual of parent KINDEROPVANG ZONNESTRAAL 0413.351.642 same zetel same board),2026-06-30,2025,2025,200083,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244618.pdf,Public CIK dual of mined city_sint_niklaas,Publish Opgroeien T1/T2/stad/ouder/parent matrix behind 73 200k + why 70 empty + why 73 pass-through 60/61 + why 20 VE vs 13k assets + dual vs parent 0413.351.642,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>ZonnestraalJunior>JR2025_statutory_L5,tick2410 EVERY-10; Strong official native PDF; leftover city_sint_niklaas after Elfenbankje@2409; NOT parent 0413.351.642; NOT Grimbergen VAPH Zonnestraal; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Zonnestraal Junior 73 DROP 200k / omzet empty / bruto -88 / pnl LOSS 294 / destin 0 (YE2025 Sint-Niklaas CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>ZonnestraalJunior>JR2025,200083,200083,PDF 73 DROP 200083 CIK envelope; omzet70 empty; bruto9900 -88; 76A empty; bedrijfswinst -88; pnl LOSS -294; equity DROP 4522; assets DROP 13118; debt DROP 8596; FTE unpublished; kapitaalsubsidies empty; destin691 empty; cash DROP 4522; geldbeleggingen empty; gebouwen empty; 60/61 200170; 20 VE residual vs parent 0413.351.642 1 VE same zetel same board,strong,{SRC_PDF},Opgroeien + CIK leftover city_sint_niklaas,Opgroeien Kind en Gezin + leftover city_sint_niklaas,200k 73 DROP; omzet empty; bruto -88; pnl LOSS 294; 20 VE vs 13k assets; leftover city_sint_niklaas,5.50,1.50,5.20,3.23,FOI Opgroeien T1/T2/stad/ouder/parent matrix behind 73 200k + why 70 empty + why 73 pass-through 60/61 + why 20 VE vs 13k assets + dual vs parent 0413.351.642,active,,tick2410 EVERY-10; Strong official NBB native PDF + Strong KBO; leftover city_sint_niklaas after Elfenbankje@2409; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>ZonnestraalJunior>CIK,{EID},Opgroeien T1/T2/stad/ouder/parent split behind 73 200083 and why 70 empty; why 73 pass-through 60/61 200170; why pnl LOSS -294 (was -449) and 9901 -88; why destin 691 empty; why 20 VE vs assets 13118 DROP and dual vs parent KINDEROPVANG ZONNESTRAAL 0413.351.642 same zetel same board; FTE unpublished,Strong official PDF leftover public CIK of city_sint_niklaas; 200k 73; public vergunde kinderopvang not private clinic; not parent 0413.351.642; not Grimbergen VAPH Zonnestraal; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Zonnestraal Junior / Raad van Bestuur,info@kinderopvangzonnestraal.be,"Gladiolenstraat 10, 9100 Sint-Niklaas",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2410 EVERY-10; ready NOT sent; Strong official native NBB PDF; leftover city_sint_niklaas CIK after Elfenbankje@2409; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
