#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Coba():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("mWnd")
        self.window.set_default_size(200,100)
        self.window.set_resizable(False)
        self.window.show_all()

    def mWnd_destroy_cb(self,window):
        Gtk.main_quit()

    def mBtnQuit_clicked_cb(self,button):
        Gtk.main_quit()

    def mBtnMsg_clicked_cb(self,button):
        print("Template Python GTK")

if __name__ == "__main__":
    app = Coba()
    Gtk.main()

