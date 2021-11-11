# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:27:27 2021

@author: daaze
"""
from karatsuba import karatsuba
'''
unit tests for karatsuba recursive implementation
'''
def test_karatsuba_1():
    assert (karatsuba(1234, 5678) == 1234*5678)
def test_karatsuba_2():
    assert (karatsuba(12345678, 56781234) == 12345678*56781234)
def test_karatsuba_3():
    assert (karatsuba(12, 5) == 60)
