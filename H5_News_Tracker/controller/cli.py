"""
Command Line Interface for H5 NewsTracker
"""
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description="H5 command line interface")
    parser.add_argument('--url', dest='url', action='store', default="",
                        help="enter a RSS url", nargs='*')
    parser.add_argument('--file', action='store', dest='file', default="",
                        help="please enter a file name", nargs='*')
    parser.add_argument('--config', action='store', dest='config', default="",
                        help="enter .yaml file to configure", nargs='*')

        #args = parser.parse_args(args)
    return parser.parse_args(args)
