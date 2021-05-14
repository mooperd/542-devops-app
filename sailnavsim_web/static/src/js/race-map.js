function overlayTileChange() {
    wxWindLayer.remove();
    wxWindGustLayer.remove();
    wxOceanCurrentLayer.remove();
    wxSeaIceLayer.remove();
    wxWaveHeightLayer.remove();
    var overlayTile = document.getElementById("overlayTile").value;
    if (overlayTile == "wind") {
        wxWindLayer.addTo(mymap);
    } else if (overlayTile == "wind_gust") {
        wxWindGustLayer.addTo(mymap);
    } else if (overlayTile == "ocean_current") {
        wxOceanCurrentLayer.addTo(mymap);
    } else if (overlayTile == "sea_ice") {
        wxSeaIceLayer.addTo(mymap);
    } else if (overlayTile == "wave_height") {
        wxWaveHeightLayer.addTo(mymap);
    }
}
