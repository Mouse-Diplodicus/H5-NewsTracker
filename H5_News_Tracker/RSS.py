"""
Reused code on StackOverFlow
https://stackoverflow.com/questions/49362820/update-rss-feed-every-2-minutes
"""

import feedparser
import webbrowser
import tkinter as tk


def callback(event, link):
    webbrowser.open_new(article_link)


feed = feedparser.parse('http://www.reddit.com/r/python/.rss')
feedShow = {'entries': [{feed['entries'][0]['title']}]}

root = tk.Tk()
text = tk.Text(root)


for entry in feed.entries:
    headline = entry.title
    headlineIndex = 0
    try:
        headline = feed['entries'][headlineIndex]['title']
    except IndexError:
        """This will happen if we go beyond the end of the list of entries"""
        headlineIndex = 0
        headline = feed['entries'][headlineIndex]['title']
        headlineIndex += 1
    article_link = entry.link

    print("{}[{}]".format(headline, article_link))

    link = tk.Label(root, text="{}\n".format(headline), fg="blue", cursor="hand2")
    link.pack()

    link.bind("<Button-1>", lambda event, link=article_link: callback(event, link))

text.tag_config("here")
root.mainloop()
