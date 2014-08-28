# Makefile
#
M_JAVAD = /usr/java
M_JVJDK = $(M_JAVAD)/jdk/bin
M_JUTIL = $(M_JAVAD)/utils
#
U_JVCLI = $(M_JUTIL)/commons-cli-1.2.jar
#
M_JAVAC = $(M_JVJDK)/javac -g -cp .:$(U_JVCLI):$(M_JTUPL)
M_JAVAR = $(M_JVJDK)/java     -cp .:$(U_JVCLI):$(M_JTUPL)

APP0 = dirFiles
APP1 = dirFilesOpen

all: $(APP0).class $(APP1).run


$(APP0).class:	   $(APP0).java
	$(M_JAVAC) $(APP0).java 

$(APP1).class:	   $(APP1).java
	$(M_JAVAC) $(APP1).java 

$(APP1).run:       $(APP1).class
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP1) -a
	@echo "\n--------------------------------------------"

clean:
	rm -rf $(APP0).class 
	rm -rf $(APP1).class 

#(END)
