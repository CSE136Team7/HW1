#!/usr/bin/php
<?php
echo "Content-type: text/html \n\n";
echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>process data in PHP</title>
      </head>
      <body>";
        if($_SERVER['REQUEST_METHOD']=="GET"){
          parse_str($_SERVER['QUERY_STRING']);
          for($i = 0; $i<$magicnum;$i++){
          echo  "<h1>Hello ".username." with a password of  ".$password." !</h1>";
          }
        }

        if($_SERVER['REQUEST_METHOD']=="POST") {
          while($f = fgets(STDIN)){
            $string=  $f;
          }
          parse_str($string);
          for($j = 0; $j<$magicnum;$j++){
          echo "<h1>Hello ".$username." with a password of  ".$password." !</h1>";
          }
        }

      echo "</body>
      </html>";
?>
