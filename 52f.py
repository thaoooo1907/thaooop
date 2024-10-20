# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:38:50 2024

@author: Student
"""

def tong_so_nguyen_to(n):
    def kiem_tra_nguyen_to(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    tong = 0
    for i in range(2, n):
        if kiem_tra_nguyen_to(i):
            tong += i
    return tong
n = int(input("Nhập số nguyên dương n: "))
ket_qua = tong_so_nguyen_to(n)
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {ket_qua}")
