#!/usr/bin/node

function main1(){
   
var username = document.forms["post"]["usernamename"].value;
   
var myWindow = window.open("", "_self");
myWindow.document.write("<h1>Hello " + username +" with a password of </h1></br>");

}
 
 main1();
