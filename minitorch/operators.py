"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable


def mul(x : float,y : float) -> float:
    return x*y

def add(x : float,y : float) -> float:
    return x+y

def id(i):
    return i

def neg(x : float) -> float:
    return -1 * x

def lt(x : float , y : float) -> bool:
    return x < y 

def eq(x : float, y: float) -> bool:
    return x == y

def max(x : float , y : float) -> float:
    return max(x,y)

def is_close(x: float , y : float , threshold : float =1e-2) -> bool : 
    return abs(x-y) < threshold

def exp(x : float) -> float : 
    return math.exp(x)

def sigmoid(x : float) -> float:
    return  1 / (1 + exp(-x))
    # if x >=0 :
    #     return  1 / (1 + exp(-x))
    # else:
    #     return exp(x) / (1 + exp(x))


def inv(x : float) -> float : 
    try : 
        r = 1 / x 
        return r 
    except ZeroDivisionError:
        return 1e16
    
def log(x : float) -> float : 
    return math.log(x)


def log_back(x : float, y : float) -> float : 
    return y * (1 / x)
    
def inv_back(x : float,y:float) -> float : 
    return y * (-1 / x**2)

def relu_back(x : float , y : float) -> float: 
    return y if x > 0 else 0


def relu(x : float) -> float: 
    return x if x>0 else 0

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
