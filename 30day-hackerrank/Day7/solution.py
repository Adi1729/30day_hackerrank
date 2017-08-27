#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = []
l = len(arr)
for i in range(0,l):
    print(arr[l-i-1],end = ' ')
