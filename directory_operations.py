#!/usr/bin/python
import os

# os.rmdir("dir1")
print('Current directory location : ', os.getcwd())

print('Creating new directory...')
os.mkdir("dir1")

print('Changing directory to newly created directory...')
os.chdir("dir1")

print('Current directory location : ', os.getcwd())

os.chdir("../")
print('Current directory location : ', os.getcwd())

print('Removing directory dir1...')
os.rmdir("dir1")

print('Current directory location : ', os.getcwd())