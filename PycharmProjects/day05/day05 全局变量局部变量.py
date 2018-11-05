# 使用全局变量处理函数间共享数据，在 funcA 函数修改全局变量，在 funcB 函数打印全局变量的值
# 使用传参处理函数间共享数据，在 funcA 返回一个数字，并把返回值作为实参传递给 funcB，在 funcB 打印接收的值
# 使用函数嵌套处理函数间共享数据，在 funcA 返回一个数字，在 funcB 调用 funcA 获取返回值并打印

#全局变量
def funcA():
    global a
    a = 99
    print('funcA',a)

def funcB():
    print('funcB',a)
a=100
funcB()
funcA()
funcB()

#函数传参
# def funcA():
#     a = 112
#     return a
# def funcB(t):
#     print('funcB',t)
# q = funcA()
# funcB(q)

#函数嵌套
# def funcA():
#     a = 99
#     return a
# def funcB():
#     t = funcA()
#     print('funcB',t)
# funcB()
