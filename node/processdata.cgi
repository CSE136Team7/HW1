#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);
if (process.env.REQUEST_METHOD==='GET') {
  var obj = process.env;
   var b = obj['QUERY_STRING'];


  var res = b.split("&");
  var username = res[0].split("=")[1];
  var password = res[1].split("=")[1];
  var magicnumber = res[2].split("=")[1];


  if(!username || !password || magicnumber < 0 || isNaN(magicnumber) ||!magicnumber){
      console.log("<!DOCTYPE html> <html lang='en'> <head>  <title>Processdata form node</title></head><body ><h1>There was an error with your input</h1></body></html>");
    }else{
      for (var i=0; i<magicnumber; i++) {
          console.log("<!DOCTYPE html> <html lang='en'> <head>  <title>Processdata form node</title></head><body > <h1> Hello " + username + "with a password of " + password+ "!<br> </h1></body></html>");
      }
  }
}
else if(process.env.REQUEST_METHOD==='POST'){
	var data = '';
	process.stdin.on('data', function(chunk) {
		data+=chunk;
	});
  process.stdin.on('end', function() {
    var res = data.split("&");
    var username = res[0].split("=")[1];
    var password = res[1].split("=")[1];
    var magicnumber = res[2].split("=")[1];
    if(!username || !password || magicnumber < 0 || isNaN(magicnumber) ||!magicnumber){
      console.log("<!DOCTYPE html> <html lang='en'> <head>  <title>Processdata form node</title></head><body ><h1>There was an error with your input</h1></body></html>");
      }else{
        for (var i=0; i<magicnumber; i++) {
          console.log("<!DOCTYPE html> <html lang='en'> <head>  <title>Processdata form node</title></head><body > <h1> Hello " + username + "with a password of " + password+"!<br> </h1></body></html>");
          }
    }
  });
}
