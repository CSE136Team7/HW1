import java.util.*;
import java.io.*;

class htmlform {

  public static void main (String args[])
  {
    //
    // Print the required cgi header
    //
    System.out.println("Content-Type: text/html\n\n");

    //
    // Create the Top of the returned HTML page
    //
    String Top = "<!doctype html>\n"
        + "<head>\n"
        + "<meta charset='UTF-8'>\n"
        + "<title>\n"
        + "java src"
        + "\n"
        + "</title>\n"
        + "</head>\n"
        + "<body>\n";
          System.out.println(Top);
    

        System.out.println("<hr>");
    System.out.println("<h1>POST FORM</h1>");
        System.out.println("<form action='getdata.cgi' method='post'>");
        System.out.println("<label>Name: <input type='text' name='username'></label>");
        System.out.println(" <br>");
        System.out.println("<label>Password: <input type='password' name='password'></label>");
        System.out.println("<br>");
        System.out.println("<label>Magic Number: <input type='text' name='magicnum' size='2' maxlength='2'></label>");
        System.out.println("<br>");


        System.out.println("<br>");
        System.out.println("<input type='hidden' name='test' value='it'>");
        System.out.println("<input type='submit' value='send'>");
        System.out.println("</form>");

        System.out.println("<hr>");

        System.out.println("<h1>GET FORM</h1>");
        System.out.println("<form action='getdata.cgi' method='get'>");
        System.out.println("<label>Name: <input type='text' name='username'></label>");
        System.out.println(" <br>");
        System.out.println("<label>Password: <input type='password' name='password'></label>");
        System.out.println("<br>");
        System.out.println("<label>Magic Number: <input type='text' name='magicnum' size='2' maxlength='2'></label>");
        System.out.println("<br>");




        System.out.println("<br>");
        System.out.println("<input type='hidden' name='test' value='it'>");
        System.out.println("<input type='submit' value='send'>");
        System.out.println("</form>");



      //
      // Create the Bottom of the returned HTML page to close it cleanly.
      //
      System.out.println("</body>\n</html>\n");

  }

}
