# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:07:45 2024

@author: Windows
"""

can_nang= float(input(" Nhập số cân nặng: "))
chieu_cao= float(input(" Nhập số chiều cao: "))
cong_thuc_bmi= round(can_nang / chieu_cao ** 2, 2)
print(" Vậy số đo sức khoẻ bmi của bạn là: ", cong_thuc_bmi)