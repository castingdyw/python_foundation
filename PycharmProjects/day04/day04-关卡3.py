# 有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现
import random

ball = ['红','红','红','蓝','蓝','蓝','白','白','白','白']

while True:
    box = [[], [], []]
    for i in ball:
        j = random.randint(0,2)
        box[j].append(i)
    if ('白' in box[0]) and ('白' in box[1]) and ('白' in box[2]):
        print(box)
        break
    # else:
    #     continue