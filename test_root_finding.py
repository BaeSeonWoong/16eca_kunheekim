# -*- coding: utf8 -*-

# [2013112007] [김건희]











import unittest

import root_finding as rf


def f(x):







    x_float = float(x)



    return x_float * x_float * x_float -3.0


def dfdx(x):







    x_float = float(x)

    return 3.0 * x_float * x_float




class TestRootFinding(unittest.TestCase):
    def test_bisecsion(self):








        result = rf.bisection(f, 0.01, 100, epsilon=1e-8)



        self.assertAlmostEqual(0.0, f(result), places=6)



    def test_newton(self):






        result = rf.newton(f, dfdx, 100, epsilon=1e-8)


        self. assertAlmostEqual(0.0, f(result), places=6)



if '__main__' == __name__:

    unittest.main()