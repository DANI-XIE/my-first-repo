"""
[summary] 
数据类型转化为函数
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-23
"""

#!------------------------------------------------------------------------------
#!                              数据类型转化为函数
#!------------------------------------------------------------------------------
num1 = 1
str1 = '10'
print(type(float(num1)))  # 输出num1类型，应该是整数类型
print(float(num1))  # 将整数转换为浮点数

print(float(str1)) # 将字符串转换为浮点数

print(type(str(num1)))

list1 = [10, 20, 30]
print(tuple(list1))  # 将列表转换为元组

t1 = (100, 200, 300)  
print(list(t1))

str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'

print(type(eval(str2)))
print(type(eval(str3))) 
print(type(eval(str4))) 
print(type(eval(str5)))  