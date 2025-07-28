s1 = {10, 20}

# 1. 集合是可变类型
# add()
s1.add(100)
print(s1)

# 集合有去重功能
s1.add(100)
print(s1)

s1.add([10, 20, 30, 100])  # 报错
print(s1)
# update()