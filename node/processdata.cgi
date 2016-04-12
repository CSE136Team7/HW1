#!/usr/bin/node

var header ='Content-type: text/html\n\n';
console.log(header);

var qs = require('querystring');

function (request, response) {
    if (request.method === 'POST') {
        var body = '';

        request.on('data', function (data) {
            body += data;

            // Too much POST data, kill the connection!
            // 1e6 === 1 * Math.pow(10, 6) === 1 * 1000000 ~~~ 1MB
            if (body.length > 1e6)
                request.connection.destroy();
        });

        request.on('end', function () {
            var post = qs.parse(body);
            // use post['blah'], etc.
        });

        var username = post.username;
        var password = post.password;
        var magicNum = post.magicnum;

        console.log(username);
        console.log(password);
        console.log(magicNum);

        for(var i = 0; i < magicNum; i++){
          console.log("Hello " + username + " with a password of " + password);
        }

    } else {
      var obj = process.env;
       var b = obj['QUERY_STRING'];


      var res = b.split("&");
      var username = res[0].split("=")[1];
      var password = res[1].split("=")[1];
      var magicnumber = res[2].split("=")[1];



      var s='<h1> Hello ' + username + ' with a password of ' + password+ '<br> </h1>';
      for (var i=0; i<magicnumber; i++) {
      console.log(s);
      }
    }
}
