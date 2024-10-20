# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:27:27 2024

@author: Student
"""

def tinh_can_bac(n, x):
    if n < 0 or x <= 0:
        return "n phải là số nguyên dương và x phải lớn hơn 0."
    return n ** (1 / x)

n = int(input("Nhập số nguyên dương n: "))
x = int(input("Nhập căn bậc x: "))
ket_qua = tinh_can_bac(n, x)
print(f"Căn bậc {x} của {n} là: {ket_qua}")