# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:56:01 2021

@author: Ruich
"""
class Empty(Exception):
    pass

class Node:
    def __init__(self,element,NextNode):
        self.element = element
        self.next = NextNode
        
class LinekedQueue:
    '''used linked node to implement queue'''
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def enqueue(self,element):
        n = Node(element,None)
        if self.is_empty():
            self._head = n
        else:
            self._tail.next = n
        # enqueue the first element, the head and tail will
        # the same value.
        # when the second element is enqueued, the head will point to the second
        self._tail = n
        self._size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        res = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return res
    
    def first(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        res = self._head.element
        return res


def test_queue1():
    queue = LinekedQueue()
    assert len(queue)==0
    for i in range(10):
        queue.enqueue(i)
    queue.enqueue(10)
    assert len(queue) == 11
    
    assert queue.dequeue() == 0
    assert queue.dequeue() == 1
    assert len(queue) == 9
    
def test_queue2():
    queue = LinekedQueue()
    queue.first()
    

if __name__ == '__main__':
    test_queue1()
    test_queue2()