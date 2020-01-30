#Sequence Equation

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l=[]
    result=[]
    for i in range(1,len(p)+1):
        for j in range(len(p)):
            if i==p[j]:
                l.append(j+1)
    for i in l:
        for j in range(len(p)):
            if i==p[j]:
                result.append(j+1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

