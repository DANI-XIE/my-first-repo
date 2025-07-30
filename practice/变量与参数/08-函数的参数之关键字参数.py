def user_info(name, age, gender):
    print(f'您的名字{name}, 年龄是{age}, 性别是{gender}')

# 调用函数传参
user_info('ROSE', age=20, gender='女')
user_info('达尼', gender='女', age=20)  # 关键字参数之技安不分先后顺序
# 位置参数必须写在关键字参数的前面
# user_info(age=20, gender='男', 'TOM')