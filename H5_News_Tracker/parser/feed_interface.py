"""
 vThe feed_interface module is responsible for pulling the RSS and ATOM feeds from a URL and building a list consisting
of headline and associated url pairs.
"""
import ssl
import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup


def parse(feed_url):
    """
    The parse function accepts a url of an RSS or ATOM feed and will return a BeautifulSoup object of the feeds
    """
    context = ssl.create_default_context()
    xml_url_to_parse = urlopen(feed_url, context=context)
    xml_page = xml_url_to_parse.read()
    xml_url_to_parse.close()
    return BeautifulSoup(xml_page, "xml")


def build_library(soup_page):
    """
    The build_library function accepts a BeautifulSoup object as an argument and will return a list of the headlines
    and associated links
    """
    library = ThreadSafeList()
    if not soup_page.find_all("item"):              # This statement will be true if the feed uses the ATOM format
        news_list = soup_page.find_all("entry")     # The "entry" field is what contains the titles and links for ATOM
        for item in news_list:
            lib_item = [item.title.text, item.link['href']]   # Atom is weird, this is how you pull the text for the url
            library.append(lib_item)
    else:
        news_list = soup_page.find_all("item")      # RSS feed case, "item" field contains the relevant information
        for item in news_list:
            lib_item = [item.title.text, item.link.text]
            library.append(lib_item)
    return library


# ThreadSafeList code taken from Dr Beaty
# Added the iterate and check_len functions
class ThreadSafeList():
    """
    This class creates a list and locks it so that only one thread can work on the list at a time
    """
    def __init__(self):
        self.list = []
        self.lock = threading.Lock()

    def append(self, element):
        self.lock.acquire()
        self.list.append(element)
        self.lock.release()

    def extend(self, elements):
        self.lock.acquire()
        self.list.extend(elements)
        self.lock.release()

    def rotate(self):
        self.lock.acquire()
        ret = self.list.pop()
        self.list.insert(0, ret)
        self.lock.release()
        return ret

    def clear(self):
        self.lock.acquire()
        self.list.clear()
        self.lock.release()

    def iterate(self, item):
        self.lock.acquire()
        temp = self.list.pop(item)
        self.lock.release()
        return temp

    def check_len(self):
        self.lock.acquire()
        length = len(self.list)
        self.lock.release()
        return length
