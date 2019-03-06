#!/usr/bin/python

string = 'sagas'
string2 = string[::-1]
print(string[::-1])  # (start:stop:step) as the step is -1 here, start is set to end of the string & stop is set to begiining of the string by-default
if(string==string2):
    print('String is palindrome!')
else:
    print('String is not palindrome!')