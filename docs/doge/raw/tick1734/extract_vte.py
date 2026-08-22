import re
from pathlib import Path

t = Path("docs/doge/raw/tick1734/wzc_sintjozef_extract.txt").read_text(encoding="utf-8")
for pat in [
    r"9087.{0,200}",
    r"9096.{0,200}",
    r"1003.{0,120}",
    r"Gemiddeld.{0,200}",
    r"VTE.{0,120}",
    r"voltijds.{0,150}",
    r"SOCIA.{0,80}",
]:
    ms = re.findall(pat, t, re.I | re.S)
    print("====", pat)
    for m in ms[:8]:
        print(repr(m[:300]))

for i, block in enumerate(t.split("===== PAGE")):
    if re.search(
        r"9087|9096|Tewerkstelling|SOCIAAL|sociale balans|voltijds equivalent|Gemiddeld aantal",
        block,
        re.I,
    ):
        print("---PAGE", i, "len", len(block))
        print(block[:3000])
        print("====END====")
