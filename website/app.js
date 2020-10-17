var express = require('express');

var port = 8888;

var app = express();

app.use(express.static(__dirname + '/public'));

app.listen(port, function() {
    console.log(`Listening on port ${port}`);
});