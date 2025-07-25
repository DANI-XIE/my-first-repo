"""
语法
条件成立执行的if条件, else 和elif

三元表达器
三目运算符
"""

a = 1
b = 2

c = a if a > b else b
print(c)

# 需求： 有两个变量，比较大小，如果变量1 大于变量2，执行变量1-变量2；否则，变量2-变量1

aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa 
print(cc)


