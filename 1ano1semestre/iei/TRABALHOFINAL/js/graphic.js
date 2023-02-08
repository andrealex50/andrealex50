var ctx = document.getElementById('graphic').getContext('2d');

var vehicleData = {
    labels: ['1900', '1910', '1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990'],
    datasets: [{
        label: 'Número de carros produzidos no século XX',
        data: [2500000, 2000000, 9000000, 4000000, 1500000, 35000000, 55000000, 60000000, 65000000, 75000000],
        backgroundColor: '#ff638433',
        borderColor: '#ff6384',
        borderWidth: 1
    }]
};

var vehicleOptions = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

var graphic = new Chart(ctx, {
    type: 'line',
    data: vehicleData,
    options: vehicleOptions
});