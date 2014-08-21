#!/usr/bin/python2

import sys
import argparse


def main(args):
	#
	print "\n--- main() ---\n"
	print "args:      : ", args
	print "args.foo   : ", args.foo
	print "args.foo1  : ", args.foo1
	print "args.foo2  : ", args.foo2
	print "args.name  : ", args.name
	print "args.ints  : ", args.ints
	print "args.input : ", args.input
	#
	if args.input == None:
		sys.exit(0)
	#
	#--------------------------------------------
	# read from a file line by line (incl. '\n')
	#--------------------------------------------
	line = args.input.readline()
	while line:
		print line.strip()
		line = args.input.readline()
	#
	# args.input.close
	#
	print "read done..."
	args.input.seek(0)
	#
	#--------------------------------------------
	# read from a file everything (incl. '\n')
	#--------------------------------------------
	lines = args.input.readlines()
	args.input.close()
	#
	for line in lines:
		print line,
	print "read done..."


#-----------------------------------------------------
# MAIN Procedure
#-----------------------------------------------------

if __name__ == "__main__":
	#
	#
	parser = \
	argparse.ArgumentParser(
		description = '= Process some integers =',	# help: header
		epilog      = '(end of help)',				# help: footer
		add_help	= True							# help: option -h,--help
	)
	#
	#
	parser.add_argument(
		'name',										# Positional argument 1
		metavar = 'S',								# for help message
		nargs   = '+',
		help    = 'an integer for the accumulator'
	)
	#
	parser.add_argument(
		'ints',										# Positional argument 2
		metavar = 'N',								# for help message
		type    = float,							# default: string
		nargs   = 1,
		help    = 'an integer for the accumulator'
	)
	#
	parser.add_argument(
		'--sum', '-sum',							# Optional argument 1
		dest    = 'accumulate',
		action  = 'store_const',
		default = max,
		const   = sum,
		help    = 'sum the integers (default: find the max)'
	)
	#
	parser.add_argument(
		'--foo', '-foo',							# Optional (flag) 
		action  = 'store_true',
		help    = 'just testing foo'
	)
	#
	parser.add_argument(
		'--foo1', '-foo1',							# Optional (1 arg) 
		action  = 'store_const',
		default = 0,								# 0: if no -foo 
		const   = 1,								# 1: if    -foo there
		help    = 'just testing foo1'
	)
	#
	parser.add_argument(
		'--foo2', '-foo2',							# Optional (two args) 
		metavar = 'val',
		nargs	= 2,
		default = [0, 0],
		help    = 'just testing foo2'
	)
	#
	parser.add_argument(
		'--input', '-input',
		metavar = 'filename',
		# type	= argparse.FileType('wb', 0)
		type	= argparse.FileType('r', 0)
	)
	#
	args = parser.parse_args()
	print args.accumulate(args.ints)

	main(args)

	print "\nEND OF SCRIPT\n"


#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# vim: tabstop=4           shiftwidth=4 softtabstop=4
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#-----------------------------------------------------
