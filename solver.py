""" Solver Linear equation using inverse matrix """
import numpy as np

class LinearEquationSolver(object):
    """ Linear Equation solver using inverse matrix 
    
    equation: AX = B

    X = inverse(A) . B

    Args:
        A: matrix A (np array)
        B: Matrix B (np array)

    return:
        value of X
    """

    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def is_valid(self):
        """ 
        check if the correct matrix
        # checking if A is square matrix and dot product possible for A and B (n *m )(m*n)
        """
        shape_A = self.A.shape
        shape_B = self.B.shape

        
        if shape_A[1] == shape_B[0]:
            if shape_A[0] == shape_A[1]: 
                return True
            else:
                raise Exception("A is not a Square matrix")
        else:
            raise Exception("Dot Product not possible for A and B")   

    def inverse_matrix(self, matrix):
        """ Inverse the matrix """
        try:
            inverse_matix = np.linalg.inv(matrix)
            return inverse_matix
        except Exception as e:
            raise ValueError("Inverse of matrix not possible")

    def solve(self):
        """ main function to solve the equation by calling the dot product between 
            inverse(A) and B.
        """
        coff = 0
        if self.is_valid():
            inverse_A = self.inverse_matrix(self.A)
            coff = np.dot(inverse_A, self.B)
            
        return coff
