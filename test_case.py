
import unittest
import numpy as np

from solver import LinearEquationSolver


class LinearEquationSolverTest(unittest.TestCase):
    def test_one(self):
        A = np.array([[3, 8], [4, 11]])
        B = np.array([5, 7])
        solver = LinearEquationSolver(A, B)
        coff = solver.solve()
        self.assertTrue(np.array_equal(coff, [-1., 1.]))


if __name__ == "__main__":
    unittest.main()
