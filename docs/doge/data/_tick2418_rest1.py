#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2418_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kos"
SRC_PDF = "src_kos_jr2025_nbb_pdf_2418"
COMM = "comm_kos_jr2025_statutory_omzet_1_86m_73_empty_pnl_jump_68k"
LB = "lb_kos_omzet_1_86m_73_empty_pnl_jump_68k_destin_0_jr2025"
GAP = "gap_kos_opgroeien_matrix_omzet_1_86m_73_empty_pnl_jump_68k_destin_0_l5"
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
    '"{""2025_omzet"":1857493,""2025_bruto9900"":1704362,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":1857493,'
    '""2025_pnl"":67833,""2025_bedrijfswinst"":56600,'
    '""2025_equity"":1257420,""2025_assets"":1357837,""2025_debt"":100417,'
    '""2025_fte"":27.3,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":1102512,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":1628145,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":14374,'
    '""2025_fondsen10"":12377,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":1245043,""2025_66A"":0,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2024_omzet"":1802296,""2024_bruto9900"":1649474,""2024_73"":0,'
    '""2024_opbr"":1802296,""2024_pnl"":46260,""2024_bedrijfswinst"":29766,'
    '""2024_equity"":1189587,""2024_assets"":1319739,'
    '""2024_debt"":130152,""2024_cash"":1140020,""2024_fte"":26.2,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},KOS vzw YE2025 (omzet JUMP 1.86m / 73 empty / pnl JUMP 68k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_oostende,VZW Kinderopvang Scholengroep Stroom / KOS (KBO 0891.472.362; Actief; 5 VE Vogelzang + De Klimop + De Lettertuin + t Arnoldje + t groeiboompje; RSZ2025 88.911; Kind en Gezin CIK 5 KDV Oostende/Gistel/Koekelare/Oudenburg),2026-06-12,2025,2025,1857493,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00167075.pdf,Public CIK dual of mined city_oostende,Publish Opgroeien/stad/ouder matrix behind omzet 1.86m + why 73 empty + why 9901 JUMP 57k + pnl JUMP 68k + destin 0 + leveranciers JUMP 98k,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Oostende>KOS>JR2025_statutory_L5,tick2418; Strong official native PDF; leftover city_oostende after AG-O / IVOO / OVCO / Woonsprong; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},KOS omzet JUMP 1.86m / 73 empty / pnl JUMP 68k / destin 0 (YE2025 Oostende CIK),L5,cik_vzw_statutory,Vlaanderen>West-Vlaanderen>Oostende>KOS>JR2025,1857493,1857493,PDF omzet70 JUMP 1857493 CIK envelope; 73 empty; 76A empty; bruto9900 JUMP 1704362; bedrijfswinst JUMP 56600; pnl JUMP 67833; equity JUMP 1257420; assets JUMP 1357837; debt DROP 100417; FTE JUMP 27.3; kapitaalsubsidies empty; destin691 empty; cash DROP 1102512; geldbeleggingen empty; gebouwen empty; 5 VE Vogelzang + De Klimop + De Lettertuin + t Arnoldje + t groeiboompje,strong,{SRC_PDF},Opgroeien + CIK leftover city_oostende,Opgroeien Kind en Gezin + leftover city_oostende,1.86m omzet JUMP; 73 empty; 9901 JUMP 57k; pnl JUMP 68k; destin 0; leftover city_oostende,5.36,5.28,5.16,5.27,FOI Opgroeien/stad/ouder matrix behind omzet 1.86m + why 73 empty + why 9901 JUMP 57k + pnl JUMP 68k + destin 0 + leveranciers JUMP 98k,active,,tick2418; Strong official NBB native PDF + Strong KBO; leftover city_oostende after AG-O / IVOO / OVCO / Woonsprong; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Oostende>KOS>CIK,{EID},Opgroeien/stad/ouder split behind omzet 1857493 and why 73 empty on VKT; why 9901 JUMP 56600 (was 29766) and pnl JUMP 67833 (was 46260); why destin 691 empty and 9905 67833 fully to overgedragen 14 1245043; why cash DROP 1102512 and debt DROP 100417 via 42/48 leveranciers JUMP 97923 (was 1554) and overlopend passief DROP 2494 (was 128598); FTE 27.3 JUMP; 5 VE; Vogelzang + De Klimop + De Lettertuin + t Arnoldje + t groeiboompje,Strong official PDF leftover public CIK of city_oostende; 1.86m omzet; public CIK not private clinic; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Scholengroep Stroom / Raad van Bestuur,info@sterkescholen.be,"Leffingestraat 1, 8400 Oostende",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2418; ready NOT sent; Strong official native NBB PDF; leftover city_oostende CIK after AG-O / IVOO / OVCO / Woonsprong; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
