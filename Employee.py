#!/usr/bin/python

class Employee:
    'Employee class, a simple example'
    empCount = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Employee.empCount += 1

    def displayCount(self):
        print('Employee count is : %d' % Employee.empCount)

    def displayEmployeeInfo(self):
        print('Name : ', self.name, ' ID : ', self.id)

emp1 = Employee("Vaibhav", 8767)
emp2 = Employee("Siddhi", 123456)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()
emp1.displayCount()
emp2.displayCount()
print('Total employees : ', Employee.empCount)