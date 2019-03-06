#!/usr/bin/python

for character in 'Python':
	if (character == 'h'): break
	print ('Current character : ', character)

fruits = ['mango' , 'apple' , 'banana']
for f in fruits:
	if f == 'apple': continue
	print ('Current fruit : ', f)

for index in range(len(fruits)):      #Iterating by sequence index
	if fruits[index] == 'apple' :
		pass
		print ('This is a pass block : ')
	print ('Current fruit : ', fruits[index])

#  create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newList = [int(number) for number in numbers if number > 0]
print('List of +ve numbers is: %s' % newList)
