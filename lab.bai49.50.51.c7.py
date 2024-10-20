# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:17:19 2024

@author: Tien
"""
#bai 49
def ktra_so(n):
    return n<0 and n%2 == 0
#bai50
def kiem_tra(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    return 0
#bai 51
def ktra_gtri(n):
    gtri = input("nhap gia tri:")
    if gtri.repalce('.','',1).replace('-','',1).isdigit():
        gtri = float(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print("Khong hop le, nhap lai")
    return ktra_gtri()

if __name__== '__main__':
    print(ktra_so(3))
    print(kiem_tra(3))
    print(ktra_gtri(32))
    