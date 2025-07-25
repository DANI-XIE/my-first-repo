"""
步骤
    1.导入模块 import random
    2.用这个模块中的功能  random.randint()
"""

import random

player = input('请出拳:0--石头; 1--剪刀;2--布;') # 玩家出拳

# computer = 1
computer = random.randint(0, 2)
print(computer)

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜，哈哈哈哈')
elif player == computer:
    print('平局，别走，再来一局')
else:
    print('电脑获胜')
