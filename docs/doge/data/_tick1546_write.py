#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1546 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzwl"
SRC = "src_hvzwl_jr2025_bbc"
PDF = "https://www.zuidwestlimburg.be/content/documents/01-jaarverslag-2025-hvzzwl.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},HVZ Zuid-West-Limburg official activiteitenrapport 2025,{PDF},HVZ Zuid-West Limburg,2026-08-20,budget,tick1546; official activiteitenrapport / jaarverslag 2025; PDF 45p / 7678268 bytes; pdfinfo created 09.07.2026 13:22:44 UTC Microsoft Word 365; stale PDF title metadata jaarverslag 2022; financien section 6; euros PDF only; zoneraad 16.03.2026 named Goedkeuring rekening 2025 but full rekening unpublished",
        "src_hvzwl_kbo_0500919876,KBO Hulpverleningszone Zuidwest Limburg 0500.919.876,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500919876,FPS Economy KBO,2026-08-20,official_register,tick1546; leftover IGS hulpverleningszone of mined Hasselt + leftover of remaining ZWL gemeenten; zetel Zwarte-Brugstraat 1 3500 Hasselt; KBO 0500.919.876 Actief; naam HULPVERLENINGSZONE ZUIDWEST LIMBURG; prefix hvzwl unused; official register resolved (prior stalled run KBO conflict)",
        "src_hvzwl_site,HVZ Zuid-West-Limburg official site (activiteitenrapport 2025 published),https://www.zuidwestlimburg.be/hulpverleningszone-zwl/jaarverslagen,HVZ Zuid-West Limburg,2026-08-20,official_web,tick1546; leftover IGS of mined Hasselt; official JV2025 live on zuidwestlimburg.be; full rekening 2025 unpublished (zoneraad 16.03.2026 named approval only)",
        "src_hvzwl_foi_contact,HVZ Zuid-West-Limburg FOI channel (brandweer@zuidwestlimburg.be),https://www.zuidwestlimburg.be/,HVZ Zuid-West Limburg,2026-08-20,official_web,tick1546; leftover IGS of mined Hasselt; FOI ready not sent; Zwarte-Brugstraat 1 3500 Hasselt; official e-mail brandweer@zuidwestlimburg.be; NOT leftover HVZ Noord-Limburg 1545 / leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzwl," in raw or raw.startswith(b"igs_hvzwl,"):
        raise SystemExit("igs_hvzwl already present")
    if b"0500.919.876" in raw or b"0500919876" in raw:
        raise SystemExit("HVZ Zuid-West-Limburg KBO already present as entity")
    row = (
        "igs_hvzwl,Hulpverleningszone Zuid-West Limburg / HVZ ZWL / HVZZWL (leftover IGS hulpverleningszone of mined Hasselt + leftover of Alken/Beringen/Diepenbeek/Gingelom/Halen/Heers/Herk-de-Stad/Herstappe/Heusden-Zolder/Lummen/Nieuwerkerken/Sint-Truiden/Tessenderlo-Ham/Tongeren-Borgloon/Wellen/Zonhoven; NOT leftover HVZ Noord-Limburg 1545 / leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Brandweerzone Rand / leftover HVZ Vlaams-Brabant West / leftover HVZ Fluvia),"
        "Zone de secours Zuid-West-Limburg (IGS residuel / zone de secours),"
        "HVZ Zuid-West-Limburg leftover fire-rescue IGS of mined Hasselt + remaining ZWL municipalities (not leftover HVZ Noord-Limburg / leftover HVZ Oost-Limburg / leftover CAW Limburg / leftover CGG Integra / leftover CGG Kohesi / leftover Wonen in Limburg),"
        "other,city_hasselt,nl,https://www.zuidwestlimburg.be/,brandweer@zuidwestlimburg.be,Zwarte-Brugstraat 1 3500 Hasselt,"
        "tick1546 leftover residual IGS hulpverleningszone of mined Hasselt after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JV2025 taken; KBO 0500.919.876 Actief official kbo-bce.fgov.be; zetel Hasselt 3500; live official activiteitenrapport 2025 45p 7678268 created 09.07.2026; sourced euros uitgaven_gewone 29117176 pers 20930221 werking 5782142 overdrachten 676531 schuld 1728282 gemeente 20908513 volksgezondheid 4478255 prestaties 2291333 invest 4393168 ontvangsten 35360400; FOI ready not sent; parent city_hasselt; prefix hvzwl; NOT leftover HVZ Noord-Limburg 1545 / leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzwl")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
