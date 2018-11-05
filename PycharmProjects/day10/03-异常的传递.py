def f1():
    print(1/0)


def f2():
    print('f2执行')
    try:
        f1()
    except Exception as exp:
        print('捕捉到异常',exp)
        raise
    print('f2结束')


f2()
