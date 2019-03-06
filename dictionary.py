#!/usr/bin/python

dict = {}
dict['one'] = 'vaibhav'
dict[2] = 'thorat'

employeeDictionary = {'name' : 'vaibhav' , 'employeeId' : '008767' , 'dept' : 'telecom'}

print (dict)
print (dict['one'])
print (dict[2])
print (dict['one'] + ' ' + dict[2])
print (employeeDictionary)
print (employeeDictionary.keys())
print (employeeDictionary.values())

del (employeeDictionary['dept'])   # delete dept 
print ('After deletion : ', employeeDictionary)
employeeDictionary['company'] = 'Persistent' # Add new entry
print ('After adding company : ', employeeDictionary)
print ('Dictionary items : ', employeeDictionary.items())
employeeDictionary.clear()    # Clear dictionary conent
print ('After clearing dictionary : ', employeeDictionary)
del (employeeDictionary)    # delete the dictionary
print ('After deleting dictionary : ', employeeDictionary)