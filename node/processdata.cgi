#!/usr/bin/node

var header ='Content-type: text/html\n\n';

//console.log("Content-Type: text/html;charset=utf-8\n\n");
var username = request.post.form['username'].value;

console.log(header + '<h1>Hello  with a password of </h1></br>');
