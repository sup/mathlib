#random.py
#Charles J. Lai
#August 18, 2013

import time

"""
======
random
======
This module contains a variety of methods/functions for generating sequences
of random numbers with various distributions. This can be used for a variety 
of different purposes with statistics, cryptography, finance, and
other fields that may require large sequences of random numbers.

Contents
--------
Pseudorandom Generators (Uniformly Distributed):
* LCG

Distributions:
* Normal/Gaussian
* Poisson

"""
#=============================
#	Pseudorandom Generators
#=============================
def LCG(limits=[0,1], size=10):
	"""
	Returns: A series of pseudorandom numbers of range *limits* and size
	*size*. Default: 10 numbers with range between 0 and 1.

	===========
	Description
	===========
	A standard technique for generating pseudorandom numbers is known as
	he linear congruential generator (LCG). Choose:

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
	return series


#===================
#	Distributions
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





