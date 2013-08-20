#matrix.py
#Charles J. Lai
#August 18, 2013

import unimath

"""
======
matrix
======
This module contains a wrapper class that represents a matrix and
functions that can be used to analyze/evaluate a matrix class. 

Addition, subtraction, division, and multiplication functionality are 
implemented as cases within the appropriate functions in the unimath (core
math functions) module for Matrix class types as well as overloaded 
operators defined within the Matrix class.

Contents
--------
* Array 	   - A one-dimensional array class with various methods
* Matrix 	   - A matrix class with various methods
* fliplr() 	   - Reverses an array or column of a matrix
* eig() 	   - Returns the eigenvector of a matrix
* transpose()  - Returns the transpose of a matrix or array
"""

class Matrix(object):
	"""
	"""
	#Properties
	_matrix = None
	_number_of_rows = 0
	_number_of_columns = 0
	_is_square = False
	_is_li = False

	#Methods
	def __init__(self, pre_matrix):
		#Test if the "pre_matrix" argument is valid
		assert type(pre_matrix) == list, "Argument given is not a 2D-List"
		assert _has_same_length_rows(pre_matrix) == True, "Argument has different length rows"
		#Set the properties
		self._matrix = pre_matrix
		self._number_of_rows = len(self._matrix)
		self._number_of_columns = len(self._matrix[0])
		if self._number_of_rows == self._number_of_columns:
			self._is_square == True

	def __str__(self):
		pass


#======================
#	Property Testers
#======================

def is_square(matrix):
	pass


def is_li(matrix):
	pass


def _has_same_length_rows(pre_matrix):
	"""
	"""
	#Check the first row
	first_row_length = len(pre_matrix[0])
	#Test if the rest of the rows are the same length
	for r in range(1, len(pre_matrix)):
		if len(pre_matrix[r]) != first_row_length:
			return False
	return True

