#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:58:04 2020

@author: Soham
"""
import math


c = [4,6.1,1]
p = [10,14,70]


totalc = 0

def sumtasks(r,x):
    retsum = 0
    for i in range(y):
        retsum += math.ceil((r/p[i]))*c[i]
    return retsum

def ithsum(i):
    retsum1 = 0 
    for x in range(i+1):
        retsum1 += c[x]
    return retsum1


for y in range(len(c)):
    if(y==0):
        continue
    else:
        totalc = ithsum(y)
        while(totalc<=p[y]):
            totalcold = totalc
            totalc = c[y]+sumtasks(totalc,y)
            if(totalcold == totalc):
                print("done task "+str(y+1)+" is schedulable.")
                print("totalcold: "+str(totalcold))
                print("totalc: "+str(totalc))
                break
    if(totalc != totalcold):
        print("done task "+str(y+1)+" is not schedulable.")
        print("totalcold: "+str(totalcold))
        print("totalc: "+str(totalc))
        
    
        