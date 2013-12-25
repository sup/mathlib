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

Basic Math:
-----------
* add(a, b)
* subtract(a, b)
* multiply(a, b)
* divide(a, b)
* factorial(n)

List Operations
---------------
* fliplr(list)
* listsum(list, value)
* inclist(list, value)
* sublist(list, value)
* mullist(list, value)
* divlist(list, value)
* zeros(m, n)

Markup Languages:
-----------------
* latex() - Returns the LaTeX code for a matrix or polynomial object.

"""

#== Basic Algebraic Functions ============================================
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
        #Case: a and b are both lists
        if type(a) == list and type(b) == list:
            function = lambda m,n: m+n
            return map(function, a, b)
            

def sub(a, b):
    """
    Return: The difference of two items a and b
    """
    #Attempt to use overloaded operators
    try:
        return a - b
    #If this fails, go case by case until it works.
    except Exception:
        #Case: a is a list, b is a scalar
        if type(a) == list and isinstance(b, (int,long,float)):
            return sublist(a, b)
        #Case: a is a scalar, b is a list
        #Case: a and b are both lists
        if type(a) == list and type(b) == list:
            function = lambda m,n: m-n
            return map(function, a, b)


def div(a, b):
    """
    Returns: The quotient of two items a and b.
    """
    #Attempt to use overloaded operators
    try:
        return a / b
    #If this fails, go case by case until it works.
    except Exception:
        #Case: a and b are both lists
        if type(a) == list and type(b) == list:
            function = lambda m,n: m/n
            return map(function, a, b)


def mult(a, b):
    """
    Returns: The product of two items a and b.
    """
    #Attempt to use overloaded operators
    try:
        return a * b
    #If this fails, go case by case until it works.
    except Exception:
        #Case: a and b are both lists
        if type(a) == list and type(b) == list:
            function = lambda m,n: m*n
            return map(function, a, b)

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


#== Sequence Operations ==================================================
def listsum(list):
    """
    Returns: The cummulative sum of values in a list.

    Precondition: values in the lists are numbers.
    """
    sum = 0
    for element in list:
        sum = sum + element
    return sum

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


def zeros(m, n):
    """
    Returns: A list of zeroes with dimensions m x n
    """
    matrix = [[0] * n]
    counter = 0
    #Add the rest of the rows of zeros
    while counter < m - 1:
        matrix = matrix + [[0]*n]
        counter += 1
    return matrix


def fliplr(list):
    """
    Returns: A reversed version of a given sequence.
    """
    #Case 1: list is a simple list
    if type(list) == list:
        flipped_list = []
        #For each element in list, add to the front of flipped_list
        for element in list:
            flipped_list = [element] + flipped_list
        return flipped_list


#== Markup Code Generators ===============================================
def latex(obj):
    """
    """
    markup_code = ""
    if type(obj) == Polynomial:
        formula = obj.formula
    return markup_code

