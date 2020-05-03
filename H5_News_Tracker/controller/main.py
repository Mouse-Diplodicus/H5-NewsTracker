"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
import logging
import yaml
import argparse
import sys
import os
sys.path.append(os.getcwd())        # Add current working directory to PythonPath in order to import other modules
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow


def url_list_from_file(file_path):
    """ Accepts a path to a test file and will return an array of urls"""
    file_object = open(file_path, "r")
    url_list = file_object.readlines()
    file_object.close()
    length = len(url_list)
    for i in range(length):
        url_list[i] = url_list[i].rstrip()
        url_list[i] = url_list[i].replace(',', '')
    logging.info("Pulled the following urls from file: ")
    logging.info(url_list)
    return url_list


def load_config_file(path):
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
            for item, doc in data.items():
                print(item, ":", doc)
                print(">>>>>>>>>>>>>>>>>")
    except FileNotFoundError:
        pass


def mk_config_file():
    pass


def update_config_file():
    pass


def logger_setup():
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")


class Controller:
    """"""
    # Constants
    cycle_time = 5  # in seconds
    url_list = []  # list of urls to pull feeds from for new ticker

    def __init__(self, **kw):
        """Uses ticker_window to show the news feeds provided by the url argument"""
        logger_setup()
        logging.info("Starting News Ticker")
        self.parse_args()
        library = []
        for url in self.url_list:
            library += feed_interface.build_library(feed_interface.parse(url))
        root = tkinter.Tk()
        self.ticker = TickerWindow(master=root)
        news_cycle_thread = threading.Thread(target=self.cycle, args=[library],
                                             name="News-Cycling-Thread", daemon=True)
        logging.info("Starting Threads")
        news_cycle_thread.start()
        self.ticker.start()
        logging.info("Program Exit")

    def cycle(self, library):
        """Cycles through the various headlines"""
        logging.info("Starting cycling of headlines")
        run = True
        while run:
            for item in library:
                self.ticker.update_headline(item[0], item[1])
                time.sleep(self.cycle_time)

    def parse_args(self):
        if ARGS.feed_url:
            self.url_list = ARGS.feed_url[0]
        else:
            self.url_list = ['https://news.google.com/news/rss']

        if ARGS.file_path:
            self.url_list = url_list_from_file(ARGS.file_path[0])

        if ARGS.config:
            settings = load_config_file(os.getcwd() + "config.yml")

            # args.config.close() #producing atterr because this is trying to close 'list' object not actual file
        if ARGS.verbose:
            levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
            level = levels[min(len(levels) - 1, args.verbose)]  # capped to number of levels
            logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")
            logging.info("set Logger level to " + level)


parser = argparse.ArgumentParser(description="H5-NewsTracker")
parser.add_argument('-u', '--url', action='store', dest='feed_url', type=str, default="",
                    help="enter a RSS or Atom feed url", nargs='*')
parser.add_argument('-f', '--file', action='store', dest='file_path', default="",
                    help="enter path to flat list test document of feed urls")
parser.add_argument('-c', '--config', action='store', dest='config', default="",
                    # type=argparse.FileType(mode='r'),
                    help="enter .yaml file to configure", nargs='*')
parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity (-v, -v -v, -vvv etc.)")
ARGS = parser.parse_args()

if __name__ == '__main__':
    Controller()
