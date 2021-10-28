# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:35:53 2021

@author: Ruich
"""

class Empty(Exception):
    pass

class Node:
    def __init__(self,element,NextNode):
        self.element = element
        self.next = NextNode


class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
        
    def add_first(self,value):
        if self._head is not None:
            node = Node(value,self._head)
            self._head = node
        else:
            self._head = Node(value,None)
        self._size += 1
    
    def remove_first(self):
        if self._size == 0:
            raise Empty("The linkedlist is empty!")
        self._head = self._head.next
        self._size -= 1
    
    def __len__(self):
        return self._size
    
    def insert_element(self,target,element):
        '''if the node.value == target, then add a node with value element after target node 
        in this algo, if there are more than one target value in the linked list, all element will be insert after that'''
        this = self._head
        change = False
        while this is not None:
            value = this.element
            if value == target:
                this.next = Node(element,this.next)
                print("Insert {} after {}".format(element,target))
                change = True
            this = this.next
        if change == False:
            print("No target value : {} in linked list".format(target))
    
    def remove_element(self,target):
        while self._head.element == target:
            self._head = self._head.next
            self._size -= 1
            print("Remove {} from head".format(target))
            if self._head is None:
                return 
        
        thisNode = self._head
        nextNode = thisNode.next
        while nextNode is not None:
            if nextNode.element == target:
                thisNode.next = nextNode.next
                print("Remove {} from single linked list".format(target))
                self._size -= 1
                nextNode = thisNode.next
            else:
                thisNode = thisNode.next
                nextNode = thisNode.next
                

    def __iter__(self):
        this = self._head
        while this is not None:
            value = this.element
            this = this.next
            yield value

def test_SingleLinkedList1():
    sll = SingleLinkedList()
    for i in range(10):
        sll.add_first(i)
    for _ in range(5):
        sll.remove_first()
    for _ in range(3):
        sll.insert_element(4,10)
        
    sll.remove_element(4)
    for i in sll:
        print(i)
        
    sll.remove_element(10)
    for i in sll:
        print(i)

def test_SingleLinkedList2():
    sll = SingleLinkedList()
    for _ in range(10):
        sll.add_first(10)
    sll.remove_element(10)
    for i in sll:
        print(i)

if __name__ == '__main__':
    test_SingleLinkedList1()
    test_SingleLinkedList2()
