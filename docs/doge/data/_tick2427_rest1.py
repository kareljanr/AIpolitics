#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2427_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kisme"
SRC_PDF = "src_kisme_jr2025_nbb_pdf_2427"
COMM = "comm_kisme_jr2025_statutory_bruto_630k_omzet73_empty_pnl_drop_119k"
LB = "lb_kisme_bruto_630k_omzet73_empty_pnl_drop_119k_destin_0_jr2025"
GAP = "gap_kisme_opgroeien_matrix_bruto_630k_omzet73_empty_pnl_drop_119k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_73"":0,""2025_76A"":0,'
    '""2025_bruto"":630193,'
    '""2025_pnl"":119349,""2025_bedrijfswinst"":110897,'
    '""2025_equity"":1128223,""2025_assets"":1232071,""2025_debt"":103848,'
    '""2025_fte"":14.5,""2025_kapitaalsubsidies"":144415,""2025_destin691"":0,'
    '""2025_cash"":77248,""2025_geldbeleggingen"":469393,'
    '""2025_personnel62"":519248,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":643866,""2025_capex"":647901,'
    '""2025_fondsen10"":2000,""2025_overgedragen14"":981808,'
    '""2025_66A"":0,""2025_66B"":0,""2025_voorzieningen16"":0,'
    '""2025_76B"":0,""2025_630"":49,'
    '""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto"":632964,""2024_pnl"":174950,""2024_bedrijfswinst"":163691,'
    '""2024_equity"":864459,""2024_assets"":897686,'
    '""2024_debt"":33227,""2024_cash"":880356,""2024_fte"":9.1,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},KISME vzw YE2025 (bruto DROP 630k / omzet+73 empty / pnl DROP 119k / destin 0 / Strong PDF),{EID},Opgroeien + leftover city_eeklo CIK,VZW Kinderopvang Scholengroep Meetjesland / KISME (KBO 0894.549.440; Actief; 3 VE Beukenstraat 1 9900 Eeklo; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap),2026-05-11,2025,2025,630193,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00117266.pdf,Public CIK dual of mined city_eeklo,Publish Opgroeien/ouderbijdragen matrix behind bruto 630k + why 70+73 empty vs jaarverslag Opgroeien 622k + why 9904 DROP 119k + destin 0 + cash DROP 77k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Eeklo>KISME>JR2025_statutory_L5,tick2427; Strong official native PDF; leftover mined city_eeklo after Welzijnsband / Woonmaatschappij Meetjesland / HVZ Meetjesland / Ascendere; also leftover mined city_aalter; NOT Kloosterstraat 6 Drongen; NOT Kinderlach 0450.275.186; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT Kinderopvang Baloo BV 0762.684.274; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},KISME bruto DROP 630k / omzet+73 empty / pnl DROP 119k / destin 0 (YE2025 leftover city_eeklo CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Eeklo>KISME>JR2025,630193,630193,PDF bruto 9900 DROP 630193 envelope (omzet70 empty VKT; 73 empty VKT; 76A empty); bedrijfswinst DROP 110897; pnl DROP 119349; equity JUMP 1128223; assets JUMP 1232071; debt JUMP 103848; FTE 14.5; kapitaalsubsidies JUMP 144415; destin691 empty; cash DROP 77248; geldbeleggingen JUMP 469393; gebouwen empty; aanbouw JUMP 643866; 3 VE Eeklo+Aalter,strong,{SRC_PDF},Opgroeien + leftover city_eeklo,Opgroeien CIK + leftover city_eeklo,630k bruto; omzet+73 empty; 9901 111k DROP; pnl DROP 119k; destin 0; leftover city_eeklo,5.14,1.92,5.06,5.12,FOI Opgroeien/ouderbijdragen matrix behind bruto 630k + why 70+73 empty vs jaarverslag Opgroeien 622k + why 9904 DROP 119k + destin 0 + cash DROP 77k,active,,tick2427; Strong official NBB native PDF + Strong KBO; leftover mined city_eeklo after Welzijnsband / Woonmaatschappij Meetjesland / HVZ Meetjesland / Ascendere; also leftover mined city_aalter; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Eeklo>KISME>CIK,{EID},Opgroeien/ouderbijdragen split behind bruto 630193 (omzet 70 empty + 73 empty VKT); why 70+73 empty while jaarverslag lists Opgroeien werkingssubsidies 621747.92 + Maribel 27258.14; why 9904 DROP 119349 (was 174950) and 9901 DROP 110897 (was 163691); why destin 691 empty and overgedragen 14 981808; why cash DROP 77248 (was 880356) at geldbeleggingen JUMP 469393 and aanbouw JUMP 643866 and capex 647901; FTE 14.5; 3 VE Eeklo+Aalter,Strong official PDF leftover public CIK of mined city_eeklo; 630k bruto; public Opgroeien CIK not private clinic; not Kloosterstraat 6 Drongen; not Kinderlach 0450.275.186; not Kindercentrum 0408.226.775; not KOS 0891.472.362; not Kinderopvang Baloo BV 0762.684.274; not WZC De Linde Wortegem-Petegem 0425.773.085; not OLV Gasthuis Poperinge 0445.066.385; not Huize Zonnelied 0415.082.497; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Scholengroep Meetjesland / Raad van Bestuur,kinderopvang@go-dynamiek.be,"Beukenstraat 1, 9900 Eeklo",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2427; ready NOT sent; Strong official native NBB PDF; leftover mined city_eeklo CIK after Welzijnsband / Woonmaatschappij Meetjesland / HVZ Meetjesland / Ascendere; also leftover mined city_aalter; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
