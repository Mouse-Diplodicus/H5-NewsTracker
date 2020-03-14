"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""
import threading
import feedparser
from H5_News_Tracker.gui import ticker_window


def main(**kw):
    """Uses ticker_window to show the google news feed"""
    print("importing and parsing rss feed")
    google_news = feedparser.parse('https://news.google.com/news/rss')
    # feed_show = {'entries': [{feed['entries'][0]['title']}]}
    news_ticker = ticker_window.TickerWindow()
    news_ticker.update(google_news.feed.title, google_news.feed.link)
    gui_update_thread = threading.Thread(target=news_ticker.start(), name="GUI-Main-Thread")
    gui_update_thread.start()
    print("when do we get here?")


if __name__ == '__main__':
    print("Program starting")
    main()
