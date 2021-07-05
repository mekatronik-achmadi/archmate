#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2

def on_entry(entry):
    url = "http://%s" % entry.get_text()
    webview.load_uri(url)

default_url = "https://google.com"

window = Gtk.Window()
window.set_default_size(480, 320)
window.set_resizable(False)
window.set_title("GTK WebBrowser")
window.connect("destroy", Gtk.main_quit)

webview = WebKit2.WebView()
webview.load_uri(default_url)

scrolled_window = Gtk.ScrolledWindow()
scrolled_window.add(webview)

headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)

entry = Gtk.Entry()
entry.set_text(default_url)
entry.connect("activate",on_entry)
headerbar.set_custom_title(entry)

window.add(scrolled_window)
window.set_titlebar(headerbar)
window.show_all()

Gtk.main()
