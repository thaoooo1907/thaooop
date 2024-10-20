# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:55:53 2024

@author: Tien
"""

def fibonacci(n):
    a=0
    b=1
    day =[]
    for i in range(n):
        day.append(a)
        a,b=a,a+b
        return day
n = int(input("Nhập phần tử của dãy Fibonacci:"))
result = fibonacci(n)
print(f"dãy Fibonacci gồm {n} phần tử: {result}")
