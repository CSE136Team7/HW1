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
          parse_str($_SERVER['QUERY_STRING']);
          echo $username;
          # for($j = 0; $j<$_POST["magicnum"];$j++){
          # echo "<h1>Hello ".$_POST['username']." with a password of  ".$_POST['password']." !</h1>";
          # }
        }

      echo "</body>
      </html>";
?>
