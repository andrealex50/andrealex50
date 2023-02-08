let type = "line"; // line graphic by default

function graphic() {
  e = document.getElementById("selection");
  type = e.options[e.selectedIndex].value;
}


function draw() {
    $("#myGraph").highcharts({
        chart: { type: type },
        title: { text: "Temperatures Average" },
        xAxis: { categories: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
                              "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
               },
        series:[
                { 
                    name: "Lisboa",
                    data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
                },
                {
                    name: "Aveiro",
                    data: [10.0, 9.5, 12.0, 13.4, 15.0, 17.2, 20.4, 18.7, 17.1, 16.5, 14.7, 12.4]
                },
               ]
    });
}    
    