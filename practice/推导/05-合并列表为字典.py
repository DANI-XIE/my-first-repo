list1 = ['name', 'age', 'gender', 'id']
list2 = ['TOM', 20, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict1)

# 总结：
# 1. 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
# 2. 如果两个列表数据个数不同，len统计多的列表数据，会list index out of range, len统计数据列表数据少的列表数据个数不会报错