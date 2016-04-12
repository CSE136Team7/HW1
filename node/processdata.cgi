#!/usr/bin/node

function main2(){
try {
var usernamelist = document.getElementsByName("username");

var username = "";
var i;
for (i = 0; i < usernamelist.length ;i++) {
   username += usernamelist.elements[i].value + "<br>";
   
var passwordlist = document.getElementsByName("password");

var password = "";
var i;
for (i = 0; i < passwordlist.length ;i++) {
   password += passwordlist.elements[i].value + "<br>";
   
var magicnum = document.getElementsByName("magicnum");
}
catch(err) {
   console.log("<p>There was an error with your input: </p>" + err);
}
//var s = "<h1>Hello " + username +" with a password of " + password +"</h1></br>";
//s = s * magicnum1;
else {
   
var myWindow = window.open("", "_self");
myWindow.document.write("<h1>Hello " + username +" with a password of " + password+ "</h1></br>");

}
}
 
 main2();
