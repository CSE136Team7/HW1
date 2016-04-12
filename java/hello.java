import java.util.*;
import java.io.*;

class hello {

  public static void main (String args[])
  {
    //
    // Print the required cgi header
    //
    System.out.println("Content-Type: text/html\n\n");

    //
    // Create the Top of the returned HTML page
    //
    String Top = "<html>\n"
        + "<head>\n"
        + "<title>\n"
        + "java src"
        + "\n"
        + "</title>\n"
        + "<style>\n";
        
        // Generate a number between 1 and 16
        Random rand = new Random();
        int r = rand.nextInt(16);
    switch(r){
          case 0:
            Top += "body { background: aqua; color: black; }\n"; break;
          case 1:
            Top += "body { background: black; color: white; }\n"; break;
          case 2:
            Top += "body { background: blue; color: white; }\n"; break;
          case 3:
            Top += "body { background: fuchsia; color: black; }\n"; break;
          case 4:
            Top += "body { background: gray; color: black; }\n"; break;
          case 5:
            Top += "body { background: green; color: white; }\n"; break;
          case 6:
            Top += "body { background: lime; color: black; }\n"; break;
          case 7:
            Top += "body { background: maroon; color: white; }\n"; break;
          case 8:
            Top += "body { background: navy; color: white; }\n"; break;
          case 9:
            Top += "body { background: olive; color: black; }\n"; break;
          case 10:
            Top += "body { background: purple; color: white; }\n"; break;
          case 11:
            Top += "body { background: red; color: white; }\n"; break;
          case 12:
            Top += "body { background: silver; color: black; }\n"; break;
          case 13:
            Top += "body { background: teal; color: white; }\n"; break;
          case 14:
            Top += "body { background: white; color: black; }\n"; break;
          case 15:
            Top += "body { background: yellow; color: black; }\n"; break;

        }




        Top += "</style>\n" 
        + "</head>\n"
        + "<body>\n";
          System.out.println(Top);
          System.out.println("Hello World from Java @" + new Date());
    

    System.out.println("<hr>");



        Map<String, String> env = System.getenv();
        int sindex = 0, bindex = 0;

        for (String envName : env.keySet() {
            if (envName.startsWith("HTTP") || envName.startsWith("REQUEST") || envName.startsWith("REMOTE") || envName.startsWith("QUERY") || envName.startsWith("I")) {
                bindex++;
            }
            else 
                sindex++;
        }
        
        String server[] = new String[sindex];
        String browser[] = new String[bindex];
        bindex = 0;
        sindex = 0;
        for (String envName : env.keySet())
        {
            if (envName.startsWith("HTTP") || envName.startsWith("REQUEST") || envName.startsWith("REMOTE") || envName.startsWith("QUERY") || envName.startsWith("I"))
            {
              browser[bindex] = envName;
              bindex++;
            }
            else
            {
              server[sindex] = envName;
              sindex++;
            }
        }
        Arrays.sort(server);
        Arrays.sort(browser);
        
        System.out.println("<h1>Browser</h1>");
        System.out.println("<table>");
        for (int bi = 0; bi <= bindex; bi++)
        {
            System.out.println("<tr>");
            System.out.println("<td>");
            System.out.format("<strong>%s</strong>", browser[bi]);
            System.out.println("</td>");
            System.out.println("<td>");
            System.out.format("%s%n", env.get(browser[bi]));
            System.out.println("</td>");
            System.out.println("</tr>");
        }
        System.out.println("</table>");

        System.out.println("<h1>Server</h1>");  
        System.out.println("<table>");
        for (int si = 0; si <= sindex; si++)
        {
            System.out.println("<tr>");
            System.out.println("<td>");
            System.out.format("<strong>%s</strong>", server[si]);
            System.out.println("</td>");
            System.out.println("<td>");
            System.out.format("%s%n", env.get(server[si]));
            System.out.println("</td>");
            System.out.println("</tr>");
        }
        System.out.println("</table>");




 
    System.out.println("<h1>Form Test</h1>");
        System.out.println("<hr>");
        System.out.println("<form action='hello.cgi' method='post'>");
        System.out.println("<label>Name: <input type='text' name='username'></label>");
        System.out.println(" <br>");
        System.out.println("<label>Password: <input type='password' name='password'></label>");
        System.out.println("<br>");
        System.out.println("<label>Magic Number: <input type='text' name='magicnum' size='2' maxlength='2'></label>");
        System.out.println("<br>");
        System.out.println("<label>Magic Number: <input type='text' name='magicnum2' size='2' maxlength='2'></label>");

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
