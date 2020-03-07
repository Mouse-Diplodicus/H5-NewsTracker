"""
Reused code from StackOverFlow
https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
"""


import tkinter as ttk
import webbrowser


def go_to(url):
    """Sends the url link to your default browser"""
    webbrowser.open_new(url)


ROOT = ttk.Tk()
LINK = ttk.Label(ROOT, text="Reddit Hyperlink", fg="black", cursor="hand2")

LINK.bind("<Button-1>", lambda e: go_to('http://www.reddit.com/'))
LINK.pack()

ROOT.mainloop()
