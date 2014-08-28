#!/usr/bin/python2

import os
import sys
import argparse
# from sets import Set 


def procFile( file ):
    #
    print ("====== printing: " + file)
    #
    try:
        inf = open(file, "r")
        line = inf.readline()   # option: use readlines()
        while line:
            print (line.strip())
            line = inf.readline()
        print ("...... printing done ...")
    except IOError as e:
       return False
    #
    inf.close()
    return True


def main(args):
    #
    # fSet = Set()
    fLst = list()
    #
    dir = "./"
    ext = None
    cwd = ""

    if args.ext != None:
        ext = "." + args.ext

    if args.dir != None:
        dir = args.dir.strip() 

    if dir[0] != '/':
        cwd = os.getcwd()
        dir = cwd + '/' + dir 

    if os.path.exists( dir ) == False:
        print ("(err) " + dir + " - does not exist")
        sys.exit(1)

    if os.path.isdir( dir ) == False:
        print ("(err) " + dir + " - is not a directory")
        sys.exit(1)

    for file in os.listdir( dir ):
        if ext != None and file.endswith(ext) == False:
            continue
        if os.path.isdir( dir + '/' + file ) == True:   # may not need 
            continue                                     # may not need
        fLst.insert(0, dir + '/' + file)
        # fLst.append(dir + '/' + file)
        # fLst.sort()
        # fSet.add(dir + '/' + file)

    # TODO
    # recursive sub directory
    # process them in parallel if possible    

    for file in fLst:
        if procFile( file ) == False:
            print ("(err): " + file)

    #
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
    parser = \
    argparse.ArgumentParser(
        description = 'Process files in a DIR',     # help: header
        epilog      = '(end of help)',              # help: footer
        add_help    = True                          # help: option -h,--help
    )
    #
    parser.add_argument(
        '--dir', '-dir',                            # Optional argument 1
        help    = 'directory name'
    )
    #
    parser.add_argument(
        '--ext', '-ext',                            # Optional argument 1
        help    = 'file type (extension)'
    )
    #
    args = parser.parse_args()

    #-------------------------
    # main procedure
    #-------------------------
    main(args)
    sys.exit(0)


#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# ...: tabstop=4           shiftwidth=4 softtabstop=4
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#-----------------------------------------------------
