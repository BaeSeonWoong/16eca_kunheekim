# -*- coding: utf8 -*-

# [2013112007] [김건희]











import itertools
import unittest

import numpy as np

import ode




class TestNumericalIntegration(unittest.TestCase):
    def setUp(self):

        self.ti_sec = 0.0
        slef.te_sec = 5.0
        self.delta_t_sec = 0.02
        self.x_init = (0.0, 0.0)

        self.expected_t_sec = np.arrange(self.ti_sec, self.te_sec, self.delta_t_sec)
        self.expected_x0 = [ode.exact(t_sec) for t_sec in self.expected_t_sec]

        def test_mod_euler(self):






            result_t, result_x = ode.mod.euler(ode.func, self.x_init, self.ti_sec, self.te_sec, self.delta_t_sec)


            result_x1, result_x2 = itertools.izip(*result_x)


            for expected, result in itertools.izip(self.expected_x0, result_x1):

                self.assertAlmostEqual(expected, result, delta=1e-4)



if '__main__' ==__name__:

    unittest,main()