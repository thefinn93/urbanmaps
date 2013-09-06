function getinfo(id) {
    $.get("/info?id=" + id).success(function(raw) {
            var data = JSON.parse(raw)[0]['fields']
            var table = $("<table>")
                .append($("<tr>")
                    .append($("<td>").attr("colspan","2")
                        .append($("<b>")
                            .append($("<center>")
                                .text(data['title'])
                                )
                            )
                        )
                    );
            for(var key in data) {
                if(key != 'title') {
                    table.append($("<tr>")
                        .append($("<td>").text(key))
                        .append($("<td>").text(data[key])
                        )
                    )
                }
            }
            
            $("#infobox").html(table).show(250);
        }
    );
}

var map = L.map('map').setView([47.7, -122.3], 10);
L.tileLayer(tileurl, {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);
