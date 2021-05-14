function wsOpen() {
    ws.send(JSON.stringify({
        cmd: 'bdl',
        key: '8778615748e7d311a8f9302acd5faa23'
    }));
}

function wsClose() {
    updateLiveBoat(null);
    ws = null;
}

function wsMsg(event) {
    updateLiveBoat(JSON.parse(event.data));
}

function liveBoatModeClick() {
    var ch = document.getElementById("liveBoatMode").checked;
    if (ch == true) {
        ws = new WebSocket(wsUri)
        ws.onopen = function(event) {
            wsOpen()
        };
        ws.onclose = function(event) {
            wsClose()
        };
        ws.onmessage = function(event) {
            wsMsg(event)
        };
        ws.onerror = function(event) {
            ws.close()
        };
    } else {
        ws.close();
    }
}

function updateLiveBoat(boat) {
    if (boat == null) {
        liveBoatMarker.remove();
        liveBoatMarkerAdded = false;
        return;
    }
    liveBoatMarker.setLatLng(L.latLng(boat.lat, boat.lon));
    liveBoatMarker.setRotationAngle(boat.ctw);
    var tw_str = printAngleMag(boat.ctw, boat.stw);
    var og_str = printAngleMag(boat.cog, boat.sog);
    liveBoatMarker.bindPopup("<center><b>Captain Mooperd</b><br><i>--- LIVE ---</i></center><hr width=80% color=#c0c0c0><p align=right>Through Water: " + tw_str + "<br>Over Ground: " + og_str + "</p>");
    if (liveBoatMarkerAdded == false) {
        liveBoatMarker.addTo(mymap);
        liveBoatMarkerAdded = true;
    }
}
