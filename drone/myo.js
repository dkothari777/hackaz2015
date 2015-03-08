var Myo = require('myo');
var myMyo = Myo.create();

myMyo.on('fist', function(edge){
    if(!edge) return;
    //fly up
    else {
        var conn = null;
        conn = new XMLHttpRequest();
        conn.open("GET", "192.168.1.3:3000/u", false);
        conn.send(null);
    }
});

myMyo.on('relax', function(edge) {
    if(!edge) return;
    //drones hover
    else {
        var conn = null;
        conn = new XMLHttpRequest();
        conn.open("GET", "192.168.1.3:3000/stop", false);
        conn.send(null);
    }
});

myMyo.on('myo_tap', function(edge) {
    if(!edge) return;
    //fly down
    else {
        var conn = null;
        conn = new XMLHttpRequest();
        conn.open("GET", "192.168.1.3:3000/d", false);
        conn.send(null);
    }
});
