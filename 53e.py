# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:34:50 2024

@author: ADMIN
"""

def giai_thua(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

if __name__ == '__main__':
    n = 2 
    print(f"Giai thừa của {n} là: {giai_thua(n)}")
