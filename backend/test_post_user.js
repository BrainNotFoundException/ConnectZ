let user_id = Math.floor(Math.random() * (6) + 1);
console.log(`Results for user of user_id = ${user_id}`)
fetch("http://localhost:5000/getusers", {
    method:"POST",
    body: JSON.stringify({
        user_id : user_id
    }),
    headers: {
        "Content-type": "application/json"
    },
})
.then((res)=>res.json()).then((json)=>console.log(json))
