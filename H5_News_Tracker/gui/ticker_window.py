"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import tkinter as tk
import webbrowser
import time
from tkinter import font
from tkinter import ttk
# from tkinter.ttk import OptionMenu
# from H5_News_Tracker.gui import color_test
# from H5_News_Tracker.gui.color_test import root, Menu, main_menu


class TickerWindow(tkinter.Frame):
    """
    Class creates tkinter window. It builds, displays, & modifies
    receiving input from the controller.
    """

    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "black"]
    font_sizes = ['6', '8', '10', '12', '14', '16', '18', '20', '24', '26', '28', '36', '48']
    max_label_width = 80
    font_size = 12
    updating_feed = []

    def __init__(self, master=None, logger=None, config=None):
        """Initializes the display window for the news  ticker"""
        self.logger = logger
        self.logger.info("constructing gui")
        super().__init__(master)
        master.title('H5-NewsTracker')
        self.master = master
        self.winfo_toplevel().title("H5-NewsTracker")
        self.style = ttk.Style()
        self.style.configure("default.TLabel", foreground="#000000", background="#ffffff")
        self.label_ticker = ttk.Label(master)
        self.label_ticker.configure(padding=[0, -1, 0, -1], style="default.TLabel")
        self.build_menu_bar()
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=config['font_size'])
        self.label_ticker.pack()
        self.pack()
        self.logger.info("Gui constructed")

    def build_menu_bar(self):
        """ View.main_view.MainView.menu_bar adds a drop down menu for our tk window. """
        menubar = tk.Menu(self)
        background_menu = tk.Menu(menubar, tearoff=0)
        font_color_menu = tk.Menu(menubar)
        font_size_menu = ttk.Menu(menubar)

        for color in self.colors:
            background_menu.add_command(label=color, command=lambda c=color: self.change_background_color(c))
            font_color_menu.add_command(label=color, command=lambda c=color: self.change_text_color(c))

        for size in self.font_sizes:
            font_size_menu.add_command(label=size)
        menubar.add_cascade(label='Background color', menu=background_menu)
        menubar.add_cascade(label='Font color', menu=font_color_menu)
        menubar.add_cascade(label='Font size', menu=font_size_menu)

        self.master.config(menu=menubar)

    def change_text_color(self, color):
        """
        H5_News_tracker.gui.ticker_window.TickerWindow.change_text_color
        This method changes the color of the styling for the background color of the label_ticker

        Arguments:
            color -- the new text color for the ticker label
        """
        self.style.configure("default.TLabel", foreground=color)

    def change_background_color(self, color):
        """
        H5_News_tracker.gui.ticker_window.TickerWindow.change_background_color
        This method changes the color of the styling for the background color of the label_ticker

        Arguments:
            color -- the new background color for the ticker label
        """
        self.style.configure("default.TLabel", background=color)

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

    def update_headline(self, headline, url):
        """Function updates the headline and associated url being displayed"""
        output = self.size_headline(headline)
        self.label_ticker.configure(text=output)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
        self.label_ticker.update()

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
