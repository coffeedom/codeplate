import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;


class fieldsRead
{
    static String infile = "datFields.txt";

    public static void main( String args[] )
    {
        try
        {
            File            inf = new File(infile);
            FileReader       fr = new FileReader(inf);
            BufferedReader  buf = new BufferedReader(fr);

            boolean eof = false;
            while (!eof)
            {
                System.out.println("------------------");
                String line = buf.readLine();
                if (line == null)
                {
                    eof = true;
                    continue;
                }
                String fields[] = line.trim().split("\\t");
                int numFields = fields.length;
                for (int i=0; i < numFields; i++)
                {
                    System.out.println("field[" + i + "] = " + fields[i]);
                }
            }
            buf.close();
            System.out.println("------------------");
        }
        catch (IOException e)
        {
            System.out.println("Error: " + e.toString());
        }

    }
}


//-----------------------------------------------------
// edit ~ , add "set modeline"
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
// xxx: tabstop=4           shiftwidth=4 softtabstop=4
//-----------------------------------------------------
