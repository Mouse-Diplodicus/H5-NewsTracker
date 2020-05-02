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

    entry_title = "[BLANK Entry Title]"
    entry_link = "[BLANK Entry Link]"

    root = tkinter.Tk()

    # main_menu = ttk.Menu(root)
    # menu_bar = ttk.Menu(root)
    # textColor = tkinter.StringVar()
    # textColor.set('white')
    # background = tkinter.StringVar()
    # background.set('black')

    var = tkinter.StringVar(root)
    # var.set('Select')
    # choices = ['Background Options', 'Black', 'White', 'Blue', 'Pink']

    label_ticker = ttk.Label(root)
    root.title("New JRRS")

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        self.entry_link = self.entry_link
        self.entry_title = self.entry_title
        print("constructing gui")

        super().__init__(master)
        self.master = master
        self.label_ticker.configure(width=8, background='#ffffff', foreground='#000000')
        # self.set_style()
        self.build()
        self.menu_bar()
        print("Gui constructed")


    def menu_bar(self):
        """ View.main_view.MainView.menu_bar adds a drop down menu for our tk window. """
        self.menubar = ttk.Menu(self)

        self.dropdown_menu = ttk.Menu(self.menubar, tearoff=0)
        self.dropdown_menu.add_command(label='white', command=self.bg_white)
        self.dropdown_menu.add_command(label='red', command=self.bg_red)
        self.dropdown_menu.add_command(label='blue', command=self.bg_blue)
        self.dropdown_menu.add_command(label='green', command=self.bg_green)
        self.menubar.add_cascade(label='bg color', menu=self.dropdown_menu)
        self.master.config(menu=self.menubar)

        self.font_menu = ttk.Menu(self.menubar)
        self.font_menu.add_command(label='8', command=self.font_8)
        self.font_menu.add_command(label='9', command=self.font_9)
        self.font_menu.add_command(label='10', command=self.font_10)
        self.font_menu.add_command(label='11', command=self.font_11)
        self.font_menu.add_command(label='12', command=self.font_12)
        self.font_menu.add_command(label='13', command=self.font_13)

        self.menubar.add_cascade(label='Font size', menu=self.font_menu)

        self.font_color = ttk.Menu(self.menubar)
        self.font_color.add_command(label='red', command=self.font_red)
        self.font_color.add_command(label='blue', command=self.font_blue)
        self.font_color.add_command(label='yellow', command=self.font_yellow)
        self.menubar.add_cascade(label='Font color', menu=self.font_color)

    def font_red(self):
        """ View.main_view.MainView.font_red sets font color to red. """
        self.content_label['fg'] = 'red'

    def font_yellow(self):
        """ View.main_view.MainView.font_yellow sets font color to yellow. """
        self.content_label['fg'] = 'yellow'

    def font_blue(self):
        """ View.main_view.MainView.font_blue sets font color to blue. """
        self.content_label['fg'] = 'blue'

    def font_8(self):
        """ View.main_view.MainView.font_8 sets font size to 8. """
        self.content_label['font'] = 'times 8'

    def font_9(self):
        """ View.main_view.MainView.font_9 sets font size to 9. """
        self.content_label['font'] = 'times 9'

    def font_10(self):
        """ View.main_view.MainView.font_10 sets font size to 10. """
        self.content_label['font'] = 'times 10'

    def font_11(self):
        """ View.main_view.MainView.font_11 sets font size to 11. """
        self.content_label['font'] = 'times 11'

    def font_12(self):
        """ View.main_view.MainView.font_12 sets font size to 12. """
        self.content_label['font'] = 'times 12'

    def font_13(self):
        """ View.main_view.MainView.font_13 sets font size to 13. """
        self.content_label['font'] = 'times 13'

    def bg_white(self):
        """ View.main_view.MainView.bg_white sets background color to white. """
        self.content_label['bg'] = 'white'

    def bg_red(self):
        """ View.main_view.MainView.bg_red sets background color to red. """
        self.content_label['bg'] = 'red'

    def bg_blue(self):
        """ View.main_view.MainView.bg_blue sets background color to blue. """
        self.content_label['bg'] = 'blue'

    def bg_green(self):
        """ View.main_view.MainView.bg_green sets background color to green. """
        self.content_label['bg'] = 'green'

    def start(self):
        """Start gui main update loop"""
        print("starting main loop")
        self.root.mainloop()

    def set_style(self):
        """Sets styling for various Tkinter objects"""
        print("setting styling")
        style = ttk.Style()
        style.configure("default.TLabel", foreground="#000000", background="#ffffff")
        style.configure("WB.TLabel", foreground="#ffffff", background="#000000")
        style.configure("BR.TLabel", foreground="#000000", background="#931113")
        # self.label_ticker.configure(style="WB.TLabel")


    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        # self.menu.grid(row=10, column=0)
        self.label_ticker.grid(row=0, column=0)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.winfo_toplevel().title("Tiny Ticker")
        self.label_ticker["text"] = self.entry_title
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
        self.pack()

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

    def open_article(self, link):

        """ View.main_view.MainView.open_article opens the web page associated with the current entry_title
        Arguments:
            link: url for the current entry_title
        """

        webbrowser.open_new(link)
        self.content_label.update()