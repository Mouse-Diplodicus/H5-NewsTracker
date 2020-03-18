"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""
import ssl
import threading
import time
import feedparser
from H5_News_Tracker.gui import ticker_window

# Constants
CYCLE_TIME = 2  # in seconds


def main():
    """Uses ticker_window to show the google news feed"""
    google_news = pull_feed('https://news.google.com/news/rss')
    library = build_library(google_news)
    ticker = ticker_window.TickerWindow()
    news_cycle_thread = threading.Thread(target=cycle, args=[ticker, library], name="News-Cycling-Thread", daemon=True)
    print("Starting Threads:")
    news_cycle_thread.start()
    ticker.start()
    print("when do we get here?")


def cycle(ticker, library):
    """Cycles through the various headlines"""
    print("starting cycling of headlines")
    count = len(library)
    # while True:
    for i in range(0, count):
        ticker.update(library[i][0], library[i][1])
        time.sleep(CYCLE_TIME)


def build_library(feed):
    """puts headlines and associated urls into a list"""
    print("building library...")
    library = []
    count = len(feed.entries)
    for i in range(0, count):
        item = feed.entries[i]
        lib_item = [item.title, item.link]
        library.append(lib_item)
    print(library)
    return library


def pull_feed(feed_url):
    """pulls news feed from a url, monkey patching certification as feedparser doesn't have another solution"""
    print("importing and parsing rss feed")
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