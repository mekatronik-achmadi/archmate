console.log('Client Template Running');

const btnMsgWeb = document.getElementById('btnMsgWeb');
const btnMsgCLI = document.getElementById('btnMsgCLI');
const btnQuit = document.getElementById('btnQuit');

btnMsgWeb.addEventListener('click', function() {
    // shown in webbrowser console
    console.log('Template NodeJS Web');

    // shown in a pop up window
    window.alert('Template NodeJS Web');
});

btnMsgCLI.addEventListener('click', function() {
    // request back to server.js
    fetch('/clicked',{method: 'POST'})
    .then(function(resp) {
        if(resp.ok){
            // shown in webbrowser console
            console.log('click log requested');
            return;
        }

        // if server disconnected
        throw new Error('click request failed');
    })
    .catch(function(err) {
        // shown in webbrowser console
        console.log(err);
    });
});

btnQuit.addEventListener('click', function() {
    // request back to server.js
    fetch('/stopit',{method: 'POST'})
    .then(function(resp) {
        if(resp.ok){
            // shown in webbrowser console
            console.log('stop server requested');
            return;
        }

        // if server disconnected
        throw new Error('stop server failed');
    })
    .catch(function(err) {
        // shown in webbrowser console
        console.log(err);
    });
});

