var express = require('express');
var app = express();

var turnSpeed = .2;
var moveSpeed = .2;
var vertSpeed = .2;

app.get('/takeoff', function(req, res) {
	gc('Taking off.', res)
});

app.get('/tr', function(req, res) {
	gc('Turning right', res)

});
app.get('/tl', function(req, res) {
	gc('Turning left', res)

});
app.get('/mr', function(req, res) {
	gc('Moving right', res)

});
app.get('/ml', function(req, res) {
	gc('Moving left', res)

});
app.get('/u', function(req, res) {
	gc('Moving up', res)

});
app.get('/d', function(req, res) {
	gc('Moving down', res)

});
app.get('/f', function(req, res) {
	gc('Moving forward', res)

});
app.get('/b', function(req, res) {
	gc('Moving backward', res)

});

app.get('/panic', function(req, res) {
	gc('Panicking!', res)

});

app.get('/land', function(req, res) {
	gc('Landing', res);

});

// default case
app.get('*', function(req, res) {
	gc('Received unknown command. Halting.', res)

});

function gc(out, response) {
	console.log(out);
	response.sendStatus(200);
}

function diff(drone) {
	drone.up(vertSpeed);
	drone.after(10000,function(){
		this.stop();
	});
}

app.listen(3000);
