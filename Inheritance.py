#!/usr/bin/python

class Parent:
    'Parent class'
    parentAttr = 100

    def __init__(self):
        print('Parent constructor called...')

    def parentMethod(self):
        print('Parent method called...')

    def setAttr(self, attr):
        print('Setting parent attribute to ', attr)
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent attribute : ', Parent.parentAttr)

    def myMethod(self):
        print('myMethod from Parent')

class Child(Parent):
    'Child class extending Parent'

    def __init__(self):
        print('Child constructor called...')

    def childMethod(self):
        print('Child method called...')
    
    def myMethod(self):   # Method overriding
        print('myMethod from Child')

c = Child()
c.childMethod()
c.parentMethod()
c.getAttr()
c.setAttr(50)
c.getAttr()
c.myMethod()