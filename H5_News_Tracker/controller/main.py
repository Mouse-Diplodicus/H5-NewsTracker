"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
import logging
import sys
import argparse
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.controller import utilities

LOGGER = utilities.get_logger()
ARGS = None


def start():
    """ Function initializes values for the Controller and TickerWindow Objects"""
    parse_args()
    if ARGS.verbose:
        levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
        level = levels[min(len(levels) - 1, ARGS.verbose)]  # capped to number of levels
        LOGGER.setLevel(level)
        LOGGER.info("set Logger level to {0}".format(str(level)))

    config = utilities.load_config_file()
    ticker_config = config['ticker_window']
    if ARGS.font_size:
        ticker_config['font_size'] = ARGS.font_size
    if ARGS.text_color:
        ticker_config['text_color'] = ARGS.text_color
    if ARGS.background:
        ticker_config['background_color'] = ARGS.background

    url_list = None
    if ARGS.file_path:
        url_list = url_list_from_file(ARGS.file_path[0])
    if ARGS.feed_url and url_list is None:
        url_list = [ARGS.feed_url[0]]
    if config['source']['path_to_file'] and url_list is None:
        url_list = url_list_from_file(config['source']['path_to_file'])
    if config['source']['default_url'] and url_list is None:
        url_list = [config['source']['default_url']]
    LOGGER.info('url_list set to:')
    LOGGER.info(url_list)

    LOGGER.info('Building library')
    library = build_library(url_list)

    if ARGS.cycle_time:
        ct = ARGS.cycle_time
    else:
        ct = config['source']['cycle_time']

    control = Controller(library, cycle_time=ct, ticker_config=ticker_config)
    control.start_gui()


def url_list_from_file(file_path):
    """ Accepts a path to a test file and will return an array of urls"""
    try:
        LOGGER.info('attempting to load file from: {0}'.format(file_path))
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
    except FileNotFoundError:
        LOGGER.error('failed to load file from: {0}'.format(file_path))
        return None


def build_library(url_list):
    """ Returns a list of headline, url pairs generated from the url_list of feeds"""
    library = []
    for url in url_list:
        library += feed_interface.build_library(feed_interface.parse(url))
    return library


def parse_args():
    print(sys.argv)
    parser = argparse.ArgumentParser(description="H5-NewsTracker")
    parser.add_argument('-l', '--file', action='store', dest='file_path',
                        help="enter path to flat list test document of feed urls")
    parser.add_argument('-u', '--url', action='store', dest='feed_url', type=str,
                        help="enter a RSS or Atom feed url", nargs='*')
    parser.add_argument('-t', '--time', action='store', dest='cycle_time', type=int,
                        help="enter desired cycle time in seconds e.g. -t 5", nargs='*')
    parser.add_argument('-f', '--font', action='store', dest='font_type', type=str,
                        help="enter desired font e.g. -f", nargs='*')
    parser.add_argument('-s', '--size', action='store', dest='font_size', type=int,
                        help="enter desired font size e.g. -s 14", nargs='*')
    parser.add_argument('-c', '--color', action='store', dest='text_color', type=str,
                        help="enter desired text color e.g. -c black", nargs='*')
    parser.add_argument('-b', '--background', action='store', dest='background', type=str,
                        help="enter desired background color e.g. -b white", nargs='*')
    parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity (-v, -v -v, -vvv etc.)")
    global ARGS
    ARGS = parser.parse_args()


class Controller:
    """
    Class creates a Controller. It feeds and updates the display with new headlines and urls
    """
    # Constants

    def __init__(self, library, cycle_time=7, ticker_config=None):
        """Uses ticker_window to show the news feeds provided by the url argument"""
        LOGGER.info("Starting News Ticker")
        self.cycle_time = cycle_time
        root = tkinter.Tk()
        self.ticker = TickerWindow(master=root, config=ticker_config)
        news_cycle_thread = threading.Thread(target=self.cycle, args=[self.ticker, library],
                                             name="News-Cycling-Thread", daemon=True)
        LOGGER.info("Starting Threads")
        news_cycle_thread.start()
        LOGGER.info("Program Exit")

    def cycle(self, ticker, library, iterations=None):
        """Cycles through the various headlines"""
        LOGGER.info("Starting cycling of headlines")
        while iterations is None or iterations > 0:
            for item in library:
                ticker.update_headline(item[0], item[1])
                time.sleep(self.cycle_time)
            if iterations is not None:
                iterations = iterations-1

    def start_gui(self):
        """Method starts the gui interface"""
        self.ticker.start()
