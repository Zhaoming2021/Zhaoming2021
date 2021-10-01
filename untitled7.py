#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:32:01 2021

@author: zhaomingli
"""

"""
Egyptian algorithm
"""

def egyptian_multiplication(a, n):
    """
    returns the product a * n
    assume n is a nonegative integer
    """
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)



def power(a, n):
    """
    computes the power a ** n
    assume n is a nonegative integer
    """
    s=a
    for i in range (n-1):
        s=egyptian_multiplication(s,a)
    return s

print(power(2,3))
