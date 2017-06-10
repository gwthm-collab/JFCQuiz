from Tkinter import *
import tkMessageBox

def fun_Login():
    tkMessageBox._show("Information","Displayed")


tk = Tk()
txt1, txt2 = StringVar(),StringVar()
lbl1 = Label(tk, text = "Username: ")
lbl2 = Label(tk, text = "Password: ")
entry1 = Entry(tk, textvariable = txt1)
entry2 = Entry(tk, textvariable = txt2)
lbl1.grid(row = 0)
lbl2.grid(row = 1)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)
btnLogin = Button(tk, text = "Login", command = fun_Login)
btnLogin.grid(row = 2)
tk.mainloop()