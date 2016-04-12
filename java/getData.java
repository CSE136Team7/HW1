import java.util.*;
import java.io.*;

class getData {

  public static String urlDecode(String in) {
    StringBuffer out = new StringBuffer(in.length());
          int i = 0;
          int j = 0;

          while (i < in.length())
          {
             char ch = in.charAt(i);
             i++;
             if (ch == '+') ch = ' ';
             else if (ch == '%')
             {
                ch = (char)Integer.parseInt(in.substring(i,i+2), 16);
                i+=2;
             }
             out.append(ch);
             j++;
          }
          return new String(out);
  }

public static boolean MethGet()
  {
     String RequestMethod = System.getProperty("cgi.request_method");
     boolean returnVal = false;

     if (RequestMethod != null)
     {
         if (RequestMethod.equals("GET") ||
             RequestMethod.equals("get"))
         {
             returnVal=true;
         }
     }
     return returnVal;
  }


  public static void main(String args[]) {

    System.out.println("Content-type: text/html\n\n");

    String top = "<!doctype html>\n"
          + "<meta charset='UTF-8'>\n"
          + "<title>\n"
          + "java src"
          + "\n"
          + "</title>\n"
          + "<body>\n";

    System.out.println(top);

    Hashtable<String, String> form_data = new Hashtable<String, String>();

    String inBuffer = "";

    if (MethGet()) {
        inBuffer = System.getProperty("cgi.query_string");
    }

   else{

    DataInput d = new DataInputStream(System.in);
    String line;
    try
    {
      while(d != null && (line = d.readLine()) != null)
      {
          inBuffer = inBuffer + line;
      }
    }
    catch (IOException ignored) { }
   }


    //
    //  Split the name value pairs at the ampersand (&)
    //
    StringTokenizer pair_tokenizer = new StringTokenizer(inBuffer,"&");

    while (pair_tokenizer.hasMoreTokens())
    {
        String pair = urlDecode(pair_tokenizer.nextToken());
        //
        // Split into key and value
        //
        StringTokenizer keyval_tokenizer = new StringTokenizer(pair,"=");
        String key = new String();
        String value = new String();
        if (keyval_tokenizer.hasMoreTokens())
          key = keyval_tokenizer.nextToken();
        else ; // ERROR - shouldn't ever occur
        if (keyval_tokenizer.hasMoreTokens())
          value = keyval_tokenizer.nextToken();
        else ; // ERROR - shouldn't ever occur
        //
        // Add key and associated value into the form_data Hashtable
        //
        form_data.put(key,value);
    }

    String username = form_data.get("username");
    String password = form_data.get("password");
    String magicNum = form_data.get("magicnum");

    int magicnum = Integer.parseInt(magicNum);

    for(int i = 0; i < magicnum; i++){
      System.out.println("<h1>Hello " + username + " with a password of " + password + "</h1>");
    }

    System.out.println("</body>\n</html>\n");
  }


}
