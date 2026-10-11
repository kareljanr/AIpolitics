#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1547 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzf"
SRC = "src_hvzf_jr2025_bbc"
PDF = "https://www.brandweerfluvia.be/media/597/download?attachment"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Brandweer Fluvia official activiteitenverslag 2025,{PDF},Brandweer Fluvia / HVZ Fluvia,2026-08-20,budget,tick1547; official activiteitenverslag 2025; PDF 23p / 16667787 bytes; pdfinfo created 02.04.2026 07:28:23 UTC Adobe InDesign 21.3; financien section 9 gewone + buitengewone; euros PDF only",
        "src_hvzf_kbo_0500929774,KBO Brandweer Fluvia 0500.929.774,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500929774,FPS Economy KBO,2026-08-20,official_register,tick1547; leftover IGS hulpverleningszone of mined Kortrijk + leftover of 13 remaining Fluvia gemeenten; zetel Doorniksesteenweg 214 bus A 8500 Kortrijk; KBO 0500.929.774 Actief; naam BRANDWEER FLUVIA sinds 01.01.2026; prefix hvzf unused; official register resolved",
        "src_hvzf_site,Brandweer Fluvia official site (activiteitenverslag 2025 published),https://www.brandweerfluvia.be/team,Brandweer Fluvia / HVZ Fluvia,2026-08-20,official_web,tick1547; leftover IGS of mined Kortrijk; official AV2025 linked from team page /media/597/download; full rekening 2025 / balans / expl / PnL unpublished",
        "src_hvzf_foi_contact,Brandweer Fluvia FOI channel (info@hvzfluvia.be),https://www.brandweerfluvia.be/,Brandweer Fluvia / HVZ Fluvia,2026-08-20,official_web,tick1547; leftover IGS of mined Kortrijk; FOI ready not sent; Doorniksesteenweg 214 bus A 8500 Kortrijk; official e-mail info@hvzfluvia.be (KBO) / info@brandweerfluvia.be (site); NOT leftover HVZ Westhoek 1544 / leftover HVZ1 1539 / leftover HVZ Midwest 1541 / leftover CAW ZWVL 1534 / leftover CGG Mandel en Leie 1522",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzf," in raw or raw.startswith(b"igs_hvzf,"):
        raise SystemExit("igs_hvzf already present")
    if b"0500.929.774" in raw or b"0500929774" in raw:
        raise SystemExit("HVZ Fluvia KBO already present as entity")
    row = (
        "igs_hvzf,Brandweer Fluvia / Hulpverleningszone Fluvia / HVZ Fluvia (leftover IGS hulpverleningszone of mined Kortrijk + leftover of Anzegem/Avelgem/Deerlijk/Harelbeke/Kuurne/Ledegem/Lendelede/Menen/Spiere-Helkijn/Waregem/Wevelgem/Wielsbeke/Zwevegem; NOT leftover HVZ Westhoek 1544 / leftover HVZ1 1539 / leftover HVZ Midwest 1541 / leftover CAW ZWVL 1534 / leftover CGG Mandel en Leie 1522 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover DVV Midwest / leftover AGB Kortrijk / leftover HVZ ZWL 1546 / leftover Brandweerzone Centrum / leftover Brandweerzone Rand / leftover HVZ Vlaams-Brabant West / leftover HVZ Zuid-Oost / leftover HVZ Rivierenland / leftover HVZ Waasland),"
        "Zone de secours Fluvia (IGS residuel / zone de secours),"
        "HVZ Fluvia leftover fire-rescue IGS of mined Kortrijk + remaining Fluvia municipalities (not leftover HVZ Westhoek / leftover HVZ1 / leftover HVZ Midwest / leftover CAW ZWVL / leftover CGG Mandel en Leie),"
        "other,city_kortrijk,nl,https://www.brandweerfluvia.be/,info@hvzfluvia.be,Doorniksesteenweg 214 bus A 8500 Kortrijk,"
        "tick1547 leftover residual IGS hulpverleningszone of mined Kortrijk after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official AV2025 taken; KBO 0500.929.774 Actief official kbo-bce.fgov.be; zetel Kortrijk 8500; live official activiteitenverslag 2025 23p 16667787 created 02.04.2026; sourced euros uitgaven_gewone 20237541 pers 15462341 werking 4652717 overdrachten 122484 ontvangsten 21496867 gemeente 11650000 fed_bw 4684000 fed_dgh 3091000 prestaties 1837568 invest 1598798 buitengewoon 3872440; FOI ready not sent; parent city_kortrijk; prefix hvzf; NOT leftover HVZ Westhoek 1544 / leftover HVZ1 1539 / leftover HVZ Midwest 1541 / leftover CAW ZWVL 1534 / leftover CGG Mandel en Leie 1522 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzf")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
