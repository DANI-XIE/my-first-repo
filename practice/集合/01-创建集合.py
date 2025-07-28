# 创建集合使用{}或set(), 但如果要创建空集合只能使用set(), 因为{}用来创建空字典。

# 1.创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 20, 30, 40, 50, 10, 30, 20}
print(s2)

s3 = set('abcdefg')
print(s3)

# 2. 创建无数据的空集合

s4 = set()
print(s4)
print(type(s4))

s5 = {}
print(s5)
print(type(s5))