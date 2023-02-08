function decreaseImage(element){
    var height = parseInt(element.style.height,10);
    for( ; height > 0; height--){
    element.style.height = height+"px";
    }
}

function resetImage(element){
    element.style.display = "block";
    element.style.height = "370px";
    element.style.width ="550px";
}
    