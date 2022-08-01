function enviar(){
    var nom = document.getElementById("name")
    let nome = nom.value
    var em = document.getElementById("email")
    let email = em.value
    var coment = document.getElementById("coments")
    let comentario = coment.value

    var data_base = {
        nome : nome,
        email : email,
        comentario : comentario
    }

    var data = JSON.stringify(data_base)
    fetch("https://4c1b-138-185-17-139.sa.ngrok.io/JLBarbosa/comentarios/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: data,
    })
}