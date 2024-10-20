# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:13:52 2024

@author: Tien
"""
import math
#bai c
def ktra_chinhphuong(n):
    return int(math.sqrt(n)**2) == n
#bai d
def ktra_songuyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
#bai e
def tich_sole(n):
    tich = 1
    for i in str(n):
      if int(i)%2 != 0:
          tich *=int(i)
    return tich
#bai f
def tong_ngto_nho_n(n):
    tong_ngto = 0
    for i in range(2,n):
        if tong_ngto_nho_n(i):
            tong_ngto += i
    return tong_ngto
#bai g 
def tong_chinhphuong(n):
    tong_cp = 0
    for i in range(1,n):
        if ktra_chinhphuong(i):
            tong_cp += i
    return tong_cp
#bai h
def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i 
    return tong



if __name__=='__main__':
    print(ktra_chinhphuong(2))
    print(ktra_songuyento(1))
    print(tich_sole(7))
    print(tong_ngto_nho_n(4))
    print(tong_chinhphuong(5))
    print(tong_uoc(8))
    