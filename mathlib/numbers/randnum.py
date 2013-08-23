#random.py
#Charles J. Lai
#August 18, 2013

import time

"""
=======
randnum
=======
This module contains a variety of methods/functions for generating sequences
of random numbers with various distributions. This can be used for a variety 
of different purposes such as cryptography, Monte Carlo simulations, as well
as procedural generation.

Pseudorandom Number Generators (PRNG):
======================================
Also known as a deterministic random bit generator (DRBG); a PRNG is an
algorithm for generating a sequence of numbers that approximates properties
of truly random numbers. A PRNG is deterministic and dependent on a small 
set of initial values (known as the state) which includes a stochastic 
seed. Common typees include linear congruential generators, lagged Fibbonachi
generators, and linear feedback shift registers. Special PRNGs that have
strong randomness guarantees based on computational hardness assumptions
such as the Blum Blum Shub, Fortuna, and Mersenne Twister algorithms.

Contents
--------
Pseudorandom Generators (Uniformly Distributed):
* LCG
* Park-Miller
* Mersenne Twister
* ICG

Distributions:
* Normal/Gaussian
* Poisson

"""
#=============================
#   Pseudorandom Generators
#=============================
def LCG(limits=[0,1], size=1):
    """
    Returns: A series of pseudorandom numbers of range *limits* and size
    *size*. Default: 1 number with range between 0 and 1.

    ===========
    Description
    ===========
    Linear Congruential Generator (Basic)
    A standard technique for generating pseudorandom numbers is known as
    he linear congruential generator (LCG). This class of PRNG has:

                            *A modulus -> m
                            *A multiplier -> a
                            *An increment -> c
                            *A random seed -> Z

    Our values were chosen trough careful, scientific, face-to-keyboard
    smashing. 

    Then, given a random seed Z, we generate the first pseudorandom number.

                            X_0 = (aZ + c) mod m

    Afterwords, the remaining numbers are generated recursively such that:

                            X_n+1 = (aX_n + c) mod m

    This is good enough for most applications, but for serious cryptographic
    applications by companies and professionals, more complex random number
    generators are used. 
    """
    #Initialize: empty list, seed, modulus, multiplier, and increment.
    series = []
    seed = time.clock()
    modulus = 12387409          
    multiplier = 11234345 
    increment = 7569
    #Generate the first pseudorandom number and add it to the empty list.
    next = (seed * multiplier + increment) % modulus
    series = series + [next]
    #Then generate the remaining pseudorandom numbers with LCG. 
    for n in range(0, size-1):
        next = (series[n] * multiplier + increment) % modulus
        series = series + [next]
    #Adjust the numbers to account for the range specified.
    limit_divisor = modulus/limits[1]
    for i in range(0, len(series)):
        series[i] = series[i]/limit_divisor
    if size == 1:
        return series[0]
    return series


def lehmer(limits=[0,1], size=1):
    """
    Returns: A series of pseudorandom numbers of range *limits* and size
    *size*. Default: 1 number with range between 0 and 1.

    ===========
    Description
    ===========
    Lehmer RNG A.K.A. Park-Miller RNG

    This PRNG is a variant of linear congruential genertors that operates
    in multiplicative group of integers modulo n of the form:

                         X_n+1 = (aX_n) mod n
    
    This is a special case of LCG without a constant increment c and where 
    the modulus n is a prime number or power of a prime number. The multiplier
    a is an element of high multiplicative order modulo n (i.e. a primitive
    root modulo n). The seed X0 is co-prime to n.

    Park and Miller suggested a Lehmer RNG with parameters:

                        n = 2^31 - 1 (Mersenne Prime M31)
                        a = 7^5 (Primitive root mod M31)
    
    These parametes are now know as MINSTD and are used in this particular
    python implementation of the Lehmer RNG.
    """
    #Initialize: empty list, seed, modulus, multiplier, and increment.
    series = []
    seed = time.clock()
    modulus = 2147483647    #Mersenne Prime M31 = 2^31 - 1          
    multiplier = 16807      #Primitive Root modulo M31 = 7^5
    #Generate the first pseudorandom number and add it to the empty list.
    next = (seed * multiplier) % modulus
    series = series + [next]
    #Then generate the remaining pseudorandom numbers with Lehmer RNG. 
    for n in range(0, size-1):
        next = (series[n] * multiplier) % modulus
        series = series + [next]
    #Adjust the numbers to account for the range specified.
    limit_divisor = modulus/limits[1]
    for i in range(0, len(series)):
        series[i] = series[i]/limit_divisor
    if size == 1:
        return series[0]
    return series

def mersenne_twister(limits=[0,1], size=1):
    """
    Returns:

    ===========     
    Description     
    ===========     
    The Mersenne twister is a PRNG developed in 1997 by Makoto Matsumoto
    and Takuji Nishimura that is based on a matrix linear recurrence over 
    a finite binary field F_2. It provides for fast generation of quality 
    pseudorandom numbers, having been designed specifically to rectify many 
    of the flaws found in older algorithms. 

    Its name derives from the fact that period length is chosen
    to be a Mersenne prime. There are at least two common variants of the 
    algorithm, differing only in the size of the Mersenne primes used. The 
    newer and more commonly used one is the Mersenne Twister MT19937, with 
    32-bit word length. There is also a variant with 64-bit word length, 
    MT19937-64, which generates a different sequence. For a k-bit word length,
    the Mersenne Twister generates numbers with an almost uniform
    distribution in the range [0, 2^k-1]. 

    This is the default type of PRNG used in python. This implementation will
    use the Mersenne Twister, MT19937 variant for 32-bit integers. 
    """
    #Create a length 624 list to store generator state
    MT = range(0,624)
    index = 0
    #Initialize the generator from a seed
    #Extract a tempered Pseudorandom number based on the index-th value
    #Generate an array of 624 untempered numbers
    pass


def ICG(limits=[0,1], size):
    """
    Returns:

    ===========
    Description
    ===========
    Generalized Inversive Congruential PRNG
    """
    pass


#===================
#   Distributions
#===================

def normal(random_numbers):
    pass


def exponential(random_numbers, alpha, beta):
    pass


def tdist(random_numbers):
    pass


def chisquare(random_numbers):
    pass


def poisson(random_numbers):
    pass





