# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:00:09 2021

@author: Ruich
"""

'''sorted priority queue implement by double linked list'''
from PriorityQueueBase import PriorityQueueBase
from PriorityQueueBase import _Item
import random

class Empty(Exception):
    pass

class _DNode:
    '''double linked node'''
    def __init__(self,_element,_prev,_next):
        self._element = _element
        self._prev = _prev
        self._next = _next
    
    def is_na(self):
        return self._element is None
    
    def prev_node(self):
        return self._prev
    
    def next_node(self):
        return self._next
        
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


class DoubleLinkedList(_DoubleLinkedBase):
    def __init__(self):
        super().__init__()
        
    def first(self):
        if self.is_empty():
            raise Empty("Empty list")
        return self._head._next
    
    def last(self):
        if self.is_empty():
            raise Empty("Empty list")
        return self._trailer._prev
            
    def insert_first(self,element):
        self._insert_between(element,self._head,self._head._next)
    
    def insert_last(self,element):
        self._insert_between(element,self._trailer._prev,self._trailer)
        
    def delete_first(self):
        if self.is_empty():
            raise Empty("Empty list")
        return self._delete_between(self._head._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty("Empty list")
        return self._delete_between(self._trailer._prev)

    def __iter__(self):
        if self.is_empty():
            raise Empty("Empty double linked list")
        thisNode = self._head._next ## notice the head of the list is None
        while not thisNode.is_na():
            yield thisNode
            thisNode = thisNode._next


class SortedPriorityQueue(PriorityQueueBase):
    '''head to tail,small to big'''
    def __init__(self):
        self._data = DoubleLinkedList()
        
    def __len__(self):
        return len(self._data)
    
    def add(self,key,value):
        item = _Item(key,value)
        if self.is_empty():
            self._data.insert_first(item)
        else:
            insert = 0
            for node in self._data:
                if (node._element.key < item.key) and (insert == 0):
                    self._data._insert_between(item,node._prev,node)
                    insert = 1
            if insert == 0:
                self._data.insert_last(item)
    
    def get_min(self):
        if self.is_empty():
            assert Empty("Empty queue")
        p = self._data.first()
        return (p.key,p.value)
    
    def remove_min(self):
        if self.is_empty():
            assert Empty("Empty queue")
        p = self._data.delete_first()
        return (p.key,p.value)


def test_SortedPriorityQueue():
    q = SortedPriorityQueue()
    for _ in range(10):
        q.add(random.randint(a= 0,b = 10),0)
    while not q.is_empty():
        print(q.remove_min())

if __name__ == '__main__':
    test_SortedPriorityQueue()



