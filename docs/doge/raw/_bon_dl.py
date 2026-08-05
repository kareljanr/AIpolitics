import urllib.request
from pathlib import Path
url = "https://www.bonheiden.be/file/download/56531/77CE3BD1BD1F15F3E60466B39939452F"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
data = urllib.request.urlopen(req, timeout=120).read()
Path("docs/doge/raw/bonheiden_jr2025.pdf").write_bytes(data)
print("saved", len(data), data[:5])
url2 = "https://www.bonheiden.be/file/download/56532/26224C6E8C6A68B8DF9D6E172A3041C8"
data2 = urllib.request.urlopen(urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read()
Path("docs/doge/raw/bonheiden_jr2025_doc.pdf").write_bytes(data2)
print("doc", len(data2), data2[:5])
