var liveBoatIconYellow = new L.Icon({
    iconUrl: './img/top-yellow.png',
    iconSize: [16, 35],
    iconAnchor: [16, 17.5],
    popupAnchor: [0, -25],
});
var liveBoatIcon = new L.Icon({
    iconUrl: './img/top-yellow.png',
    iconSize: [16, 35],
    iconAnchor: [8, 17.5],
    popupAnchor: [0, -20],
});
var liveBoatMarker = L.marker([0, 0], {
    icon: liveBoatIcon,
    rotationAngle: 0,
    rotationOrigin: "center"
});

var startMarker = L.circleMarker(
    [35.717, 140.888], {
        radius: 6,
        weight: 2,
        color: '#002080',
        fillColor: '#0040ff',
        fillOpacity: 0.1
    }).addTo(mymap);
var startMarkerL = L.circleMarker(
    [35.717, -219.112], {
        radius: 6,
        weight: 2,
        color: '#002080',
        fillColor: '#0040ff',
        fillOpacity: 0.1
    }).addTo(mymap);
var startMarkerR = L.circleMarker(
    [35.717, 500.888], {
        radius: 6,
        weight: 2,
        color: '#002080',
        fillColor: '#0040ff',
        fillOpacity: 0.1
    }).addTo(mymap);

var whiteIcon = new L.Icon({
    iconUrl: './img/white.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var whiteIconE = new L.Icon({
    iconUrl: './img/white_e.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var whiteIconD = new L.Icon({
    iconUrl: './img/white_d.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var yellowIcon = new L.Icon({
    iconUrl: './img/yellow.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var yellowIconE = new L.Icon({
    iconUrl: './img/yellow_e.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var yellowIconD = new L.Icon({
    iconUrl: './img/yellow_d.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var lightGreenIcon = new L.Icon({
    iconUrl: './img/light_green.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var lightGreenIconE = new L.Icon({
    iconUrl: './img/light_green_e.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var lightGreenIconD = new L.Icon({
    iconUrl: './img/light_green_d.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var darkGreenIcon = new L.Icon({
    iconUrl: './img/dark_green.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var darkGreenIconE = new L.Icon({
    iconUrl: './img/dark_green_e.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var darkGreenIconD = new L.Icon({
    iconUrl: './img/dark_green_d.png',
    iconSize: [32, 32],
    iconAnchor: [16, 26],
    popupAnchor: [0, -20],
});
var yellowIcon2 = new L.Icon({
    iconUrl: './img/yellow.png',
    iconSize: [20, 20],
    iconAnchor: [10, 17],
    popupAnchor: [0, -13],
});
var yellowIcon2E = new L.Icon({
    iconUrl: './img/yellow_e.png',
    iconSize: [20, 20],
    iconAnchor: [10, 17],
    popupAnchor: [0, -13],
});
var darkGreenIcon2 = new L.Icon({
    iconUrl: './img/dark_green.png',
    iconSize: [20, 20],
    iconAnchor: [10, 17],
    popupAnchor: [0, -13],
});
var darkGreenIcon2E = new L.Icon({
    iconUrl: './img/dark_green_e.png',
    iconSize: [20, 20],
    iconAnchor: [10, 17],
    popupAnchor: [0, -13],
});

startMarker.bindPopup("Race start position");
startMarkerL.bindPopup("Race start position");
startMarkerR.bindPopup("Race start position");

var finishPoly = L.polygon([
    [35.083666666667, 141.838],
    [35.267, 141.838],
    [35.267, 142.75466666667],
    [35.083666666667, 142.75466666667]
], {
    weight: 2,
    color: '#008020',
    fillColor: '#00ff40',
    fillOpacity: 0.1
}).addTo(mymap);
var finishPolyL = L.polygon([
    [35.083666666667, -218.162],
    [35.267, -218.162],
    [35.267, -217.24533333333],
    [35.083666666667, -217.24533333333]
], {
    weight: 2,
    color: '#008020',
    fillColor: '#00ff40',
    fillOpacity: 0.1
}).addTo(mymap);
var finishPolyR = L.polygon([
    [35.083666666667, 501.838],
    [35.267, 501.838],
    [35.267, 502.75466666667],
    [35.083666666667, 502.75466666667]
], {
    weight: 2,
    color: '#008020',
    fillColor: '#00ff40',
    fillOpacity: 0.1
}).addTo(mymap);

finishPoly.bindPopup("Finish anywhere (land or water) within box");
finishPolyL.bindPopup("Finish anywhere (land or water) within box");
finishPolyR.bindPopup("Finish anywhere (land or water) within box");