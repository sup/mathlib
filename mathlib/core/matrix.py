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

Usage/Syntax
============
Creating a matrix using a constructor or setter requires the use of a 
Matlab-like syntax. For example, a 3*3 matrix:

								1 2 3
								3 2 1
								5 1 4
		
has a raw string expression using Matlab syntax: "1,2,3;3,2,1;5,1,4"
with no spaces, using semi-colons to separate rows, and commas to
separate elements within each row. X and Y coordinates also mimic
Matlab's non-zero coordinate system for traversing a matrix.

Contents
--------
* Array 	   - A one-dimensional array class with various methods
* Matrix 	   - A matrix class with various methods
* fliplr() 	   - Reverses an array or column of a matrix
* ref() 	   - Returns the row echelon form of a matrix
* rref() 	   - Returns the reduced row echelon form of a matrix
* trans() 	   - Returns the transpose of a matrix or array
* det() 	   - Returns the determinant of a matrix
* diag() 	   - Returns the diagonalized form of a matrix
* eig() 	   - Returns the eigenvector of a matrix
"""

class Matrix(object):
	"""
	"""
	#Properties
	_matrix = None
	_m = 0
	_n = 0
	_is_square = False

	@property 
	def matrix(self):
		return self._matrix

	@matrix.setter
	def matrix(self, raw_matrix):
		self._matrix = raw_matrix

	@property #immutable
	def m(self):
		return self._m

	@property #immutable
	def n(self):
		return self._n

	@property #immutable
	def is_square(self):
		return self._is_square

	#Constructor
	def __init__(self, raw_matrix):
		"""
		Constructor: Create a new instance of a Matrix
        
        Precondition: raw_matrix is a valid matrix input according to the
        description in the meta documentation.
		"""
		#Set and check the matrix
		self._parse(raw_matrix)
		self._check()

	#Built-In Methods/Operator Overloading
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

	#Methods Proper
	def disp(self, heading = "Matrix:"):
		"""
		Procedure: Prints a string representation of the matrix object
		"""
		print heading
		#Iteratively print the elements of the matrix
        for x in range(0, self._m):
            for y in range(0, self._n):
                print '%10.3f' % self._matrix[x][y],
        #Print an empty line
		print ""

	def get(self, x, y):
		"""
		Returns: Value a specified coordinate point within the matrix.

		Precondition: x and y are valid coordinates using Matlab coordinate
		rules.
		"""
		return self._matrix[x-1][y-1]

	def set(self, x, y, value):
		"""
		Procedure: Sets value at a specfied coordinate point to a new value.

		Precondition: x and y are valid coordinates using Matlab coordinate
		rules.
		"""
		#Check if the value specified is a string or an actual list.
		assert type(value) == float or type(value) == int
		self._matrix[x-1][y-1] = value

	def add_row(self, row):
		"""
		Procedure: Adds a given row to the matrix

		Preconditions: The row must be have the same length as other rows in
		the matrix. Argument passed to row is a python list.
		"""
		assert len(row) == self._row_length, "The row has an invalid length"

	def add_col(self, col):
		"""
		Procedure: Adds a given col to the matrix
		"""
		pass

	def sub_row(self, row_number):
		"""
		Procedure: Subtracts a given row from the matrix by row number
		"""
		pass

	def sub_col(self, col_number):
		"""
		Procedure: Subtracts a given column from the matrix by column number
		"""
		pass

	#Helper Methods
	def _parse(self, raw_matrix):
		"""
		Procedure: Parses the raw_matrix string and updates the Matrix object.

		Precondition: raw_matrix is a valid input according to the description
		in the meta documentation at the top of the document.
		"""
		#Initialize default values
		self._m = -1
		self._n = -1
		#Split the matrix up into rows of strings and set m to len(self._matrix
		self._matrix = raw_matrix.split(';')
		self._m = len(self._matrix)
		#Continue parsing the input, make rows into lists of numbers
		for x in range(0, self._m):
			self._matrix[x] = self.matrix[x].split(",")
			self._matrix[x] = list(map(float, self.matrix[x]))
		#Set n to the number of elements in each row
		self._n = len(self._matrix[0])
		#Set whether the matrix is a square matrix
		if self._m == self._n:
			self._is_square == True


	def _check(self):
		"""
		Procedure: Checks if the raw input was valid by QCing the properties
		of the matrix.
		"""
		#Test if the rest of the rows are the same length
		for r in range(0, len(self._m)):
			assert len(self._matrix[r]) == self._n, "Invalid row lengths"
			assert type(self._matrix[r]) == list, "Some rows aren't lists"

#======================
#	Matrix Functions
#======================
def fliplr(array):
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

