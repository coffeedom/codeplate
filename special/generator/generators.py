#!/usr/bin/python2

import sys

#---------------------------------
# Very Simple Iteration on a List
#---------------------------------
print "====== test 0. Simple Iteration ======"
mylist = [1, 2, 3]
for i in mylist:
	print(i)

#--------------------------------
# Using a List Comprehension
#--------------------------------
print "====== test 1. List Comprehension ======"
mylist = [x*x for x in range(3)]
for i in mylist:
	print(i)

#-------------------------------------------------------------------
# Using a Generator:
# Generators = Iterators. 
# Can iterate over them only once.
# Generators don't store all the values in memory.
# They generate the values on the fly.
#-------------------------------------------------------------------
print "====== test 2a. Generator 1st ======"
mygene = (x*x for x in range(3))
for i in mygene:
	print(i)
print "====== test 2b. Generator 2nd ======"
for i in mygene:
	print(i)
print "====== test 2c. Generator 3rd ======"
mygene = (x*x for x in range(3))
for i in mygene:
	print(i)
#-------------------------------------------------------------------
# Use [] for (list) Comprehension.
# Use () for Generators.
# Can't iterate: for i in the generator 'mygene' a second time.
# Calculate 0, then forget about it and calculate 1, then 4,
# one by one.
#-------------------------------------------------------------------


#----------------------------------------------
# The 'yield' is like 'return'
# The function doesn't return a value 
# The function returns a generator.
#----------------------------------------------
print "====== test 3. yield ======"
def createGenerator():
	mylist = range(3)
	for i in mylist:		# this code does not run,
		yield i*i			# doesn't return i*i value(s),
							# but returns a generator. 
mygene = createGenerator()
print(mygene)				# mygene is an object.
for i in mygene:			# code is run each time
	print(i)				# the for uses the generator.
							#
print "====== test 3. yield (next) ======"
mygene = createGenerator()
print mygene.next()
print mygene.next()
print mygene.next()


#-----------------------------------------------------
# edit ~/.vimrc , add "set modeline"
# then, do not remove:
# ###: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# vim: tabstop=4           shiftwidth=4 softtabstop=4
#-----------------------------------------------------
