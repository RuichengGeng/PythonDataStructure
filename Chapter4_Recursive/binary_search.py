# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:51:21 2021

@author: Ruich
"""
import random
import time

def binary_search(array,low,high,target):
    '''
    
    Parameters
    ----------
    array : TYPE
        sorted array.
    low : TYPE
        low index of the array.
    high : TYPE
        high index of the array.
    target : TYPE
        target value.

    Returns
    -------
    index of target if target in the array else False.
    
    '''
    if low > high:
        return False
    else:
        mid = int((low + high) / 2)
        if target == array[mid]:
            return mid
        else:
            if target < array[mid]:
                return binary_search(array,low,mid - 1,target)
            elif target > array[mid]:
                return binary_search(array,mid + 1,high,target)

def search(array,target):
    for i in array:
        if i == target:
            return i

if __name__ == '__main__':
    for _ in range(10):
        array_size = int(2 * 1e7)
        array = list(range(array_size))
        target = random.randint(1,array_size)

        start = time.time()
        index = binary_search(array,0,array_size,target)
        end = time.time()
        print("Binary search : {}".format(end - start))
        
        start = time.time()
        index = search(array,target)
        end = time.time()
        print("Normal search : {}".format(end - start))


