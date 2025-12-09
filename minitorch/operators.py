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
    return x if x>y else y

def is_close(x: float , y : float , threshold : float =1e-2) -> bool : 
    if isinstance(x,(float,int)) and isinstance(y,(float,int)):
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

def fnList(fn:Callable[[float,float],bool]) -> Callable[[Iterable[float],Iterable[float]],Iterable[float]] :
    def apply(ls1 : Iterable[float], ls2 : Iterable[float]):
        ret = []
        for x,y in zip(ls1,ls2):
            ret.append(fn(x,y))
        return ret 
    return apply


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


def map(fn : Callable[[float],float]) -> Callable[[Iterable[float]],Iterable[float]]:
    def apply(l: Iterable[float]) -> Iterable[float]:
        ret = []
        for k in l:
            ret.append(fn(k))
        return ret
    return apply



def ZipWith(fn : Callable[[Iterable[float]],Iterable[float]]) -> Callable[[Iterable[float],Iterable[float]],Iterable[float]]:
    def apply(l1: Iterable[float],l2 : Iterable[float]) -> Iterable[float]:
        ret = []
        for l_1,l_2 in zip(l1,l2):
            ret.append(fn(l_1,l_2))
        return ret
    return apply

def reduce(fn : Callable[[float,float],float]) -> Callable[[Iterable[float]],float] : 
    def apply(l : Iterable[float]) -> float:
        if l:    
            res = l[0]
            for k in l[1:]:
                res = fn(k,res)
            return res
        else:
            return None
    return apply

negList = map(neg)
addLists = ZipWith(add)
sum = reduce(add)
prod = reduce(mul)