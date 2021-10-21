# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:22:25 2021

@author: Ruich
"""

class Empty(Exception):
    pass

class Node:
    def __init__(self,element,NextNode):
        self.element = element
        self.next = NextNode
        
class LinkedStack:
    '''use linked node to implement stack
    the advantage compared with list implement stack is node save memory'''
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,value):
        self._head = Node(value,self._head)
        self._size += 1
        
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        res = self._head.element
        self._head = self._head.next
        self._size -= 1
        return res
    
def reverse(s):
    '''use stack FILO to reverse a string'''
    stack = LinkedStack()
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
    stack = LinkedStack()
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

