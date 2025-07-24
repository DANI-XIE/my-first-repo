#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!------------------------------------------------------------------------------
#!                         列表基础操作
#!------------------------------------------------------------------------------
fruits = ["apple", "banana", "orange", "葡萄", "草莓"]  

print(f"My favorite fruit：{fruits}")
print(f"List length：{len(fruits)}")
print(f"The first fruit：{fruits[0]}")  # 索引从0开始
print(f"The last fruit：{fruits[-1]}")  # 负索引

fruits.append("西瓜")  # 在列表末尾添加一个水果
fruits.insert(0, "芒果")  # 在列表开头插入一个水果

print(f"The final list：{fruits}")

#!------------------------------------------------------------------------------
#!                         列表的增删改查
#!------------------------------------------------------------------------------
scores = [85, 92, 78, 96, 88, 73, 89]  # 学生成绩列表
print(f"原始成绩：{scores}")

max_score = max(scores)  # 找出最高分
min_score = min(scores)  # 找出最低分

print(f"最高分：{max_score}")
print(f"最低分：{min_score}")

average = sum(scores) / len(scores)  # 计算平均分

print(f"平均分：{average:.2f}")

scores.remove(min_score)  # 删除最低分
print(f"删除最低分后：{scores}")  

scores.sort()  # 将所有成绩按升序排列
print(f"排序后：{scores}")

#!------------------------------------------------------------------------------
#!                         元组操作
#!------------------------------------------------------------------------------
person_info = ("张三", 25, "北京", "程序员")  # 创建一个包含个人信息的元组(姓名, 年龄, 城市, 职业)

print(f"个人信息：{person_info}")
print(f"姓名：{person_info[0]}")
print(f"年龄：{person_info[1]}")
print(f"城市：{person_info[2]}")
print(f"职业：{person_info[3]}")

coordinates = [(0, 0), (1, 2), (3, 4), (2, 1), (4, 3)]  # 坐标点元组
print(f"坐标点：{coordinates}")

print("各点到原点的距离：")  # 遍历坐标点，计算每个点到原点的距离
for point in coordinates:
    x, y = point  # 元组解包
    distance = (x**2 + y**2)**0.5  # 计算距离公式
    print(f"点{point}到原点的距离：{distance:.2f}")

#!------------------------------------------------------------------------------
#!                         字典基础操作
#!------------------------------------------------------------------------------
student = {"name": "小明", "age": 20, "major": "计算机", "grade": 85}  # 创建一个学生信息字典

print(f"学生信息：{student}")

student["email"] = "xiaoming@email.com"  # 添加新的键值对
student["age"] = 21  # 修改现有值

print(f"修改后的信息：{student}")

print("字典遍历：")  # 遍历字典
for key, value in student.items():
    print(f"{key}: {value}")

#!------------------------------------------------------------------------------
#!                         字典高级应用 - 词频统计
#!------------------------------------------------------------------------------
text = "python is great python is powerful python is fun"
words = text.split()
print(f"单词列表：{words}")

word_count = {}  # 统计每个单词出现的次数
for word in words:
    if word in word_count:  # 完成词频统计逻辑
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"词频统计：{word_count}")

most_frequent_word = ""  # 找出出现次数最多的单词
max_count = 0
for word, count in word_count.items():  # 遍历word_count找到最大值
    if count > max_count:
        max_count = count
        most_frequent_word = word

print(f"出现最多的单词：'{most_frequent_word}' ({max_count}次)")

#!------------------------------------------------------------------------------
#!                         集合操作
#!------------------------------------------------------------------------------

class_a = {"Alice", "Bob", "Charlie", "David", "Eve"}  # 两个班级的学生名单
class_b = {"Bob", "Diana", "Eve", "Frank", "Grace"}

print(f"A班学生：{class_a}")
print(f"B班学生：{class_b}")

common_students = class_a & class_b  # 找出两班共同的学生
print(f"两班共同学生：{common_students}")

only_in_a = class_a - class_b  # 找出只在A班的学生
print(f"只在A班的学生：{only_in_a}")

