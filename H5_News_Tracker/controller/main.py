"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
import logging
import yaml
import argparse
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.controller import cli

# Constants
CYCLE_TIME = 5  # in seconds
URL_LIST = []  # list of urls to pull feeds from for new ticker


def build_news_ticker(**kw):
    """Uses ticker_window to show the news feeds provided by the url argument"""
    logger_setup()
    logging.error("Starting News Ticker")
    library = []
    for url in URL_LIST:
        library += feed_interface.build_library(feed_interface.parse(url))
    root = tkinter.Tk()
    ticker = TickerWindow(master=root)
    news_cycle_thread = threading.Thread(target=cycle, args=[ticker, library], name="News-Cycling-Thread", daemon=True)
    logging.info("Starting Threads")
    news_cycle_thread.start()
    ticker.start()
    logging.info("Program Exit")


def cycle(ticker, library):
    """Cycles through the various headlines"""
    logging.info("Starting cycling of headlines")
    run = True
    while run:
        for item in library:
            ticker.update_headline(item[0], item[1])
            time.sleep(CYCLE_TIME)


def logger_setup():
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")


def parse_args(self):
    if args.feed_url:
        self.URL_LIST = args.feed_url[0]
    else:
        self.URL_LIST = []

    if args.feed_links:
        xml_file = args.feed_links
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for elem in root:
            for subelem in elem:
                print(subelem.text)

    if args.config:
        with open("/Users/thematrix/Desktop/H5-NewsTracker/.travis.yml") as f:
            data = yaml.safe_load(f)
            print(">>>>>>>>>>>>>>>>>")
            for item, doc in data.items():
                print(item, ":", doc)
                print(">>>>>>>>>>>>>>>>>")

        # args.config.close() #producing atterr because this is trying to close 'list' object not actual file
    if args.verbose:
        levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
        level = levels[min(len(levels) - 1, args.verbose)]  # capped to number of levels
        logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")
        logging.info("set Logger level to " + level)


parser = argparse.ArgumentParser(description="H5-NewsTracker")
parser.add_argument('-u', '--url', action='store', dest='feed_url', type=str, default="",
                    help="enter a RSS or Atom feed url", nargs='*')
parser.add_argument('-f', '--file', action='store', dest='feed_links', default="",
                    help="enter path to flat list test document of feed urls")
parser.add_argument('-c', '--config', action='store', dest='config', default="",
                    # type=argparse.FileType(mode='r'),
                    help="enter .yaml file to configure", nargs='*')
parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity (-v, -v -v, -vvv etc.)")
args = parser.parse_args()

if __name__ == '__main__':
    print("Program starting")
    URLS = ['https://news.google.com/news/rss', 'https://news.google.com/news/atom']
    cli.parse_args()
    build_news_ticker(URLS)

