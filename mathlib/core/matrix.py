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
* Array        - A one-dimensional array class with various methods
* Matrix       - A matrix class with various methods
* fliplr()     - Reverses an array or column of a matrix
* ref()        - Returns the row echelon form of a matrix
* rref()       - Returns the reduced row echelon form of a matrix
* trans()      - Returns the transpose of a matrix or array
* det()        - Returns the determinant of a matrix
* diag()       - Returns the diagonalized form of a matrix
* eig()        - Returns the eigenvector of a matrix
"""

class Matrix(object):
    """
    Instances represent a two-dimensional matrix.

    ===========
    Description
    ===========
    A matrix is a type of data structure that can hold two two-dimensional
    data on a discrete map of points. #ADD MORE DESCRIPTION/HISTORY#

    The actual matrix iteself is represented by a two-dimensional list
    wrapped in this matrix class which provides methods and properties
    for various matrix-based applications and analysis. Our implementation
    was created with Matlab-style constructors and matrix traversals in
    mind. This syntax is familiar with most people and thus a solid design
    decision for this module/package.

    Coordinate positions in the matrix start with ones (for example, the
    top left value in a matrix is at coordinate point [1, 1]).

               [1, 1]   <-----  1 2 3 4 5 
                                1 2 3 4 5
                                1 2 3 4 5
                                1 2 3 4 5
                                1 2 3 4 5

    The number of rows is denoted by the "m" property value and the number
    of columns is denoted by the "n" property value (again familiar notation
    for most people). The entire matrix object is of size m x n.

    Each matrix contains a variety of different methods for adding,
    subtracting, setting, and getting values/rows/columns as well as
    overloaded operatros for matrix scalar addition/subtraction in 
    addition to matrix multiplication and division.

    Note: Addition, subtraction, multiplication, and division can also be done
    with add(), sub(), mult(), div() from the unimath module in the core package.
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
        #Case 1: raw_matrix is a string -> Matlab style
        self._parse(raw_matrix)
        self._check()

    #Built-In Methods/Operator Overloading
    def __add__(self, other):
        """
        Returns: The sum of two matrices 
        OR
        Procedure: Scalar addition of self.

        Precondition: The two matrices must be the same size.
        """
        #Enforce the preconditions
        assert self._m == other.m, "The two matrices differ in number of rows"
        assert self._n == other.n, "The two matrices differ in number of cols"
        #Add the two matrices
        #Add a scalar to every value in the matrix
        if type(other) == int or type(other) == float:
            for x in range(0, self._m):
                for y in range(0, self._n):
                    self._matrix[x][y] = self._matrix[x][y] + other
        pass

    def __sub__(self, other):
        """
        Returns: The difference of two matrices
        OR
        Procedure: Scalar subtraction of self.

        Precondition: The two matrices must be the same size.
        """
        #Enforce the preconditions
        assert self._m == other.m, "The two matrices differ in number of rows"
        assert self._n == other.n, "The two matrices differ in number of cols"
        #Subtract the two matrices
        #Subtract the matrix by a scalar
        pass


    def __mul__(self, other):
        """
        Returns: The product of two matrices such that [self] * [other]
        OR
        Procedure: Scalar multiplication of self by other.

        Precondition: self.n == other.m

        ===========
        Description
        ===========
        Matrix multiplication is more than simple addition where cooresponding
        values in the first matrix are added to the second matrix.
        """
        #Enforce the preconditions
        assert self._n == other.m, "The dimensions of the matrices are invalid."
        #Create the return matrix
        temp_list = unimath.zeros(self._m, other.n)
        product_matrix = Matrix(temp_list)
        #Multiply the two matrices
        row_counter = 1
        col_counter = 1
        while col_counter <= other._n:
            while row_counter <= self._m:
                #Multiply the all rows by the column and get the product
                temp_row = self.get_row(row_counter)
                temp_col = other.get_col(col_counter)
                pre_sum = unimath.mult(temp_row, temp_col)
                final_sum = unimath.listsum(pre_sum)
                #Set the product to the correct space in the product matrix
                product_matrix.set(row_counter, col_counter, final_sum)
                row_counter += 1
            #Reset the row counter and continue with the mext column
            row_counter = 1
            col_counter += 1
        return product_matrix
        #Multiply the matrix by a scalar
        pass

    def __div__(self, other):
        """
        Procedure: Scalar division of self.
        """
        pass

    #Methods Proper
    def disp(self, heading = "Matrix:"):
        """
        Procedure: Prints a string representation of the matrix object
        """
        print " "
        print heading
        print " "
        #Iteratively print the elements of the matrix
        for x in range(0, self.m):
            for y in range(0, self.n):
                print '%10.3f' % self._matrix[x][y],
            print "\n"

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

        Precondition:b x and y are valid coordinates using Matlab coordinate
        rules.
        """
        #Check if the value specified is a string or an actual list.
        assert type(value) == float or type(value) == int
        self._matrix[x - 1][y - 1] = value


    def get_row(self, row_number):
        """
        Returns: The specified row in matrix self. The row is a python list.
        """
        assert row_number <= self._m and row_number > 0, "This is not a valid row number"
        return self._matrix[row_number - 1]

    def set_row(self, row_number, row): #FINISH THIS METHOD - NOT COMPLETE
        """
        Procedure: Sets the value for a specfied row.
        """
        assert type(row) == list, "The row data given is not a list."
        assert row_number >= 1 and row_number <= self.m, "The row number is invalid"
        assert len(row) == self.n, "The row given is not a valid length"
        col_number = 1
        #Iterate over columns in a single row and set values.
        for e in row:
            self.set(row_number, col_number, e)
            col_number += 1

    def get_col(self, col_number):
        """
        Returns: The specified col in matrix self. The col is a python list.
        """
        assert col_number <= self._n and col_number > 0, "This is not a valid col number"
        column = []
        row_number = 0
        while row_number < self._m:
            column = column + [self._matrix[row_number][col_number - 1]]
            row_number += 1
        return column

    def set_col(self, col_number, col):
        """
        Procedure: Sets the value for a specified column.
        """
        assert col_number <= self._n and col_number >= 1, "This is not a valid col number"
        assert type(col) == list, "The col data given is not a list."
        assert len(col) == self.m, "The column given is not a valid length."
        row_number = 1
        #Iterate over rows in a single column and set values
        for e in col:
            self.set(row_number, col_number, e)
            row_number += 1

    def add_row(self, row):
        """
        Procedure: Adds a given row to the matrix to the bottom.

        Precondition: The row must be have the same length as other rows in
        the matrix. Argument passed to row is a python list.
        """
        assert len(row) == self._n, "The row has an invalid length"
        #Add the whole row to the end of the matrix
        self._matrix = self._matrix + [row]
        self._m += 1

    def add_col(self, col):
        """
        Procedure: Adds a given col to the matrix to the right

        Precondition: The column must have the same length as other rows 
        """
        assert len(col) == self._m, "The column has an invalid length"
        #Add each element to the end of each row
        x = 0
        for y in col:
            self._matrix[x] = self._matrix[x] + [y]
            x += 1
        self._n += 1
        

    def sub_row(self, x):
        """
        Procedure: Subtracts a given row from the matrix by row number. x
        represents a specific row number.

        Precondition: x must be a valid row number
        """
        assert self._m >= x, "The row number given is too large"
        assert x > 0, "Try again with a row number > 0"
        self._matrix.remove(self._matrix[x - 1])

    def sub_col(self, y):
        """
        Procedure: Subtracts a given column from the matrix by column number.

        Precondition: y must be a valid column number.
        """
        assert self._n >= y, "The column number given is too large"
        assert y > 0, "Try again with a column number > 0"
        for x in range(0, self._m):
            self._matrix.remove(self._matrix[x][y])

    #Helper Methods
    def _parse(self, raw_matrix):
        """
        Procedure: Parses the raw_matrix string and updates the Matrix object.
        Called during object construction.

        Precondition: raw_matrix is a valid input according to the description
        in the meta documentation at the top of the document.
        """
        #Case 1: raw_matrix is a string
        if type(raw_matrix) == str:
            #Some assertions statements to QC the raw_matrix input
            assert type(raw_matrix) == str, "The matrix given is not a string"
            assert raw_matrix[0] != "[", "Use Matlab matrix notation without braces"
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
        #Case 2: raw_matrix is a valid 2D list in matrix form:
        elif type(raw_matrix) == list:
            self._matrix = raw_matrix
            self._m = len(self._matrix)
            self._n = len(self._matrix[0])
            if self._m == self._n:
                self._is_square == True

    def _check(self):
        """
        Procedure: Checks if the raw input was valid by QCing the properties
        of the matrix. Called during object construction.
        """
        #Test if the rest of the rows are the same length
        for r in range(0, self.m):
            assert len(self._matrix[r]) == self._n, "Invalid row lengths"
            assert type(self._matrix[r]) == list, "Some rows aren't lists"


#======================
#   Matrix Functions
#======================
def ref(matrix):
    """
    Returns: The row echelon form of a given matrix.
    """
    pass


def rref(matrix):
    """
    Returns: The reduced row echelon form of a given matrix.
    """
    #==============
    #FORWARD PHASE:
    #==============
    #
    #1) Begin with the leftmost nonzero column. This is a pivot column. The pivot
    #   position is at the top.
    pivot_col = matrix.get_col()
    #2) Select a nonzero entry in the pivot column as a pivot. If necessary, interchange rows 
    #   to move this entry into the pivot position. 
    #
    #3) Use row addition operations to create zeros in all positions below the pivot.
    #
    #4) Cover (or ignore) the row containing the pivot position and cover all rows, if
    #   any, above it. apply steps 1-3 to the submatrix that remains. Repeat the
    #   process until there are no more nonzero rows to modify.
    #
    #===============
    #BACKWARD PHASE:
    #===============
    #
    #1) Beginning with the rightmost pivot and working upward and to the left, create
    #   zeros above each pivot. If a pivot is not 1, make it 1 by a scaling operation.
    pass

def trans(matrix):
    """
    Returns: The transpose of a given matrix.
    """
    transpose = unimath.zeros(matrix.n, matrix.m)
    transpose = Matrix(transpose)
    col_count = 1
    while col_count <= matrix.n:
        col = matrix.get_col(col_count)
        ele_count = 1
        #Set each value in the column to cooresponding row values
        for e in col:
            transpose.set(col_count, ele_count, e)
            ele_count += 1
        #Repeat for the next column
        col_count += 1
    return transpose


def det(matrix):
    """
    Returns: The determinant of a given matrix.
    """
    pass


def diag(matrix):
    """
    Returns: The diagonalized form of a given matrix.
    """
    pass


def sym(matrix):
    """
    Returns: The symmetrical form of a given matrix.
    """
    return matrix * trans(matrix)


def eig(matrix):
    """
    Returns: eigenvectors of a given matrix.
    """
    pass


#======================
#   Property Testers
#======================
def is_square(matrix):
    """
    Returns: True if the matrix is square, else False.

    Precondition: matrix is a Matrix object.
    """
    pass


def is_li(matrix):
    """
    """
    pass
