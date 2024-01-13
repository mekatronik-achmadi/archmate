#!/usr/bin/node

// commands to run:
//npm install
//node main.js

//////////////////// Simple Server /////////////////
const express = require('express')
const app = express()
const port = 3000

app.get('/',(req,res) => {
    res.send('NodeJS Template')
})

server = app.listen(port,() => {
    console.log(`Running server on port ${port} closed`)
});

//////////////////// Desktop Gtk /////////////////
const path = require('path')
const gi = require('node-gtk')
const Gtk = gi.require('Gtk','3.0')

gi.startLoop()
Gtk.init()

const uiFile = path.join(__dirname,'main.glade')
const builder = Gtk.Builder.newFromFile(uiFile)

function appClose(){
    server.close(() => {
        console.log(`Express Server on port ${port} closed`)
    })
    Gtk.mainQuit()
}

const handlers = {
    mBtnMsg_clicked_cb: function() {
        let msgbox = new Gtk.MessageDialog({
            text: 'Template NodeJS GTK',
            buttons: Gtk.ButtonsType.OK,
        })
        msgbox.run()
        msgbox.destroy()
    },
    mBtnQuit_clicked_cb: appClose,
}

builder.connectSignals(handlers)

const win = builder.getObject('mWnd')
win.setDefaultSize(200,100)
win.setResizable(false)

win.showAll()
Gtk.main()
