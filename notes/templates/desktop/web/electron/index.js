const {ipcRenderer} = require('electron');

function replaceText(selector,text) {
    const element = document.getElementById(selector);
    if(element) element.innerText = text;
}

const btnCnt = document.getElementById('btnCnt');
const btnMsg = document.getElementById('btnMsg');
const btnQuit = document.getElementById('btnQuit');
const txtCnt = document.getElementById('txtCnt');

btnCnt.addEventListener('click', () => {
    // send messagebox request
    ipcRenderer.send('msgbox',txtCnt.innerText);
});

btnMsg.addEventListener('click', () => {
    // shown in renderer console
    console.log('Template Electron Web');

    // shown in a pop up window
    window.alert('Template Electron Web');
});

btnQuit.addEventListener('click',() => {
    ipcRenderer.send('quit');
});

ipcRenderer.on('counter',(_,arg) => {
    // shown in renderer console
    console.log(`counter: ${arg}`);

    replaceText('txtCnt',arg);
});
