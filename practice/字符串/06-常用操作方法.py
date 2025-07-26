# 所谓的字符串查找方法即是查找穿在字符串中的位置或出现的次数


# find() 检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1
# index()
# count() 返回某个子串符出现的次数

# 语法：
# 字符串序列find(子串，开始位置下标，结束位置下标)

mystr = "hello world and itcast and itcast and python"

# find()
print(mystr.find('and'))  #12
print(mystr.find('and', 15, 30))  #12
print(mystr.find('ands'))  #-1, ands子串不存在

# index()
print(mystr.index('and'))  #12
print(mystr.index('and', 15, 30))  #23
print(mystr.index('and'))  # 如果index查找子串不存在，报错