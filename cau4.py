# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:39:03 2024

@author: Windows
"""

n=int(input(" Nhập số nguyên dương n có 2 chữ số: "))
chu_so_hang_chuc= n//10
chu_so_hang_don_vi= n%10
tong_cac_chu_so_cua_n= chu_so_hang_chuc + chu_so_hang_don_vi
if 10 <=n<=99:
    print("Tổng các chữ số của n là: ", tong_cac_chu_so_cua_n)
else:
    print("Nhập lại số nguyên có hai chữ số!")
    





