#!/usr/bin/node

document.write("Content-Type: text/html;charset=utf-8\n\n") 
var username = document.forms['post']['username'].value;

document.write("<h1>Hello " + username +" with a password of </h1></br>");
