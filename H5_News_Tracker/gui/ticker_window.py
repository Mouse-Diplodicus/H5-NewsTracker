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
    root.overrideredirect(True)  # Delete border

    menu_bar = tk.Menu(root)
    textColor = tkinter.StringVar()
    textColor.set('black')
    background = tkinter.StringVar()
    background.set('white')


    var = tkinter.StringVar(root)
    # var.set('Select')
    choices = ['Background Options', 'Black', 'White', 'Blue', 'Pink']

    label_ticker = ttk.Label(root)
    button_exit = ttk.Button(root)
    root.title("New JRRS")

    def __init__(self, master=None, **kw):
        """Initializes the display window for the news ticker"""
        print("constructing gui")
        self.root.overrideredirect(1)
        self.label_ticker.configure(width=8, background='#000000', foreground='#ffffff')
        self.button_exit.configure(text="X", padding=[2, 0, 2, 0], command=self.root.quit)
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
        self.button_exit.configure(style="BR.TLabel")
        # self.menu.configure(style=" WB.TLabel")
        # if self.choices == 'Black':
        #     style.configure(background='black')

    # def background(self, menu, label_ticker):
    #     if menu == 'Black':
    #         ttk.Label(style='WB.TLabel')
    #     elif menu == 'White':
    #         label_ticker.configure(background='white')
    #     elif menu == 'Blue':
    #         label_ticker.configure(background='blue')
    #     elif menu == 'Pink':
    #         label_ticker.configure(background='pink')
    #
    # menu = OptionMenu(root, var, *choices, command=background)

    def build(self):
        """Sets organization for label and exit button"""
        print("organizing gui layout")
        # self.menu.grid(row=10, column=0)
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=10)

    def update(self, headline, url):
        print("updating ticker to headline: ", headline, "   url: ", url)
        self.label_ticker.configure(text=headline, width=len(headline))
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))

    edit_menu = tk.Menu(menu_bar)

    submenu = tk.Menu(edit_menu)
    submenu.add_command(label="Default")
    submenu.add_command(label="Red")
    submenu.add_command(label="Blue")
    edit_menu.add_cascade(label="Text settings", menu=submenu)

    submenu2 = tk.Menu(edit_menu)
    submenu2.add_command(label="Black")
    submenu2.add_command(label="White")
    submenu2.add_command(label="Pink")
    submenu2.add_command(label="Blue")
    edit_menu.add_cascade(label="Background settings", menu=submenu2)

    menu_bar.add_cascade(menu=edit_menu, label="Edit")

    root.config(menu=menu_bar)
