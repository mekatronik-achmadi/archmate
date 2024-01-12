#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class Template():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("200x100")
        self.window.title("Template")

        self.txtlabel = tk.Label(self.window,text="Template Tkinter")
        self.txtlabel.pack(side=tk.TOP,expand=True)

        self.btnfrm = tk.Frame(self.window)

        self.btnmsg = tk.Button(self.btnfrm,text="Message",command=self.onbtnmsg)
        self.btnmsg.pack(side=tk.TOP,expand=True)

        self.btnquit = tk.Button(self.btnfrm,text="Quit",command=self.onbtnquit)
        self.btnquit.pack(side=tk.BOTTOM,expand=True)

        self.btnfrm.pack(side=tk.BOTTOM,expand=True)

    def run(self):
        self.window.mainloop()

    def onbtnquit(self):
        self.window.destroy()

    def onbtnmsg(self):
        messagebox.showinfo("Template","Template Python Tkinter")

if __name__ == "__main__":
    app = Template()
    app.run()

