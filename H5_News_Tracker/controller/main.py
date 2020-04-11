"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow

# Constants
CYCLE_TIME = 2  # in seconds


def build_rss_ticker(urls, **kw):
    """Uses ticker_window to show the news feeds provided by the url argument"""
    library = []
    for url in urls:
        library += feed_interface.build_library(feed_interface.parse(url))
    root = tkinter.Tk()
    ticker = TickerWindow(master=root)
    news_cycle_thread = threading.Thread(target=cycle, args=[ticker, library], name="News-Cycling-Thread", daemon=True)
    print("Starting Threads:")
    news_cycle_thread.start()
    if __name__ != '__main__':
        ticker.start_with_timer(3)
    else:
        ticker.start()
    print("when do we get here?")


def cycle(ticker, library):
    """Cycles through the various headlines"""
    print("starting cycling of headlines")
    run = True
    while run:
        for item in library:
            ticker.update(item[0], item[1])
            time.sleep(CYCLE_TIME)
        if __name__ != '__main__':
            run = False


if __name__ == '__main__':
    print("Program starting")
    URLS = ['https://news.google.com/news/rss', 'https://news.google.com/news/atom']
    build_rss_ticker(URLS)
