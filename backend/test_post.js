fetch("http://localhost:5000/getevents", {
    method:"POST",
    body: JSON.stringify({
    }),
    headers: {
        "Content-type": "application/json"
    },
})
.then((res)=>res.json()).then((json)=>console.log(json))

/*fetch("http://localhost:5000/register", {
    method:"POST",
    body: JSON.stringify({
        username: "Lav",
        name: "Lavnish",
        email: "sup@gmail.com",
        password: "oopsie",
        interests: ["Machine Learning", "YeeHaw"]
    }),
    headers: {
        "Content-type": "application/json"
    },
})
.then((res)=>res.json()).then((json)=>console.log(json))*/