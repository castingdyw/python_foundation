#先分析九九乘法表第一个数代表列，第二个数代表行，当列=行时停
#while嵌套中，每个外循环对应全部内循环，内循环对应一行中全部列

#方法1
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j,i,j*i),end=' ')
        j += 1
    print()
    i += 1
#方法2
i1 = 1
while i1 <= 9:
    j1 = 1
    while j1 <= 9:
        if j1 == i1+1:
            break
        print("%d*%d=%d" % (j1,i1,j1*i1),end=' ')
        j1 += 1
    print()
    i1 += 1
#方法三：for循环
for i2 in range(1,10):
    for j2 in range(1,10):
        print("%d*%d=%d" % (j2,i2,j2*i2),end=' ')
        if j2 == i2:
            break
    print()