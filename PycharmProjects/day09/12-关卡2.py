# 1. 使用多态实现下面的需求
# 	* 提供 军犬、缉毒犬、人 的类
# 	* 人能通过一个方法和所有的小狗互动
# class Dogs(object):
#     def work(self):
#         pass
# class Army_dog(Dogs):
#     def work(self):
#         print('军犬能攻击')
# class Track_dog(Dogs):
#     def work(self):
#         print('缉毒犬能缉毒')
# class Person(object):
#     def work_dog(self, dog):
#         dog.work()
# p = Person()
# a_dog = Army_dog()
# t_dog = Track_dog()
# p.work_dog(a_dog)
# p.work_dog(t_dog)

# 定义一个类，自动记录这个类创建的实例对象个数。(使用类属性处理。)
# class Person(object):
#     n = 0
#     def __init__(self):
#         Person.n += 1
#     @classmethod
#     def get_n(cls):
#         print('创建了%d个对象' % cls.n)
# zs = Person()
# ls = Person()
#
# # Person.get_n()
# print(Person.n)

# 任意定义一个类，练习类方法和静态方法的定义和调用
# class Person(object):
#     n = 0
#     def __init__(self):
#         Person.n += 1
#     @classmethod
#     def get_n(cls):
#         print('创建了%d个对象' % cls.n)
#     @staticmethod
#     def add(a, b):
#         print(a + b)
# p = Person()
# Person.get_n()
# p.add(5,6)

# 实现一个简单的单例模式代码。保证这个类只能创建一个对象。
class Person(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if Person.instance == None:
            Person.instance = object.__new__(cls)
        return Person.instance

zs = Person()
print(zs)
ls = Person()
print(ls)