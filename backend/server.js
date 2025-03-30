const express = require('express')
const bcrypt = require('bcrypt')
const userModel = require('./config')
const mongoose = require('mongoose')
require('dotenv').config()

const port = 5000
const app = express()

const db_connection = mongoose.connect(`mongodb+srv://ghostgamerinsane:${process.env.DB_PASS}@logindata.4udiaeq.mongodb.net/`)


app.use(express.static("public"))



app.get('/', (req, res)=>{
    //render the login page
})

app.get('/signup', (req, res)=>{
    //render the signup page
})

app.post('/register', (req, res)=>{
    userModel.create(req.body).then(
        user=> res.json(user)
    ).catch(
        err=>res.json(err)
    )
})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})