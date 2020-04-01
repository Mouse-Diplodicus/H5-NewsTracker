from tkinter import *

root = Tk()
textColor = StringVar()
textColor.set('black')
background = StringVar()
background.set('white')


# ////////////////////////////////////
# Changes text color
def text_update_green():
    textColor.set('green')
    print
    textColor.get()
    l.configure(fg=textColor.get())


def text_update_blue():
    textColor.set('blue')
    print
    textColor.get()
    l.configure(fg=textColor.get())


def text_update_red():
    textColor.set('red')
    print
    textColor.get()
    l.configure(fg=textColor.get())


def text_update_white():
    textColor.set('white')
    print
    textColor.get()
    l.configure(fg=textColor.get())


def text_update_default():
    textColor.set('black')
    print
    textColor.get()
    l.configure(fg=textColor.get())


# /////////////////////////////////
# Changes background color

def bg_update_blue():
    background.set('blue')
    print
    background.get()
    l.configure(bg=background.get())


def bg_update_black():
    background.set('black')
    print
    background.get()
    l.configure(bg=background.get())


def bg_update_pink():
    background.set('pink')
    print
    background.get()
    l.configure(bg=background.get())


def bg_update_white():
    background.set('white')
    print
    background.get()
    l.configure(bg=background.get())


main_menu = Menu(root)
root.config(menu=main_menu)

editMenu = Menu(main_menu)

submenu = Menu(editMenu)
submenu.add_command(label="Default", command=text_update_default)
submenu.add_command(label="White", command=text_update_white)
submenu.add_command(label="Red", command=text_update_red)
submenu.add_command(label="Blue", command=text_update_blue)
submenu.add_command(label="Green", command=text_update_green)
editMenu.add_cascade(label="Text settings", menu=submenu)

main_menu.add_cascade(label="Edit", menu=editMenu)

submenu2 = Menu(editMenu)
submenu2.add_command(label="Black", command=bg_update_black)
submenu2.add_command(label="White", command=bg_update_white)
submenu2.add_command(label="Pink", command=bg_update_pink)
submenu2.add_command(label="Blue", command=bg_update_blue)
editMenu.add_cascade(label="Background settings", menu=submenu2)

l = Label(root, text="Change My Text Color", fg=textColor.get(), bg=background.get())
l.pack()

root.mainloop()
