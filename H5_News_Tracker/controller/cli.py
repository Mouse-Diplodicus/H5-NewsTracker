"""
Command Line Interface for H5 NewsTracker
"""
import argparse
import os


#def parse_args():
parser = argparse.ArgumentParser(description="H5-NewsTracker command line interface")
parser.add_argument('-u', '--url', dest='url', action='store', default="",
                        help="enter a RSS or Atom feed url", nargs='*')
parser.add_argument('-f', '--feed_file', action='store', dest='input_file', default="",
                        help="enter a file name", nargs='*')
parser.add_argument('-c', '--config', action='store', dest='config', default="",
                        help="enter .yaml file to configure", nargs='*')

args = parser.parse_args()
    #return args

def file_check(file):
    if not os.path.exists(file):
        raise argparse.ArgumentTypeError('The file entered is not present')

    return file

if args.input_file:
    file_check(file)