"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter.ttk import OptionMenu


class TickerWindow:
    root = tkinter.Tk()

    menubar = tk.Menu(root)

    var = tkinter.StringVar(root)
    var.set('Select')
    choices = ['Background Options', 'Black', 'White', 'Blue', 'Pink']

    label_ticker = ttk.Label(root)
    button_exit = ttk.Button(root)
    root.title("New JRRS")

    def background(self, select):
        if select == 'Black':
            self.menu.configure(background='black')
        elif select == 'White':
            self.menu.configure(background='white')
        elif select == 'Blue':
            self.menu.configure(background='blue')
        elif select == 'Pink':
            self.menu.configure(background='pink')

    menu = OptionMenu(root, var, *choices, command=background)

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        print("constructing gui")
        self.root.overrideredirect(0)
        self.label_ticker.configure(width=8)
        self.button_exit.configure(text="X", padding=[4, 0, 4, 0], command=self.root.quit)
        self.set_style()
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
        style.configure("black.TLabel", foreground="#ffffff", background="#000000")
        style.configure("WB.TLabel", foreground="#ffffff", background="#000000")
        style.configure("BR.TLabel", foreground="#000000", background="#931113")
        # self.label_ticker.configure(style="WB.TLabel")
        self.button_exit.configure(style="BR.TLabel")
        # self.menu.configure(style="WB.TLabel")
        if self.choices == 'Black':
            self.label_ticker.configure(style="black")


    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        self.menu.grid(row=10, column=0)
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=10)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))

    editmenu = tk.Menu(menubar, tearoff=0, foreground="black")
    editmenu.add_cascade(label="Text settings")

    text_setting = tk.Menu(editmenu)
    editmenu.add_command(label="Text Color")

    editmenu.add_cascade(label="Background settings", command=background)
    menubar.add_cascade(menu=editmenu, label="Edit")


    root.config(menu=menubar)