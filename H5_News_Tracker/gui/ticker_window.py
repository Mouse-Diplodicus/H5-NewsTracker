"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
import webbrowser
from logging import root
from tkinter import ttk
from tkinter.ttk import Label


def combo_click_bg():
    if myCombo_bg.get() == 'Red':
        myLabel = Label(root, text="Text is now red", background="#f44336").pack()

    if myCombo_bg.get() == 'Green':
        myLabel = Label(root, text="Text is now green", background="#4caf50").pack()

    if myCombo_bg.get() == 'Blue':
        myLabel = Label(root, text="Text is now Blue", background="#2196f3").pack()

    if myCombo_bg.get() == 'Default':
        myLabel = Label(root, text="Text is in default", background="#212121").pack()


def combo_click_text():
    if myCombo_text.get() == 'Red':
        myLabel = Label(root, text="Text is now red", foreground="#f44336").pack()

    if myCombo_text.get() == 'Green':
        myLabel = Label(root, text="Text is now green", foreground="#4caf50").pack()

    if myCombo_text.get() == 'Blue':
        myLabel = Label(root, text="Text is now Blue", foreground="#2196f3").pack()

    if myCombo_text.get() == 'Default':
        myLabel = Label(root, text="Text is in default", foreground="#212121").pack()


text_options = [
    "Default",
    "Red",
    "Green",
    "Blue",
]

myCombo_text = ttk.Combobox(root, value=text_options)
myCombo_text.current()  # shows the current value
myCombo_text.bind("<<ComboboxSelected>>", combo_click_text)
myCombo_text.pack()


bg_options = [
    "Default",
    "Red",
    "Green",
    "Blue",
]

myCombo_bg = ttk.Combobox(root, value=bg_options)
myCombo_bg.current()  # shows the current value
myCombo_bg.bind("<<ComboboxSelected>>", combo_click_bg)
myCombo_bg.pack()


class TickerWindow:
    root = tkinter.Tk()
    label_ticker = ttk.Label(root)
    button_exit = ttk.Button(root)
    root.title("New JRRS")

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
        # self.label_ticker.configure(style="WB.TLabel")
        self.button_exit.configure(style="BR.TLabel")
        # self.menu.configure(style="WB.TLabel")

    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        combo_click_bg().grid(row=10, column=0)
        combo_click_text().grid(row=10, column=2)
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=10)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
