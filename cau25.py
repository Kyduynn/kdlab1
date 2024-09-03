# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:52:20 2024

@author: Windows
"""

chucai = input("Nhập chữ cái bất kì:")
if chucai.islower():
    chucai = chucai.upper()
elif chucai.isupper ():
    chucai = chucai.lower()
else:
    print("Đây không phải là chữ cái hợp lệ!")
print("Hợp lệ!", chucai)