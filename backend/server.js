const express = require('express')
const port = 5000
const app = express()

app.get('/', (req, res)=>{
    res.send("Sup G")
})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})