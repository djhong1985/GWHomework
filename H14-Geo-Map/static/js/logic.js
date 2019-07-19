// Store our API endpoint inside queryUrl
// var queryUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson';
// var queryUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson';
var queryUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';

d3.json(queryUrl, function(data) {
  createFeatures(data.features);
});

function getColor(mag){
  switch(parseInt(mag)){
      case 0: return '#b7f34d';
      case 1: return '#e1f34d';
      case 2: return '#f3db4d';
      case 3: return '#f3ba4d';
      case 4: return '#f0a76b';
      default: return '#f06b6b';
  }
}

function createFeatures(earthquakeData) {
  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place + 
      "</h3><hr><p>" + feature.properties.mag +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
  }
  
  function pointToLayer(feature, latlng) {
    return L.circleMarker(latlng,{
            stroke: false,
            fillOpacity: 0.75,
            color: "white",
            fillColor: getColor(feature.properties.mag),
            radius: feature.properties.mag*3
        });
  }

  var earthquakes = L.geoJSON(earthquakeData, {
  onEachFeature: onEachFeature,
  pointToLayer: pointToLayer,
  });

  createMap(earthquakes);
}

function createMap(earthquakes) {
  // Define streetmap and darkmap layers
  var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  });

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Street Map": streetmap,
    "Dark Map": darkmap
  };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Earthquakes: earthquakes
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [streetmap, earthquakes]
  });

  // Create a layer control Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

CreateLegend();
function CreateLegend(){
   var legend = L.control({position: "bottomright"});
   legend.onAdd = function(){
       var div = L.DomUtil.create("div","info legend");
       var labels = ["0-1","1-2","2-3","3-4","4-5","5+"];
       var legends = [];
       for(var i=0;i<labels.length;i++){
           legends.push("<li style=\"list-style-type:none;\"><div style=\"background-color: " + getColor(i) + "\">&nbsp;</div> " +
           "<div>" + labels[i] + "</div></li>");}
           div.innerHTML += "<ul class='legend'>" + legends.join("") + "</ul>";
           return div;
       };
       legend.addTo(myMap);
}
}