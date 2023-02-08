var op = "+"; // variável global que representa a operação a realizar (adição por defeito)

function operation() {
    var e = document.getElementById( "operation" );
    op = e.options[e.selectedIndex].value;
    console.log( "Operation: "+op ); // mostra a operação na consola
    var opt = document.getElementById( "op-view" );
    opt.innerHTML = op; // atualiza a operação na página
}

function calculate() {
    var x = document.getElementById( "op1" );
    var y = document.getElementById( "op2" );
    var op1 = parseFloat(x.value)
    var op2 = parseFloat(y.value)
    console.log(op1);
    console.log(op2);
    var z = document.getElementById( "res" );
    switch (op) {
        case "+":
            z.value = op1 + op2;
            break;
        case "-":
            z.value = op1 - op2;
            break;
        case "x":
            z.value = op1 * op2
            break;
        case ":":
            z.value = op1 / op2
            break
    }
    console.log( z.value ); // mostra o resultado da soma na consola
}

function move(){
    var e = document.getElementById( "btn" );
    
    e.style.position = "absolute";
    e.style.top = (Math.random() * window.innerHeight)+"px";
    e.style.left = (Math.random() * window.innerWidth)+"px";
}
    