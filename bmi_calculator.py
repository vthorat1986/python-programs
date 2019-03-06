#!/usr/bin/python

height = [1.87, 1.87, 1.75]
weight = [81.3, 75.5, 82.2]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

bmi = (np_weight / np_height ** 2)

print(bmi)
print(bmi[bmi > 23])
addition = np_height + np_weight

print(addition)