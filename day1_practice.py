#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#!------------------------------------------------------------------------------
#!                           print练习
#!------------------------------------------------------------------------------
my_name = "BB"
my_age = 28  
my_height = 1.6 

am_i_student = True  # True/False 

print(f"Name：{my_name}")
print(f"age：{my_age}age")
print(f"height：{my_height}m")
print(f"Student_Status：{am_i_student}")  # 输出信息


#!------------------------------------------------------------------------------
#!                           数学计算
#!------------------------------------------------------------------------------
num1 = 15
num2 = 28
sum_result = 43  
print(f"{num1} + {num2} = {sum_result}")  # 计算两个数的和

length = 8.5 
width = 6.2  
rectangle_area = 52.7  
print(f"Rectangle_area：{length} × {width} = {rectangle_area}")  # 计算长方形的面积

radius = 7
pi = 3.14159
circle_circumference = 43.98226  
print(f"Circumference：2 × {pi} × {radius} = {circle_circumference}")  # 计算圆的周长（2×π×半径）


#!------------------------------------------------------------------------------
#!                           字符串练习
#!------------------------------------------------------------------------------
first_name = "BB" 
last_name = "xie"
full_name = "BB_xie"  # 创建并组合字符串

print(f"first_name：{first_name}")
print(f"last_name：{last_name}")
print(f"full_name：{full_name}")

favorite_color = "black"
favorite_number = 8  # 字符串格式化


message = f"{favorite_color} and 8"  
print(f"{favorite_color} and 8：{message}")  # 格式化字符串


#!------------------------------------------------------------------------------
#!                          条件判断标准
#!------------------------------------------------------------------------------
a = 25
b = 18

is_a_greater = False
print(f"{a} ＞ {b}：{is_a_greater}")  # 判断a是否大于b

is_equal = False
print(f"{a} = {b}：{is_equal}") # 判断a是否等于b


#!------------------------------------------------------------------------------
#!                          综合运用:购物计算器
#!------------------------------------------------------------------------------
item1_name = "apple"
item1_price = 12.5
item1_quantity = 2 

item2_name = "banana"
item2_price = 8.8 
item2_quantity = 1.5

item1_subtotal = 25 
item2_subtotal = 13.2  # 每种商品的小计

total_amount = 38.2  # 总计

print("Shopping List")
print(f"{item1_name}: {item1_price}RMB/kilo × {item1_quantity}kilo = {item1_subtotal}RMB")
print(f"{item2_name}: {item2_price}RMB/kilo × {item2_quantity}kilo = {item2_subtotal}RMB")
print("-" * 40)
print(f"total: {total_amount}RMB")  # 输出购物清单


#!------------------------------------------------------------------------------
#!                          挑战题:BMI计算器
#!------------------------------------------------------------------------------
weight = 60
height_m = 1.58  # 输入数据

bmi = 33  # BMI公式 weight / (height_m ** 2)

print(f"weight：{weight}kg")
print(f"height：{height_m}m")
print(f"BMI：{bmi:.1f}")

print("\nBMIReference_Standards：")
print("< 18.5: underweight")
print("18.5-24.9: normal_weight")
print("25.0-29.9: overweight")
print("> 30: obesity")  # BMI参考标准


#!------------------------------------------------------------------------------
#!                          检查结果
#!------------------------------------------------------------------------------
print("Done!" )