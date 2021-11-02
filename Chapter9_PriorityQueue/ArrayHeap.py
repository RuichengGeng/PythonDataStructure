# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:30:25 2021

@author: Ruich
"""

from PriorityQueueBase import PriorityQueueBase
from PriorityQueueBase import _Item
from SortedPriorityQueue import SortedPriorityQueue
import random
import time
'''
index start from 0
left child of p is 2p + 1
right child of p is 2p + 2
parent of p is (p - 1) // 2
'''
class Empty(Exception):
    pass

class Heap(PriorityQueueBase):
    #----------------------non publice behavior
    def _parent(self,p):
        return (p - 1) // 2
    
    def _left(self,p):
        return 2*p + 1
    
    def _right(self,p):
        return 2*p + 2
    
    def _has_right(self,p):
        return self._right(p) < len(self._data)
    
    def _has_left(self,p):
        return self._left(p) < len(self._data)
    
    def _swap(self,i,j):
        self._data[i],self._data[j] = self._data[j],self._data[i]
    
    # use heap up when a new item is added to the end of tree
    def _heap_up(self,p):
        parent = self._parent(p)
        if p > 0 and self._data[p] < self._data[parent]:
            self._swap(p,parent)
            self._heap_up(parent)
    
    # use heap down when smallest item removed from tree and random new in root
    def _heap_down(self,p):
        if self._has_left(p):
            ## find smallest children
            left = self._left(p)
            small_idx = left
            small_child = self._data[left]
            if self._has_right(p):
                right = self._right(p)
                if small_child > self._data[right]:
                    small_idx = right
                    small_child = self._data[right]
            ## swap smallest children and parent
            if small_child < self._data[p]:
                self._swap(p,small_idx)
                self._heap_down(small_idx)
    
    def _heapify(self):
        start = self._parent(len(self._data) - 1) ## the biggest index of non-leave node
        for i in range(start,-1,-1): ## do downheap from bottom to top
            self._heap_down(i)
    #---------------------- publice behavior
    def __init__(self,contents = None):
        if contents is not None:
            self._data = [_Item(k,v) for k,v in contents]
        else:
            self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def add(self,key,value):
        item = _Item(key,value)
        self._data.append(item)
        self._heap_up(len(self._data) - 1)
        
    def get_min(self):
        if self.is_empty():
            assert Empty("Empty Tree")
        item = self._data[0]
        return item.key,item.value
    
    def remove_min(self):
        if self.is_empty():
            assert Empty("Empty Tree")
        self._swap(0,len(self._data) -1)
        item = self._data.pop()
        self._heap_down(0)
        return item.key,item.value
        
def test_Heap():
    q = Heap()
    for _ in range(15):
        q.add(random.randint(a= 0,b = 10),0)
    while not q.is_empty():
        print(q.remove_min())

        
        
if __name__ == '__main__':
    test_Heap()