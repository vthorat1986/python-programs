#!/usr/bin/python

def verifyAge(age):
	assert(int(age) > 0), "Invalid age provided!" # this error message won't be printed as Assertion error is handled below
	print('Provided age is : ', age)
	return

age = 0
try:
	age = input('Provide age : ')
	verifyAge(age)
except:
	print('AsertionError caught!')
	try:
		int(age)
	except:
		print("ValueError caught! Provided age '", age, "' is not a number!!!")
	else:
		print("Provided age '", age , "' is less than or equal to ZERO!!!")
else:
	print('This is else block! Provided age is greater than ZERO!! ')
finally:
	print('This is finally block')