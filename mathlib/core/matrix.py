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
	_row_length = 0
	_col_length = 0
	_number_of_rows = 0
	_number_of_columns = 0
	_is_square = False
	_is_li = False

	@property 
	def matrix(self):
		return self._matrix

	@matrix.setter
	def matrix(self, pre_matrix):
		assert type(pre_matrix) == list, "Argument given is not a 2D-List"
		assert _has_same_length_rows(pre_matrix) == True, "Argument has different length rows"
		self._matrix = pre_matrix

	@property #immutable
	def row_length(self):
		return self._row_length

	@property #immutable
	def col_length(self):
		return self._col_length

	@property #immutable
	def number_of_rows(self):
		return self._number_of_rows

	@property #immutable
	def number_of_columns(self):
		return self._number_of_columns

	@property #immutable
	def is_square(self):
		return self._is_square

	@property #immutable
	def is_li(self):
		return self._is_li

	#Methods
	def __init__(self, pre_matrix):
		"""
		"""
		#Test if the "pre_matrix" argument is valid
		assert type(pre_matrix) == list, "Argument given is not a 2D-List"
		assert _has_same_length_rows(pre_matrix) == True, "Argument has different length rows"
		#Set the matrix
		self._matrix = pre_matrix
		#Set row/col length/numbers
		self._number_of_rows = len(self._matrix)
		elf._number_of_columns = len(self._matrix[0])
		self._col_length = self._number_of_rows
		self._row_length = self._number_of_columns
		#Set whether the matrix is a square matrix
		if self._number_of_rows == self._number_of_columns:
			self._is_square == True

	def __str__(self):
		"""
		"""
		pass

	def __add__(self):
		"""
		"""
		pass

	def __sub__(self):
		"""
		"""
		pass

	def __mul__(self):
		"""
		"""
		pass

	def __div__(self):
		"""
		"""
		pass
#======================
#	Matrix Functions
#======================

def add_row(matrix, row):
	"""
	Procedure: Adds a given row to a specified matrix

	Preconditions: The row must be have the same length as other rows in
	the matrix.
	"""
	assert len(row) == matrix.row_length, "The row has an invalid length"
	pass


def add_col(matrix, col):
	"""
	"""
	pass


def sub_row(matrix, row_number):
	"""
	"""
	pass


def sub_col(matrix, col_number):
	"""
	"""
	pass


def ref(matrix):
	"""
	"""
	pass


def rref(matrix):
	"""
	"""
	pass


def trans(matrix):
	"""
	"""
	pass


def det(matrix):
	"""
	"""
	pass


def diag(matrix):
	"""
	"""
	pass


def eig(matrix):
	"""
	"""
	pass
#======================
#	Property Testers
#======================

def is_square(matrix):
	"""
	"""
	pass


def is_li(matrix):
	"""
	"""
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

