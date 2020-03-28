"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
from tkinter import ttk


class TickerWindow:
    root = tkinter.Tk()
    label_ticker = ttk.Label(root)
    button_exit = ttk.Button(root)
    root.title("New JRRS")

    options = [
        "Default",
        "Red",
        "Green",
        "Blue",
    ]

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
        style.configure("WB.TLabel", foreground="#ffffff", background="#000000")
        style.configure("BR.TLabel", foreground="#000000", background="#931113")
        style.configure("RBg.TLabel", background="#f44336")
        # style.configure("RT.TLabel", foreground="#f44336")
        style.configure("GBg.TLabel", background="#4caf50")
        # style.configure("GT.TLabel", foreground="#4caf50")
        style.configure("BBg.TLabel", background="#2196f3")
        # style.configure("BT.TLabel", foreground="#2196f3")
        # self.label_ticker.configure(style="WB.TLabel")
        self.button_exit.configure(style="BR.TLabel")
        # self.menu.configure(style="WB.TLabel")

    def combo_click_bg(self):
        if self.myCombo_bg.get() == 'Red':
            self.label_ticker.configure(background="f44336")

        elif self.myCombo_bg.get() == 'Green':
            self.label_ticker.configure(background="4caf50")

        elif self.myCombo_bg.get() == 'Blue':
            self.label_ticker.configure(background="2196f3")

        elif self.myCombo_bg.get() == 'Default':
            self.label_ticker.configure(background="4caf50")

    myCombo_bg = ttk.Combobox(root, value=options)
    myCombo_bg.current()  # shows the current value

    myCombo_bg.bind("<<ComboboxSelected>>", combo_click_bg)
    myCombo_bg.pack()

    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        self.myCombo_bg.grid(row=10, column=0)
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=10)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
