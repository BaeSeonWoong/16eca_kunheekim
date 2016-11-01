# -*- coding:utf8 -*-

# [2013112007] [김건희]











import math
import unittest

import num_int


def f(theta_rad):







    theta_rad_float = float(theta_rad)

    return math.sin(theta_rad_float)


def integrated_f(theta_rad):







    theta_rad_float = float(theta_rad)

    return -math.cos(theta_rad_float)




class TestNumericalIntegration(unittest.TestCase):
    def setUp(self):

        self.xi_rad = 0.0
        self.xe_rad = 2.0 * math.pi


        self.expected = integrated_f(self.xe_rad) - integrated_f(self.xi_rad)

    def test_rect(self):






        result = num_int.rect0(f, self.xi_rad, self.xe_rad, 360)


        self.assertAlmostEqual(self.expected, result, places=6)

    def test_trapezoid(self):






        result = num_int.trapezoid1(f, self.xi_rad, self.xe_rad, 360)


        self.assertAlmostEqual(self.expected, result, places=6)



if '__main__' == __name__:

    unittest.main()