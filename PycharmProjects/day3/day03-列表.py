# 从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字
# 从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生

a = []
for i in range(5):
    b = input('name:')
    a.append(b)
    print(b[1])

import random
c = random.randint(0,4)
print(c)
print(a[c])

