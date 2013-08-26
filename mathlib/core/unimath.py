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
* sum(list, value)
* inclist(list, value)
* sublist(list, value)
* mullist(list, value)
* divlist(list, value)
* zeros(m, n)

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
        #LARGE SWITCH-CASE SYSTEM:
        #Case: a AND b are LIST types. Multiply respective elements
        if type(a) == list and type(b) == list:
            try:
                temp_list = []
                for element_a in a:
                    index_b = 0
                    temp_list = temp_list + [element_a * b[index_b]]
                    index_b += 1
                return temp_list
            except Exception:
                print "These lists are not the same size."

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

