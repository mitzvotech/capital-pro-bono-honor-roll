var express = require('express');
var mongoose = require('mongoose');

var app = express();
var Record = require('./record')

mongoose.connect('mongodb://localhost/cpbhr');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function callback () {
	console.log("Successfully connected to mongodb.")
});

app.get('/', function(req, res){
	res.send('Hello World!');
});

app.listen(3000, 'localhost', function() {
	console.log('Express server listening on port 3000')
});