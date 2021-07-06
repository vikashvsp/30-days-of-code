

import math
import os
import random
import re
import sys



def factorial(n):
    if(n<1):
        return 1
    else: return n*factorial(n-1)

n=int(input("Enter the number whose factorial yuou want:- "))
print(factorial(n))
