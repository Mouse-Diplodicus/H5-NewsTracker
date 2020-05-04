"""
Program displays a window with text using Tkinter when run.
"""
import tkinter as tk
import webbrowser
import time
from tkinter import font
from tkinter import ttk
from H5_News_Tracker.controller.utilities import get_logger

LOGGER = get_logger()


class TickerWindow(tk.Frame):
    """
    Class creates tkinter window. It builds, displays, & modifies
    receiving input from the controller.
    """

    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "black"]
    font_sizes = ['6', '8', '10', '12', '14', '16', '18', '20', '24', '26', '28', '36', '48']
    max_label_width = 80
    style_string = "default.TLabel"

    def __init__(self, master=None, config=None):
        """Initializes the display window for the news  ticker"""
        super().__init__(master)
        master.title('H5-NewsTracker')
        self.master = master
        self.winfo_toplevel().title("H5-NewsTracker")

        LOGGER.info("constructing gui")

        self.font = font.nametofont('TkDefaultFont')
        self.font.configure(size=config['font_size'])

        self.style = ttk.Style()
        self.style.configure(self.style_string, foreground=config['text_color'],
                             background=config['background_color'], font='TkDefaultFont')

        self.label_ticker = ttk.Label(master)
        self.label_ticker.configure(padding=['0', '-1', '0', '-1'], style=self.style_string)

        self.build_menu_bar()
        self.label_ticker.pack()
        LOGGER.info("Gui constructed")

    def build_menu_bar(self):
        """ H5_News_tracker.gui.ticker_window.TickerWindow.build_menu_bar adds the drop down menus for our tk window."""
        self.menubar = tk.Menu(self)
        background_menu = tk.Menu(self.menubar, tearoff=0)
        font_color_menu = tk.Menu(self.menubar, tearoff=0)
        font_size_menu = tk.Menu(self.menubar, tearoff=0)

        for color in self.colors:
            background_menu.add_command(label=color, command=lambda c=color: self.change_background_color(c))
            font_color_menu.add_command(label=color, command=lambda c=color: self.change_text_color(c))

        for size in self.font_sizes:
            font_size_menu.add_command(label=size, command=lambda s=size: self.change_font_size(s))
        self.menubar.add_cascade(label='Background color', menu=background_menu)
        self.menubar.add_cascade(label='Font color', menu=font_color_menu)
        self.menubar.add_cascade(label='Font size', menu=font_size_menu)

        self.master.config(menu=self.menubar)

    def change_background_color(self, color):
        """
        H5_News_tracker.gui.ticker_window.TickerWindow.change_background_color
        This method changes the color of the styling for the background color of the label_ticker

        Arguments:
            color -- the new background color for the ticker label
        """
        self.style.configure("self.style_string", background=color)

    def change_text_color(self, color):
        """
        H5_News_tracker.gui.ticker_window.TickerWindow.change_text_color
        This method changes the color of the styling for the background color of the label_ticker

        Arguments:
            color -- the new text color for the ticker label
        """
        self.style.configure("self.style_string", foreground=color)

    def change_font_size(self, size):
        """
        H5_News_tracker.gui.ticker_window.TickerWindow.change_text_color
        This method changes the color of the styling for the background color of the label_ticker

        Arguments:
            size -- the new font size for the text of the ticker label
        """
        self.font.configure(size=size)

    def start(self):
        """Start gui main update loop """
        LOGGER.info("starting main loop")
        self.master.mainloop()

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
        max_pixel_width = font.Font.measure(self.font, "n")*self.max_label_width
        if max_pixel_width < font.Font.measure(self.font, headline):
            index = self.max_label_width
            max_pixel_width -= font.Font.measure(self.font, "...")
            while max_pixel_width > font.Font.measure(self.font, headline[:index]):
                index += 1
            output = headline[:index-1]+"..."
        else:
            output = headline
        return output

    def close(self, delay):
        """Method will kill the ticker window instance currently running"""
        LOGGER.info('will close window in: ' + str(delay) + ' seconds')
        time.sleep(delay)
        LOGGER.info('closing program')
        self.master.quit()
