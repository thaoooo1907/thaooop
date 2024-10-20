# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:47:31 2024

@author: Student
"""

def tong_so_chinh_phuong(n):
    tong = 0
    i = 1
    
    while i * i < n:
        tong += i * i
        i += 1
    
    return tong
n = int(input("Nhập số nguyên dương n: "))
ket_qua = tong_so_chinh_phuong(n)
print(f"Tổng các số chính phương nhỏ hơn {n} là: {ket_qua}")
