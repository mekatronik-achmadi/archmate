#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

def onbtnquit():
    window.destroy()

def onbtnmsg():
    messagebox.showinfo("Template","Template Python Tkinter")

window = tk.Tk()
window.geometry("200x100")
window.title("Template")

txtlabel = tk.Label(window,text="Template Tkinter")
txtlabel.pack(side=tk.TOP,expand=True)

btnfrm = tk.Frame(window)

btnmsg = tk.Button(btnfrm,text="Message",command=onbtnmsg)
btnmsg.pack(side=tk.TOP,expand=True)

btnquit = tk.Button(btnfrm,text="Quit",command=onbtnquit)
btnquit.pack(side=tk.BOTTOM,expand=True)

btnfrm.pack(side=tk.BOTTOM,expand=True)

window.mainloop()

