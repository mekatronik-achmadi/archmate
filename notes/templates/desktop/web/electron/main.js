const {app, BrowserWindow, ipcMain} = require('electron');
const path = require('node:path');

let mainWindow;
let counter = 0;

function createWindow(){
    mainWindow = new BrowserWindow({
        width: 400,
        height: 300,
        webPreferences: {
            preload: path.join(__dirname,'info.js'),
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile('index.html');
    mainWindow.removeMenu();

    // Open the DevTools.
    //mainWindow.webContents.openDevTools()
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

ipcMain.on('msgbox',(_,arg)=> {
    console.log('Message from Renderer');
    console.log(`Last counter: ${arg}`);

    counter = counter + 1;
    mainWindow.webContents.send('counter',counter.toString());
});

ipcMain.on('quit', () => {
    console.log("Electron App Quit from Renderer");

    if(process.platform !== 'darwin') app.quit();
});
