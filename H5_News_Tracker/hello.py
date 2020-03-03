"""
high level support for doing this and that.
"""
import tkinter


def main():
    """Displays a window onscreen with the text, 'Hi, nice to see you'"""
    root = tkinter.Tk()
    label = tkinter.Label(root, text="Hi, nice to see you")
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()