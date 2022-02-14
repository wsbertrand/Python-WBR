#%% Function where 2 numbers are given and it returns the addition if both are lower than 10 and the product in the other case.
import random

def fun(arg1,arg2):
    if arg1 <10and arg2 < 10:
        return arg1 + arg2
    else:
        return arg1 * arg2
fun(10,11)

#%% Function where the coefficients of a cuadratic equation are given and the solution are shown
import math
def cuadra(a,b,c):
    delta = b*b-4*a*c
    if delta >= 0:
        x1= -b+math.sqrt(int(b*b-4*a*c))
        x2 = -b-math.sqrt(int(b*b-4*a*c))
        return (x1,x2)
    else:
        return "No solution"
cuadra(1,2,3)

#%% Program that accepts a hyphen separated sequence of words as input and prints the word in a hyphen separating sequence
#after sorthing them alphabetically
def cutting():
    x = input("What is your hyphen separated sentence?")
    cut = x.split('-')
    cut.sort()
    print('-'.join(cut))
cutting()


#%% Function that takes a number as a parameter and check the number is prime
from sympy import isprime
number = int(input("What number do you wanna check?"))
isprime(number)

#%% Function that accepts accepts a string and calculate the numb







