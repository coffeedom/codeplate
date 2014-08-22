#!/bin/sh

export LC_ALL=en_US.utf8


javac -encoding UTF-8         fileOpen.java
java  -Dfile.encoding=utf-8   fileOpen


#(END)
