const express = require('express')
const bcrypt = require('bcrypt')
const userModel = require('./config')
const mongoose = require('mongoose')
require('dotenv').config()

const port = 5000
const app = express()

const db_connection = mongoose.connect(`${process.env.DB_STRING}`)


app.use(express.static("public"))

//GET functions

app.get('/', (req, res)=>{
    //render the login page
    //post to /login for logging the user in
})

app.get('/signup', (req, res)=>{
    //render the signup page
    //post to /register for registering a new user
})

app.get('/interest', (req, res)=>{
    //render the interest stack page
    //post to /setinterests to set interests
})


//POST functions

app.post('/login', (req, res)=>{
    var {username, pass} = req.body
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
    let new_user = res.body
    userModel.findOne({username: new_user.username})
    .then(user=>{
        if(user){
            res.send("User already exists please try logging in!")
        }else{
            userModel.create(req.body).then(
                users=> res.json(users)
            ).catch(
                err=>res.json(err)
            )
        }
    })
})

app.post('/setinterests', (req, res)=>{
    let username = res.body.username
    let interest_stack = res.body.interest_stack
    userModel.findOne({username: username})
    .then(user=>{
        if (user){
            let update = userModel.findOne({username: username})
            update.interests = interest_stack
            userModel.findOneAndUpdate({username: username}, update, (err, doc)=>{
                if(err){
                    console.log(err)
                    res.send('Error encountered check logs')
                }else{
                    console.log('Database has been updated Successfully!')
                    res.send('Interests updated')
                }
            })
        }
    })
})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})

mongoose.connection.once('open', ()=>{
    console.log("Connected to MongoDB")
})