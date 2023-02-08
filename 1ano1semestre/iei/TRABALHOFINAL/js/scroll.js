function scrollDown() {
    // Vai buscar a posição do container
    var containerPosition = document.querySelector('.container').offsetTop;
    
    // Faz scroll para a posição do container
    window.scrollTo({
      top: containerPosition,
      behavior: 'smooth'
    });
}
document.querySelector('#scrollDown').addEventListener('click', scrollDown);
