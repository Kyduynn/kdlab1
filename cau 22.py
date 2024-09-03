# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:31:19 2024

@author: Windows
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a == 0 and b == 0:
    print("pt có vô số nghiệm")
elif a == 0 and b !=0:
    print("pt vô nghiệm")
else:
    print("pt có nghiệm x=", -b/a)