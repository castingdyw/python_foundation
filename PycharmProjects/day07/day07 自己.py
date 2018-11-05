# 创建类
# 实例方法
#
# 实例化对象
# 调用实例方法
#
# 添加属性
# __init__ 实例化对象自动执行    传参
# __str__  print(对象)
# __del__  删除对象自动调用



class Cat:
    def __init__(self, name, age):
        print('init被执行了')
        self.name = name
        self.age = age
    def __str__(self):
        return 'str被执行了'
    def __del__(self):
        print('del被执行了')

bai = Cat('xiaobai', 12)
print('='*10)
print(bai)
print('o'*10)
a = bai
del bai
print('u'*10)
del a
print('='*10)
