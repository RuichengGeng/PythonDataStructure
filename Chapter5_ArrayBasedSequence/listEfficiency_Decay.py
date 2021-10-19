# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:57:21 2021

@author: Ruich
"""
import time
import matplotlib.pyplot as plt

def append_time(n):
    data = []
    start = time.time()
    for _ in range(n):
        data.append(None)
    end = time.time()
    return end - start

if __name__ == '__main__':
    ns = []
    times = []
    
    for n in range(100,1000000,1000):
        t = append_time(n)
        print("list size ,time: {},{}".format(n,t))
        ns.append(n)
        times.append(t)
    
    plt.plot(ns,times)
        
        


