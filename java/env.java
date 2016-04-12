import java.util.*;
import java.io.*;

class env {

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
          System.out.println("Hello World from Java @" + new Date());
    

    System.out.println("<hr>");



        Map<String, String> env = System.getenv();
        int sindex = 0, bindex = 0;

        for (String envName : env.keySet()) {
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
        for (int bi = 0; bi < bindex; bi++)
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
        for (int si = 0; si < sindex; si++)
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


      //
      // Create the Bottom of the returned HTML page to close it cleanly.
      //
      System.out.println("</body>\n</html>\n");

  }

}
