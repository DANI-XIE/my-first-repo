# 需求：0-10的偶数数据列表

# 1. 简单列表推导式range步长
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 2. for循环加if，创建规律列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

# 3. 把for循环配合if代码，改写带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
