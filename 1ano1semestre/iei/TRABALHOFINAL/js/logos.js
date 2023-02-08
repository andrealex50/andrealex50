let texts = [
    {
        "title": "Grupo Toyota",
        "text": " <br> <ul> <li> O grupo Toyota, que lucrou 28.15 bilhões US$ em 2022 e tem um valor de mercado de 237.3 bilhões US$, produz veículos sob cinco marcas: Toyota, Hino, Lexus, Ranz e Daihatsu. <br><br> <li> Mas também tem participação significativa nas empresas Subaru, Mazda, Isuzu e ainda uma participação de 5.9% na Isuzu, 3.58% na Yamaha Motor Company e 0.27% na Tesla Motors. Conta ainda com acordos de joint-venture na China com os fabricantes locais GAC e FAW"
    },
    {
        "title": "Grupo Volkswagen",
        "text": " <br> <ul> <li> O grupo Volkswagen, que lucrou 17.54 bilhões US$ em 2022 e tem um valor de mercado de 82.4 bilhões US$, engloba empresas para produção de automóveis normais, de competição e de luxo. <br><br> <li> Essas empresas são a própria Volkswagen, Audi, Seat, Skoda, Porsche, Lamborghini, Bentley, Bugatti, Jetta, Ducati. E ainda para produção de automóveis comerciais as empresas Scania, Neoplan, Traton, MAN e International."
    },
    {
        "title": "Grupo Mercedes-Benz",
        "text": " <br> <ul> <li> O grupo Mercedes-Benz, que lucrou 27.19 bilhões US$ e tem um valor de mercado de 74.62 bilhões US$, é a cara das seguintes empresas: Mercedes-AMG, Mercedes-Maybach e Smart. Tem também posses nas empresas Daimler Truck, Denza, BAIC Motor e Aston Martin."
    },
    {
        "title": "Grupo Ford Motor",
        "text": " <br> <ul> <li> O grupo Ford Motor, que lucrou 17.94 bilhões US$ e tem um valor de mercado de 60.8 bilhões US$, vende carros comerciais sob a marca de Ford e a maioria dos seus carros de luxo sob a marca Lincoln. Também possui as empresas Troller e FPV. <br><br> <li> Tem também uma participação de 2.1% na Mazda, uma participação de 8% na Aston Martin e ainda uma participação de quase 50% na Jiangling. Também tem uma série de joint-ventures na China (Changan Ford), Taiwan (Ford Lio Ho), Tailândia (AutoAlliance Tailândia), Turquia (Ford Otosan) e Rússia (Ford Sollers)."
    },
    {
        "title": "Grupo BMW",
        "text": " <br> <ul> <li> O grupo BMW Group lucrou em 2022 14.64 bilhões US$ e tem um valor de mercado de 55.98 bilhões US$. Produz automóveis sob as marcas BMW, Mini e Rolls-Royce sendo esta última de luxo. Produz ainda motociclos sob a marca BMW Motorrad."
    },
    {
        "title": " Grupo General Motors",
        "text": " <br> <ul> <li> O grupo General Motors lucrou no ano de 2022 10.02 bilhões US$ e tem um valor de mercado de 57.89 bilhões e é a maior produtora automobilística nos EUA. As suas principais marcas são Chevrolet, Buick, GMC e Cadillac. <br><br> <li> Também tem participações nas marcas chinesas Wuling Motors e Baojun, assim como na marca DMAX através de joint-ventures. <br><br> <li> Tem também posse sob a BrightDrop que é um serviço focado no setor de entregas e na GM Defense que é focada em produzir veículos militares para o Departamento de Defesa e o Departamento de Estado dos Estados Unidos. "
    },
    {
        "title": " Grupo Stellantis",
        "text": " <br> <ul> <li> O grupo Stellantis que foi formado a partir da união da montadora ítalo-americana Fiat Chrysler Automobiles com a montadora francesa PSA Group, após a conclusão da fusão 50-50. <br><br> <li> No ano de 2022 lucrou 16.78 bilhões US$ e tem um valor de mercado de 44.26 bilhões US$. Ao todo o grupo reúne 14 marcas : Abarth, Alfa Romeo, Chrysler, Citroen, Dodge, DS, Fiat, Jeep, Lancia, Maserati, Opel, Peugeot, Ram e Vauxhall. E tem, portanto, presença em mais de 130 países, com produção em 30 destes. "
    },
];

for (let i = 0; i < texts.length; i++) {
    let button = document.createElement("button");
    button.innerHTML = `<img src="images/${i+1}car.png" width="250" height="250">`;
    button.onclick = function() { displayText(i) };
    document.getElementById("button-container").appendChild(button);
}

function displayText(index) {
    // Create a modal container
    let modal = document.createElement("div");
    modal.id = "modal";
    modal.style.display = "block";
    document.body.appendChild(modal);

    // Create the modal content
    let modalContent = document.createElement("div");
    modalContent.id = "modal-content";
    modal.appendChild(modalContent);

    // Add the title
    let title = document.createElement("h2");
    title.innerHTML = texts[index].title;
    modalContent.appendChild(title);
    
    // Add the text to the modal content
    let text = document.createElement("p");
    text.innerHTML = texts[index].text;
    modalContent.appendChild(text);

    // Create a close button for the modal
    let closeBtn = document.createElement("button");
    closeBtn.innerHTML = "Close";
    closeBtn.style.backgroundColor = "#382e31";
    closeBtn.style.color = "white";
    closeBtn.style.padding = "10px";
    closeBtn.style.borderRadius = "6px";
    closeBtn.style.borderColor = "#87CEEB";
    closeBtn.onclick = function() {
        modal.remove();
    }
    modalContent.appendChild(closeBtn);
}
