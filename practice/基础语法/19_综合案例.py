"""
[summary] 
猜拳游戏
Author: XIE DA NI (xiedani@poweroak.net)
Created: 2025-07-23
"""

#!------------------------------------------------------------------------------
#!                            猜拳游戏
#!------------------------------------------------------------------------------  

"""
1.出拳。玩家:手动输入; 玩家:①固定剪刀; ②随机;
2.判断输赢。
    2.1玩家获胜
    2.2平局
    2.3电脑获胜
    """
player = input('请出拳:0--石头; 1--剪刀;2--布;') # 玩家出拳
computer = 1

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜，哈哈哈哈')
elif player == computer:
    print('平局，别走，再来一局')
else:
    print('电脑获胜')
