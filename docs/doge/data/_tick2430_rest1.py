#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2430_stamp.txt").read_text().strip().splitlines()
EID = "vzw_beregoed"
SRC_PDF = "src_beregoed_jr2025_nbb_pdf_2430"
COMM = "comm_beregoed_jr2025_statutory_omzet_2_98m_73_empty_pnl_jump_177k"
LB = "lb_beregoed_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_jr2025"
GAP = "gap_beregoed_opgroeien_matrix_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_l5"
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
    '"{""2025_omzet"":2979885,""2025_73"":0,""2025_76A"":10934,'
    '""2025_bruto"":2661706,'
    '""2025_pnl"":176840,""2025_bedrijfswinst"":162907,'
    '""2025_equity"":1801386,""2025_assets"":2457953,""2025_debt"":456567,'
    '""2025_fte"":40,""2025_kapitaalsubsidies"":377347,""2025_destin691"":176840,'
    '""2025_cash"":158322,""2025_geldbeleggingen"":1000000,'
    '""2025_personnel62"":2401863,""2025_gebouwen22"":875162,'
    '""2025_aanbouw27"":0,""2025_capex"":54412,'
    '""2025_fondsen10"":0,""2025_overgedragen14"":102412,'
    '""2025_bestemdefondsen13"":1321627,'
    '""2025_66A"":1529,""2025_66B"":0,""2025_voorzieningen16"":200000,'
    '""2025_76B"":0,""2025_630"":93177,'
    '""2024_omzet"":2854091,""2024_73"":0,'
    '""2024_bruto"":2607558,""2024_pnl"":83515,""2024_bedrijfswinst"":76283,'
    '""2024_equity"":1652761,""2024_assets"":2324383,'
    '""2024_debt"":471622,""2024_cash"":245324,""2024_fte"":39,'
    '""2024_destin691"":83515,""2024_kapitaalsubsidies"":405562,'
    '""2024_geldbeleggingen"":750000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Beregoed vzw YE2025 (omzet JUMP 2.98m / 73 empty / pnl JUMP 177k / destin 177k / Strong PDF),{EID},Opgroeien + leftover city_gent CIK,VZW KINDERDAGVERBLIJF BEREGOED (KBO 0447.515.042; Actief; 3 VE Michel Thieryhof 10 9000 Gent + De Bereboom + t Berenest Aalter; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap),2026-06-30,2025,2025,2979885,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00295160.pdf,Public CIK dual of mined city_gent,Publish Opgroeien/ouderbijdragen matrix behind omzet 2.98m + why 73 empty vs 87 Gent plaatsen + 2 Aalter VEs + why 9904 JUMP 177k + destin 177k + FTE 40,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>Beregoed>JR2025_statutory_L5,tick2430; Strong official native PDF; leftover mined city_gent after Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; De Bereboom / t Berenest same KBO not separate city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Beregoed omzet JUMP 2.98m / 73 empty / pnl JUMP 177k / destin 177k (YE2025 leftover city_gent CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>Beregoed>JR2025,2979885,2979885,PDF omzet 70 JUMP 2979885 envelope (73 empty VKT; 76A 10934); bruto 2661706; bedrijfswinst JUMP 162907; pnl JUMP 176840; equity JUMP 1801386; assets JUMP 2457953; debt DROP 456567; FTE 40; kapitaalsubsidies DROP 377347; destin691 176840; cash DROP 158322; geldbeleggingen JUMP 1000000; gebouwen DROP 875162; aanbouw empty; 3 VE Gent 87 plaatsen + Aalter,strong,{SRC_PDF},Opgroeien + leftover city_gent,Opgroeien CIK + leftover city_gent,2.98m omzet; 73 empty; 9901 163k JUMP; pnl JUMP 177k; destin 177k; leftover city_gent,5.20,3.50,5.10,4.24,FOI Opgroeien/ouderbijdragen matrix behind omzet 2.98m + why 73 empty vs 87 Gent plaatsen + 2 Aalter VEs + why 9904 JUMP 177k + destin 177k + FTE 40,active,,tick2430; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Gent>Beregoed>CIK,{EID},Opgroeien/ouderbijdragen split behind omzet 2979885 (omzet 70 present + 73 empty VKT); why 73 empty while site lists 87 plaatsen Gent + 2 Aalter VEs; why 9904 JUMP 176840 (was 83515) and 9901 JUMP 162907 (was 76283); why destin 691 176840 to bestemde fondsen 13 1321627 while fondsen 10 empty and overgedragen 14 stays 102412; why cash DROP 158322 (was 245324) at geldbeleggingen JUMP 1000000 and gebouwen DROP 875162 and capex 54412 and kapitaalsubsidies DROP 377347; FTE 40 JUMP (was 39); 3 VE Gent+Aalter,Strong official PDF leftover public CIK of mined city_gent; 2.98m omzet; public Opgroeien CIK not private clinic; De Bereboom / t Berenest same KBO not separate city_aalter leftover; not Kloosterstraat 6 Drongen; not Windekind 0431.806.386; not Elfenbankje 0417.638.151; not Vormingscentrum 0413.342.338; not Helan 0464.151.037; not Duinhuisjes 0413.323.037; not t Bremhuisje 0445.265.533 stopgezet 1993; not Kinderlach 0450.275.186; not KISME 0894.549.440; not Kindercentrum 0408.226.775; not KOS 0891.472.362; not WZC De Linde Wortegem-Petegem 0425.773.085; not OLV Gasthuis Poperinge 0445.066.385; not Huize Zonnelied 0415.082.497; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW KINDERDAGVERBLIJF BEREGOED / Raad van Bestuur,mireille.verwilst@azstlucas.be,"Michel Thieryhof 10, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2430; ready NOT sent; EVERY-10; Strong official native NBB PDF; leftover mined city_gent CIK after Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
