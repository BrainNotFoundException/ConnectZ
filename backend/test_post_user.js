fetch("http://localhost:5000/getusers", {
    method:"POST",
    body: JSON.stringify({
    }),
    headers: {
        "Content-type": "application/json"
    },
})
.then((res)=>res.json()).then((json)=>console.log(json))
