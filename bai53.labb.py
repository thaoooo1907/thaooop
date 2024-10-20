# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:20:05 2024

@author: tien
"""
# bai 53a
def tong(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s
#bai 53b
def tinh_tong_binh_phuong(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

#bai 53 c
def tong_phan_so(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i
    return s
#bai 53d
def tong_gthua(n):
    s = 0
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
        s += giaithua
    return s
#bai 53e
def tinh_tich(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich 


if __name__== '__main__':
    print(tong(4))
    print(tinh_tong_binh_phuong(3))
    print(tong_phan_so(2))
    print(tong_gthua(12))
    print(tinh_tich(4))
    