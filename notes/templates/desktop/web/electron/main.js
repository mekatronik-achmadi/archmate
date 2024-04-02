const {app, BrowserWindow} = require('electron');
const path = require('node:path');

let mainWindow;

function createWindow(){
    mainWindow = new BrowserWindow({
        width: 400,
        height: 300,
        webPreferences: {
            preload: path.join(__dirname,'info.js'),
            nodeIntegration: true
        }
    });

    mainWindow.loadFile('index.html');
    // mainWindow.webContents.send('welcome', 'Hello World, Electron');
}

app.whenReady().then(() => {
    console.log("Electron App Started");

    createWindow();

    app.on('activate', () => {
        if(BrowserWindow.getAllWindows().length===0){
            createWindow();
        }
    });
});

app.on('window-all-closed',() => {
    console.log("Electron App Quit");
    if(process.platform !== 'darwin') app.quit();
});
