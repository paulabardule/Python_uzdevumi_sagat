"""
Iegūt ziņas, izmantojot rss no google.lv.

"""
import feedparser # feedparser ir bibliotēka (instalet ar pip install feedparser)

# noradu rss plusmas url, kas satur google.lv zinas
rss_url="https://news.google.com/rss?hl=lv&gl=LV&ceid=LV:lv"
# lejupieladet un izanalizet rss plusmu
feed=feedparser.parse(rss_url)
# japarada zinu virsrakstus un saites
for entry in feed.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    print("\n")