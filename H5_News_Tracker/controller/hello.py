"""
Program displays a window with text using Tkinter when run.
"""
import tkinter
from tkinter import ttk


def main():
    """Displays a window onscreen with the text, 'Hi, nice to see you!'"""
    root = tkinter.Tk()
    root.overrideredirect(1)                # Makes window borderless
    style = ttk.Style()
    style.configure("WB.TLabel", foreground="#ffffff", background="#000000")
    style.configure("R.TLabel", foreground="#000000", background="#931113")
    label = ttk.Label(root, text="Hi, nice to see you!", style="WB.TLabel")
    button_exit = ttk.Button(root, text="X", padding=[4, 0, 4, 0], style="R.TLabel", command=root.quit)
    label.grid(row=0, column=0)
    button_exit.grid(row=0, column=1)
    root.mainloop()


if __name__ == "__main__":
    main()
