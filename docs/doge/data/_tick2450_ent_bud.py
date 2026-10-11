from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2450_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_tienen"
SRC_PDF="src_hartjes_jr2025_nbb_pdf_2450"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Groepsopvang De Hartjes VZW,ASBL Groepsopvang De Hartjes,Groepsopvang De Hartjes VZW (leftover city_tienen CIK),parastatal,city_tienen,nl,https://dehartjes.be,info@dehartjes.be,Oude Leuvensestraat 21 3300 Tienen,tick2450 YE2025 Strong official native NBB PDF deposit 2026-00180031 + Strong KBO 0441.374.348 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 DROP 251750 commercial-only; 73 JUMP 1342084; 76A empty DROP; opbr70/76A JUMP 1593834 envelope; bruto JUMP 1447874; pnl JUMP 154432; 9901 JUMP 147753; equity JUMP 511958; assets JUMP 695457; debt DROP 183499; FTE 20.6 FLAT; kapitaalsubsidies empty DROP; destin691 JUMP 154432 destin=pnl; 791 empty; cash JUMP 174846; geldbeleggingen FLAT 250000; leftover mined city_tienen after De Wissel Tienen-site same-KBO skip; 1 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT De Hartjes Ninove 0446.391.327; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hartjes_opbr_jr2025_statutory,{EID},2025,1593834,1593834,1593834,NBB VKT-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.21% (envelope because omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 1559358; omzet 251750 commercial-only; 73 1342084; 76A empty DROP",
f"bud_hartjes_omzet_jr2025_statutory,{EID},2025,251750,251750,251750,NBB VKT-VZW code 70 omzet YE2025 DROP -5.80% (commercial-only ouderbijdragen vs large 73; envelope is 70/76A),{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 267256",
f"bud_hartjes_73_jr2025_statutory,{EID},2025,1342084,1342084,1342084,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.14%,{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 1288700; FOI Opgroeien split behind 73 1342084",
f"bud_hartjes_pnl_jr2025_statutory,{EID},2025,154432,154432,154432,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +34.10% (was 115162),{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 115162; bedrijfswinst 9901 147753 JUMP; destin691 154432 JUMP destin=pnl",
f"bud_hartjes_bedrijfswinst_jr2025_statutory,{EID},2025,147753,147753,147753,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +37.51% (was 107446),{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 107446; 62 1277682 JUMP; 630 18499 DROP; 66A empty",
f"bud_hartjes_equity_jr2025_statutory,{EID},2025,511958,511958,511958,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +31.73%,{SRC_PDF},strong,tick2450; PDF p4 native; YE2024 identical 388648; kapitaalsubsidies empty DROP; overgedragen 14 16251 FLAT; fondsen 10 291275 FLAT; bestemde fondsen 13 204432 JUMP",
f"bud_hartjes_assets_jr2025_statutory,{EID},2025,695457,695457,695457,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +5.84%,{SRC_PDF},strong,tick2450; PDF p3 native; YE2024 identical 657053; MVA 22/27 98711 DROP; cash 174846 JUMP; geldbeleggingen 250000 FLAT; aanbouw 27 empty",
f"bud_hartjes_debt_jr2025_statutory,{EID},2025,183499,183499,183499,NBB VKT-VZW code 17/49 schulden YE2025 DROP -31.63%,{SRC_PDF},strong,tick2450; PDF p4 native; YE2024 identical 268405; 42/48 183499 DROP",
f"bud_hartjes_cash_jr2025_statutory,{EID},2025,174846,174846,174846,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +33.88%,{SRC_PDF},strong,tick2450; PDF p3 native; YE2024 identical 130603; geldbeleggingen 50/53 250000 FLAT",
f"bud_hartjes_destin_jr2025_statutory,{EID},2025,154432,154432,154432,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +208.86% (791 empty; destin=pnl; 13 JUMP 204432),{SRC_PDF},strong,tick2450; PDF p6 native; YE2024 destin 50000; overgedragen 14 16251 FLAT FOI",
f"bud_hartjes_62_jr2025_statutory,{EID},2025,1277682,1277682,1277682,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +0.66%,{SRC_PDF},strong,tick2450; PDF p5 native; YE2024 identical 1269250; FTE 20.6 FLAT",
])
print("entities+budgets ok")
