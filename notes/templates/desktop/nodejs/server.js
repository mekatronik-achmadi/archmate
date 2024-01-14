console.log('Server Template Running');

const express = require('express');
const app = express();
const port = 8001;

app.use(express.static('public'));

var server = app.listen(port, () =>{
    console.log(`Server Listening on port ${port}`);
});

app.get('/',(req,res) =>{
    res.sendFile(__dirname+'/index.html');
});

app.post('/clicked',() => {
    console.log('Web Button Just Clicked');
});

app.post('/stopit',() => {
    server.close();
    console.log('Closing Server');
    console.log('Waiting Tab/Window closed');
});

