"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
import time
from tkinter import font
from tkinter import ttk


class TickerWindow(tkinter.Frame):
    """Main Object for creating and running the news ticker gui"""

    max_label_width = 80
    font_size = 12
    updating_feed = []

    def __init__(self, master=None, logger=None, config=None):
        """Initializes the display window for the news  ticker"""
        self.logger = logger
        self.logger.info("constructing gui")
        super().__init__(master)
        self.master = master
        self.label_ticker = ttk.Label(master)
        self.label_ticker.configure(padding=[0, -1, 0, -1])
        self.set_style()
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=self.font_size)
        self.build()
        self.logger.info("Gui constructed")

    def start(self):
        """Start gui main update loop """
        self.logger.info("starting main loop")
        self.master.mainloop()

    def set_style(self):
        """Sets styling for various Tkinter objects"""
        self.logger.info("setting styling")
        style = ttk.Style()
        style.configure("default.TLabel", foreground="#000000", background="#ffffff")
        style.configure("WB.TLabel", foreground="#ffffff", background="#000000", relief="GROOVE")
        style.configure("Exit.TLabel", foreground="#000000", background="#931113", relief="RAISED")
        self.label_ticker.configure(style="WB.TLabel")

    def build(self):
        """Sets organization for label and exit button"""
        self.logger.info("organizing gui layout")
        self.label_ticker.grid(row=0, column=0)

    def update_headline(self, headline, url):
        """Function updates the headline and associated url being displayed"""
        output = self.size_headline(headline)
        self.label_ticker.configure(text=output)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))

    def size_headline(self, headline):
        """Function takes a string representing a headline and if it is longer than the maximum width allowed it will
            shorten the string and append an ellipse"""
        if headline is None:
            return ""
        max_pixel_width = font.Font.measure(self.default_font, "n")*self.max_label_width
        if max_pixel_width < font.Font.measure(self.default_font, headline):
            index = self.max_label_width
            max_pixel_width -= font.Font.measure(self.default_font, "...")
            while max_pixel_width > font.Font.measure(self.default_font, headline[:index]):
                index += 1
            output = headline[:index-1]+"..."
        else:
            output = headline
        return output

    def close(self, delay=0):
        time.sleep(delay)
        self.master.quit
