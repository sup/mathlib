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
    overloaded operators for matrix scalar addition/subtraction in 
    addition to matrix multiplication and division.

    Note: Addition, subtraction, multiplication, and division can also be done
    with add(), sub(), mult(), div() from the unimath module in the core package.
    """
    #Fields
    _data = None
    _m = 0
    _n = 0
    _is_square = False

    #Immutable Properties
    @property 
    def m(self):
        return self._m

    @property 
    def n(self):
        return self._n

    @property 
    def is_square(self):
        return self._is_square

    #Built-in Functions
    def __init__(self, raw_data):
        """
        Constructor: Create a new instance of a Matrix
        
        Precondition: raw_data is a valid matrix input according to the
        description in the meta documentation.
        """
        #Case 1: raw_data is a string -> Matlab style
        self._parse(raw_data)
        self._check()

    #Arithemetic Operator Overloading
    def __add__(self, other):
        """
        Returns: The sum of two matrices 
        OR
        Procedure: Scalar addition of self.

        Precondition: The two matrices must be the same size.
        """
        #Matrix Addition
        if type(self) == Matrix and type(other) == Matrix:
            #Enforce the preconditions
            assert self.m == other.m, "The two matrices differ in number of rows"
            assert self.n == other.n, "The two matrices differ in number of cols"
            #Create the return matrix
            sum_matrix = Matrix(unimath.zeros(self.m, other.n))
            #Subtract the two matrices
            x = 1
            while x <= other.m:
                row_a = self.get_row(x)
                row_b = other.get_row(x)
                difference = unimath.add(row_a, row_b)
                sum_matrix.set_row(x,difference)
                x += 1
            return sum_matrix
        #Add a scalar to every value in the matrix
        if type(other) == int or type(other) == float:
            for x in range(0, self.m):
                for y in range(0, self.n):
                    self._data[x][y] = self._data[x][y] + other

    def __sub__(self, other):
        """
        Returns: The difference of two matrices
        OR
        Procedure: Scalar subtraction of self.

        Precondition: The two matrices must be the same size.
        """
        #Matrix subtraction
        if type(self) == Matrix and type(other) == Matrix:
            #Enforce the preconditions
            assert self.m == other.m, "The two matrices differ in number of rows"
            assert self.n == other.n, "The two matrices differ in number of cols"
            #Create the return matrix
            difference_matrix = Matrix(unimath.zeros(self.m, other.n))
            #Subtract the two matrices
            x = 1
            while x <= other.m:
                row_a = self.get_row(x)
                row_b = other.get_row(x)
                difference = unimath.sub(row_a, row_b)
                difference_matrix.set_row(x,difference)
                x += 1
            return difference_matrix
        #Scalar subtraction        
        if type(other) == int or type(other) == float:
            for x in range(0, self.m):
                for y in range(0, self.n):
                    self._data[x][y] = self._data[x][y] - other

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
        #Matrix Multiplication
        if type(self) == Matrix and type(other) == Matrix:
            #Enforce the preconditions
            assert self.n == other.m, "The dimensions of the matrices are invalid."
            #Create the return matrix
            product_matrix = Matrix(unimath.zeros(self.m, other.n))
            #Multiply the two matrices
            x = 1
            y = 1
            while y <= other.n:
                col_b = other.get_col(y)
                while x <= self.m:
                    #Multiply the all rows by the column and get the product
                    row_a = self.get_row(x)
                    product = unimath.mult(row_a, col_b)
                    final_sum = unimath.listsum(product)
                    #Set the product to the correct space in the product matrix
                    product_matrix.set(x, y, final_sum)
                    x += 1
                #Reset the row counter and continue with the next column
                x = 1
                y += 1
            return product_matrix
        #Scalar multiplication        
        if type(other) == int or type(other) == float:
            for x in range(0, self.m):
                for y in range(0, self.n):
                    self._data[x][y] = self._data[x][y] * other

    def __div__(self, other):
        """
        Procedure: Scalar division of self.
        """
        #Matrix Division
        if type(self) == Matrix and type(other) == Matrix:
            #Enforce the preconditions
            assert self.n == other.m, "The dimensions of the matrices are invalid."
            #Create the return matrix
            quotient_matrix = Matrix(unimath.zeros(self.m, other.n))
            #Multiply the two matrices
            x = 1
            y = 1
            while y <= other.n:
                col_b = other.get_col(y)
                while x <= self.m:
                    #Multiply the all rows by the column and get the product
                    row_a = self.get_row(x)
                    quotient = unimath.div(row_a, col_b)
                    final_sum = unimath.listsum(product)
                    #Set the product to the correct space in the product matrix
                    quotient_matrix.set(x, y, final_sum)
                    x += 1
                #Reset the row counter and continue with the next column
                x = 1
                y += 1
            return quotient_matrix
        #Scalar division        
        if type(other) == int or type(other) == float:
            for x in range(0, self.m):
                for y in range(0, self.n):
                    self._data[x][y] = self._data[x][y] / other

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
                print '%10.3f' % self._data[x][y],
            print "\n"

    def get(self, x, y):
        """
        Returns: Value a specified coordinate point within the matrix.

        Precondition: x and y are valid coordinates using Matlab coordinate
        rules.
        """
        return self._data[x-1][y-1]

    def set(self, x, y, value):
        """
        Procedure: Sets value at a specfied coordinate point to a new value.

        Precondition: x and y are valid coordinates using Matlab coordinate
        rules.
        """
        #Check if the value specified is a string or an actual list.
        assert type(value) == float or type(value) == int
        self._data[x - 1][y - 1] = value


    def get_row(self, row_number):
        """
        Returns: The specified row in matrix self. The row is a python list.
        """
        assert row_number <= self.m and row_number > 0, "This is not a valid row number"
        return self._data[row_number - 1]

    def set_row(self, row_number, row):
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
        assert col_number <= self.n and col_number > 0, "This is not a valid col number"
        column = []
        row_number = 0
        while row_number < self.m:
            column = column + [self._data[row_number][col_number - 1]]
            row_number += 1
        return column

    def set_col(self, col_number, col):
        """
        Procedure: Sets the value for a specified column.
        """
        assert col_number <= self.n and col_number >= 1, "This is not a valid col number"
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
        assert len(row) == self.n, "The row has an invalid length"
        #Add the whole row to the end of the matrix
        self._data = self._data + [row]
        self._m += 1

    def add_col(self, col):
        """
        Procedure: Adds a given col to the matrix to the right

        Precondition: The column must have the same length as other rows 
        """
        assert len(col) == self.m, "The column has an invalid length"
        #Add each element to the end of each row
        x = 0
        for y in col:
            self._data[x] = self._data[x] + [y]
            x += 1
        self._n += 1
        

    def sub_row(self, x):
        """
        Procedure: Subtracts a given row from the matrix by row number. x
        represents a specific row number.

        Precondition: x must be a valid row number
        """
        assert self.m >= x, "The row number given is too large"
        assert x > 0, "Try again with a row number > 0"
        self._data.remove(self._data[x - 1])

    def sub_col(self, y):
        """
        Procedure: Subtracts a given column from the matrix by column number.

        Precondition: y must be a valid column number.
        """
        assert self.n >= y, "The column number given is too large"
        assert y > 0, "Try again with a column number > 0"
        for x in range(0, self.m):
            self._data.remove(self._data[x][y])

    #Helper Methods
    def _parse(self, raw_data):
        """
        Procedure: Parses the raw_data string and updates the Matrix object.
        Called during object construction.

        Precondition: raw_data is a valid input according to the description
        in the meta documentation at the top of the document.
        """
        #Case 1: raw_data is a string
        if type(raw_data) == str:
            #Some assertions statements to QC the raw_data input
            assert type(raw_data) == str, "The matrix given is not a string"
            assert raw_data[0] != "[", "Use Matlab matrix notation without braces"
            #Initialize default values
            self._m = 1
            self._n = 1
            #Split the matrix up into rows of strings and set m to len(self._data
            self._data = raw_data.split(';')
            self._m = len(self._data)
            #Continue parsing the input, make rows into lists of numbers
            for x in range(0, self.m):
                self._data[x] = self._data[x].split(",")
                self._data[x] = list(map(float, self._data[x]))
            #Set n to the number of elements in each row
            self._n = len(self._data[0])
            #Set whether the matrix is a square matrix
            if self.m == self.n:
                self._is_square = True
        #Case 2: raw_data is a valid 2D list in matrix form:
        elif type(raw_data) == list:
            self._data = raw_data
            self._m = len(self._data)
            self._n = len(self._data[0])
            if self._m == self.n:
                self._is_square = True

    def _check(self):
        """
        Procedure: Checks if the raw input was valid by QCing the properties
        of the matrix. Called during object construction.
        """
        #Test if the rest of the rows are the same length
        for r in range(0, self.m):
            assert len(self._data[r]) == self.n, "Invalid row lengths"
            assert type(self._data[r]) == list, "Some rows aren't lists"


#== Matrix Functions =====================================================
def ref(matrix):
    """
    Procedure: Row reduces a matrix.
    """
    #Initialize variables:
    lead = 1                #The index of the pivot column
    col_count = matrix.n    #The number of columns
    row_count = matrix.m    #The number of rows
    for r in range(1, row_count+1):
        #If we have finished RREF on the last column, end.
        if col_count < lead:
            return
        #Start with the rth row when finding a pivor entry
        i = r
        #Find the pivot entry of the pivot column - first non-zero entry
        while matrix.get(i, lead) == 0:
            i += 1
            #If the whole column is empty, go to the next column.
            if row_count < i:
                i = r
                lead += 1
                if col_count < lead:
                    return
        #Swap rows i and r such that the pivot entry is above all others
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        matrix.set_row(i, row_r)
        matrix.set_row(r, row_i)
        #Update row_i and row_r lists for next steps
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        if matrix.get(r, lead) != 0:
            #Divide the whole row by the pivot to get a 1
            pivot = matrix.get(r,lead)
            row_r = unimath.divlist(row_r, pivot)
            matrix.set_row(r, row_r)
        for i in range(r+1, row_count+1):
            #Perform pivoted row operations to get all 0 below the pivot.
            multiplier = matrix.get(i, lead)
            row_r = matrix.get_row(r)
            row_i = matrix.get_row(i)
            row_r = unimath.mullist(row_r, multiplier)
            sublist = lambda m,n: m-n
            row_i = map(sublist, row_i, row_r)
            matrix.set_row(i, row_i)
        #Set the next column to be the pivoting column.
        lead += 1


def rref(matrix):
    """
    Procedure: Reduced row echelon form of a matrix
    """
    #Initialize variables:
    lead = 1                #The index of the pivot column
    col_count = matrix.n    #The number of columns
    row_count = matrix.m    #The number of rows
    for r in range(1, row_count+1):
        #If we have finished RREF on the last column, end.
        if col_count < lead:
            return
        #Start with the rth row when finding a pivor entry
        i = r
        #Find the pivot entry of the pivot column - first non-zero entry
        while matrix.get(i, lead) == 0:
            i += 1
            #If the whole column is empty, go to the next column.
            if row_count < i:
                i = r
                lead += 1
                if col_count < lead:
                    #If last pivot is a 0, set the column as a zero vector
                    zero = [0 for x in range(row_count)]
                    matrix.set_col(col_count, zero)
                    return
        #Swap rows i and r such that the pivot entry is above all others
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        matrix.set_row(i, row_r)
        matrix.set_row(r, row_i)
        #Update row_i and row_r lists for next steps
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        if matrix.get(r, lead) != 0:
            #Divide the whole row by the pivot to get a 1
            pivot = matrix.get(r,lead)
            row_r = unimath.divlist(row_r, pivot)
            matrix.set_row(r, row_r)
        for i in range(1, row_count+1):
            #Perform pivoted row operations to get all 0 above and below pivot.
            if i != r:
                multiplier = matrix.get(i, lead)
                row_r = matrix.get_row(r)
                row_i = matrix.get_row(i)
                row_r = unimath.mullist(row_r, multiplier)
                sublist = lambda m,n: m-n
                row_i = map(sublist, row_i, row_r)
                matrix.set_row(i, row_i)
        #Set the next column to be the pivoting column.
        lead += 1

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
    if matrix.is_square:
        if matrix.n == 2:
            return (matrix.get(1,1)*matrix.get(2,2) - matrix.get(1,2)*matrix.get(2,1))
        else:
            return 


def inv(matrix):
    """
    Returns: The inverse of a given matrix.
    """
    assert matrix.is_square, "The matrix is not square and not invertible."
    inverse = identity(matrix.n)
    #Initialize variables:
    lead = 1                #The index of the pivot column
    col_count = matrix.n    #The number of columns
    row_count = matrix.m    #The number of rows
    for r in range(1, row_count+1):
        #If we have finished RREF on the last column, end.
        if col_count < lead:
            return inverse
        #Start with the rth row when finding a pivot entry
        i = r
        #Find the pivot entry of the pivot column - first non-zero entry
        while matrix.get(i, lead) == 0:
            i += 1
            #If the whole column is empty, go to the next column.
            if row_count < i:
                i = r
                lead += 1
                if col_count < lead:
                    return inverse
        #Swap rows i and r such that the pivot entry is above all others
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        matrix.set_row(i, row_r)
        matrix.set_row(r, row_i)
        #Do the same for the identity
        inv_row_i = inverse.get_row(i)
        inv_row_r = inverse.get_row(r)
        inverse.set_row(i, inv_row_r)
        inverse.set_row(r, inv_row_i)
        #Update row_i and row_r lists for next steps
        row_i = matrix.get_row(i)
        row_r = matrix.get_row(r)
        inv_row_i = inverse.get_row(i)
        inv_row_r = inverse.get_row(r)
        if matrix.get(r, lead) != 0:
            #Divide the whole row by the pivot to get a 1
            pivot = matrix.get(r,lead)
            row_r = unimath.divlist(row_r, pivot)
            inv_row_r = unimath.divlist(inv_row_r, pivot)
            matrix.set_row(r, row_r)
            inverse.set_row(r, inv_row_r)
        for i in range(1, row_count+1):
            #Perform pivoted row operations to get all 0 above and below pivot.
            if i != r:
                multiplier = matrix.get(i, lead)
                row_r = matrix.get_row(r)
                row_i = matrix.get_row(i)
                inv_row_r = inverse.get_row(r)
                inv_row_i = inverse.get_row(i)

                row_r = unimath.mullist(row_r, multiplier)
                inv_row_r = unimath.mullist(inv_row_r, multiplier)

                sublist = lambda m,n: m-n

                row_i = map(sublist, row_i, row_r)
                inv_row_i = map(sublist, inv_row_i, inv_row_r)

                matrix.set_row(i, row_i)
                inverse.set_row(i, inv_row_i)
        #Set the next column to be the pivoting column.
        lead += 1
    return inverse


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

def identity(n):
    """
    Returns: The identity matrix of size n
    """
    identity_matrix = Matrix(unimath.zeros(n,n))
    i = 1
    while i <= n:
        identity_matrix.set(i, i, 1)
        i += 1
    return identity_matrix
    
#== Properties of Matrix Testers =========================================
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
