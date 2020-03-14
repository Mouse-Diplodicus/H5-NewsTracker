"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""
import ssl
import threading
import feedparser
from H5_News_Tracker.gui import ticker_window


def main(**kw):
    """Uses ticker_window to show the google news feed"""
    print("importing and parsing rss feed")
    google_news = pull_feed('https://news.google.com/news/rss')
    library = build_library(google_news)
    news_ticker = ticker_window.TickerWindow()
    news_ticker.update(library[0][0], library[0][1])
    gui_update_thread = threading.Thread(target=news_ticker.start(), name="GUI-Main-Thread")
    gui_update_thread.start()
    print("when do we get here?")


def cycle():
    """Cycles through the various headlines"""
    print("starting cycling of headlines")


def build_library(feed):
    """puts headlines and associated urls into a list"""
    library = []
    count = len(feed.entries)
    for i in range(0, count):
        item = feed.entries[i]
        lib_item = [item.title, item.link]
        library.append(lib_item)
    return library


def pull_feed(feed_url):
    """pulls news feed from a url"""
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    return feedparser.parse(feed_url)


if __name__ == '__main__':
    print("Program starting")
    main()
