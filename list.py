#!/usr/bin/python

list1 = [ 'vaibhav' , 1 , 5.567 , 'thorat' , 'A' ]
list2 = [ 'wait' , 0.21 ]

print (list1)
print (list1[4])
print (list1[1:4])
print (list1[1:])
print (list2 * 3)
print (list1 + list2)

#modify list values
print ('Before modification : ', list1)
list1[2] = 'vijay'
print ('After modification : ', list1)
del list1[2]
print ('After deletion : ', list1)

# Membership operators
print ('vaibhav' in list1)
print ('mangesh' in list1)

# Tuples - read only lists
list3 = ('vai' , 'bhav' , 5)
list4 = ('thorat' , 4)

print (list3[2] + list4[1]) #Addition of same data type tuple items
print (list3)
print (list3[2])
print (list3[1:2])
print (list3[1:])
print (list4 * 3)
print (list3 + list4)