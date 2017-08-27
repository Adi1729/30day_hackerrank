#!/bin/python3

import sys

n = int(input().strip())
p = 1
one_count=0
max_count=0
while(n>0):
    factor = n // 2
    remainder = n - 2 * factor
    n = int(n/2)
    if(remainder == 1):
        one_count+=1
        max_count=max(max_count,one_count)
    else:
        one_count=0
        
 
print(max_count)
