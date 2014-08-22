import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;


class fileOpen
{
    static String infile = "dat3.txt";

    public static void main( String args[] )
    {
        try 
        {
            File              fin = new File(infile);
            FileInputStream   fis = new FileInputStream(fin);
            InputStreamReader isr = new InputStreamReader(fis, "UTF-8");
            BufferedReader    fbr = new BufferedReader(isr);
 
            String str;
 
            while ((str = fbr.readLine()) != null)
            {
                System.out.println(str);
            }
            fbr.close();
        } 
        catch (UnsupportedEncodingException e) 
        {
            System.out.println(e.getMessage());
        } 
        catch (IOException e) 
        {
            System.out.println(e.getMessage());
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}

//-----------------------------------------------------
// edit ~ , add "set modeline"
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
// xxx: tabstop=4           shiftwidth=4 softtabstop=4
//-----------------------------------------------------

