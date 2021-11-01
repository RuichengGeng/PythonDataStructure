# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:09:19 2021

@author: Ruich
"""
from PriorityQueueBase import PriorityQueueBase
from PriorityQueueBase import _Item
class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def add(self,key,value):
        self._data.append(_Item(key,value))
        
    def _find_min(self):
        if len(self._data) > 0:
            minItem = self._data[0]
            for item in self._data:
                if item.key < minItem.key:
                    minItem = item
        else:
            return _Item(None,None)
    
    def get_min(self):
        item = self._find_min()
        return (item.key,item.value)
    
    def delete_min(self):
        if len(self._data) > 0:
            minIdx = 0
            for idx,item in enumerate(self._data):
                if item.key < item.key:
                    minIdx = idx
            return self._data.pop(minIdx)
        else:
            return _Item(None,None)
        
