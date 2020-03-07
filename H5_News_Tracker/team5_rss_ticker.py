"""
high level support for doing this and that.
"""
import tkinter as tk
import webbrowser


def display_rss_ticker():
    """ Displays a window onscreen with a reddit link'"""
    root = tk.Tk()
    link1 = tk.Label(root, text="Reddit Hyperlink", fg="black", cursor="hand2")
    link1.bind("<Button-1>", lambda e: callback('http://www.reddit.com/'))
    link1.pack()

    root.mainloop()


def callback(url):
    """ Opens new tab displaying the url that is provided"""
    webbrowser.open_new(url)


if __name__ == "__main__":
    display_rss_ticker()
