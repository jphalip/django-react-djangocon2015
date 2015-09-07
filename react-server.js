var http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
var reactRender = require('react-render');
var argv = require('yargs').argv;

require('babel/register');  // For the JSX and ES6 conversion

var ADDRESS = argv.host || '127.0.0.1';
var PORT = argv.port || 9009;

var app = express();
var server = http.Server(app);

app.use(bodyParser.json());

app.post('/', function(request, response) {
  console.log('[' + (new Date()).toISOString() + '] Render: ' + request.body.path);
  reactRender(request.body, function(err, html) {
    var response_error = null;
    if (err) {
      response_error = {
        type: err.constructor.name,
        message: err.message,
        stack: err.stack
      };
      console.log(err.message);
    }
    response.json({
      error: response_error,
      markup: html
    });
  });
});

server.listen(PORT, ADDRESS, function() {
  console.log('React render server listening at http://' + ADDRESS + ':' + PORT);
});