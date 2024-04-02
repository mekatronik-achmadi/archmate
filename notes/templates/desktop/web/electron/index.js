const {ipcRenderer} = require('electron');

function replaceText(selector,text) {
    const element = document.getElementById(selector);
    if(element) element.innerText = text;
}

const btnMsg = document.getElementById('btnMsg');
const btnQuit = document.getElementById('btnQuit');
const txtCnt = document.getElementById('txtCnt');

btnMsg.addEventListener('click', () => {
    // shown in renderer console
    console.log('Template Electron Web');

    // shown in a pop up window
    window.alert('Template Electron Web');

    // send messagebox request
    ipcRenderer.send('msgbox',txtCnt.innerText);
});

btnQuit.addEventListener('click',() => {
    ipcRenderer.send('quit');
});

ipcRenderer.on('counter',(_,arg) => {
    // shown in renderer console
    console.log(`counter: ${arg}`);

    replaceText('txtCnt',arg);
});