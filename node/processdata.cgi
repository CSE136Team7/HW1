#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);

var data = '';
process.stdin.on('data', function(dt) {
 		data+=dt;
});

process.stdin.on('end', function() {
  var d = querystring.parse(data)
 	printBody(d.username, d.password, d.magicnum);
});
