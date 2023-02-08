var map = new L.Map("myMap", {center: [40.633258,-8.659097],zoom: 15});

var osmUrl="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
var osmAttrib="Map data OpenStreetMap contributors";
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib});

function showCoordinates(e){
    var s = document.getElementById("coordinates");
    s.innerHTML = "Latitude, Longitude = "+e.latlng.lat+", "+e.latlng.lng;
}
 
var pontos = [
    L.marker([40.633258, -8.659097]),
    L.marker([40.642729, -8.747899]),
    L.marker([40.632584, -8.646519])
    ];

var reitoria = L.polygon(
    [ [40.63102, -8.65793], [40.63149, -8.65731],
    [40.63126, -8.65699], [40.63078, -8.65759] ],
    { color: "red" } );
reitoria.addTo(map);

var deti = L.polygon(
    [ [40.63321, -8.65927], [40.63280, -8.65912],
    [40.63280, -8.65928], [40.63321, -8.65911] ],
    { color: "red" } );
deti.addTo(map);
    
var grupo = new L.featureGroup(pontos);
map.fitBounds(grupo.getBounds());

var iconeUA = L.icon({ iconUrl: "images/ua.png" });
var bed_breakfast1 = L.icon({iconUrl: "images/bed_breakfast1.png"}); 
L.marker([40.633258, -8.659097], {icon: iconeUA}).bindPopup("LABI@DETI").addTo(map);
L.marker([40.632584, -8.646519], {icon: bed_breakfast1}).bindPopup("Casa").addTo(map);

for(let i in pontos) {
    pontos[i].addTo(map);
}

L.marker([40.633258, -8.659097]).bindPopup("LABI@DETI").addTo(map);
map.addLayer(osm);
map.on("click", showCoordinates);
