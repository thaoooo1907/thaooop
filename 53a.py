# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:52:58 2024

@author: Student
"""

def tong_so(n):
    return sum(range(1, n + 1))
n = int(input("Nhập số nguyên dương n: "))
ket_qua = tong_so(n)
print(f"Tổng các số từ 1 đến {n} là: {ket_qua}")
