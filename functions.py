#!/usr/bin/python

# Pass by reference : value of the passed variable object changes
def appendme(list):
	list.append([1, 2, 3, 4])
	print('Printing list inside the function : ', list)
	return
	
mylist = [10, 20, 30]
appendme(mylist)
print('Printing list outside the function : ', mylist)

# Pass by reference : value of the passed variable does not change
def changeme(list):
	list = [5, 6, 7, 8]
	print('Printing list inside the function : ', list)
	return

mylist2 = [40, 50, 60]
changeme(mylist2)
print('Printing list outside the function : ', mylist2)