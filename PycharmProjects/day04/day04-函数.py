# def add(a, b):
#     """两个数相加"""
#     c = a + b
#     print(c)
#     return c
#
# add(11,22)
# print(add(11,22))



# 写一个程序，由用户输入一个年份，调用函数判断是否是闰年。
# 年份作为参数传递给函数
# 函数需要有返回值

# time1 = int(input('请输入年：'))
# def time(a):
#     if a % 4 == 0:
#         print('闰年')
#     else:
#         print('不是闰年')
# time(time1)


# 编写一段代码，让用户输入两个数字，求两个数之间所有整数的和，并打印。
# 比如用户输入2和4，则计算 2+3+4 的结果。
# a = int(input('输入第一个数字：'))
# b = int(input('输入第二个数字：'))
#for循环
# def sum(a,b):
#     if a > b:
#         s = 0
#         for i in range(b,a+1):
#             s =  s + i
#         print(s)
#         return s
#     elif a < b:
#         s = 0
#         for i in range(a,b+1):
#             s =  s + i
#         print(s)
#         return s
#     else:
#         s = a + b
#         print(s)
#         return s
#while循环
# def sum(a,b):
#     if a > b:
#         i = b
#         s = 0
#         while i <= a:
#             s = s + i
#             i += 1
#         print(s)
#     elif a < b:
#         i = a
#         s = 0
#         while i <= b:
#             s = s + i
#             i += 1
#         print(s)
#     else:
#         s = a + b
#         print(s)
# sum(a,b)

# 编写函数打印一条横线
# 编写有参数的函数，形参接收数字 num，函数里打印 num 条横线。打印横线的代码使用上一步的函数处理
# def line():
#     print('-'*50)
# line()
#
# def many(a):
#     i = 0
#     while i < a:
#         line()
#         i += 1
#
# many(5)

# 编写有参数的函数，形参接收数字 a、b、c，函数里计算三个数字之和，并返回
# 编写有参数的函数，形参接收数字 a、b、c，函数里计算三个数字的平均值。计算三个数之和的代码使用上一步的函数处理。
def sum(a,b,c):
    s = a + b +c
    return s
def avg(a,b,c):
    ss = sum(a,b,c)
    mean = ss / 3
    return mean

d = avg(3,3,3)
print(int(d))



