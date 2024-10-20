# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:53:35 2024

@author: Student
"""

def tong_ham_so_hoc(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    return S


n = int(input("Nhập số nguyên dương n: "))
ket_qua = tong_ham_so_hoc(n)
print(f"Tổng S = 1 + 1/2 + 1/3 + ... + 1/{n} là: {ket_qua}")
