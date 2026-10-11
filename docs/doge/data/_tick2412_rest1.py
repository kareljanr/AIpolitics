#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2412_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_turnhout"
SRC_PDF = "src_koturnhout_jr2025_nbb_pdf_2412"
COMM = "comm_koturnhout_jr2025_statutory_opbr_2_55m_73_2_23m_omzet_314k_pnl_flip_260"
LB = "lb_koturnhout_opbr_2_55m_73_2_23m_omzet_314k_pnl_flip_260_destin_0_jr2025"
GAP = "gap_koturnhout_opgroeien_matrix_opbr_2_55m_73_2_23m_omzet_314k_pnl_flip_260_destin_0_l5"
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
    '"{""2025_omzet"":314264,""2025_bruto9900"":2187383,""2025_73"":2232684,'
    '""2025_76A"":0,""2025_opbr"":2546948,'
    '""2025_pnl"":260,""2025_bedrijfswinst"":3559,'
    '""2025_equity"":134128,""2025_assets"":765516,""2025_debt"":631388,'
    '""2025_fte"":32,""2025_kapitaalsubsidies"":49295,""2025_destin691"":0,'
    '""2025_cash"":537544,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":2249341,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":6321,'
    '""2025_fondsen10"":0,""2025_bestemde13"":50000,'
    '""2025_overgedragen14"":34832,""2025_66A"":0,'
    '""2025_voorzieningen16"":0,""2025_6061"":359566,'
    '""2025_vooruitbetalingen46"":270000,'
    '""2024_omzet"":271753,""2024_bruto9900"":2043935,""2024_73"":2259836,'
    '""2024_opbr"":2538233,""2024_pnl"":-277088,""2024_bedrijfswinst"":-278901,'
    '""2024_equity"":153850,""2024_assets"":602327,'
    '""2024_debt"":338478,""2024_cash"":319132,""2024_fte"":34,'
    '""2024_destin691"":0,""2024_voorzieningen16"":110000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang Turnhout vzw YE2025 (opbr FLAT 2.55m / 73 2.23m / omzet 314k / pnl FLIP 260 / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK/BKO + leftover city_turnhout,VZW Kinderopvang Turnhout (KBO 0465.284.947; Actief; 5 VE; RSZ2025 88.911; EVA Stad Turnhout BKO 2.5-12 residual after Orion creche transfer 01.04.2024; Stad Turnhout 0207.533.082 bestuurder),2026-06-11,2025,2025,2546948,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00286204.pdf,Public CIK/BKO EVA dual of mined city_turnhout,Publish Opgroeien/stad/ouder/Orion matrix behind opbr 2.55m + why 70 commercial-only vs 73 2.23m + why pnl FLIP 260 via 110k provision release + destin 0 + debt JUMP 86pct via 270k vooruitbetalingen + residual after Orion 01.04.2024,{SRC_PDF},strong,Vlaanderen>Antwerpen>Turnhout>KinderopvangTurnhout>JR2025_statutory_L5,tick2412; Strong official native PDF; leftover city_turnhout after VERBINT@2401; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Kinderopvang Turnhout opbr FLAT 2.55m / 73 2.23m / omzet 314k / pnl FLIP 260 / destin 0 (YE2025 Turnhout CIK/BKO EVA),L5,cik_vzw_statutory,Vlaanderen>Antwerpen>Turnhout>KinderopvangTurnhout>JR2025,2546948,2546948,PDF bedrijfsopbrengsten 70+73+76A FLAT 2546948 VZW envelope; omzet70 JUMP 314264 commercial-only vs large 73 DROP 2232684; 76A empty; bruto9900 JUMP 2187383; bedrijfswinst FLIP 3559; pnl FLIP 260; equity DROP 134128; assets JUMP 765516; debt JUMP 631388; FTE DROP 32; kapitaalsubsidies DROP 49295; destin691 empty; cash JUMP 537544; geldbeleggingen empty; gebouwen empty; vooruitbetalingen 46 JUMP 270000; voorzieningen 16 released 110000; 5 VE EVA residual after Orion creche transfer 01.04.2024,strong,{SRC_PDF},Opgroeien + CIK/BKO leftover city_turnhout,Opgroeien Kind en Gezin + leftover city_turnhout,2.55m opbr FLAT; 73 2.23m; omzet 314k commercial-only; pnl FLIP 260; destin 0; leftover city_turnhout,5.38,5.28,5.16,5.27,FOI Opgroeien/stad/ouder/Orion matrix behind opbr 2.55m + why 70 commercial-only vs 73 2.23m + why pnl FLIP 260 via 110k provision release + destin 0 + debt JUMP 86pct via 270k vooruitbetalingen + residual after Orion 01.04.2024,active,,tick2412; Strong official NBB native PDF + Strong KBO; leftover city_turnhout after VERBINT@2401; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Antwerpen>Turnhout>KinderopvangTurnhout>CIK,{EID},Opgroeien/stad/ouder/Orion split behind bedrijfsopbrengsten 2546948 and why 70 314264 commercial-only vs 73 2232684; why pnl FLIP 260 (was -277088) and 9901 FLIP 3559 via voorzieningen 16 released 110000; why destin 691 empty and bestemde 13 50000 FLAT max city agreement; why debt JUMP 631388 via vooruitbetalingen 46 270000; residual after Orion creche transfer 01.04.2024; FTE 32 DROP; 5 VE; restated YE2024,Strong official PDF leftover public CIK/BKO EVA of city_turnhout; 2.55m opbr; public EVA BKO not private clinic; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Turnhout / Raad van Bestuur,kinderopvang@turnhout.be,"Druivenstraat 19, 2300 Turnhout",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2412; ready NOT sent; Strong official native NBB PDF; leftover city_turnhout CIK/BKO EVA after VERBINT@2401; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
