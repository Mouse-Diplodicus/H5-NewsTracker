from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Color Drop Down')
root.geometry("400x400")

#Each button changes text color
def comboclick(event):
    if myCombo.get() == 'Red':
        myLabel = Label(root, text="Text is now red", foreground="#f44336").pack()

    if myCombo.get() == 'Green':
        myLabel = Label(root, text="Text is now green", foreground="#4caf50").pack()

    if myCombo.get() == 'Blue':
        myLabel = Label(root, text="Text is now Blue", foreground="#2196f3").pack()

    if myCombo.get() == 'Default':
        myLabel = Label(root, text="Text is in default", foreground="#212121").pack()

# String of options in the drop menu
options = [
    "Default",
    "Red",
    "Green",
    "Blue",
]


myCombo = ttk.Combobox(root, value=options)
myCombo.current() #shows the current value
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

root.mainloop()