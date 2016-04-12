#!/usr/bin/php
<?php
echo "Content-type: text/html \n\n";
echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>process data in PHP</title>
      </head>
      <body>
        <h1>Hello ".$_GET["username"]." with a password of  ".$_GET["password"]." !</h1>
      </body>
      </html>";
?>
