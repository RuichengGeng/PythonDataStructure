# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:49:57 2021

@author: Ruich
"""
from PriorityQueueBase import PriorityQueueBase
from PriorityQueueBase import _Item
from SortedPriorityQueue import SortedPriorityQueue
from ArrayHeap import Heap
import random
import time


def compare_sorttree():
    arr = []
    for _ in range(10000):
        arr.append((random.randint(a= 0,b = 10000),0))

    hp = Heap()
    hp_res = []
    
    sq = SortedPriorityQueue()
    sq_res = []
    
    ##heap 
    start = time.time()
    start1 = time.time()
    for i,j in arr:
        hp.add(i,j)
    end1 = time.time()
    print("Heap insert : {}".format(end1 - start1))
    
    start1 = time.time()
    while not hp.is_empty():
        hp_res.append(hp.remove_min()[0])
        
    end1 = time.time()
    print("Heap pop : {}".format(end1 - start1))
    end = time.time()
    hp_time= end - start
    print("Heap : {}".format(hp_time))


    ##heap constructor
    start = time.time()
    start1 = time.time()
    hp2 = Heap(arr)
    hp2_res = []
    end1 = time.time()
    print("Heap2 insert : {}".format(end1 - start1))
    
    start1 = time.time()
    while not hp2.is_empty():
        hp2_res.append(hp2.remove_min()[0])
        
    end1 = time.time()
    print("Heap2 pop : {}".format(end1 - start1))
    end = time.time()
    hp2_time= end - start
    print("Heap2 : {}".format(hp2_time))



    ##sorted list 
    start = time.time()
    start1 = time.time()
    for i,j in arr:
        sq.add(i,j)
    end1 = time.time()
    print("sorted queue insert : {}".format(end1 - start1))
    
    start1 = time.time()
    while not sq.is_empty():
        sq_res.append(sq.remove_min()[0])
    end1 = time.time()
    print("sorted queue pop : {}".format(end1 - start1))
    end = time.time()
    sq_time = end - start
    print("sorted queue : {}".format(sq_time))
    
    
    ## check equivalence of two algo
    length = len(hp_res)
    for idx,value in enumerate(hp_res):
        
        assert value == sq_res[length - idx - 1]
        assert value == hp2_res[idx]
        
    print("sort list / heap = {}".format(sq_time / hp_time))
    print("sort list / heap2 = {}".format(sq_time / hp2_time))
    print("heap / heap2 = {}".format(hp_time / hp2_time))
    




if __name__ == '__main__':
    compare_sorttree()