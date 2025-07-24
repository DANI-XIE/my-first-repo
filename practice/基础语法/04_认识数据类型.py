"""
[summary] 
1.认识数据类型，按经验将不同的变量存储不同的类型的数据
2.验证这些数据到底是什么类型-检测数据-type

Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-23
"""

#!------------------------------------------------------------------------------
#!                           数值类型
#!------------------------------------------------------------------------------

# 数值：int整数、float浮点数、complex复数
# 布尔型： True或False
# str字符串
# list列表
# tuple元组
# dict字典
# set集合

num1 = 42
num2 = 3.14
num3 = -3.5
print(type(num1))  # 输出：<class 'int'>，整数
print(type(num2))  # 输出：<class 'float'>，小数
print(type(num3))  # 输出：<class 'float'>

a = 'hello XIE DA NI'  # 字符串类型，数据都要带引号
print(type(a))  # 输出：<class 'str'>

b = True  # 布尔类型，有两个值：True或False
print(type(b))  # 输出：<class 'bool'>

c = [10, 18, 19, 0, 52] # 集合类型，数据无序且唯一
print(type(c))  # 输出：<class 'list'>，列表

d = (1, 2, 3)  # 元组类型，数据有序且不可变
print(type(d))  # 输出：<class 'tuple'>，元组

e = {34, 56, 78}  # 集合类型，数据无序且唯一
print(type(e))  # 输出：<class 'set'>，集合

f = {'name': 'XIE DA NI', 'age': 28}  # 字典类型，键值对
print(type(f))  # 输出：<class 'dict'>，字典