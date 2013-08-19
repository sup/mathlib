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

Basic Functions:
----------------
*add(a, b)
*subtract(a, b)
*multiply(a, b)
*divide(a, b)
*factorial(n)
"""

#===============
#	Functions
#===============
def add(a, b):
	"""
	"""
	#Attempt to use overloaded operators
	try:
		return a + b
	#If this fails, go case by case until it works.
	except Exception:
		pass

def sub(a, b):
	"""
	"""
	#Attempt to use overloaded operators
	try:
		return a - b
	#If this fails, go case by case until it works.
	except Exception:
		pass


def div(a, b):
	"""
	"""
	#Attempt to use overloaded operators
	try:
		return a / b
	#If this fails, go case by case until it works.
	except Exception:
		pass


def mult(a, b):
	"""
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


