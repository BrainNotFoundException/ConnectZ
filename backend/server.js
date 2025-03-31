const express = require('express')
//const bcrypt = require('bcrypt')
const userModel = require('./config')
const mongoose = require('mongoose')
const {exec} = require('child_process') 
const { stdout } = require('process')
require('dotenv').config()

const port = 5000
const app = express()

const db_connection = mongoose.connect(`${process.env.DB_STRING}`)


app.use(express.static("public"))
app.use(express.json())

app.post('/login', (req, res)=>{
    console.log("\nLogin Attempt\n")
    let login = false

    let {username, password} = req.body
    
    userModel.findOne({username: username})
    .then(user =>{
        if(user){
            if(user.password == password){
                //log the user in
                res.json({logged_in: true})
                login = true;
            }
        }
    })
    if(!login){
        //reset login parameters and retry login
        res.json({logged_in: false})
    }
})

app.post('/register', (req, res)=>{
    let new_user = req.body
    userModel.findOne({username: new_user.username})
    .then(user=>{
        if(user){
            res.json({new_user: false})
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
                    res.json(err)
                }else{
                    res.json({database_update: true})
                }
            })
        }
    })
})

app.post('/getevents', (req, res)=>{
    
    exec('python ../ml/event_recommender_model.py', (error, stdout, stderr) =>{
        if(error){
            console.error(error)
            res.json(error)
        }
        if(stderr){
            console.error(stderr)
            res.json(stderr)
        }
        res.json(stdout)
    })

})

app.post('/getusers', (req, res) => {

    exec('python ../ml/user_recommender_model.py', (error, stdout, stderr) =>{
        if(error){
            res.json(error)
        }
        if(stderr){
            console.error(stderr)
            res.json(stderr)
        }
        res.json(stdout)
    })

})

app.listen(port, ()=>{
    console.log('Server up and running on port 5k')
})

mongoose.connection.once('open', ()=>{
    console.log("Connected to MongoDB")
})


/*ignore for now ig

//GET functions

app.get('/', (req, res)=>{
    //render the login page
    //post to /login for logging the user in
    res.send("Sup")
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
*/