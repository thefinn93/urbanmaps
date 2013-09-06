function getinfo(id) {
    $.get("/info?id=" + id).success(function(data) {
        $("#infobox").text(data).show(250);
        }
    );
}

var map = L.map('map').setView([47.7, -122.3], 10);
L.tileLayer(tileurl, {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);
