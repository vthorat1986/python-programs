#!/usr/bin/python
import os

print('Opening file in write mode...')
f = open("test.txt", "w+")
print('Name of the file : ', f.name)
print('Closed or not : ', f.closed)
print('Opening mode : ', f.mode)

f.write("My name is Anthony Gonzalvis. Main duniya me akela hoon..")

print('Closing file...')
f.close()
print('Closed or not : ', f.closed)

with open("test.txt") as f:
    for line in f:
        print(line, end="\n")

print('Opening file in read mode...')
f = open("test.txt", "r+")
str = f.read(10)
print('File content are : ', str)
position = f.tell()
print('Current file pointer position is : ', position)
f.seek(0, 1) # seek(offset, from) 0 = begining of the file, 1 = curren position , 2 = end of the file
str = f.read(40)
print('File content are : ', str)

print('Closing file...')
f.close()
print('Closed or not : ', f.closed)

print('Renaming file...')
os.rename("test.txt", "test2.txt")
f = open("test2.txt", "r+")
print('Name of the file : ', f.name)
print('Closing file...')
f.close()
print('Closed or not : ', f.closed)

print('Deleting/Removing file...')
os.remove("test2.txt")

print('Try to open removed file...')
f = open("test2.txt", "r+")