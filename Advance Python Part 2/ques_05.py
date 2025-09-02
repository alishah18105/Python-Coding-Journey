#Write a programm to find the maximun of  the numbers in a list using the reduce function

from functools import reduce
list = [23,45,67,89,12,90,34,22]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater,list))
