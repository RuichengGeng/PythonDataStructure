# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:52:25 2021

@author: Ruich
"""

class BaseTree:
    '''Abstract base class Tree'''
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")
        def __eq__(self):
            raise NotImplementedError("must be implemented by subclass")
        def __nq__(self):
            raise NotImplementedError("must be implemented by subclass")
    def root(self):
        '''return the root of the tree'''
        raise NotImplementedError("must be implemented by subclass")
        
    def parent(self,p):
        '''return parent of the position'''
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self,p):
        '''return number of children of the position'''
        raise NotImplementedError("must be implemented by subclass")
        
    def children(self,p):
        '''return generator of children of children'''
        raise NotImplementedError("must be implemented by subclass")
        
    def __len__(self):
        '''return the length of the tree'''
        raise NotImplementedError("must be implemented by subclass")
    #----------------------------------------------------------------
    # concrete implementation
    def is_root(self,p):
        return self.root() == p
    
    def is_leaf(self,p):
        return self.num_children() == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self,p):
        '''return the depth of position'''
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))
    
    def hight(self,p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.hight(i) for i in self.children(p))
    