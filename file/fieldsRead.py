#!/usr/bin/python2

import sys


def readFiles(inf0):
	#
	#--------------------------------------------
	# read from a file line by line (incl. '\n')
	#--------------------------------------------
	line = inf0.readline()
	while line:
		line = line.strip()				# not just: line.strip()
		fields = line.split('\t')
		for fieldIdx in range(len(fields)):
			print "fields[", str(fieldIdx), "] = ", fields[fieldIdx]
		print ''
		line = inf0.readline()


def usage():
    """
    Description: usage() function
    """
    print "\nUsage:", sys.argv[0], "file(tab separated)\n" 


#-----------------------------------------------------
# MAIN Procedure
#-----------------------------------------------------

if __name__ == "__main__":
	#---------------------------------------
    # sys.argv[0]       python program name
    # sys.argv[1]       actual arg1
    # len(sys.argv)     2
	#---------------------------------------

	if len(sys.argv) != 2:
		usage()
		sys.exit(2)

	try:
		inf0 = open(sys.argv[1],"r")   # read only 
	except IOError as e:
		print 'e        : ' + str(e)
		print 'type(e)  : ' + str(type(e))
		print 'e.args   : ' + str(e.args)
		print 'e.message: ' + e.message
		sys.stderr.write("ERROR open file: %s\n" % str(e))
		sys.stderr.write("ERROR open file: %s\n" % sys.argv[1])
		sys.exit(1)

	readFiles(inf0)
	inf0.close()
	#
else:
	print __name__

#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# vim: tabstop=4           shiftwidth=4 softtabstop=4
#-----------------------------------------------------
