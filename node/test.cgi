#!/usr/bin/node

var header ='Content-type: text/html\n\n';
var d = new Date();

var bgcolorlist=["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"];
var backgroundcolor=bgcolorlist[Math.floor(Math.random()*bgcolorlist.length)];

if (backgroundcolor==="black") {
  console.log(
    '<!doctype html>'
    +'<body style="color:white;">'
    +'</body>'
    +'</html>');
}

var body =
'<!doctype html>'
+'<head>'
+'<title>'
+'Hello world node'
+'</title>'
+'</head>'
+'<body style= "background-color:'+ backgroundcolor + ';">'
+'<h2 style="margin-bottom:20px"> Hello World from JavaScript @ ' + d + '</h2>'
+ '<hr>' 
+'<h2 align="center">Environment Variables</h2>'
+'</body>'
+'<html>';


console.log(header + body);

var obj = process.env;
var a =Object.getOwnPropertyNames(obj).sort();
a.forEach(function(val, idx, array) {
  console.log('<b>' + val + ': ' + '</b>'  + obj[val]+ '<br>');
}); 


console.log( '<!doctype html>'
+ '<hr style="margin-top:20px">'
+'<h3>Post Form</h3>'
+'<form id="postform" action="processdata.cgi" method="post">'
+'<label>Name: <input type="text" name="username"></label>'
+'<br>'
+'<label>Password: <input type="password" name="password"></label>'
+'<br>'
+'<label>Magic Number: <input type="text" name="magicnum" size="2" maxlength="2"></label>'
+'<br>'
+'<input type="hidden" name="test" value="it">'
+'<input type="submit" value="send">'
+'</form>'
+'<hr>'
+'<h3>Get Form</h3>'
+'<form id="getform" action="processdata.cgi" method="get">'
+'<label>Name: <input type="text" name="username"></label>'
+'<br>'
+'<label>Password: <input type="password" name="password"></label>'
+'<br>'
+'<label>Magic Number: <input type="text" name="magicnum" size="2" maxlength="2"></label>'
+'<br>'
+'<input type="hidden" name="test" value="it">'
+'<input type="submit" value="send">'
+'</form>'
+'</body>'
+'</html>');
