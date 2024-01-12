#!/usr/bin/node

// commands to run:
//npm install
//node main.js

//////////////////// Simple Server /////////////////
const server = require('express')
const app = server()
const port = 3000

app.get('/',(req,res) => {
    res.send('NodeJS Template')
})

app.listen(port, ()=> {
    console.log(`NodeJS Template on port ${port}`)
})

//////////////////// Desktop Gtk /////////////////
const path = require('path')
const gi = require('node-gtk')
const Gtk = gi.require('Gtk','3.0')

gi.startLoop()
Gtk.init()

const uiFile = path.join(__dirname,'main.glade')
const builder = Gtk.Builder.newFromFile(uiFile)

const handlers = {
    mWnd_destroy_cb: Gtk.mainQuit,
    mBtnMsg_clicked_cb: function() {
        console.log('Template NodeJS GTK')
    },
    mBtnQuit_clicked_cb: Gtk.mainQuit,
}

builder.connectSignals(handlers)

const win = builder.getObject('mWnd')
win.setDefaultSize(200,100)
win.setResizable(false)

win.showAll()
Gtk.main()
