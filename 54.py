# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:20:05 2024

@author: Student
"""

def fib(n):
    a, b = 0,1
    while a < n :
        print (a, end=' ')
        a, b = b, a+b 
print (fib(2018))
        
       