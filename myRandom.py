import numpy as np
from calc import divide
r  = np.random.random((30,30))



def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
print(add(r,r))

print(divide(10,5))