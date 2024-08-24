import numpy as np

r  = np.random.random((20,20))



def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
print(add(r,r))