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

app.post('/login', (req, res)=>{
    const {username, pass} = req.body
    let login = false
    userModel.findOne({username: username})
    .then(user =>{
        if(user){
            if(user.password == pass){
                //log the user in
                res.json('Login.')
                login = true;
            }
        }
    })
    if(!login){
        //reset login parameters and retry login
        res.json("Incorrect username or password!")
    }
})

app.post('/register', (req, res)=>{
    userModel.create(req.body).then(
        users=> res.json(users)
    ).catch(
        err=>res.json(err)
    )
})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})