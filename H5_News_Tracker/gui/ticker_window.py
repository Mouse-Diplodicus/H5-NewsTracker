"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
from tkinter import ttk


class TickerWindow:

    root = tkinter.Tk()
    menu = ttk.Label(root)
    label_ticker = ttk.Label(root)
    button_exit = ttk.Button(root)
    root.title("New JRRS")

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        print("constructing gui")
        self.root.overrideredirect(0)
        self.menu.configure(text="Change Background")
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
        self.label_ticker.configure(style="WB.TLabel")
        self.button_exit.configure(style="BR.TLabel")
        self.menu.configure(style="WB.TLabel")

    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        self.menu.grid(row=0, column=0)
        self.label_ticker.grid(row=10, column=0)
        self.button_exit.grid(row=10, column=1)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
