# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:39:08 2024

@author: ADMIN
"""

def tinh_chu_vi(chieu_dai, chieu_rong):
    return 2 * (chieu_dai + chieu_rong)

def tinh_dien_tich(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
    for i in range(chieu_rong):
        print('*' * chieu_dai)

if __name__ == '__main__':
    chieu_dai = 5
    chieu_rong = 3
    
    chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
    dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)
    
    print(f"Chu vi hình chữ nhật: {chu_vi}")
    print(f"Diện tích hình chữ nhật: {dien_tich}")
    
    print("Hình chữ nhật:")
    ve_hinh_chu_nhat(chieu_dai, chieu_rong)
