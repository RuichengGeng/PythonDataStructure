# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:29:10 2021

@author: Ruich
"""
import random

def insert_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j >=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

def test_insert_sort():
    arr = []
    for _ in range(100):
        arr.append(random.randint(0,100))
    arr = insert_sort(arr)
    return arr


if __name__ == '__main__':
    # arr = test_merge_sort()

    arr = test_insert_sort()
