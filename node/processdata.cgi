#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);
//console.log("Content-Type: text/html;charset=utf-8\n\n");
var obj = process.env;
 var b = obj['QUERY_STRING']; 
 console.log(b + '<br>');

var res = b.split("&");
var username = res[0].split("=")[1];
var password = res[1].split("=")[1];
var magicnumber = res[2].split("=")[1];




//console.log(a);
var s='<h1> Hello ' + username + ' with a password of ' + password+ '<br> </h1>';
for (var i=0; i<magicnumber; i++) {
console.log(s);
}
//var username = document.getElementsByName("username")[0].value;


