const express = require('express')
const bcrypt = require('bcrypt')
const userModel = require('./config')
const mongoose = require('mongoose')
require('dotenv').config()

const port = 5000
const app = express()

const db_connection = mongoose.connect(`${process.env.DB_STRING}`)


app.use(express.static("public"))

app.get('/interest', (req, res)=>{
    //render the interest stack page
})

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

app.post('/setinterests', (req, res)=>{
    //set user interests here
})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})

mongoose.connection.once('open', ()=>{
    console.log("Connected to MongoDB")
})