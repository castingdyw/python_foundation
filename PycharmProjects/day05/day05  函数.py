# 定义两个函数，分别实现任意个数之间的累加、累减操作。如实参为 1,2,3,4,5，累加即是1+2+3+4+5
# def add1(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(args)
#     print(s)
#
# ls = [1,2,3,4,5,6]
# add1(*ls)

# def sub(*args):
#     s = args[0]
#     for i in args[1:]:
#         s -= i
#     print(args)
#     print(s)
# ls = [1,2,3,4]
# sub(*ls)

# 使用不定长参数定义一个函数 max_min，接受的参数类型是任意个数值，最终返回这些数中的最大值
# def max1(*args):
#     a = max(args)
#     print(args)
#     print(a)
# max1(1,2,3,4,5,9,3)

# 定义一个函数
# 接收参数 n 和 command
# command 为 True 则返回0-n(包含n)以内的偶数组成的列表
# command 为 False 则返回0-n(包含n)以内的奇数组成的列表
# 默认返回全是奇数的列表
def num(n, command = False):
    if command == True:
        oushu = []
        for i in range(1,n+1):
            if i % 2 == 0:
                oushu.append(i)
        return oushu
    else:
        jishu = []
        for i in range(1,n+1):
            if i % 2 != 0:
                jishu.append(i)
        return jishu

a=num(9,True)
print(a)