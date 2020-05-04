from tkinter import *

root = Tk()
colour = StringVar()
colour.set('black')


def colour_update_green():
    colour.set('green')
    print
    colour.get()
    l.configure(fg=colour.get())


def colour_update_blue():
    colour.set('blue')
    print
    colour.get()
    l.configure(fg=colour.get())


def colour_update_red():
    colour.set('red')
    print
    colour.get()
    l.configure(fg=colour.get())


def colour_update_default():
    colour.set('black')
    print
    colour.get()
    l.configure(fg=colour.get())


main_menu = Menu(root)
root.config(menu=main_menu)

editMenu = Menu(main_menu)

submenu = Menu(editMenu)
submenu.add_command(label="Default", command=colour_update_default)
submenu.add_command(label="Red", command=colour_update_red)
submenu.add_command(label="Blue", command=colour_update_blue)
submenu.add_command(label="Green", command=colour_update_green)
editMenu.add_cascade(label="Text settings", menu=submenu)

main_menu.add_cascade(label="Edit", menu=editMenu)


l = Label(root, text="Change My Text Color", fg=colour.get())
l.pack()

root.mainloop()
