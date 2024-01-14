#!/usr/bin/node

// commands to run:
//npm install
//node main.js

const path = require('path')
const gi = require('node-gtk')
const Gtk = gi.require('Gtk','3.0')

gi.startLoop()
Gtk.init()

const uiFile = path.join(__dirname,'main.glade')
const builder = Gtk.Builder.newFromFile(uiFile)

const handlers = {
    mBtnMsg_clicked_cb: function() {
        let msgbox = new Gtk.MessageDialog({
            text: 'Template NodeJS GTK',
            buttons: Gtk.ButtonsType.OK,
        })
        msgbox.run()
        msgbox.destroy()
    },
    mBtnQuit_clicked_cb: Gtk.mainQuit
}

builder.connectSignals(handlers)

const win = builder.getObject('mWnd')
win.setDefaultSize(200,100)
win.setResizable(false)

win.showAll()
Gtk.main()

