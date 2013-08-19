#polynomials.py
#Charles J. Lai
#August 18, 2013

import unimath

"""
===========
polynomials
===========
This module contains a wrapper class that represents a polynomial and
functions that can be used to analyze/evaluate a polynomial class. These
functions are in the global namespace and are not defined within the
Polynomial class. 

Addition, subtraction, division, and multiplication functionality are 
implemented as cases within the appropriate functions in the unimath (core
math functions) module for Polynomial class types as well as overloaded 
operators defined within the Polynomial class.

Contents
--------
Polynomial   - A one-dimensional polynomial class with various methods
roots()      - Find roots of polynomial given coefficients
integral()   - Integrate polynomial
derivative() - Differentiate polynomial
evaluate()   - Evaluate polynomial at given argument
sigma() 	 - Cummulative sum of a polynomial
geom() 		 - Cummulative product of a polynomial
"""

class Polynomial(object):
	"""
	Instances represent a one-dimensional polynomial. 

	===========
	Description
	===========
	A polynomial is ...
	
	The actual polynomial itself is represented as a one-dimensional list
	where the first index position is the coefficient for the 0th order 
	variable of the polynomial and so forth.

						[5, 1, 2] -> 2x^2 + x + 5

	Each polynomial contains overloaded operators for addition, subtraction
	multiplication, and division as well as a variety of other simple methods.
	However, other points of analysis are done with public functions defined
	outside the class within this module. 

	Note: Addition, subtraction, multiplication, and division can also be done
	with add(), sub(), mult(), div() from the unimath module in the core package.
	"""
	#Properties
	_formula = []	#List of polynomial coefficients
	_length = 0 	#Length of the polynomial; Immutable

	@property
	def formula(self):
		return self._formula

	@formula.setter
	def formula(self, formula):
		self._formula = formula
		self._length = len(formula)

	@property
	def length(self):
		return self._length

	#Methods
	def __init__(self, formula):
		"""
		"""
		self._formula = formula
		self._length = len(formula)

	def __str__(self):
		"""
		Returns: The string representation of the polynomial objects of form:

									ax^2 + bx + c

		Overloads the print statement for the class such that:

									>>>print polynomial_object
									"ax^2 + bx + c"

		"""
		length = self._length
		poly_string = ""
		for var in range(0, length):
			#Case 1: For the constant, 0th order value, omit the variable
			if var == 0:
				poly_string = " + " + str(self._formula[var]) + poly_string
			#Case 2: For 1st order variable, omit the chevron and 1
			elif var == 1:
				poly_string = str(self._formula[var]) + "x" + poly_string		
			#Case 2: For the last value, omit the leading plus sign
			elif var == length - 1:
				poly_string = str(self._formula[var]) + "x" + "^" + str(var) + poly_string
			#Default Case: Add leading plus to continue the polynomial string
			else:
				poly_string = " + " + str(self._formula[var]) + "x" + "^" + str(var) + poly_string
		return poly_string

	def __len__(self):
		"""
		Returns: The length of the polynomial object.

		Overloads the len function for the class such that:

					>>>len(polynomial_object)
					polynomial_object_length

		"""
		return len(self._formula)

	def __add__(self, other):
		pass

	def __sub__(self, other):
		pass

	def __mul__(self, other):
		pass

	def __div__(self, other):
		pass


def roots(poly):
	"""
	Returns: List of roots for the a given polynomial (poly)

	===========
	Description
	===========
	"""
	pass


def derivative(poly):
	"""
	Returns: Polynomial class representing the derivative of a given
	polynomial. Orignal polynomial is not changed/removed from namespace.

	===========
	Description
	===========
	###Derivative Description###
	"""
	formula = poly.formula[1:]
	#Take the derivative: Multiply coefficients by power of x and decrement
	for var in range(0, poly.length):
		formula[var] = float(formula[var]) * (var + 1)
	derivative = Polynomial(formula)
	return derivative


def integral(poly):
	"""
	Returns: Polynomial class representing the integral of a given
	polynomial. Orignal polynomial is not changed/removed from namespace.

	===========
	Description
	===========
	###Integral Description###
	"""
	formula = poly.formula
	#Take the integral: Divide coefficients by power of x and increment
	for var in range(0, poly.length):
		formula[var] = float(formula[var]) / (var + 1)
	formula = ["C"] + formula
	integral = Polynomial(formula)
	return integral


def evaluate(poly, value_of_x):
	"""
	Returns: Sum of the values of the polynomial at a specified value of x

	===========
	Description
	===========
	"""
	formula = poly.formula
	length = poly.length
	sum = 0
	for power in range(0, length):
		#If 0th order, just add constant directly
		if power == 0:
			sum = sum + formula[power]
		#Otherwise, account for the other powers
		else:
			sum = sum + (formula[power] * (value_of_x**power))
	return sum


def sigma(base=0, limit=10, increment=1, poly=[]):
	"""
	Returns:

	===========
	Description
	===========
	"""
	total_sum = 0
	while i <= limit:
		total_sum = total_sum + evaluate(poly, i)
		i += increment
	return total_sum


def geom(base=0, limit=5, increment=1, poly=[]):
	"""
	Returns:

	===========
	Description
	===========
	"""
	total_product = 0
	while i <= limit:
		total_product = total_product * evaluate(poly, i)
		i += increment
	return total_product
