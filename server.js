var PORT_NUMBER = process.env.PORT || 5000;

// Dependencies
var async = require('async');
var bodyParser = require('body-parser');
var express = require('express');
var fs = require('fs');
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
  response.render('index.html');
});

app.get('/champ', function(request, response) {
  champJSON = null;

  async.parallel([
    function(callback) {
      fs.readFile('dataset/stats-by-champion/' + request.path + '.json',
                  function(err, data) {
        if (err) {
          console.log(err);
          return;
        }
        champJSON = data;
        response.send(champJSON);
      });
    }
  ], function(error) {
  });
});


// SERVER SETUP ================================================================
var server = require('http').Server(app);
server.listen(PORT_NUMBER, function() {
  console.log('Listening to port ' + PORT_NUMBER);
});
