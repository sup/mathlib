#Charles J. Lai
#primes.py
#August 7, 2013

import random

"""
==============
    primes
==============

This module contains bread and butter functions for basic prime number 
analysis including primality tests, prime factorizations, and other 
functions. Part of the MathLib/numbers package.

"""
#=======================
#   Prime Factorization
#=======================
def factor_primes(value):
    pass

#=====================
#   Primality Tests
#=====================
def fermat_primality(value, counter):
    pass

#DEBUG THIS
def solovay_strassen(value, counter):
    """
    Returns: False if the value is a composite number, else it 
    returns True which indicates the number is probably prime
    
    Description: Iterates `counter` amount of times for the Monte Carlo
    test.
    """
    #Initialize the loop counter
    i = 0
    while i <= counter:
        rand = random.randint(2, value-1)
        x = (value/rand)
        print x
        #If the logical conditions are met, we know its composite
        if x == 0 or (rand**((value-1)/2)) % value != x % value:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print fermat_primality(10, 100)
    print fermat_primality(17, 100)
    print solovay_strassen(10, 100)
    print solovay_strassen(17, 100)

