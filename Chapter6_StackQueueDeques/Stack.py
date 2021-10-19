# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:13:06 2021

@author: Ruich
"""

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self,e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
def reverse(s):
    '''use stack FILO to reverse a string'''
    stack = ArrayStack()
    for i in s:
        stack.push(i)
    res = []
    while not stack.is_empty():
        res.append(stack.pop())
    return ''.join(str(i) for i in res)

def test_reverse():
    s = 'abcedfg'
    if s[::-1] != reverse(s):
        print("Reverse algo fail")
        
def is_match(expr):
    '''return True if delimiter are matched'''
    stack = ArrayStack()
    leftsyms = '[{('
    rightsyms = ']})'
    for sym in expr:
        if sym in leftsyms:
            stack.push(sym)
        elif sym in rightsyms:
            if stack.is_empty():
                return False
            elif leftsyms.index(stack.pop()) != rightsyms.index(sym):
                return False
    if stack.is_empty():
        return True
    else:
        return False
    
def test_is_match():
    expr1 = "("
    if is_match(expr1) != False:
        print("is match algo1 fail")
        
    expr2 = "1+11 + (1 + 2) + ((()))"
    if is_match(expr2) != True:
        print("is match algo2 fail")

if __name__ == '__main__':
    test_reverse()
    
    test_is_match()

