# 定义一个函数. 声明一个变量：函数体内部访问、函数体外面访问
def testA():
    a = 100
    print(a)  # 函数体内部访问，能访问到a变量

testA()
print(a)