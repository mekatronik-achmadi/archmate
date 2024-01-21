#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Template():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.mWnd = self.builder.get_object("mWnd")
        self.mBtnMsg = self.builder.get_object("mBtnMsg")
        self.mBtnQuit = self.builder.get_object("mBtnQuit")

        self.mWnd.set_default_size(200,100)
        self.mWnd.set_resizable(False)
        self.mWnd.connect("destroy",self.mWnd_destroy)

        self.mBtnMsg.connect("clicked",self.mBtnMsg_clicked)
        self.mBtnQuit.connect("clicked",self.mBtnQuit_clicked)

    def show_all(self):
        self.mWnd.show_all()

    def mWnd_destroy(self,window):
        Gtk.main_quit()

    def mBtnQuit_clicked(self,button):
        Gtk.main_quit()

    def mBtnMsg_clicked(self,button):
        self.msgbox = Gtk.MessageDialog(text="Template Python GTK",
                                        buttons=Gtk.ButtonsType.OK)
        self.msgbox.run()
        self.msgbox.destroy()

if __name__ == "__main__":
    app = Template()
    app.show_all()
    Gtk.main()

