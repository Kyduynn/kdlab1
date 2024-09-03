# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:22:10 2024

@author: Windows
"""

so_xe = int(input("Nhập biển số xe của bạn: "))
chu_so_hang_nghin = so_xe // 1000
chu_so_hang_tram = ( so_xe % 1000 ) // 100
chu_so_hang_chuc = (( so_xe % 1000 ) % 100) // 10
chu_so_hang_don_vi = so_xe % 10
tong_cac_chu_so = chu_so_hang_nghin + chu_so_hang_tram + chu_so_hang_chuc + chu_so_hang_don_vi
a = tong_cac_chu_so // 10
b = tong_cac_chu_so % 10
so_nut = a + b
c = so_nut // 10
d = so_nut % 10
print("Vậy số nút của bạn là: ", c + d)