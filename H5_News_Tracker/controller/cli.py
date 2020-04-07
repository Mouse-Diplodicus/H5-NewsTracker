""" Command Line Interface for H5 NewsTracker """
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="H5 command line interface")
    parser.add_argument('--url', action='store', dest='url',default="",
                        help="enter a RSS url", nargs='*')
    parser.add_argument('--file', action='store', dest='file', default="",
                        help="please enter a file name", nargs='*')
    parser.add_argument('--config', action='store', dest='config', default="",
                        help="enter .yaml file to configure", nargs='*')
    #print(parser.parse_args(['--url', '--file', '--config']))

    args = parser.parse_args()
    return args