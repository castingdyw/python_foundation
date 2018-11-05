try:
    print('try----start')
    # print(a)
    # print(1/0)
    print('try----end')
except (NameError,ZeroDivisionError) as exp:
    print('111111111执行')
    print('捕获异常:%s' % exp)
except Exception as exp:
    print('22222执行')
    print('捕获异常:%s' % exp)
else:
    print('没有异常会执行')
finally:
    print('怎么都会执行')
