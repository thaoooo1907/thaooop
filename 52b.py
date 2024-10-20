# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:27:57 2024

@author: Student
"""

def so_dao(n):
    if n < 0:
        return "n phải là số nguyên dương."
    return int(str(n)[::-1])
n = int(input("Nhập số nguyên dương n: "))
ket_qua = so_dao(n)
print(f"Số đảo của {n} là: {ket_qua}")
