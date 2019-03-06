#!/usr/bin/python

total = 0  # global variable

def sum(arg1, arg2):
	total = arg1 + arg2  # local variable
	print('Inside the function, local variable total is : ', total) # printing local variable
	return total
	
sum(10, 20)
print('Outside the function, global variable total is : ', total) # printing global variable

# ===================================================== #
Money = 2000

def AddMoney():
	global Money
	Money = Money + 1
	
print('Money before function call : ', Money)
AddMoney()
print('Money after function call : ', Money)