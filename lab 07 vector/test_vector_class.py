# -*- coding: utf8 -*-

#[2013112007] [김건희]







import itertools


class Vector(list):


    def __add__(selfself, other):

        if len(self) == len(other):
            result = Vector([s + o for s, o in itertools.izip(self, other)])
        else:
            raise ValueError("Vector size msmathch")
        return result

    def __mul__(self, other):

        if isinstance(other, (int, float, complex)):
            """scala vector product"""
            result = Vector([s * other for s in self])
        elif isinstance(other, Vector):
            """dot product"""
            if len(self) == len(other):

                result = 0.0
                for s, o in itertools.izip(self. other):
                    result += s * o
            else:

                raise ValueError("Vector size mismatch")
        else:

