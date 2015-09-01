var PORT_NUMBER = process.env.PORT || 5000;

// DEPENDENCIES
var async = require('async');
var bodyParser = require('body-parser');
var express = require('express');
var fs = require('fs');
var morgan = require('morgan');
var swig = require('swig');
var https = require('https');

var Util = require('./server/Util');

var app = express();

// CONFIGURATION
app.engine('html', swig.renderFile);

app.set('port', PORT_NUMBER);
app.set('view engine', 'html');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(morgan('combined'));
app.use('/bower_components',
        express.static(__dirname + '/bower_components'));
app.use('/builds',
        express.static(__dirname + '/dataset/builds'));
app.use('/build_images',
        express.static(__dirname + '/dataset/build_images'));
app.use('/static',
        express.static(__dirname + '/static'));

// ROUTING
app.get('/', function(request, response) {
  response.render('index.html');
});

app.get('/about', function(request, response) {
  response.render('about.html');
});

app.get('/champion', function(request, response) {
  var champion = Util.getNormalizedChampionName(request.query.champion);
  fs.readFile('dataset/builds/' + champion + '.json',
              function(err, data) {
    if (err) {
      response.render('index.html', {
        error: 'Champion not found. Try a different query.'
      });
      return;
    }
    response.render('champion.html', {
      champion: champion,
      data: JSON.parse(data),
      displayOrder: ['Starting Items', 'Boots', 'Jungle Items', 'Endgame Items',
                     'Elixirs']
    });
  });
});

app.get('/how-to-use', function(request, response) {
  response.render('how-to-use.html');
});

// SERVER SETUP
var server = require('http').Server(app);
server.listen(PORT_NUMBER, function() {
  console.log('Listening to port ' + PORT_NUMBER);
});
