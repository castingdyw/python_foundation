#猜拳游戏：剪刀0，石头1，布2
#玩家输了就再次输入，直到赢了为止

import random

#玩家出拳
player = int(input("请出拳（剪刀0，石头1，布2）："))

#电脑出拳
computer = random.randint(0,2)

#第一把就赢了
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("你赢了")
    print("游戏结束")

#第一把没赢，再次输入，直到赢了为止
else:
    while not ((player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1)):
        player1 = int(input("再次出拳:"))
        computer1 = random.randint(0,2)
        if (player1 == 0 and computer1 == 2) or (player1 == 1 and computer1 == 0) or (player1 == 2 and computer1 == 1):
            print("你赢了")
            break
        elif player1 == computer1:
            print("平局")
            continue
        else:
            print("你输了")
            continue

    print("游戏结束")