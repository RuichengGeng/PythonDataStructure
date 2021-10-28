# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:57:17 2021

@author: Ruich
"""
class Empty(Exception):
    pass

class _DNode:
    '''double linked node'''
    def __init__(self,_element,_prev,_next):
        self._element = _element
        self._prev = _prev
        self._next = _next
        
class _DoubleLinkedBase:
    '''base class for double linked list related data type'''
    def __init__(self):
        self._head = _DNode(None,None,None)
        self._trailer = _DNode(None,None,None)
        self._head._next = self._trailer
        self._trailer._prev = self._head
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def _insert_between(self,element,_prev,_next):
        new = _DNode(element,_prev,_next)
        _prev._next = new
        _next._prev = new
        self._size += 1
        return new
    
    def _delete_between(self,node):
        _prev = node._prev
        _next = node._next
        _prev._next = _next
        _next._prev = _prev
        self._size -= 1
        element = node._element
        node._prev,node._element,node._next = None,None,None # deprecate the node
        return element

class LinkedDequeue(_DoubleLinkedBase):
    '''double end queue based on double linked list'''
    def __init__(self):
        super().__init__()
    
    def first(self):
        if self.is_empty():
            raise Empty("Empty queue")
    
    def last(self):
        if self.is_empty():
            raise Empty("Empty queue")
            
    def insert_first(self,element):
        self._insert_between(element,self._head,self._head._next)
    
    def insert_last(self,element):
        self._insert_between(element,self._trailer._prev,self._trailer)
        
    def delete_first(self):
        if self.is_empty():
            raise Empty("Empty queue")
        return self._delete_between(self._head._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty("Empty queue")
        return self._delete_between(self._trailer._prev)

def test_dequeue():
    q = LinkedDequeue()
    for i in range(10):
        q.insert_first(i)
    q.insert_first(-1)
    while len(q) > 0:
        print(q.delete_last())
        
if __name__ == '__main__':
    test_dequeue()
