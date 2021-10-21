# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:09:50 2021

@author: Ruich
"""
class Empty(Exception):
    pass

class Dequeue:
    '''circular array double end queue'''
    DEFAULT_SIZE = 10
    def __init__(self):
        self._data = [None] * 10
        self._size = 0
        self._front = 0
        self._back = (self._front + self._size - 1) % (len(self._data))
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def resize(self,newSize):
        data = [None] * newSize
        prt = self._front
        for k in range(self._size):
            data[k] = self._data[prt]
            prt = (prt + 1) % len(self._data)
        self._data = data
        self._front = 0
        self._back = (self._front + self._size - 1) % (len(self._data))
        
    def add_first(self,element):
        if self._size == len(self._data):
            self.resize(self._size * 2)
        leftAvail = (self._front - 1) % len(self._data)
        self._data[leftAvail] = element
        self._front = leftAvail
        self._size += 1
        assert self._back == (self._front + self._size - 1) % (len(self._data))
        
    def delete_first(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        res = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        assert self._back == (self._front + self._size - 1) % (len(self._data))
        if self._size < len(self._data) // 4:
            # if the real size of the queue is 4 times smaller than the data list size, resize.
            # this is to prevent frequent resize operation
            self.resize(len(self._data) // 2)
        return res
    
    def first(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        return self._data[self._front]
    
    def add_last(self,element):
        if self._size == len(self._data):
            self.resize(self._size * 2)
        rightAvail = (self._back + 1) % len(self._data)
        self._data[rightAvail] = element
        self._back = rightAvail
        self._size += 1
        assert self._back == (self._front + self._size-1) % (len(self._data))
        
    def delete_last(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        res = self._data[self._back]
        self._data[self._back] = None
        self._back = (self._back - 1) % len(self._data)
        self._size -= 1
        assert self._back == (self._front + self._size - 1) % (len(self._data))
        if self._size < len(self._data) // 4:
            # if the real size of the queue is 4 times smaller than the data list size, resize.
            # this is to prevent frequent resize operation
            self.resize(len(self._data) // 2)
        return res
    
    def last(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        return self._data[self._back]

def test_dequeue():
    q = Dequeue()
    for i in range(10):
        q.add_last(i)
    q.add_first(-1)
    while len(q) > 0:
        print(q.delete_first())
        
if __name__ == '__main__':
    test_dequeue()





