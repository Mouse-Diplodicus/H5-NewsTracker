"""
A Program that displays news feeds in a ticker window
"""
import ssl
import threading
import time
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui import ticker_window

# Constants
CYCLE_TIME = 7  # in seconds


def build_rss_ticker(urls, **kw):
    """Uses ticker_window to show the news feeds provided by the url argument"""
    library = []
    for url in urls:
        library += feed_interface.parse(url)
    ticker = ticker_window.TickerWindow()
    news_cycle_thread = threading.Thread(target=cycle, args=[ticker, library], name="News-Cycling-Thread", daemon=True)
    print("Starting Threads:")
    news_cycle_thread.start()
    ticker.start()
    print("when do we get here?")


def cycle(ticker, library):
    """Cycles through the various headlines"""
    print("starting cycling of headlines")
    while True:
        for item in library:
            ticker.update(item[0], item[1])
            time.sleep(CYCLE_TIME)


if __name__ == '__main__':
    print("Program starting")
    urls = ['https://news.google.com/news/rss', 'https://news.google.com/news/atom']
    build_rss_ticker(urls)
