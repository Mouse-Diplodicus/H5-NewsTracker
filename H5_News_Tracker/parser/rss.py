import feedparser


def parse_feed(index):
    feed = feedparser.parse('https://news.google.com/news/rss')
    # feed_show = {'entries': [{feed['entries'][index]['title']}]}
    return feed['entries'][index]['title']