#!/usr/bin/python
#print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

list_of_functions = []

for function_name in dir(re):
    if "find" in function_name:
        list_of_functions.append(function_name)

print("Sorted list of functions from 're' module which contains 'find' word : ")
print(sorted(list_of_functions))