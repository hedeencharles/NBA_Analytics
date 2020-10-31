//////////////////////////////////////////////////////////////////////////////////////////
// Loading APIs
//////////////////////////////////////////////////////////////////////////////////////////

// Load Data then call functions
// d3.json('http://127.0.0.1:5000/api/global ').then(function(result,error) {

  let ws_birthplace = result
  heat_Map(ws_birthplace);
})

// Load Data then call functions
// d3.json('http://127.0.0.1:5000/api/global ').then(function(result,error) {

  let ws_birthplace = result
  heat_Map(ws_birthplace);
})

var myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 4
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);


const url = 'mongodb://localhost:27017';

const mongodb = require('mongodb');

const MongoClient = mongodb.MongoClient;

MongoClient.connect(url, (err, client) => {
    if (err) {
        throw err;
        return;
    }

    console.log('Database connection successful');

    // This objects holds the refrence to the db
    const db = client.db(nba_players_db);

    client.close();


  var heatArray = [];

  for (var i = 0; i < data.Birth_Place.length; i++) {
    var location = data[i].WS;

    if (WS) {
      heatArray.push([data[i].latitude, data[i].longitude]);
    }
  }

console.log(heatArray);


  var heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 35
  }).addTo(myMap);

});
