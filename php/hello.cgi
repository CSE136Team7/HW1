#!/usr/bin/php
<?php
echo "Content-type: text/html \n\n";
# function generateRandomColor(){
  $array = array( "aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow");
  $color = $array[array_rand($array)];
  if ($color == $array[1] ||$color == $array[2]||$color == $array[4]||$color == $array[8] ||$color == $array[10]){
    $font_color = "white";
  }
  # return $array[array_rand($array)];
# }
# $color = generateRandomColor();

echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>Hello page in PHP</title>
      </head>
      <body style='background-color:$color; color:$font_color'>
        <h1>Hello World from PHP @ " .date("Y/m/d"). "</h1>
      </body>
      </html>";
?>
