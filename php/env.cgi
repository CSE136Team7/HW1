#!/usr/bin/php
<?php
 echo "Content-type: text/html \n\n";

echo "<!DOCTYPE html>
      <html lang='en'>
      <head>
        <title>Environmental from PHP</title>
      </head>
      <body style='background-color:$color'>
        <br>
        <h1>Browser Variables</h1>
        <table>
        <tr>
          <td>HTTP_ACCEPT</td>
          <td>".$_SERVER['HTTP_ACCEPT']."</td>
        </tr>
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td>".$_SERVER['HTTP_ACCEPT_ENCODING']."</td>
        </tr>
        <tr>
          <td>HTTP_ACCEPT_LANGUAGE</td>
          <td>".$_SERVER['HTTP_ACCEPT_LANGUAGE']."</td>
        </tr>
        <tr>
          <td>HTTP_CONNECTION</td>
          <td>".$_SERVER['HTTP_CONNECTION']."</td>
        </tr>
        <tr>
          <td>HTTP_HOST</td>
          <td>".$_SERVER['HTTP_HOST']."</td>
        </tr>
        <tr>
          <td>HTTP_REFERER</td>
          <td>".$_SERVER['HTTP_REFERER']."</td>
        </tr>
        <tr>
          <td>HTTP_UPGRADE_INSECURE_REQUESTS</td>
          <td>".$_SERVER['HTTP_UPGRADE_INSECURE_REQUESTS']."</td>
        </tr>
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td>".$_SERVER['HTTP_USER_AGENT']."</td>
        </tr>
        <tr>
          <td>QUERY_STRING</td>
          <td>".$_SERVER['QUERY_STRING']."</td>
        </tr>
        <tr>
          <td>REMOTE_ADDR</td>
          <td>".$_SERVER['REMOTE_ADDR']."</td>
        </tr>
        <tr>
          <td>REMOTE_PORT</td>
          <td>".$_SERVER['REMOTE_PORT']."</td>
        </tr>
        <tr>
          <td>REQUEST_METHOD</td>
          <td>".$_SERVER['REQUEST_METHOD']."</td>
        </tr>
        <tr>
          <td>REQUEST_SCHEME</td>
          <td>".$_SERVER['REQUEST_SCHEME']."</td>
        </tr>
        <tr>
          <td>REQUEST_TIME</td>
          <td>".$_SERVER['REQUEST_TIME']."</td>
        </tr>
        <tr>
          <td>REQUEST_TIME_FLOAT</td>
          <td>".$_SERVER['REQUEST_TIME_FLOAT']."</td>
        </tr>
        <tr>
          <td>REQUEST_URI</td>
          <td>".$_SERVER['REQUEST_URI']."</td>
        </tr>


      </table>
      <br>
      <br>
      <h1>Server Variables</h1>

      <table>
      <tr>
        <td>argc</td>
        <td>".$_SERVER['argc']."</td>
      </tr>
      <tr>
        <td>argv</td>
        <td>".$_SERVER['argv']."</td>
      </tr>
      <tr>
        <td>CONTEXT_DOCUMENT_ROOT</td>
        <td>".$_SERVER['CONTEXT_DOCUMENT_ROOT']."</td>
      </tr>
      <tr>
        <td>CONTEXT_PREFIX</td>
        <td>".$_SERVER['CONTEXT_PREFIX']."</td>
      </tr>
      <tr>
        <td>DOCUMENT_ROOT</td>
        <td>".$_SERVER['DOCUMENT_ROOT']."</td>
      </tr>
      <tr>
        <td>GATEWAY_INTERFACE</td>
        <td>".$_SERVER['GATEWAY_INTERFACE']."</td>
      </tr>
      <tr>
        <td>PATH_TRANSLATED</td>
        <td>".$_SERVER['PATH_TRANSLATED']."</td>
      </tr>
      <tr>
        <td>PHP_SELF</td>
        <td>".$_SERVER['PHP_SELF']."</td>
      </tr>
      <tr>
        <td>SCRIPT_FILENAME</td>
        <td>".$_SERVER['SCRIPT_FILENAME']."</td>
      </tr>
      <tr>
        <td>SCRIPT_NAME</td>
        <td>".$_SERVER['SCRIPT_NAME']."</td>
      </tr>
      <tr>
        <td>SERVER_ADDR</td>
        <td>".$_SERVER['SERVER_ADDR']."</td>
      </tr>
      <tr>
        <td>SERVER_ADMIN</td>
        <td>".$_SERVER['SERVER_ADMIN']."</td>
      </tr>
      <tr>
        <td>SERVER_NAME</td>
        <td>".$_SERVER['SERVER_NAME']."</td>
      </tr>
      <tr>
        <td>SERVER_PORT</td>
        <td>".$_SERVER['SERVER_PORT']."</td>
      </tr>
      <tr>
        <td>SERVER_PROTOCOL</td>
        <td>".$_SERVER['SERVER_PROTOCOL']."</td>
      </tr>
      <tr>
        <td>SERVER_SIGNATURE</td>
        <td>".$_SERVER['SERVER_SIGNATURE']."</td>
      </tr>
      <tr>
        <td>SERVER_SOFTWARE</td>
        <td>".$_SERVER['SERVER_SOFTWARE']."</td>
      </tr>
      <tr>
        <td>REQUEST_TIME_FLOAT</td>
        <td>".$_SERVER['REQUEST_TIME_FLOAT']."</td>
      </tr>
      <tr>
        <td>REQUEST_URI</td>
        <td>".$_SERVER['REQUEST_URI']."</td>
      </tr>

    </table>

      </body>
      </html>";
?>
