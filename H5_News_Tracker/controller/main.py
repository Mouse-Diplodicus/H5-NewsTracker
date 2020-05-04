"""
A Program that displays news feeds in a ticker window
"""
import threading
import time
import tkinter
import logging
import yaml
import argparse
import os
import sys
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.gui.ticker_window import TickerWindow

logger = None
ARGS = None


def start():
    parse_args()
    logger_setup()
    if ARGS.verbose:
        levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
        level = levels[min(len(levels) - 1, ARGS.verbose)]  # capped to number of levels
        logger.setLevel(level)
        logger.info("set Logger level to " + str(level))

    config = load_config_file()
    ticker_config = config['ticker_window']
    if ARGS.font_type:
        ticker_config['font'] = ARGS.font_type
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
    logger.info('url_list set to:')
    logger.info(url_list)

    if ARGS.cycle_time:
        ct = ARGS.cycle_time
    else:
        ct = config['source']['cycle_time']

    Controller(url_list, logger=logger, cycle_time=ct, ticker_config=ticker_config)


def url_list_from_file(file_path):
    """ Accepts a path to a test file and will return an array of urls"""
    try:
        logger.info('attempting to load file from: ' + file_path)
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
        logger.error('failed to load file from: ' + file_path)
        return None


def load_config_file():
    try:
        with open('config.yml') as f:
            config = yaml.safe_load(f)
            return config
    except FileNotFoundError:
        mk_config_file()
        with open('config.yml') as f:
            data = yaml.safe_load(f)
            return config


def mk_config_file():
    config = dict(
        source=dict(
            cycle_time=6,
            path_to_file=None,
            default_url='https://news.google.com/news/rss',
        ),
        ticker_window=dict(
            font=None,
            font_size=12,
            text_color='white',
            background_color='black',
        )
    )
    with open('config.yml', 'w') as outfile:
        yaml.dump(config, outfile)


def logger_setup():
    global logger
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    return logger


def parse_args():
    parser = argparse.ArgumentParser(description="H5-NewsTracker")
    parser.add_argument('-l', '--file', action='store', dest='file_path', default="",
                        help="enter path to flat list test document of feed urls")
    parser.add_argument('-u', '--url', action='store', dest='feed_url', type=str, default="",
                        help="enter a RSS or Atom feed url", nargs='*')
    parser.add_argument('-t', '--time', action='store', dest='cycle_time', type=int, default=5,
                        help="enter desired cycle time in seconds e.g. -t 5", nargs='*')
    parser.add_argument('-f', '--font', action='store', dest='font_type', type=str, default="",
                        help="enter desired font e.g. -f", nargs='*')
    parser.add_argument('-s', '--size', action='store', dest='font_size', type=int, default=12,
                        help="enter desired font size e.g. -s 14", nargs='*')
    parser.add_argument('-c', '--color', action='store', dest='text_color', type=str, default="black",
                        help="enter desired text color e.g. -c black", nargs='*')
    parser.add_argument('-b', '--background', action='store', dest='background', type=str, default="white",
                        help="enter desired background color e.g. -b white", nargs='*')
    parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity (-v, -v -v, -vvv etc.)")
    global ARGS
    ARGS = parser.parse_args()


class Controller:
    """"""
    # Constants
    url_list = []  # list of urls to pull feeds from for new ticker

    def __init__(self, url_list, cycle_time=7, ticker_config=None, **kw):
        """Uses ticker_window to show the news feeds provided by the url argument"""
        logger.info("Starting News Ticker")
        self.cycle_time = cycle_time
        library = []
        for url in url_list:
            library += feed_interface.build_library(feed_interface.parse(url))
        root = tkinter.Tk()
        self.ticker = TickerWindow(master=root, logger=logger, config=ticker_config)
        news_cycle_thread = threading.Thread(target=self.cycle, args=[library],
                                             name="News-Cycling-Thread", daemon=True)
        logger.info("Starting Threads")
        news_cycle_thread.start()
        self.ticker.start()
        logger.info("Program Exit")

    def cycle(self, library):
        """Cycles through the various headlines"""
        logger.info("Starting cycling of headlines")
        run = True
        while run:
            for item in library:
                self.ticker.update_headline(item[0], item[1])
                time.sleep(self.cycle_time)
