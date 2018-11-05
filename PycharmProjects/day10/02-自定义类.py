# 编写代码，自定义一个异常类，如果两个数相除，余数不为零则抛出自定义异常。
class MyError(Exception):
    def __str__(self):
        return '余数不为0'


a = eval(input('请输入数字'))
b = eval(input('请输入数字'))
if a % b != 0:
    raise MyError()