console.log('Server WASM Start');

const express = require('express');
const app = express();
const port = 8001;

app.use(express.static('.'));

var server = app.listen(port, ()=> {
    console.log(`Server Listening on port ${port}`);
});

app.get('/',(req,res) => {
    res.sendFile(__dirname+'/main.html');
});

