import urllib.request, ssl, re, json
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
url="https://www.northdata.com/Neutraal%20Syndicaat%20voor%20Zelfstandigen%20VZW,%20Brussel/KBO%200410.357.609"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
# extract financial series for 2025
for key in ["Total assets","Equity","Earnings","Gross profit","Employees","Liabilities","Cash"]:
    pass
# find JSON blobs with year 2025 values
# simpler: print segments with value0 and year 2025
for m in re.finditer(r"\{[^{}]*\"year\"\s*:\s*\"2025\"[^{}]*\}", html):
    print(re.sub(r"\s+"," ", m.group(0))[:300])
print("==== LARGER CONTEXT ====")
# get surrounding metric names
for m in re.finditer(r"\"(name|title|label|id)\"\s*:\s*\"([^\"]+)\"[^]]{0,2000}?\"year\"\s*:\s*\"2025\"[^]]{0,400}?\"value0\"\s*:\s*([-\d.]+)", html):
    print(m.group(2), m.group(3))
# alternate: unescape and find chart data
text=html.replace("&quot;","\"")
# find metrics blocks
for m in re.finditer(r"\"name\"\s*:\s*\"([^\"]+)\"[\s\S]{0,800}?\"year\"\s*:\s*\"2025\"[\s\S]{0,200}?\"value0\"\s*:\s*([-\d.]+)", text):
    print("METRIC", m.group(1), m.group(2))
