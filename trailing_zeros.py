#This program finds the number of trailing zeros at the end of a factorial of a number
from functools import reduce

def zeros(n):
    factorial = reduce((lambda x, y: x * y), [a for a in range(1, n+1)])
    trail = 0
    for x in str(factorial)[::-1]:
        if x != "0":
            break
        trail += 1
    return trail