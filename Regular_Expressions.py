#!/usr/bin/python
import re

# ========== Search & Replace ==============
phoneNum = '8149-13-80-26  # This is a phone number'

num = re.sub(r'#.*$', '', phoneNum)
print('Phone number after commet removal : ', num)

num = re.sub(r'\D', '', phoneNum)
print('Phone number ater removal of all non-digits : ', num)


# ========= Search , Match ============
matchObj = ''
searchObj = ''

def printObject(obj):
    if(obj == matchObj):
        print('Printing matchObj result : ')
    elif(obj == searchObj):
        print('Printing searchObj result : ')
    else:
        print('Invalid object...')

    if(obj):
        print('obj.group() : ', obj.group())
        print('obj.group(1) : ', obj.group(1))
        print('obj.group(2) : ', obj.group(2))
    else:
        print('No string matched!!')

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

printObject(matchObj)
printObject(searchObj)

matchObj = re.match(r'dogs', line, re.M|re.I)
searchObj = re.search(r'dogs', line, re.M|re.I)

printObject(matchObj)
printObject(searchObj)