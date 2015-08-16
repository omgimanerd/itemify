var PORT_NUMBER = process.env.PORT || 5000;

// RIOT API key(?) and URL setup
//var secret = require('secret.js');
var API_KEY = '';
var API_URL = 'https://na.api.pvp.net';

// Dependencies
var async = require('async');
var bodyParser = require('body-parser');
var express = require('express');
var swig = require('swig');
var https = require('https');

var app = express();

// CONFIGURATION ===============================================================
app.engine('html', swig.renderFile);

app.set('port', PORT_NUMBER);
app.set('view engine', 'html');

app.use('/bower_components',
        express.static(__dirname + '/bower_components'));
app.use('/static',
        express.static(__dirname + '/static'));
app.use(bodyParser.urlencoded({ extended: true }));
// CONFIGURATION ===============================================================


// ROUTING =====================================================================
app.get('/', function(request, response) {
  var championIDs;
  https.get(API_URL + '/api/lol/na/v1.2/champion?api_key=' + API_KEY, function(response){
  var data = '';
  response.on('data', function(chunk){
    data += chunk;
  });
  response.on('end',function(){
    championIDs = JSON.parse(data);
    console.log(championIDs);
  })
});
  //console.log(championIDs);
  response.render('index.html', {championIDs:championIDs});
});
// ROUTING =====================================================================


// SERVER SETUP ================================================================
var server = require('http').Server(app);
server.listen(PORT_NUMBER, function() {
  console.log('Listening to port ' + PORT_NUMBER);
});
// SERVER SETUP ================================================================