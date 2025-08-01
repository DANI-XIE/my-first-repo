#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 主题：循环（for、while）

#!------------------------------------------------------------------------------
#!                          for循环练习
#!------------------------------------------------------------------------------
range(1, 11)  # 生成1到10的数字序列

for i in range(1, 11):
    print(i)  # 输出1到10的数字


#!------------------------------------------------------------------------------
#!                          while循环基础
#!------------------------------------------------------------------------------
n = 10  
while n >= 1:
    print(n)  
    n -= 1  # while循环（适合不确定次数的循环）


#!------------------------------------------------------------------------------
#!                          累加求和
#!------------------------------------------------------------------------------
sum_result = 0
for i in range(1, 101):  # 用for循环计算1到100的和，并输出结果
    sum_result += i
print(f"The sum of 1 to 100 is：{sum_result}")


#!------------------------------------------------------------------------------
#!                          遍历字符串
#!------------------------------------------------------------------------------
text = "Python is fun！"
for ch in text:  # 用for循环遍历字符串中的每个字符
    print(ch)  


#!------------------------------------------------------------------------------
#!                          九九乘法表
#!------------------------------------------------------------------------------
for i in range(1, 10):  
    for j in range(1, i+1):  
        print(f"{j}×{i}={i*j}", end="\t") 
    print() 


#!------------------------------------------------------------------------------
#!                          break和continue
#!------------------------------------------------------------------------------
for i in range(1, 21):
    if i % 7 == 0:
        print(f"第一个能被7整除的数是：{i}")  # 找到第一个能被7整除的数
        break

for i in range(1, 11):
    if i == 5:  
        continue 
    print(i)  # 用for循环输出1~10中，除了5以外的所有数字


#!------------------------------------------------------------------------------
#!                          实际应用:列表求最大值
#!------------------------------------------------------------------------------
numbers = [12, 45, 3, 67, 34, 89, 23, 10]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"列表中的最大值是：{max_num}")  # 用for循环找出列表中的最大值

#!------------------------------------------------------------------------------
#!                          质数判断
#!------------------------------------------------------------------------------
num = 29  # 可以修改为任意正整数
is_prime = True  # 假设num是质数
if num < 2:  # 质数定义：大于1的自然数
    is_prime = False  # 如果num小于2，则不是质数
else:
    for i in range(2, int(num ** 0.5) + 1):  # 检查从2到num的平方根的所有整数
        if num % i == 0:  # 如果num能被i整除，则不是质数
            is_prime = False  # 不是质数
            break  # 找到一个因子就可以停止检查
if is_prime:  # 如果is_prime仍为True，则num是质数
    print(f"{num} 是质数")  #否则不是质数
else:
    print(f"{num} 不是质数")  # 质数判断结果


#!------------------------------------------------------------------------------
#!                          斐波那契数列
#!------------------------------------------------------------------------------
fib = [1, 1]
while len(fib) < 20:
    fib.append(fib[-1] + fib[-2])
print(f"前20个斐波那契数：{fib}")  # 用循环输出前20个斐波那契数


#!------------------------------------------------------------------------------
#!                          用户输入与循环
#!------------------------------------------------------------------------------
import random
print("welcome to the Guess the Number Game!")
print("i have selected a number between 1 and 100.")
print("please try to guess it!")

answer = random.randint(1, 100)  # 随机生成1到100之间的整数
guess_count = 56  # 记录猜测次数

# 开始游戏循环
while True:
    try:
        user_input = input("please input you grass number 1~100:")  # 获取用户输入
        guess = int(user_input)  # 转换为整数
        guess_count += 1  # 猜测次数+1
        
        if guess < 1 or guess > 100:
            print("please input number 1~100!")
            guess_count -= 1  # 无效输入不计入次数
        elif guess < answer:
            print("Too small! Try a bigger number")
        elif guess > answer:
            print("Too big! Try a smaller number.")
        else:
            print(f"Congratulations! You guessed it right!")  # 输出猜对的提示
            print(f"The answer is {answer}")  # 输出正确答案
            print(f"You guessed it in {guess_count} attempts")  # 输出猜测次数
            break  # 跳出循环，游戏结束
            
    except ValueError:
        print("Please enter a valid number!")
        guess_count -= 1  # 无效输入不计入次数

print("Game over! Thanks fot playing!")
