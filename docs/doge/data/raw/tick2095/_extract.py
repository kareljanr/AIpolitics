# -*- coding: utf-8 -*-
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent

for name in ["begralim_nl.html", "begralim_en.html", "kbo_begralim.html"]:
    t = (RAW / name).read_text(encoding="utf-8")
    print("====", name)
    # all year blocks
    for m in re.finditer(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
        r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        t,
    ):
        print("Y", m.group(1), "pnl", m.group(2), "eq", m.group(3), "bruto", m.group(4), "omzet", m.group(5))
    # FTE history if present
    for pat in [
        r'amountOfEmployees\s*=\s*"([^"]+)"',
        r'personeel[^0-9]{0,40}([0-9]+[.,]?[0-9]*)',
        r'Workforce[^0-9]{0,40}([0-9]+[.,]?[0-9]*)',
        r'>(20\d\d)</[^>]+>\s*<[^>]+>[^<]*personeel',
        r'fte[\"\']?\s*[:=]\s*[\"\']?([0-9.,]+)',
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print("PAT", pat[:50], ms[:8])
    # trends JUMP/DROP near metrics
    trends = re.findall(r"(JUMP|DROP|FLIP|N/A)", t)
    print("trends", trends[:20], "n", len(trends))
    # emails / site
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", t)))
    print("emails", [e for e in emails if "companyweb" not in e.lower() and "sentry" not in e.lower()][:10])
    sites = re.findall(r'https?://(?:www\.)?(?!companyweb|google|facebook|linkedin)[a-z0-9.\-]+\.[a-z]{2,}[^\"\s<]*', t, re.I)
    print("sites", sites[:10])
    # address
    for m in re.finditer(r"Demerstraat[^<]{0,80}|3500 Hasselt", t):
        print("addr", re.sub(r"\s+", " ", m.group(0))[:100])
        break

# KBO deep
t = (RAW / "kbo_begralim.html").read_text(encoding="utf-8")
# strip tags for readability chunks
text = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
text = re.sub(r"\n+", "\n", text)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "e-mail",
            "webadres",
            "nace",
            "aanbested",
            "vestiging",
            "rsz",
            "actief",
            "rechtsvorm",
            "naam",
            "adres",
            "hasselt",
            "demer",
            "87.",
            "telefoon",
        ]
    ):
        window = " | ".join(lines[i : i + 4])
        print("KBO", window[:220])
