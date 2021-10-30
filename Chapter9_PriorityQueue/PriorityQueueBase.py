# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:05:46 2021

@author: Ruich
"""
class _Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def __lt__(self,other):
        return self.key < other.key


class PriorityQueueBase:
    '''abstract base class for priority queue'''
    def is_empty(self):
        return len(self) == 0



