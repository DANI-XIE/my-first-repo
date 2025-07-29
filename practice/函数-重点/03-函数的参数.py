# 1. 函数：固定数据1 和 2 加法
def add_num1():
    result = 1 + 2
    print(result)

add_num1()

# 2.参数形式传入真实数据 做加法运算
# 定义函数同时定义了接收用户数据的参数a和b, a和b是形参
def add_num2(a, b):
    result = a + b 
    print(result)

# 调用函数时传入了真实的数据10和20 真实数据为实参
# 参数的作用，让数据使用更加灵活
add_num2(10, 20)

add_num2(100, 200)

# add_num2(100)  # 报错：定义函数有两个参数，传入数据也要是2个
