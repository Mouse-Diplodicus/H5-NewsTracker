"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import tkinter as tk
import webbrowser
from tkinter import ttk
# from tkinter.ttk import OptionMenu
# from H5_News_Tracker.gui import color_test
# from H5_News_Tracker.gui.color_test import root, Menu, main_menu


class TickerWindow(tk.Frame):
    """
    Class creates tkinter window. It builds, displays, & modifies
    receiving input from the controller.
    """

    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "black"]
    font_sizes = ['6', '8', '10', '12', '14', '16', '18', '20', '24', '26', '28', '36', '48']

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        super().__init__(master)
        master.title('H5-NewsTracker')
        self.master = master

        self.style = ttk.Style()
        self.style.configure("default.TLabel", foreground="#000000", background="#ffffff")
        self.label_ticker = ttk.Label(master)
        self.label_ticker.configure(width=8, style="default.TLabel")
        self.label_ticker.configure(style="default.TLabel")
        self.build_menu_bar()
        self.label_ticker.pack()
        self.pack()
        print("Gui constructed")

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
        print("starting main loop")
        self.master.mainloop()

    def update(self, headline, url):
        """Function updates the headline and associated url being displayed"""
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.winfo_toplevel().title("H5-NewsTracker")
        self.label_ticker.configure(text=headline)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
        self.label_ticker.update()

    def display_entry(self, entry_title: str, entry_link: str):

        """ Viw.main_view.MainView.display_entry changes the displayed title and associated link.
        This function updates both entry_title and entry_link with the appropriate parameters and changes the text of
        content_label to that of the new entry_title.
        Arguments:
            entry_title: a string showing a headline
            entry_link: a string that is the url for entry_title
        """
        self.content_label["text"] = self.entry_title
        self.content_label.update()