all_students = class_a | class_b  # 找出所有学生
print(f"所有学生：{all_students}")
print(f"学生总数：{len(all_students)}")

#!------------------------------------------------------------------------------
#!                         嵌套数据结构
#!------------------------------------------------------------------------------
classroom = {
    "class_name": "Python入门班",
    "teacher": "张老师",
    "students": [
        {"name": "小明", "age": 20, "scores": [85, 92, 78]},
        {"name": "小红", "age": 19, "scores": [90, 88, 95]},
        {"name": "小李", "age": 21, "scores": [82, 79, 88]}
    ]
}

print(f"班级：{classroom['class_name']}")
print(f"老师：{classroom['teacher']}")

print("\n学生成绩统计：")  # 计算每个学生的平均成绩
for student in classroom["students"]:
    name = student["name"]
    scores = student["scores"]
    average = sum(scores) / len(scores)  # 计算平均成绩
    print(f"{name}: 成绩{scores}, 平均分{average:.1f}")

#!------------------------------------------------------------------------------
#!                         列表推导式入门
#!------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始数字：{numbers}")

squares = [x**2 for x in numbers]  # 生成所有数字的平方
print(f"平方数：{squares}")

even_numbers = [x for x in numbers if x % 2 == 0]  # 筛选出偶数
print(f"偶数：{even_numbers}")

even_squares = [x**2 for x in numbers if x % 2 == 0]  # 生成偶数的平方
print(f"偶数的平方：{even_squares}")

#!------------------------------------------------------------------------------
#!                         综合应用 - 学生管理系统
#!------------------------------------------------------------------------------
students_db = []  # 存储所有学生信息的列表

def add_student(name, age, grade):  # 实现添加学生函数
    """添加学生到数据库"""
    student = {"name": name, "age": age, "grade": grade}
    students_db.append(student)
    print(f"已添加学生：{name}")

def find_student(name):  # 实现查找学生函数
    """根据姓名查找学生"""
    for student in students_db:
        if student["name"] == name:
            return student
    return None

add_student("Alice", 20, 85)  # 测试系统
add_student("Bob", 19, 92)
add_student("Charlie", 21, 78)

print(f"\n学生数据库：{students_db}")

found_student = find_student("Alice")  # 查找功能测试
if found_student:
    print(f"找到学生：{found_student}")
else:
    print("未找到学生")

#!------------------------------------------------------------------------------
#!                         挑战题 - 购物车系统
#!------------------------------------------------------------------------------
inventory = {  # 商品库存（字典：商品名 -> [价格, 库存数量]）
    "苹果": [5.0, 100],
    "香蕉": [3.0, 80], 
    "橘子": [4.0, 60],
    "葡萄": [8.0, 40]
}

shopping_cart = {}  # 购物车

print("商品库存：")
for item, (price, stock) in inventory.items():
    print(f"{item}: ¥{price}/个, 库存{stock}个")

def add_to_cart(item_name, quantity):  # 实现购物车功能
    """添加商品到购物车"""
    if item_name not in inventory:
        print(f"商品 {item_name} 不存在")
        return
    
    price, stock = inventory[item_name]
    if quantity > stock:
        print(f"库存不足！{item_name} 只有 {stock} 个")
        return
    
    if item_name in shopping_cart:
        shopping_cart[item_name] += quantity
    else:
        shopping_cart[item_name] = quantity
    
    print(f"已添加 {quantity} 个 {item_name} 到购物车")

def show_cart():
    """显示购物车和总价"""
    if not shopping_cart:
        print("购物车为空")
        return
    
    print("购物车内容：")
    total = 0
    for item, quantity in shopping_cart.items():
        price = inventory[item][0]
        subtotal = price * quantity
        total += subtotal
        print(f"{item}: {quantity}个 × ¥{price} = ¥{subtotal}")
    
    print(f"总计：¥{total:.2f}")

add_to_cart("苹果", 3)  # 测试购物车
add_to_cart("香蕉", 2)
add_to_cart("葡萄", 1)
show_cart()

#!------------------------------------------------------------------------------
#!                         练习完成检查
#!------------------------------------------------------------------------------
print("done!")
