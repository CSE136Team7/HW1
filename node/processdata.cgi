#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);

process.stdin.resume();
process.stdin.setEncoding('utf8');
var data = '';
	process.stdin.on('data', function(chunk) {
		data+=chunk;
	});

	process.stdin.on('end', function() {
		var d = querystring.parse(data);
		printBody(d.username, d.password, d.magicnum);
		console.log('hello there');
	});


var obj = process.env;
 var b = obj['QUERY_STRING']; 
 

var res = b.split("&");
var username = res[0].split("=")[1];
var password = res[1].split("=")[1];
var magicnumber = res[2].split("=")[1];



var s='<h1> Hello ' + username + ' with a password of ' + password+ '<br> </h1>';
for (var i=0; i<magicnumber; i++) {
console.log(s);
}

