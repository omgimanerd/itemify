/**
 * This handles all request to Riot's API.
 */

var https = require('https');

function Rest() {

}

/**
 * The api key to use for querying Riot.
 */
Rest.API_KEY = process.env.API_KEY || require('./API_KEY').API_KEY;

/**
 * The base URL from which we will construct all queries from.
 */
Rest.API_URL = 'https://na.api.pvp.net';

Rest.prototype.getItems = function(callback) {
});
