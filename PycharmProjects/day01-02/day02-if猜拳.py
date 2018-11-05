#猜拳游戏：剪刀，石头，布

import random
'''

#玩家出拳
player = int(input("请出拳（剪刀0，石头1，布2）："))


#电脑出拳
computer = random.randint(0,3)

#判断结果
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("你赢了")

elif player == computer:
    print("平局")

else:
    print("你输了")
    
print("游戏结束")
'''
a = int(input("出拳剪刀0石头1布2："))
b = random.randint(0,2)

if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    print("你赢了")
elif a == b:
    print("平局")
else:
    print("你输了")

