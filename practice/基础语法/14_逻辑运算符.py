"""
[summary] 
逻辑运算符
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-23
"""

#!------------------------------------------------------------------------------
#!                              逻辑运算符
#!------------------------------------------------------------------------------

a = 0
b = 1
c = 2 

print((a < b) and (c > b))  # and:与：都真才真
print((a > b) and (c > b))  

print((a < b) or (c > b))# 一真才真，一假才假
print((a > b) or (c > b))

print(not False)  # 取反义词
print(not (c > b))

