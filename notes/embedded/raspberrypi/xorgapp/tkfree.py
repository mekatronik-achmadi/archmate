#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess as sp

def appquit():
    """ Quit Program"""
    window.destroy()

def memfree():
    txtbox.delete('1.0',tk.END)
    mfree = sp.run(["free","-h"],stdout=sp.PIPE,stderr=None).stdout.decode("utf-8")
    txtbox.insert(tk.END,mfree)

window = tk.Tk()
window.geometry("480x320")
window.title("Tk MemFree")

txtbox = tk.Text(window,height=20,width=80)
txtbox.config(font=("Liberation Mono",8))
txtbox.pack(side=tk.TOP)

btnfrm = tk.Frame(window)

btnmem = tk.Button(btnfrm,text="MemFree",command=memfree)
btnmem.pack(side=tk.LEFT)

btnquit = tk.Button(btnfrm, text="  Quit  ", command=appquit)
btnquit.pack(side=tk.RIGHT)

btnfrm.pack(side=tk.BOTTOM, expand=True)

window.mainloop()
