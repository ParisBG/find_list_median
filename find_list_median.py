#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:28:01 2022

@author: parisbg
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


#if len(arr) is odd the median is the middle value
#if len(arr) is even the median is the avg of the middle 2 values
arr = [1,90,3,4,5]

arr.sort()
length = len(arr)

if length % 2 != 0:
    middle_pos = int(length/2)
    print( arr[middle_pos])
else:
    middle_pos2 = int(length/2)
    middle_pos1 = middle_pos2 - 1
    print( (arr[middle_pos1] + arr[middle_pos2])/2)
        
    
'''
ORRRR
'''
    
print()

from statistics import median
print(median(arr))

