#!/usr/bin/python2

import sys


def usage():
    """
    Description: usage() function
    """
    print "\nUsage:", sys.argv[0], "[file]\n"


#-----------------------------------------------------
# MAIN Procedure
#-----------------------------------------------------

if __name__ == "__main__":
	#---------------------------------------
    # sys.argv[0]       python program name
    # sys.argv[1]       actual arg1
    # len(sys.argv)     2
	#---------------------------------------

	try:
		if len(sys.argv) == 1:
			inf1 = sys.stdin
		elif len(sys.argv) == 2:
			inf1 = open(sys.argv[1],"r")    # read only
		else:
			usage()
			sys.exit(2)
	except IOError as e:
		print 'e        : ' + str(e)
		print 'type(e)  : ' + str(type(e))
		print 'e.args   : ' + str(e.args)
		print 'e.message: ' + e.message
		sys.stderr.write("ERROR open file: %s\n" % str(e))
		sys.stderr.write("ERROR open file: %s\n" % sys.argv[1])
		sys.exit(1)

        
	line = inf1.readline()			# read from a file line by line (incl. '\n')
	while line:
		print line.strip()			# sys.stdout.write(str+'\n')
		line = inf1.readline()
	inf1.close()
	#
	#
else:
	print __name__

#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# vim: tabstop=4           shiftwidth=4 softtabstop=4
#-----------------------------------------------------
