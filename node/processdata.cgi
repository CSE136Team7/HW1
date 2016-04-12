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



  for (var i=0; i<magicnumber; i++) {
    if(username == "" || password == "" || magicnum < 0 || isNaN(magicnum)){
      console.log("There was an error with your input");
    }else{
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

    for (var i=0; i<magicnumber; i++) {
      if(username == "" || password == "" || magicnum < 0 || isNaN(magicnum)){
        console.log("There was an error with your input");
      }else{
      console.log("<!DOCTYPE html> <html lang='en'> <head>  <title>Processdata form node</title></head><body > <h1> Hello " + username + "with a password of " + password+"!<br> </h1></body></html>");
      }
    }
  });
}
