# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:18:53 2021

@author: Ruich
"""


from BaseTree import BaseTree

class BaseBinaryTree(BaseTree):
    '''abstract base class representing binary tree'''
    def left(self,p):
        '''return the left child of p'''
        raise NotImplementedError("must be implemented by subclass")
        
    def right(self,p):
        '''return the right child of p'''
        raise NotImplementedError("must be implemented by subclass")

    #----------------------------------------------------------------
    # concrete implementation
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self,p):
        '''generate an iteration of children of p'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)