#probability.py
#Charles J. Lai
#August 8, 2013

import mathlib.core.unimath

"""
==========================
Probability (And Counting)
===========================
[INSERT DECRIPTION]

--------
Contents
--------

Counting:
---------
*combination(a, b)
*permute(a, b)

"""

def combination(n ,r):
	"""
	Calculates the result of a combination of *n* numbers and *r* choices.
	The result of the function is simply: n!/r!(n-r)!
	"""
	return factorial(n)/(factorial(r) * factorial(n-r)


def permute(n, r):
	"""
	Calculates the result of a permtation of *n* numbers and *r* choices.
	The result of the function is simply: n!/(n-r)!
	"""
	return factorial(n)/factorial(n-r)