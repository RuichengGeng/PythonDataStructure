# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:16:12 2021

@author: Ruich
"""
import random
import time
import copy

def merge(arr1,arr2,arr):
    i,j = 0,0
    while i + j < len(arr):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[i+j] = arr1[i]
                i += 1
            else:
                arr[i+j] = arr2[j]
                j += 1
        elif i == len(arr1):
            arr[i+j] = arr2[j]
            j += 1
        elif j == len(arr2):
            arr[i+j] = arr1[i]
            i += 1

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return 
    arr1 = arr[: n//2]
    arr2 = arr[n//2:]
    merge_sort(arr1)
    merge_sort(arr2)
    merge(arr1,arr2,arr)
    return arr
    
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def test_merge_sort():
    arr = []
    for _ in range(100):
        arr.append(random.randint(0,100))
    arr = merge_sort(arr)
    return arr

def compare_sort():
    arr = []
    for _ in range(10000):
        arr.append(random.randint(0,100))
        
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    
    start = time.time()
    merge_sort(arr1)
    end = time.time()
    print("merge sort : {}".format(end - start))
    
    start = time.time()
    bubble_sort(arr2)
    end = time.time()
    print("bubble sort : {}".format(end - start))


if __name__ == '__main__':
    # arr = test_merge_sort()
    compare_sort()
    arr = test_merge_sort()
