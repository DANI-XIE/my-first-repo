# 字典推导式的作用：快速合并列表或提取字典中目标数据。

# 需求：创建一个字典key是1-5的数字，v是这个数字的平方
# dict = {k: v for i in range(1, 5)}
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}