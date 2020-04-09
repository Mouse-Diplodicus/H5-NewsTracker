"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
import time
from tkinter import ttk
from tkinter import font


class TickerWindow:
    """Main Object for creating and running the news ticker gui"""

    max_label_width = 80
    font_size = 12

    def __init__(self):
        """Initializes the display window for the news  ticker"""
        print("constructing gui")
        self.root = tkinter.Tk()
        self.label_ticker = ttk.Label(self.root)
        self.button_exit = ttk.Button(self.root)
        self.root.overrideredirect(1)
        self.label_ticker.configure(padding=[0, -1, 0, -1])
        self.button_exit.configure(text="X", padding=[2, -1, 2, -1], command=self.root.quit)
        self.set_style()
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=self.font_size)
        self.build()
        print("Gui constructed")

    def start(self):
        """Start gui main update loop """
        print("starting main loop")
        self.root.mainloop()

    def start(self, timer):
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
