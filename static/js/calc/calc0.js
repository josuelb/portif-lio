import url from '../script0.js'

console.log(url)
const xhttp = new XMLHttpRequest()

var url_final = url+"conteudos/"

console.log(url_final)

xhttp.open("GET", url_final, false)
xhttp.send()

let conteudo = xhttp.responseText
var conteud = JSON.parse(conteudo)

function iniciar() {
    var container = document.getElementById('container')
    for(let p=0; p < conteud.length; p += 1){
        if (conteud[p].local == 'calc/'){
            container.innerHTML = `
            
            <div class="conteudo">
                <a href=`+conteud[p].link+`>
                    <img src="`+conteud[p].image+`" alt="idroid" height="150px" class="idroid_img"><br>
                    <h3>`+conteud[p].titulo+`</h3><br>
                </a>
            </div>

            `
        }
    }
}

iniciar()