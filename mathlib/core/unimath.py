#unimath.py
#Charles J. Lai
#August 8, 2013

"""
========================
Universal Math Functions
========================
Core mathematical functions that are used by almost all packages in MathLib.

Not all of these are necessary or useful (i.e. add, multiply, add etc), but 
were decided to be included for completeness/thoroughness sake.

--------
Contents
--------

List Operations
---------------
* inclist(list, value)
* sublist(list, value)
* mullist(list, value)
* divlist(list, value)

Basic Math:
-----------
* add(a, b)
* subtract(a, b)
* multiply(a, b)
* divide(a, b)
* factorial(n)

Markup Languages:
-----------------
* latex() - Returns the LaTeX code for a matrix or polynomial object.

"""
#=====================
#   List Operations
#=====================

def inclist(list, value):
    """
    Returns: A new list where each value in a given list is incremented by
    a specified value.

    ===========
    Description
    ===========
    """
    new_list = []
    for i in range(0, len(list)):
        #Increment each item in the list by value for all indices i
        new_list = new_list + [(list[i] + float(value))]
    return new_list


def sublist(list, value):
    """
    Returns: A new list where each value in a given list is subtracted by
    a specified value.

    ===========
    Description
    ===========
    """
    new_list = []
    for i in range(0, len(list)):
        #Subtract each item in the list by value for all indices i
        new_list = new_list + [(list[i] - float(value))]
    return new_list


def mullist(list, value):
    """
    Returns: A new list where each value in a given list is multiplied by
    a specified value.

    ===========
    Description
    ===========
    """
    new_list = []
    for i in range(0, len(list)):
        #Multiply each item in the list by value for all indices i
        new_list = new_list + [(list[i] * float(value))]
    return new_list


def divlist(list, value):
    """
    Returns: A new list where each value in a given list is divided by
    a specified value.

    ===========
    Description
    ===========
    """
    new_list = []
    for i in range(0, len(list)):
        #Divide each item in the list by value for all indices i
        new_list = new_list + [(list[i] / float(value))]
    return new_list


#================
#   Basic Math
#================
def add(a, b):
    """
    Return: The sum of two items a and b.
    """
    #Attempt to use overloaded operators
    try:
        return a + b
    #If this fails, go case by case until it works.
    except Exception:
        if type(a) == Polynomial and type(b) == Polynomial:
            pass
            


def sub(a, b):
    """
    Return: The difference of two items a and b
    """
    #Attempt to use overloaded operators
    try:
        return a - b
    #If this fails, go case by case until it works.
    except Exception:
        pass


def div(a, b):
    """
    Returns: The quotient of two items a and b.
    """
    #Attempt to use overloaded operators
    try:
        return a / b
    #If this fails, go case by case until it works.
    except Exception:
        pass


def mult(a, b):
    """
    Returns: The product of two items a and b.
    """
    #Attempt to use overloaded operators
    try:
        return a * b
    #If this fails, go case by case until it works.
    except Exception:
        pass


def factorial(n):
    """
    Computes the factorial of an integer n. Not optimized with memoization.
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def GCD(a, b):
    pass

#======================
#   Markup Languages
#======================

def latex(obj):
    """
    """
    markup_code = ""
    if type(obj) == Polynomial:
        formula = obj.formula
    return markup_code

