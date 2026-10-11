#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2408_stamp.txt").read_text().strip().splitlines()
EID = "vzw_eekhoorntje"
SRC_PDF = "src_eekhoorntje_jr2025_nbb_pdf_2408"
COMM = "comm_eekhoorntje_jr2025_statutory_bruto_2_14m_omzet_433k_73_empty_pnl_drop_destin_271k"
LB = "lb_eekhoorntje_bruto_2_14m_omzet_433k_73_empty_pnl_drop_271k_destin_271k_jr2025"
GAP = "gap_eekhoorntje_opgroeien_matrix_bruto_2_14m_omzet_433k_73_empty_pnl_drop_271k_destin_271k_l5"
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
    '"{""2025_omzet"":433265,""2025_bruto9900"":2138490,""2025_73"":0,'
    '""2025_pnl"":271456,""2025_bedrijfswinst"":246424,'
    '""2025_equity"":2983796,""2025_assets"":3242913,""2025_debt"":259117,'
    '""2025_fte"":30.4,""2025_kapitaalsubsidies"":66913,""2025_destin691"":271456,'
    '""2025_cash"":770104,""2025_geldbeleggingen"":500000,'
    '""2025_personnel62"":1857057,""2025_gebouwen22"":1707909,'
    '""2025_aanbouw27"":4931,""2025_capex"":485850,""2025_bestemde13"":1704554,'
    '""2025_overgedragen14"":172243,""2025_76A"":53372,""2025_630"":100435,'
    '""2025_fondsen10"":1040087,""2025_8189"":434176,""2025_voorzieningen16"":0,'
    '""2025_6061"":336524,""2025_6408"":58506,'
    '""2024_omzet"":418884,""2024_bruto9900"":2017762,""2024_pnl"":301691,'
    '""2024_bedrijfswinst"":278262,""2024_equity"":2457392,""2024_assets"":2817485,'
    '""2024_debt"":235093,""2024_kapitaalsubsidies"":94551,""2024_cash"":222947,'
    '""2024_fte"":28.6,""2024_destin691"":301691,""2024_gebouwen22"":1205084,'
    '""2024_geldbeleggingen"":1150000,""2024_6408"":4967}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang t Eekhoorntje vzw YE2025 (bruto JUMP 2.14m / omzet 433k / 73 empty / pnl DROP 271k / destin 271k / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_leuven,VZW Kinderopvang t Eekhoorntje (KBO 0414.453.680; Actief; 2 VE; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; slorpte Het Kinderhofje 0459.530.471 since 01.01.2025),2026-05-29,2025,2025,2138490,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00131193.pdf,Public CIK dual of mined city_leuven,Publish Opgroeien T1/T2/stad/ouder matrix behind bruto 2.14m + why 73 empty while omzet 433k + pnl DROP 271k + destin 271k 100pct + fusie Kinderhofje + cash JUMP 770k vs beleggingen DROP 500k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Leuven>Eekhoorntje>JR2025_statutory_L5,tick2408; Strong official native PDF; leftover city_leuven after 3Wplus@2407; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},t Eekhoorntje bruto JUMP 2.14m / omzet 433k / 73 empty / pnl DROP 271k / destin 271k (YE2025 Leuven CIK),L5,cik_vzw_statutory,Vlaanderen>Vlaams-Brabant>Leuven>Eekhoorntje>JR2025,2138490,2138490,PDF bruto9900 JUMP 2138490 CIK envelope; omzet70 433265 JUMP; 73 empty; 76A 53372; bedrijfswinst DROP 246424; pnl DROP 271456; equity JUMP 2983796; assets JUMP 3242913; debt JUMP 259117; FTE JUMP 30.4; kapitaalsubsidies DROP 66913; destin691 DROP 271456; cash JUMP 770104; geldbeleggingen DROP 500000; gebouwen JUMP 1707909; aanbouw 4931; capex 485850; personeel 62 1857057; fusie Kinderhofje 01.01.2025; 2 VE,strong,{SRC_PDF},Opgroeien + CIK leftover city_leuven,Opgroeien Kind en Gezin + leftover city_leuven,2.14m bruto JUMP; omzet 433k; 73 empty; pnl DROP 271k; destin 271k; leftover city_leuven,5.32,5.35,5.14,5.27,FOI Opgroeien T1/T2/stad/ouder matrix behind bruto 2.14m + why 73 empty while omzet 433k + pnl DROP 271k + destin 271k 100pct + fusie Kinderhofje + cash JUMP 770k,active,,tick2408; Strong official NBB native PDF + Strong KBO; leftover city_leuven after 3Wplus@2407; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams-Brabant>Leuven>Eekhoorntje>CIK,{EID},Opgroeien T1/T2/stad/ouder split behind bruto 2138490 and why 73 empty while omzet 70 is 433265; why pnl DROP 271456 (was 301691) and 9901 DROP 246424; why destin 691 271456 is 100pct of 9905; why fusie Kinderhofje 0459.530.471 01.01.2025 added 282587 permanente financiering + 8189 434176; why cash JUMP 770104 vs geldbeleggingen DROP 500000; 2 VE + FTE 30.4,Strong official PDF leftover public CIK of city_leuven; 2.14m bruto; public vergunde kinderopvang not private clinic; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang t Eekhoorntje / Raad van Bestuur,info@eekhoorntje.be,"Guldensporenlaan 65, 3010 Leuven",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2408; ready NOT sent; Strong official native NBB PDF; leftover city_leuven CIK after 3Wplus@2407; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
