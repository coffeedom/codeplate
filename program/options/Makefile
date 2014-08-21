# Makefile
#
M_JAVAD = /usr/java
M_JVJDK = $(M_JAVAD)/jdk/bin
M_JUTIL = $(M_JAVAD)/utils
#
U_JJAMA = $(M_JUTIL)/Jama-1.0.3.jar
U_JTUPL = $(M_JUTIL)/javatuples-1.2.jar
U_JVCLI = $(M_JUTIL)/commons-cli-1.2.jar
#
M_JAVAC = $(M_JVJDK)/javac -g -cp .:$(U_JVCLI):$(M_JTUPL)
M_JAVAR = $(M_JVJDK)/java     -cp .:$(U_JVCLI):$(M_JTUPL)

APP0 = argsOption

all:  $(APP0).run


$(APP0).class:	   $(APP0).java
	$(M_JAVAC) $(APP0).java 

$(APP0).run:       $(APP0).class
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -a
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -o xxx
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -x
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -i
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -i aaa,bbb
	@echo "\n--------------------------------------------"
	$(M_JAVAR) $(APP0) -i aaa,bbb,ccc,ddd
	@echo "\n--------------------------------------------"

clean:
	rm -rf $(APP0).class 

#(END)
