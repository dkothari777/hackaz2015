var express = require('express');
var app = express();

var turnSpeed = .2;
var moveSpeed = .2;
var vertSpeed = .2	;

var c;

app.get('/takeoff', function(req, res) {
	var arDrone = require('ar-drone');
	var client = arDrone.createClient();
	c = client;

	gc('Taking off.').takeoff();
	res.sendStatus(200);
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
	res.sendStatus(200);
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
	c.stop();
	return c;
}

app.listen(3000);
