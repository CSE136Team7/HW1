#!/usr/bin/php
<?php
echo "Content-type: text/html \n\n";
echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>process data in PHP</title>
      </head>
      <body>";
      echo "i am here";
        if($_GET) {
          echo "i am here";
          for($i = 0; $i<$_GET["magicnum"];$i++){
            echo "i am there";
          echo  "<h1>Hello ".$_GET['username']." with a password of  ".$_GET['password']." !</h1>";
        }
        }

        if($_POST) {
          for($j = 0; $j<$_POST["magicnum"];$j++){
          echo "<h1>Hello ".$_POST['username']." with a password of  ".$_POST['password']." !</h1>";
        }
        }

      echo "</body>
      </html>";
?>
