#!/usr/bin/python2

import sys
import pickle


def serialize(inf0):
	#
	list = [ 0.0, 1.1, 2.2, 3.3, 4.4 ]
	pickle.dump(list, inf0)
	print list

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
		inf0 = open(sys.argv[1],"w")   # write only 
	except IOError as e:
		print 'e: ' + str(e)
		sys.exit(1)

	serialize(inf0)
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
