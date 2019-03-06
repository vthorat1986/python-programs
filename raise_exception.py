#!/usr/bin/python

def func(level):
	if(level < 1):
		raise Exception("Invalid level!", level)
	else:
		print('Level is : ', level)
	return
	
try:
	func(int(input('provide level : ')))
except Exception as error:
	print('Caught error...', error)
else:
	print('Level is provided correctly!')