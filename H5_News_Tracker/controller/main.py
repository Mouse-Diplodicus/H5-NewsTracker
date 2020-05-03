"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow

# Constants
CYCLE_TIME = 5  # in seconds


def build_news_ticker(urls, **kw):
    """Uses ticker_window to show the news feeds provided by the url argument"""
    library = []
    for url in urls:
        library += feed_interface.build_library(feed_interface.parse(url))
    root = tkinter.Tk()
    ticker = TickerWindow(master=root)
    news_cycle_thread = threading.Thread(target=cycle, args=[ticker, library], name="News-Cycling-Thread", daemon=True)
    print("Starting Threads:")
    news_cycle_thread.start()
    ticker.start()
    print("when do we get here?")


def cycle(ticker, library):
    """Cycles through the various headlines"""
    print("starting cycling of headlines")
    run = True
    while run:
        for item in library:
            ticker.update_headline(item[0], item[1])
            time.sleep(CYCLE_TIME)


def url_list_from_file(file_path):
    """ Accepts a path to a test file and will return an array of urls"""
    file_object = open(file_path, "r")
    url_list = file_object.readlines()
    file_object.close()
    length = len(url_list)
    for i in range(length):
        url_list[i] = url_list[i].rstrip()
        url_list[i] = url_list[i].replace(',', '')
    print(url_list)
    return url_list


if __name__ == '__main__':
    print("Program starting")
    URLS = ['https://news.google.com/news/rss', 'https://news.google.com/news/atom']
    build_news_ticker(URLS)
