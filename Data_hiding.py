#!/usr/bin/python

class Counter:
    'A Normal counter class'
    __secretCounter = 0   # private variable

    def showCount(self):
        self.__secretCounter += 1
        print('Count is : ', self.__secretCounter)

counter = Counter()
counter.showCount()  # Access private variable through a method
counter.showCount()
print('Total count is : ', counter._Counter__secretCounter) # Access private variable through instance object & class name
print('Total count is : ', counter.__secretCounter) # throws AttributeError while accessing private variable through instance object