"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""
import tkinter as ttk
import webbrowser
import feedparser


FEED = feedparser.parse('https://news.google.com/news/rss')
FEED_SHOW = {'entries': [{FEED['entries'][0]['title']}]}


def goto() -> object:
    """Sends the url link to your default browser"""
    webbrowser.open_new()


class App(ttk.Frame):
    """Creates the GUI frame"""
    def __init__(self, master=None, **kw):
        """Sets index headline @ 0 to increment into the GUI"""
        ttk.Frame.__init__(self, master=master, **kw)
        self.txt_headline = ttk.StringVar()
        self.headline = ttk.Label(self, textvariable=self.txt_headline)
        self.headline.bind(self, "<Button-1>", lambda e: goto())
        self.headline.grid()
        self.headline_index = 0
        self.update_headline()

    def update_headline(self):
        """Grabs headline from RSS feed and uses the title as well as incrementing index"""
        try:
            headline = FEED['entries'][self.headline_index]['title']
        except IndexError:
            """This will happen if we go beyond the end of the list of entries"""
            self.headline_index = 0
            headline = FEED['entries'][self.headline_index]['title']

        self.txt_headline.set(headline)
        self.headline_index += 1
        self.after(5000, self.update_headline)


if __name__ == '__main__':
    root = ttk.Tk()
    App(root).pack()
    root.mainloop()
