const responses=[]
const maxResponses=4
var sent=false

// Comprovacions:
// 	- Encara es poden posar més paraules
// 	- No s'ha enviat la llista
// 	- Trim

function search() {
    if(event.keyCode == 13) {
        getName();
        if (responses.length == 4) {
            submitWords(); 
        }
    }
}

function getName(){

    var text = document.getElementById("usr").value;
    var list = document.getElementById("list-words");
    var li = document.createElement("li");
    const logInput=document.getElementById("error-input")

    li.appendChild(document.createTextNode(text));
    list.appendChild(li);
    li.classList.add("list-group-item");

    li.addEventListener('click', function onclick(){
        responses.splice(text, 1)
        li.remove();
    });

    li.addEventListener('mouseover', function mouseover(){
        li.style.backgroundColor = "#F9917A";
        li.innerHTML = "Remove element!";
    });
    li.addEventListener('mouseout', function mouseout(){
        li.style.backgroundColor = "white";
        li.innerHTML = text;
    });

    if (sent){
        logInput.style.color="red"
        logInput.innerText="Already sent"
        return
    }
    if (text.length==0){
        return
    }
    if (responses.length>=maxResponses){
        logInput.style.color="red"
        logInput.innerText="You can't add more than "+maxResponses+" words"
        text.style.backgroundColor= "#fce4e4"
        text.style.border= "1px solid #cc0033"
        text.style.outline= "none"
        return
    }
    logInput.style=""
    logInput.innerText=""
    responses.push(text)
    console.log(responses)
    //document.getElementById("llista-paraules").innerHTML+='<li class="list-group-item active">'+word+'</li>'
}

function submitWords() {
if (sent){
    return
}
const logInput=document.getElementById("error-input")
if (responses.length<maxResponses){
    const textField=document.getElementById("usr")
    logInput.style.color="red"
    if(responses.length==0){
        logInput.innerText="You must be so fun at parties..."
    }else{
        logInput.innerText="You just added "+responses.length+" of "+maxResponses+" possible words"
    }
    textField.style.backgroundColor= "#fce4e4"
    textField.style.border= "1px solid #cc0033"
    textField.style.outline= "none"
    return
}


logInput.style.color="green"
logInput.innerText="Successfully sent"
const text=JSON.stringify({responses})
// CANVIAR PER FER LA PETICIÓ
fetch("{% url 'wordinput' %}",{method: 'POST',body : text})
    .then(res=>console.log("hola"));

form.appendChild(formField);
form.submit();
}