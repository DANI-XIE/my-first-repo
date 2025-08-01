# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5]

# 2. 准备2次方计算的函数
def func(x):
    return x ** 2

# 3. 调用map
result = map(func, list1)

# 4. 参数验收
print(result)  # <map object at 0x0000001376793748>
print(list(result))  # [1, 4, 9, 16, 25]