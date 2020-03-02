import tkinter as tk
import webbrowser


def callback(url):
    webbrowser.open_new(url)


root = tk.Tk()
link1 = tk.Label(root, text="Reddit Hyperlink", fg="black", cursor="hand2")

link1.bind("<Button-1>", lambda e: callback('http://www.reddit.com/'))
link1.pack()

root.mainloop()