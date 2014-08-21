#!/usr/bin/python2

import sys


#-----------------------------------------------------
# MAIN Procedure
#-----------------------------------------------------

if __name__ == "__main__":
	#
	print "__main__	: ", __name__
	print "sys.argv	: ", sys.argv
	print "len(sys.argv)	: ", len(sys.argv)
	#
	for i in range(len(sys.argv)):
		print "sys.argv[", i , "]	: ", sys.argv[i]
	#
	i = -1
	print "sys.argv[", i , "]	: ", sys.argv[i]


#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# vim: tabstop=4           shiftwidth=4 softtabstop=4
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#-----------------------------------------------------
