# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:57:20 2021

@author: Ruich
"""
class Empty(Exception):
    pass

class ArrayQueue:
    '''circular array queue'''
    DEFAULT_SIZE = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_SIZE
        self._front = 0
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def resize(self,newSize):
        data = [None] * newSize
        prt = self._front
        for i in range(self._size):
            data[i] = self._data[prt]
            prt = (prt + 1) % len(self._data)
        self._data = data
        self.front = 0
        
    def enqueue(self,element):
        if self._size == len(self._data):
            self.resize(self._size * 2)
        availPrt = (self._front + self._size) % len(self._data)
        self._data[availPrt] = element
        self._size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        res = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < len(self._data) // 4:
            # if the real size of the queue is 4 times smaller than the data list size, resize.
            # this is to prevent frequent resize operation
            self.resize(len(self._data) // 2)
        return res
    
    def first(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        return self._data[self._front]
    
def test_queue1():
    queue = ArrayQueue()
    assert len(queue)==0
    for i in range(10):
        queue.enqueue(i)
    queue.enqueue(10)
    assert len(queue._data) == 20
    
    assert queue.dequeue() == 0
    assert queue.dequeue() == 1
    assert len(queue._data) == 20
    
def test_queue2():
    queue = ArrayQueue()
    queue.first()
    

if __name__ == '__main__':
    test_queue1()
    test_queue2()


