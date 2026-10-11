#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1506 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T02:20:00Z"
ENT = "zorg_wvbl"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_crlf(DATA / "sources.csv", [
        "src_wvbl_kbo_1013719482,KBO Welzijnsvereniging Blankenberge 1013.719.482,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=1013719482,KBO,2026-08-20,official_register,tick1506; leftover zorg of mined Blankenberge; Vereniging van OCMW's Actief since 25.06.2024; zetel Frans Masereellaan 9 8370 Blankenberge; 2 VE; lasthebber Steven Verdoolaege; RSZ since 01.01.2026; BTW since 01.03.2026; NACE 87.101 RVT; no KBO financials",
        "src_wvbl_motena_start,Motena: Welzijnsvereniging Blankenberge officieel van start,https://www.motena.be/blog/welzijnsvereniging-blankenberge-officieel-van-start,Motena / Stad Blankenberge,2026-08-20,official_web,tick1506; leftover zorg of mined Blankenberge; oprichting 25.06.2024; Motena + Stad Blankenberge; zorgsite WZC 120 / dagverzorging 20-30 / kribbe / bistro; target ~2028; no JR2025 euros",
        "src_wvbl_tsv_24139864,Belgisch Staatsblad TSV oprichting Welzijnsvereniging Blankenberge 24139864,http://www.ejustice.just.fgov.be/tsv_pdf/2024/09/26/24139864.pdf,Belgisch Staatsblad / eJustice,2026-08-20,primary_pdf,tick1506; leftover zorg of mined Blankenberge; TSV 24139864 pub 26.09.2024; 213199 bytes / 8p image-only; no statutory JR2025 euros extracted",
        "src_wvbl_foi_contact,Welzijnsvereniging Blankenberge FOI channel (Stad + OCMW Blankenberge),https://www.blankenberge.be,Stad Blankenberge / Welzijnsvereniging Blankenberge,2026-08-20,official_web,tick1506; leftover zorg of mined Blankenberge; FOI ready not sent; info@blankenberge.be; Frans Masereellaan 9 8370 Blankenberge / J.F. Kennedyplein 1 8370 Blankenberge; NOT leftover AGB Blankenberge 1323 / leftover Zetus 1490 / leftover Motena / leftover Vitare 1505",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nzorg_wvbl," in raw or raw.startswith(b"zorg_wvbl,"):
        raise SystemExit("zorg_wvbl already present")
    if b"1013.719.482" in raw or b"1013719482" in raw:
        raise SystemExit("WV Blankenberge KBO already present as entity")
    row = (
        "zorg_wvbl,Welzijnsvereniging Blankenberge (leftover zorg / vereniging van OCMW's of mined Blankenberge; NOT leftover AGB Blankenberge 1323 / leftover Zetus 1490 prefix ztus / leftover Motena / leftover Vitare 1505 prefix vitr / leftover AGB Deinze / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Association de CPAS Welzijnsvereniging Blankenberge (soin residuel Blankenberge),"
        "Welzijnsvereniging Blankenberge leftover OCMW association / care EVA of mined Blankenberge (not leftover AGB Blankenberge / leftover Zetus / leftover Motena / leftover Vitare / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "ocmw_association,city_blankenberge,nl,https://www.motena.be/blog/welzijnsvereniging-blankenberge-officieel-van-start,info@blankenberge.be,Frans Masereellaan 9 8370 Blankenberge / J.F. Kennedyplein 1 8370 Blankenberge,"
        "tick1506 leftover residual zorg after leftover AGB/APB hunt; KBO 1013.719.482 Actief since 25.06.2024; no fetchable JR2025 BBC/NBB PDF; no sourced euros; parent city_blankenberge; prefix wvbl"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 zorg_wvbl")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
