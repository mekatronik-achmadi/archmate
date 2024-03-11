const path = require('path');
const gi = require('node-gtk');
const Gtk = gi.require('Gtk','3.0');

gi.startLoop();
Gtk.init();

const uiFile = path.join(__dirname,'main.glade');
const builder = Gtk.Builder.newFromFile(uiFile);

const mWnd = builder.getObject('mWnd');
mWnd.setDefaultSize(200,100);
mWnd.setResizable(false);
mWnd.on('destroy',()=>{
    Gtk.mainQuit();
});

const mBtnMsg = builder.getObject('mBtnMsg');
mBtnMsg.on('clicked', () => {
    let msgbox = new Gtk.MessageDialog({
        text: 'Template NodeJS GTK3',
        buttons: Gtk.ButtonsType.OK,
    });

    msgbox.run();
    msgbox.destroy();
});

const mBtnQuit = builder.getObject('mBtnQuit');
mBtnQuit.on('clicked', () => {
    Gtk.mainQuit();
});

mWnd.showAll();

Gtk.main();

