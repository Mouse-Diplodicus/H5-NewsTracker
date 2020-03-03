"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""

import feedparser
import webbrowser
import tkinter as tk

feed = feedparser.parse('http://www.reddit.com/r/python/.rss')
feedShow = {'entries': [{feed['entries'][0]['title']}]}


def callback():
    """Sends the url link to your default browser"""
    webbrowser.open_new()


class App(tk.Frame):
    def __init__(self, master=None, **kw):
        """Sets index headline @ 0 to increment and creates the GUI frame"""
        tk.Frame.__init__(self, master=master, **kw)
        self.txtHeadline = tk.StringVar()
        self.headline = tk.Label(self, textvariable=self.txtHeadline)
        self.headline.grid()
        self.headlineIndex = 0
        self.updateHeadline()

    def updateHeadline(self):
        try:
            headline = feed['entries'][self.headlineIndex]['title']
        except IndexError:
            """This will happen if we go beyond the end of the list of entries"""
            self.headlineIndex = 0
            headline = feed['entries'][self.headlineIndex]['title']

        self.txtHeadline.set(headline)
        self.headlineIndex += 1
        self.after(10000, self.updateHeadline)


if __name__ == '__main__':
    root = tk.Tk()
    App(root).grid()
    root.mainloop()
