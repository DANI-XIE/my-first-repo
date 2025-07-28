dict1 = {'name':'TOM', 'age': 20, 'gender': '男'}

# 1. [key]
#print(dict1['name']) # Tom
#print(dict1['id'])  # 报错

# 2. 函数

# 2.1 get()
# print(dict1.get('name'))
# print(dict1.get('names'))
# print(dict1.get('name', 'Lily'))

# 2.2 keys() 查找字典中所有的key,返回可迭代对象
# print(dict1.keys())

# 2.3 values() 查找字典中所有的values,返回可迭代对象
# # print(dict1.values())

# 2.4 items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key,元组数据2是字典的keys
print(dict1.items())