# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:07:15 2024

@author: Windows
"""

a = int(input("Nhập a là: "))
b = int(input("Nhập b là: "))
A = ((a + b) / (pow(a, ( 1 / 3 )) + pow(b, ( 1 / 3 )))) - pow(a * b, (1 / 3))
B = (pow(a, ( 1 / 3)) - pow(b, (1 / 3))) ** 2
print("Kết quả là", A / B)