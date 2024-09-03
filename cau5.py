# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:43:45 2024

@author: Windows
"""
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
tong_giay= gio * 3600 + phut * 60 + giay
print("Tổng số giây là: ", tong_giay )
