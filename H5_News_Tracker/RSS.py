"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""

import feedparser
import webbrowser
import tkinter as ttk

feed = feedparser.parse('https://news.google.com/news/rss')
feedShow = {'entries': [{feed['entries'][0]['title']}]}


def goto() -> object:
    """Sends the url link to your default browser"""
    webbrowser.open_new()


class App(ttk.Frame):
    def __init__(self, master=None, **kw):
        """Sets index headline @ 0 to increment and creates the GUI frame"""
        ttk.Frame.__init__(self, master=master, **kw)
        self.txtHeadline = ttk.StringVar()
        self.headline = ttk.Label(self, textvariable=self.txtHeadline)
        self.headline.bind(self, "<Button-1>", lambda e: goto())
        self.headline.grid()
        self.headlineIndex = 0
        self.updateHeadline()

    def updateHeadline(self):
        """Grabs headline from RSS feed and uses the title as well as incrementing index"""
        try:
            headline = feed['entries'][self.headlineIndex]['title']
        except IndexError:
            """This will happen if we go beyond the end of the list of entries"""
            self.headlineIndex = 0
            headline = feed['entries'][self.headlineIndex]['title']

        self.txtHeadline.set(headline)
        self.headlineIndex += 1
        self.after(5000, self.updateHeadline)


if __name__ == '__main__':
    root = ttk.Tk()
    App(root).pack()
    root.mainloop()
