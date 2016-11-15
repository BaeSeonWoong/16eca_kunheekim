# -*- coding: utf8 -*-

#[2013112007] [김건희]
















import itertools
import unittest


class MyTestCase(unittest.TestCase):
    def asserSequenceAlmostEqual(self, seq1, seq2, msg=None, places=None, delta=None):

        self. assertEqual(len(seq1), len(seq2), msg="len(seq1) != len(seq2)")


        for elem1, elem2 in itertools.izip(seq1, seq2):
            self.asserAlmostEqual(elem1, elem2, places=places, msg=msg, delta=delta)


main = unittest.main