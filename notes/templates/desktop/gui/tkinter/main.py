#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

class Template():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("200x100")
        self.window.title("Template")

        #self.style = ttk.Style(self.window)
        #self.style.theme_use("alt")
        self.style = ThemedStyle(self.window)
        self.style.theme_use("clearlooks")

        self.txtlabel = ttk.Label(self.window,text="Template Tkinter")
        self.txtlabel.pack(side=tk.TOP,expand=True,fill='both')

        self.btnfrm = ttk.Frame(self.window)

        self.btnmsg = ttk.Button(self.btnfrm,text="Message",command=self.onbtnmsg)
        self.btnmsg.pack(side=tk.TOP,expand=True,fill='both')

        self.btnquit = ttk.Button(self.btnfrm,text="Quit",command=self.onbtnquit)
        self.btnquit.pack(side=tk.BOTTOM,expand=True,fill='both')

        self.btnfrm.pack(side=tk.BOTTOM,expand=True,fill='both')

    def run(self):
        self.window.mainloop()

    def onbtnquit(self):
        self.window.destroy()

    def onbtnmsg(self):
        messagebox.showinfo("Template","Template Python Tkinter")

if __name__ == "__main__":
    app = Template()
    app.run()

