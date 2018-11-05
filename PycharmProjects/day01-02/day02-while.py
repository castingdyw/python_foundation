#基本while
i = 1
while i <= 5:
    print("正在输出第 %d 个数" % i)
    i += 1

#1-100累计和
j = 1
sum = 0
while j <= 100:
    sum += j
    print(j,sum)
    j += 1

#1-100偶数累计和
#方法1
j1 = 2
sum1 = 0
while j1 <= 100:
    sum1 += j1
    j1 += 2
print(sum1)

#方法2
j2 = 1
sum2 = 0
while j2 <= 100:
    if j2 % 2 == 0:
        sum2 += j2
    j2 += 1
print(sum2)