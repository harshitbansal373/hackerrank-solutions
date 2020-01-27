'''
problem:-

Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1. For example, if your array is a=[1,1,2,2,4,4,5,5,5], you can create two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

Function Description:-
Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.
pickingNumbers has the following parameter(s):
a: an array of integers

Input Format:-
The first line contains a single integer , the size of the array .
The second line contains  space-separated integers .

Output Format:-
A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is <=1.

Sample Input 0:-
6
4 6 5 3 3 1

Sample Output 0:-
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    l=a
    max=0
    for i in a:
        c=b=0
        for j in range(len(l)):
            if i-l[j]==1 or i-l[j]==0:
                c+=1
        for j in range(len(l)):
            if i-l[j]==1 or i-l[j]==0:
                b+=1
        if max<c:
            max=c
        if max<b:
            max=b
    return max



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

