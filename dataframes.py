#!/usr/bin/python

import pandas as pd

participants = pd.read_csv('participants.csv', index_col = 0)

print(participants)
print(participants.loc[[3, 2]]) # this uses index names
print(participants.iloc[2])  # this uses actual index number, starting from 0