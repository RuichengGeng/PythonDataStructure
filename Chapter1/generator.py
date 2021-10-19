# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:02:22 2021

@author: Ruich
"""


def factor(n):
    k = 1
    while k * k < n: 
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k ==n:
        yield k
        

if __name__ == '__main__':
    for i in factor(30):
        print(i)
        
        
        