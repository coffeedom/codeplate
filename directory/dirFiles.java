import java.io.File;

public class dirFiles
{
    public static void listFilesDir(final File dire)
    {
        for (final File file : dire.listFiles())
        {
       	    if (file.isDirectory())
            {
                listFilesDir(file);
                // or just ignore with 'continue'
            }
            else
            {
                System.out.println(file.getName());
            }
        }
    }

    public static void main(String args[])
    {    
        final File dire = new File("./subdir");
        listFilesDir(dire);
    }
}

// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
