# class Person(object):
#
#     instance = None
#
#     is_first_run = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance == None:
#             cls.instance = object.__new__(cls)
#         return cls.instance
# # 每次返回的都是同一个对象
#
#     def __init__(self, name=''):
#         if Person.is_first_run:
#             self.name = name
#             Person.is_first_run = False
# # 每次返回都是第一次传入的属性（name）
#
#     def set_name(self, new_name):
#          self.name = new_name
# # 想修改属性
#
# zs = Person('zs')
# print(zs.name)
# ls = Person('ls')
# print(ls.name)
# ls.set_name('ls')
# print(ls.name)





class Person(object):
    isinstance = None
    is_first = True
    def __new__(cls, *args, **kwargs):
        if Person.isinstance == None:
            Person.isinstance = object.__new__(cls)
        return Person.isinstance  # 第一次创建对象之后，每次返回的对象都是第一次创建的

    def __init__(self, name):
        if Person.is_first:
            self.name = name
            Person.is_first = False  # 第一次添加名字之后，每次返回的都是第一次的名字

    def set_name(self, new_name):
        self.name = new_name

zs = Person('张三')
print(zs)
print(zs.name)
ls = Person('李四')
print(ls)
print(ls.name)
ls.set_name('李四')
print(ls.name)


