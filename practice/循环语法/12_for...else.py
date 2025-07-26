"""
[summary]
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-26
"""

str1 = 'iloveyou'
for i in str1:
    if i == 'e':
        #break
        continue
    print(i)
else:
    print('循环正常结束执行')