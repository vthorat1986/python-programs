#!/usr/bin/python

# Keyword arguments
print(' ============ Keyword arguments ==============')
def employeeInfo(name, age):
	print('Name of the employee is : ', name)
	print('Age of the employee is : ', age)
	return
	
employeeInfo(age = 32, name = 'Vaibhav')

# Default arguments
print(' ============ Default arguments ==============')
def info(name, age = 32):
	print('Name of the employee is : ', name)
	print('Age of the employee is : ', age)
	return
	
info(name = 'Vaibhav', age = 35)
info(name = 'Vaibhav')

# Variable arguments
print(' ============ Variable arguments ==============')
def variableArgs(var, *variableVar):
	print('Normal variable : ', var)
	for i in variableVar:
		print('variable var : ', i)
	return
	
variableArgs(22)
variableArgs(10, 20, 30, 40)

# Anonymous function
print(' ============ Anonymous function ==============')
sum = lambda arg1, arg2 : arg1 + arg2

print('Addition of 10 & 20 is : ', sum(10, 20))

# Function with return value
print(' ============ Function with return value ==============')
def sum2(arg1, arg2):
	total = arg1 + arg2
	return total

print('Total is : ', sum2(20, 25))