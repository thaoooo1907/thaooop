# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:35:17 2024

@author: Student
"""

def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số nguyên dương n: "))
is_nguyen_to = kiem_tra_nguyen_to(n)
if is_nguyen_to:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
