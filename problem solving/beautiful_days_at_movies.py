'''
problen:-

Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days,[i...j] and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.

Function Description:-
Complete the beautifulDays function in the editor below. It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):
i: the starting day number
j: the ending day number
k: the divisor

Input Format:-
A single line of three space-separated integers describing the respective values of i, j, and k.

Output Format:-
Print the number of beautiful days in the inclusive range between i and j.

Sample Input:-
20 23 6

Sample Output:-
2

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    c=0
    for n in range(i,j+1):
        r=0
        x=n
        while n:
            r=r*10+n%10
            n=n//10
        if abs(x-r)%k==0:
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

