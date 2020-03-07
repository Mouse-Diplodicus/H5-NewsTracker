"""
Reused code from StackOverFlow
https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
"""

import tkinter as tk
import webbrowser


def callback(url):
    """Sends the url link to your default browser"""
    webbrowser.open_new(url)


root = tk.Tk()
link1 = tk.Label(root, text="Reddit Hyperlink", fg="black", cursor="hand2")

link1.bind("<Button-1>", lambda e: callback('http://www.reddit.com/'))
link1.pack()

root.mainloop()