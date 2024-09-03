# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:34:57 2024

@author: Windows
"""

import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b * b - 4 * a * c
if a == 0:
   print("Phương trình có nghiệm duy nhất x=", -b/c)
elif a !=0 and delta < 0:
   print("Phương trình vô nghiệm")
elif a !=0 and delta == 0:
   print("Phương trình có nghiệm kép x1=x2 = ", -b/(2*a))
elif a !=0 and b*b - (4*a*c) > 0:
    print("Phương trình có 2 nghiệm pb x1 =", (-b + math.sqrt(delta))/(2 * a))
    print("Phương trình có 2 nghiệm pb x2 =", (-b - math.sqrt(delta))/(2 * a))
       