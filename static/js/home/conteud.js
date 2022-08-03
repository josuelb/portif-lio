import url from '../script0.js'

var url_final = url+'conteudos/'

const xhttp = new XMLHttpRequest()

xhttp.open("GET", url_final, false)
xhttp.send()

let conteudo = JSON.parse(xhttp.responseText)

function iniciar() {
    var container = document.getElementById('container')
    
    for(let p in conteudo){
        if(conteudo[p].local == 'home/'){
            container.innerHTML += `
            
                <div class="conteudo">
                    <a href=`+conteudo[p].link+`>
                        <img src="`+conteudo[p].image+`" alt="idroid" class="conteudo_img"><br>
                        <h3>`+conteudo[p].titulo+`</h3><br>
                    </a>
                </div>

                `
        }
    }
}

iniciar()
