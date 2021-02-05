import feedparser
import unidecode

rss = 'https://www.blog.pythonlibrary.org/feed/'
feed = feedparser.parse(rss)
for key in feed['entries']:
    print(unidecode.unidecode(key['title']))