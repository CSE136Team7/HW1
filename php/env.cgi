#!/usr/bin/php
<?php
 echo "Content-type: text/html \n\n";
 while ( ($fruit_name = current($_SERVER)) !== FALSE ) {
        echo key($_SERVER)."  ". (current($_SERVER)).'<br>';
       next($_SERVER);
}
echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>Hello page in PHP</title>
      </head>
      <body style='background-color:$color'>
        <h1>Hello World from PHP @ " .date("Y/m/d"). "</h1>
        <br>
        <br>

      </body>
      </html>";
?>
