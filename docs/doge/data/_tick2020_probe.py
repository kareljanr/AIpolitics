# ephemeral probe tick2020
import pathlib
import re

p = pathlib.Path("docs/doge/data/raw/tick2020/sint_vincentius_avelgem_en.html")
t = p.read_text(encoding="utf-8")
idx = t.find("Financial data")
print("idx", idx)
if idx < 0:
    idx = t.find("Profit/Loss")
print("idx2", idx)
snip = t[idx : idx + 12000] if idx >= 0 else t[:12000]
pathlib.Path("docs/doge/data/raw/tick2020/avelgem_fin_snip.txt").write_text(snip, encoding="utf-8")
# find numbers that look like euros
nums = re.findall(r"[\d]{1,3}(?:[.,\u00a0 ]\d{3})+(?:[.,]\d+)?|\d+\.\d+", snip)
print("nums sample", nums[:40])
# look for JSON embedded
for key in ["turnover", "profit", "equity", "gross", "employees", "omzet"]:
    ms = re.findall(key + r".{0,80}", t, re.I)
    print(key, len(ms), (ms[0][:100] if ms else None))

# NL page
p2 = pathlib.Path("docs/doge/data/raw/tick2020/sint_vincentius_avelgem.html")
t2 = p2.read_text(encoding="utf-8")
idx2 = t2.find("Financi")
print("NL idx", idx2)
snip2 = t2[idx2 : idx2 + 12000] if idx2 >= 0 else ""
pathlib.Path("docs/doge/data/raw/tick2020/avelgem_nl_snip.txt").write_text(snip2, encoding="utf-8")
print("NL snip head:", snip2[:500].replace("\n", " "))
