#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Template():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("mWnd")
        self.window.set_default_size(200,100)
        self.window.set_resizable(False)
        self.window.show_all()

    def mBtnQuit_clicked_cb(self,button):
        Gtk.main_quit()

    def mBtnMsg_clicked_cb(self,button):
        self.msgbox = Gtk.MessageDialog(text="Template Python GTK",
                                        buttons=Gtk.ButtonsType.OK)
        self.msgbox.run()
        self.msgbox.destroy()

if __name__ == "__main__":
    app = Template()
    Gtk.main()

