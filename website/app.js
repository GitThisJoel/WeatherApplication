var express = require('express');
const {spawn} = require('child_process');

var port = 8888;

var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/loc/:lat-:long', (req, res) => {
    console.log(req.params);
    lat = req.params["lat"];
    long = req.params["long"];

    var dataToSend;
    const python = spawn('python3', ['src/TestWeatherFetching.py']);
    python.stdout.on('data', function(data) {
        console.log('Pipe data from python script');
        dataToSend = data.toString();
    });
    python.on('close', (code) => {
        console.log(`Child process close all stdio with code ${code}`);
        res.send(dataToSend);
    })
});

app.listen(port, function() {
    console.log(`Listening on port ${port}`);
});