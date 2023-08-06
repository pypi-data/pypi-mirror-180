#!/usr/bin/env python3
# File       : ElementaryFunc.py
# Description: 
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np

from dual import Dual
from Node import Node

# Trig functions
def sin(x):
    """
    Return the sine value of x.

    Parameters
    ----------
    x : int, float, Dual, Node
      Input to the sine function.
    
    Returns
    -------
    value : int, float, Dual
      The sine value of the dual number implementation or the sine value of a real number.

    """
    if isinstance(x, Node):
        child = Node(np.sin(x.value))
        x.children.append({'partial_der':np.cos(x.value), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.sin(x.real), np.cos(x.real) * x.dual)
    else:
        return np.sin(x)

def cos(x):
    """
    Return the cosine value of x.

    Parameters
    ----------
    x : int, float, Dual
      Input to the cosine function.
    
    Returns
    -------
    value : int, float, Dual
      The cosine value of the dual number implementation or the cosine value of a real number.

    """
    if isinstance(x, Node):
        child = Node(np.cos(x.value))
        x.children.append({'partial_der':-np.sin(x.value), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.cos(x.real), -np.sin(x.real) * x.dual)
    else:
        return np.cos(x)

def tan(x):
    """
    Return the tangent value of x.

    Parameters
    ----------
    x : int, float, Dual
      Input to the tangent function.
    
    Returns
    -------
    value : int, float, Dual
      The tangent value of the dual number implementation or the tangent value of a real number.

    """
    if isinstance(x, Node):
        child = Node(np.tan(x.value))
        x.children.append({'partial_der':1/(np.cos(x.value)**2), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.tan(x.real), 1/np.cos(x.real)**2*np.asarray(x.dual))
    else:
        return np.tan(x)

# Inverse trig functions
def arcsin(x):
    """
    Return the arcsine value of x.

    Parameters
    ----------
    x : int, float, Dual
      Input to the arcsine function.

    Returns
    -------
    value : int, float, Dual
      The arcsine value of the dual number implementation or the arcsine value of a real number.

    """
    if isinstance(x,Node):
        child = Node(np.arcsin(x.value))
        temp = 1 - x.value**2
        if temp <= 0:
            raise ValueError('The domain of sqrt should be larger than 0')
        x.children.append({'partial_der':1/(np.sqrt(temp)), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.arcsin(x.real), x.dual / np.sqrt(1 - x.real**2))
    else:
        return np.arcsin(x)


def arccos(x):
    """
    Return the arccosine value of x.

    Parameters
    ----------
    x : int, float, Dual
      Input to the arccosine function.
    
    Returns
    -------
    value : int, float, Dual
      The arccosine value of the dual number implementation or the arccosine value of a real number.
    
    """
    if isinstance(x,Node):
        child = Node(np.arccos(x.value))
        temp = 1 - x.value**2
        if temp <= 0:
            raise ValueError('The domain of sqrt should be larger than 0')
        x.children.append({'partial_der':-1/(np.sqrt(temp)), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.arccos(x.real), -x.dual / np.sqrt(1 - x.real**2))
    else:
        return np.arccos(x)


def arctan(x):
    """
    Return the arctangent value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the arctangent function.
    
    Returns
    -------
    value : int, float, Dual
      The arctangent value of the dual number implementation or the arctangent value of a real number.

    """
    if isinstance(x,Node):
        child = Node(np.arctan(x.value))
        x.children.append({'partial_der':1/(1+x.value**2), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.arctan(x.real), x.dual / (1 + x.real**2))
    else:
        return np.arctan(x)

# Exponentials
def exp(x):
    """
    Return the exponential value of x with base e.

    Parameters
    ----------
    x : int, float, Dual
      Input to the exponential function with base e.
    
    Returns
    -------
    value : int, float, Dual
      The exponential value of the dual number implementation or the exponential value of a real number with base e.

    """
    if isinstance(x,Node):
        child = Node(np.exp(x.value))
        x.children.append({'partial_der':np.exp(x.value), 'node':child})
        return child
    elif isinstance(x, Dual):
        return Dual(np.exp(x.real), np.exp(x.real) * x.dual)
    else:
        return np.exp(x)

def exponential(base, x):
    """
    Return the exponential value of x with specified base.

    Parameters
    ----------
    base: int, float
      Base of the exponential function.

    x : int, float, Dual
      Input to the exponential function with specified base.
    
    Returns
    -------
    value : int, float, Dual
      The exponential value of the dual number implementation or the exponential value of a real number with specified base.
    
    """
    if isinstance(x,Node):
        child = Node(np.exp(x.value))
        x.children.append({'partial_der':base**x.value, 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(base**x.real, np.log(base) * (base**x.real) * x.dual)
    else:
        return base**x


# Hyperbolic functions
def sinh(x):
    """
    Return the sinh value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the sinh function.
    
    Returns
    -------
    value : int, float, Dual
      The sinh value of the dual number implementation or the sinh value of a real number.

    """
    if isinstance(x,Node):
        child = Node(np.sinh(x.value))
        x.children.append({'partial_der':np.cosh(x.value), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(np.sinh(x.real), np.cosh(x.real) * x.dual)
    else:
        return np.sinh(x)

def cosh(x):
    """
    Return the cosh value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the cosh function.
    
    Returns
    -------
    value : int, float, Dual
      The cosh value of the dual number implementation or the cosh value of a real number.

    """
    if isinstance(x,Node):
        child = Node(np.cosh(x.value))
        x.children.append({'partial_der':np.sinh(x.value), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(np.cosh(x.real), np.sinh(x.real) * x.dual)
    else:
        return np.cosh(x)

def tanh(x):
    """
    Return the tanh value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the tanh function.
    
    Returns
    -------
    value : int, float, Dual
      The tanh value of the dual number implementation or the tanh value of a real number.

    """
    if isinstance(x,Node):
        child = Node(np.tanh(x.value))
        x.children.append({'partial_der':1/np.cosh(x.value)**2, 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(np.tanh(x.real), (1 - np.tanh(x.real)**2) * x.dual)
    else:
        return np.tanh(x)

# Logistic function
def logistic(x):
    """
    Return the logistic value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the logistic function.
    
    Returns
    -------
    value : int, float, Dual
      The logistic value of the dual number implementation or the logistic value of a real number.

    """
    if isinstance(x,Node):
        child = Node(1/(1+np.exp(-x.value)))
        nom = np.exp(x.value)
        dom = (1+np.exp(x.value))**2
        x.children.append({'partial_der':nom/dom, 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(1 / (1 + np.exp(-x.real)), np.exp(-x.real) * x.dual / (1 + np.exp(-x.real))**2)
    else:
        return 1 / (1 + np.exp(-x))


# Logarithms
def log(x):
    """
    Return the logarithm value of x with base e.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the logarithm function with base e.
    
    Returns
    -------
    value : int, float, Dual
      The logarithm value of the dual number implementation or the logarithm value of a real number with base e.

    """
    if isinstance(x,Node):
        child = Node(np.log(x.value))
        x.children.append({'partial_der':(1/(x.value)), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        if x.real <= 0:
            raise ValueError('Domain of logarithm should be greater than 0')
        return Dual(np.log(x.real), x.dual / x.real)
    else:
        return np.log(x)

def log2(x):
    """
    Return the logarithm value of x with base 2.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the logarithm function with base 2.
    
    Returns
    -------
    value : int, float, Dual
      The logarithm value of the dual number implementation or the logarithm value of a real number with base 2.

    """
    if isinstance(x,Node):
        child = Node(np.log2(x.value))
        x.children.append({'partial_der':(1/(x.value*np.log(2))), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        if x.real <= 0:
            raise ValueError('Domain of logarithm should be greater than 0')
        return Dual(np.log2(x.real), x.dual / (x.real * np.log(2)))
    else:
        return np.log2(x)

def log10(x):
    """
    Return the logarithm value of x with base 10.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the logarithm function with base 10.
    
    Returns
    -------
    value : int, float, Dual
      The logarithm value of the dual number implementation or the logarithm value of a real number with base 10.

    """
    if isinstance(x,Node):
        child = Node(np.log10(x.value))
        x.children.append({'partial_der':(1/(x.value*np.log(10))), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        if x.real <= 0:
            raise ValueError('Domain of logarithm should be greater than 0')
        return Dual(np.log10(x.real), x.dual / (x.real * np.log(10)))
    else:
        return np.log10(x)

def logarithm(x, base):
    """
    Return the logarithm value of x with specified base.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the logarithm function with specified base.
    
    base: int
      Base of the logarithm function.
    
    Returns
    -------
    value : int, float, Dual
      The logarithm value of the dual number implementation or the logarithm value of a real number with specified base.

    """
    if isinstance(x,Node):
        child = Node(np.log(x.value)/np.log(base))
        x.children.append({'partial_der':(1/(x.value*np.log(base))), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        if x.real <= 0:
            raise ValueError('Domain of logarithm should be greater than 0')
        return Dual(np.log(x.real) / np.log(base), x.dual / (x.real * np.log(base)))
    else:
        return np.log(x) / np.log(base)


# Square root
def sqrt(x):
    """
    Return the square root value of x.
    
    Parameters
    ----------
    x : int, float, Dual
      Input to the square root function.
    
    Returns
    -------
    value : int, float, Dual
      The square root value of the dual number implementation or the square root value of a real number.

    """
    if isinstance(x,Node):
        child = Node(x.value**(1/2))
        x.children.append({'partial_der':((1/2)*x.value**(-1/2)), 'node':child}) 
        return child
    elif isinstance(x, Dual):
        return Dual(np.sqrt(x.real), 2 * x.real * x.dual)
    else:
        return np.sqrt(x)


# if __name__=='__main__':
#     val = Dual(3,1)
#     val2 = Dual(2,[1,2])
#     z = sin(val)
#     print(z)

#     print(cos(val))
#     print(tan(val2))

#     val = Dual(0.5,0.5)
#     print(arcsin(val))

#     val=Dual(0.5,0.5)
#     print(arccos(val))

#     print(arctan(val))

#     print(exp(val))
#     base = 2
#     print(exponential(2,val))

#     print(sinh(val))
#     print(cosh(val))
#     print(tanh(val))
#     print(logistic(val))
#     print(log(val))
#     print(log2(val))
#     print(log10(val))
#     print(logarithm(val,base))
#     print(sqrt(val))

