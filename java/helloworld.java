import java.util.*;
import java.io.*;

class helloworld {

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
    



      //
      // Create the Bottom of the returned HTML page to close it cleanly.
      //
      System.out.println("</body>\n</html>\n");

  }

}
