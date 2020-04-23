"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter.ttk import OptionMenu
from H5_News_Tracker.gui import color_test
from H5_News_Tracker.gui.color_test import root, Menu, main_menu


class TickerWindow:
    root = tkinter.Tk()

    main_menu = tk.Menu(root)
    menu_bar = tk.Menu(root)

    var = tkinter.StringVar(root)

    label_ticker = ttk.Label(root)
    root.title("New JRRS")

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        print("constructing gui")
        self.label_ticker.configure(width=8, background='#ffffff', foreground='#000000')
        # self.set_style()
        self.build()
        print("Gui constructed")

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
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))

    def build_submenus(self):
        editMenu = tk.Menu(main_menu)
        submenu = tk.Menu(editMenu)

        submenu.add_command(label="Default", command=color_test.text_update_default)
        submenu.add_command(label="White", command=color_test.text_update_white)
        submenu.add_command(label="Red", command=color_test.text_update_red)
        submenu.add_command(label="Blue", command=color_test.text_update_blue)
        submenu.add_command(label="Green", command=color_test.text_update_green)
        editMenu.add_cascade(label="Text settings", menu=submenu)

        main_menu.add_cascade(label="Edit", menu=editMenu)

        submenu2 = tk.Menu(editMenu)
        submenu2.add_command(label="Black", command=color_test.bg_update_black)
        submenu2.add_command(label="White", command=color_test.bg_update_white)
        submenu2.add_command(label="Pink", command=color_test.bg_update_pink)
        submenu2.add_command(label="Blue", command=color_test.bg_update_blue)
        editMenu.add_cascade(label="Background settings", menu=submenu2)

    root.config(menu=main_menu)