#!/usr/bin/python
import time
import calendar

print ('time.time() : ', time.time())
print ('time.localtime(time.time()) : ', time.localtime(time.time()))


# Printing month of a calendar
january = calendar.month(2019, 1)
print("Here's the January month calendar : ")
print (january)

print ('time.asctime(time.localtime(time.time())) : ', time.asctime(time.localtime(time.time())))
print ('Going to sleep for 5 seconds')
time.sleep(5)  # sleeps for 5 seconds
print ('Woke up after 5 seconds!')
print ('time.asctime(time.localtime(time.time())) : ', time.asctime(time.localtime(time.time())))