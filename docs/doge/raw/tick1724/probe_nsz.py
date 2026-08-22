import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# probe NSZ staatsbladmonitor for YE2025 deposit
for url in [
 "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410357609",
 "https://www.staatsbladmonitor.be/jaarrekening.html?ondernemingsnummer=0410357609",
]:
  try:
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
      html=resp.read().decode("utf-8","replace")
    print("URL", url, "len", len(html))
    deps=re.findall(r"20\d{2}-\d{8}", html)
    print("deps", sorted(set(deps))[-15:])
    pdfs=re.findall(r"cdn\.staatsbladmonitor[^\"']+\.pdf", html)
    print("pdfs", pdfs[:10])
    for m in re.finditer(r".{0,40}(2025|2026-\d+|neerlegging|bruto).{0,80}", html, re.I):
      s=re.sub(r"\s+"," ", m.group(0))
      if "2025" in s or "2026" in s:
        print("CTX", s[:180])
  except Exception as e:
    print("FAIL", url, e)

# also try northdata / consult for deposit id - probe likely recent deposits around Aug 2026
# companyweb says filed 12-08-2026 - deposit numbers around that date often 2026-00xxxxx
# Try to find via consult.cbso API?
for path in [
 "https://consult.cbso.nbb.be/consult-enterprise/0410357609",
]:
  try:
    req=urllib.request.Request(path, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
      print("NBB consult", resp.status, resp.getheader("Content-Type"), len(resp.read()))
  except Exception as e:
    print("NBB", type(e).__name__, getattr(e,"code",None))
