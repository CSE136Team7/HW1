#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header + '<h1>Hello  with a password of </h1></br>');
//console.log("Content-Type: text/html;charset=utf-8\n\n");
var username = process.env.REQUEST_METHOD==='GET';

console.log(username);
//var username = document.getElementsByName("username")[0].value;


