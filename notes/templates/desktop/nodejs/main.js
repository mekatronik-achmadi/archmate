#!/usr/bin/node

// commands to run:
//npm install
//node main.js

const server = require('express')
const app = server()
const port = 3000

app.get('/',(req,res) => {
    res.send('NodeJS Template')
})

app.listen(port, ()=> {
    console.log(`NodeJS Template on port ${port}`)
})

