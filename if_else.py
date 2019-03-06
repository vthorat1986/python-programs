#!/usr/bin/python

var = int(input("Please enter the age : "))

if (var < 18 ):
	print ("Not allowed to drink and marry!")
elif (var > 17 and var < 21):
	print ("Not allowed to drink!")
else :
	print ("Allowed to marry being drunk!")