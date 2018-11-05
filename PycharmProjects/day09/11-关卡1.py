# class Car(object):
#     addr = "China"
#
#     def __init__(self):
#         self.name = 'changcheng'
#         self.money = 100000
# # 如果要修改类属性该怎么做? 如果要修改实例属性该怎么做?
# car = Car()
# print(car.name)
# print(Car.addr)

# class Car(object):
#     addr = "China"
#
#     def __init__(self):
#         self.name = 'changcheng'
#         self.money = 100000
#         Car.addr = 'English'
#
#     def get_addr(self):
#         return Car.addr
#
# car = Car()
# print(Car.addr)


# 定义类方法的格式是什么？对于类方法的参数有什么要求? 调用类方法的格式是什么?
# class Person(object):
#     __n = 1
#     def eat(self):
#         print('能吃')
#
#     @classmethod
#     def get_n(cls):
#         return cls.__n
#
# p = Person()
# print(Person.get_n(p))
# print(Person.get_n())  # 调用


# 定义静态方法的格式是什么? 对于静态方法的参数有什么要求?调用静态方法的格式是什么?
class Person(object):
    @staticmethod
    def add(a, b):
        return a + b
p = Person()
res = p.add(1,5)
print(res)

