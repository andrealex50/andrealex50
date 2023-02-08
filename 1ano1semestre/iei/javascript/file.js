/* comentário */
for(var i=0;i<16;i++){
    document.write("uma-string" - 2);
    document.write("<br>");
    }
    document.write("Batman");

function soma(x,y){
    return x+y;
}

var resultado = soma(3,4);
console.log(resultado);

function multiplicaçao(x,y){
    return x*y;
}

var resultado = multiplicaçao(3,4);
console.log(resultado);

function subtração(x,y){
    return x-y;
}

var resultado = subtração(3,4);
console.log(resultado);

var a = "3";
var b = 3;
if (a == b) alert("Iguais");
else alert("Diferentes");

var a ="abc";
switch(a) {
    case "abc": alert("string abc"); break;
    case 3: alert("inteiro 3"); break;
    default: alert("outro");
}  