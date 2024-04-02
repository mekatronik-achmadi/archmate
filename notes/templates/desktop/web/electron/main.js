const {app, BrowserWindow} = require('electron');

function createWindow(){
    const mainWindow = new BrowserWindow({
        width: 400,
        height: 300
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();
});

