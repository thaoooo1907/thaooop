# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:46:13 2024

@author: ADMIN
"""

import math 
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    hinh_name = {
        'vuong': (lambda canh: (4*canh, canh**2)),
        'chunhat': (lambda dai, rong: (2* (dai+rong), dai*rong)),
        'tron' : (lambda bk : (2* math.pi *bk, math.pi * bk **2 ))
        }
    if hinh in hinh_name : 
        return hinh_name[hinh](*args)[0] if pheptinh == 'chuvi' else hinh_name[hinh](*args)[1]
    
if __name__ == '__main__':
        print ('chu hinh vuong:',chuvi_dt('vuong', 'chuvi',3))  
        print ('dien tich hinh vuong:', chuvi_dt('vuong', 'dientich',3))
        print ('chu vi hinh chu nhat:', chuvi_dt('chunhat', 'chuvi',3,4)) 
        print ('dien tich hinh chu nhat:', chuvi_dt('chunhat', 'dientich', 3,4)) 
        print ('chu vi hinh tron:', chuvi_dt('tron', 'chuvi',3)) 
        print ('dien tich hinh tron:', chuvi_dt('tron', 'dientich',3))                                                    
        