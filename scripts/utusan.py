import feedparser

FEED = "https://www.utusan.com.my/feed/"
LIMIT = 5

feed = feedparser.parse(FEED)

rss = []
rss.append('<?xml version="1.0" encoding="UTF-8"?>')
rss.append('<rss version="2.0"><channel>')
rss.append('<title>Utusan Malaysia</title>')
rss.append('<link>https://www.utusan.com.my</link>')
rss.append('<description>Utusan Malaysia RSS</description>')

for e in feed.entries[:LIMIT]:
    title = e.title
    link = e.link
    guid = link

    rss.append('<item>')
    rss.append(f'<title>{title}</title>')
    rss.append(f'<link>{link}</link>')
    rss.append(f'<description>{title}</description>')
    rss.append(f'<guid>{guid}</guid>')
    rss.append('</item>')

rss.append('</channel></rss>')
open("feeds/utusan.xml", "w", encoding="utf-8").write("\n".join(rss))
