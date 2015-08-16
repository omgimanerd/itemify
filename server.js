var PORT_NUMBER = process.env.PORT || 5000;

// RIOT API key(?) and URL setup
//var secret = require('secret.js');
var API_KEY = process.env.API_KEY || require('./API_KEY').API_KEY;
var API_URL = 'https://na.api.pvp.net';

console.log();

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


// ROUTING =====================================================================
app.get('/', function(request, response) {
  var data = null;

  async.parallel([
    function(callback) {
      https.get(API_URL + '/api/lol/na/v1.2/champion?api_key=' + API_KEY,
                function(res) {
        res.on('data', function(chunk) {
          data += chunk;
        });
        res.on('end',function() {
          callback();
        });
      });
    }
  ], function(error) {
    response.render('index.html', {
      championIDs: data
    });
  });
});


// SERVER SETUP ================================================================
var server = require('http').Server(app);
server.listen(PORT_NUMBER, function() {
  console.log('Listening to port ' + PORT_NUMBER);
});
