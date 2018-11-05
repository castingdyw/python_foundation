#每个i都要循环9次j
#i控制能输出多少行，j控制一行有多少列
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("j=%d" % j , end=' ')
        j += 1
    print("i=%d" % i)
    i += 1