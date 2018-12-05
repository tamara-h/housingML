
import pandas
import numpy as np
import sklearn.linear_model as lm
from sklearn.model_selection import KFold
from sklearn import preprocessing as pre
import random
import matplotlib.pyplot as plt

"""Load in the California housing dataset. Originally downloaded from https://github.com/ageron/handson-ml/tree/master/datasets/housing"""

housing = pandas.read_csv('./data/housing.csv')


long_buckets = []

for i in housing.longitude:
    # rounding the longitude values into buckets
    i = float(round(i,0))
    found = False
    # print(buckets)
    if(long_buckets):
        for j in range(len(long_buckets)):
            if i == long_buckets[j][0]:
                long_buckets[j][1] += 1
                found = True
        if not found:
            long_buckets.append([i,1])
    else:
        long_buckets.append([i,1])
print(long_buckets)
print(len(long_buckets))

lat_buckets = []

for i in housing.latitude:
    # rounding the latitude values into buckets
    i = float(round(i,0))
    found = False
    # print(buckets)
    if(lat_buckets):
        for j in range(len(lat_buckets)):
            if i == lat_buckets[j][0]:
                lat_buckets[j][1] += 1
                found = True
        if not found:
            lat_buckets.append([i,1])
    else:
        lat_buckets.append([i,1])
print(lat_buckets)
print(len(lat_buckets))
