# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:31:23 2024

@author: Student
"""

def kiem_tra_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

n = int(input("Nhập số nguyên dương n: "))
is_chinh_phuong = kiem_tra_chinh_phuong(n)
if is_chinh_phuong:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
