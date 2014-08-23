import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;

// stdin, stdout and pipe also works!

class stdinRead 
{
    static String infile;    // = "dat3.txt";
    static String outfile;   // = "dat3.out.txt";

    public static void main( String args[] )
    {
        try 
        {
            File    fin;
            File    fot;
            // FileInputStream    fis = null;
            // FileOutputStream   fos = null;
            InputStream    fis = null;
            OutputStream   fos = null;

            if (args.length == 2)
            {
                infile  = args[0];
                outfile = args[1];
                fin = new File(infile);
                fot = new File(outfile);
                fis = new FileInputStream(fin);
                fos = new FileOutputStream(fot, true);
            }
            else
            {
                fis = System.in;            
                fos = System.out;
            }

            InputStreamReader  isr = new InputStreamReader(fis, "UTF-8");
            BufferedReader     fbr = new BufferedReader(isr);
 
            OutputStreamWriter osr = new OutputStreamWriter(fos, "UTF-8");
            BufferedWriter     fbw = new BufferedWriter(osr);

            String str;
 
            while ((str = fbr.readLine()) != null)
            {
                System.out.println(str);
                fbw.write("out: " + str + '\n'); 
            }
            fbr.close();
            fbw.close();
        } 
        catch (UnsupportedEncodingException e) 
        {
            System.out.println("err2: " + e.getMessage());
        } 
        catch (IOException e) 
        {
            System.out.println("err1: " + e.getMessage());
        }
        catch (Exception e)
        {
            System.out.println("err0: " + e.getMessage() + e.toString());
        }
    }
}

//-----------------------------------------------------
// edit ~ , add "set modeline"
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
// xxx: tabstop=4           shiftwidth=4 softtabstop=4
//-----------------------------------------------------

