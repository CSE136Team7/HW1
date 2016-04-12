#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);


var ReadableStream = Object.getPrototypeOf(process.stdin);
console.log('readable:' + ReadableStream[0]);


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


/*
process.stdin('data', function(chunk) {
 process.stdout.write('data: ' + chunk);
 data++;
});
*/

process.stdin.on('readable', function() {
  var chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write(chunk);
  }
});

process.stdin.on('end', function() {
  process.stdout.write('end');
});




