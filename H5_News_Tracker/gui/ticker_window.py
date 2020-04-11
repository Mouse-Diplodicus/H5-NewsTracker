"""
Program displays a window with text using Tkinter when run.
"""
import time
import tkinter
import webbrowser
from tkinter import font
from tkinter import ttk


class TickerWindow(tkinter.Frame):
    """Main Object for creating and running the news ticker gui"""

    max_label_width = 80
    font_size = 12
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
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=self.font_size)
        self.build()
        print("Gui constructed")

    def start(self):
        """Start gui main update loop """
        print("starting main loop")
        self.master.mainloop()

    def start_with_timer(self, timer):
        """Start gui main update loop with timer"""
        print("starting main loop")
        self.root.mainloop()
        time.sleep(timer)
        self.root.quit()

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
        output = self.size_headline(headline)
        print("updating ticker to headline: ", output, "   url: ", url)
        self.label_ticker.configure(text=output)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))

    def size_headline(self, headline):
        """Function takes a string representing a headline and if it is longer than the maximum width allowed it will
            shorten the string and append an ellipse"""
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
