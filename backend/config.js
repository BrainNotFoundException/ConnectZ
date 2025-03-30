const mongoose = require('mongoose')

const LoginData = new mongoose.Schema({
    name: String,
    username: String,
    email: String,
    password: String
})

const userModel = mongoose.model("users", LoginData)

module.exports = userModel