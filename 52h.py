# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:50:54 2024

@author: Student
"""

def tong_uoc_so(n):
    tong = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i           
    return tong
n = int(input("Nhập số nguyên dương n: "))
ket_qua = tong_uoc_so(n)
print(f"Tổng các ước số dương của {n} là: {ket_qua}")
