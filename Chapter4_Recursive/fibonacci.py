# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:43:06 2021

@author: Ruich
"""
import time

def bad_fibonacci(n):
    '''return the nth item of fibonacci series'''
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n - 1)
        return (a + b,a)

if __name__ == '__main__':
    nth = 30
    for _ in range(10):
        start = time.time()
        bad_fibonacci(nth)
        end = time.time()
        print("Bad fibonacci : {}".format(end - start))
        
        start = time.time()
        good_fibonacci(nth)
        end = time.time()
        print("Good fibonacci : {}".format(end - start))
        
        