#!/usr/bin/python

import calendar

def printMonth(year, month):
	month = calendar.month(year, month)
	print('Calendar for given month is : ')
	print(month)
	return