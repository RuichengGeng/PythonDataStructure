# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:36:44 2021

@author: Ruich
"""
import random
import time
import copy

def quick_sort(arr,left = None,right = None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left < right:
        partitionIndex = partition(arr,left,right)
        quick_sort(arr,left = left,right = partitionIndex - 1)
        quick_sort(arr,left = partitionIndex + 1,right = right)
    return arr

def partition(arr,left,right):
    pivotIndex = left
    pivotValue = arr[pivotIndex]
    index = pivotIndex + 1 #index is to control index of the first element greater or equal to pivot value
    i = index # i is to control the loop of the arr
    while i <= right:
        if arr[i] < pivotValue:
            arr[i],arr[index] = arr[index],arr[i]
            index += 1
        i += 1
    arr[pivotIndex],arr[index - 1] = arr[index - 1],arr[pivotIndex]
    return index - 1

def test_quick_sort():
    arr = []
    for _ in range(100):
        arr.append(random.randint(0,100))
    arr = quick_sort(arr)
    return arr

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


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

def compare_sort():
    arr = []
    for _ in range(10000):
        arr.append(random.randint(0,100))
        
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    
    start = time.time()
    quick_sort(arr1)
    end = time.time()
    print("quick sort : {}".format(end - start))
    
    start = time.time()
    merge_sort(arr2)
    end = time.time()
    print("merge sort : {}".format(end - start))
    
    start = time.time()
    bubble_sort(arr3)
    end = time.time()
    print("bubble sort : {}".format(end - start))



if __name__ == '__main__':
    arr = compare_sort()
    # arr = test_quick_sort()
