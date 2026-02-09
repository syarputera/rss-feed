import requests
from bs4 import BeautifulSoup
from hashlib import md5

URL = "https://www.buletintv3.my/berita-terkini/"
BASE = "https://www.buletintv3.my"
LIMIT = 5

html = requests.get(URL, timeout=20).text
soup = BeautifulSoup(html, "html.parser")
items = soup.select("a.summary-title-link")[:LIMIT]

rss = []
rss.append('<?xml version="1.0" encoding="UTF-8"?>')
rss.append('<rss version="2.0"><channel>')
rss.append('<title>Buletin TV3</title>')
rss.append(f'<link>{BASE}</link>')
rss.append('<description>Buletin TV3 RSS</description>')

for a in items:
    title = a.get_text(strip=True)
    link = a.get("href")
    if not link.startswith("http"):
        link = BASE + link
    guid = md5(link.encode()).hexdigest()

    rss.append('<item>')
    rss.append(f'<title>{title}</title>')
    rss.append(f'<link>{link}</link>')
    rss.append(f'<description>{title}</description>')
    rss.append(f'<guid>{guid}</guid>')
    rss.append('</item>')

rss.append('</channel></rss>')
open("feeds/tv3.xml", "w", encoding="utf-8").write("\n".join(rss))
