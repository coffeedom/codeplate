// Apache CLI
// http://commons.apache.org/proper/commons-cli/javadocs/api-release/index.html

import org.apache.commons.cli.*;
import org.apache.commons.cli.BasicParser;


public class argsOption
{
    public static void main(String args[])
    {
        //----------------------------------------------------
        // STEP 1. - Create a Parser with your Choice
        //----------------------------------------------------

        CommandLineParser parser0 = new BasicParser();
        CommandLineParser parser1 = new PosixParser();
        CommandLineParser parser  = new   GnuParser();

        //--------------------------------------------------------------
        // STEP 2. - Create an Options object (not Option, but Options)
        //--------------------------------------------------------------

        Options options = new Options();

        //----------------------------------------------------
        // STEP 3. - Set short and long options
        //----------------------------------------------------
        // options: (1) short, (2) long, (3) an arg, (4) description


        // Method 1                (1)    (2)     (3)       (4)
        Option input = new Option( "i", "inputs", true, "input files");
            // input.setLongOpt("input-files");
               input.setRequired( false );		// mandatory option?
               input.setArgName( "f1,f2,f3,f4" );
               input.setArgs(4);
               input.setValueSeparator(',');
        options.addOption( input );

        // Method 2               (1)    (2)    (3)           (4)
        Option help = new Option( "h", "help", false, "print this message" );
        options.addOption( help );

        // Method 3        (1)    (2)       (3)        (4)
        options.addOption( "a",  "all",    false,  "all of them" );
        options.addOption( "o",  "output", true,   "output file" );

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

        if (cmd.hasOption("a"))
            System.out.println("option 'a' is given");
        if (cmd.hasOption("all"))
            System.out.println("option 'all' is given");
        if (cmd.hasOption("o"))
            System.out.println("option 'o' is given");
        if (cmd.hasOption("output"))
        {
            System.out.println("option 'output' is given");
            System.out.println("val = " + cmd.getOptionValue("o"));
            System.out.println("val = " + cmd.getOptionValue("output"));
        }
        if (cmd.hasOption("inputs"))
        {
            System.out.println("option 'inputs' is given");
            for (int i=0; i < cmd.getOptionValues("i").length; i++) {
                System.out.println("val = " + cmd.getOptionValues("i")[i]);
            }
        }

        System.out.println("(info.): end of test program");
        return;
    }
}

