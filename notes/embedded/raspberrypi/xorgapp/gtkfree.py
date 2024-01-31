#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')

import subprocess
from gi.repository import Gtk

def on_click(self):
    r = subprocess.run(["free", "-h"], stdout=subprocess.PIPE, stderr=None)
    res = r.stdout.decode('utf-8')
    txtbuffer.set_text(res)

window = Gtk.Window()
window.set_default_size(360, 240)
window.set_resizable(False)
window.set_title("GTK Memory")
window.connect("destroy", Gtk.main_quit)

txtbuffer = Gtk.TextBuffer()
txtview = Gtk.TextView()
txtview.set_buffer(txtbuffer)

scrolled_window = Gtk.ScrolledWindow()
scrolled_window.add(txtview)

headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)

go_back = Gtk.Button()
go_back_arrow = Gtk.Image.new_from_icon_name("go-down", Gtk.IconSize.SMALL_TOOLBAR)
go_back.add(go_back_arrow)
go_back.connect("clicked",on_click)
headerbar.pack_start(go_back)

window.add(scrolled_window)
window.set_titlebar(headerbar)
window.show_all()

Gtk.main()
