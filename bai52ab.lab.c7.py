# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:00:30 2024

@author: Tien

"""
#bai52a
def can_bac_n(x,n):
    return x ** (1/n)
#b cach 1
def dao_so(n):
    return str(n)[::-1]
#b cach 2
def dao(n):
    return int(str(n)[::-1])
#b cach 3
def dao_so_(n):
    dao = 0
    while dao>0:
        dao=dao*10 + n%10
        n//=10
    return dao










if __name__=='__main__':
    print(can_bac_n(3,6))
    print(dao_so(543210))
    print(dao(7))
    print(dao_so_(12340))
