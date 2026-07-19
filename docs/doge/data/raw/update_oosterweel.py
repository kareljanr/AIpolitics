from pathlib import Path

p = Path(__file__).resolve().parents[1] / "commitments.csv"
raw = p.read_bytes()
for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
    try:
        text = raw.decode(enc)
        break
    except UnicodeDecodeError:
        continue
else:
    raise SystemExit("decode fail")
lines = text.splitlines()
out = []
found = False
for L in lines:
    if L.startswith("cmt_oosterweel_2026,"):
        found = True
        out.append(
            "cmt_oosterweel_2026,Oosterweel BO2026 annual correction line,vlaanderen_gov,Lantis / Oosterweel,"
            "BO2026 balance-target correction,2025-09-22,2026,2026,889859000,"
            '"{""2026"":889859000}",,active,,Antwerp ring annual budget correction,Part of multi-year project,'
            "src_vl_centenboekje_bo2026,strong,Vlaanderen>MOW>Oosterweel,"
            "Table 2-1 Oosterweel BO2026 889859 kEUR only"
        )
        out.append(
            "cmt_oosterweel_total,Oosterweel full project cost envelope,vlaanderen_gov,Lantis / Oosterweel,"
            "Flemish Oosterweel programme,2018-01-01,2018,2030,7200000000,"
            '"{""2026"":889859000}",,active,,Complete Antwerp ring Oosterweel link,CBA transparency no scope creep,'
            "src_oosterweel_7_2bn,strong,Vlaanderen>MOW>Oosterweel,"
            "Total about EUR 7.2bn VRT 2024; not sum of single budget year"
        )
    elif L.startswith("cmt_oosterweel_total,"):
        continue  # avoid dup if re-run
    else:
        out.append(L)
if not found:
    out.append(
        "cmt_oosterweel_total,Oosterweel full project cost envelope,vlaanderen_gov,Lantis / Oosterweel,"
        "Flemish Oosterweel programme,2018-01-01,2018,2030,7200000000,"
        '"{""2026"":889859000}",,active,,Complete Antwerp ring Oosterweel link,CBA transparency no scope creep,'
        "src_oosterweel_7_2bn,strong,Vlaanderen>MOW>Oosterweel,"
        "Total about EUR 7.2bn VRT 2024; not sum of single budget year"
    )
p.write_text("\n".join(out) + "\n", encoding="utf-8")
print("updated commitments encoding", enc, "found", found)

