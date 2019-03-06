#!/usr/bin/python

str1 = 'Hello world!'
str2 = 'Vaibhav Thorat'

# substrings
print ('str1[6] : ', str1[6])
print ('str2[2:8] : ', str2[2:8])

# update part of a string
print ('Before update string is : ', str1)
print ('Updated string : ', str1[:6] + 'Vaibhav!')

# String formatting
print ('My name is %s & my age is %d' % ('Vaibhav' , 32))

# raw string to print special characters
print ('Before raw string : C:\\something')
print ('After raw string : ')
print (r'C:\\something')