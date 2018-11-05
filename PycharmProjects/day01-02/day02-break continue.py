#第7个盘子不刷
i = 10
while i > 0:
    if i == 7:
        i -= 1
        continue
    print("刷了第 %-2d 个盘子" % i)
    i -= 1

#第7个及第7个以后都不刷
j = 10
while j > 0:
    if j == 7:
        break
    print("刷了第 %-2d 个盘子" % j)
    j -= 1