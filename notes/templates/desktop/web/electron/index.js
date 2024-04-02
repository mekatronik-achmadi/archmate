// const {ipcRenderer} = require('electron');

const btnMsgWeb = document.getElementById('btnMsgWeb');

btnMsgWeb.addEventListener('click', function() {
    // shown in electron render console
    console.log('Template Electron Web');

    // shown in a pop up window
    window.alert('Template Electron Web');
});

// ipcRenderer.on('welcome',(_,arg) => {
//     window.alert('Welcome Electron');
// });