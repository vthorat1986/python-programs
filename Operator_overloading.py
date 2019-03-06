#!/usr/bin/python

class Vector:
    'A vector class'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):    # Similar to the .toString() method in JAVA
        return('Vector (%d, %d)' % (self.a, self.b))

    def __add__(self, other):   # Operator overloading
        return(Vector(self.a + other.a, self.b + other.b))

v1 = Vector(2, 3)
v2 = Vector(5, -1)
print(v1 + v2)