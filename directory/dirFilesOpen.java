
import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.*;


public class dirFilesOpen
{
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
	// STEP 4. - Parse arguments
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
        // STEP 5. - Check options are given or not
        //----------------------------------------------------

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

        System.out.println("(info.): end of test program");
        return;
    }
}

