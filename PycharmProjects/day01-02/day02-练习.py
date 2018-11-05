'''
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print("hello world")
    i += 1
'''
# a = int(input("1-7:"))
# if a == 6 or a == 7:
#     print("周末")
# elif a in range(1,6):
#     print("工作日")
# else:
#     print("error")

#简易计算器
# a = int(input("num1:"))
# b = input("+-*/:")
# c = int(input("num2:"))
# if b == "+":
#     print(a + c)
# elif b == "-":
#     print(a - c)
# elif b == '*':
#     print(a * c)
# elif b == '/' and c != 0:
#     print(a / c)
# else:
#     print('error')

#for循环打印乘法表
# for i in range(1,9):
#     for j in range(1,9):
#         print("%d*%d=%d" % (j,i,j*i), end=" ")
#         if j == i:
#             break
#     print()

# 让用户输入银行卡的余额
# 让用户输入要付款的金额
# 使用三元运算符判断银行卡余额是否足够付款，并将结果赋值给一个变量
# 如果足够则'使用银行卡付款'，否则为'余额不足'
# 打印变量
# a = eval(input("银行卡余额："))
# b = eval(input("要付款金额："))
# c = 1 if a >= b else 0
# if c == 1:
#     print("使用银行卡付款")
#     print("付款后余额：%f" % (a - b))
# else:
#     print("余额不足")
#     print("还差金额：%f" % (b - a))

#设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字
# i = 1
# s = 1
# while i <= 100:
#     if i % 7 != 0:
#         #print(i,s)
#         i += 1
#         s += 1
#     else:
#         print(i,end=' ')
#         i += 1

#两个三角形
# i1 = 1
# while i1 <= 5:
#     j1 = 1
#     while j1 <= i1:
#         print('*',end=' ')
#         j1 += 1
#     print()
#     i1 += 1
# i = 4
# while i >= 1:
#     j = 1
#     while j <= i:
#         print('*',end=' ')
#         j += 1
#     print()
#     i -= 1


i = 1
while i <= 9:
    if i <= 5:
        j = 1
        while j <= i:
            print('*',end=' ')
            j += 1
    else:
        j = 1
        while j <= 9-i+1:
            print('*',end=' ')
            j += 1
    print()
    i += 1

