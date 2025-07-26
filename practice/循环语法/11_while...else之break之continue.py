"""
[summary]
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-26
"""

i = 1
while i <= 3:
    if i == 2:
        break
    print('姐姐我道歉')
    i += 1
else:
    print('弟弟原谅我了, 真开心啊！')


i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print('姐姐我道歉')
    i += 1
else:
    print('弟弟原谅我了, 真开心啊！')