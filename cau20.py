# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:14:05 2024

@author: Windows
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
maxvalue = a
if b > maxvalue :
    maxvalue = b
if c > maxvalue :
    maxvalue = c
    print("Kết quả lớn nhất là: ", maxvalue)