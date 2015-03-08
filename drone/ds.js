var express = require('express');
var app = express();

var turnSpeed = .5;
var moveSpeed = .5;
var vertSpeed = .5;

app.get('/takeoff', function(req, res) {
	gc('Taking off.').takeoff();
});

app.get('/tr', function(req, res) {
	gc('Turning right').clockwise(turnSpeed);
});
app.get('/tl', function(req, res) {
	gc('Turning left').counterClockwise(turnSpeed);
});
app.get('/mr', function(req, res) {
	gc('Moving right').right(moveSpeed);
});
app.get('/ml', function(req, res) {
	gc('Moving left').left(moveSpeed);
});
app.get('/u', function(req, res) {
	gc('Moving up').up(vertSpeed);
});
app.get('/d', function(req, res) {
	gc('Moving down').down(vertSpeed);
});
app.get('/f', function(req, res) {
	gc('Moving forward').front(moveSpeed);
});
app.get('/b', function(req, res) {
	gc('Moving backward').back(moveSpeed);
});

app.get('/panic', function(req, res) {
	gc('Panicking!').land();
});

app.get('/land', function(req, res) {
	var client = gc('Landing');
	client.stop();
	client.land();
});

// default case
app.get('*', function(req, res) {
	gc('Received unknown command. Halting.').stop();
});

function gc(out) {
	console.log(out);
	return getClient();
}

function getClient() {
	var arDrone = require('ar-drone');
	var client = arDrone.createClient();

	client.stop();
	return client;
}

app.listen(3000);
