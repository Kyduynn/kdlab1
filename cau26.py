# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:56:38 2024

@author: Windows
"""

a = int(input("Nhập a là: "))
b = int(input("Nhập b là: "))
c = int(input("Nhập c là: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    
    N = int(input("nhập số nguyên N"))
    danh_sach = list(N)
    sap_xep = danh_sach.sort()
    sap_xep_danh_sach = "".join(danh_sach)
    print(sap_xep_danh_sach)