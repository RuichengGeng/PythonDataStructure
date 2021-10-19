# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:44:37 2021

@author: Ruich
"""

import pytest

def generate_max_squared(n):
    i = 0
    while (i + 1)**2  <= n:
        i += 1
    return i**2
# generate_max_squared(16)


def test_generate_max_squared0():
    assert generate_max_squared(0) == 1