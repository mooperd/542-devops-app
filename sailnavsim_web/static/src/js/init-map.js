var rulerOpts = {
    lengthUnit: {
        factor: 0.539956803,
        display: "NM",
        decimal: 1,
        label: "Distance"
    },
    angleUnit: {
        factor: null,
        display: "&deg;",
        decimal: 1,
        label: "Course"
    }
};

var wxWindLayer = L.tileLayer('https://8bitbyte.ca/sailnavsim/wxtile.php?z={z}&x={x}&y={y}&t=wind');
var wxWindGustLayer = L.tileLayer('https://8bitbyte.ca/sailnavsim/wxtile.php?z={z}&x={x}&y={y}&t=wind_gust');
var wxOceanCurrentLayer = L.tileLayer('https://8bitbyte.ca/sailnavsim/wxtile.php?z={z}&x={x}&y={y}&t=ocean_current');
var wxSeaIceLayer = L.tileLayer('https://8bitbyte.ca/sailnavsim/wxtile.php?z={z}&x={x}&y={y}&t=sea_ice');
var wxWaveHeightLayer = L.tileLayer('https://8bitbyte.ca/sailnavsim/wxtile.php?z={z}&x={x}&y={y}&t=wave_height');
var wsUri = 'wss://8bitbyte.ca/sailnavsim/snsws/v1/ws';
var ws = null;

// createMap([35.717121, 140.917724], 7)
function createMap(centre_coordinates, zoom) {
    return L.map('mapid').setView(centre_coordinates, zoom);
}

function configureMap(map) {
    L.control.scale().addTo(map);
    L.control.ruler(rulerOpts).addTo(map);
    L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
        attribution: 'Map tiles by <a href="https://stamen.com/">Stamen Design</a>, under <a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="https://www.openstreetmap.org/">OpenStreetMap</a>, under <a href="https://www.openstreetmap.org/copyright">ODbL</a>.',
    }).addTo(map);
}
