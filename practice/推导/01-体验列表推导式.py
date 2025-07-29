# 作用：永一个表达式创建一个有规律的列表或控制一个有规律的列表。

# 需求：0，2，2，4
# 1.循环实现；2.列表推导式（化简代码：创建或控制有规律的列表）

""" 
1.1 创建空列表
1.2 循环将有归来吧的数据写入到列表
"""

# # while 循环实现
# list1 = []

# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1

# print(list1)


# for 循环实现
# list1 = []
# for i in range(10):
#     list1.append(i)

# print(list1)


# 列表推导 实现
# 作用：创建规律性的数据列表，一行实现代码输出
list1 = [i for i in range(10)]
print(list1)
