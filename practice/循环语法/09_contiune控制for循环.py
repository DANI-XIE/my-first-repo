"""
[summary]
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-26
"""

str1 = 'iloveyou'
for i in str1:
    # 当某些条件成立退出循环→break：条件i取到字符e
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)

# break和continue在for/while循环语句里用法一样的

