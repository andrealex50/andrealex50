var ctx = document.getElementById('graphic').getContext('2d');

var emissionsData = {
    labels: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019','2020'],
    datasets: [{
        label: 'Quantidade de CO2 libertada pelos carros em MtCO2eq (Equivalência de emissões de CO2)',
        data: [31157, 32044, 32392, 33008, 33087, 32948, 32984, 33527, 34335, 34191, 32252],
        backgroundColor: '#ff638433',
        borderColor: '#ff6384',
        borderWidth: 1
    }]
};

var emissionsOptions = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

var graphic = new Chart(ctx, {
    type: 'line',
    data: emissionsData,
    options: emissionsOptions
});