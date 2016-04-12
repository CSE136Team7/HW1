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
//var a = Object.getOwnPropertyNames(obj);
console.log(username  + '<br>');
console.log(password  + '<br>');
console.log(magicnumber  + '<br>');



//console.log(a);
var s='Hello ' + username + ' with a password of ' + password;
s=s*magicnumber;
console.log(s);
//var username = document.getElementsByName("username")[0].value;


