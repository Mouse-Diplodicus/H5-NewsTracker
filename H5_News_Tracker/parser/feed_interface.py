"""
The feed_interface module is responsible for pulling the RSS and ATOM feeds from a URL and building a list consisting
of headline and associated url pairs.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup


def parse(feed_url):
    """
    The parse function accepts a url of an RSS or ATOM feed and will return a list consisting of headline and
    associated url pairs.
    """
    xml_url_to_parse = urlopen(feed_url)
    xml_page = xml_url_to_parse.read()
    xml_url_to_parse.close()
    return build_library(BeautifulSoup(xml_page, "xml"))


def build_library(soup_page):
    """
    The build_library function accepts a BeautifulSoup object as an argument and will return a list of the headlines
    and associated links
    """
    library = []
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


if __name__ == '__main__':
    print(parse('https://news.google.com/news/atom'))
    print(parse('https://news.google.com/news/rss'))
