# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:03:50 2024

@author: Windows
"""

import math
nhap = input("Nhập hình: ")
"n" == "Hình chữ nhật"
"v" == "Hình vuông"
"t" == "Hình tròn"
if nhap == "n":
    print("Tính P và S của Hình chữ nhật: ")
    a = int(input("Nhập chiều rộng = "))
    b = int(input("Nhập chiều dài = "))
    P = (a + b) * 2
    S = a * b
    print(f"Kết quả {P} {S} ")
elif nhap == "v":
    print("Tính P và S của Hình vuông: ")
    a = int(input("Nhập độ dài của cạnh = "))
    P = a * 4
    S = pow(a, 2)
    print(f"Kết quả {P} {S} ")
else:
    print("Tính P và S của Hình tròn: ")
    r = int(input("Nhập bán kính của đường tròn = "))
    P = round(2 * math.pi * r, 2)
    S = round(pow(r, 2) * math.pi, 2)
    print(f"Kết quả {P} {S}")