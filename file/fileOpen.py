#!/usr/bin/python2

import sys

import time
import datetime


def readFiles(inf1, inf2):
	#
    #--------------------------------------------
	# write a date string to inf1.
    #--------------------------------------------
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	inf1.write(st+'\n')
	inf1.flush()
	inf1.close()
	#
    #--------------------------------------------
    # read from a file all bytes (incl. '\n')
    #--------------------------------------------
	bytes = inf2.read()
	# inf2.close()				# can be closed!
	lines = bytes.split('\n')
	for line in lines:
		print line
	print "read done..."
	inf2.seek(0)
	#
	#--------------------------------------------
	# read from a file line by line (incl. '\n')
	#--------------------------------------------
	line = inf2.readline()
	while line:
		print line.strip()
		line = inf2.readline()
	print "read done..."
	inf2.seek(0)
	#
	#--------------------------------------------
	# read from a file everything (incl. '\n')
	#--------------------------------------------
	lines = inf2.readlines()
	inf2.close()
	#
	for line in lines:
		print line,
	print "read done..."



def usage():
    """
    Description: usage() function
    """
    print "\nUsage:", sys.argv[0], "file1(arg[1]) file2(arg[2])\n" 


#-----------------------------------------------------
# MAIN Procedure
#-----------------------------------------------------

if __name__ == "__main__":
	#---------------------------------------
    # sys.argv[0]       python program name
    # sys.argv[1]       actual arg1
    # sys.argv[2]       actual arg2
    # len(sys.argv)     3
	#---------------------------------------

	if len(sys.argv) != 3:
		usage()
		sys.exit(2)

	try:
		#### = open(sys.argv[1],"r+")  # read/write
		inf1 = open(sys.argv[1],"a")   # read/write-append
		inf2 = open(sys.argv[2],"r")   # read only 
	except IOError as e:
		print 'e        : ' + str(e)
		print 'type(e)  : ' + str(type(e))
		print 'e.args   : ' + str(e.args)
		print 'e.message: ' + e.message
		sys.stderr.write("ERROR open file: %s\n" % str(e))
		sys.stderr.write("ERROR open file: %s\n" % sys.argv[1])
		sys.stderr.write("ERROR open file: %s\n" % sys.argv[2])
		sys.exit(1)

	readFiles(inf1, inf2)
	  
	inf1.close()
	inf2.close()
	#
else:
	print __name__

#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# vim: tabstop=4           shiftwidth=4 softtabstop=4
#-----------------------------------------------------
