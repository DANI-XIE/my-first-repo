# 定义一个函数后，程序员如何书写程序能够快速提示这个函数的作用？
#help(len) # help函数作用：查看函数的说明文档(函数的解释说明的)

# 语法
# 定义函数的说明文档
# def 函数名(参数):
#     """ 
#     说明文档的位置
#     """
#     代码

def sum_num(a, b):
    """求和函数"""
    return a + b

help(sum_num)

# 函数说明文档的高级使用
def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b

help(sum_num1)