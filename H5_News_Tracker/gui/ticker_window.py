"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
from tkinter import ttk
import time


class TickerWindow(tkinter.Frame):
    """Main Object for creating and running the news ticker gui"""

    updating_feed = []

    def __init__(self, master=None):
        """Initializes the display window for the news  ticker"""
        print("constructing gui")
        super().__init__(master)
        self.master = master
        self.label_ticker = ttk.Label(master)
        self.button_exit = ttk.Button(master)
        self.master.overrideredirect(1)
        self.label_ticker.configure(width=70, padding=[0, -1, 0, -1])
        self.button_exit.configure(text="X", padding=[2, -1, 2, -1], command=self.master.quit)
        self.set_style()
        self.build()
        print("Gui constructed")

    def start(self):
        """Start gui main update loop """
        print("starting main loop")
        # while time.sleep(2):
        self.master.mainloop()
        # self.root.destroy()

    def set_style(self):
        """Sets styling for various Tkinter objects"""
        print("setting styling")
        style = ttk.Style()
        style.configure("default.TLabel", foreground="#000000", background="#ffffff")
        style.configure("WB.TLabel", foreground="#ffffff", background="#000000", relief="GROOVE")
        style.configure("Exit.TLabel", foreground="#000000", background="#931113", relief="RAISED")
        self.label_ticker.configure(style="WB.TLabel")
        self.button_exit.configure(style="Exit.TLabel")

    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=1)

    def update(self, headline, url):
        """Function updates the headline and associated url being displayed"""
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
