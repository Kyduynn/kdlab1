# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:07:24 2024

@author: Windows
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
minvalue = a
if b < minvalue :
    minvalue = b
if c < minvalue :
    minvalue = c
if d < minvalue :
    minvalue = d
print("Kết quả nhỏ nhất", minvalue)
