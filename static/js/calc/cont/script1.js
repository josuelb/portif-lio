function contar(){
    var ini = document.getElementById('txtI')
    var fim = document.getElementById('txtF')
    var pass = document.getElementById('txtP')
    let res = document.getElementById('res') //var e let são a mesma coisa.
    
    if (ini.value.length == 0 || fim.value.length == 0 || pass.value.length == 0){
        res.innerHTML = 'Impossível contar!'
    }
    else {
        res.innerHTML = 'Contando...'
        let i = Number(ini.value)
        let f = Number(fim.value)
        let p = Number(pass.value)

        if (p <= 0) {
            window.alert('Passo inválido! Considerando passo = 1')
            p = 1
        }

        if (i < f) {
            //Contagem crescente
            for(var c = i; c <= f; c += p) {
            res.innerHTML += ` ${c} \u{1F449}`
            }
        }
        else { 
            //Contagem regressiva
            for(let c = i; c >= f; c -= p){
                res.innerHTML += ` ${c} \u{1F449}`
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }
}

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