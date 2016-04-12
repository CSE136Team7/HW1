#!/usr/bin/node

var header ='Content-type: text/html\n\n';
var d = new Date();

var bgcolorlist=["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"];
var backgroundcolor=bgcolorlist[Math.floor(Math.random()*bgcolorlist.length)];

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
+'<h2 align="center">Environment Variables</h2>';


console.log(header + body);

var obj = process.env;
var a =Object.getOwnPropertyNames(obj).sort();
var server = [];
var browser = [];
var sindex = 0;
var bindex = 0;
for (int i = 0; i < obj.length; i++){
    if (obj[i].startsWith("HTTP") || obj[i].startsWith("REQUEST") || obj[i].startsWith("REMOTE") || obj[i].startsWith("QUERY") || obj[i].startsWith("I")) {
        browser[bindex] = obj[i];
        bindex++;
    }
    else{
        server[sindex] = obj[i];
        sindex++;
    }
}

//a.forEach(function(val, idx, array) {
//  console.log('<b>' + val + ': ' + '</b>'  + obj[val]+ '<br>');
//}); 
 
console.log("<h1>Browser</h1>");
bindex = 0;
browser.forEach(function(val, idx, array) {
    console.log('<b>' + val + ': ' + '</b>' + browser[bindex] + '<br>');
    bindex++;
});
 
console.log("<h1>Server</h1>");
sindex = 0;
server.forEach(function(val, idx, array) {
    console.log('<b>' + val + ': ' + '<b>' + server[sindex] + '<br>');
    sindex++;
});

console.log("</body></html>");
