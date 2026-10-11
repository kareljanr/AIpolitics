#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2421_stamp.txt").read_text().strip().splitlines()
EID = "vzw_quattro"
SRC_PDF = "src_quattro_jr2025_nbb_pdf_2421"
COMM = "comm_quattro_jr2025_statutory_omzet_247k_73_empty_pnl_loss_9k"
LB = "lb_quattro_omzet_247k_73_empty_bruto_239k_pnl_loss_9k_destin_0_jr2025"
GAP = "gap_quattro_zorg_matrix_omzet_247k_73_empty_bruto_239k_pnl_loss_9k_destin_0_l5"
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
    '"{""2025_omzet"":247410,""2025_73"":0,""2025_76A"":0,'
    '""2025_bruto9900"":239381,""2025_opbr"":247410,'
    '""2025_pnl"":-9071,""2025_bedrijfswinst"":-10194,'
    '""2025_equity"":81093,""2025_assets"":264015,""2025_debt"":182922,'
    '""2025_fte"":2.8,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":68360,""2025_geldbeleggingen"":100000,'
    '""2025_personnel62"":232282,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":3074,'
    '""2025_fondsen10"":150000,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":-68907,""2025_66A"":0,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2025_overlopend492"":137389,'
    '""2024_omzet"":120000,""2024_73"":0,'
    '""2024_bruto9900"":103853,""2024_pnl"":-66794,""2024_bedrijfswinst"":-67985,'
    '""2024_equity"":90164,""2024_assets"":173863,'
    '""2024_debt"":83699,""2024_cash"":129453,""2024_fte"":0,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Quattro vzw YE2025 (omzet JUMP 247k / 73 empty / bruto JUMP 239k / pnl LOSS 9k / destin 0 / Strong PDF),{EID},Departement Zorg + leftover city_kortrijk WZC-collab,VZW QUATTRO (KBO 0555.667.072; Actief; 1 VE Kloosterstraat 18 Marke; RSZ2025 88.109; samenwerkingsverband 8 WZC),2026-06-19,2025,2025,247410,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00188800.pdf,Public WZC-collab dual of mined city_kortrijk,Publish WZC-bijdrage matrix behind omzet 247k + why 73 empty + why 9901 LOSS 10k + pnl LOSS 9k + destin 0 + debt JUMP 183k + extra ICT,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>Quattro>JR2025_statutory_L5,tick2421; Strong official native PDF; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder / WZC De Ruyschaert; NOT Kloosterstraat 6 Drongen; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Quattro omzet JUMP 247k / 73 empty / bruto JUMP 239k / pnl LOSS 9k / destin 0 (YE2025 Kortrijk WZC-collab),L5,wzc_collab_vzw_statutory,Vlaanderen>West-Vlaanderen>Kortrijk>Quattro>JR2025,247410,247410,PDF omzet70 JUMP 247410 envelope 73 empty; bruto9900 JUMP 239381; 76A empty; bedrijfswinst LOSS IMPROVE -10194; pnl LOSS IMPROVE -9071; equity DROP 81093; assets JUMP 264015; debt JUMP 182922; FTE 2.8; kapitaalsubsidies empty; destin691 empty; cash DROP 68360; geldbeleggingen JUMP 100000; gebouwen empty; 1 VE Kloosterstraat 18 Marke,strong,{SRC_PDF},Departement Zorg + leftover city_kortrijk,Departement Zorg WZC-collab + leftover city_kortrijk,247k omzet; 73 empty; bruto 239k; 9901 LOSS 10k; pnl LOSS 9k; destin 0; leftover city_kortrijk,5.22,2.50,5.12,3.70,FOI WZC-bijdrage matrix behind omzet 247k + why 73 empty + why 9901 LOSS 10k + pnl LOSS 9k + destin 0 + debt JUMP 183k + extra ICT,active,,tick2421; Strong official NBB native PDF + Strong KBO; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder / WZC De Ruyschaert; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Kortrijk>Quattro>WZC-collab,{EID},WZC-bijdrage split behind omzet 247410 (73 empty so omzet is envelope; jaarverslag bijdragen huizen + toetreding De Linde 25k); why 73 empty at a WZC-samenwerkingsverband; why 9901 LOSS IMPROVE -10194 (was LOSS -67985) and pnl LOSS IMPROVE -9071 (was LOSS -66794); why destin 691 empty and 9905 -9071 fully to overgedragen 14 -68907; why 492/3 JUMP 137389 (was empty); why debt JUMP 182922 (was 83699); FTE 2.8; 1 VE Kloosterstraat 18 Marke; 8 aangesloten WZC,Strong official PDF leftover public WZC-collab of city_kortrijk; 247k omzet; public WZC-samenwerkingsverband not private clinic; not Kloosterstraat 6 Drongen; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW QUATTRO / Raad van Bestuur,boekhouding@de-ruyschaert.be,"Kloosterstraat 18, 8510 Marke",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2421; ready NOT sent; Strong official native NBB PDF; leftover city_kortrijk WZC-collab after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder / WZC De Ruyschaert; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
