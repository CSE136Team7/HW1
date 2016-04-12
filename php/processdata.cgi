#!/usr/bin/php
<?php
echo "Content-type: text/html \n\n";
echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>process data in PHP</title>
      </head>
      <body>";
       echo strcmp($_SERVER['REQUEST_METHOD'],"GET");
       echo strcmp($_SERVER['REQUEST_METHOD'],"get");
        if(strcmp($_SERVER['REQUEST_METHOD'],"get")==0){
          for($i = 0; $i<$_GET["magicnum"];$i++){
          echo  "<h1>Hello ".$_GET['username']." with a password of  ".$_GET['password']." !</h1>";
          }
        }

        if(strcmp($_SERVER['REQUEST_METHOD'],"post")==0) {
          for($j = 0; $j<$_POST["magicnum"];$j++){
          echo "<h1>Hello ".$_POST['username']." with a password of  ".$_POST['password']." !</h1>";
          }
        }

      echo "</body>
      </html>";
?>
