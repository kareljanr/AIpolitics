#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2420_stamp.txt").read_text().strip().splitlines()
EID = "vzw_ruyschaert"
SRC_PDF = "src_ruyschaert_jr2025_nbb_pdf_2420"
COMM = "comm_ruyschaert_jr2025_statutory_omzet_8_83m_73_1_68m_pnl_flip_242k"
LB = "lb_ruyschaert_omzet_8_83m_73_1_68m_opbr_11_21m_pnl_flip_242k_destin_0_jr2025"
GAP = "gap_ruyschaert_zorg_matrix_omzet_8_83m_73_1_68m_opbr_11_21m_pnl_flip_242k_destin_0_l5"
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
    '"{""2025_omzet"":8827505,""2025_73"":1681843,""2025_74"":357939,'
    '""2025_76A"":343692,""2025_opbr"":11210979,'
    '""2025_pnl"":241655,""2025_bedrijfswinst"":231417,'
    '""2025_equity"":449438,""2025_assets"":2398167,""2025_debt"":1797724,'
    '""2025_fte"":121.2,""2025_kapitaalsubsidies"":3504,""2025_destin691"":0,'
    '""2025_cash"":667324,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":8461817,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":222899,'
    '""2025_fondsen10"":301954,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":143980,""2025_66A"":63,'
    '""2025_66B"":0,""2025_voorzieningen16"":151005,""2025_76B"":0,'
    '""2024_omzet"":8634912,""2024_73"":1614070,'
    '""2024_opbr"":10545142,""2024_pnl"":-479473,""2024_bedrijfswinst"":-492989,'
    '""2024_equity"":209534,""2024_assets"":2521760,'
    '""2024_debt"":2140726,""2024_cash"":740936,""2024_fte"":122.3,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":5256,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},WZC De Ruyschaert vzw YE2025 (omzet JUMP 8.83m / 73 1.68m / opbr 11.21m / pnl FLIP 242k / destin 0 / Strong PDF),{EID},Departement Zorg + RIZIV + leftover city_kortrijk,VZW Integrale Bejaardenzorg Sint-Jozef / WZC De Ruyschaert (KBO 0434.996.993; Actief; 1 VE Kloosterstraat 25 Marke; RSZ2025 87.301; WZC 111 woongelegenheden),2026-06-10,2025,2025,8827505,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00183610.pdf,Public WZC dual of mined city_kortrijk,Publish Zorg/RIZIV/dagprijs matrix behind omzet 8.83m + why 73 1.68m + why 76A 344k Marcade/GroenWest + why 9901 FLIP 231k + pnl FLIP 242k + destin 0 + debt DROP 1.80m,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>WZC De Ruyschaert>JR2025_statutory_L5,tick2420; Strong official native PDF; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder; NOT Kloosterstraat 6 Drongen; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},WZC De Ruyschaert omzet JUMP 8.83m / 73 1.68m / opbr 11.21m / pnl FLIP 242k / destin 0 (YE2025 Kortrijk WZC),L5,wzc_vzw_statutory,Vlaanderen>West-Vlaanderen>Kortrijk>WZC De Ruyschaert>JR2025,8827505,8827505,PDF omzet70 JUMP 8827505 envelope not commercial-only; 73 JUMP 1681843; 74 JUMP 357939; 76A JUMP 343692; opbr 70/76A JUMP 11210979; bedrijfswinst FLIP 231417; pnl FLIP 241655; equity JUMP 449438; assets DROP 2398167; debt DROP 1797724; FTE DROP 121.2; kapitaalsubsidies DROP 3504; destin691 empty; cash DROP 667324; geldbeleggingen empty; gebouwen empty; 1 VE Kloosterstraat 25 Marke,strong,{SRC_PDF},Departement Zorg + leftover city_kortrijk,Departement Zorg RIZIV + leftover city_kortrijk,8.83m omzet; 73 1.68m; opbr 11.21m; 76A 344k one-off; 9901 FLIP 231k; pnl FLIP 242k; destin 0; leftover city_kortrijk,5.40,5.50,5.20,5.40,FOI Zorg/RIZIV/dagprijs matrix behind omzet 8.83m + why 73 1.68m + why 76A 344k Marcade/GroenWest + why 9901 FLIP 231k + pnl FLIP 242k + destin 0 + debt DROP 1.80m,active,,tick2420; Strong official NBB native PDF + Strong KBO; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Kortrijk>WZC De Ruyschaert>WZC,{EID},Zorg/RIZIV/dagprijs split behind omzet 8827505 (BTZ 4269117 + dagprijs 3492815; not commercial-only vs 73 1681843); why 76A JUMP 343692 (Marcade/GroenWest huurcorrectie 317692 + wagen 26000); why 9901 FLIP 231417 (was LOSS -492989) and pnl FLIP 241655 (was LOSS -479473); why destin 691 empty and 9905 241655 fully to overgedragen 14 143980; why 48 DROP 229324 (was 541225); FTE 121.2 DROP; 1 VE Kloosterstraat 25 Marke,Strong official PDF leftover public WZC of city_kortrijk; 8.83m omzet; public WZC not private clinic; not Kloosterstraat 6 Drongen; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Integrale Bejaardenzorg Sint-Jozef / WZC De Ruyschaert / Raad van Bestuur,boekhouding@de-ruyschaert.be,"Kloosterstraat 25, 8510 Marke",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2420; ready NOT sent; Strong official native NBB PDF; leftover city_kortrijk WZC after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
