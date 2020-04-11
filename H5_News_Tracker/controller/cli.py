"""
Command Line Interface for H5 NewsTracker
"""
import argparse
import webbrowser
import logging
import sys


#def parse_args():
parser = argparse.ArgumentParser(description="H5-NewsTracker command line interface")
parser.add_argument('-u', '--url', dest='feed_url', action='store', type=str, default="",
                        help="enter a RSS or Atom feed url", nargs='*')
parser.add_argument('-f', '--feed_file', action='store', dest='feed_file', default="",
                        help="enter a feed file name", nargs='*')
parser.add_argument('-c', '--config', action='store', dest='config', default="",
                        help="enter .yaml file to configure", nargs='*')
parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity (-v, -v -v, -vvv etc.)")

args = parser.parse_args()
    #return args
"""
def file_check(file):
    if not os.path.exists(file):
        raise argparse.ArgumentTypeError('The file entered is not present')

    return input_file

if args.input_file:
    file_check(file)
"""
if args.feed_url:
    #url = args.feed_url
    webbrowser.get().open("https://www.google.com")

if args.feed_file:
    """
    do something
    """
if args.config:
    """
    do something
    """
if args.verbose:
    print("Running '{}'".format(__file__))
    #print("~ Verbose: {}".format(args.verbose))
    levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, args.verbose)]  # capped to number of levels
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")
    logging.debug("a debug message")
    logging.info("a info message")
    logging.warning("a warning message")
    logging.error("an error message")
    logging.critical("a critical message")