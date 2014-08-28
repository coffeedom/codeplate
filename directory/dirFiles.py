#!/usr/bin/python2

import glob
import os


print "\n============= proc. 1 =============="
os.chdir("./subdir")
for file in glob.glob("*.txt"):
    print file
os.chdir("..")



print "\n============= proc. 2 (recommend) =============="
cwd = os.getcwd()
for file in os.listdir(cwd + "/subdir"):
    if file.endswith(".txt"):
        print file


print "\n============= proc. 3 =============="
cwd = os.getcwd()
for root, dirs, files in os.walk(cwd+"/subdir"):
    for file in files:
        if file.endswith(".txt"):
             print os.path.join(root, file)


print ""
