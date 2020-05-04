import unittest
from bs4 import BeautifulSoup
from pathlib import Path
from H5_News_Tracker.parser import feed_interface


class TestFeedInterface(unittest.TestCase):

    def test_parser(self):
        soup = feed_interface.parse('https://news.google.com/news/rss')
        self.assertIsNotNone(soup)
        self.assertEqual('Top stories - Google News', soup.title.text)

    def test_build_library(self):
        try:
            with open("tests/sample_rss_feed.xml") as test_rss:
                soup = BeautifulSoup(test_rss, "xml")
        except FileNotFoundError:
            path = Path(__file__).resolve().parents[1]
            path = path / 'tests' / 'sample_rss_feed.xml'
            print(path)
            with open(path) as test_rss:
                soup = BeautifulSoup(test_rss, "xml")

        result = feed_interface.build_library(soup)
        self.assertEqual(result[0][0],
                         "Bernie Sanders Drops Out of 2020 Democratic Race for President - The New York Times")
        self.assertEqual(result[0][1],
                         "https://news.google.com/__i/rss/rd/articles/CBMiTGh0dHBzOi8vd3d3Lm55dGltZXMuY29tLzIwMjAvMDQvM"
                         "DgvdXMvcG9saXRpY3MvYmVybmllLXNhbmRlcnMtZHJvcHMtb3V0Lmh0bWzSAVBodHRwczovL3d3dy5ueXRpbWVzLmNvbS"
                         "8yMDIwLzA0LzA4L3VzL3BvbGl0aWNzL2Jlcm5pZS1zYW5kZXJzLWRyb3BzLW91dC5hbXAuaHRtbA?oc=5")
        self.assertEqual(result[1][0],
                         "New York Gov. Cuomo says state won't return to 'normal' as daily coronavirus deaths reach new"
                         " high - CNBC")
        self.assertEqual(result[1][1],
                         "https://news.google.com/__i/rss/rd/articles/CBMigwFodHRwczovL3d3dy5jbmJjLmNvbS8yMDIwLzA0LzA4L"
                         "25ldy15b3JrLWdvdi1jdW9tby1zYXlzLXN0YXRlLXdvbnQtcmV0dXJuLXRvLW5vcm1hbC1hcy1kYWlseS1jb3JvbmF2aX"
                         "J1cy1kZWF0aHMtcmVhY2gtbmV3LWhpZ2guaHRtbNIBhwFodHRwczovL3d3dy5jbmJjLmNvbS9hbXAvMjAyMC8wNC8wOC9"
                         "uZXcteW9yay1nb3YtY3VvbW8tc2F5cy1zdGF0ZS13b250LXJldHVybi10by1ub3JtYWwtYXMtZGFpbHktY29yb25hdmly"
                         "dXMtZGVhdGhzLXJlYWNoLW5ldy1oaWdoLmh0bWw?oc=5")

        try:
            with open("tests/sample_atom_feed.xml") as test_atom:
                soup = BeautifulSoup(test_atom, "xml")
        except FileNotFoundError:
            path = Path(__file__).resolve().parents[1]
            path = path / 'tests' / 'sample_atom_feed.xml'
            print(path)
            with open(path) as test_atom:
                soup = BeautifulSoup(test_atom, "xml")

        result = feed_interface.build_library(soup)
        self.assertEqual(result[0][0],
                         "Bernie Sanders Drops Out of 2020 Democratic Race for President - The New York Times")
        self.assertEqual(result[0][1],
                         "https://news.google.com/__i/rss/rd/articles/CBMiTGh0dHBzOi8vd3d3Lm55dGltZXMuY29tLzIwMjAvMDQvM"
                         "DgvdXMvcG9saXRpY3MvYmVybmllLXNhbmRlcnMtZHJvcHMtb3V0Lmh0bWzSAVBodHRwczovL3d3dy5ueXRpbWVzLmNvbS"
                         "8yMDIwLzA0LzA4L3VzL3BvbGl0aWNzL2Jlcm5pZS1zYW5kZXJzLWRyb3BzLW91dC5hbXAuaHRtbA?oc=5")
        self.assertEqual(result[1][0],
                         "New York Gov. Cuomo says state won't return to 'normal' as daily coronavirus deaths reach new"
                         " high - CNBC")
        self.assertEqual(result[1][1],
                         "https://news.google.com/__i/rss/rd/articles/CBMigwFodHRwczovL3d3dy5jbmJjLmNvbS8yMDIwLzA0LzA4L"
                         "25ldy15b3JrLWdvdi1jdW9tby1zYXlzLXN0YXRlLXdvbnQtcmV0dXJuLXRvLW5vcm1hbC1hcy1kYWlseS1jb3JvbmF2aX"
                         "J1cy1kZWF0aHMtcmVhY2gtbmV3LWhpZ2guaHRtbNIBhwFodHRwczovL3d3dy5jbmJjLmNvbS9hbXAvMjAyMC8wNC8wOC"
                         "9uZXcteW9yay1nb3YtY3VvbW8tc2F5cy1zdGF0ZS13b250LXJldHVybi10by1ub3JtYWwtYXMtZGFpbHktY29yb25hdm"
                         "lydXMtZGVhdGhzLXJlYWNoLW5ldy1oaWdoLmh0bWw?oc=5")


if __name__ == '__main__':
    unittest.main()
