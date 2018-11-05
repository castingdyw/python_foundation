# 1、在下一行打印的内容中写出Python中常用的数据类型
print("Python中常用的数据类型有：int, float, True, False, 字符串， 列表， 元组， 字典， 集合                ")

# 2、编写函数求三个数的平均值，并调用函数，打印出结果
def sum(a,b,c):
    s = a+b+c
    return s
def avr(a,b,c):
    sum1 = sum(a,b,c)
    mean = sum1 / 3
    return mean
res = avr(2,3,4)
print('三个数平均值是%d' % res)

# 3、打印出100以内不包含7的倍数以及数字7的其他整数(例如不能包含7、14、17、21、27...71、72...)
s = []
for i in range(1,100):
    if i % 7 != 0:
        if '7' not in str(i):
            s.append(i)

print(s)



# 4、使用while循环输出下图图形(注意行数)
"""
*
**
***
****
"""
for i in range(1,5):
    for j in range(0,5):
        if i == j:
            break
        else:
            print('*',end='')
    print()


# 5、让用户输入两个数字，求两个数字之间(包括两个数)所有偶数的和(注意是偶数)
n1 = int(input('请输入第一个数字：'))
n2 = int(input('请输入第二个数字：'))
s = 0
if n1 > n2:
    for i in range(n2,n1+1):
        if i % 2 == 0:
            s += i
    print('两个数之间所有偶数和--%d' % s)
elif n1 < n2:
    for i in range(n1,n2+1):
        if i % 2 == 0:
            s += i
    print('两个数之间所有偶数和--%d' % s)
else:
    if n1 % 2 == 0:
        s = n1 *2
    print('两个数之间所有偶数和--%d' % s)


