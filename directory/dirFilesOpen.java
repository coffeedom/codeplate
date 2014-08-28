
import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;


public class dirFilesOpen
{
    private void procFile(String file)
    {
        try
        {
            File              fin = new File(file);
            FileInputStream   fis = new FileInputStream(fin);
            InputStreamReader isr = new InputStreamReader(fis, "UTF-8");
            BufferedReader    fbr = new BufferedReader(isr);

            System.out.println("===== process: " + fin.getName() + " ======");

            String str = null;

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


    private boolean matchExtension(String file, String ext)
    {
        if (ext == null) return true;

        int idx = file.lastIndexOf('.');

        if (idx == -1)  // the file name does not have ".". 
        {
            if (ext.length() == 0)
                return true;
            else
                return false;
        }

        // the file name has ".".

        if ( ext.compareTo(".") != 0 )
            ext = "." + ext;    // use sb.

        if ( ext.compareTo(file.substring(idx)) == 0)
            return true;

        return false;
    } 

    private List<String> createFileList(String dirname, String extensn)
    {
        List<String> fileList = new ArrayList<String>();

        File dire = new File(dirname);

        for (File file : dire.listFiles())
        {
            if (file.isDirectory())
            {
                continue;
            }
            else
            {
                if (matchExtension(file.getName(), extensn))
                    fileList.add(dirname + "/" + file.getName());
            }
        }
        // System.out.println(fileList);
        Collections.sort(fileList);
        return fileList;
    }




    public static void main(String args[])
    {
        CommandLineParser parser = new GnuParser();
        Options          options = new Options();

        // options: (1) short, (2) long, (3) an arg, (4) description

        // Option 1               (1)    (2)         (3)       (4)
        Option dire = new Option( "d", "directory", true, "directory name");
               dire.setRequired( false );
        options.addOption( dire );

        // Option 2               (1)    (2)         (3)       (4)
        Option extn = new Option( "e", "extension", true, "file extension");
               extn.setRequired( false );
        options.addOption( extn );


        // Option 3               (1)    (2)    (3)           (4)
        Option help = new Option( "h", "help", false, "print this message" );
        options.addOption( help );

        // Help Message
        HelpFormatter formatter = new HelpFormatter();


        //----------------------------------------------------
        // Parse arguments
        //----------------------------------------------------

        CommandLine cmd = null;

        try
        {
            cmd = parser.parse( options, args, false );
        }
        catch (UnrecognizedOptionException e)
        {
            System.out.println("(error0): " + e.toString());
            formatter.printHelp( "prog.", options );
            System.exit(0);
        }
        catch (MissingArgumentException e)
        {
            System.out.println("(error1): " + e.toString());
            formatter.printHelp( "prog.", options );
            System.exit(0);
        }
        catch (ParseException e)
        {
            System.out.println("(error2): " + e.toString());
            formatter.printHelp( "prog.", options );
            System.exit(0);
        }
        finally
        {
            // System.exit(2);
        }


        //----------------------------------------------------
        // Get option flag or values
        //----------------------------------------------------
/*
        if (cmd.hasOption("d"))
            System.out.println("option 'd' is given");
        if (cmd.hasOption("e"))
            System.out.println("option 'e' is given");

        if (cmd.hasOption("directory"))
        {
            System.out.println("option 'directory' is given");
            System.out.println("val = " + cmd.getOptionValue("d"));
        }
        if (cmd.hasOption("extension"))
        {
            System.out.println("option 'extension' is given");
            System.out.println("val = " + cmd.getOptionValue("extension"));
        }
*/

        String dirname = cmd.getOptionValue("directory");
        String extensn = cmd.getOptionValue("extension");


        //---------------------------------------------------
        // Main Processes
        //---------------------------------------------------

        if (dirname == null)
            dirname = ".";

        dirFilesOpen dfo = new dirFilesOpen();
        List<String> fileList = dfo.createFileList(dirname, extensn);

        for (String file : fileList)
        {
            dfo.procFile(file);
        }

        System.out.println("\n\n(info.): end of test program");
        return;
    }
}

// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
